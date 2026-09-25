# Open Technical Questions — Toumai after P0.1

These are **confirmed public-evidence gaps or unresolved questions**, not assumptions that the capabilities are absent.

## A. Control and actuation
1. What subsystem does the reported 4000 Hz master–slave frequency refer to exactly?
2. How is the 250 μs response time measured?
3. What are the low-level servo frequencies, gains and stability margins?
4. How are motion scaling and tremor filtering parameterised?
5. What states are available under degraded/failed remote connectivity?
6. What exact conditions trigger hold, standby, command rejection or emergency stop?
7. What is the behavior of in-flight commands during a link transition?

## B. Vision
8. Exact sensor models, stereo baseline, resolution and frame rate by configuration?
9. Full sensor-to-display latency decomposition?
10. Architecture/training data/validation of Vascular Enhancement and Intelligent Smoke Removal?
11. Can enhancement be disabled?
12. Are raw pre-enhancement frames available?
13. Does enhancement alter features relevant to learned segmentation/detection/phase models?

## C. Remote video transport
14. What video codec(s), profiles and encoder settings are used?
15. What bitrate, frame-rate or resolution adaptation exists?
16. What packet-loss concealment / frame-recovery method is used?
17. What buffering strategy is used under jitter?
18. How are stereo streams synchronized?
19. How are video and control streams synchronized?
20. What is the complete motion-to-photon latency budget?
21. Is network/QoS telemetry exposed programmatically and frame-aligned?

## D. Redundancy and failover
22. Which failover mechanisms are intrinsic to Toumai vs supplied by hospital/network infrastructure?
23. Is link switching automatic, operator-mediated, SD-WAN-based or deployment-specific?
24. Is make-before-break supported?
25. What thresholds/timers/hysteresis govern switching?
26. What is measured failover duration?
27. What robot safe-state is entered during switching?
28. Are backup links continuously probed?
29. Can control and video fail over independently?

## E. Cybersecurity
30. Which encryption/authentication mechanisms are intrinsic to the commercial system?
31. How are remote operator identity and session authorization handled?
32. What replay/integrity protection is used for control commands?
33. How are keys provisioned/rotated?
34. What audit/event logs are retained?
35. How much of the VPN/firewall design reported in individual papers is site-specific?

## F. Nigeria RHV–Nisa
36. Actual Starlink RTT/one-way latency distribution?
37. Jitter, packet loss and throughput distribution?
38. MTN role: bonded, hot standby, warm standby or cold standby?
39. Was an actual failover performed intraoperatively or only pre-tested?
40. Measured failover time?
41. Weather/network-quality telemetry during surgery?
42. Video quality/resolution/framerate throughout?
43. Archived frame-level and network telemetry?
44. Power architecture/UPS/generator supporting robot, console, vision and network devices?
45. Cybersecurity/VPN topology used between RHV and Nisa?

## G. Reliable visual inference
46. At what point in the visual pipeline would a learned CV model receive frames?
47. Would it receive raw, enhanced, compressed or decoded video?
48. Can telemetry be aligned to each video frame?
49. Can clinical/optical shifts be separated experimentally from communication-induced shifts?
50. Which reliability metric is most appropriate for each surgical-CV task?
51. Do calibration, selective risk or conformal coverage degrade before task metrics do?
52. Can network telemetry add predictive value over image-only uncertainty for identifying unsafe AI assistance?
