# MEMORY.md — Persistent Research Context

This file preserves durable project context for researchers and AI-assisted research sessions. It should contain stable decisions and validated context—not transient task lists.

## Project identity

**Repository:** `reliable-surgical-vision`

**Programme:** Reliable Visual Inference Under Distribution Shift for Robot-Assisted and Tele-Robotic Surgery.

## Umbrella question

How can computer-vision systems used in robot-assisted and tele-robotic surgery maintain reliable inference—or safely abstain—when visual, clinical, hardware, and communication conditions differ from those encountered during development?

## Current tracks

### Track A — Compound Shift
Study performance and reliability degradation under individual and compound visual/network-induced shifts.

### Track B — Selective Inference
Study uncertainty, calibration, conformal prediction, selective prediction, and abstention under surgical distribution shift.

### Track C — Network-Aware Inference
Study reliability estimation using both visual evidence and network/system telemetry.

## Key conceptual hypothesis

Network degradation can alter the visual input distribution through compression, frame loss, resolution adaptation, corruption, temporal irregularity, or related mechanisms. Therefore, network state may be relevant to downstream computer-vision reliability.

This is a hypothesis to investigate, not an established project conclusion.

## Research status

The programme is in **Phase 0: Research Foundation**. No paper title, novelty claim, dataset choice, model architecture, or experimental conclusion is final.

## Durable decisions

- One repository contains all three tracks.
- `main` is the canonical research record.
- Tracks are directories rather than long-lived branches.
- Feature/experiment branches are created only for bounded implementation work.
- Literature and dataset reconnaissance precede major experimentation.
- Research tracks may merge, split, change direction, or be abandoned based on evidence.
- Reproducibility, provenance, and negative-result reporting are first-class requirements.

- **P0.2 Surgical Computer-Vision Landscape Reconnaissance completed (2026-09-25).**
- Keep workflow/phase, action/gesture/triplets, detection/keypoints, semantic/instance segmentation, anatomy/scene and skill as distinct task structures.
- Workflow recognition is intrinsically temporal; segmentation/detection provide complementary spatial failure modes.
- Surgical-CV public data are concentrated in laparoscopic cholecystectomy; dataset provenance/overlap must be audited before cross-dataset claims.
- Multicentre HeiChole and PhaKIR show that strong single-centre/i.i.d. scores do not imply cross-centre generalisation.
- Metric implementation/protocol details must be pinned; identical metric names do not guarantee comparable results.
- Phase/workflow recognition and instrument/anatomy segmentation/detection are candidate families only; final selection remains gated by P0.3–P0.7.
- Every completed Phase 0 task should include an `rq-answer-matrix.md`.

- **P0.3 Dataset Reconnaissance completed (2026-09-25).**
- Cross-dataset evaluation is not considered cross-domain until source-video overlap is ruled out.
- CholecT50, CholecSeg8k and CholecInstanceSeg have documented Cholec80 lineage; derived dataset names must never be used as evidence of independent procedures.
- CAMMA explicitly warns of overlap among Cholec80, CholecT50 and Endoscapes; exact video IDs must be resolved before combined experiments.
- Full-video datasets are required for temporal/network degradation; frame-only datasets are used only for visual/spatial corruption unless sequence data are separately available.
- Working core candidates are Cholec80 (temporal), SAR-RARP50 (human robot-assisted), Endoscapes2023 (spatial/anatomy/CVS) and PhaKIR (multicentre temporal+spatial validation).
- HeiChole, HeiCo/ROBUST-MIS, AutoLaparo and MultiBypass140 remain high-value validation candidates; MultiBypass140 is on operational hold until its current archive issue is rechecked.
- Dataset/article/code licences are treated separately; current access/DUA terms must be verified again at download time.
- Final dataset selection remains gated by P0.4–P0.7.

- **P0.4 Distribution-Shift Literature Reconnaissance completed (2026-09-25).**
- Surgical-CV distribution shift is established across centre, recording system, instrument version, procedure/workflow, modality and sim-to-real settings.
- Smoke, bleeding/blood and low-light robustness are already directly benchmarked in surgical tool segmentation; they must not be framed as untouched novelty.
- UDA, DG, strong augmentation, synthetic data, causal vision+kinematics, temporal consistency and foundation-model domain-robustness strategies already exist.
- Natural centre shift is usually compound and should not be interpreted as one causal factor.
- Adjacent GI-endoscopy work provides clinically calibrated corruption severity/compound methodology, but surgical severity values require re-calibration.
- Temporal prediction consistency is not the same as input/network degradation.
- Endo-C6 (2026) provides emerging surgical/endoscopy temporal-VLM evidence including packet-loss bursts; broad packet-loss robustness is therefore not a safe novelty claim.
- The working P0.4 shift set retains natural centre/device/procedure shifts, core visual smoke/blood/low-light, blur/color/compression/resolution, and temporal/compound candidates whose network parameters remain blocked until P0.6.
- Final Track A/C novelty remains gated by P0.6/P0.7.

- **P0.5 Reliable-Inference Literature Reconnaissance completed (2026-09-25).**
- Calibration, uncertainty estimation, OOD detection, prediction-failure monitoring, selective prediction and conformal coverage are treated as distinct concepts throughout the programme.
- In-distribution calibration must not be assumed to survive distribution shift.
- Direct surgical reliability precedents now include FGRM surgical segmentation UQ, calibrated phase confidence, open-set surgical phase recognition, selective surgical VQA, conformal surgical instrument-trajectory forecasting, and recent conformal/temporal surgical segmentation failure monitoring.
- OpenMIBOOD/PhaKIR establishes direct surgical-relevant OOD benchmarking, including smoke covariate shift.
- TCSR-Monitor (2026) creates strong novelty overlap for generic surgical segmentation failure monitoring under acquisition degradation using confidence + temporal/image-quality cues + conformal calibration.
- AI abstention means withholding/defering AI assistance while the surgeon/standard clinical workflow remains in control.
- Vanilla split conformal prediction gives marginal finite-sample coverage under exchangeability; it does not guarantee per-phase, per-centre, per-severity or per-case coverage.
- Class-conditional/Mondrian, importance-weighted and adaptive conformal methods are established but require explicit assumptions/data-access settings.
- P0.5 working baselines favor transparent reliability ladders: max probability/entropy, temperature scaling, ensemble/MC-dropout, explicit failure detection, risk–coverage/AURC, and task-appropriate conformal/risk control.
- Final Track B method and novelty remain gated by P0.6/P0.7.

- **P0.6 Telesurgery / Network Literature Reconnaissance completed (2026-09-26).**
- No universal safe network latency is assumed; one-way/RTT/network/encode-decode/display/total latency definitions remain separate.
- Bandwidth capacity and encoded video bitrate are different variables; required bandwidth is platform/codec/traffic specific.
- Raw packet loss is not equivalent to decoded frame loss, and network jitter is not equivalent to AI-input timing jitter after recovery/buffering.
- Network→video effects are mediated by packetization, FEC/RTX, redundancy, congestion control, encoder adaptation, buffers and decoder concealment.
- Combined latency/bandwidth/jitter/loss effects are already directly studied in telesurgery (Heemeyer 2026), so broad compound-network novelty is unsafe.
- Packet-loss-burst corruption is already present in surgical/endoscopy AI robustness (Endo-C6 2026); broad packet-loss-AI novelty is unsafe.
- Track C is narrowed to whether network/system telemetry adds incremental reliability/failure-prediction or selective-inference value beyond received-video evidence.
- The preferred future design distinguishes decoded-video abstraction from mechanistic network+codec experiments.
- Final task/dataset/shift/reliability/network choice and all novelty claims remain gated by P0.7.

## Update rule

Only add information here when it is expected to remain useful across many future research sessions. Put current actions in `TASK.md` and dated observations in `RESEARCH_LOG.md`.
