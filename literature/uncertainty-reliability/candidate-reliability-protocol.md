# P0.5 Working Reliable-Inference Protocol

## Status

**Working protocol only — not an experimental commitment.**

P0.5 determines a minimal, defensible reliability toolkit that can be paired with P0.4 shifts. P0.6 must still define network/video mechanisms, and P0.7 must decide the final task × dataset × shift × reliability intersection.

---

# 1. Reliability questions to answer separately

A future model should be evaluated along five distinct questions:

1. **Calibration:** Does predicted confidence match empirical correctness/quality?
2. **Failure prediction:** Can the system identify its likely errors?
3. **OOD detection:** Can it identify inputs outside the development distribution?
4. **Selective inference:** Does abstaining on high-risk cases reduce retained error at useful coverage?
5. **Conformal/risk control:** Can uncertainty sets or risk-control outputs meet their nominal target under stated assumptions?

No one metric substitutes for all five.

---

# 2. Phase-recognition working baseline stack

## Base predictor
Use the task baseline selected after P0.7.

## R1 — deterministic confidence baseline
- maximum softmax probability;
- predictive entropy.

Purpose:
- minimum baseline;
- error ranking;
- selection threshold.

## R2 — probability calibration baseline
- temperature scaling fitted on an **ID calibration split** only.

Evaluate:
- NLL;
- Brier;
- ECE + adaptive/classwise calibration;
- per-phase reliability.

## R3 — uncertainty baseline
At least one:
- deep ensemble (strong but expensive), or
- MC dropout if architecture permits.

Purpose:
- compare simple confidence with model-marginalizing uncertainty.

## R4 — OOD/failure detection baseline
- MSP/entropy;
- energy score if task/model allows;
- explicitly evaluate prediction error detection separately from OOD.

OpenMIBOOD provides surgical-relevant OOD methodology through PhaKIR.

## R5 — selective inference
Use a calibration-set-selected threshold.

Report:
- risk–coverage curve;
- AURC;
- error at fixed coverage values;
- per-phase accepted coverage;
- temporal transition behavior.

## R6 — conformal classification
Candidate:
- split APS/RAPS;
- Mondrian/class-conditional by phase as an important diagnostic;
- weighted CP only if unlabeled target-domain covariates are explicitly available and the covariate-shift assumption is defended;
- adaptive conformal only if online adaptation is part of the declared deployment setting.

Report:
- marginal and per-phase coverage;
- set size;
- singleton/full-set rate;
- repeated calibration splits;
- coverage per P0.4 shift.

---

# 3. Segmentation working baseline stack

## R1 — probability/uncertainty baselines
- pixel entropy / foreground probability;
- MC dropout or ensemble where feasible;
- FGRM only as an advanced direct-surgical comparator if implementation/dataset fit is practical.

## R2 — image-level confidence
Include:
- mean/quantile entropy baseline;
- Soft Dice Confidence or task-aligned expected-quality estimator where feasible.

## R3 — explicit failure monitoring
For a predeclared segmentation-quality threshold:

`failure = 1[Dice or IoU < τ]`

Evaluate:
- AUROC;
- AUPRC;
- false alarm rate;
- missed failure rate.

TCSR-Monitor demonstrates why observable geometry/temporal/image-quality cues may outperform confidence alone.

## R4 — selective segmentation
Choose **one clear abstention unit**:
- whole frame/image; or
- pixel/region; or
- object/instance.

Do not mix the semantics.

For early experiments, **image/frame-level abstention** is easier to audit and compare with risk–coverage curves than partially suppressing pixels.

## R5 — conformal/risk-control layer
Possible references:
- risk-controlling prediction sets;
- morphological conformal segmentation;
- task-specific risk calibration.

Before use, define what is guaranteed:
- mask containment?
- IoU/Dice-related loss?
- missed-instrument risk?
- object coverage?

A guarantee with no clinically meaningful output unit is not sufficient.

---

# 4. Clean-to-shift reliability evaluation

For every selected reliability method:

```text
ID clean
↓
P0.4 controlled visual shifts
↓
natural external shift
↓
P0.6 temporal/network-derived shift
↓
compound shift
```

At every level evaluate **both prediction and reliability**.

Example:

| Dimension | Predictive metric | Reliability metric |
|---|---|---|
| Clean | Accuracy / Dice | ECE, AURC, coverage |
| Visual shift | Accuracy / Dice | calibration degradation, error AUROC, AURC |
| Natural shift | external task score | centre-specific calibration/coverage |
| Temporal/network | task score | detection/abstention/recovery reliability |
| Compound | task score | interaction in failure + reliability degradation |

---

# 5. Calibration data policy

Minimum three-way separation:

```text
training
calibration/validation
final test
```

For conformal/selective methods:
- calibration data must not be reused as final test;
- selection threshold must not be tuned on final OOD test;
- if target-domain calibration examples are used, the setting must be called target adaptation/recalibration rather than unseen-domain testing.

P0.3 procedure-level leakage rules remain active.

---

# 6. Repeated-calibration requirement

Medical datasets can have small procedure counts.

Because conformal/calibration behavior can vary with the calibration sample, later experiments should preferably repeat over multiple procedure-level calibration splits/seeds and report:
- mean/median coverage;
- variability;
- worst split;
- set size/coverage distributions.

This is especially important for rare surgical phases.

---

# 7. Shift-aware conformal hierarchy

Use the simplest method whose assumptions are defensible.

### Level 0 — split CP
Use only as a reference when calibration/test are exchangeable.

### Level 1 — Mondrian/class-conditional
Use to diagnose rare-phase/class undercoverage.

### Level 2 — weighted CP
Only if:
- target unlabeled covariates are available;
- covariate shift is plausible;
- density-ratio estimation is stable.

### Level 3 — adaptive CP
Only if the research question allows online updating.

Do not choose a more complex variant only because it produces better test coverage.

---

# 8. Abstention policy

For this research programme:

> **Abstention means the AI withholds or flags its assistance and hands the case/frame back to the human-controlled surgical workflow.**

A future paper should specify:
- what is hidden or suppressed;
- what message/alarm is shown;
- whether the next frame is evaluated normally;
- whether the abstention persists until confidence recovers;
- what coverage/alert burden is acceptable.

P0.5 does not set a clinical alert threshold.

---

# 9. Track B working hypothesis after P0.5

The broad hypothesis:

> “Uncertainty / calibration / conformal prediction can make surgical AI safer”

is too broad and already substantially occupied.

A narrower testable hypothesis may be:

> **Reliability estimators that appear adequate in-distribution may degrade differently under natural, visual, and network-derived shifts; task-aware selective/conformal mechanisms may reduce retained risk only if their calibration assumptions and failure unit remain valid.**

This is still provisional.

---

# 10. Methods P0.5 does NOT authorize as final

P0.5 does not choose:
- a final ensemble size;
- a final conformal method;
- a final abstention threshold;
- a final segmentation failure threshold;
- a final dataset;
- a final shift severity;
- online adaptation;
- a final Track B paper.

Those decisions remain for P0.7 after P0.6.

---

# 11. Gate to P0.7

Before finalizing Track B:

- [ ] P0.6 establishes the decoded-video/network shift mechanism.
- [ ] P0.7 checks direct overlap with TCSR-Monitor, OpenMIBOOD, FGRM, open-set phase recognition and surgical conformal trajectory work.
- [ ] Calibration and conformal assumptions are matched to the chosen data split.
- [ ] Abstention granularity is explicit.
- [ ] Evaluation includes error detection and selective risk, not uncertainty visualization alone.
- [ ] The proposed contribution remains useful without a “first” claim.
