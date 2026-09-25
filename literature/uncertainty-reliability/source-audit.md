# P0.5 Source Audit

## Audit decision

P0.5 is **complete at the focused reliable-inference reconnaissance level**.

The retained evidence is sufficient to answer:
- how calibration/UQ/OOD/failure detection/selective prediction/conformal prediction differ;
- what direct surgical precedents already exist;
- which medical-imaging methods are mature enough to serve as baselines;
- what conformal guarantees require;
- how distribution shift challenges reliability;
- how phase recognition and segmentation need different reliability units;
- how strongly Track B must be narrowed.

P0.5 does not authorize final novelty or a final reliability method.

## Final audit set

- **36 retained sources/resources**
- **12 excluded/deferred categories**
- **48 audit records/categories**

## Coverage assessment

| Area | Coverage | Assessment |
|---|---|---|
| General calibration theory/baselines | Guo; Ovadia; Nixon | Strong |
| General UQ | MC dropout; deep ensembles; aleatoric/epistemic | Strong |
| Medical-imaging UQ reviews | 2022 systematic review; 2024 review; 2026 clinical review | Strong |
| Medical segmentation calibration/UQ | Mehrtash; Karimi; calibrated ensembles context | Strong representative |
| Direct surgical segmentation UQ | FGRM; TCSR-Monitor | Strong current evidence |
| Direct surgical phase reliability | calibrated confidence; open-set phase; Meta-SurDiff preprint | Strong representative |
| Surgical selective inference | surgical VQA + TCSR alarm | Direct but task-specific |
| Medical selective segmentation | post-hoc under shift; Soft Dice Confidence; learning-to-abstain | Strong |
| OOD detection | OpenMIBOOD/PhaKIR + foundations | Strong surgical-relevant benchmark |
| Conformal foundations | RAPS, weighted CP, adaptive CP, risk control | Strong |
| Medical conformal under shift | triage, class-conditional MS, finite-sample critique | Strong current evidence |
| Surgical conformal prediction | instrument trajectory + TCSR calibration | Direct emerging evidence |
| Conformal phase/standard surgical segmentation under programme's exact shift suite | not established as a mature literature by retained evidence | Unresolved; P0.7 check required |

## Major novelty correction

Before P0.5, Track B could still be interpreted broadly as “selective/conformal reliable inference for surgical AI.”

That framing is now too broad.

Direct surgical work already covers:
- uncertainty-aware segmentation;
- calibrated phase confidence;
- open-set phase recognition;
- selective surgical VQA;
- conformal surgical trajectory forecasting;
- conformal/temporal failure monitoring under surgical acquisition degradation.

Therefore no final proposal should claim novelty simply from adding:
- uncertainty;
- calibration;
- OOD detection;
- abstention;
- conformal prediction.

## Most important current warning

The recent TCSR-Monitor work is highly overlapping with a generic idea of:

> “monitor surgical segmentation failures under corruption using confidence, temporal cues and conformal calibration.”

P0.7 must explicitly compare any segmentation Track B/C design against TCSR-Monitor before experimentation.

## Evidence-status discipline

- Peer-reviewed surgical evidence is treated as primary.
- Meta-SurDiff and class-conditional MS CP are retained with preprint status.
- TCSR-Monitor is retained as a very recent arXiv/MICCAI-UNSURE workshop contribution and must not be described as a mature clinical validation.
- Medical/clinical adjacent work is not represented as surgical evidence.

## Negative-evidence wording

P0.5 states that a mature literature was **not established in the retained search** for some exact intersections.

It does not claim no paper exists anywhere.

## Gate recommendation

P0.5 can be closed.

Next: **P0.6 — Telesurgery / Network Literature Reconnaissance**.
