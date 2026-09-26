# P0.6 Research Question Answer Matrix

## RQ1 — What communication architecture and traffic classes characterize telesurgery?
**Answer:** Published systems carry at least robot command/control, visual feedback, audio/telepresence, system/network telemetry, and security/management traffic. Video is generally the dominant sustained flow, while control has stricter timing/safety implications. Clinical systems use dedicated fiber/OTN, 5G, hybrid links, best-effort/SD-WAN and satellite, often with redundancy and QoS.  
**Evidence:** NW01–NW03, NW11–NW16, NW18–NW25.  
**Detailed:** `network-architecture.md`, `access-technology-map.csv`.

## RQ2 — Which QoS variables matter, and how should they be defined?
**Answer:** RTT/one-way latency, encode/decode latency, display latency, jitter, packet loss, frame loss, bandwidth/capacity, throughput, video bitrate, buffer delay, availability and failover time are distinct quantities. Reported “latency” values cannot be pooled without endpoint definitions.  
**Evidence:** NW01, NW05–NW10, NW14–NW17, NW23, NW26.  
**Detailed:** `qos-metric-taxonomy.csv`, `latency-decomposition.md`, `clinical-network-metrics.csv`.

## RQ3 — Are there universal safe network thresholds?
**Answer:** **No universal threshold was established.** The Japanese 2026 guideline uses ≤100 ms for network RTT + new encode/decode processing, while CRSA consensus recommends total teleoperation latency <300 ms and ideally <200 ms. Experiments and specialized satellite/control systems report different tolerated ranges. Required bandwidth is explicitly robot/codec specific.  
**Evidence:** NW01, NW03, NW05–NW10, NW16, NW20.  
**Detailed:** `network-threshold-evidence.csv`, `latency-decomposition.md`.

## RQ4 — How can network impairment alter the received video?
**Answer:** Network impairment is mediated by transport and media layers. Loss may trigger FEC/retransmission or damage codec NAL units; jitter may be buffered; congestion may drive bitrate/quantization/layer adaptation; recovery failure may yield concealment, frame skip/freeze or delayed playout. Therefore raw packet loss is not equivalent to frame loss and raw jitter is not equivalent to AI-input timing jitter.  
**Evidence:** NW26–NW34 plus telesurgery compression/congestion studies NW05, NW09–NW12.  
**Detailed:** `network-to-video-mechanism.md`, `codec-transport-recovery-map.csv`.

## RQ5 — What redundancy/failover mechanisms are established?
**Answer:** Evidence supports dual links, packet duplication, multi-carrier hot standby, QoS prioritization, automatic VPN/path recovery, safe robot states, bedside takeover and emergency drills. Redundancy can prevent a degraded path from becoming a visible video failure; monitoring must therefore retain both path-level and decoded-video state.  
**Evidence:** NW01–NW03, NW11, NW13, NW16, NW21–NW22.  
**Detailed:** `redundancy-failover-map.csv`.

## RQ6 — What does the evidence say about access technologies?
**Answer:** Dedicated/guaranteed fiber and OTN provide the strongest stable evidence; 5G can be clinically feasible but SA/NSA, QoS, radio conditions and congestion matter; LEO satellite offers reach with potentially large temporal variability; GEO can operate only with high-latency-aware system design in current evidence. Hybrid architectures improve resilience but add failover complexity.  
**Evidence:** NW11–NW21, NW24.  
**Detailed:** `access-technology-map.csv`, `clinical-network-metrics.csv`.

## RQ7 — What directly links network/video degradation to downstream surgical AI?
**Answer:** Direct evidence remains limited. Endo-C6 (MICCAI 2026) directly tests packet-loss-burst corruption in temporal surgical/endoscopy VLMs and shows substantial robustness failure. Telesurgery studies provide strong indirect evidence that bandwidth/loss/congestion can alter decoded video, but a mature conventional phase/segmentation benchmark coupling measured network state through a real codec/decoder to calibration/selective reliability was not established by P0.6.  
**Evidence:** NW05, NW09–NW12, NW18–NW19, NW35.  
**Detailed:** `downstream-vision-evidence.md`.

## RQ8 — What network/system variables and impairment abstractions should be carried to P0.7?
**Answer:** Carry a two-level design: (A) decoded-video abstractions for reproducible AI sensitivity and (B) a network+codec pipeline for mechanistic Track C testing. Candidate network variables are latency, jitter, loss/burst loss, capacity and failover state; candidate decoded variables are bitrate, resolution, frame rate, missing/duplicate/frozen frames and codec/buffer state. The key Track C comparison is video-only vs telemetry-only vs video+telemetry failure prediction.  
**Evidence:** synthesis of NW01–NW35.  
**Detailed:** `candidate-network-impairment-protocol.md`.

# Overall conclusion
P0.6 closes the conceptual bridge from generic “network degradation” to an explicit transport/codec/decoder mechanism. It also narrows novelty: combined network impairments are already studied in telesurgery, and packet-loss-like corruption is already studied in surgical AI. The unresolved intersection is whether mechanistically grounded network/system telemetry improves prediction or selective handling of downstream **standard surgical-CV reliability failures** beyond what is visible in the received video. This remains a P0.7 question, not a novelty claim.
