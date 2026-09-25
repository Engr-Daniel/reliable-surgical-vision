# P0.1 Research Question Answer Matrix

## RQ1 — System Architecture
**Answer:** Public evidence supports MSS810 surgeon console, SSS800 patient platform and VSS820 vision platform, with 3D endoscopy, image processing and instruments. Regulatory material describes master sensing/kinematics to patient-side closed-loop joint control.  
**Evidence:** S01–S03.  
**Detailed:** `docs/architecture/toumai-system-architecture.md`, Sections 1–3.

## RQ2 — Visual Pipeline
**Answer:** Reported architecture includes 3D endoscopy, FPGA processing, dual-fiber internal transport, vascular enhancement, smoke removal and <50 ms reported image-path latency. Remote codec/adaptation internals remain unknown.  
**Evidence:** S03, S13–S14.  
**Detailed:** architecture report Section 4.

## RQ3 — Teleoperation Pipeline
**Answer:** High-level master–slave sensing, kinematic mapping, reference joint-state generation and patient-side closed-loop control are documented. Reported 4000 Hz/250 μs characteristics are not treated as total remote latency.  
**Evidence:** S01, S03.  
**Detailed:** architecture report Section 2.

## RQ4 — Communications Architecture
**Answer:** Published deployments use heterogeneous 5G, fiber, hybrid and redundant networks; manufacturer sources additionally report broadband/satellite. No one topology or latency is universal.  
**Evidence:** S04–S14.  
**Detailed:** architecture report Sections 6–7 and `toumai-network-metrics.csv`.

## RQ5 — Reliability and Safety
**Answer:** Public evidence supports device safeguards, redundancy in some deployments, monitoring/testing and bedside human takeover. Exact failover thresholds/state machine remain unknown.  
**Evidence:** S03, S06, S11–S12.  
**Detailed:** architecture report Section 5.

## RQ6 — Reliable Visual Inference Relevance
**Answer:** Clinical/optical conditions, platform processing and communication can plausibly alter the visual distribution seen by CV systems. Network→video→CV reliability remains a hypothesis, not an established Toumai failure mode.  
**Evidence:** P0.1 synthesis.  
**Detailed:** architecture report Sections 8–11.
