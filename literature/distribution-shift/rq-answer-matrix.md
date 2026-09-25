# P0.4 Research Question Answer Matrix

This file is the concise traceability layer between the Phase 0 specification and the P0.4 evidence artifacts.

---

## RQ1 — What distribution shifts are documented in surgical computer vision?

### Answer
The literature supports a broad taxonomy:

- **natural shift:** institution/centre, recording system, instrument version/vendor, procedure/workflow, patient/anatomy, calendar cohort and imaging modality;
- **source-generation shift:** simulation/VR/ex-vivo/porcine → clinical;
- **controlled visual shift:** illumination, smoke, blood/bleeding, blur, colour/white balance, compression/resolution, noise, haze, background/style and optical obstruction;
- **temporal/video shift:** temporal instability and context effects are established; direct controlled frame-loss/jitter evidence is much thinner, with recent Endo-C6 providing an important packet-loss-burst exception for temporal VLMs;
- **compound shift:** naturally present in multicentre evaluation and already used in synthetic image-corruption methodology.

### Evidence
SH01–SH05, SH07–SH12, SH17–SH18, SH25.

### Detailed artifacts
`shift-taxonomy.md`, `natural-shift-map.csv`, `synthetic-corruption-map.csv`, `temporal-video-shift-map.csv`.

---

## RQ2 — How are natural shifts operationalized and measured?

### Answer
The strongest designs hold out a real centre, device, procedure or external cohort and evaluate a fixed model on that independent domain.

Examples:
- ROBUST-MIS: staged increasing procedure/domain gap;
- Kitaguchi: controlled changes to recorder, instrument and surgery type;
- MultiBypass140: two-centre train/test permutations;
- PhaKIR: three-centre multi-task challenge;
- inter-hospital phase transfer: public multicentre training → local hospital test;
- recent spine studies: internal, temporal-external and cross-dataset external tests.

Natural centre shifts are usually **compound** and should not be interpreted as one causal variable.

### Evidence
SH01–SH08.

### Detailed artifact
`natural-shift-map.csv`.

---

## RQ3 — What controlled corruptions and severity protocols exist?

### Answer
Direct surgical precedent is strongest for:
- smoke;
- bleeding/blood;
- low brightness;
- altered background.

SegSTRONG-C provides photo-realistic smoke, over-bleeding and low-brightness robot-tool segmentation benchmarks. CaRTS uses controlled counterfactual low-brightness, smoke, blood and background changes.

Recent Endo-C6 expands surgical/endoscopic video robustness to defocus, haze, motion blur, shot noise, cautery smoke and packet-loss bursts.

The strongest explicit severity-calibration methodology found is adjacent GI endoscopy: Jaspers et al. evaluate 11 distortion types across 10 severity levels with clinical calibration. This is methodological precedent, not a validated surgical severity scale.

### Evidence
SH09–SH10, SH17–SH19.

### Detailed artifacts
`synthetic-corruption-map.csv`, `evaluation-practices.md`.

---

## RQ4 — Which tasks and datasets have been evaluated under shift?

### Answer
Shift evaluation is no longer restricted to one task.

Evidence exists for:
- instrument binary/instance segmentation — ROBUST-MIS, SegSTRONG-C, EndoVis-derived UDA/DG studies;
- instrument keypoints — PhaKIR / ROBUST-MIPS;
- phase/step recognition — MultiBypass140, inter-hospital transfer, few-shot transfer;
- action recognition — SurgVisDom / SDA-CLIP;
- surgical scene segmentation — multicentre/unseen-domain DG studies;
- temporal VLMs — Endo-C6;
- robotic tool segmentation with kinematics — CaRTS/TC-CaRTS.

Therefore “surgical CV under distribution shift” is already an established research area. A contribution must be defined at a narrower intersection.

### Evidence
SH01, SH03–SH05, SH09–SH18, SH22–SH24.

### Detailed artifact
`distribution-shift-literature-map.csv`.

---

## RQ5 — Which mitigation strategies are established?

### Answer
Established families include:

- multicentre/diverse training;
- site-specific retraining/fine-tuning;
- photometric/strong augmentation;
- synthetic data generation;
- UDA (teacher–student, feature/graph alignment);
- DG / single-domain DG;
- object-centric representations;
- causal multimodal vision + robot kinematics;
- temporal constraints and consistency learning;
- foundation-model/domain-agnostic pipelines;
- few-shot adaptation;
- video-text adaptation.

This means P0.7 should not frame ordinary augmentation, UDA or DG as novel by itself.

### Evidence
SH03, SH05–SH08, SH10–SH16, SH20–SH24.

### Detailed artifact
`method-baseline-map.csv`.

---

## RQ6 — How should shifted performance be evaluated?

### Answer
At minimum:

- clean/source-domain score;
- shifted/target score;
- absolute degradation;
- relative retention;
- per-shift/per-centre results;
- severity curves for controlled corruptions;
- worst-case reporting;
- procedure-level confidence intervals or repeated seeds;
- explicit disclosure of whether target-domain data were used.

For temporal tasks, add segmental/consistency/recovery metrics rather than relying only on framewise accuracy.

Robustness and clean accuracy should be reported separately.

### Evidence
SH01–SH05, SH09, SH17–SH21.

### Detailed artifacts
`evaluation-practices.md`, `quantitative-evidence.csv`.

---

## RQ7 — What evidence exists for temporal/video degradation and compound shift?

### Answer
Three levels must be distinguished:

1. **temporal prediction consistency** is well established as a problem in workflow/video models;
2. **controlled packet-loss-like video corruption** now has emerging direct precedent in Endo-C6 for temporal VLMs;
3. a mature conventional surgical phase/segmentation benchmark systematically crossing realistic visual severity with network/decoder temporal severity was **not established** by the retained P0.4 evidence.

Compound natural shift is common in multicentre testing, and compound synthetic image corruption has adjacent endoscopy precedent. Therefore neither “temporal robustness” nor “compound corruption” can be claimed broadly as new.

### Evidence
SH03–SH05, SH11, SH17–SH21.

### Detailed artifacts
`temporal-video-shift-map.csv`, `compound-shift-evidence.md`.

---

## RQ8 — Which shift set should be carried forward?

### Answer
The working set is intentionally tiered:

### Natural
- centre/institution;
- device/recording system;
- procedure/workflow.

### Controlled visual
- low brightness;
- smoke;
- blood/bleeding;
- motion blur;
- defocus;
- colour/white-balance;
- compression;
- resolution reduction.

### Temporal/video — pending P0.6 parameterization
- reduced sampling/context;
- missing-frame events;
- burst loss/freeze;
- irregular timing.

### Compound — pending P0.6/P0.7
- visual + visual;
- natural + controlled;
- visual + temporal/network.

No exact network-derived corruption parameter is fixed in P0.4.

### Detailed artifact
`candidate-shift-protocol.md`.

---

# P0.4 Overall Conclusion

Distribution shift in surgical CV is already an established problem with direct evidence for cross-centre failure, cross-device/procedure failure and clinically plausible visual corruption.

The remaining opportunity must be formulated more narrowly than:

> “make surgical AI robust to distribution shift.”

In particular, smoke/blood/low-light robustness, ordinary UDA/DG, and compound image corruption already have clear precedents.

The potentially less-saturated intersection involving **standard surgical-CV tasks, reliable/selective inference, and defensibly network-induced temporal/video shift** remains unresolved and must be tested by P0.5–P0.7 before any novelty claim.
