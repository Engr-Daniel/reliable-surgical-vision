# Research Log

Use dated entries. Record questions, evidence, decisions, failed attempts, unexpected observations, and next actions.

## 2026-09-25 — Repository foundation

### Decision
Created a single research repository with three provisional research tracks rather than three long-lived paper branches.

### Rationale
The tracks share literature, datasets, reliability methods, evaluation infrastructure, and likely code. Their eventual publication boundaries should be determined by evidence rather than repository structure.

## 2026-09-25 — P0.1 Toumai Technical Literature & Architecture Reconnaissance completed

### Scope
Completed a focused public-evidence technical reconnaissance of Toumai MT-1000 and its tele-robotic deployments.

### Method
Used reproducible query families across peer-reviewed databases/journals, regulatory technical-review material, official manufacturer sources, and current Nigerian deployment reporting. A final audit screening set of 25 unique records/categories was documented: 16 retained and 9 excluded/deprioritized. Claims were classified by evidence type and extracted into a claim-level evidence table.

### Key findings
- Regulatory evidence identifies MSS810 surgeon console, SSS800 patient platform and VSS820 vision platform and describes the master–slave kinematic/closed-loop control principle.
- Peer-reviewed literature reports 4000 Hz master–slave response, 250 μs response time, force feedback to 0.1 N, FPGA image processing, dual-fiber image transport, <50 ms imaging latency, 3D endoscopy and image-enhancement algorithms.
- The same paper states that force-feedback precision and image-algorithm reliability were not objectively quantified.
- Toumai human telesurgery has been reported over multiple network architectures; no single universal network topology should be assumed.
- Detailed clinical network evidence now includes delay/RTT, jitter, packet loss, throughput, multi-carrier redundancy, QoS thresholds, stress testing and emergency-disconnection drills.
- The Nigerian RHV–Nisa case is confirmed as a >500-km Toumai deployment with Starlink primary and MTN backup, but no public raw telemetry was identified by the evidence cutoff.
- Codec, adaptive-streaming logic, failover thresholds/state machine and frame-aligned network telemetry remain unresolved/proprietary.
- `network state → received-video characteristics → CV reliability` remains a hypothesis for later phases, not a P0.1 conclusion.

### Decision
P0.1 passes its exit criteria at the focused public-evidence reconnaissance level.

### Milestone
Tag after repository integration/review: `v0.0.1`.

### Next
P0.2 — Surgical Computer-Vision Landscape Reconnaissance.