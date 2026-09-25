# P0.3 Open Questions Carried Forward

## P0.4 — Distribution Shift
1. Which visual corruptions already have surgical-CV benchmarks?
2. Which natural shift definitions are valid for Cholec80→PhaKIR/HeiChole and for robot-assisted datasets?
3. Can procedure shift and centre shift be disentangled?
4. Which severity ranges produce meaningful but not absurd surgical video degradation?
5. What compound spatial+temporal shifts have already been studied?

## P0.5 — Reliable Inference
6. For phase recognition, should reliability be measured per frame, temporal segment, transition or procedure?
7. For segmentation, should abstention occur per frame, region, object or whole prediction?
8. Which datasets have enough independent calibration procedures for conformal methods without contaminating test data?
9. How should rare phases/tools/classes be treated in calibration and coverage analysis?

## P0.6 — Networking
10. What codec/container should be used when re-encoding full surgical videos?
11. Which source frame rates should remain native versus standardized?
12. How should packet loss/jitter be translated into reproducible frame/video perturbations without falsely claiming network equivalence?
13. Which full-video candidates expose timestamps/frame numbers well enough for telemetry alignment?
14. Can we preserve label synchronization after frame dropping, duplication and variable delay?

## P0.7 — Intersection / final design
15. Is one temporal task plus one spatial task scientifically stronger than a single multitask dataset?
16. Does SAR-RARP50's direct robotic relevance outweigh its narrow procedural-phase scope?
17. Can PhaKIR's eight public videos support a statistically defensible external reliability analysis?
18. Should HeiChole or MultiBypass140 be added despite their storage burden?
19. What exact CAMMA overlap IDs must be removed from any Cholec80/Endoscapes/CholecT50 comparison?
20. Which dataset combination survives the literature novelty stress-test?

## Operational
21. Has `multibypass03.zip` been repaired?
22. Is the CaDIS official download live again?
23. Have any Endoscapes PhysioNet licence/DUA terms changed?
24. Has ESAD released its test set?
25. Has CAMMA updated its overlap map or dataset versions?
