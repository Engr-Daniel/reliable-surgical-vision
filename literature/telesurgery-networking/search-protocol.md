# P0.6 Search and Review Protocol

## Identity
- **Programme:** Reliable Surgical Vision
- **Task:** P0.6 — Telesurgery / Network Literature Reconnaissance
- **Search/final audit date:** 2026-09-26
- **Evidence cutoff:** 2026-09-26
- **Type:** focused network / video-transport / downstream-vision reconnaissance
- **Not claimed as:** exhaustive systematic review or final novelty analysis

## Objective
Establish the technical bridge:

`network state → transport/recovery/adaptation → encoded/decoded video state → received AI input → downstream prediction/reliability`

P0.6 deliberately distinguishes **network telemetry** from **decoded-video effects**. A packet-loss percentage is not treated as a frame-loss percentage, and network jitter is not treated as model-input timing jitter without accounting for buffering/recovery.

## Research questions
1. What communication/data planes and network architectures are used in telesurgery?
2. Which QoS variables are measured and how are latency terms defined?
3. What quantitative thresholds/ranges are supported, and are any universal?
4. Through what transport/codec/decoder mechanisms can network impairment alter received video?
5. What redundancy, recovery, QoS and failover mechanisms are used?
6. How do fiber/OTN, 5G, public/best-effort, LEO and GEO satellite links differ in evidence and failure modes?
7. What direct evidence links network/video impairment to downstream surgical AI?
8. Which network/system variables and impairment abstractions can defensibly be carried to P0.7?

## Search surfaces
PubMed/PMC; BMJ; Springer; Wiley; ScienceDirect; PLOS; IETF/RFC Editor; MICCAI; official project/guideline sources; existing P0.1 Toumai evidence.

## Query families
- telesurgery latency bandwidth jitter packet loss frame loss clinical trial
- telesurgery guideline 100 ms redundancy bandwidth jitter packet loss
- remote robotic surgery technical guidelines network failover QoS
- telesurgery multidimensional latency bandwidth jitter packet loss interaction
- hinotori bandwidth compression packet loss image degradation
- telesurgery delay image compression bitrate 10 20 60 120 Mbps
- 5G standalone telesurgery buffer video freeze congestion
- redundant communication packet duplication telesurgery
- Starlink / LEO / GEO satellite telesurgery latency freezing
- RTP H.264 packet loss NAL fragmentation retransmission FEC jitter buffer
- surgical video packet loss AI robustness Endo-C6

## Inclusion
Retain sources that contribute direct evidence on telesurgery network performance, clinically relevant guidelines, network/video compression experiments, failover/redundancy, access-technology behavior, media transport/recovery mechanisms, or direct downstream surgical-AI effects.

## Evidence hierarchy
1. randomized/controlled human clinical evidence;
2. peer-reviewed clinical case series/trials;
3. current consensus/guidelines;
4. peer-reviewed experimental/animal/system validation;
5. standards (IETF) for codec/transport mechanisms;
6. peer-reviewed generic video-coding evidence, explicitly labelled adjacent;
7. accepted surgical-AI evidence where it directly tests packet-loss-like corruption.

## Interpretation rules
- Preserve **one-way**, **RTT**, **network delay**, **added latency**, **encode/decode**, **display**, and **total teleoperation latency** as separate quantities.
- A reported tolerated latency is system/task/operator specific unless a guideline defines it normatively.
- Bandwidth requirement is system + codec + traffic-mix dependent.
- Raw packet loss ≠ frame loss.
- Packet loss may be hidden or transformed by FEC, retransmission, path redundancy, jitter buffering and decoder concealment.
- Jitter measured at RTP/network level may be partially absorbed before decoded frames reach the model.
- Adaptive bitrate/resolution/frame-rate changes are encoder/control responses, not direct synonyms for low bandwidth.
- Satellite and best-effort networks must be characterized over time; a single mean can hide severe tails.
- P0.6 may identify a working impairment abstraction but cannot finalize Track C novelty before P0.7.

## Screening accounting
- **35 retained sources/resources**
- **12 excluded/deferred categories**
- **47 audit records/categories**

## Reproducibility
Before experiments or manuscript submission, re-check recent 2026 sources, guideline revisions, codec/transport implementation details for the selected system, and any actual network emulator/decoder stack used.
