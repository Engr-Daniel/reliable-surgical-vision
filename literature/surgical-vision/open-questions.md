# P0.2 Open Questions Carried Forward

## P0.3 — Dataset reconnaissance
1. Which candidate datasets are actually downloadable and under what terms?
2. Which permit derived corruptions/features and publication of derivatives?
3. Which official splits are procedure/patient level?
4. Which provide raw video rather than frames only?
5. Which expose centre/device/surgeon metadata for natural shifts?
6. Which are human vs porcine/ex-vivo/training?
7. Which have enough independent procedures for training, calibration and shifted test sets?
8. How much source-video overlap exists among Cholec80, CholecT50, CholecSeg8k and CholecInstanceSeg?
9. Which provide frame-rate/timestamp metadata needed for temporal/network degradation?
10. Which annotations have documented quality control/inter-rater evidence?

## P0.4 — Distribution shift
11. Which studies explicitly benchmark surgical corruption robustness?
12. Which natural shifts are studied: hospital, surgeon, device, procedure, anatomy, geography?
13. Which synthetic corruptions plausibly represent visual degradation without pretending to be network physics?
14. How should temporal/frame-loss/jitter corruptions be parameterised?
15. Which papers already study compound spatial+temporal shift?

## P0.5 — Reliable inference
16. What calibration/uncertainty baselines exist for the shortlisted surgical tasks?
17. What is the right unit for abstention in segmentation: frame, object, region or pixel?
18. What is the right conformal coverage unit for structured outputs?
19. Which abstention semantics are clinically meaningful when surgery continues under human control?
20. Which metrics remain valid under severe class imbalance?

## P0.6 — Networking
21. Which network/video impairments yield reproducible pixel/temporal changes under realistic codecs?
22. How should frame loss, jitter, compression and adaptive bitrate be emulated?
23. Can telemetry be aligned to individual predictions?
24. Do temporal workflow models fail differently from framewise segmentation models?

## P0.7 — Intersection / novelty
25. Has compound visual+temporal/network shift already been benchmarked for the selected task?
26. Has network telemetry already been used to predict surgical-CV unreliability?
27. Does network telemetry add value beyond image-only uncertainty?
28. Should temporal and spatial task families form one benchmark suite or separate workstreams?
29. What useful contribution remains if a proposed novelty claim weakens?
