# P0.5 Reliable-Inference Taxonomy

P0.5 uses **reliable inference** as an umbrella term for methods that estimate, communicate, detect, or act on the possibility that a model output is unreliable.

These concepts are related but **not interchangeable**.

## 1. Predictive confidence

A scalar or vector derived from a model's output, such as maximum softmax probability.

Example:

`confidence(x) = max_k p(y=k | x)`

A high confidence score does **not** guarantee correctness and can remain high under shift.

**Use:** baseline ranking signal.  
**Do not interpret as:** calibrated probability, epistemic uncertainty, OOD status, or guarantee.

---

## 2. Calibration

A classifier is calibrated when predictions assigned confidence `q` are correct approximately fraction `q` of the time, under the distribution being evaluated.

### Types relevant here
- global/marginal calibration;
- class-conditional calibration;
- subgroup/domain calibration;
- pixel calibration;
- image-level segmentation calibration.

### Typical methods
- temperature scaling;
- Platt scaling;
- isotonic regression;
- vector/Dirichlet calibration;
- calibration-aware training.

### Key P0.5 lesson
**In-distribution calibration does not imply calibration after distribution shift.**

Ovadia et al. show uncertainty/calibration can deteriorate as shift severity increases. Surgical P0.4 shifts must therefore be treated as new reliability evaluation domains rather than assuming one calibration fit remains valid.

---

## 3. Predictive uncertainty

A score/distribution expressing uncertainty about the prediction.

### Epistemic uncertainty
Uncertainty associated with limited model knowledge.

Representative approximations:
- MC dropout;
- deep ensembles;
- Bayesian neural networks;
- evidential models.

### Aleatoric uncertainty
Uncertainty associated with ambiguity/noise in the observation or label-generating process.

In surgery, examples can include:
- smoke/occlusion;
- ambiguous phase-transition frames;
- indistinguishable tissue boundaries.

**Caution:** the epistemic/aleatoric distinction is conceptually useful but practical estimates are method-dependent and need not cleanly separate causal sources.

---

## 4. Prediction error / failure detection

Question:

> **Is this specific prediction likely to be wrong or below an acceptable quality threshold?**

Examples:
- classify a phase prediction as likely correct/incorrect;
- predict whether segmentation IoU will fall below 0.75;
- estimate expected Dice.

This is closer to operational safety than generic OOD detection.

TCSR-Monitor is direct surgical evidence: it monitors segmentation failure using confidence, geometry, temporal consistency and image-quality cues.

---

## 5. OOD detection

Question:

> **Does this input appear outside the development distribution?**

OOD detection can be useful, but:

- an OOD sample can still be predicted correctly;
- an ID sample can still be predicted wrongly;
- detecting image corruption is not the same as detecting model failure.

OpenMIBOOD directly establishes this as a surgical-relevant benchmark through PhaKIR.

### Related terms
- covariate-shifted ID (cs-ID);
- near-OOD;
- far-OOD;
- open-set recognition.

---

## 6. Open-set recognition

The classifier is expected to recognize known classes while identifying inputs/classes not represented in the closed training label set.

Direct surgical precedent now exists for phase recognition (Geyer et al., 2026).

Open-set phase recognition is distinct from:
- same-phase-label prediction under a camera shift;
- failure detection under smoke;
- confidence calibration.

---

## 7. Selective prediction / rejection / abstention

The model uses a **selection policy**:

`predict if confidence/risk is acceptable; otherwise abstain/defer`

### Core quantities
- **coverage:** fraction of cases accepted;
- **selective risk:** error/loss among accepted cases;
- **risk–coverage curve:** selective risk as coverage changes;
- **AURC:** area under the risk–coverage curve.

### Surgical interpretation
Abstention means:

> **the AI withholds or defers its guidance/output; the surgeon and standard clinical workflow remain in control.**

It does **not** mean the surgery should stop.

### Granularity choices
- frame-level;
- temporal segment;
- video/procedure;
- whole segmentation image;
- object/instance;
- pixel/region.

The right granularity is task-specific.

---

## 8. Conformal prediction (CP)

Conformal prediction wraps a model using held-out calibration data to create:
- label sets;
- prediction intervals;
- structured prediction sets;
- risk-controlling outputs.

### Vanilla split CP
Provides finite-sample **marginal coverage** under exchangeability of calibration and test data.

For classification:

`P(Y_test ∈ C(X_test)) ≥ 1 - α`

### Important boundaries
This does **not** mean:
- each individual prediction has `1-α` correctness probability;
- every class/group/domain has `1-α` coverage;
- the guarantee automatically survives arbitrary distribution shift.

### Shift-aware variants
- importance-weighted conformal prediction for covariate shift;
- adaptive conformal inference for changing online distributions;
- Mondrian/class-conditional CP for group/class-specific calibration;
- risk-controlling prediction sets for general losses.

---

## 9. Conformal risk control

For structured outputs, exact set membership may be less useful than controlling a task loss.

Examples:
- segmentation IoU/coverage risk;
- false-negative risk;
- hierarchical/multilabel loss.

Risk-controlling prediction sets and Learn-then-Test-style methods generalize the calibration objective beyond classification label coverage.

---

## 10. Reliability hierarchy for this programme

```text
Model output
   ↓
confidence / uncertainty score
   ↓
calibration assessment
   ↓
error/failure detection
   ↓
OOD/open-set monitoring
   ↓
selective decision: predict or abstain
   ↓
(optional) conformal / risk-control layer
   ↓
human-controlled clinical action
```

These layers can be combined, but one must not be used as a synonym for another.

---

# P0.5 canonical terminology

Use:

- **calibrated confidence** for probability-frequency agreement;
- **uncertainty score** for a model-derived uncertainty quantity;
- **failure risk** for estimated probability/score of unacceptable prediction quality;
- **OOD score** for distribution-membership novelty;
- **selection score** for the quantity used to rank/accept predictions;
- **coverage** for fraction of predictions accepted in selective inference;
- **conformal coverage** for true-label/target inclusion in conformal sets under stated assumptions;
- **abstain/defer** for withholding AI output or escalating to human review.

Avoid the vague phrase **“confidence means reliability.”**
