# P0.5 Research Question Answer Matrix

## RQ1 — What concepts belong to reliable inference, and how do they differ?

**Answer:** Reliable inference comprises calibration, uncertainty estimation, OOD/open-set detection, failure prediction, selective prediction and conformal/risk control. These answer different questions and must not be used interchangeably. Confidence is merely a model score; calibration tests probability-frequency agreement; OOD detects distribution novelty; failure detection estimates wrongness; selective prediction makes an accept/defer decision; conformal methods target coverage/risk under explicit assumptions.

**Evidence:** RI01–RI05, RI18–RI21, RI26–RI29.  
**Detailed:** `reliability-taxonomy.md`.

---

## RQ2 — How does calibration behave under distribution shift?

**Answer:** A calibration fit that works in-distribution cannot be assumed to remain valid after shift. Ovadia et al. show calibration/uncertainty degradation with increasing dataset shift and limitations of ordinary post-hoc calibration. Medical segmentation papers confirm deep models can be overconfident. Surgical phase recognition already uses calibrated confidence, but P0.5 found no basis for assuming that one calibration model transfers across the P0.4 centre/device/corruption suite.

**Evidence:** RI01, RI02, RI09, RI10, RI13.  
**Detailed:** `calibration-metrics-guide.md`, `assumptions-and-failure-modes.md`.

---

## RQ3 — Which uncertainty-estimation methods are established in surgical/medical vision?

**Answer:** Established baselines include MC dropout, deep ensembles, Bayesian/aleatoric-epistemic models, deterministic/post-hoc confidence, evidential learning and task-specific confidence estimators. Direct surgical evidence includes FGRM for calibrated surgical scene-segmentation uncertainty, calibrated phase confidence, Meta-SurDiff frame uncertainty and surgical VQA uncertainty decomposition.

**Evidence:** RI03–RI09, RI12–RI16, RI23.  
**Detailed:** `uncertainty-method-map.csv`.

---

## RQ4 — What is known about OOD detection versus actual failure prediction?

**Answer:** OOD detection and failure prediction overlap but are not equivalent. OpenMIBOOD provides a direct PhaKIR medical/surgical-relevant OOD benchmark including smoke covariate shift and near/far OOD data. Direct surgical open-set phase recognition also exists. However, recent TCSR-Monitor evidence shows why an operational monitor should predict actual segmentation failure rather than merely image degradation/OOD; within corrupted frames it reports AUROC 0.946 versus entropy 0.594.

**Evidence:** RI11, RI14, RI17–RI19, RI34.  
**Detailed:** `ood-failure-detection-map.csv`.

---

## RQ5 — What selective-prediction / abstention approaches are established?

**Answer:** Selective prediction is mature in classification and increasingly developed for medical segmentation. Available approaches include confidence thresholding, integrated reject heads, image-level segmentation abstention (Soft Dice Confidence), pixel-level rejection and cost-aware clinical deferral. Direct surgical VQA includes selective answering and TCSR provides surgical failure alarms. Therefore “make the AI abstain when uncertain” is not itself a novelty claim.

**Evidence:** RI15, RI20–RI25, RI34, RI36.  
**Detailed:** `selective-prediction-map.csv`, `calibration-metrics-guide.md`.

---

## RQ6 — What can conformal prediction guarantee, and what changes under shift?

**Answer:** Vanilla split conformal prediction gives finite-sample marginal coverage when calibration and test data are exchangeable. It does not automatically provide per-class, per-centre, per-severity, or per-case guarantees. Under covariate shift, weighted CP can be used if density ratios/target covariates are available; adaptive conformal targets long-run coverage in online nonstationarity; Mondrian/class-conditional CP targets strata but needs sufficient calibration examples. Medical evidence shows marginal CP can hide severe minority-class undercoverage, and small calibration sets can yield practically unstable one-time coverage.

Direct surgical conformal precedent already exists in instrument trajectory forecasting and recent conformalized segmentation failure monitoring.

**Evidence:** RI25–RI34.  
**Detailed:** `conformal-prediction-map.csv`, `assumptions-and-failure-modes.md`.

---

## RQ7 — How should reliability be operationalized for phase recognition versus segmentation?

**Answer:** The tasks require different reliability units.

For phase recognition: evaluate frame/segment confidence, class/phase calibration, error ranking, risk–coverage, transition behavior and, if used, conformal label-set coverage/size.

For segmentation: evaluate foreground calibration, predicted mask quality/failure ranking, image/object/pixel abstention explicitly, selective Dice risk–coverage and task-defined conformal/risk-control outputs. Pixel calibration alone does not establish object or frame reliability.

**Evidence:** RI09–RI13, RI20–RI24, RI29–RI34.  
**Detailed:** `task-reliability-crosswalk.csv`, `calibration-metrics-guide.md`.

---

## RQ8 — What reliability toolkit should be carried forward, and what does P0.5 imply for Track B?

**Answer:** A transparent reliability ladder should be carried forward rather than committing to one new UQ architecture:

- max probability / entropy;
- temperature scaling;
- deep ensemble or MC dropout;
- explicit error/failure detection;
- risk–coverage/AURC selective evaluation;
- task-aware conformal/risk-control method if its assumptions fit the deployment setting.

For phase recognition, APS/RAPS plus phase-conditional coverage is a credible research baseline. For segmentation, image-level failure/selective confidence and structured risk control are more interpretable than treating every pixel identically.

Track B remains scientifically motivated but is **narrowed strongly**. Calibration, surgical UQ, surgical open-set recognition, abstention and surgical conformal work already exist. The remaining question is whether these reliability mechanisms remain trustworthy across the programme's natural, visual and mechanistically grounded network-derived shifts.

**Detailed:** `candidate-reliability-protocol.md`, `reliable-inference-landscape.md`.

---

# P0.5 Overall Conclusion

A surgical model cannot be called reliable merely because it reports uncertainty, is calibrated in-distribution, detects OOD data, or meets a marginal conformal target.

Reliable deployment requires matching:
- the failure question;
- the prediction/abstention unit;
- the calibration population;
- the shift setting;
- the decision metric;
- the formal assumptions.

P0.5 closes the broad Track B novelty space and carries forward a narrower **reliability-under-shift** question for P0.6/P0.7.
