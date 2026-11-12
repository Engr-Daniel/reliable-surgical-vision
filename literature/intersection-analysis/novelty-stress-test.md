# P0.7 Novelty Stress-Test — Tracks A, B and C

## Method
For each provisional track:
1. state the candidate contribution claims, from broadest to narrowest;
2. test each claim against the closest retained evidence (`intersection-map.csv` cells);
3. give a verdict: **CLOSED** (occupied), **NARROWED** (survives only in a narrower form), or **OPEN IN RETAINED EVIDENCE** (no occupying work found, with residual risk);
4. state what survives with all "first"/novelty language removed;
5. state the result that would end the track (kill criterion).

A verdict of OPEN IN RETAINED EVIDENCE is **not** a novelty claim.

---

## Track A — Compound Shift

**Provisional question:** How do individual and compound visual/network-induced shifts affect surgical-CV performance and reliability?

| # | Candidate claim | Closest evidence | Verdict |
|---|---|---|---|
| A1 | Surgical CV degrades under distribution shift | X01, X02 (many) | **CLOSED** |
| A2 | Smoke/blood/low light degrade surgical models | X03 (SegSTRONG-C, CaRTS) | **CLOSED** |
| A3 | Compound/combined corruption degrades surgical models | X05 (SH17 adjacent, IX04 combined photometric) | **CLOSED** as a general idea |
| A4 | Network-like (packet-loss) corruption degrades surgical AI | X07 (Endo-C6) | **CLOSED** as a general idea |
| A5 | Multiple network factors interact | X10 (Heemeyer 2026; VISTA tiers) | **CLOSED** for human outcomes; the same design applied to AI would be incremental |
| A6 | Conventional online phase recognition evaluated on video from a real encoder→transport→emulator→decoder pipeline, with degradation attributed to mechanism (spatial artefact vs freeze/frame loss vs delay) | X08; VISTA shows matched-PSNR tiers produce different *human* outcomes | **OPEN IN RETAINED EVIDENCE**, medium residual risk |
| A7 | Visual × decoder-mediated network interaction for phase recognition | X05 + X08 | **OPEN IN RETAINED EVIDENCE**, medium residual risk; low standalone value |

**What survives:** A6, a mechanism-level characterisation. It asks whether conditions with *matched* decoded-video quality degrade an online phase model differently depending on the degradation mechanism. This finding is useful even without novelty language, because it tells practitioners whether a video-quality metric is a sufficient proxy for AI risk.

**Assessment:** As a standalone publication, Track A would mostly be "an existing pipeline idea (VISTA) plus an existing task." Its main value is as the **shift substrate** for Tracks B and C.

**Kill criterion:** If, at matched VMAF/PSNR, phase-error differences between mechanisms fall within procedure-level bootstrap uncertainty, A6 is reported as a negative result and video quality is accepted as a sufficient proxy for this task.

**Decision:** Track A is **absorbed** as the shift-construction and degradation-characterisation work package (WP-A). It keeps one secondary RQ (RQ3).

---

## Track B — Selective Inference

**Provisional question:** Can uncertainty-aware, selective and/or conformal methods improve the reliability of surgical visual inference under distribution shift?

| # | Candidate claim | Closest evidence | Verdict |
|---|---|---|---|
| B1 | Uncertainty / calibration for surgical CV | X12 (FGRM, calibrated phase, Meta-SurDiff) | **CLOSED** |
| B2 | OOD / open-set detection for surgical CV | X13 (open-set phase, OpenMIBOOD) | **CLOSED** |
| B3 | Abstention / selective prediction in medical/surgical CV | X15, RI15 | **CLOSED** |
| B4 | Conformal prediction in surgical CV | RI31, RI34 | **CLOSED** as a general idea |
| B5 | Surgical failure monitoring under acquisition degradation with conformal calibration | X14 (TCSR-Monitor) | **CLOSED** for segmentation |
| B6 | Audit: do calibration, risk–coverage and conformal coverage of **online phase recognition** hold under natural shift and **decoder-mediated** network impairment? | X16, X17, X18, X19 | **OPEN IN RETAINED EVIDENCE** (X16/X19), medium residual risk |
| B7 | Conformal calibration **conditioned on deployment-observable network state** (telemetry-Mondrian) restores per-condition coverage | X24; nearest is TCSR severity-aware Mondrian, where severity is *not* observable at deployment | **OPEN IN RETAINED EVIDENCE**, medium residual risk; method novelty is minor |

**What survives:** B6 is an empirical reliability audit and B7 is a design choice evaluated inside it. Both are useful without novelty language: they tell a deployer whether clean-data reliability guarantees carry over to network-delivered video, and whether observable network state is a usable conditioning variable.

**Kill criterion:** B6 cannot be killed, since both coverage holding and coverage failing are informative. B7 is dropped if telemetry-stratified calibration is no closer to nominal per-condition coverage than global recalibration, or if strata are too small for stable quantiles at the available procedure counts.

**Decision:** Track B is **narrowed** to the reliability-evaluation layer (WP-B) and keeps one secondary RQ (RQ2). No new UQ/conformal method is proposed.

---

## Track C — Network-Aware Inference

**Provisional question:** Can visual evidence and network/system telemetry jointly identify unreliable CV inference in telesurgical settings? `R = f(X, N)`

| # | Candidate claim | Closest evidence | Verdict |
|---|---|---|---|
| C1 | Network conditions affect DNN accuracy | X20 (DDS, AccMPEG, VANET) | **CLOSED** (generic) |
| C2 | Network conditions affect telesurgical video quality | X11 (VISTA, hinotori, 5G SA studies) | **CLOSED** |
| C3 | Telemetry can forecast network QoS | X21 (pQoS) | **CLOSED** (generic) |
| C4 | Network/transport telemetry predicts AI-model failure, **in any domain** | X22; adjacent IX09 (AI impact steers transport), patents (telemetry → human video quality) | **OPEN IN RETAINED EVIDENCE**, **high** residual risk: networking/video-analytics venues were only shallowly searched |
| C5 | In surgical phase recognition on network-delivered video, **receiver-observable** network + transport + decoder telemetry improves failure prediction and selective deferral **beyond a strong video-only monitor** (model confidence + decoded-frame quality + temporal cues, TCSR-style) | X23 | **OPEN IN RETAINED EVIDENCE**, **high** residual risk |
| C6 | Telemetry gives **earlier warning** of failure onset than video-only cues | X23 | **OPEN IN RETAINED EVIDENCE**; depends on C5 |
| C7 | Network-aware monitor transfers to unseen impairment tiers / codec settings | X23 + RI34 LOCO protocol | **OPEN IN RETAINED EVIDENCE**; depends on C5 |

**Overlap pressure, combined conceptually:** Endo-C6 (loss corruption → surgical AI), TCSR-Monitor (multi-cue failure monitor + Mondrian CP), VISTA (surgical network pipeline) and DNN-aware streaming (network ↔ DNN accuracy) together surround C5 on every side. C5 survives only because none of them asks whether **non-pixel** information adds to a **strong pixel-based** monitor. The comparison must therefore be against a deliberately strong video-only baseline. A weak baseline (e.g. softmax only) would make any telemetry gain uninformative.

**What survives:** C5, with C6/C7 as conditional follow-ups. With novelty language removed, the claim reads: *"we measure whether the reliability layer of a surgical video model benefits from network-side information, and by how much."* A clear negative result is decision-relevant on its own: it would mean the video itself should be monitored, and network-side integration can be skipped.

**Kill criterion (pre-specified):** On held-out procedures, if adding telemetry (N1+N2) to the video-only monitor (V0+V1) does not improve failure-detection AUROC by ≥ 0.02 with a procedure-level 95% bootstrap CI excluding 0, *and* does not reduce AURC with a CI excluding 0, then H1 is rejected and reported as a negative result. C6/C7 are then not pursued.

> *Superseded wording:* the final test is in `research/integrated-study/preregistration.md` §7.1 (v1.1): a superiority test with 0.02 as the smallest effect of interest.

**Pre-experimental kill:** If the Phase 1 targeted search (see `phase1-direction.md`) finds work that already tests C4/C5 against a video-only baseline, Track C is reformulated around the remaining differences or discontinued.

**Decision:** Track C becomes the **primary** programme question (RQ1).

**P1.1 update (2026-11-12):** the targeted search of video analytics, teleoperated driving, semantic communication, V2X and MICCAI 2026 found no occupying study. Residual risk for C4/C5 is lowered to **medium**. The video-only comparator must now include a learned pixel→AI-error predictor (`literature/gap-validation/gap-validation-report.md`).

---

## Cross-track claim hygiene
Programme documents must not make any of the following claims:
- "first" to study packet loss, compression or network effects on surgical AI (Endo-C6, VISTA, generic VA);
- "first" conformal/selective/uncertainty work in surgery (RI12–RI16, RI31, RI34);
- "first" compound-shift or multi-network-factor study (SH17, IX04, NW04, IX01);
- that telemetry-based AI-failure prediction is new in general (C4 is unverified and high-risk);
- clinical safety, safe thresholds or deployment readiness from emulated experiments.
