# P0.5 Reliable-Inference Landscape for Surgical Vision

**Task:** P0.5 — Reliable-Inference Literature Reconnaissance  
**Evidence cutoff:** 2026-09-25  
**Status:** Complete focused evidence-backed reconnaissance

---

## Executive synthesis

P0.5 substantially narrows Track B.

Reliable inference in surgical/medical AI is no longer an open field waiting for a first application of uncertainty, calibration, OOD detection, abstention, or conformal prediction.

Direct surgical evidence now includes:
- calibrated confidence for phase recognition;
- uncertainty-aware surgical scene segmentation;
- open-set surgical phase recognition;
- calibrated selective surgical VQA;
- conformal surgical instrument-trajectory forecasting;
- a recent conformal/temporal surgical segmentation failure monitor under acquisition degradation.

Medical-imaging evidence is even more mature:
- calibration and predictive uncertainty for segmentation;
- failure and OOD detection;
- selective semantic segmentation under shift;
- image-level and pixel-level abstention;
- conformal segmentation and risk control.

Therefore Track B cannot be framed as:

> “Apply uncertainty / conformal prediction / abstention to surgical AI.”

The potentially useful contribution is narrower:

> **Evaluate whether reliability mechanisms themselves remain trustworthy across the explicit natural, visual, and network-derived shifts identified by the programme, and whether abstention/coverage behavior remains clinically/operationally useful when the model is confidently wrong.**

---

# 1. Reliable inference is not one problem

P0.5 separates six questions.

## 1.1 Calibration
Are predicted probabilities statistically aligned with observed correctness?

## 1.2 Uncertainty estimation
Does the model produce a useful uncertainty score/distribution?

## 1.3 OOD/open-set detection
Does the input appear outside the development distribution or label set?

## 1.4 Failure prediction
Is the current prediction likely to be wrong or below a quality threshold?

## 1.5 Selective prediction
Should the AI output be accepted or withheld?

## 1.6 Conformal/risk control
Can a set/interval/structured output satisfy a predeclared coverage or risk target under explicit assumptions?

These are complementary. None is a synonym for “reliability.”

---

# 2. Calibration under distribution shift is a central risk

Temperature scaling is a useful baseline because it is simple and often effective in-distribution.

But Ovadia et al. establish the core warning for this programme: uncertainty quality and calibration can deteriorate as the deployment distribution moves away from training, and ordinary post-hoc calibration need not remain adequate.

P0.4 already established surgical shifts in:
- centre;
- recording system;
- instruments;
- procedure;
- smoke/blood/illumination;
- temporal/video degradation.

P0.5 therefore treats calibration as **shift-specific evidence**, not a once-and-done preprocessing step.

For surgical phase recognition, the 2024 calibrated-confidence study confirms that probability calibration already has direct surgical use.

---

# 3. Surgical segmentation UQ is already direct research territory

FGRM (NeurIPS 2023) is especially important.

It directly targets:
- surgical scene segmentation;
- uncertainty estimation;
- calibration of prediction risk;
- real-time one-pass inference.

This means a future Track B contribution cannot claim novelty merely because it adds uncertainty maps to surgical segmentation.

The research question must concern:
- shift behavior;
- failure detection;
- abstention;
- formal risk/coverage;
- multimodal/system context;
or another narrower gap.

---

# 4. OOD detection is already surgical-relevant

OpenMIBOOD (CVPR 2025) includes a PhaKIR endoscopy benchmark.

Its PhaKIR setting explicitly distinguishes:
- ID;
- smoke-based covariate-shifted ID;
- near-OOD surgical/endoscopic datasets;
- far-OOD datasets.

It evaluates 24 post-hoc OOD methods and finds that method rankings from natural-image benchmarks do not simply carry over to medical imaging.

This removes another overly broad novelty claim:

> “Use OOD detection for surgical video”

is already occupied.

P0.7 must distinguish **OOD detection** from the more operational question **“will the current surgical model output fail?”**

---

# 5. Direct surgical failure monitoring now exists

The August 2026 TCSR-Monitor work is highly relevant.

It targets surgical instrument-segmentation failures under acquisition degradation and explicitly argues that confidence/entropy can miss **confident failures**.

Its monitor combines:
- model confidence;
- mask geometry;
- temporal consistency;
- image quality.

It also includes:
- leave-one-corruption-out generalization;
- a circularity control to distinguish failure detection from mere corruption detection;
- Mondrian conformal calibration across degradation severities.

Reported within corrupted frames:
- TCSR failure AUROC: 0.946;
- entropy failure AUROC: 0.594.

But the work also documents an important operational limitation: a global threshold can false-alarm on roughly 40% of correctly segmented frames at a moderate corruption severity.

This is exactly the kind of result P0.5 wants to preserve:
high discrimination does not automatically imply a practical alarm system.

### Track consequence
A Track B paper about “failure monitoring for corrupted surgical segmentation using uncertainty + temporal features + conformal calibration” would now overlap heavily with this recent work.

---

# 6. Selective prediction is mature enough to demand task-specific design

Classification reject options and SelectiveNet established the risk–coverage framework.

Medical segmentation now has:
- post-hoc selective prediction under distribution shift;
- Soft Dice Confidence for image-level abstention;
- explicit pixel-level learning-to-abstain methods.

Direct surgical VQA includes selective answering.

Therefore “let the model abstain when uncertain” is also not a sufficient contribution.

The unresolved design issue is **what unit should abstain**.

## Phase recognition
Possible:
- frame;
- temporal segment;
- transition.

## Segmentation
Possible:
- whole frame;
- instrument instance;
- region;
- pixel.

A pixel-level rejection mask may be mathematically attractive but operationally confusing in a surgical overlay. A frame-level abstention is simpler to audit but can be overly coarse.

P0.5 leaves this choice open for P0.7.

---

# 7. Conformal prediction has direct surgical precedent

P0.5 found direct surgical CP evidence:

## Conformal surgical instrument trajectory forecasting
MICCAI 2025 applies standard CP and conformalized quantile regression to surgical instrument motion forecasting, evaluating interval coverage and size.

## TCSR-Monitor
Recent surgical segmentation failure monitoring uses Mondrian conformal calibration across degradation severities.

Thus the broad statement:

> “Conformal prediction has not been applied in surgical guidance”

is no longer safe as a programme-level novelty claim.

However, P0.5 did not establish a mature literature for **conformal phase-label prediction sets or conformal instrument/anatomy segmentation reliability systematically evaluated across the exact P0.4 + P0.6 shift suite**.

That narrower intersection remains for P0.7.

---

# 8. Conformal guarantees need careful interpretation

The most important methodological conclusion is:

> **A conformal guarantee is only meaningful when the guarantee, prediction unit, calibration regime, and shift assumptions are stated.**

Vanilla split CP gives marginal coverage under exchangeability.

It does not guarantee:
- each surgical phase is covered;
- every centre is covered;
- every shift severity is covered;
- an individual prediction has the nominal probability of being correct.

Recent medical evidence demonstrates why this matters.

## Class imbalance + shift
In the 2026 multiple-sclerosis MRI study, marginal CP under 1.5T shift showed:
- MS-class coverage: 16.9%;
- control coverage: 95.2%.

Class-conditional CP improved MS coverage to 77.5%, still demonstrating that severe shift can challenge nominal behavior.

## Calibration-set size
The 2026 critical perspective on medical CP emphasizes that standard marginal theory can coexist with substantial one-time calibration-set-conditional variability when the calibration set is small.

### Surgical implication
Rare phases + limited independent procedures make repeated calibration splits and per-phase coverage essential.

---

# 9. Shift-aware conformal methods already exist

If exchangeability is broken, P0.5 identifies established routes:

- importance-weighted CP under covariate shift;
- adaptive conformal inference under changing online distributions;
- Mondrian/class-conditional CP for class/group coverage;
- risk-controlling prediction sets for non-classification losses.

But these are not free fixes.

Weighted CP needs:
- a defensible covariate-shift model;
- target covariates/density-ratio estimation.

Adaptive CP changes the guarantee to an online long-run notion.

Mondrian CP fragments the calibration sample.

Therefore P0.7 must choose methods according to information available at deployment, not according to which one rescues test-set coverage best.

---

# 10. Track B novelty stress-test

## Broad claim 1
**“Surgical AI needs uncertainty estimation.”**

Not novel. FGRM and other direct surgical work already establish this.

## Broad claim 2
**“Calibrate confidence in surgical phase recognition.”**

Not novel. Direct calibrated phase recognition exists.

## Broad claim 3
**“Detect unknown surgical phases/OOD.”**

Not novel. Open-set surgical phase work and OpenMIBOOD/PhaKIR exist.

## Broad claim 4
**“Allow surgical AI to abstain.”**

Too broad. Direct surgical selective answering and medical selective segmentation exist.

## Broad claim 5
**“Use conformal prediction in surgery.”**

Not novel. Surgical instrument trajectory CP and recent TCSR conformal calibration exist.

## Narrower unresolved intersection

The retained evidence does **not** establish a saturated literature at this exact intersection:

```text
standard surgical phase/segmentation task
×
explicit P0.4 natural + visual shifts
×
P0.6 mechanistically grounded network/video shift
×
calibration + failure prediction + selective/conformal behavior
×
procedure-level external evaluation
```

This remains **unresolved, not declared novel**.

---

# 11. Best methodological direction after P0.5

Instead of proposing one exotic UQ model first, the programme should initially compare a transparent reliability ladder.

## Simple
- max probability / entropy;
- temperature scaling.

## Strong standard UQ
- deep ensemble or MC dropout.

## Task-aware
- phase-specific classwise calibration;
- Soft Dice/task-quality confidence for segmentation;
- direct failure-risk monitor.

## Formal risk/coverage
- APS/RAPS or class-conditional conformal for phase;
- structured/risk-control conformal method for segmentation.

Then ask:

> **Which methods fail first, and how, as the shift becomes more deployment-realistic?**

That question is scientifically stronger than “which uncertainty method has the best clean ECE?”

---

# 12. P0.5 conclusion

P0.5 can be closed.

The evidence strongly supports studying reliable/selective inference under surgical distribution shift, but it eliminates broad novelty claims around:
- uncertainty estimation;
- calibration;
- OOD/open-set detection;
- abstention;
- conformal prediction.

The potentially valuable contribution now lies in **failure-aware reliability under the specific compound natural/visual/network conditions identified by the programme, with explicit assumptions and operational abstention semantics**.

P0.6 must now determine what “network-induced” means physically and computationally before P0.7 can decide whether Tracks A–C should remain separate or converge.
