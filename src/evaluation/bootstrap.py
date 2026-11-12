"""Procedure-level (cluster) bootstrap with BCa intervals (preregistration v1.1 §7–8).

The resampling unit is always the procedure: all frames and all impairment tiers of a
procedure are drawn together. A resample is a vector of integer weights (multiplicity of
each procedure), so statistics are written as ``stat(weights) -> float``.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.stats import norm


@dataclass
class BootResult:
    estimate: float
    lo: float
    hi: float
    p_one_sided: float  # bootstrap estimate of P(stat <= 0) under resampling (for H: stat > 0)
    boots: np.ndarray
    method: str

    def band(self, margin: float) -> str:
        """Pre-registered interpretation band for H1a (preregistration v1.1 §7.1)."""
        if self.lo > margin:
            return "practically relevant gain"
        if self.lo > 0:
            return "detectable gain; practical relevance not established"
        if self.hi < margin:
            return "any gain is below the practical margin"
        return "no detectable gain"


def cluster_bootstrap(stat: Callable[[np.ndarray], float], n_clusters: int, n_boot: int = 2000,
                      alpha: float = 0.05, seed: int = 20261112, method: str = "bca") -> BootResult:
    rng = np.random.default_rng(seed)
    ones = np.ones(n_clusters)
    est = stat(ones)
    boots = np.empty(n_boot)
    for b in range(n_boot):
        boots[b] = stat(np.bincount(rng.integers(0, n_clusters, n_clusters), minlength=n_clusters).astype(float))
    boots = boots[np.isfinite(boots)]
    if method == "percentile":
        lo, hi = np.percentile(boots, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    elif method == "bca":
        # bias correction
        prop = np.clip(np.mean(boots < est) + 0.5 * np.mean(boots == est), 1e-6, 1 - 1e-6)
        z0 = norm.ppf(prop)
        # acceleration by cluster jackknife
        jack = np.empty(n_clusters)
        for i in range(n_clusters):
            w = ones.copy()
            w[i] = 0.0
            jack[i] = stat(w)
        jack = jack[np.isfinite(jack)]
        d = jack.mean() - jack
        denom = 6.0 * (np.sum(d ** 2) ** 1.5)
        a = np.sum(d ** 3) / denom if denom > 0 else 0.0
        z = norm.ppf([alpha / 2, 1 - alpha / 2])
        adj = norm.cdf(z0 + (z0 + z) / (1 - a * (z0 + z)))
        lo, hi = np.quantile(boots, adj)
    else:
        raise ValueError(method)
    return BootResult(float(est), float(lo), float(hi), float(np.mean(boots <= 0)), boots, method)


def holm(pvalues: dict[str, float], alpha: float = 0.05) -> dict[str, bool]:
    """Holm step-down: returns reject decisions per hypothesis."""
    items = sorted(pvalues.items(), key=lambda kv: kv[1])
    m = len(items)
    out, still = {}, True
    for k, (name, p) in enumerate(items):
        still = still and p <= alpha / (m - k)
        out[name] = still
    return out
