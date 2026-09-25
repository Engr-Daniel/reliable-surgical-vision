# Execution Brief

## Purpose

This programme will develop rigorous, reproducible research on reliable computer-vision inference for robot-assisted and tele-robotic surgery. Work will proceed from evidence mapping to carefully bounded experimentation, with research direction refined as the literature and empirical results develop.

## Standard

The programme is guided by scientific excellence, methodological transparency, reproducibility, and responsible interpretation.

### 1. Evidence before experimentation
Experiments should answer a defined question grounded in prior work. Literature reconnaissance must establish what is known before novelty is asserted.

### 2. Reproducibility by design
Every substantive experiment should preserve:
- dataset/version provenance;
- preprocessing and shift-generation logic;
- model and checkpoint identity;
- configuration/hyperparameters;
- random seeds where relevant;
- environment/dependency information;
- evaluation code;
- raw metric outputs;
- sufficient instructions to reproduce the run.

### 3. Bounded experiments
Begin with the smallest experiment capable of falsifying or supporting a hypothesis. Scale only when the initial evidence justifies additional complexity.

### 4. Reliability beyond accuracy
Where appropriate, evaluation should consider discrimination/performance together with calibration, uncertainty, selective risk, coverage, abstention, OOD behaviour, failure modes, and clinically relevant limitations.

### 5. Controlled shift construction
Synthetic corruptions must be parameterised, documented, and justified. Natural/domain shifts must have clearly defined source and target distributions. Compound shifts must retain enough structure to isolate interactions where possible.

### 6. Transparent results
Positive, negative, and inconclusive results are research outputs. Do not hide failed hypotheses or selectively report favourable configurations.

### 7. Safety-aware interpretation
Experimental performance is not evidence of clinical safety. Avoid translating benchmark success directly into clinical deployment claims.

### 8. Progressive research gates

**Gate 0 — Foundation:** architecture, literature, dataset, and gap reconnaissance.

**Gate 1 — Feasibility:** confirm accessible datasets, implementable tasks, valid metrics, and computational feasibility.

**Gate 2 — Baseline:** establish reproducible unshifted baselines.

**Gate 3 — Shift:** characterise degradation under controlled and/or natural shifts.

**Gate 4 — Reliability:** evaluate calibration, uncertainty, OOD/selective/conformal methods as justified.

**Gate 5 — Systems:** investigate network-aware or multimodal reliability where evidence supports it.

**Gate 6 — Publication readiness:** replicate key findings, perform ablations/sensitivity analyses, document limitations, audit statistical claims, and freeze reproducible artefacts.

## Research cadence

Progress is evidence-driven rather than activity-driven. Reading, dataset verification, implementation, failed experiments, replication, and documentation are all valid research progress when they reduce uncertainty.

## Definition of done

A research result is not complete merely because code ran. It is complete when the question, method, provenance, configuration, result, limitations, and reproducibility path are documented.
