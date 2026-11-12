# P0.7 Search and Review Protocol

## Identity
- **Programme:** Reliable Surgical Vision
- **Task:** P0.7 — Intersection Analysis & Novelty Stress-Test
- **Refresh search date:** 2026-11-12
- **Evidence cutoff:** 2026-11-12 (P0.1–P0.6 evidence cutoffs remain 2026-09-25/26)
- **Type:** integration of P0.1–P0.6 plus a targeted overlap-refresh search
- **Not claimed as:** an exhaustive systematic review or a definitive statement that any intersection is empty

## Objective
P0.7 has two evidence activities:

1. **Integration.** Code every retained P0.1–P0.6 source on common programme dimensions (task, shift, reliability concept, network layer, downstream-AI evaluation, telemetry use) in `global-evidence-matrix.csv`, using the reproducible builder `build_global_evidence_matrix.py`.
2. **Overlap refresh.** About seven weeks passed between the P0.6 cutoff and P0.7. P0.7 therefore searched specifically for work that could occupy the candidate intersections identified by P0.4–P0.6. It also searched outside the surgical domain (video analytics, teleoperated driving), where the Track C idea may already exist in another form.

## Refresh questions
1. Has any surgical or telesurgical study evaluated a downstream CV model on video delivered through a network/codec pipeline?
2. Has network/system telemetry been used to predict AI failure or gate AI output, in any domain?
3. Has surgical phase recognition been evaluated with conformal, selective or calibrated reliability under visual, temporal or network shift?
4. Has new surgical corruption/failure-monitoring work appeared since P0.5 (TCSR-Monitor) and P0.4 (Endo-C6)?
5. Do generic (non-medical) video-analytics or teleoperation fields already establish the network→DNN-accuracy relationship?

## Search surfaces
Web search across arXiv, MICCAI 2025/2026 pages, IEEE Xplore, Springer, Wiley, ACM-indexed pages, PubMed/PMC, NSF PAR and institutional repositories.

## Query families used (2026-11-12)
- network telemetry predict DNN video analytics accuracy packet loss streaming
- video compression effect surgical phase recognition deep learning performance
- telesurgery artificial intelligence network latency packet loss video degradation model robustness 2026
- conformal prediction surgical phase recognition distribution shift 2026
- surgical phase recognition robustness frame dropping temporal perturbation benchmark
- surgical video corruption robustness benchmark segmentation phase 2026 arXiv
- packet loss H.264 impact object detection accuracy DNN remote inference prediction
- surgical segmentation failure detection quality control uncertainty under shift MICCAI 2026
- cloud edge surgical AI inference 5G network phase recognition real-time remote video stream
- DNN-aware video streaming analytics accuracy bandwidth adaptation AccMPEG DDS loss-resilient Grace
- conformal prediction surgical video phase recognition prediction sets coverage
- predictive QoS teleoperated driving video stream object detection performance network conditions

Full text was read for the two sources with the largest bearing on Track C novelty (VISTA, NetFI) and for the abstract-level scope of the MICCAI 2026 phase-stability paper.

## Inclusion
Retain a refresh source if it changes or sharpens an occupancy judgement in `intersection-map.csv`:
- surgical/telesurgical work on video under network impairment;
- any-domain work evaluating DNN accuracy under network/codec conditions;
- any-domain work using network telemetry to predict QoS or AI behaviour;
- surgical phase-recognition reliability or robustness work not already in P0.2/P0.4/P0.5;
- medical segmentation failure-detection benchmarks that set baseline expectations.

## Exclusion
- patents (commercial existence is noted, not used as scientific evidence);
- industry blogs/marketing material;
- control-path-only teleoperation work (no video/AI);
- generic segmentation-robustness papers that do not change an occupancy judgement;
- single-author unreviewed preprints with no direct bearing on a programme intersection.

## Interpretation rules
- An intersection is rated **NOT FOUND IN RETAINED EVIDENCE**, never "novel" or "first".
- Each occupancy rating carries a **residual risk** that unretrieved work exists: low / medium / high. Generic networking and video-analytics venues are large and only shallowly searched here, so Track C carries **high** residual risk until Phase 1 completes the targeted search set out in `phase1-direction.md`.
- Adjacent-domain evidence (video analytics, teleoperated driving) counts toward occupancy of the **idea**, even when it does not occupy the **surgical instantiation**.
- Accepted-but-unpublished and preprint evidence is labelled `PP` and treated as occupying an intersection for planning purposes. It is still labelled as not peer-reviewed.

## Screening accounting
- **12 retained refresh sources** (IX01–IX12)
- **12 excluded/deferred refresh records/categories**
- **24 refresh audit records/categories**
- Integrated matrix: **175 rows / 165 unique sources** after collapsing 10 cross-task duplicates
