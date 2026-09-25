# P0.4 Evaluation Practices for Distribution Shift

## 1. Minimum reporting unit

Every shifted experiment should report both:

- **clean / source-domain performance**, and
- **shifted / target-domain performance**.

A robustness claim based only on shifted performance is incomplete because there is no reference for the degradation.

Recommended reporting:

`clean score`, `shifted score`, `absolute delta`, `relative retention`, and `confidence interval / repeated-seed variation`.

For metric \(M\):

`absolute_drop = M_clean - M_shift`

`relative_retention = M_shift / M_clean`

Use “drop” only when larger values are better.

---

## 2. Natural-shift evaluation

### Required
- procedure/video-level independence;
- source and target centre/device/procedure identified;
- exact target domain stated;
- per-domain results, not only pooled mean;
- target-domain data access during training/adaptation disclosed;
- source-video provenance checked using P0.3 rules.

### Preferred
- external validation with no target labels used during model development;
- multiple centres;
- centre-held-out or leave-one-centre-out designs;
- confidence intervals at the patient/procedure level;
- stratification by device/procedure where sample size permits.

### Caution
“Centre A → Centre B” is not a causal label. It can bundle:
camera + lighting + workflow + instrument + patient + surgeon + preprocessing.

Do not conclude which factor caused failure unless it was isolated.

---

## 3. Controlled-corruption evaluation

For each corruption:

- clean score;
- corruption operator/version;
- severity parameter;
- severity curve;
- mean corruption performance;
- worst-corruption performance;
- per-corruption results;
- multiple random realizations where the operator is stochastic.

Avoid reporting only a grand average because one catastrophic corruption can be hidden by easy ones.

---

## 4. Severity design

### Surgical-specific evidence
SegSTRONG-C provides direct surgical corruption classes:
- smoke;
- over-bleeding;
- low brightness.

CaRTS provides controlled counterfactual domains:
- low brightness;
- smoke;
- blood;
- altered background.

### Adjacent methodological precedent
Jaspers et al. use **10 severity levels** for 11 endoscopic distortions and clinically calibrate realistic ranges. Their public repository notes:
- levels 1–2 ≈ degradation expected in expert-quality data;
- levels up to 5 remain within clinically calibrated realistic ranges for their GI-endoscopy setting;
- levels 8–10 are useful for extreme stress testing.

This is a **methodological precedent**, not a ready-made surgical severity scale.

### P0.4 decision
Do not blindly import ImageNet-C or GI-endoscopy severity constants.

For surgical experiments:
1. preserve the operator family;
2. define physical/visual parameter values;
3. inspect examples at each level;
4. calibrate plausible ranges using surgical-domain evidence/expert review where possible;
5. keep “stress-test extreme” levels separate from “deployment-plausible” levels.

---

## 5. Compound corruption

For a compound test:
- record every component corruption;
- record application order;
- record each severity;
- distinguish independent random composition from mechanistically linked composition.

Adjacent endoscopy work already samples combinations of multiple distortions. Therefore, the contribution cannot simply be “we combined corruptions.”

A stronger surgical design would ask whether interaction effects exceed what single-shift performance predicts.

---

## 6. Temporal / video robustness

Recommended additional metrics:
- prediction volatility / flicker;
- segmental F1 / edit score for workflow tasks;
- recovery time after a corrupted/missing burst;
- transition timing error;
- consistency across adjacent frames;
- worst-window performance;
- burst-level failure rate.

For segmentation:
- framewise Dice/IoU;
- temporal mask consistency;
- failure duration;
- recovery after degradation.

P0.4 found direct emerging packet-loss corruption in Endo-C6 for temporal VLMs, but not a mature standardized frame-loss/jitter protocol for conventional surgical phase/segmentation tasks.

---

## 7. Adaptation-setting disclosure

Use precise labels:

- **DG:** no target-domain data during training.
- **UDA:** unlabeled target-domain data are used.
- **Supervised/few-shot adaptation:** labeled target-domain samples are used.
- **Test-time adaptation:** target test stream influences the model at deployment.

Do not compare these as if they solve the same information setting.

---

## 8. Model-selection leakage

Do not choose hyperparameters or corruption severity using the final external/OOD test set.

Recommended:
- source-domain validation for DG;
- separate target adaptation/calibration split where adaptation is allowed;
- untouched shifted test procedures.

P0.5 will separately define calibration/conformal splits.

---

## 9. Robustness is multidimensional

A model may:
- have higher clean performance but larger shift degradation;
- have lower clean performance but better relative retention;
- fail catastrophically only on one shift;
- appear robust on average while unstable temporally.

Therefore report **clean accuracy and robustness separately** rather than compressing them into one unqualified “best model” statement.

---

# P0.4 evaluation decision

Later experiments should report a **shift profile**, not a single robustness number:

`clean + each single shift + natural external shift + compound shift + temporal shift (when justified) + worst-case summary`.
