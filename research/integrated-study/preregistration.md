# Pre-registration — Telemetry-Aware Reliability of Online Surgical Phase Recognition

**Version:** 1.1 · **Frozen:** 2026-11-12 (Phase 1, P1.2; amended the same day before any data, see §12) · **Author:** Oyewale Daniel  
**Status:** frozen before any data were acquired and before any model was trained or evaluated. Any later change is logged in §12 with date and reason. Test-set results may not motivate changes to §§3–9.

Companion specifications: [`pipeline-spec.md`](pipeline-spec.md) (media pipeline), [`feature-spec.md`](feature-spec.md) (monitor features and leakage controls), [`dataset-desk-checks.md`](dataset-desk-checks.md), [`baseline-selection.md`](baseline-selection.md), [`feasibility/`](feasibility/) (power and compute).

---

## 1. Questions
- **RQ1 (primary):** In online surgical phase recognition on network-delivered video, does receiver-observable network and transport/decoder telemetry improve failure detection and selective deferral beyond a strong video-only monitor?
- **RQ2 (secondary):** Do calibration and split-conformal prediction sets calibrated on clean video remain valid under decoder-mediated impairment and natural centre shift, and does telemetry-stratified calibration restore per-condition coverage more efficiently than global recalibration?
- **RQ3 (secondary):** At matched decoded-video quality, does phase-recognition failure depend on the degradation mechanism?

Evidence basis: `literature/intersection-analysis/` (P0.7) and `literature/gap-validation/` (P1.1).

## 2. Data
| Role | Dataset | Procedures | Notes |
|---|---|---|---|
| Phase-model training | Cholec80 videos 1–32 | 32 | standard TeCNO-style split |
| Phase-model validation / clean conformal calibration | Cholec80 videos 33–40 | 8 | early stopping, temperature scaling, clean CP calibration |
| **Primary test** (monitor cross-fitting, all RQ1/RQ3 estimates) | Cholec80 videos 41–80 | 40 | never used for phase-model training or tuning |
| External natural-shift replication (descriptive) | PhaKIR public release | 8 (3 centres) | same 7-phase taxonomy as Cholec80 (verified, P1.5) |
| Cross-procedure replication (optional, gated) | AutoLaparo 10/4/7 | 21 | separate phase model on its own label set |

Phase labels are evaluated at 1 fps (standard for Cholec80). Video is streamed at native 25 fps.

## 3. Conditions (impairment tiers)
Each test procedure is streamed once under every condition, with the forward video path only ([`pipeline-spec.md`](pipeline-spec.md)):

| Tier | Bandwidth | One-way delay | Jitter | Gilbert–Elliott loss pE / mean burst | Basis |
|---|---|---|---|---|---|
| T0 Local (no network) | — | — | — | — | reference |
| T1 Hospital LAN | 100 Mbps | 3 ms | 1 ms | 0.01% / 2 pkts | VISTA tier |
| T2 5G Urban | 20 Mbps | 35 ms | 8 ms | 0.5% / 3 pkts | VISTA tier |
| T3 4G Rural | 5 Mbps | 150 ms | 30 ms | 2.0% / 6 pkts | VISTA tier |
| T4 LEO satellite | 30 Mbps | 30 ms | 10 ms | 1.5% / 5 pkts | VISTA tier |
| T5 GEO satellite | 10 Mbps | 600 ms | 50 ms | 0.5% / 2 pkts | VISTA tier |

Tier parameters are taken from the published VISTA tier table (IX01). VISTA's pipeline code is not publicly released (checked 2026-11-12), so the pipeline is built independently. Recovery settings (NACK/RTX on; FEC off) are fixed for the primary analysis. An RTX-off / FEC-on sensitivity factor is secondary.

RQ3 adds pre-specified one-factor conditions (§7.3).

## 4. Models
Two online phase models, fixed before testing ([`baseline-selection.md`](baseline-selection.md)):
- **M1:** TeCNO (ResNet-50 features + causal MS-TCN), trained on clean Cholec80 1–32;
- **M2:** Surgformer in online mode, trained on clean Cholec80 1–32.

Neither model is trained on impaired video in the primary analysis. RQ1 is analysed per model; the primary inference is on **M1**, and **M2** is a robustness replication.

## 5. Outcomes
- **Frame failure** `F_t = 1` if the online prediction at 1-fps step *t* ≠ ground truth.
- **Sustained failure event:** ≥ 2 s of consecutive `F_t = 1`. Event onset is the first frame.
- **Transition-relaxed sensitivity analysis:** exclude ±2 s around ground-truth phase transitions.

## 6. Reliability monitors (RQ1)
Feature tiers are defined exactly in [`feature-spec.md`](feature-spec.md):
- **Video-only monitor A:** V0 + V1, where V1 includes a learned frame-quality → error predictor;
- **Full monitor B:** V0 + V1 + N1 + N2.

Monitor learner: L2-regularised logistic regression (**primary**) and gradient-boosted trees (**secondary**). Hyperparameters are chosen by inner cross-validation within training folds only.

**Cross-fitting.** The 40 test procedures are split into 5 procedure-level folds, fixed by a seeded shuffle (seed 20261112). Monitors are trained on 4 folds (all tiers) and scored on the held-out fold. Every frame therefore receives an out-of-fold score. All tiers of a procedure always stay in the same fold.

Telemetry window *W* ∈ {0.5, 1, 2} s is selected by inner cross-validation on training folds and reported.

## 7. Hypotheses and tests

### 7.1 RQ1 (co-primary H1a, H1b; Holm-corrected at α = 0.05)
- **H1a:** ΔAUROC = AUROC(B) − AUROC(A) for frame failure, pooled over T1–T5, is > 0. Inference: one-sided test via 2,000 procedure-level bootstrap resamples (all tiers of a procedure resampled together; BCa interval), Holm-adjusted. **0.02 is the smallest effect of interest**: the effect the study is powered to detect and the benchmark for practical relevance. Every result is reported with its point estimate and 95% CI relative to both 0 and 0.02:
  - CI lower bound > 0.02 → *practically relevant gain*;
  - CI lower bound > 0 but ≤ 0.02 → *detectable gain; practical relevance not established*;
  - CI includes 0 → *no detectable gain*;
  - CI upper bound < 0.02 → *any gain is below the practical margin* (informative negative).
- **H1b:** ΔAURC (selective deferral, A − B) > 0, with the same bootstrap, Holm-adjusted together with H1a.
- **H1c (secondary, only if H1a holds):** median alarm lead time for sustained failure events, at the operating point giving 1 false alarm/min on training folds, is longer for B than A. Paired procedure-level bootstrap.
- **H1d (secondary, only if H1a holds):** leave-one-tier-out (T1–T5): Δ remains > 0 for at least 4 of 5 held-out tiers.
- **Pre-specified subgroup:** frames whose V1 quality is in the nominal (T1) range. This estimates how much telemetry adds when the pixels look fine.

### 7.2 RQ2
- **H2a:** marginal coverage of clean-calibrated APS and RAPS sets (1−α = 0.90; calibration on Cholec80 33–40, clean) falls by > 2 percentage points in at least one of T2–T5. ECE (15 bins) and NLL are reported with CIs.
- **H2b:** Mondrian CP with strata from **binned receiver-observable telemetry** (tertiles of N1 loss and N2 freeze indicators, fixed on training folds) gives per-stratum coverage within 2 pp of nominal, at a smaller mean set size than global recalibration on mixed-tier data. Calibration data are training folds (cross-fitted). Minimum stratum size: 1,500 calibration frames from ≥ 4 procedures. Smaller strata are merged as specified in `feature-spec.md` §5.
- **H2c (descriptive):** PhaKIR coverage and ECE per centre, with no hypothesis test.

### 7.3 RQ3
One-factor conditions on top of T1: bitrate caps {8, 4, 2, 1} Mbps (compression-dominated); Gilbert–Elliott burst loss {0.5, 1, 2, 4}% at mean burst 5 (loss/freeze-dominated); added delay {100, 300, 600} ms with jitter 10% of delay (delay-dominated).
- **H3:** in the matched band of mean VMAF (±3 VMAF points, band fixed after measuring VMAF only, before computing any model output), the sustained-failure rate is higher under loss-dominated than compression-dominated conditions. Paired procedure-level bootstrap CI of the difference excludes 0.
- **Exploratory:** low-light (Level-A visual corruption, severity 3) × burst loss 2%, mixed-effects logistic model with random intercept per procedure.

## 8. Analysis rules
- The unit of resampling is always the **procedure**.
- Report every pre-specified estimate with its 95% CI, whether or not it is significant.
- No outlier exclusion. A procedure whose stream fails to complete under a tier is re-streamed once. If it fails again, the failure is logged and that procedure-tier is dropped, and the drop count is reported.
- Secondary analyses are labelled as such. Analyses not listed here are labelled **exploratory**.

## 9. Stopping and reporting
- No interim looks at test-set monitor performance.
- All of H1a/H1b, H2a/H2b and H3 are reported in the main results, including negative and null results.
- If H1a and H1b both fail (or the CI upper bound for ΔAUROC is < 0.02), RQ1 is reported as a primary negative result ("telemetry adds no detectable value beyond video-only monitoring in this pipeline"). H1c/H1d are not run.
- Segmentation (X25) is not started unless both RQ1 and RQ2 are reported.

## 10. Power and feasibility
See [`feasibility/README.md`](feasibility/README.md). Simulations assuming heterogeneous telemetry value suggest that 40 test procedures × 5 impaired tiers give a high probability that the CI excludes 0 when the true Δ ≈ 0.02 (CI width ≈ 0.01). The simulation does **not** model monitor-training error or train/test tier shift, so it is optimistic. If the observed CI is wider than 0.03, the result is reported as imprecise rather than null.

## 11. Known limitations (stated in advance)
- The network is emulated (NetEm), not a clinical telesurgery link. Tier parameters come from a published benchmark, not from any proprietary platform.
- Cholec80 is single-centre. The external replication (PhaKIR, n = 8) is descriptive only.
- Phase labels at 1 fps; ambiguous transitions handled by sensitivity analysis.
- NetEm randomness is not bit-reproducible across runs. Realised packet traces and received bitstreams are archived, and decoding is deterministic from the archived streams (`pipeline-spec.md` §6).

## 12. Amendment log
| Date | Section | Change | Reason |
|---|---|---|---|
| 2026-11-12 | — | v1.0 frozen | — |
| 2026-11-12 | §7.1 H1a | Replaced "Δ ≥ 0.02 **and** CI > 0" with a superiority test (Δ > 0), keeping 0.02 as the smallest effect of interest with four pre-specified interpretation bands. Percentile bootstrap replaced by BCa | P1.6 simulation showed that requiring the point estimate ≥ 0.02 gives only 0.33 power when the true Δ ≈ 0.02 (40 procedures × 5 tiers), and that the percentile bootstrap's one-sided false-positive rate was 3–6% vs nominal 2.5%. Amended before any data were acquired |
