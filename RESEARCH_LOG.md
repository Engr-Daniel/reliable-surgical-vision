# Research Log

Use dated entries. Record questions, evidence, decisions, failed attempts, unexpected observations, and next actions.

## 2026-09-25 — Repository foundation

### Decision
Created a single research repository with three provisional research tracks rather than three long-lived paper branches.

### Rationale
The tracks share literature, datasets, reliability methods, evaluation infrastructure, and likely code. Their eventual publication boundaries should be determined by evidence rather than repository structure.

### Current state
Phase 0 — Research Foundation.

### Next action
Conduct Toumai technical-literature and architecture reconnaissance.

## 2026-09-25 — P0.2 Surgical Computer-Vision Landscape Reconnaissance completed

### Method
Focused evidence-backed field reconnaissance across peer-reviewed reviews, primary model/dataset papers, EndoVis/MICCAI challenge reports and official benchmark resources. Final audit: 45 records/categories, 33 retained and 12 excluded/deferred.

### Key findings
- The field spans workflow/phase, action/gesture/triplets, instrument presence/detection/keypoints/segmentation, anatomy/scene perception, safety state, skill and emerging video-language models.
- Public benchmarks are heavily concentrated in laparoscopic cholecystectomy; derived datasets may share source procedures.
- Workflow is intrinsically temporal; segmentation/detection provide complementary spatial failure modes.
- HeiChole and PhaKIR show important cross-centre generalisation limitations; PhaKIR reports poor cross-centre generalisability across all three of its tasks.
- ROBUST-MIS explicitly evaluates increasing domain gap and observes degradation.
- Metric implementations/protocols must be pinned; identical metric names do not ensure comparable results.
- Online/high-FPS benchmark capability is not clinical reliability.

### Decision
Phase/workflow recognition and instrument/anatomy segmentation/detection remain credible candidate task families. Final selection is deferred to P0.3–P0.7.

### Status
P0.2 passes its exit criteria. Suggested tag after commit/review: `v0.0.2`.

### Next
P0.3 — Dataset Reconnaissance.

## 2026-09-25 — P0.3 Dataset Reconnaissance completed

### Scope
Audited candidate surgical-video datasets for access, licensing, provenance, overlap, split integrity, annotation structure, temporal/network suitability, natural-shift value and operational feasibility.

### Method
Seeded candidates from P0.2 and re-verified against official dataset/project pages, institutional repositories, peer-reviewed dataset papers, official challenge documentation and live access-status information. The detailed registry contains 18 datasets supported by 36 retained evidence sources.

### Key findings
- Dataset-name diversity can hide source-video reuse. CholecT50 contains 45 Cholec80 videos; CholecSeg8k derives from 17 Cholec80 videos; CholecInstanceSeg combines multiple Cholec80-family sources.
- CAMMA explicitly warns about overlap among Cholec80, CholecT50 and Endoscapes; exact video-ID overlap must be resolved before cross-dataset evaluation.
- CaDIS derives from the CATARACTS training videos and is not an independent external domain.
- Full-video availability is required for later frame-loss/jitter/re-encoding experiments; sparse-frame segmentation sets are primarily visual-corruption resources.
- Multicentre candidates include PhaKIR, HeiChole and MultiBypass140; ROBUST-MIS/HeiCo offers explicit procedure-domain gap.
- SAR-RARP50 provides a comparatively manageable, directly accessible human robot-assisted segmentation/action benchmark.
- Current access terms vary materially: request forms, CC BY-NC-SA, challenge registration, controlled access and PhysioNet DUA.
- MultiBypass140 is scientifically attractive but has a current unresolved archive-integrity issue and a very large storage burden.
- CaDIS' official page currently does not expose a live download link.

### Working shortlist
Development/core candidates: Cholec80, SAR-RARP50, Endoscapes2023, PhaKIR.

High-value validation candidates: HeiChole, HeiCo/ROBUST-MIS, AutoLaparo, MultiBypass140 when operationally available.

### Decision
No final Phase 1 dataset is selected. P0.4–P0.7 remain mandatory gates.

### Status
P0.3 passes its exit criteria.

### Suggested milestone
`v0.0.3 — Dataset Feasibility Map`

### Next
P0.4 — Distribution-Shift Literature Reconnaissance.

## 2026-09-25 — P0.4 Distribution-Shift Literature Reconnaissance completed

### Scope
Mapped natural surgical-CV domain shift, controlled non-adversarial corruption, temporal/video robustness, compound shift, and representative UDA/DG/robustness methods.

### Method
Focused evidence reconnaissance across peer-reviewed multicentre/generalization studies, robustness challenges, surgical UDA/DG work, recent 2026 external-validation studies, and current accepted/preprint evidence where it materially changed the landscape. Final audit: 25 retained sources/resources and 10 excluded/deferred categories.

### Key findings
- Cross-centre, recording-system, instrument-version and procedure/workflow shifts are already directly demonstrated in surgical CV.
- ROBUST-MIS, MultiBypass140 and PhaKIR provide structured evidence that performance degrades as natural domain gap increases.
- SegSTRONG-C directly benchmarks surgical smoke, over-bleeding and low-brightness corruption for robot-tool segmentation.
- CaRTS/TC-CaRTS already combine visual evidence with robot kinematics for robust segmentation under counterfactual surgical visual domains.
- UDA, DG, synthetic diversification, photometric augmentation, object-centric models, video-text adaptation and foundation-model strategies are established method families.
- Adjacent GI-endoscopy work provides a strong clinically calibrated severity/compound-corruption methodology, but its numeric severity values cannot be assumed valid for surgery.
- Temporal prediction volatility/consistency is established; controlled conventional surgical-CV frame-loss/jitter benchmarks remain sparse.
- Endo-C6 (2026) materially narrows the gap by explicitly including packet-loss bursts in a temporal surgical/endoscopy VLM corruption benchmark.
- Therefore neither broad “compound shift” nor broad “packet-loss robustness” can be treated as untouched territory.

### Track implications
- Track A is narrowed from generic compound shift toward interaction-aware, mechanistically grounded visual × temporal/network reliability.
- Track B gains stronger motivation but requires P0.5 method/assumption review.
- Track C remains plausible, but multimodal robustness and packet-loss corruption precedents mean network telemetry must show added reliability value beyond received-video evidence.

### Decision
P0.4 passes its exit criteria. No final novelty claim is made.

### Suggested milestone
`v0.0.4 — Distribution-Shift Evidence Map`

### Next
P0.5 — Reliable-Inference Literature Reconnaissance.

## 2026-09-25 — P0.5 Reliable-Inference Literature Reconnaissance completed

### Scope
Mapped calibration, uncertainty quantification, OOD/open-set detection, prediction-failure monitoring, selective prediction/abstention, conformal prediction and risk control for surgical/medical visual inference.

### Method
Focused evidence reconnaissance across direct surgical reliability papers, medical-imaging UQ/segmentation literature, clinical conformal/selective work under shift, and foundational reliability methodology. Final audit: 36 retained sources/resources and 12 excluded/deferred categories.

### Key findings
- Calibration, uncertainty, OOD detection, failure prediction, selective prediction and conformal coverage are distinct reliability questions.
- In-distribution calibration cannot be assumed to survive the P0.4 distribution shifts.
- Direct surgical UQ/calibration already includes FGRM scene-segmentation uncertainty, calibrated phase confidence, surgical VQA uncertainty decomposition and emerging phase-diffusion uncertainty.
- OpenMIBOOD includes a PhaKIR benchmark with smoke covariate shift plus near/far OOD; direct open-set surgical phase recognition also exists.
- Selective prediction is established in classification and increasingly mature in medical segmentation through post-hoc image-level confidence, Soft Dice Confidence and pixel-level learning-to-abstain.
- Direct surgical conformal evidence exists in MICCAI 2025 instrument-trajectory forecasting.
- Recent TCSR-Monitor work directly targets confident surgical segmentation failures under acquisition degradation using confidence, geometry, temporal consistency, image-quality cues and Mondrian conformal calibration.
- TCSR-Monitor's strong within-corruption failure AUROC does not eliminate operational false alarms, reinforcing the need to evaluate monitors as decision systems rather than scores.
- Vanilla split conformal coverage is marginal and depends on exchangeability; recent medical evidence shows class imbalance, distribution shift and limited calibration size can produce practically poor subgroup/conditional behavior.
- Weighted, class-conditional/Mondrian and adaptive conformal variants already exist; their assumptions and target-data access must be explicit.

### Track implications
- Track B remains motivated but broad novelty around uncertainty, calibration, OOD, abstention or surgical conformal prediction is no longer defensible.
- A narrower question remains: how reliability mechanisms themselves degrade under natural, visual and mechanistically grounded network/video shifts, and whether selective/conformal behavior remains useful.
- TCSR-Monitor creates strong overlap pressure for a generic corrupted-surgical-segmentation failure-monitor paper.
- P0.6 is now critical for determining whether network telemetry adds information beyond received-video/temporal failure signals.

### Decision
P0.5 passes its exit criteria. No final reliability method or novelty claim is fixed.

### Suggested milestone
`v0.0.5 — Reliable-Inference Evidence Map`

### Next
P0.6 — Telesurgery / Network Literature Reconnaissance.

