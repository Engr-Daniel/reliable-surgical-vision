import numpy as np
import pytest
from sklearn.metrics import roc_auc_score

from src.evaluation.bootstrap import cluster_bootstrap, holm
from src.evaluation.crossfit import CHOLEC80_TEST, procedure_folds, assert_disjoint
from src.evaluation.metrics import (SortedScores, aurc, auroc, brier, ece, nll, sustained_events,
                                    transition_mask)
from src.uncertainty.conformal import MondrianConformal, SplitConformal, coverage, merge_small_strata


def test_auroc_matches_sklearn_with_ties():
    rng = np.random.default_rng(0)
    s = np.round(rng.normal(size=2000), 1)
    y = rng.random(2000) < 1 / (1 + np.exp(-2 * s))
    assert auroc(s, y) == pytest.approx(roc_auc_score(y, s), abs=1e-12)


def test_weighted_auroc_equals_replication():
    rng = np.random.default_rng(1)
    g = np.repeat(np.arange(10), 50)
    s = rng.normal(size=500)
    y = rng.random(500) < 0.3
    w = rng.integers(0, 3, 10).astype(float)
    rep = np.repeat(np.arange(500), w[g].astype(int))
    assert SortedScores(s, y, g).auroc(w) == pytest.approx(roc_auc_score(y[rep], s[rep]), abs=1e-9)


def test_aurc_perfect_and_random():
    err = np.r_[np.zeros(80), np.ones(20)]
    perfect = aurc(-err, err)
    rng = np.random.default_rng(2)
    random = np.mean([aurc(rng.random(100), err) for _ in range(200)])
    assert perfect < random
    assert random == pytest.approx(0.2, abs=0.03)


def test_calibration_metrics():
    rng = np.random.default_rng(3)
    p = rng.dirichlet(np.ones(7), 5000)
    y = np.array([rng.choice(7, p=pi) for pi in p])  # perfectly calibrated by construction
    assert ece(p, y) < 0.03
    assert nll(p, y) > 0 and 0 < brier(p, y) < 2


def test_events_and_transitions():
    f = np.array([0, 1, 1, 0, 1, 1, 1, 0], bool)
    assert sustained_events(f, 2) == [(1, 3), (4, 7)]
    assert sustained_events(f, 3) == [(4, 7)]
    m = transition_mask(np.array([0, 0, 0, 1, 1, 1]), 1)
    assert m.tolist() == [False, False, True, True, False, False]


def test_cluster_bootstrap_ci_covers_truth():
    rng = np.random.default_rng(4)
    hits = 0
    for rep in range(40):
        u = rng.normal(0, 1, 30)              # cluster effects
        x = (u[:, None] + rng.normal(0, 1, (30, 20)))  # true mean 0
        def stat(w):
            return float(np.sum(w[:, None] * x) / (w.sum() * 20))
        r = cluster_bootstrap(stat, 30, n_boot=400, seed=rep)
        hits += r.lo <= 0 <= r.hi
    assert hits >= 33  # ~95% nominal; generous lower bound for 40 reps


def test_bands():
    from src.evaluation.bootstrap import BootResult
    b = lambda lo, hi: BootResult(0, lo, hi, 0, np.zeros(1), "bca").band(0.02)
    assert b(0.025, 0.05) == "practically relevant gain"
    assert b(0.005, 0.04) == "detectable gain; practical relevance not established"
    assert b(-0.01, 0.015) == "any gain is below the practical margin"
    assert b(-0.01, 0.05) == "no detectable gain"


def test_holm():
    assert holm({"H1a": 0.01, "H1b": 0.04}) == {"H1a": True, "H1b": True}
    assert holm({"H1a": 0.03, "H1b": 0.04}) == {"H1a": False, "H1b": False}


def _synthetic_phase(n, rng, sharp=2.0):
    logits = rng.normal(size=(n, 7)) * sharp
    p = np.exp(logits) / np.exp(logits).sum(1, keepdims=True)
    y = np.array([rng.choice(7, p=pi) for pi in p])
    return p, y


@pytest.mark.parametrize("lam", [0.0, 0.01])
def test_split_conformal_coverage(lam):
    rng = np.random.default_rng(5)
    p, y = _synthetic_phase(8000, rng)
    cp = SplitConformal(alpha=0.1, lam=lam, k_reg=1, seed=1).fit(p[:4000], y[:4000])
    assert coverage(cp.predict(p[4000:]), y[4000:]) == pytest.approx(0.90, abs=0.02)


def test_mondrian_restores_per_stratum_coverage():
    rng = np.random.default_rng(6)
    p_good, y_good = _synthetic_phase(6000, rng, sharp=3.0)
    # degraded stratum: model probabilities overconfident relative to labels
    p_bad, _ = _synthetic_phase(6000, rng, sharp=3.0)
    y_bad = rng.integers(0, 7, 6000)
    p = np.vstack([p_good, p_bad]); y = np.r_[y_good, y_bad]; s = np.r_[np.zeros(6000, int), np.ones(6000, int)]
    idx = rng.permutation(12000); cal, te = idx[:6000], idx[6000:]
    glob = SplitConformal(0.1, seed=2).fit(p[cal], y[cal]).predict(p[te])
    mond = MondrianConformal(0.1, seed=2).fit(p[cal], y[cal], s[cal]).predict(p[te], s[te])
    good = s[te] == 0
    assert coverage(glob[good], y[te][good]) > 0.93 and coverage(glob[~good], y[te][~good]) < 0.87
    for m in (good, ~good):
        assert coverage(mond[m], y[te][m]) == pytest.approx(0.90, abs=0.025)


def test_merge_small_strata():
    s = np.r_[np.zeros(2000, int), np.ones(100, int), np.full(2000, 2)]
    g = np.arange(len(s)) % 8
    merged = merge_small_strata(s, g)
    assert set(np.unique(merged)) == {0, 2}


def test_folds_deterministic_and_balanced():
    f1, f2 = procedure_folds(CHOLEC80_TEST), procedure_folds(CHOLEC80_TEST)
    assert f1 == f2
    assert sorted(np.bincount(list(f1.values()))) == [8, 8, 8, 8, 8]
    with pytest.raises(AssertionError):
        assert_disjoint([41, 42], [42, 43])
