# P0.6 Open Questions Carried Forward to P0.7

## Network / media implementation
1. Which codec/transport stack can be implemented reproducibly for the chosen dataset and task?
2. H.264 or HEVC? Which encoder/decoder implementation and version?
3. What GOP/keyframe interval is representative enough to study loss propagation?
4. Should NACK/RTX and/or FEC be enabled, and how should recovery telemetry be exposed?
5. What jitter-buffer policy should be used?
6. Can the pipeline expose actual decoded-frame corruption, concealment, freeze and timestamp information?

## Experimental operating region
7. Which latency/loss/jitter/capacity levels correspond to nominal, degraded-plausible and stress-test regimes for the chosen system abstraction?
8. Should distributions/tails be used instead of static symmetric impairments?
9. How should burst loss be modeled from measured traces rather than independent Bernoulli loss?
10. Should asymmetric forward/reverse paths be included?
11. Which failover/outage events are scientifically useful without turning the project into a network-reliability paper?

## AI reliability intersection
12. Which standard surgical-CV task should anchor the network experiment: phase recognition, segmentation, or both?
13. Does network telemetry predict model error before visible degradation appears in the decoded stream?
14. After adding decoded-video quality features, does network telemetry retain independent predictive value?
15. Does telemetry help calibration, selective risk, conformal set size/coverage or only binary failure detection?
16. What temporal window should align network telemetry to each AI prediction?
17. How should delayed labels/predictions be handled when video buffering changes timestamp alignment?
18. Does a network-aware reliability model transfer across codecs, datasets or network types?

## Novelty stress test
19. How close is the proposed network-aware failure monitor to Endo-C6 and TCSR-Monitor when their ideas are combined conceptually?
20. Does Heemeyer 2026 already occupy the compound-network interaction component of Track A?
21. Is the remaining contribution primarily a benchmark, a reliability method, a mechanistic study, or a multimodal prediction study?
22. Is a claim still useful without “first” language?
23. What negative result would cause Track C to be dropped (e.g., telemetry adds no value beyond decoded-video features)?

## Toumai / real deployment
24. Can public or collaborator-accessible telemetry from an actual telesurgery system be obtained?
25. If no proprietary codec/network telemetry is available, how should the study explicitly state the abstraction gap from Toumai?
26. Can Nigeria/Starlink evidence be used only as motivation unless raw telemetry becomes available?
