# P0.5 Reliable-Inference Source Index

## RI01 — On Calibration of Modern Neural Networks
- **Authors:** Guo C, Pleiss G, Sun Y, Weinberger KQ
- **Year / venue:** 2017 — ICML
- **Evidence type:** General foundational calibration
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** Calibration
- **Method:** Temperature scaling and post-hoc calibration
- **DOI/URL:** https://proceedings.mlr.press/v70/guo17a.html
- **P0.5 finding:** Modern neural networks can be miscalibrated; temperature scaling is a strong simple post-hoc baseline.
- **Boundary:** In-distribution benchmark setting; calibration under shift requires separate evidence.

## RI02 — Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift
- **Authors:** Ovadia Y et al.
- **Year / venue:** 2019 — NeurIPS
- **Evidence type:** General shift-UQ benchmark
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** Calibration under shift
- **Method:** Large-scale comparison of probabilistic/UQ methods
- **DOI/URL:** https://papers.neurips.cc/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html
- **P0.5 finding:** Accuracy and calibration degrade under dataset shift; ordinary post-hoc calibration can fall short, while model-marginalizing approaches are comparatively strong.
- **Boundary:** Natural-image/general ML benchmark, not surgical.

## RI03 — Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles
- **Authors:** Lakshminarayanan B, Pritzel A, Blundell C
- **Year / venue:** 2017 — NeurIPS
- **Evidence type:** General UQ method
- **Scope:** General
- **Task:** Classification/regression
- **Reliability topic:** Epistemic/predictive UQ
- **Method:** Deep ensembles
- **DOI/URL:** https://proceedings.neurips.cc/paper_files/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Paper.pdf
- **P0.5 finding:** Independent ensembles provide a simple high-quality predictive-uncertainty baseline without full Bayesian inference.
- **Boundary:** Compute/storage cost scales with number of models.

## RI04 — Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning
- **Authors:** Gal Y, Ghahramani Z
- **Year / venue:** 2016 — ICML
- **Evidence type:** General UQ method
- **Scope:** General
- **Task:** Classification/regression
- **Reliability topic:** Epistemic UQ
- **Method:** Monte Carlo dropout
- **DOI/URL:** https://proceedings.mlr.press/v48/gal16.html
- **P0.5 finding:** Inference-time dropout can approximate Bayesian model uncertainty using repeated stochastic forward passes.
- **Boundary:** Approximation quality and calibration are task/model dependent.

## RI05 — What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?
- **Authors:** Kendall A, Gal Y
- **Year / venue:** 2017 — NeurIPS
- **Evidence type:** General UQ taxonomy/method
- **Scope:** General
- **Task:** Segmentation/depth
- **Reliability topic:** Aleatoric vs epistemic UQ
- **Method:** Bayesian + heteroscedastic uncertainty modeling
- **DOI/URL:** https://arxiv.org/abs/1703.04977
- **P0.5 finding:** Provides the widely used aleatoric/epistemic distinction and models both in computer vision.
- **Boundary:** The conceptual decomposition is useful, but practical disentanglement is model-dependent.

## RI06 — Uncertainty Estimation in Medical Image Classification: Systematic Review
- **Authors:** Kurz A et al.
- **Year / venue:** 2022 — JMIR Medical Informatics 10(8):e36427
- **Evidence type:** Systematic review
- **Scope:** Medical imaging
- **Task:** Classification
- **Reliability topic:** UQ review
- **Method:** Systematic review of 22 studies
- **DOI/URL:** https://medinform.jmir.org/2022/8/e36427
- **P0.5 finding:** MC dropout and deep ensembles were the most frequently used UQ methods; metrics and evaluation practice were heterogeneous.
- **Boundary:** Classification-only review covering literature through 2021.

## RI07 — A review of uncertainty quantification in medical image analysis: Probabilistic and non-probabilistic methods
- **Authors:** Huang L, Ruan S, Xing Y, Feng M
- **Year / venue:** 2024 — Medical Image Analysis 97:103223
- **Evidence type:** Review
- **Scope:** Medical imaging
- **Task:** Multiple
- **Reliability topic:** UQ review
- **Method:** Probabilistic + non-probabilistic UQ taxonomy
- **DOI/URL:** https://doi.org/10.1016/j.media.2024.103223
- **P0.5 finding:** Medical-imaging UQ spans probabilistic, ensemble, deterministic, calibration and other strategies with task-dependent evaluation.
- **Boundary:** Broad review; not surgical-specific.

## RI08 — Uncertainty quantification for artificial intelligence in medical imaging: what every radiologist needs to know
- **Authors:** Vega Lara F et al.
- **Year / venue:** 2026 — Abdominal Radiology
- **Evidence type:** Clinical-oriented review
- **Scope:** Medical imaging
- **Task:** Multiple
- **Reliability topic:** Clinical UQ translation
- **Method:** Narrative review
- **DOI/URL:** https://doi.org/10.1007/s00261-026-05714-8
- **P0.5 finding:** Distinguishes prediction confidence from UQ and highlights triage, thresholding, calibration, computational cost and prospective-validation challenges.
- **Boundary:** Radiology-focused and narrative, not surgical.

## RI09 — Confidence Calibration and Predictive Uncertainty Estimation for Deep Medical Image Segmentation
- **Authors:** Mehrtash A et al.
- **Year / venue:** 2020 — IEEE Transactions on Medical Imaging 39(12):3868–3878
- **Evidence type:** Medical segmentation primary
- **Scope:** Medical imaging
- **Task:** Semantic segmentation
- **Reliability topic:** Calibration/UQ
- **Method:** Calibration and predictive uncertainty for FCNs
- **DOI/URL:** https://doi.org/10.1109/TMI.2020.3006437
- **P0.5 finding:** Medical segmentation networks can be poorly calibrated and overconfident on correct and erroneous pixels; calibration/UQ must be evaluated explicitly.
- **Boundary:** Non-surgical datasets.

## RI10 — Improving Calibration and Out-of-Distribution Detection in Deep Models for Medical Image Segmentation
- **Authors:** Karimi D, Gholipour A
- **Year / venue:** 2023 — IEEE Transactions on Artificial Intelligence 4(2):383–397
- **Evidence type:** Medical segmentation primary
- **Scope:** Medical imaging
- **Task:** Segmentation
- **Reliability topic:** Calibration + OOD
- **Method:** Multi-task calibration + spectral feature OOD detection
- **DOI/URL:** https://doi.org/10.1109/TAI.2022.3159510
- **P0.5 finding:** Multi-task training improves calibration and spectral feature-map signatures can identify OOD segmentation inputs.
- **Boundary:** Medical imaging rather than surgical video.

## RI11 — Failure Detection in Deep Neural Networks for Medical Imaging
- **Authors:** Ahmed S et al.
- **Year / venue:** 2022 — Frontiers in Medical Technology 4:919046
- **Evidence type:** Medical reliability primary
- **Scope:** Medical imaging
- **Task:** Classification
- **Reliability topic:** Failure detection
- **Method:** Bayesian DNN/self-assessment under natural noise
- **DOI/URL:** https://doi.org/10.3389/fmedt.2022.919046
- **P0.5 finding:** Frames failure detection as identifying likely model errors rather than merely identifying OOD inputs.
- **Boundary:** Not surgical and method/task-specific.

## RI12 — Uncertainty Estimation for Safety-critical Scene Segmentation via Fine-grained Reward Maximization
- **Authors:** Yang H et al.
- **Year / venue:** 2023 — NeurIPS 2023
- **Evidence type:** Direct surgical primary
- **Scope:** Surgical direct
- **Task:** Surgical scene segmentation
- **Reliability topic:** Calibration/UQ
- **Method:** FGRM evidential uncertainty fine-tuning
- **DOI/URL:** https://papers.neurips.cc/paper_files/paper/2023/hash/71ec377d5df1fc61ee7770857820519b-Abstract-Conference.html
- **P0.5 finding:** Direct surgical evidence that scene-segmentation uncertainty/calibration can be optimized while preserving task accuracy using one-pass inference.
- **Boundary:** Method-specific; does not by itself establish robustness under the full P0.4 shift suite.

## RI13 — Surgical Phase Recognition in Laparoscopic Cholecystectomy
- **Authors:** Li Y et al.
- **Year / venue:** 2024 — Procedia Computer Science 239:2006–2012
- **Evidence type:** Direct surgical primary
- **Scope:** Surgical direct
- **Task:** Phase recognition
- **Reliability topic:** Calibrated confidence
- **Method:** Calibrated confidence for dynamic model switching
- **DOI/URL:** https://doi.org/10.1016/j.procs.2024.06.386
- **P0.5 finding:** Calibrated confidence is already used operationally in surgical phase recognition to choose between models.
- **Boundary:** Does not systematically evaluate reliability across natural/controlled distribution shifts.

## RI14 — When Surgery Meets the Unknown: Uncertainty-Aware Open-Set Recognition for Surgery Phase Classification
- **Authors:** Geyer S, Kalogeiton V, Roitberg A
- **Year / venue:** 2026 — VISAPP 2026
- **Evidence type:** Direct surgical primary
- **Scope:** Surgical direct
- **Task:** Phase recognition
- **Reliability topic:** Open-set/OOD
- **Method:** Benchmark of open-set algorithms + evidential GEAR
- **DOI/URL:** https://doi.org/10.5220/0014311000004084
- **P0.5 finding:** Open-set surgical phase recognition and uncertainty-aware rejection are already directly studied on cholecystectomy data.
- **Boundary:** Open-set unknown-class setting differs from covariate-shift failure prediction.

## RI15 — Scene graph-guided uncertainty decomposition improves confidence calibration in surgical visual question answering
- **Authors:** Song J et al.
- **Year / venue:** 2026 — Frontiers in Medicine 13:1849346
- **Evidence type:** Direct surgical primary
- **Scope:** Surgical direct
- **Task:** Surgical VQA
- **Reliability topic:** Calibration + selective answering
- **Method:** Scene-graph UQ decomposition + Dirichlet calibration
- **DOI/URL:** https://doi.org/10.3389/fmed.2026.1849346
- **P0.5 finding:** Direct surgical evidence combines uncertainty decomposition, calibration and selective answering; reported accuracy 63.58%, ECE 16.97%, risk-coverage AUC 0.0861.
- **Boundary:** VQA differs from phase recognition/segmentation and uses constructed scene-graph pipeline.

## RI16 — Meta-SurDiff: Classification Diffusion Model Optimized by Meta Learning is Reliable for Online Surgical Phase Recognition
- **Authors:** Li Y et al.
- **Year / venue:** 2025 — arXiv:2506.14181
- **Evidence type:** Direct surgical preprint
- **Scope:** Surgical direct
- **Task:** Online phase recognition
- **Reliability topic:** Frame-level uncertainty
- **Method:** Classification diffusion + meta-learning
- **DOI/URL:** https://arxiv.org/abs/2506.14181
- **P0.5 finding:** Emerging work explicitly models frame-level uncertainty for online phase recognition across five datasets.
- **Boundary:** Preprint; reliability/calibration claims require peer-reviewed confirmation.

## RI17 — OpenMIBOOD: Open Medical Imaging Benchmarks for Out-Of-Distribution Detection
- **Authors:** Gutbrod M, Rauber D, Nunes DW, Palm C
- **Year / venue:** 2025 — CVPR 2025
- **Evidence type:** Medical OOD benchmark with surgical domain
- **Scope:** Surgical-relevant medical benchmark
- **Task:** OOD detection
- **Reliability topic:** OOD benchmark
- **Method:** 24 post-hoc OOD methods across 3 medical benchmarks
- **DOI/URL:** https://openaccess.thecvf.com/content/CVPR2025/html/Gutbrod_OpenMIBOOD_Open_Medical_Imaging_Benchmarks_for_Out-Of-Distribution_Detection_CVPR_2025_paper.html
- **P0.5 finding:** PhaKIR is a dedicated endoscopy benchmark with smoke covariate shift plus near/far OOD datasets; rankings from natural-image OOD do not directly transfer to medical imaging.
- **Boundary:** OOD detection is not the same as predicting whether a surgical model output is wrong.

## RI18 — A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks
- **Authors:** Hendrycks D, Gimpel K
- **Year / venue:** 2017 — ICLR
- **Evidence type:** General OOD/failure foundation
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** OOD/failure detection
- **Method:** Maximum softmax probability
- **DOI/URL:** https://mlanthology.org/iclr/2017/hendrycks2017iclr-baseline/
- **P0.5 finding:** Provides the canonical simple confidence baseline for error/OOD detection.
- **Boundary:** OOD membership and prediction error are related but not equivalent.

## RI19 — Energy-based Out-of-distribution Detection
- **Authors:** Liu W et al.
- **Year / venue:** 2020 — NeurIPS
- **Evidence type:** General OOD method
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** OOD detection
- **Method:** Energy score
- **DOI/URL:** https://proceedings.neurips.cc/paper/2020/hash/f5496252609c43eb8a3d147ab9b9c006-Abstract.html
- **P0.5 finding:** Energy scores provide a strong post-hoc/energy-based baseline for OOD detection.
- **Boundary:** General benchmark; medical/surgical performance must be verified rather than assumed.

## RI20 — Selective Classification for Deep Neural Networks
- **Authors:** Geifman Y, El-Yaniv R
- **Year / venue:** 2017 — arXiv / selective-classification foundation
- **Evidence type:** General selective prediction
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** Selective prediction
- **Method:** Confidence-based reject option with risk control
- **DOI/URL:** https://arxiv.org/abs/1705.08500
- **P0.5 finding:** Formalizes the accuracy/risk versus coverage trade-off for deep classifiers with rejection.
- **Boundary:** General classification; task-specific confidence for segmentation/temporal outputs differs.

## RI21 — SelectiveNet: A Deep Neural Network with an Integrated Reject Option
- **Authors:** Geifman Y, El-Yaniv R
- **Year / venue:** 2019 — ICML
- **Evidence type:** General selective prediction
- **Scope:** General
- **Task:** Classification/regression
- **Reliability topic:** Selective prediction
- **Method:** Integrated selection head and coverage objective
- **DOI/URL:** https://proceedings.mlr.press/v97/geifman19a.html
- **P0.5 finding:** End-to-end selective prediction can optimize risk–coverage rather than using only post-hoc thresholds.
- **Boundary:** Requires retraining; deployment constraints may favor post-hoc monitors.

## RI22 — Selective Prediction for Semantic Segmentation under Distribution Shift
- **Authors:** Borges BLC, Pacheco BM, Silva D
- **Year / venue:** 2024 — ICLR 2024 Workshop
- **Evidence type:** Medical segmentation workshop
- **Scope:** Medical imaging
- **Task:** Semantic segmentation
- **Reliability topic:** Selective segmentation under shift
- **Method:** Post-hoc image-level confidence estimators
- **DOI/URL:** https://mlanthology.org/iclrw/2024/borges2024iclrw-selective/
- **P0.5 finding:** Selective prediction for semantic segmentation under distribution shift is already directly evaluated in medical imaging.
- **Boundary:** Workshop paper; not surgical-specific.

## RI23 — Soft Dice Confidence: A Near-Optimal Confidence Estimator for Selective Prediction in Semantic Segmentation
- **Authors:** Borges BLC, Pacheco BM, Silva D
- **Year / venue:** 2026 — Machine Learning 115:176
- **Evidence type:** Medical segmentation selective prediction
- **Scope:** Medical imaging
- **Task:** Semantic segmentation
- **Reliability topic:** Selective segmentation
- **Method:** Image-level Soft Dice Confidence
- **DOI/URL:** https://doi.org/10.1007/s10994-026-07096-w
- **P0.5 finding:** Provides a theoretically motivated image-level confidence estimator for Dice-oriented selective segmentation and evaluates six medical-imaging tasks including OOD scenarios.
- **Boundary:** Image-level abstention may be too coarse for surgical overlays; not surgical-specific.

## RI24 — Learning to Abstain: Reliable Medical Image Segmentation With Rejection Option
- **Authors:** Sanisoglu MA, Navab N, Kim ST
- **Year / venue:** 2026 — IEEE Access 14:32655–32665
- **Evidence type:** Medical segmentation selective prediction
- **Scope:** Medical imaging
- **Task:** Segmentation
- **Reliability topic:** Selective segmentation
- **Method:** Pixel-level rejection training
- **DOI/URL:** https://doi.org/10.1109/ACCESS.2026.3669004
- **P0.5 finding:** Directly trains segmentation models to abstain on uncertain pixels and reports improved accepted-pixel Dice across coverage levels.
- **Boundary:** Non-surgical medical segmentation; pixel-level abstention has different human-interface implications.

## RI25 — Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift
- **Authors:** Kwon H, Kim DJ
- **Year / venue:** 2026 — Scientific Reports 16:10016
- **Evidence type:** Clinical selective/conformal primary
- **Scope:** Clinical adjacent
- **Task:** Sepsis classification
- **Reliability topic:** Calibration + CP + deferral under shift
- **Method:** Temperature scaling + split/Mondrian/weighted CP + cost-aware deferral
- **DOI/URL:** https://doi.org/10.1038/s41598-026-40637-w
- **P0.5 finding:** A combined calibrated conformal deferral pipeline reduces retained-case error at 80% coverage by 49.6% ID and 46.7% OOD; weighted CP is most robust under temporal shift.
- **Boundary:** Tabular sepsis triage, not imaging/surgery; weighted CP assumes access to unlabeled target covariates.

## RI26 — Uncertainty Sets for Image Classifiers Using Conformal Prediction
- **Authors:** Angelopoulos AN, Bates S, Jordan M, Malik J
- **Year / venue:** 2021 — ICLR
- **Evidence type:** Conformal classification foundation
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** Conformal prediction
- **Method:** RAPS prediction sets
- **DOI/URL:** https://mlanthology.org/iclr/2021/angelopoulos2021iclr-uncertainty/
- **P0.5 finding:** Conformal prediction can wrap a classifier to achieve finite-sample marginal coverage under exchangeability with efficient label sets.
- **Boundary:** Coverage guarantee relies on calibration/test exchangeability unless using shift-aware variants.

## RI27 — Conformal Prediction Under Covariate Shift
- **Authors:** Tibshirani RJ, Barber RF, Candès EJ, Ramdas A
- **Year / venue:** 2019 — NeurIPS
- **Evidence type:** Shift-aware conformal foundation
- **Scope:** General
- **Task:** Prediction sets/intervals
- **Reliability topic:** Conformal under shift
- **Method:** Importance-weighted conformal prediction
- **DOI/URL:** https://papers.nips.cc/paper/2019/hash/8fb21ee7a2207526da55a679f0332de2-Abstract.html
- **P0.5 finding:** Coverage can be extended to covariate shift using likelihood-ratio weighting when the shift assumptions and density ratios are available/estimable.
- **Boundary:** Assumes covariate-shift structure and reliable weighting; not arbitrary concept shift.

## RI28 — Adaptive Conformal Inference Under Distribution Shift
- **Authors:** Gibbs I, Candès E
- **Year / venue:** 2021 — NeurIPS
- **Evidence type:** Online shift-aware conformal foundation
- **Scope:** General
- **Task:** Online prediction sets
- **Reliability topic:** Adaptive conformal
- **Method:** Adaptive online alpha update
- **DOI/URL:** https://proceedings.neurips.cc/paper/2021/hash/0d441de75945e5acbc865406fc9a2559-Abstract.html
- **P0.5 finding:** Adaptive conformal inference targets long-run coverage under time-varying distributions without ordinary exchangeability.
- **Boundary:** Long-run frequency control differs from per-case or subgroup guarantees.

## RI29 — Distribution-free, Risk-controlling Prediction Sets
- **Authors:** Bates S, Angelopoulos A, Lei L, Malik J, Jordan MI
- **Year / venue:** 2021 — Journal of the ACM 68(6)
- **Evidence type:** Risk-control foundation
- **Scope:** General
- **Task:** Classification/multilabel/segmentation
- **Reliability topic:** Risk control
- **Method:** Risk-controlling prediction sets
- **DOI/URL:** https://doi.org/10.1145/3478535
- **P0.5 finding:** Extends finite-sample risk control beyond simple classification coverage to general losses including image segmentation.
- **Boundary:** Holdout calibration and risk definition are central; not a surgical deployment guarantee by itself.

## RI30 — Conformal Prediction for Image Segmentation Using Morphological Prediction Sets
- **Authors:** Mossina L, Friedrich C
- **Year / venue:** 2025 — MICCAI 2025
- **Evidence type:** Medical segmentation conformal
- **Scope:** Medical imaging
- **Task:** Binary segmentation
- **Reliability topic:** Conformal segmentation
- **Method:** Morphological dilation prediction sets
- **DOI/URL:** https://doi.org/10.1007/978-3-032-04965-0_8
- **P0.5 finding:** Model-agnostic conformal mask margins provide coverage-controlled segmentation uncertainty on medical applications.
- **Boundary:** Binary masks; morphology-based coverage does not directly solve instance-level surgical segmentation.

## RI31 — Conformal forecasting for surgical instrument trajectory
- **Authors:** Sangalli S et al.
- **Year / venue:** 2025 — MICCAI 2025
- **Evidence type:** Direct surgical conformal primary
- **Scope:** Surgical direct
- **Task:** Instrument trajectory forecasting
- **Reliability topic:** Conformal prediction
- **Method:** Standard CP + conformalized quantile regression
- **DOI/URL:** https://papers.miccai.org/miccai-2025/0168-Paper0260.html
- **P0.5 finding:** Direct surgical guidance work applies CP/CQR to instrument trajectory forecasts with coverage/interval-size evaluation and multiple-testing corrections.
- **Boundary:** Trajectory forecasting, not phase recognition or image segmentation; in-house data.

## RI32 — A critical perspective on finite sample conformal prediction theory in medical applications
- **Authors:** Kladny KR et al.
- **Year / venue:** 2026 — Artificial Intelligence in Medicine 180:103462
- **Evidence type:** Medical conformal critique
- **Scope:** Medical imaging
- **Task:** Medical classification
- **Reliability topic:** Conformal assumptions/calibration-size
- **Method:** Theory + empirical critique
- **DOI/URL:** https://doi.org/10.1016/j.artmed.2026.103462
- **P0.5 finding:** Marginal finite-sample coverage can be practically misleading with small one-time calibration sets because calibration-set-conditional coverage varies substantially.
- **Boundary:** Does not invalidate conformal theory; clarifies what the standard marginal guarantee does and does not mean.

## RI33 — Reliable Uncertainty Under Class Imbalance and Distribution Shift: Class-Conditional Conformal Prediction of Multiple Sclerosis
- **Authors:** Millar AS et al.
- **Year / venue:** 2026 — medRxiv / PubMed-indexed preprint
- **Evidence type:** Medical conformal under shift
- **Scope:** Medical imaging
- **Task:** MRI classification
- **Reliability topic:** Class-conditional conformal under shift
- **Method:** Marginal vs class-conditional CP across scanner/degradation shifts
- **DOI/URL:** https://www.medrxiv.org/content/10.64898/2026.05.12.26353057v1
- **P0.5 finding:** Marginal CP can hide severe minority-class undercoverage: at 1.5T, MS coverage was 16.9% vs 95.2% controls; class-conditional CP improved MS coverage to 77.5%.
- **Boundary:** Preprint and non-surgical; even class-conditional coverage remained below nominal under severe shift.

## RI34 — Beyond Uncertainty: Generalizable Failure Monitoring for Surgical Segmentation under Acquisition Degradation
- **Authors:** Pham HD, Cao DPM, Huynh TT
- **Year / venue:** 2026 — arXiv:2608.16748 / MICCAI 2026 UNSURE workshop
- **Evidence type:** Direct surgical recent preprint/workshop
- **Scope:** Surgical direct
- **Task:** Instrument segmentation
- **Reliability topic:** Failure monitoring + conformal calibration under shift
- **Method:** TCSR-Monitor: confidence + shape + temporal consistency + image quality; Mondrian conformal calibration
- **DOI/URL:** https://arxiv.org/abs/2608.16748
- **P0.5 finding:** Directly targets confident surgical segmentation failures under acquisition degradation; within corrupted frames reports AUROC 0.946 versus entropy 0.594 and shows severity-aware conformal calibration, but false alarms remain substantial.
- **Boundary:** Very recent; EndoVis 2017/corruption benchmark; global threshold false alarms up to ~40% at moderate corruption and SAM2 transfer limitations.

## RI35 — Measuring Calibration in Deep Learning
- **Authors:** Nixon J et al.
- **Year / venue:** 2019 — CVPR Workshops
- **Evidence type:** Calibration metric methodology
- **Scope:** General
- **Task:** Classification
- **Reliability topic:** Calibration metrics
- **Method:** ECE variants / adaptive calibration
- **DOI/URL:** https://openaccess.thecvf.com/content_CVPRW_2019/html/Uncertainty_and_Robustness_in_Deep_Visual_Learning/Nixon_Measuring_Calibration_in_Deep_Learning_CVPRW_2019_paper.html
- **P0.5 finding:** Calibration conclusions can depend strongly on binning, class conditioning, probability selection and norm; ECE alone is insufficient.
- **Boundary:** General classification.

## RI36 — A Novel Characterization of the Population Area Under the Risk Coverage Curve (AURC) and Rates of Finite Sample Estimators
- **Authors:** Zhou H et al.
- **Year / venue:** 2025 — ICML 2025
- **Evidence type:** Selective-prediction metric methodology
- **Scope:** General
- **Task:** Selective classification
- **Reliability topic:** Risk-coverage metric
- **Method:** AURC statistical characterization
- **DOI/URL:** https://proceedings.mlr.press/v267/zhou25y.html
- **P0.5 finding:** Formalizes AURC as a principal metric for evaluating selective classifiers across coverage thresholds.
- **Boundary:** General classification; segmentation risk must be defined task-appropriately.
