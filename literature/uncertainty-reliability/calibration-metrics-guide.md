# P0.5 Calibration and Reliability Metrics Guide

## 1. Why task accuracy is insufficient

A model can have acceptable average accuracy/Dice while:
- being overconfident on errors;
- failing silently under shift;
- producing poor confidence ranking;
- retaining rare-class errors after abstention;
- violating a nominal conformal coverage target.

P0.5 therefore separates:

1. predictive task performance;
2. probability calibration;
3. error/OOD discrimination;
4. selective risk;
5. conformal coverage/efficiency;
6. task- and subgroup-specific reliability.

---

# 2. Classification / surgical phase recognition

## Predictive performance
Preserve the benchmark's established metrics:
- accuracy;
- precision/recall/F1;
- Jaccard where used for phase recognition;
- segmental/edit metrics if temporal segmentation is evaluated.

## Probability calibration

### Negative log-likelihood (NLL)
Proper scoring rule sensitive to probability quality.

### Brier score
Mean squared error between predicted probability vector and one-hot outcome.

### Reliability diagram
Visual diagnostic: confidence versus empirical accuracy.

### Expected Calibration Error (ECE)
Useful summary but **not sufficient by itself**.

ECE depends on:
- bin count;
- binning strategy;
- whether only maximum confidence is used;
- sample size;
- class imbalance.

Nixon et al. show calibration rankings can change with metric design.

### Preferred reporting
For phase recognition:
- NLL;
- Brier;
- ECE;
- adaptive/classwise calibration error (ACE/SCE/TACE-style where practical);
- reliability diagram;
- **per-phase calibration**, especially for rare phases;
- calibration around phase transitions.

---

# 3. Uncertainty / prediction-error ranking

If an uncertainty score is expected to identify incorrect predictions, evaluate the actual error-detection task.

Recommended:
- AUROC(error vs correct);
- AUPRC(error as positive);
- AUPRC must be interpreted relative to failure prevalence;
- uncertainty–error correlation where meaningful.

Do not report only mean entropy.

For segmentation, define the failure event explicitly, e.g.:

`failure = Dice < τ` or `IoU < τ`

The threshold `τ` must be justified and sensitivity-tested.

---

# 4. OOD detection

Recommended standard metrics:
- AUROC;
- AUPR-IN;
- AUPR-OUT;
- FPR@95TPR.

For a surgical benchmark, separately report:
- covariate-shifted ID;
- near-OOD;
- far-OOD.

OpenMIBOOD provides a direct precedent through PhaKIR.

## Critical distinction

A good OOD detector answers:
> “Is this input unusual relative to development data?”

It does not necessarily answer:
> “Will the model's current prediction be wrong?”

Later P0.7 experiments should evaluate both if they are used.

---

# 5. Selective prediction / abstention

Define a selection function `g(x)` that accepts or rejects a prediction.

## Coverage
Fraction of examples for which the model predicts:

`coverage = accepted / total`

## Selective risk
Average task loss among accepted examples.

Examples:
- phase classification error among accepted frames;
- `1 - Dice` among accepted segmentation images.

## Risk–coverage curve
Vary the selection threshold and plot risk against coverage.

## AURC
Area under the risk–coverage curve.

Lower is better when risk is an error/loss.

AURC is preferable to quoting one arbitrary threshold because it evaluates ranking across operating points.

## Also report clinically/operationally interpretable points
Examples:
- error at 90%, 80%, 70% coverage;
- coverage achievable below a chosen error target;
- false alarm / miss rate of a failure monitor.

Avoid choosing the operating point on the final shifted test set.

---

# 6. Semantic / instrument segmentation

Segmentation reliability can be measured at several levels.

## Pixel-level calibration
Possible:
- pixel NLL;
- pixel Brier;
- pixel ECE/classwise ECE.

**Caution:** background pixels can dominate. Report foreground/instrument-specific calibration.

## Image-level quality prediction
Define a case-level quality such as:
- Dice;
- IoU;
- boundary score.

Then assess whether confidence predicts quality:
- correlation;
- error AUROC;
- AUPRC for failure event;
- selective Dice risk–coverage.

Soft Dice Confidence is an important recent baseline for image-level selective segmentation.

## Pixel-level abstention
If the model may reject pixels:
- Dice/IoU on accepted pixels;
- pixel coverage;
- classwise coverage;
- spatial pattern of abstentions.

Pixel rejection can create fragmented overlays; qualitative/human-interface implications must be documented.

## Object/instance-level reliability
For instance segmentation consider:
- instance-level IoU quality;
- missing-object risk;
- false-instance risk;
- per-instrument confidence.

Do not assume pixelwise calibration implies instance reliability.

---

# 7. Temporal phase/video reliability

Framewise calibration can hide temporal failures.

Add:
- per-phase calibration;
- transition-window calibration;
- prediction volatility/flicker;
- segmental F1 / edit score;
- recovery time after a degradation burst;
- longest consecutive failure run;
- confidence before/during/after transitions.

A temporal smoother can improve apparent stability while delaying detection of a true phase change, so latency/transition error must also be checked.

---

# 8. Conformal classification metrics

For target miscoverage `α`:

## Coverage
`mean[ y_i ∈ C(x_i) ]`

Report:
- marginal coverage;
- per-class coverage;
- per-centre/per-shift coverage;
- coverage confidence interval / repeated calibration splits.

## Efficiency
- average set size;
- median set size;
- singleton rate;
- full-set rate;
- empty-set rate where possible.

A method that always returns all labels has excellent coverage but poor utility.

## Conditional diagnostics
Because vanilla CP guarantees are marginal:
- rare-phase coverage;
- centre-specific coverage;
- shift-severity coverage;
- calibration-split sensitivity.

---

# 9. Conformal segmentation / risk control

Depending on method:

### Set/mask coverage
Does the conformal prediction region contain the target structure under the method's definition?

### Risk control
Report the actual bounded loss:
- missed-object fraction;
- IoU/Dice-related risk;
- false-negative area;
- other clinically motivated segmentation loss.

Also report:
- prediction-set/margin size;
- uncertainty-region area;
- spatial usefulness.

A very large conformal margin can satisfy coverage while being operationally unhelpful.

---

# 10. Distribution-shift reporting

For every reliability metric:

```text
clean
natural external
each controlled visual shift × severity
temporal/network-derived shift (after P0.6)
compound shift (after P0.6/P0.7)
```

Report both:
- **predictive degradation**, and
- **reliability degradation**.

Example:
A model might lose only 3 points of accuracy but become sharply overconfident, or lose substantial accuracy while its uncertainty successfully ranks errors.

These are different deployment outcomes.

---

# 11. Recommended minimum P0.7 metric bundle

## Phase recognition
- accuracy/F1/Jaccard;
- NLL + Brier + ECE/classwise calibration;
- error-detection AUROC/AUPRC;
- risk–coverage curve + AURC;
- conformal marginal + per-phase coverage and set size, if CP is used;
- temporal transition/flicker diagnostics.

## Segmentation
- Dice/IoU;
- foreground calibration;
- failure AUROC/AUPRC for a predeclared quality threshold;
- selective Dice risk–coverage / AURC;
- image-level or object-level abstention metrics;
- conformal/risk-control coverage + efficiency if used;
- temporal consistency for video segmentation.

---

# 12. Metric governance rule

No claim such as “more reliable” is allowed unless the statement names the reliability dimension:

- better calibrated;
- better error ranking;
- better OOD discrimination;
- lower selective risk at matched coverage;
- better conformal coverage/efficiency;
- lower false-alarm/miss rate;
- more stable under shift.

“Reliability” without a metric is too vague for the programme.
