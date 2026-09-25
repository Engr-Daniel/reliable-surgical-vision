# P0.4 Distribution-Shift Landscape in Surgical Computer Vision

**Task:** P0.4 — Distribution-Shift Literature Reconnaissance  
**Evidence cutoff:** 2026-09-25  
**Status:** Complete focused evidence-backed reconnaissance

---

## Executive synthesis

Distribution shift is already a mature enough problem in surgical computer vision that the programme cannot plausibly frame its contribution as simply “robustness under distribution shift.”

The retained evidence establishes three strong bodies of prior work:

1. **natural external-domain failure** — cross-centre, cross-device, cross-instrument and cross-procedure performance degradation;
2. **controlled surgical visual corruption** — particularly smoke, bleeding/blood and low illumination;
3. **domain adaptation/generalization methods** — UDA, synthetic diversification, object-centric DG, causal multimodal approaches, photometric augmentation and recent foundation-model strategies.

A fourth body is emerging:

4. **temporal/video corruption** — temporal consistency has long been studied, and recent Endo-C6 work directly includes packet-loss bursts in surgical/endoscopic temporal VLM robustness.

The remaining research opportunity must therefore be narrower than any of these individual components.

---

# 1. Natural distribution shift is empirically established

## 1.1 Procedure and domain gap

ROBUST-MIS remains a foundational benchmark because it was explicitly designed around robustness and generalization. Its three validation stages increase the domain gap between training and evaluation, and the challenge reports degradation as the domain gap grows.

This is stronger evidence than simply observing that one model does poorly on another dataset: the benchmark intentionally structures the external-domain difficulty.

## 1.2 Acquisition system, instrument and surgery type

Kitaguchi et al. provide unusually clean evidence that even apparently small environment changes matter.

Reported mAP / mIoU:

| Test condition | mAP | mIoU |
|---|---:|---:|
| same training conditions | 0.941 | 0.887 |
| different laparoscopic recording system | 0.866 | 0.671 |
| slightly different target forceps | 0.772 | 0.676 |
| different surgery type | 0.588 | 0.395 |

This establishes:
- camera/recording-system shift;
- instrument morphology/version shift;
- procedure/background shift

as distinct practical concerns.

## 1.3 Cross-centre workflow shift

MultiBypass140 provides two-centre gastric-bypass phase/step evaluation. The worst experiments are the direct cross-centre transfers, while multicentre training improves performance.

The correct interpretation is not simply “more data is better.” The centres differ in workflow and surgical technique, so the model encounters a genuine temporal/clinical domain shift.

## 1.4 Cross-centre multi-task shift

PhaKIR is particularly important because poor cross-centre generalization is reported across:
- phase recognition;
- instrument keypoint estimation;
- instrument instance segmentation.

Therefore centre shift is not merely a workflow-classification problem.

## 1.5 Hospital transfer and shortcut features

The 2025 inter-hospital cholecystectomy study shows that training on heterogeneous public data still does not guarantee transfer to a local hospital. Combining/retraining with site-specific data improves performance, and explainability analysis highlights manufacturer-specific instrument dependencies.

This is relevant to the programme because a phase model may use tool appearance as a shortcut for workflow context.

---

# 2. Natural shift is usually compound

A centre label is a proxy for multiple simultaneous changes:

```text
centre
├─ camera / recorder
├─ processing pipeline
├─ instrument vendor/version
├─ surgeon / technique
├─ workflow order
├─ patient/anatomy mix
├─ illumination
└─ local preprocessing / storage
```

This makes multicentre evaluation realistic but limits causal attribution.

For later experiments:
- natural external data should test **ecological generalization**;
- controlled synthetic shifts should test **factor-specific sensitivity**.

Both are needed.

---

# 3. Surgical visual corruption is already directly benchmarked

## 3.1 SegSTRONG-C

SegSTRONG-C directly targets plausible non-adversarial corruption in robot-assisted tool segmentation.

The benchmark includes:
- smoke;
- over-bleeding;
- low brightness.

This has a major implication:

> A proposed paper whose central contribution is simply testing surgical segmentation under smoke, blood and low light would overlap an existing EndoVis challenge.

## 3.2 CaRTS / TC-CaRTS

CaRTS evaluates controlled counterfactual domains including:
- low brightness;
- smoke;
- blood;
- altered background.

CaRTS reports Dice 93.4 on the regular domain and 91.8 on the altered domains, compared with an image-only comparator dropping from 95.0 to 86.7.

This work is also important conceptually: robustness can come from **additional causal/system information** (robot kinematics), not only stronger image features.

TC-CaRTS later adds temporal constraints, showing that temporal observability can improve robustness/convergence.

This is relevant when later evaluating Track C: multimodal reliability is not new in the broad sense, even though **network telemetry** is a different modality from robot kinematics.

---

# 4. Colour and acquisition shortcuts are measurable

Recent 2026 endoscopic-spine work gives unusually direct evidence of inter-institutional colour-domain shift.

A baseline maximum DSC drops from:
- 0.962 internal
to
- 0.784 external.

Aggressive photometric augmentation reaches a peak external DSC of 0.975 in that study, while feature-space analysis supports reduced domain-specific shortcut learning.

A separate deployment-realistic cross-dataset study shows a two-stage foundation model can fail because its **detector**, not its segmentor, is domain limited.

This suggests an important later rule:

> Reliability must be assessed for the complete deployed pipeline, not an oracle component in isolation.

---

# 5. Domain adaptation and domain generalization are established research families

P0.4 identified several already-developed surgical approaches.

## 5.1 UDA
- teacher–student sim-to-real adaptation;
- graph-based domain-common knowledge adaptation.

These approaches use unlabeled target-domain data.

## 5.2 DG / unseen-domain robustness
- object-centric graph representations;
- one-to-many synthetic surgical scene generation;
- photometric augmentation;
- recent single-domain style-normalization work;
- domain-agnostic SAM2/anomaly approaches.

## 5.3 Multimodal / causal robustness
- vision + robot kinematics in CaRTS;
- video + text in SDA-CLIP.

## 5.4 Few-shot transfer
Recent phase-recognition evidence shows performance declines as source/target mismatch increases, even under a few-shot framework.

### P0.4 conclusion
A future contribution cannot claim novelty merely because it uses:
- augmentation;
- UDA;
- DG;
- synthetic data;
- foundation models;
- multimodal input.

Novelty must reside in the exact problem formulation, information available, reliability objective or evidence.

---

# 6. Severity calibration remains uneven

## Surgical-specific protocols

SegSTRONG-C provides plausible surgical corruption classes but not a universally reusable numeric severity ontology.

CaRTS creates discrete counterfactual domains rather than a clinically calibrated continuous severity curve.

## Adjacent GI-endoscopy precedent

Jaspers et al. provide the strongest explicit methodology located for clinically calibrated corruption severity:
- 11 distortion families;
- 10 severity levels;
- clinician-calibrated realistic range;
- compound random corruption sets;
- public generation code.

The study reports an average performance decline of 11.6% ± 1.5 under clinically calibrated degradations, reduced to 7.7% ± 2.03 with stronger model/pretraining strategies.

This protocol is highly useful methodologically, but the calibration was created for GI endoscopy, not surgical operative video.

### Decision

P0.4 adopts the **principle of clinical calibration**, not the numeric parameters.

Any surgical severity scale must be revalidated in the surgical domain.

---

# 7. Temporal robustness is not one concept

P0.4 separates three issues.

## 7.1 Prediction instability

Workflow models can flicker between classes even when the underlying phase has not changed.

Das et al. formally define prediction volatility and show temporal smoothing reduces it.

SurgflowNet later uses consistency learning and unannotated video to improve stable workflow recognition.

These are important reliability issues but they are **model-output instability**, not communication degradation.

## 7.2 Temporal information as robustness

TC-CaRTS demonstrates that temporal constraints can improve segmentation under different domains.

Again, this does not test missing frames or network jitter.

## 7.3 Controlled communication-style video corruption

The 2026 Endo-C6 work changes the landscape.

Its six perturbations include:
- defocus;
- haze;
- motion blur;
- shot noise;
- cautery smoke;
- packet-loss bursts.

This means P0.4 can no longer say that packet-loss corruption is entirely absent from surgical/endoscopic AI robustness research.

But important boundaries remain:
- Endo-C6 is a temporal VLM benchmark;
- it uses a fixed high-severity protocol;
- it does not establish a universal mapping from network packet loss to decoded surgical video;
- it does not answer how standard phase/segmentation reliability/calibration behaves under measured telesurgical network conditions.

That mechanistic mapping is still a P0.6 problem.

---

# 8. Compound shift is partly occupied

## Already established

### Natural compound shift
Multicentre validation changes many factors simultaneously.

### Synthetic compound image corruption
Adjacent endoscopy robustness work already combines multiple distortions.

Therefore:
- “compound shift” is not a novelty claim;
- “multiple corruptions at once” is not a novelty claim.

## Less mature intersection

What remains less established in the retained evidence is a systematic conventional surgical-CV study that crosses:

```text
clinically grounded visual shift
×
mechanistically grounded network/decoded-video shift
×
reliable/selective inference
```

This is **not yet declared novel**.

P0.5, P0.6 and P0.7 must determine whether that intersection is genuinely under-studied.

---

# 9. Working shift set carried forward

## Natural
- centre/institution;
- recording/device;
- procedure/workflow.

## Controlled visual
Core:
- low illumination;
- smoke;
- blood/bleeding.

Extended:
- motion blur;
- defocus;
- colour/white balance;
- compression;
- resolution reduction.

## Temporal/video
Carry as questions, not fixed parameters:
- reduced temporal sampling;
- missing-frame events;
- burst missing frames;
- freeze/duplication;
- irregular timing.

## Compound
- visual + visual;
- natural + controlled;
- visual + temporal/network.

Exact network-derived temporal transformations remain blocked until P0.6.

---

# 10. Implications for the provisional tracks

## Track A — Compound Shift

**Narrowed substantially.**

Broad “compound visual shift” is already occupied.

Potential value may lie in:
- interaction analysis rather than simple corruption averaging;
- visual × network-derived temporal shift;
- natural external domain × controlled temporal degradation;
- reliability rather than predictive performance alone.

No novelty claim yet.

## Track B — Selective Inference

P0.4 strengthens its motivation:
- models can fail substantially under centre/device/procedure/corruption shift;
- clean performance does not reveal deployment risk.

Whether selective/conformal methods handle these shifts is a P0.5 question.

## Track C — Network-Aware Inference

P0.4 provides both support and warning.

Support:
- external system variables can matter;
- kinematics already improve robust robot-tool segmentation;
- packet-loss corruption can affect temporal VLMs.

Warning:
- multimodal robustness is not novel by itself;
- packet-loss robustness is no longer untouched;
- the specific added value of **network telemetry for predicting model unreliability** must survive P0.6/P0.7.

---

# 11. P0.4 scientific conclusion

The evidence is now sufficient to close P0.4.

The programme should stop asking:

> “Does surgical AI fail under distribution shift?”

The answer is already clearly **yes** across multiple tasks and shift mechanisms.

The next scientifically useful questions concern:
- whether model confidence/reliability indicators fail with performance;
- whether abstention/calibration can remain valid;
- how network state maps to decoded visual/temporal degradation;
- whether compound effects are predictable from individual shifts;
- whether network telemetry provides information beyond the visual stream.

Those are exactly the questions P0.5–P0.7 are designed to resolve.
