# P0.4 Distribution-Shift Source Index

## SH01 — Comparative validation of multi-instance instrument segmentation in endoscopy: Results of the ROBUST-MIS 2019 challenge
- **Authors:** Roß T et al.
- **Year / venue:** 2021 — Medical Image Analysis 70:101920
- **Evidence type:** Peer-reviewed challenge report
- **DOI/URL:** https://doi.org/10.1016/j.media.2020.101920
- **Task:** Instrument binary/instance segmentation and detection
- **Shift:** Natural procedure/domain gap; challenging blood/smoke/motion artifacts
- **Dataset/domain:** ROBUST-MIS
- **Method/evaluation:** Multi-team benchmark; increasing domain-gap validation stages
- **P0.4 finding:** A canonical surgical robustness/generalization benchmark; performance worsens as domain gap increases.
- **Boundary:** Primarily colorectal procedures from one institutional ecosystem; not a network/video-transport study.

## SH02 — Limited generalizability of single deep neural network for surgical instrument segmentation in different surgical environments
- **Authors:** Kitaguchi D et al.
- **Year / venue:** 2022 — Scientific Reports 12:12575
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1038/s41598-022-16923-8
- **Task:** Instrument segmentation
- **Shift:** Recording system; instrument morphology/version; surgery/procedure background
- **Dataset/domain:** 5,238 images from 128 intraoperative videos
- **Method/evaluation:** Cross-condition testing with fixed model
- **P0.4 finding:** Generalization falls even under seemingly modest changes in camera system, instrument or procedure.
- **Boundary:** Single study setting and task; factors are controlled but not a multicentre benchmark.

## SH03 — Challenges in multi-centric generalization: phase and step recognition in Roux-en-Y gastric bypass surgery
- **Authors:** Lavanchy JL et al.
- **Year / venue:** 2024 — International Journal of Computer Assisted Radiology and Surgery 19:2249–2257
- **Evidence type:** Peer-reviewed multicentre study
- **DOI/URL:** https://doi.org/10.1007/s11548-024-03166-3
- **Task:** Phase and step recognition
- **Shift:** Hospital/centre; workflow/technique; recording environment
- **Dataset/domain:** MultiBypass140 (70 Strasbourg + 70 Bern)
- **Method/evaluation:** Within-centre, pooled, and cross-centre experiments
- **P0.4 finding:** Mono-centre models generalize poorly cross-centre; multicentre training improves generalization.
- **Boundary:** Two centres and one procedure; centre shift bundles several causal factors.

## SH04 — Comparative validation of surgical phase recognition, instrument keypoint estimation, and instrument instance segmentation in endoscopy: Results of the PhaKIR 2024 challenge
- **Authors:** Rueckert T et al.
- **Year / venue:** 2026 — Medical Image Analysis 109:103945
- **Evidence type:** Peer-reviewed multicentre challenge
- **DOI/URL:** https://doi.org/10.1016/j.media.2026.103945
- **Task:** Phase recognition; keypoints; instrument instance segmentation
- **Shift:** Medical centre / acquisition / workflow domain shift
- **Dataset/domain:** 13 full cholecystectomies from 3 centres
- **Method/evaluation:** Challenge evaluation across centres/tasks
- **P0.4 finding:** Methods show poor cross-centre generalizability across all three evaluated tasks.
- **Boundary:** Small number of full procedures; challenge-specific protocols.

## SH05 — Inter-hospital transferability of AI: A case study on phase recognition in cholecystectomy
- **Authors:** Renz-Kiefel L et al.
- **Year / venue:** 2025 — Computers in Biology and Medicine 192:110235
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1016/j.compbiomed.2025.110235
- **Task:** Surgical phase recognition
- **Shift:** Hospital/surgeon/environment; manufacturer-specific instrument cues
- **Dataset/domain:** 104 public surgeries from 3 centres + 21 local MHB videos
- **Method/evaluation:** Public-only, local-only, combined and fine-tuned training
- **P0.4 finding:** Public-only models transferred poorly to the local centre; diverse + site-specific data improved transfer.
- **Boundary:** Task/procedure specific; local adaptation uses target-site data.

## SH06 — Optimizing latent graph representations of surgical scenes for unseen domain generalization
- **Authors:** Satyanaik S et al.
- **Year / venue:** 2024 — International Journal of Computer Assisted Radiology and Surgery 19:1243–1250
- **Evidence type:** Peer-reviewed multicentre method
- **DOI/URL:** https://doi.org/10.1007/s11548-024-03121-2
- **Task:** Surgical scene understanding / domain generalization
- **Shift:** Unseen centre; workflow/camera/patient variation
- **Dataset/domain:** Multicentre surgical-scene data
- **Method/evaluation:** Object-centric latent graph representation
- **P0.4 finding:** Object-centric scene representations are investigated to reduce unseen-centre domain sensitivity.
- **Boundary:** Method-specific study; not a standardized corruption benchmark.

## SH07 — Overcoming color domain shift in endoscopic spine surgery: robust instrument segmentation via aggressive photometric augmentation
- **Authors:** Rhee W et al.
- **Year / venue:** 2026 — Scientific Reports
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1038/s41598-026-61273-4
- **Task:** Instrument segmentation
- **Shift:** Inter-institutional color/photometric shift
- **Dataset/domain:** Internal/external endoscopic-spine cohorts; 10,662 segmentations
- **Method/evaluation:** Photometric augmentation; CIELAB/MMD analysis
- **P0.4 finding:** Baseline external DSC drops markedly; aggressive photometric augmentation restores strong external performance and reduces feature-domain discrepancy.
- **Boundary:** Color shift is a specific factor; recent early-version article.

## SH08 — Benchmarking deep learning pipelines for surgical instrument segmentation in endoscopic spine surgery: cross-dataset evaluation under deployment-realistic conditions
- **Authors:** Mun BS et al.
- **Year / venue:** 2026 — European Spine Journal
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1007/s00586-026-10162-5
- **Task:** Instrument segmentation
- **Shift:** Temporal external + cross-dataset/institutional shift
- **Dataset/domain:** SNUBH biportal (56 patients) + SEA uniportal (60 patients)
- **Method/evaluation:** Seven pipelines; patient-level internal/temporal/cross-dataset evaluation
- **P0.4 finding:** Cross-dataset performance can be detector-limited even for foundation-model pipelines; broader domain training substantially improves external results.
- **Boundary:** Endoscopic-spine task; small external samples limit equivalence claims.

## SH09 — SegSTRONG-C: Segmenting Surgical Tools Robustly On Non-adversarial Generated Corruptions — An EndoVis'24 Challenge
- **Authors:** Ding H et al.
- **Year / venue:** 2024–2026 — EndoVis / arXiv 2407.11906
- **Evidence type:** Challenge report / preprint
- **DOI/URL:** https://arxiv.org/abs/2407.11906
- **Task:** Binary robot-tool segmentation
- **Shift:** Photo-realistic smoke; over-bleeding; low brightness; digital corruptions
- **Dataset/domain:** Mock endoscopic video sequences (6600 train / 3600 val / 5400 test cases on challenge site)
- **Method/evaluation:** Corruption benchmark + augmentation baselines
- **P0.4 finding:** Direct surgical benchmark showing plausible non-adversarial corruptions materially challenge tool segmentation.
- **Boundary:** Mock endoscopy rather than human surgery; current canonical report is preprint/challenge material.

## SH10 — CaRTS: Causality-Driven Robot Tool Segmentation from Vision and Kinematics Data
- **Authors:** Ding H et al.
- **Year / venue:** 2022 — MICCAI 2022
- **Evidence type:** Peer-reviewed conference
- **DOI/URL:** https://doi.org/10.1007/978-3-031-16449-1_37
- **Task:** Robot-tool segmentation
- **Shift:** Counterfactual low brightness, smoke, blood, altered background
- **Dataset/domain:** Controlled synthetic + real dVRK scenarios
- **Method/evaluation:** Causal vision + robot-kinematics model
- **P0.4 finding:** Kinematics-informed causal segmentation preserves performance better than image-only baselines under counterfactual visual changes.
- **Boundary:** Controlled dVRK setting; not human clinical deployment and not network telemetry.

## SH11 — Rethinking causality-driven robot tool segmentation with temporal constraints
- **Authors:** Ding H et al.
- **Year / venue:** 2023 — International Journal of Computer Assisted Radiology and Surgery 18:1009–1016
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1007/s11548-023-02872-8
- **Task:** Robot-tool segmentation
- **Shift:** Unseen visual domains including smoke/blood; temporal robustness context
- **Dataset/domain:** CaRTS video-domain experiments
- **Method/evaluation:** Temporal constraints + kinematics correction + spatio-temporal regularization
- **P0.4 finding:** Temporal observability improves CaRTS convergence and maintains performance across tested domains.
- **Boundary:** Not a controlled frame-loss/jitter study.

## SH12 — Simulation-to-real domain adaptation with teacher–student learning for endoscopic instrument segmentation
- **Authors:** Sahu M et al.
- **Year / venue:** 2021 — International Journal of Computer Assisted Radiology and Surgery 16:849–859
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1007/s11548-021-02383-4
- **Task:** Instrument segmentation
- **Shift:** Simulation-to-real; real-domain visual gap
- **Dataset/domain:** Simulation + three real endoscopic datasets
- **Method/evaluation:** Teacher–student UDA using labeled synthetic + unlabeled real data
- **P0.4 finding:** Unlabeled real target frames improve sim-to-real segmentation over pure simulation training.
- **Boundary:** UDA assumes access to target-domain unlabeled data.

## SH13 — Graph-Based Surgical Instrument Adaptive Segmentation via Domain-Common Knowledge
- **Authors:** Liu J, Guo X, Yuan Y
- **Year / venue:** 2022 — IEEE Transactions on Medical Imaging 41:715–726
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1109/TMI.2021.3121138
- **Task:** Instrument segmentation
- **Shift:** Unlabeled target-domain shift
- **Dataset/domain:** Multiple surgical segmentation domain-adaptation tasks
- **Method/evaluation:** Interactive Graph Network; domain-common knowledge UDA
- **P0.4 finding:** Representative surgical UDA work showing target-domain adaptation is already well established as a method family.
- **Boundary:** Needs unlabeled target domain; not unseen-domain DG.

## SH14 — Generalizing Surgical Instruments Segmentation to Unseen Domains with One-to-Many Synthesis
- **Authors:** Wang A et al.
- **Year / venue:** 2023 — IEEE/RSJ IROS 2023
- **Evidence type:** Peer-reviewed conference
- **DOI/URL:** https://doi.org/10.1109/IROS55552.2023.10341609
- **Task:** Instrument segmentation
- **Shift:** Unseen real domains / site-patient appearance variation
- **Dataset/domain:** Endo2017; Endo2018; RoboTool
- **Method/evaluation:** One-to-many synthetic composition + hybrid augmentation
- **P0.4 finding:** Synthetic data diversification can improve unseen-domain surgical instrument segmentation.
- **Boundary:** Synthetic compositing does not reproduce every clinical shift mechanism.

## SH15 — SDA-CLIP: surgical visual domain adaptation using video and text labels
- **Authors:** Li Y et al.
- **Year / venue:** 2023 — Quantitative Imaging in Medicine and Surgery 13
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.21037/qims-23-376
- **Task:** Surgical action recognition
- **Shift:** Virtual-reality/simulation to clinical domain
- **Dataset/domain:** SurgVisDom
- **Method/evaluation:** Video-text CLIP domain adaptation
- **P0.4 finding:** Video-text semantic alignment improves hard and soft cross-domain surgical action recognition.
- **Boundary:** VR-to-clinical adaptation is not equivalent to hospital or communication shift.

## SH16 — Few-shot learning for surgical phase recognition: Performance and generalization in cholecystectomy
- **Authors:** Bajraktari F et al.
- **Year / venue:** 2026 — Computer Methods and Programs in Biomedicine 282:109386
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1016/j.cmpb.2026.109386
- **Task:** Phase recognition
- **Shift:** Cross-domain/domain-specific transfer with few-shot support
- **Dataset/domain:** Cholec80 + non-surgical/action pretraining splits
- **Method/evaluation:** Transformer few-shot learning
- **P0.4 finding:** Performance declines as training domain moves farther from surgical target; domain-specific support remains important.
- **Boundary:** Split definitions are study-specific and not a multicentre clinical benchmark.

## SH17 — Robustness evaluation of deep neural networks for endoscopic image analysis: Insights and strategies
- **Authors:** Jaspers TJM et al.
- **Year / venue:** 2024 — Medical Image Analysis 94:103157
- **Evidence type:** Peer-reviewed adjacent endoscopy robustness study
- **DOI/URL:** https://doi.org/10.1016/j.media.2024.103157
- **Task:** GI endoscopic CADe/CADx (adjacent, not surgery)
- **Shift:** Clinically calibrated blur/exposure/color/compression/resolution distortions; compound corruption
- **Dataset/domain:** Multiple endoscopy datasets + low-quality test set
- **Method/evaluation:** Clinically calibrated 10-level corruptions; augmentation/pretraining analysis
- **P0.4 finding:** Provides a strong severity-calibration and compound-corruption protocol precedent transferable as methodology, not surgical evidence.
- **Boundary:** GI endoscopy cancer detection/diagnosis rather than surgical video.

## SH18 — On the Robustness of Temporal Vision-Language Models for Surgical Endoscopy Videos
- **Authors:** Rashid D et al.
- **Year / venue:** 2026 — MICCAI 2026 / arXiv 2608.14262
- **Evidence type:** Accepted conference preprint
- **DOI/URL:** https://arxiv.org/abs/2608.14262
- **Task:** Temporal surgical/endoscopic video-language understanding
- **Shift:** Defocus; haze; motion blur; shot noise; cautery smoke; packet-loss bursts
- **Dataset/domain:** Kvasir; TEMSET-24K; CholecT50
- **Method/evaluation:** Endo-C6 fixed-high-severity controlled OOD benchmark + few-shot VeRA adaptation
- **P0.4 finding:** Emerging direct evidence that packet-loss-like and visual corruptions can collapse temporal VLM performance.
- **Boundary:** Very recent; fixed high severity; task is TVLM/video-text rather than conventional phase/segmentation.

## SH19 — Performance and Non-adversarial Robustness of the Segment Anything Model 2 in Surgical Video Segmentation
- **Authors:** Shen Y et al.
- **Year / venue:** 2024 — arXiv 2408.04098
- **Evidence type:** Preprint
- **DOI/URL:** https://arxiv.org/abs/2408.04098
- **Task:** Surgical video segmentation
- **Shift:** Smoke; bleeding; low illumination on SegSTRONG-C
- **Dataset/domain:** SegSTRONG-C
- **Method/evaluation:** Zero-shot SAM2 prompt-strategy robustness evaluation
- **P0.4 finding:** Foundation video segmentation is also evaluated under surgical non-adversarial corruptions; temporal prompting can affect robustness.
- **Boundary:** Preprint; prompt-based zero-shot setting.

## SH20 — Reducing prediction volatility in the surgical workflow recognition of endoscopic pituitary surgery
- **Authors:** Das A et al.
- **Year / venue:** 2022 — International Journal of Computer Assisted Radiology and Surgery 17:1445–1452
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1007/s11548-022-02599-y
- **Task:** Phase/step recognition
- **Shift:** Temporal instability from occlusion/endoscope withdrawal (not a controlled network shift)
- **Dataset/domain:** 50 pituitary-surgery videos
- **Method/evaluation:** Prediction-volatility metric + modal/threshold smoothing
- **P0.4 finding:** Temporal prediction instability is clinically relevant and can be reduced by smoothing.
- **Boundary:** Does not manipulate frame loss, jitter or packet loss.

## SH21 — SurgflowNet: Leveraging unannotated video for consistent endoscopic pituitary surgery workflow recognition
- **Authors:** Wijekoon A et al.
- **Year / venue:** 2026 — Artificial Intelligence in Medicine 172:103309
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1016/j.artmed.2025.103309
- **Task:** Workflow recognition
- **Shift:** Temporal prediction consistency; limited-label setting
- **Dataset/domain:** Pituitary surgical video / PitVis context
- **Method/evaluation:** Unannotated video + consistency loss
- **P0.4 finding:** Consistency-focused training reduces unstable workflow predictions.
- **Boundary:** Temporal consistency is not equivalent to communication-induced video corruption.

## SH22 — ROBUST-MIPS: A Combined Skeletal Pose and Instance Segmentation Dataset for Laparoscopic Surgical Instruments
- **Authors:** Han Z et al.
- **Year / venue:** 2026 — Scientific Data 13:684
- **Evidence type:** Peer-reviewed dataset descriptor
- **DOI/URL:** https://doi.org/10.1038/s41597-026-06938-5
- **Task:** Instrument pose + instance segmentation
- **Shift:** Inherits ROBUST-MIS procedure-domain structure
- **Dataset/domain:** 10,040 ROBUST-MIS images with added pose labels
- **Method/evaluation:** Pose/segmentation benchmark extension
- **P0.4 finding:** Extends the established robustness dataset to pose estimation and richer tool localization.
- **Boundary:** Derived from ROBUST-MIS; not independent shift evidence.

## SH23 — Domain-agnostic weakly supervised surgical instrument segmentation
- **Authors:** Peter R et al.
- **Year / venue:** 2026 — Scientific Reports 16:9337
- **Evidence type:** Peer-reviewed primary
- **DOI/URL:** https://doi.org/10.1038/s41598-026-43054-1
- **Task:** Instrument segmentation
- **Shift:** Cross surgical domain and imaging modality
- **Dataset/domain:** EndoVis2017; CaDIS; PASO-SIS
- **Method/evaluation:** PatchCore anomaly localization + SAM2 prompting
- **P0.4 finding:** A domain-agnostic, weakly supervised foundation-model pipeline is evaluated across diverse surgical modalities.
- **Boundary:** Different tasks/modalities complicate direct performance comparison; not a corruption benchmark.

## SH24 — RobustSurg: Tackling domain generalisation for out-of-distribution surgical scene segmentation
- **Authors:** Ali M et al.
- **Year / venue:** 2025 — arXiv 2512.02188
- **Evidence type:** Preprint
- **DOI/URL:** https://arxiv.org/abs/2512.02188
- **Task:** Surgical scene segmentation
- **Shift:** Unseen centre / imaging modality / style-content variation
- **Dataset/domain:** CholecSeg8k → newly curated HeiCholSeg; other OOD set
- **Method/evaluation:** Single-domain DG with style normalization/restitution/whitening
- **P0.4 finding:** Shows active work specifically targeting surgical OOD scene segmentation from one source domain.
- **Boundary:** Preprint; curated target dataset and claims require peer-reviewed confirmation.

## SH25 — CholecInstanceSeg: A Tool Instance Segmentation Dataset for Laparoscopic Surgery
- **Authors:** Alabi O et al.
- **Year / venue:** 2025 — Scientific Data 12:825
- **Evidence type:** Peer-reviewed dataset descriptor / contextual evidence
- **DOI/URL:** https://doi.org/10.1038/s41597-025-05163-w
- **Task:** Tool instance segmentation
- **Shift:** Observed hard cases: motion blur, smoke, blood/occlusion, reflections, lighting, lens dirtiness
- **Dataset/domain:** CholecInstanceSeg
- **Method/evaluation:** Annotation protocol explicitly covers difficult visual conditions
- **P0.4 finding:** Provides direct evidence that several proposed visual-shift factors occur in real laparoscopic data.
- **Boundary:** Not itself a controlled robustness experiment.
