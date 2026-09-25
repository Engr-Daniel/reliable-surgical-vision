# P0.5 Assumptions and Failure Modes

## 1. Temperature scaling

### Assumption / role
Fits a scalar temperature on a calibration set to correct probability sharpness.

### Can fail when
- the deployment distribution differs from calibration;
- classwise biases require more than one global scalar;
- model ranking is poor;
- the model is confidently wrong under unseen shift.

### Programme rule
Use as a **baseline**, not as proof of reliable uncertainty.

---

## 2. MC dropout

### Role
Approximate epistemic uncertainty through stochastic forward passes.

### Failure modes
- dropout posterior approximation may be weak;
- uncertainty can still be miscalibrated;
- repeated passes increase latency;
- low variance does not guarantee correctness under unfamiliar systematic shift.

### Programme rule
Useful baseline when architecture already supports dropout; not mandatory for real-time deployment.

---

## 3. Deep ensembles

### Role
Strong model-marginalizing predictive uncertainty baseline.

### Failure modes
- high training/storage/inference cost;
- members can share the same dataset bias;
- ensemble confidence can still degrade under distribution shift.

### Programme rule
Valuable research reference even if too expensive for final real-time design.

---

## 4. Evidential uncertainty

### Role
Single-pass uncertainty outputs, attractive for real-time settings.

### Failure modes
- evidence parameterization can be overconfident;
- training objective/regularization strongly affects meaning;
- “epistemic” interpretation should not be assumed from formula alone.

### Programme rule
Evaluate empirically against actual error/shift, not just uncertainty magnitude.

---

## 5. OOD score

### Assumption
Unusual inputs correlate with deployment risk.

### Failure modes
- unusual but easy/correct samples;
- common-looking but wrongly predicted samples;
- semantic/near-OOD overlap;
- detector simply learns image degradation rather than model failure.

### Programme rule
If used for safety, evaluate:
1. OOD discrimination, and
2. error/failure prediction.

TCSR-Monitor's within-corrupted-frame circularity control is a useful precedent.

---

## 6. Selective prediction

### Assumption
The selection score ranks low-risk predictions above high-risk predictions.

### Failure modes
- threshold tuned on test shift;
- coverage collapses under shift;
- rare classes are disproportionately rejected;
- accepted errors remain overconfident;
- operational deferral load is too high.

### Programme rule
Report risk–coverage across each shift and per-class/centre coverage. Do not optimize threshold on final OOD test.

---

## 7. Vanilla split conformal prediction

### Standard condition
Calibration and test examples are exchangeable.

### Guarantee
Finite-sample **marginal** coverage.

### Does not guarantee
- per-case probability of correctness;
- each class has nominal coverage;
- each centre/severity has nominal coverage;
- coverage survives arbitrary distribution shift.

### Failure modes
- shifted calibration/test distribution;
- class imbalance hides minority undercoverage;
- small calibration set causes high calibration-set-conditional variability;
- inefficient huge prediction sets.

### Programme rule
Always report:
- marginal coverage;
- class/phase/centre/shift coverage;
- set size;
- repeated calibration-split sensitivity.

---

## 8. Class-conditional / Mondrian conformal

### Strength
Can target group/class-specific coverage.

### Failure modes
- small groups give unstable quantiles;
- rare surgical phases may require large sets;
- defining groups after seeing test errors risks leakage.

### Programme rule
Predefine phase/group partitions.

---

## 9. Weighted conformal prediction

### Assumptions
A covariate-shift structure and a useful density-ratio estimate, usually with access to unlabeled target covariates.

### Failure modes
- wrong shift model;
- extreme/unstable importance weights;
- conditional relationship changes;
- target covariates unavailable.

### Programme rule
If target data are used, label the setting explicitly. Do not call it zero-target-data generalization.

---

## 10. Adaptive conformal inference

### Strength
Designed for online changing distributions.

### Boundary
Long-run coverage-frequency control differs from a guarantee that every period/phase/centre is covered.

### Programme rule
Potentially relevant to streaming surgical video, but only after P0.6/P0.7 decide whether online adaptation is allowed.

---

## 11. Conformal segmentation

### Core difficulty
“What must be covered?” is not unique.

Possible units:
- every ground-truth pixel;
- object mask;
- boundary;
- IoU loss;
- missed-object risk.

### Failure modes
- prediction set/margin becomes huge;
- background dominates;
- pixel guarantees do not imply object or clinical-task guarantees.

### Programme rule
Choose the coverage/risk unit before choosing the algorithm.

---

## 12. Failure-monitor calibration under corruption

Recent TCSR-Monitor evidence shows even a purpose-built surgical failure monitor can retain substantial false alarms under moderate degradation, despite severity-aware conformal calibration.

### Programme implication
A monitor should be evaluated as a **decision system**:
- missed failures;
- false alarms on correct predictions;
- coverage/deferral burden;
- cross-corruption and cross-model transfer.

Not just AUROC.

---

## 13. Human-controlled surgery

In this repository:

> **AI abstention/defer means withdrawing or suppressing unreliable AI assistance.**

The operating surgeon/bedside team remains responsible for care.

No reliability method in P0.5 is treated as authorization for autonomous surgical action.

---

# Assumption ledger required for future experiments

Every reliability experiment must record:

```text
task
prediction_unit
uncertainty_method
calibration_data
calibration_n
selection_threshold_source
target_domain_data_used? yes/no/type
conformal_method
nominal_alpha
coverage_unit
risk_definition
shift_type
adaptation_allowed? yes/no
abstention_granularity
human_fallback interpretation
```

Without this ledger, apparently similar reliability results may not be comparable.
