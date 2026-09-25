# P0.2 Benchmark and Metrics Guide

## Procedure-level independence
Adjacent surgical frames are highly correlated. Prefer official challenge splits or patient/video-level separation; avoid random frame-level train/test splits that can leak procedure, device, anatomy, lighting and workflow context.

## Task-specific metrics
- **Phase/workflow:** accuracy, precision, recall, F1, Jaccard/IoU-style phase overlap; segment/edit metrics where used.
- **Tool presence / multi-label:** AP/mAP, precision, recall, F1.
- **Detection:** AP/mAP at specified IoU thresholds.
- **Semantic segmentation:** Dice, IoU/mIoU, class-wise and boundary metrics where applicable.
- **Instance segmentation:** mask AP and overlap/challenge-specific metrics.
- **Triplets:** AP/mAP for instrument, verb, target and triplet combinations.
- **Keypoints:** use the challenge-defined distance/PCK-like metric without silently changing normalization.

`Metrics Matter in Surgical Phase Recognition` (SV32) shows that identical metric names can hide different averaging and transition-handling conventions. Exact implementations must therefore be pinned.

## Online vs offline
Live surgical assistance requires causal inference. Record for every later baseline:
- online/causal yes/no;
- look-ahead allowed;
- temporal context length;
- smoothing/post-processing;
- buffering.

TeCNO is representative of causal temporal modelling; phase-recognition literature contains both online and offline variants.

## FPS / latency
Reported FPS is not directly comparable across papers because hardware, resolution, preprocessing, batch size, precision and temporal windows differ. The 2025 scoping review (SV06) reports a broad 5–298 FPS range across segmentation studies; this demonstrates feasibility potential, not a universal deployment guarantee.

Later experiments should report hardware, resolution, batch size, preprocessing+inference timing, mean/tail latency and achieved FPS.

## Challenge reproducibility
Use BIAS (SV07) as a benchmark-reporting reference. Record:
- eligibility;
- split design;
- hidden/public labels;
- ranking metric;
- aggregation;
- test composition;
- missing/failed cases;
- external-centre status;
- code/evaluation provenance.

## Generalisation
HeiChole (SV13) and PhaKIR (SV14) are critical:
- HeiChole provides a 33-video, three-centre phase/action/instrument/skill benchmark.
- PhaKIR reports poor cross-centre generalisability for phase recognition, keypoints and instance segmentation.

ROBUST-MIS (SV22) explicitly evaluates increasing domain gap and reports performance degradation.

These are evidence that generalisation is a problem; they do not by themselves establish a novel gap for this programme.

## Reproducibility checklist for later experiments
- [ ] dataset version and source recorded
- [ ] procedure/patient split recorded
- [ ] no frame leakage
- [ ] preprocessing/augmentation documented
- [ ] seed(s) recorded
- [ ] model/checkpoint provenance recorded
- [ ] exact metric code/version pinned
- [ ] causal/offline constraint declared
- [ ] hardware/timing methodology reported
- [ ] per-class/per-centre results retained when possible
- [ ] post-processing/TTA disclosed
- [ ] failures/negative results preserved
