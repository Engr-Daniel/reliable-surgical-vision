# P0.7 Refresh Source Index

Sources retained by the 2026-11-12 overlap refresh. P0.1–P0.6 sources keep their original IDs and indices in their own folders; every retained source in the programme is coded in `global-evidence-matrix.csv`.

Bibliographic fields marked **verify** were not fully confirmed from a primary page during the refresh and must be checked before citation in a manuscript.

---

## IX01 — VISTA: A Benchmark for Real-Time Video Streaming under Network Impairments in Surgical Teleoperation
- **Authors:** Deng Z, Yuan Z, Lu T, Li G, Huang M, Zou L
- **Year / venue:** 2026 — arXiv:2605.08886 (eess.IV), preprint; no peer-reviewed venue stated
- **URL:** https://arxiv.org/abs/2605.08886 · code: https://github.com/Dzxx623/VISTA
- **Evidence type:** Preprint, hardware-in-the-loop benchmark
- **Setup:** laparoscopic box-trainer camera, 640×480 at 30 fps; H.264 (libx264, GOP 15, zerolatency); UDP with a custom per-chunk header carrying frame ID and capture timestamp; Linux NetEm with Gilbert–Elliott loss on the forward video path only.
- **Network tiers:** Hospital LAN, 5G Urban, 4G Rural, LEO and GEO satellite, spanning 5–100 Mbps, 3–600 ms one-way delay, 1–50 ms jitter, 0.01–2% loss with 2–6-packet mean bursts.
- **Outcomes:** PSNR/SSIM/VMAF on decoded frames, freeze rate, one-way delay, human peg-transfer success and time (375 trials, 15 operators).
- **P0.7 finding:** Occupies the *surgical network → decoded-video benchmark* layer that P0.6 proposed as "Level B". Tiers with similar mean PSNR (4G Rural vs LEO) gave very different human success rates, which the authors attribute to different degradation mechanisms.
- **Boundary:** No downstream AI/CV model is evaluated, and no telemetry is used to predict AI behaviour. Fixed codec configuration; box-trainer scene rather than clinical video.
- **Programme use:** Reusable, citable starting envelope for impairment tiers and pipeline design (licence to verify before reuse). It also motivates the "matched quality, different mechanism" hypothesis (H3).

## IX02 — A Comprehensive Analysis of the Effects of Network Quality of Service on Robotic Telesurgery
- **Authors:** Zhang Z, Roodabeh SHR, Alemzadeh H (University of Virginia)
- **Year / venue:** 2026 — arXiv:2603.06824; venue **verify**
- **URL:** https://arxiv.org/abs/2603.06824
- **Evidence type:** Preprint, user study with model-based fault injection
- **Setup:** NetFI emulator with a four-state Gilbert–Elliott packet-loss model (Lomax bursts), a hyperexponential delay model and a communication-loss model, applied to the command path in SurRoL with a dVTrainer console.
- **P0.7 finding:** Communication loss and severe delay degraded human task performance more than even substantial packet loss. NetFI is a parameterised, trace-informed impairment design.
- **Boundary:** Video was not impaired; no AI model was evaluated.

## IX03 — Stabilizing Temporal Inference Dynamics for Online Surgical Phase Recognition
- **Authors:** Liu Y, Zhu N, Peng J, Chen X, Granados A, Wang G, Ourselin S
- **Year / venue:** 2026 — arXiv:2605.16387; early accepted, MICCAI 2026
- **URL:** https://arxiv.org/abs/2605.16387
- **Evidence type:** Accepted conference paper (preprint version read)
- **P0.7 finding:** Attributes online phase-prediction instability to error cascades and memoryless transitions. Proposes a training loss, an evidence-gated transition predictor and a Temporal Fragmentation Index (TFI), evaluated on Cholec80 and AutoLaparo.
- **Boundary:** At abstract level, there is no evaluation under input corruption, frame loss or network degradation, and no calibration, selective or conformal analysis.
- **Programme use:** TFI is a candidate secondary temporal-reliability metric. Evidence gating is a candidate confounder: a gated model may hide failures that a monitor would otherwise flag.

## IX04 — Towards Robust Algorithms for Surgical Phase Recognition via Digital Twin Representation
- **Authors:** Ding H, Zhang Y, Cheng W, Wang X, Lian X, Yu C, Shu H, Kim JW, Krieger A, Unberath M
- **Year / venue:** 2024 — arXiv:2410.20026
- **URL:** https://arxiv.org/abs/2410.20026
- **Evidence type:** Preprint
- **P0.7 finding:** Evaluates phase recognition (Surgformer baseline vs a digital-twin intermediate representation) on a combined-corruption Cholec80 test set (hue, brightness, contrast) and on OOD robotic datasets. This directly establishes *phase recognition under controlled visual corruption*.
- **Boundary:** Photometric corruptions only; no temporal, codec or network degradation; no reliability analysis.

## IX05 — Comparative benchmarking of failure detection methods in medical image segmentation: Unveiling the role of confidence aggregation
- **Authors:** Zenk M et al.
- **Year / venue:** 2025 — Medical Image Analysis 101:103392
- **DOI:** https://doi.org/10.1016/j.media.2024.103392 (preprint arXiv:2406.03323)
- **Evidence type:** Peer-reviewed benchmark
- **P0.7 finding:** Recommends risk–coverage analysis for failure detection under realistic test-time shift. Pairwise Dice between ensemble members is a simple, strong baseline, and many prior works evaluate proxy tasks instead of failure detection.
- **Boundary:** 3D non-surgical segmentation.
- **Programme use:** Sets the expected baseline strength and evaluation protocol for any failure monitor.

## IX06 — Development, deployment and scaling of operating room-ready artificial intelligence for real-time surgical decision support
- **Authors:** Protserov S, Hunter J, Zhang H, Mashouri P, Masino C, Brudno M, Madani A
- **Year / venue:** 2024 — npj Digital Medicine 7:231
- **DOI:** https://doi.org/10.1038/s41746-024-01225-2
- **Evidence type:** Peer-reviewed system/deployment study
- **P0.7 finding:** Surgical guidance segmentation was served through an equipment-agnostic web platform and optimised for a range of network speeds. It reports a prediction stream of at least 60 fps and at most 70 ms round-trip above 8 Mbps.
- **Boundary:** Addresses delivery throughput and latency, not model accuracy or reliability under network impairment.

## IX07 — Server-Driven Video Streaming for Deep Learning Inference (DDS)
- **Authors:** Du K et al. (full author list **verify**)
- **Year / venue:** 2020 — ACM SIGCOMM 2020 (**verify**)
- **URL:** https://par.nsf.gov/servlets/purl/10174381
- **Evidence type:** Peer-reviewed networking systems paper
- **P0.7 finding:** In machine-centric video streaming, the server-side DNN's output decides which regions are re-sent at higher quality. Network/codec adaptation tuned to DNN accuracy is an established generic idea.
- **Boundary:** Optimises bandwidth against accuracy; does not predict or flag AI failure; non-medical.

## IX08 — AccMPEG: Optimizing Video Encoding for Video Analytics
- **Authors:** Du K, Zhang Q, Arapin A, Wang H, Xia Z, Jiang J
- **Year / venue:** 2022 — arXiv:2204.12534 (published venue **verify**)
- **URL:** https://arxiv.org/abs/2204.12534
- **Evidence type:** Preprint (networking systems)
- **P0.7 finding:** A cheap model estimates the DNN accuracy gradient per frame to guide encoding quality.
- **Boundary:** Encoding optimisation, not reliability monitoring; non-medical.

## IX09 — Minimizing packet retransmission for real-time video analytics
- **Authors:** **verify**
- **Year / venue:** 2022 — listed as Int. Conf. on Management of Data 2022 (workshop/short paper; **verify**)
- **URL:** https://aminer.org/pub/63aa965890e50fcafd008599/minimizing-packet-retransmission-for-real-time-video-analytics
- **Evidence type:** Short paper
- **P0.7 finding:** In high-bandwidth networks, delay is bounded mainly by loss and jitter. The paper argues retransmission decisions should depend on a packet's impact on DNN inference. This is the closest retained idea linking transport state to downstream AI outcome.
- **Boundary:** Uses AI impact to steer transport; does not use transport state to predict AI failure; non-medical.

## IX10 — VANET Meets Deep Learning: The Effect of Packet Loss on the Object Detection Performance
- **Authors:** Wang Y, Menkovski V, Ho IW-H, Pechenizkiy M
- **Year / venue:** 2019 — IEEE VTC2019-Spring
- **DOI:** https://doi.org/10.1109/VTCSpring.2019.8746657
- **Evidence type:** Peer-reviewed conference paper
- **P0.7 finding:** Simulated vehicular packet loss degrades deep-learning (point-cloud) object detection, with rapid decline beyond high loss levels.
- **Boundary:** Point clouds over VANET; generic; does not predict failure from telemetry.

## IX11 — System Modeling and Performance Evaluation of Predictive QoS for Future Tele-Operated Driving
- **Authors:** Schippers H, Schüler C, Sliwa B, Wietfeld C
- **Year / venue:** 2022 — arXiv:2201.11432 (conference venue **verify**)
- **URL:** https://arxiv.org/abs/2201.11432
- **Evidence type:** Preprint/conference paper
- **P0.7 finding:** Predictive QoS from radio/network measurements is an established approach for teleoperation, motivated by preventing service interruption.
- **Boundary:** Predicts network QoS, not perception-model reliability.

## IX12 — Recognizing Surgical Phases Anywhere: Few-Shot Test-time Adaptation and Task-graph Guided Refinement (SPA)
- **Authors:** Yuan K, Chen T, Li S, Lavanchy JL, Heiliger C, Özsoy E, Huang Y, Bai L, Navab N, Srivastav V, Ren H, Padoy N
- **Year / venue:** 2025 — MICCAI 2025; arXiv:2506.20254
- **URL:** https://arxiv.org/abs/2506.20254
- **Evidence type:** Peer-reviewed conference paper
- **P0.7 finding:** Few-shot spatial adaptation, task-graph temporal priors and test-time adaptation transfer phase recognition across institutions and procedures.
- **Boundary:** A mitigation method for natural shift; no corruption, network or reliability analysis.
