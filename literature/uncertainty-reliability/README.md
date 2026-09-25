# Uncertainty & Reliability Literature — P0.5

P0.5 maps **calibration, uncertainty quantification, OOD/failure detection, selective prediction, conformal prediction, risk control, and abstention** for reliable surgical/medical visual inference.

## Start here

1. `rq-answer-matrix.md` — concise answers to every P0.5 research question.
2. `reliable-inference-landscape.md` — narrative synthesis and Track B stress-test.
3. `reliability-taxonomy.md` — canonical terminology.
4. `calibration-metrics-guide.md` — what to measure for phase recognition and segmentation.
5. `uncertainty-method-map.csv` — UQ/calibration baselines.
6. `ood-failure-detection-map.csv` — OOD vs actual failure monitoring.
7. `selective-prediction-map.csv` — abstention methods and granularities.
8. `conformal-prediction-map.csv` — conformal variants, assumptions and guarantees.
9. `task-reliability-crosswalk.csv` — phase/segmentation/task-specific mapping.
10. `assumptions-and-failure-modes.md` — what each method can and cannot guarantee.
11. `candidate-reliability-protocol.md` — non-final protocol carried to P0.6/P0.7.
12. `quantitative-evidence.csv` — selected current numerical evidence.
13. `search-protocol.md`, `source-screening-log.csv`, `source-index.md`, `source-audit.md` — reproducibility trail.
14. `open-questions.md` — unresolved P0.6/P0.7 questions.
15. `references.bib` — retained source registry.

## Critical P0.5 rules

- Calibration ≠ uncertainty ≠ OOD detection ≠ failure prediction ≠ abstention ≠ conformal coverage.
- AI abstention means withholding/defering AI assistance; it does **not** mean stopping surgery.
- Vanilla conformal coverage requires exchangeability and is marginal unless a stronger conditional/group formulation is used.
- Reliability must be re-evaluated under the explicit shifts from P0.4.
- Do not claim surgical conformal prediction, uncertainty, OOD, or abstention as broadly novel.

## Status

**P0.5 complete — 2026-09-25.**

Final reliability method and Track B novelty remain deferred to P0.7 after P0.6.
