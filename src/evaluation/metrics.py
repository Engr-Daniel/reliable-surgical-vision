"""Reliability metrics used by the pre-registered analyses (preregistration v1.1 §7).

All functions accept optional per-sample weights. Procedure-level bootstrap resamples are
implemented as integer weights (number of times each procedure was drawn), so a single
pre-sort serves every resample (see ``SortedScores``).
"""
from __future__ import annotations

import numpy as np


def auroc(score: np.ndarray, label: np.ndarray, weight: np.ndarray | None = None) -> float:
    """Weighted AUROC (probability a random failure scores higher than a random success).

    Ties count 1/2. ``label`` = 1 marks the event to detect (frame failure).
    """
    s = np.asarray(score, float)
    y = np.asarray(label, bool)
    w = np.ones_like(s) if weight is None else np.asarray(weight, float)
    order = np.argsort(s, kind="mergesort")
    s, y, w = s[order], y[order], w[order]
    # group ties
    uniq, start = np.unique(s, return_index=True)
    end = np.append(start[1:], len(s))
    wpos = np.where(y, w, 0.0)
    wneg = np.where(~y, w, 0.0)
    pos_g = np.add.reduceat(wpos, start)
    neg_g = np.add.reduceat(wneg, start)
    neg_below = np.cumsum(neg_g) - neg_g
    num = np.sum(pos_g * (neg_below + 0.5 * neg_g))
    den = wpos.sum() * wneg.sum()
    return float(num / den) if den > 0 else float("nan")


class SortedScores:
    """Pre-sorted scores for fast weighted AUROC under many procedure-weight vectors.

    Assumes continuous scores (ties are broken by sort order, which is negligible for
    real-valued monitor outputs; use ``auroc`` for exact tie handling).
    """

    def __init__(self, score, label, group):
        order = np.argsort(np.asarray(score, float), kind="mergesort")
        self.y = np.asarray(label, bool)[order]
        self.g = np.asarray(group)[order]

    def auroc(self, group_weight: np.ndarray) -> float:
        w = group_weight[self.g]
        wneg = np.where(self.y, 0.0, w)
        below = np.cumsum(wneg) - wneg
        num = np.sum(np.where(self.y, w * below, 0.0))
        den = np.sum(np.where(self.y, w, 0.0)) * wneg.sum()
        return float(num / den) if den > 0 else float("nan")


def risk_coverage(confidence: np.ndarray, error: np.ndarray, weight: np.ndarray | None = None):
    """Selective risk at each coverage when accepting the most confident samples first."""
    c = np.asarray(confidence, float)
    e = np.asarray(error, float)
    w = np.ones_like(c) if weight is None else np.asarray(weight, float)
    order = np.argsort(-c, kind="mergesort")
    cw = np.cumsum(w[order])
    risk = np.cumsum((w * e)[order]) / cw
    coverage = cw / cw[-1]
    return coverage, risk


def aurc(confidence, error, weight=None) -> float:
    """Area under the risk–coverage curve (lower is better)."""
    cov, risk = risk_coverage(confidence, error, weight)
    w = np.diff(np.concatenate([[0.0], cov]))
    return float(np.sum(w * risk))


def ece(prob: np.ndarray, label: np.ndarray, n_bins: int = 15) -> float:
    """Top-label expected calibration error with equal-width bins."""
    p = np.asarray(prob, float)
    y = np.asarray(label)
    conf = p.max(1)
    pred = p.argmax(1)
    correct = (pred == y).astype(float)
    bins = np.minimum((conf * n_bins).astype(int), n_bins - 1)
    total = 0.0
    for b in range(n_bins):
        m = bins == b
        if m.any():
            total += m.mean() * abs(correct[m].mean() - conf[m].mean())
    return float(total)


def nll(prob: np.ndarray, label: np.ndarray, eps: float = 1e-12) -> float:
    p = np.asarray(prob, float)
    return float(-np.mean(np.log(np.clip(p[np.arange(len(label)), label], eps, 1.0))))


def brier(prob: np.ndarray, label: np.ndarray) -> float:
    p = np.asarray(prob, float)
    onehot = np.eye(p.shape[1])[label]
    return float(np.mean(np.sum((p - onehot) ** 2, 1)))


def sustained_events(fail: np.ndarray, min_len: int) -> list[tuple[int, int]]:
    """(start, end_exclusive) of runs of ``fail`` lasting >= ``min_len`` steps."""
    f = np.asarray(fail, bool)
    padded = np.concatenate([[False], f, [False]])
    edges = np.flatnonzero(padded[1:] != padded[:-1])
    return [(s, e) for s, e in zip(edges[::2], edges[1::2]) if e - s >= min_len]


def transition_mask(labels: np.ndarray, radius: int) -> np.ndarray:
    """True for steps within ``radius`` of a ground-truth phase change (excluded in sensitivity analysis)."""
    y = np.asarray(labels)
    change = np.flatnonzero(y[1:] != y[:-1]) + 1
    m = np.zeros(len(y), bool)
    for c in change:
        m[max(0, c - radius):min(len(y), c + radius)] = True
    return m
