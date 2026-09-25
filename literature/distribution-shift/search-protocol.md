# P0.4 Search and Review Protocol

## Identity

- **Programme:** Reliable Surgical Vision
- **Phase:** Phase 0 — Research Foundation
- **Task:** P0.4 — Distribution-Shift Literature Reconnaissance
- **Search/final audit date:** 2026-09-25
- **Evidence cutoff:** 2026-09-25
- **Review type:** focused evidence-backed literature reconnaissance
- **Not claimed as:** PRISMA systematic review, exhaustive bibliometric census, or final novelty analysis

## Objective

Map how distribution shift has actually been defined, generated, evaluated, and mitigated in surgical computer vision.

P0.4 separates four evidence classes that should not be conflated:

1. **natural domain shift** — site, device, instrument, procedure, patient, workflow, modality or time;
2. **controlled visual corruption** — image/video appearance changes introduced for robustness testing;
3. **temporal/video shift** — changes to frame availability, ordering, timing or temporal context;
4. **compound shift** — more than one changed factor, either naturally bundled or deliberately composed.

The task also records domain adaptation/generalization strategies, but does not turn P0.4 into a method leaderboard.

## Research questions

1. What shift types are documented in surgical CV?
2. How are natural shifts operationalized and measured?
3. Which synthetic/controlled corruptions and severity protocols exist?
4. Which surgical tasks, datasets and model families have been evaluated under shift?
5. Which mitigation strategies (augmentation, UDA, DG, causal/multimodal, foundation-model adaptation) are established?
6. How should shifted performance be evaluated and reported?
7. What evidence exists for temporal/video degradation and compound shifts?
8. Which **working, non-final shift set** should be carried into P0.5–P0.7?

## Search surfaces

- PubMed / PubMed Central
- Medical Image Analysis / ScienceDirect
- SpringerLink
- IEEE-indexed publications
- Scientific Reports / Nature portfolio
- MICCAI / EndoVis challenge records
- institutional publication repositories where needed for metadata
- arXiv only for recent/important work without a peer-reviewed replacement
- official challenge/project repositories for benchmark protocols

## Representative query families

- `"surgical computer vision" domain shift generalization`
- `"ROBUST-MIS" domain gap surgical instrument segmentation`
- `"limited generalizability" surgical instrument segmentation recording system instrument surgery`
- `"multi-centric generalization" surgical phase step recognition`
- `"PhaKIR" cross-centre generalizability`
- `"inter-hospital transferability" phase recognition cholecystectomy`
- `"surgical" unseen domain generalization scene graph`
- `"color domain shift" endoscopic instrument segmentation`
- `"cross-dataset" surgical instrument segmentation deployment realistic`
- `"SegSTRONG-C" smoke bleeding low brightness`
- `"CaRTS" low brightness smoke blood background`
- `"simulation-to-real" surgical instrument segmentation`
- `"surgical instrument" unsupervised domain adaptation`
- `"surgical instrument segmentation" unseen domains synthesis`
- `"SDA-CLIP" surgical domain adaptation`
- `"few-shot" surgical phase recognition generalization`
- `"robustness evaluation" endoscopic clinically calibrated corruptions`
- `"surgical endoscopy" packet loss robustness video`
- `"prediction volatility" surgical workflow`
- `"domain-agnostic" surgical instrument segmentation`
- `"RobustSurg" out-of-distribution surgical scene segmentation`

## Inclusion criteria

Retain a source if it contributes material evidence on at least one of:

- natural shift definition/evaluation;
- controlled non-adversarial corruption;
- surgical robustness benchmark;
- multicentre/cross-device/cross-procedure evaluation;
- sim-to-real or cross-modality adaptation;
- UDA/DG methods evaluated on surgical data;
- temporal instability or explicit temporal/video corruption;
- compound corruption protocol;
- recent evidence that materially changes the novelty landscape.

## Exclusion / defer rules

- generic natural-image robustness without a surgical/endoscopic bridge;
- radiology/pathology shift literature;
- calibration/conformal/selective prediction without shift-method relevance (P0.5);
- pure network/QoS evidence without downstream CV evaluation (P0.6);
- augmentation-only papers with no shifted test evaluation;
- “robust” claims based only on i.i.d. performance;
- adversarial attacks as the main shift mechanism;
- unstable secondary summaries when primary evidence is available.

## Screening accounting

Final P0.4 audit set:

- **25 retained sources/resources**
- **10 excluded/deferred categories**
- **35 total audit records/categories**

This is a targeted research map, not the total number of search hits.

## Evidence classes

- peer-reviewed natural-shift benchmark;
- peer-reviewed controlled-corruption study;
- peer-reviewed domain adaptation/generalization method;
- peer-reviewed temporal-consistency evidence;
- challenge report / official benchmark;
- recent accepted/preprint evidence;
- adjacent endoscopy methodology evidence.

Adjacent GI-endoscopy evidence is labelled explicitly and is never presented as direct surgical evidence.

## Extraction fields

For each retained source:

- source ID;
- title / year / venue / DOI;
- task;
- dataset/domain;
- shift type and mechanism;
- whether shift is natural or controlled;
- mitigation method;
- evaluation design;
- major finding;
- limitation / transfer boundary.

## Interpretation rules

1. **Centre shift is compound.** It can bundle camera, lighting, workflow, instruments, patient population, surgeon and preprocessing changes.
2. **Cross-dataset is not necessarily independent shift.** P0.3 provenance rules remain active.
3. **Synthetic visual corruption is not network impairment.**
4. **Frame dropping is not automatically packet loss.** Mapping network events to decoded-video behavior is a P0.6 question.
5. **Temporal prediction volatility is not itself an input distribution shift.**
6. **Target-domain adaptation and unseen-domain generalization are different settings.**
7. **A robustness method is not evidence that the underlying shift is novel.**
8. **Preprints are evidence of current research activity, but peer-review status is preserved.**
9. **No final Track A novelty claim is allowed until P0.6/P0.7.**

## Reproducibility

A future audit should:
1. rerun the query families;
2. resolve retained records by DOI/identifier;
3. apply the inclusion/defer rules;
4. compare `source-screening-log.csv`;
5. update recent 2026+ accepted/preprint records;
6. regenerate the shift and method maps;
7. forward-search core benchmarks before manuscript submission.
