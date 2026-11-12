"""Split conformal prediction sets for phase classification (preregistration v1.1 §7.2).

APS (adaptive prediction sets) and RAPS (regularised APS), with randomisation for exact
marginal coverage, plus Mondrian (stratum-conditional) calibration where the stratum is a
deployment-observable quantity (binned receiver telemetry), never the impairment tier label.
"""
from __future__ import annotations

import numpy as np


def _sorted(prob):
    order = np.argsort(-prob, axis=1, kind="mergesort")
    sp = np.take_along_axis(prob, order, axis=1)
    return order, sp


def aps_scores(prob: np.ndarray, label: np.ndarray, rng: np.random.Generator,
               lam: float = 0.0, k_reg: int = 0) -> np.ndarray:
    """Non-conformity of the true label (RAPS if lam > 0)."""
    order, sp = _sorted(prob)
    rank = np.argmax(order == label[:, None], axis=1)  # 0-based position of true label
    cum = np.cumsum(sp, axis=1)
    before = np.where(rank > 0, cum[np.arange(len(label)), np.maximum(rank - 1, 0)], 0.0)
    true_p = sp[np.arange(len(label)), rank]
    u = rng.random(len(label))
    score = before + u * true_p
    if lam > 0:
        score = score + lam * np.maximum(rank + 1 - k_reg, 0)
    return score


def conformal_quantile(scores: np.ndarray, alpha: float) -> float:
    n = len(scores)
    if n == 0:
        return np.inf
    k = int(np.ceil((n + 1) * (1 - alpha)))
    if k > n:
        return np.inf
    return float(np.sort(scores)[k - 1])


def prediction_sets(prob: np.ndarray, qhat: np.ndarray | float, rng: np.random.Generator,
                    lam: float = 0.0, k_reg: int = 0) -> np.ndarray:
    """Boolean (n, K) membership matrix. ``qhat`` may be per-sample (Mondrian)."""
    n, K = prob.shape
    order, sp = _sorted(prob)
    cum = np.cumsum(sp, axis=1)
    before = cum - sp
    u = rng.random((n, 1))
    ranks = np.arange(K)[None, :]
    score = before + u * sp + (lam * np.maximum(ranks + 1 - k_reg, 0) if lam > 0 else 0.0)
    q = np.asarray(qhat, float)
    q = q.reshape(-1, 1) if q.ndim else np.full((n, 1), float(q))
    include_sorted = score <= q  # randomised APS: empty sets are allowed and keep exact coverage
    member = np.zeros((n, K), bool)
    np.put_along_axis(member, order, include_sorted, axis=1)
    return member


class SplitConformal:
    def __init__(self, alpha: float = 0.10, lam: float = 0.0, k_reg: int = 0, seed: int = 0):
        self.alpha, self.lam, self.k_reg = alpha, lam, k_reg
        self.rng = np.random.default_rng(seed)
        self.qhat = None

    def fit(self, prob, label):
        self.qhat = conformal_quantile(aps_scores(prob, label, self.rng, self.lam, self.k_reg), self.alpha)
        return self

    def predict(self, prob):
        return prediction_sets(prob, self.qhat, self.rng, self.lam, self.k_reg)


class MondrianConformal(SplitConformal):
    """Stratum-conditional calibration. Strata are integer codes from observable features."""

    def fit(self, prob, label, stratum):
        self.qhat = {}
        scores = aps_scores(prob, label, self.rng, self.lam, self.k_reg)
        for s in np.unique(stratum):
            self.qhat[int(s)] = conformal_quantile(scores[stratum == s], self.alpha)
        return self

    def predict(self, prob, stratum):
        q = np.array([self.qhat.get(int(s), np.inf) for s in stratum])
        return prediction_sets(prob, q, self.rng, self.lam, self.k_reg)


def coverage(member: np.ndarray, label: np.ndarray) -> float:
    return float(member[np.arange(len(label)), label].mean())


def merge_small_strata(stratum: np.ndarray, groups: np.ndarray, min_n: int = 1500, min_groups: int = 4) -> np.ndarray:
    """Merge strata with < min_n samples or < min_groups procedures into the next-lower
    stratum code (feature-spec §5, control 6: loss-first order is encoded in the codes)."""
    s = np.asarray(stratum).copy()
    changed = True
    while changed:
        changed = False
        codes = np.unique(s)
        for c in codes:
            m = s == c
            if (m.sum() < min_n or len(np.unique(groups[m])) < min_groups) and len(codes) > 1:
                target = codes[codes < c].max() if (codes < c).any() else codes[codes > c].min()
                s[m] = target
                changed = True
                break
    return s
