# P0.2 Research Question Answer Matrix

## RQ1 — Task taxonomy
**Answer:** Surgical CV is a hierarchy: workflow phase/step; action/gesture/triplets; instrument presence/detection/keypoints; semantic/instance segmentation; anatomy/scene understanding; safety-state assessment; skill; and emerging video-language tasks. These cannot be collapsed because outputs, labels, temporal structure and error modes differ.  
**Evidence:** SV02–SV06, SV08, SV12–SV31.  
**Detailed:** `task-taxonomy.md`.

## RQ2 — Input and temporal structure
**Answer:** Presence/detection/segmentation can be framewise, although temporal continuity matters. Phase/step/action/skill and long-video reasoning are intrinsically temporal. Live assistance requires causal inference; dropped/irregular frames are therefore especially relevant to workflow models.  
**Evidence:** SV02, SV03, SV09–SV17, SV32.  
**Detailed:** `task-taxonomy.md`, `benchmark-practices.md`.

## RQ3 — Model families and baselines
**Answer:** Representative families progress from CNN/RNN to TCN, encoder–decoder segmentation/detectors, temporal/video Transformers, SAM adaptations and video-language pretraining. Later reliability experiments should use reproducible task-specific baselines rather than select only by leaderboard rank.  
**Evidence:** SV08–SV11, SV17, SV22–SV28.  
**Detailed:** `model-baseline-map.csv`.

## RQ4 — Dataset relationships
**Answer:** Public benchmarks are concentrated in laparoscopic cholecystectomy. Cholec80/M2CAI16 anchor phase recognition; CholecT50 actions; CholecSeg8k/CholecInstanceSeg/Endoscapes dense perception; HeiChole/PhaKIR multicentre evaluation. Robotic resources include JIGSAWS, EndoVis, ESAD, SAR-RARP50 and SurgVU. Dataset overlap must be audited in P0.3.  
**Evidence:** SV08, SV12–SV31.  
**Detailed:** `task-dataset-crosswalk.csv`.

## RQ5 — Metrics
**Answer:** Metrics are task-specific: classification F1/accuracy/AP, detection mAP, segmentation Dice/IoU, triplet AP/mAP, benchmark-defined keypoint metrics and temporal/segmental measures. Metric implementation details can materially alter phase results.  
**Evidence:** SV02, SV05–SV07, SV17, SV22, SV32.  
**Detailed:** `benchmark-practices.md`.

## RQ6 — Benchmark practice and reproducibility
**Answer:** Strong practice uses procedure-level splits, hidden test sets, standardized code, explicit causal constraints and multicentre evaluation. Weaknesses include metric inconsistency, incomplete annotation reporting, single-centre dominance, frame leakage risk and hardware-dependent FPS claims.  
**Evidence:** SV01–SV07, SV13, SV14, SV22, SV32.  
**Detailed:** `benchmark-practices.md`.

## RQ7 — Deployment proximity
**Answer:** Online/causal phase models and high-throughput segmentation show technical potential, but clinical deployment remains limited. Multicentre failures show benchmark speed/accuracy is not clinical reliability.  
**Evidence:** SV01, SV06, SV09–SV14, SV19–SV29.  
**Detailed:** `surgical-cv-landscape.md`.

## RQ8 — Suitability for later reliability research
**Answer:** **Phase/workflow recognition** and **instrument/anatomy segmentation or detection** are especially credible candidate families because they provide complementary temporal and spatial failure modes, mature datasets/metrics and generalisation evidence. This is not a final selection; P0.3–P0.7 remain gating tasks.  
**Evidence:** SV13, SV14, SV22, SV25, SV26, SV32.  
**Detailed:** `reliability-relevance-matrix.csv`.

# Overall conclusion
Use established surgical-CV tasks and benchmark conventions as the predictive backbone, then evaluate reliability explicitly under defined shifts. Do not invent a new perception task or claim novelty at P0.2.
