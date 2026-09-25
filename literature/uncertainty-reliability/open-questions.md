# P0.5 Open Questions Carried Forward

## P0.6 — Telesurgery / network mechanisms

1. Which network variables are observable at the same time scale as a model prediction?
2. How do packet loss, jitter, bandwidth and latency map to the **decoded video** seen by the AI?
3. Which impairments are hidden by retransmission, buffering, FEC or decoder concealment?
4. What failure-monitor features remain useful if visible degradation is subtle but network telemetry is abnormal?
5. Can network state predict model failure before the visual stream becomes obviously degraded?
6. What is the appropriate temporal alignment between network telemetry and frame-level predictions?
7. How should burst duration / GOP structure enter a failure-risk model?
8. Which P0.5 reliability signals can operate at real-time telesurgical latency budgets?

## P0.7 — Intersection / novelty stress-test

9. Has any peer-reviewed study evaluated phase-recognition calibration/selective/conformal behavior under both surgical visual corruption and network-derived temporal shift?
10. Has surgical segmentation failure monitoring already combined **measured network telemetry** with visual/temporal features?
11. Does TCSR-Monitor already occupy enough of the visual+temporal failure-monitoring space that Track B/C should merge around network telemetry?
12. Does OpenMIBOOD/PhaKIR make a separate OOD component redundant for the final experiment?
13. Should the research prioritize **failure prediction** rather than generic OOD detection?
14. Is a conformal prediction layer scientifically necessary, or would risk–coverage + calibrated failure monitoring be clearer?
15. If conformal prediction is used, what exact guarantee is meaningful for the selected surgical task?
16. Does class-conditional/Mondrian calibration have enough samples for rare phases?
17. Can the final contribution remain valuable without claiming a “first” use of conformal prediction, abstention, or surgical UQ?
18. Should Track B and Track C become one workstream: network-aware failure monitoring with selective deferral?
19. Is phase recognition or segmentation the better task for observing a network-telemetry benefit beyond the received video?
20. What is the minimum independent-procedure count needed for stable calibration/coverage estimates?

## Experiment design

21. For phase recognition, should abstention persist for one frame or until a recovery condition is satisfied?
22. For segmentation, should abstention suppress the whole overlay, flag the overlay, or reject only low-confidence regions?
23. What Dice/IoU threshold defines an operational segmentation failure, and how sensitive are results to that threshold?
24. Should selection thresholds be global or phase/instrument/shift-specific?
25. How many repeated procedure-level calibration splits are needed to quantify conformal/calibration variability?
26. Which calibration metric should be primary: NLL/Brier with ECE diagnostic, or another task-specific score?
27. How should risk–coverage curves be aggregated across videos without letting long videos dominate?
28. Should calibration be frozen from ID or allow limited target recalibration? Both settings answer different deployment questions.
29. How should alert false alarms be costed in a surgical workflow?
30. What is the correct human-fallback interpretation for each AI output type?

## Method-selection caution

31. If a stronger UQ method improves AURC but not probability calibration, which property matters for the intended intervention?
32. If OOD detection is strong but error detection is weak, should OOD be excluded from the final safety mechanism?
33. If conformal sets become large under shift, is abstention preferable to returning ambiguous sets?
34. If network telemetry improves failure prediction only after visible degradation has occurred, does it add practical value?
