# P0.7 Revised Research Questions

These replace the provisional Track A–C questions. They are **candidate** questions: Phase 1 (Gap Validation) must confirm them before any experiment is run. Numeric thresholds are proposed pre-registration values. They may be revised during Phase 1 with recorded rationale, but must be frozen before any test-set result is inspected.

## Umbrella question (unchanged)
How can computer-vision systems used in robot-assisted and tele-robotic surgery maintain reliable inference, or safely abstain, when deployment conditions differ from those encountered during development?

## Shared setting
- **Task:** online (causal) surgical phase recognition.
- **Input path:** source video → encoder → RTP/UDP → network emulator → receiver (jitter buffer, recovery) → decoder → model. Impairments are applied only to the forward video path.
- **Impairment design:** tiered scenarios seeded from published envelopes (P0.6 protocol; VISTA tiers IX01), plus one-factor sweeps. Decoded-video abstractions (Level A) serve as controls.
- **Data:** Cholec80 for development (procedure-level train / calibration / validation / test); PhaKIR for external natural-shift replication; AutoLaparo optional.
- **Feature tiers available to a reliability monitor at time *t*** (receiver-observable only; the emulator configuration and tier label are never inputs):
  - **V0, model-internal:** max-softmax, entropy, temperature-scaled confidence, ensemble/MC disagreement, recent prediction-change rate.
  - **V1, decoded-video:** pixel-only quality and continuity cues computed from received frames (no-reference quality, blockiness/blur, frame-difference freeze detection, temporal consistency of features). This is the TCSR-style strong video-only baseline.
  - **N1, network:** receiver-side loss rate, burst-loss statistics, inter-arrival jitter, one-way delay/RTT estimates, delivered throughput over a trailing window.
  - **N2, transport/decoder:** retransmission/FEC recovery counts, jitter-buffer delay and underruns, decoder error/concealment indicators, frame-arrival lateness.
- **Failure label:** online prediction ≠ ground-truth phase at frame *t*. A **sustained failure event** is ≥ *k* s of consecutive error (proposed *k* = 2 s). Sensitivity analysis excludes ±*b* s around ground-truth transitions (proposed *b* = 2 s), in line with relaxed-boundary practice in phase evaluation (SV32).
- **Statistical unit:** the procedure (video). All CIs use procedure-level bootstrap (proposed 2,000 resamples) so that long videos do not dominate.

---

## RQ1 — Primary (former Track C)
> In online surgical phase recognition on network-delivered video, does receiver-observable network and transport/decoder telemetry improve the detection of model failure, and selective deferral, beyond a strong monitor that uses only model outputs and decoded frames?

**H1a (incremental detection).** On held-out test procedures, a monitor using V0+V1+N1+N2 achieves frame-level failure-detection AUROC at least **0.02** higher than V0+V1, with the 95% procedure-level bootstrap CI of the difference excluding 0.

**H1b (incremental selective value).** The same comparison reduces the area under the risk–coverage curve (AURC) of selective deferral, with the CI of the difference excluding 0.

**H1c (earlier warning; conditional on H1a).** For sustained failure events, the median alarm lead time relative to event onset (at a fixed operating false-alarm rate per minute, pre-specified on validation) is greater for V0+V1+N1+N2 than for V0+V1.

**H1d (transfer; conditional on H1a).** The H1a gain persists under leave-one-impairment-tier-out evaluation, following the leave-one-corruption-out logic of RI34.

**Ablations:** N1 only, N2 only, N1+N2 without V; telemetry window *W* ∈ {0.5, 1, 2} s, selected on validation only.

**Rejection:** H1a and H1b both fail → telemetry adds no detectable value beyond video-only monitoring for this task and pipeline. This is reported as a primary negative result.

**Key confound controls:**
- V1 must include pixel-detectable freeze/repeat detection. Otherwise telemetry would "win" simply by signalling something visible in the frames.
- Leakage control: no emulator ground truth, and no tier identity, in any feature.
- Matched-comparison analysis: telemetry gain is reported separately for frames whose V1 quality is in the nominal range, which isolates information that is *not visible* in the pixels.

---

## RQ2 — Secondary (former Track B)
> Do calibration, selective risk–coverage and split-conformal phase prediction sets calibrated on clean development video remain valid under decoder-mediated network impairment and natural centre shift, and does conditioning the calibration on observable network state restore per-condition coverage more efficiently than global recalibration?

**H2a (degradation).** At degraded tiers, marginal coverage of clean-calibrated APS/RAPS sets at nominal 1−α = 0.90 falls by more than **2 percentage points**, and ECE/NLL worsen relative to clean test procedures.

**H2b (telemetry-stratified calibration).** Mondrian conformal calibration with strata defined by **binned receiver-observable telemetry** (not tier labels) brings per-stratum coverage to within 2 percentage points of nominal, at a smaller mean set size than recalibrating globally on mixed-condition calibration data.

**H2c (natural shift, descriptive).** Coverage and calibration on PhaKIR are reported with procedure-level uncertainty. With 8 public procedures this arm is **descriptive**, and no hypothesis test is planned.

**Rejection of H2b:** per-stratum coverage is no closer to nominal than global recalibration, or strata contain too few calibration procedures for stable quantiles (minimum stratum size fixed in Phase 1).

---

## RQ3 — Secondary (former Track A)
> Under decoder-mediated network impairment, does online phase-recognition error depend on the degradation mechanism (sustained spatial artefacts vs freezes/frame loss vs added delay) when overall decoded-video quality is matched?

**H3.** At matched mean VMAF (within a pre-specified band), conditions dominated by burst loss/freezes yield a higher sustained-failure rate than conditions dominated by bitrate-limited compression, with a procedure-level CI on the difference excluding 0.

**Secondary (exploratory, pre-specified pairs only):** interaction between one visual factor (low light *or* smoke, Level A) and one network factor (burst loss) for phase error, analysed with a mixed-effects model with procedure as a random effect.

**Rejection:** the mechanism difference at matched VMAF falls within uncertainty. Video-quality metrics are then accepted as an adequate risk proxy for this task.

---

## What these RQs deliberately do not claim
- No clinical safety, no safe network threshold, no deployment readiness.
- No equivalence between the emulated pipeline and any proprietary platform (e.g. Toumai). The abstraction gap is reported explicitly.
- No novel UQ, OOD or conformal **method**. The contributions are empirical evidence about a measurable question.
