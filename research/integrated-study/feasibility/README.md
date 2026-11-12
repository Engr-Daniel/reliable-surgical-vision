# Feasibility and Power (P1.6)

**Date:** 2026-11-12 · **Script:** [`power_sim.py`](power_sim.py) (numpy only) · **Results:** [`power_sim_results.csv`](power_sim_results.csv)

## 1. Question
With *N* held-out test procedures, each streamed through *K* impairment tiers, how precise is the procedure-level bootstrap CI for ΔAUROC = AUROC(full monitor) − AUROC(video-only monitor), and how often does it exclude 0 when the true gain is about 0.02?

## 2. Simulation model (deliberately simple)
- Per frame (1 fps, 15 min per procedure-tier), failure probability depends on a **video-visible** risk `z_v` and a **network-only** risk `z_n`. Both are AR(1)-autocorrelated (φ = 0.95), so failures come in runs.
- Procedure and tier random intercepts.
- **Heterogeneous telemetry value:** the network-only risk carries no weight on the clean tier, a random multiplier U(0.3, 1.7) on impaired tiers, and a random per-procedure slope N(1, 0.8), so it can be useless or even misleading for some procedures.
- Monitors see their signals with correlated noise (ρ = 0.7). The weight on `z_n` is calibrated to hit the target population Δ.
- 100 simulated studies per cell; 300 procedure-level bootstrap resamples each (weighted AUROC, exact).

## 3. Results
| True Δ | N procedures | K tiers | P(CI excludes 0) | Mean CI width | Mean Δ̂ |
|---|---|---|---|---|---|
| 0 (null) | 20 / 40 / 60 | 3 or 5 | 0.03–0.06 (nominal one-sided 0.025) | 0.002–0.005 | ≈ 0 |
| ≈ 0.02 | 20 | 3 / 5 | 0.98 / 1.00 | 0.012 / 0.013 | 0.015 / 0.019 |
| ≈ 0.02 | **40** | **5** | **1.00** | **0.010** | **0.020** |
| ≈ 0.02 | 60 | 5 | 1.00 | 0.008 | 0.019 |
| ≈ 0.03 | 40 | 5 | 1.00 | 0.016 | 0.029 |
| ≈ 0.04 | 20 / 40 / 60 | 5 | 0.97 / 1.00 / 0.99 | 0.041 / 0.030 / 0.024 | ≈ 0.045 |

Full grid in the CSV.

## 4. What this changed in the pre-registration
1. **Criterion fixed.** v1.0 required "point estimate ≥ 0.02 **and** CI > 0". At true Δ ≈ 0.02 that joint criterion succeeded in only **33%** of simulated studies (it succeeds 96% of the time at Δ ≈ 0.03). v1.1 uses a superiority test (Δ > 0), with 0.02 as the smallest effect of interest and four interpretation bands.
2. **BCa bootstrap.** The percentile bootstrap's one-sided false-positive rate under the null was 3–6% against a nominal 2.5% (Monte-Carlo SE ≈ 1.6–2%). v1.1 specifies BCa intervals with 2,000 resamples.
3. **Five impaired tiers, not three.** With three tiers the realised Δ is diluted (the clean tier carries no network signal), giving a mean Δ̂ of 0.016 against 0.020.
4. **Effect heterogeneity drives CI width.** Larger effects with more procedure-to-procedure variation give wider CIs (≈ 0.03 at Δ ≈ 0.04). The procedure, not the frame, is the effective unit, which confirms procedure-level resampling.

## 5. Why these numbers are optimistic
The simulation does **not** include:
- estimation error from **training** the monitors (cross-fitting on 32 procedures per fold);
- distribution shift between training-fold and test-fold tiers (the H1d leave-one-tier-out setting);
- the real correlation between telemetry and pixel evidence. The real network-only signal may be much smaller than any value simulated here; that is the point of the study.

Precision was therefore treated as necessary but not sufficient: N = 40 × 5 tiers is **adequate** for H1a under these assumptions, and the pre-registration commits to reporting any CI wider than 0.03 as *imprecise* rather than null.

## 6. Compute and storage
See [`../pipeline-spec.md`](../pipeline-spec.md) §7. Real-time streaming is the binding constraint: ≈ 500 h of stream time in total, ≈ 32 h wall-clock with 16 parallel namespace pairs, and ≤ 1.8 TB of archived received streams. GPU inference at 1 fps is modest (≈ 1.8 M frames per model).

## 7. Reproduce
```bash
python3 research/integrated-study/feasibility/power_sim.py --reps 100 --boot 300   # full grid, ~1 h on 2 cores
python3 research/integrated-study/feasibility/power_sim.py --targets 0.02 --n 40 --tiers 5 --reps 100 --boot 300 --out check.csv
```
Seeded (`20261112`). The published CSV merges three runs; the `run` column identifies each.
