#!/usr/bin/env python3
"""P1.6 precision/power simulation for H1a (Delta AUROC >= 0.02, procedure-level bootstrap).

Question: with N held-out test procedures, each replayed through K impairment tiers,
how often does a procedure-level bootstrap 95% CI for
    Delta = AUROC(V0+V1+N1+N2) - AUROC(V0+V1)
exclude 0 when the true Delta is ~0.02, and how wide is the CI?

Generative model (a deliberately simple, conservative stand-in, not a model of surgery):
  per frame:  logit P(fail) = a + u_proc + u_tier + b_v * z_v + b_n,proc * m_tier * z_n
    (b_n,proc random per procedure; m_tier = 0 on the clean tier, U(0.3,1.7) otherwise)
    z_v ~ N(0,1): failure risk visible in the received video
    z_n ~ N(0,1): failure risk visible only on the network side
    u_proc ~ N(0, s_proc), u_tier ~ N(0, s_tier): procedure / tier random effects
  video-only monitor score   = z_v + e1
  full monitor score         = z_v + w * z_n + e2      (w tuned so true Delta ~ target)
  e1, e2 ~ N(0, s_e), correlated rho (shared monitor noise)
Frames are subsampled to 1 fps; failure events are autocorrelated via AR(1) latents
(phase errors come in runs), which shrinks the effective sample size.

Usage:
    python3 research/integrated-study/feasibility/power_sim.py [--reps 200] [--boot 300]
Writes power_sim_results.csv next to this script. numpy is the only dependency.
"""
import argparse
import csv
import os

import numpy as np


def auroc(score, label):
    order = np.argsort(score, kind="mergesort")
    ranks = np.empty(len(score))
    ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool)
    n1, n0 = pos.sum(), (~pos).sum()
    if n1 == 0 or n0 == 0:
        return np.nan
    return (ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def ar1(rng, n, phi):
    x = np.empty(n)
    x[0] = rng.standard_normal()
    eps = rng.standard_normal(n) * np.sqrt(1 - phi ** 2)
    for i in range(1, n):
        x[i] = phi * x[i - 1] + eps[i]
    return x


def simulate(rng, n_proc, n_tiers, w, frames=1500, phi=0.95, a=-1.6, b_v=1.2, b_n=1.0,
             s_proc=0.6, s_tier=0.5, s_e=0.8, rho=0.7, s_bn=0.8):
    """Return per-procedure arrays (score_v, score_full, label).

    Heterogeneity of telemetry value: tier 0 is a clean link (network-only risk carries no
    weight); other tiers get a random multiplier ~ U(0.3, 1.7); each procedure gets a
    random slope b_n_proc ~ N(1, s_bn) (can be ~0 or negative), so in some procedures the
    network-side signal is uninformative or misleading.
    """
    tier_eff = rng.normal(0, s_tier, n_tiers)
    tier_mult = np.concatenate([[0.0], rng.uniform(0.3, 1.7, n_tiers - 1)])
    out = []
    for _ in range(n_proc):
        u = rng.normal(0, s_proc)
        bn_proc = b_n * rng.normal(1.0, s_bn)
        sv, sf, lab = [], [], []
        for t in range(n_tiers):
            zv, zn = ar1(rng, frames, phi), ar1(rng, frames, phi)
            p = 1 / (1 + np.exp(-(a + u + tier_eff[t] + b_v * zv + bn_proc * tier_mult[t] * zn)))
            y = rng.random(frames) < p
            e = rng.multivariate_normal([0, 0], [[s_e ** 2, rho * s_e ** 2], [rho * s_e ** 2, s_e ** 2]], frames)
            sv.append(zv + e[:, 0])
            sf.append(zv + w * zn + e[:, 1])
            lab.append(y)
        out.append((np.concatenate(sv), np.concatenate(sf), np.concatenate(lab)))
    return out


class Sorted:
    """Pre-sorted pooled data so each bootstrap resample is a weighted AUROC in O(n)."""

    def __init__(self, procs):
        pid = np.concatenate([np.full(len(p[2]), i) for i, p in enumerate(procs)])
        y = np.concatenate([p[2] for p in procs]).astype(bool)
        self.parts = []
        for k in (0, 1):
            s = np.concatenate([p[k] for p in procs])
            o = np.argsort(s, kind="mergesort")
            self.parts.append((pid[o], y[o]))

    def wauroc(self, k, wproc):
        pid, y = self.parts[k]
        w = wproc[pid]
        wneg = np.where(y, 0.0, w)
        below = np.cumsum(wneg) - wneg
        num = np.sum(np.where(y, w * below, 0.0))
        return num / (np.sum(np.where(y, w, 0.0)) * wneg.sum())

    def delta(self, wproc):
        return self.wauroc(1, wproc) - self.wauroc(0, wproc)


def delta(procs, idx):
    sv = np.concatenate([procs[i][0] for i in idx])
    sf = np.concatenate([procs[i][1] for i in idx])
    y = np.concatenate([procs[i][2] for i in idx])
    return auroc(sf, y) - auroc(sv, y), auroc(sv, y)


def calibrate_w(target, seed=0):
    """Find w giving the target population Delta AUROC (large simulated population)."""
    rng = np.random.default_rng(seed)
    lo, hi = 0.0, 1.5
    for _ in range(14):
        mid = (lo + hi) / 2
        procs = simulate(rng, 60, 5, mid, frames=1500)
        d, base = delta(procs, range(len(procs)))
        lo, hi = (mid, hi) if d < target else (lo, mid)
    return (lo + hi) / 2, base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=120)
    ap.add_argument("--boot", type=int, default=300)
    ap.add_argument("--targets", default="0,0.02,0.04")
    ap.add_argument("--n", default="20,40,60")
    ap.add_argument("--tiers", default="3,5")
    ap.add_argument("--out", default="power_sim_results.csv")
    ap.add_argument("--frames", type=int, default=900, help="frames per procedure-tier at 1 fps (900 = 15 min)")
    args = ap.parse_args()
    rng = np.random.default_rng(20261112)
    rows = []
    for target in [float(x) for x in args.targets.split(",")]:
        n_list = [int(x) for x in args.n.split(",")]
        w, base = calibrate_w(target) if target > 0 else (0.0, np.nan)
        for n_proc in n_list:
            for n_tiers in [int(x) for x in args.tiers.split(",")]:
                hits, widths, ests, both = 0, [], [], 0
                for _ in range(args.reps):
                    procs = simulate(rng, n_proc, n_tiers, w, frames=args.frames)
                    S = Sorted(procs)
                    d_hat = S.delta(np.ones(n_proc))
                    boots = np.array([S.delta(np.bincount(rng.integers(0, n_proc, n_proc), minlength=n_proc).astype(float))
                                      for _ in range(args.boot)])
                    lo, hi = np.nanpercentile(boots, [2.5, 97.5])
                    hits += lo > 0
                    both += (lo > 0) and (d_hat >= 0.02)
                    widths.append(hi - lo)
                    ests.append(d_hat)
                rows.append(dict(true_delta=target, w=round(w, 4), n_test_procedures=n_proc, n_tiers=n_tiers,
                                 reps=args.reps, boot=args.boot,
                                 p_ci_excludes_0=round(hits / args.reps, 3),
                                 p_ci_excl0_and_point_ge_002=round(both / args.reps, 3),
                                 mean_ci_width=round(float(np.mean(widths)), 4),
                                 mean_delta_hat=round(float(np.mean(ests)), 4)))
                print(rows[-1], flush=True)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    with open(path, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
    print("wrote", path)


if __name__ == "__main__":
    main()
