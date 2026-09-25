# P0.4 Distribution-Shift Taxonomy for Surgical Computer Vision

## Core definition

For this programme, **distribution shift** means that the joint distribution encountered at evaluation/deployment differs materially from the development distribution.

A useful abstraction is:

`development domain D_s → changed acquisition/clinical/system process → deployment domain D_t`

The change may affect `P(X)`, `P(Y)`, or the relationship `P(Y|X)`. P0.4 does not assume every observed performance drop is pure covariate shift.

---

## A. Natural shifts

### A1 — Institution / centre
Examples:
- different hospitals;
- different operating rooms;
- different local protocols;
- different surgeons and teams;
- different image-processing defaults.

**Evidence:** MultiBypass140, PhaKIR, inter-hospital phase transfer, endoscopic-spine external cohorts.

**Important:** centre shift is usually a **compound natural shift**, not a single causal factor.

### A2 — Acquisition device / recording system
Examples:
- laparoscopic stack manufacturer/model;
- camera sensor/endoscope;
- video processor;
- acquisition settings.

Kitaguchi et al. directly demonstrate reduced instrument-segmentation performance under a different laparoscopic recording system.

### A3 — Instrument morphology / manufacturer / version
Changes in tool design or manufacturer-specific appearance can break learned shortcuts.

Evidence includes Kitaguchi et al. and manufacturer-specific instrument dependencies observed in the inter-hospital phase-transfer study.

### A4 — Procedure / workflow
Examples:
- training on one surgical procedure and testing another;
- centre-specific ordering/technique;
- different phase/step execution.

ROBUST-MIS and MultiBypass140 provide explicit procedure/workflow domain-gap evidence.

### A5 — Patient / anatomy / pathology
Different anatomy, tissue appearance, pathology and demographics can alter visual distributions.

Often confounded with centre/procedure shift because public surgical datasets expose limited patient metadata.

### A6 — Temporal / calendar drift
A later cohort may differ due to:
- equipment upgrades;
- practice change;
- surgeon experience;
- new instruments;
- acquisition pipelines.

Recent endoscopic-spine work explicitly separates internal, temporal external and cross-dataset external testing.

### A7 — Modality / platform
Examples:
- robotic vs conventional laparoscopy;
- cataract microscope vs laparoscope;
- RGB endoscopy vs OCT;
- biportal vs uniportal endoscopy.

This can be an intentionally large shift and may also change label semantics.

### A8 — Simulation / VR / ex-vivo → clinical
A distinct adaptation setting:
- synthetic/VR source;
- real clinical target.

Sahu et al., SDA-CLIP and CaRTS-family work show that this is already an established surgical research direction.

---

## B. Controlled visual corruptions

### B1 — Illumination / exposure
- low brightness;
- overexposure;
- brightness/gamma changes;
- uneven illumination.

Direct surgical precedent: SegSTRONG-C low brightness; CaRTS counterfactual low brightness.

### B2 — Smoke / haze / medium
- cautery smoke;
- smoke plume;
- haze/fluid-induced visibility reduction.

Direct surgical precedent: SegSTRONG-C, CaRTS/TC-CaRTS; emerging Endo-C6.

### B3 — Blood / bleeding / occlusion
- blood on tissue/instrument;
- over-bleeding;
- partial occlusion.

Direct surgical precedent: SegSTRONG-C, CaRTS; real-data hard cases are documented in CholecInstanceSeg.

### B4 — Blur
- motion blur;
- defocus;
- local defocus/lens blur.

Clinically motivated and directly relevant to moving endoscopes. Endo-C6 includes motion blur/defocus; adjacent endoscopy robustness literature calibrates blur severity.

### B5 — Color / white balance / contrast
- color shift;
- saturation;
- hue;
- contrast;
- white balance.

Recent endoscopic-spine evidence directly shows inter-institutional color shift and shortcut learning.

### B6 — Resolution / sampling
- downscaling;
- pixelation;
- spatial sampling changes.

Relevant to video pipelines, but network causality should not be assumed until P0.6.

### B7 — Compression
- JPEG / JPEG2000 for image-level protocols;
- video codec/bitrate artifacts require P0.6.

Adjacent endoscopy evidence shows compression can materially affect model performance and provides calibrated methodology.

### B8 — Noise
- sensor/shot noise;
- additive noise.

Endo-C6 includes shot noise. Surgical-specific severity calibration remains limited.

### B9 — Reflection / lens contamination / obstruction
- specular reflection;
- attached tissue;
- lens dirtiness;
- liquid;
- camera partially in port.

These are observed real surgical hard cases but are less standardized as controlled robustness benchmarks.

### B10 — Background/style alteration
Controlled counterfactual background change appears in CaRTS and synthetic/DG methods.

---

## C. Temporal / video shifts

### C1 — Reduced sampling rate
Subsampling is widespread as preprocessing in surgical workflow models.

**Caution:** routine 1-fps preprocessing is not evidence of robustness to accidental frame loss.

### C2 — Frame loss
Missing decoded frames or dropped observations.

Direct conventional surgical-CV evidence remains sparse in the retained literature.

### C3 — Burst frame loss / packet-loss-derived corruption
Endo-C6 (2026) is an important emerging exception: packet-loss bursts are explicitly included in a temporal surgical/endoscopy VLM benchmark.

**Caution:** packet loss at network level can result in different decoded-video effects depending on codec, GOP, transport recovery and buffering. P0.6 must define the mapping.

### C4 — Freeze / duplication
Repeated last-good frame after missing delivery or buffering.

P0.4 found no mature standardized surgical benchmark for this in conventional phase/segmentation tasks.

### C5 — Irregular inter-frame timing / jitter-inspired delivery
A plausible telesurgical shift, but a standardized surgical-CV protocol was not established by the retained P0.4 literature.

### C6 — Context truncation / temporal discontinuity
Relevant to phase/action models and long-video VLMs.

Temporal consistency and prediction-volatility papers show the importance of temporal context but are not direct network-degradation experiments.

### C7 — Reordering
Potential network phenomenon, but decoded video commonly hides/handles transport-level reordering. Must not be simulated without P0.6 evidence.

---

## D. Compound shift

### D1 — Natural compound shift
A hospital change may simultaneously alter:
- camera;
- illumination;
- workflow;
- instrument set;
- surgeon;
- patient mix;
- preprocessing.

PhaKIR/MultiBypass/HeiChole-style cross-centre evaluation therefore measures an aggregate shift unless factors are separately controlled.

### D2 — Synthetic compound visual corruption
Adjacent endoscopy work by Jaspers et al. applies random combinations of multiple clinically calibrated distortions.

Therefore **compound corruption as a general idea is not novel**.

### D3 — Controlled visual + temporal/network compound shift
The retained surgical evidence is much thinner here.

Endo-C6 includes both visual and packet-loss corruption types in the same benchmark taxonomy, but P0.4 does not establish a mature conventional surgical-CV benchmark systematically crossing visual severity with network/temporal severity.

This remains a question for P0.6/P0.7, **not a novelty claim**.

---

## E. Shift-setting terminology

### Domain adaptation (DA)
Target-domain data are available during adaptation.
- supervised DA;
- semi-supervised DA;
- unsupervised DA.

### Domain generalization (DG)
Target domain is unseen during training.

### Single-domain generalization (SDG)
Only one labeled source domain is assumed.

### Corruption robustness
A clean test sample is transformed by a defined corruption operator.

### Natural external validation
Real data from another centre/time/procedure/device are evaluated without synthetic transformation.

### OOD detection
Determining whether an input lies outside a training/development distribution. Detailed reliable-inference review is deferred to P0.5.

---

# Taxonomy decision

Later experiments must always record:

`shift_source`, `shift_mechanism`, `natural_or_controlled`, `severity`, `task`, `source_domain`, `target_domain`, `temporal_structure`, and `whether_target_data_were_used_for_adaptation`.

A single label such as “OOD” is insufficient.
