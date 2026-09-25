# P0.5 Search and Review Protocol

## Identity
- **Programme:** Reliable Surgical Vision
- **Phase:** Phase 0 — Research Foundation
- **Task:** P0.5 — Reliable-Inference Literature Reconnaissance
- **Search/final audit date:** 2026-09-25
- **Evidence cutoff:** 2026-09-25
- **Review type:** focused evidence-backed reconnaissance
- **Not claimed as:** an exhaustive systematic review or final novelty analysis

## Objective
Map the methods, assumptions, metrics, and current surgical/medical evidence for **calibration, uncertainty quantification, OOD/failure detection, selective prediction, conformal prediction, and abstention**.

The purpose is not to find a fashionable uncertainty score. It is to determine:

> **What does it mean for a surgical-CV model to know when it may be wrong, which reliability methods are already established, what assumptions break under the P0.4 shifts, and which evaluation protocol is defensible for later experiments?**

## Research questions
1. What concepts belong to reliable inference and how do they differ?
2. How does calibration behave under distribution shift?
3. Which uncertainty-estimation methods are established in surgical/medical imaging?
4. What is known about OOD detection versus actual failure prediction?
5. What selective-prediction / abstention methods and metrics are established?
6. What can conformal prediction guarantee, under which assumptions, and what changes under shift?
7. How should reliability be operationalized for phase recognition versus segmentation?
8. What non-final reliability toolkit should be carried to P0.6–P0.7, and what does P0.5 do to Track B?

## Search surfaces
- PubMed / PubMed Central
- Medical Image Analysis / ScienceDirect
- IEEE journals / proceedings
- NeurIPS, ICML, ICLR, CVPR
- MICCAI open-access proceedings
- Springer Nature
- Frontiers journals
- SciTePress/VISAPP
- PMLR
- arXiv only when recent work materially changes the current surgical landscape

## Representative query families
- `"surgical" uncertainty calibration segmentation`
- `"surgical phase recognition" calibrated confidence`
- `"open-set" surgical phase uncertainty`
- `"surgical visual question answering" uncertainty calibration selective`
- `"surgical segmentation" failure monitoring conformal`
- `"OpenMIBOOD" PhaKIR`
- `"medical image segmentation" calibration uncertainty`
- `"medical imaging" failure detection uncertainty`
- `"selective prediction" medical segmentation distribution shift`
- `"conformal prediction" surgical`
- `"conformal prediction" medical segmentation`
- `"conformal prediction" distribution shift medical`
- `"class-conditional conformal" medical distribution shift`
- `"risk coverage" selective prediction segmentation`
- `"calibration" ECE limitations`
- `"predictive uncertainty" dataset shift`

## Evidence priority
1. direct peer-reviewed surgical reliability papers;
2. surgical challenge/benchmark evidence;
3. direct surgical conference/preprint evidence when very recent and materially relevant;
4. peer-reviewed medical-imaging reliability work;
5. clinical selective/conformal work with explicit shift evaluation;
6. general foundational methods/theory required to interpret assumptions and metrics.

## Inclusion criteria
Retain a source if it materially informs at least one P0.5 question:
- confidence calibration;
- epistemic/aleatoric/predictive uncertainty;
- failure/error detection;
- OOD/open-set detection;
- selective prediction / rejection / deferral;
- conformal prediction / risk control;
- reliability under distribution shift;
- task-specific reliability for classification, temporal prediction, or segmentation;
- evaluation metrics/assumptions needed for safe interpretation.

## Exclusion/defer criteria
- uncertainty used only for pseudo-label selection;
- accuracy-only “reliability” claims;
- adversarial-only work;
- pure domain adaptation without reliability estimation;
- pure networking/QoS work;
- generic LLM abstention;
- unstable secondary summaries when primary evidence exists.

## Screening accounting
Final P0.5 audit set:
- **36 retained sources/resources**
- **12 excluded/deferred categories**
- **48 audit records/categories**

This is a structured evidence map, not the number of raw search results.

## Interpretation rules
1. **Confidence is not uncertainty.**
2. **Calibration is not OOD detection.**
3. **OOD detection is not failure detection.**
4. **Failure detection is not selective prediction.**
5. **Selective prediction is a decision policy, not automatically a statistical guarantee.**
6. **Conformal coverage is not the same as probability calibration.**
7. **Vanilla split conformal guarantees rely on exchangeability of calibration and test examples.**
8. **Marginal coverage can hide poor class/group/condition-specific coverage.**
9. **Target-domain data use must be disclosed:** none (DG), unlabeled (weighted/UDA-like), labeled (recalibration/adaptation), or online.
10. **AI abstention means withholding/defering AI guidance, not stopping the surgery.**
11. Surgical direct evidence is distinguished from medical-imaging and general-methodological evidence.
12. Preprints/workshop papers are labelled as such and are not promoted to peer-reviewed fact.

## Reproducibility
A future update should:
1. rerun query families;
2. resolve retained records via DOI/official proceedings;
3. forward-search the direct surgical sources (FGRM, surgical open-set phase, conformal trajectory, TCSR-Monitor);
4. update 2026+ conformal/segmentation literature;
5. regenerate the method, assumption and task crosswalks;
6. repeat the Track B novelty stress-test before manuscript submission.
