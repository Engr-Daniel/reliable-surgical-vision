# P0.4 Open Questions Carried Forward

## P0.5 — Reliable inference

1. How does calibration change under the natural and controlled shifts retained by P0.4?
2. Are uncertainty scores predictive of errors under smoke/blood/low-light versus centre shift?
3. For phase recognition, what is the correct abstention unit: frame, temporal segment, transition or procedure?
4. For segmentation, what is the correct abstention/coverage unit: frame, image, object, region or pixel?
5. Which conformal formulations remain valid when the calibration and test distributions differ?
6. Should natural-shift calibration be performed with target-centre examples, or should the method be evaluated without target recalibration?
7. What reliability metrics expose failures that Dice/F1/accuracy miss?

## P0.6 — Telesurgery / networking

8. What decoded-video artifacts actually result from latency, jitter and packet loss under realistic surgical video codecs?
9. When does packet loss cause no visible effect because retransmission/FEC/concealment recovers the stream?
10. How do GOP structure, keyframe spacing and packetization affect corruption persistence?
11. What mapping should be used from packet-loss percentage to missing/corrupted decoded frames?
12. What network conditions cause bitrate/resolution/frame-rate adaptation in real telesurgery?
13. Is last-frame freeze a realistic response for relevant streaming stacks?
14. Which network variables can be aligned to each decoded frame?
15. What latency/jitter/loss ranges are clinically/deployment plausible?
16. How should Endo-C6 packet loss be compared with a network-emulated decoded-video protocol?

## P0.7 — Intersection / novelty

17. Has any study combined standard phase/segmentation models with both controlled visual and network-derived temporal shift and evaluated calibration/selective prediction?
18. Does network telemetry add predictive value beyond image/video uncertainty after controlling for visible degradation?
19. Does a compound visual + network shift create interaction effects beyond single shifts?
20. Is a dual-task benchmark (phase + segmentation) scientifically necessary, or does it dilute the contribution?
21. Which working dataset combination permits independent natural shift without P0.3 provenance leakage?
22. Does the emerging Endo-C6 literature already occupy enough of Track C/A that the research question must narrow further?
23. Which contribution remains useful even if “first”/novelty claims are removed?

## Experimental design

24. How should surgical-domain experts calibrate plausible visual-severity levels?
25. Should corruption parameters be calibrated by perceptual quality, task degradation, or physical/acquisition variables?
26. What sample size is needed for procedure-level confidence intervals under external shift?
27. Should compound interaction be analysed through mixed-effects models, response surfaces or a simpler factorial design?
28. Which clean-vs-shift model checkpoint-selection rule avoids OOD-test leakage?
