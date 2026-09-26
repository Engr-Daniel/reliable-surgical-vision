# P0.6 Telesurgery / Network Evidence Landscape

**Evidence cutoff:** 2026-09-26  
**Status:** Complete focused technical reconnaissance

## Executive synthesis
P0.6 establishes that telesurgery networking is not a single “latency” problem. It is a coupled cyber-physical and media-transport problem in which delay, jitter, loss and capacity interact with QoS, path redundancy, encoder adaptation, codec dependency, retransmission/FEC, buffering and decoder concealment.

The field has now progressed from feasibility demonstrations to randomized clinical evidence, current guidelines, explicit failover/QoS validation, satellite trials and multidimensional network experiments. Consequently, broad claims such as “study multiple network impairments in telesurgery” are already occupied.

The research opportunity for Reliable Surgical Vision is narrower: **connect measured/system-grounded network state to the decoded video actually seen by a surgical-CV model, then test whether network/system telemetry adds reliability information beyond the video itself.**

## 1. There is no universal latency threshold
Current sources deliberately use different definitions and contexts. Japan’s 2026 guideline recommends ≤100 ms for network round-trip transmission plus new compression/decompression delay. CRSA’s 2026 consensus uses <300 ms total teleoperation latency, ideally <200 ms. Experimental work ranges from sub-100-ms preferred regions to successful specialized high-delay demonstrations.

The contradiction is only apparent: platform controllers, tasks, operators, video processing and metric endpoints differ. P0.6 therefore treats latency thresholds as **system-specific operating regions**.

## 2. Bandwidth affects video through adaptation and congestion
Hinotori bandwidth experiments show that a high video bitrate can overload a constrained link, increasing packet loss and degrading the image. Lower encoder bitrates may preserve operation by sacrificing source image quality. Other systems dynamically adjust compression as bandwidth falls.

Thus low bandwidth does not have one fixed visual signature. It can produce:
- queueing/latency;
- packet loss;
- lower encoder bitrate;
- stronger quantization/compression;
- resolution/frame-rate/layer adaptation;
- or combinations of these.

## 3. Packet loss is not frame loss
RTP/H.264 and HEVC standards make the mapping explicit: one video frame can span many packets/NAL units, and reference dependencies can propagate damage. FEC, RTX, packet duplication and decoder concealment may hide packet loss. Conversely, one critical packet loss can damage more than one displayed frame.

A future experiment that randomly drops decoded frames is scientifically useful as a temporal stress test, but it must not be labelled equivalent to network packet loss.

## 4. Jitter can be hidden by buffering
RTP-level jitter is packet-arrival timing variation. Interactive media systems commonly use jitter/playout buffers; moderate variation can be absorbed at the price of latency. Consequently the model may receive regularly timed frames even when the network is jittery, or may receive freezes/skips only once buffering is exhausted.

## 5. Redundancy can decouple network failure from video failure
Telesurgery evidence includes:
- duplicated packets over two independent links;
- multi-carrier hot standby;
- QoS prioritization;
- automatic rerouting/VPN recovery;
- bedside takeover and safe-state behavior.

This has a direct Track C implication: **network telemetry could be abnormal while received video remains normal because redundancy worked.** A useful network-aware model must learn this conditional relationship rather than treating bad network metrics as automatic AI failure.

## 6. Network type alone is a weak descriptor
“5G,” “fiber,” or “satellite” is not sufficient. Evidence shows major differences among 5G SA/NSA configurations, QoS settings and congestion states. Starlink can be smooth one day and show severe latency/bitrate tails another. GEO satellite can support a specialized controller despite very high latency.

Experiments should characterize the actual QoS trace and media pipeline, not only the access label.

## 7. Combined network impairments are already studied
Heemeyer et al. 2026 explicitly model latency, bandwidth, jitter and packet loss as a multidimensional space and report interaction effects, with latency and packet loss dominant in their in-vitro navigation setup.

Therefore Track A cannot claim novelty merely from testing several network variables jointly.

## 8. Direct network→AI evidence is still much thinner
Endo-C6 now provides direct surgical/endoscopy AI evidence for packet-loss-burst corruption, so “packet loss in surgical AI” is not untouched. But its corruption operates at the video-clip level rather than through a measured telesurgical transport/codec stack.

P0.6 did not establish a mature conventional phase/segmentation benchmark that has all of:
- real/emulated network telemetry;
- codec/transport/recovery;
- decoded surgical video;
- downstream prediction + calibration/uncertainty/selective inference;
- network-telemetry incremental-value analysis.

That intersection is the primary P0.7 target.

## 9. Clinical network evidence is now substantial
The 2026 multicentre randomized BMJ trial provides stronger clinical evidence than feasibility cases alone: under stable networks (RTT 20.1–47.5 ms, 0–1.5 frame losses per telesurgery), telesurgery was non-inferior to local robotic surgery within the trial’s defined margin.

This does not mean those values are safety thresholds; it means stable operation in that observed region has randomized clinical support.

## 10. Satellite evidence warns against averages
LEO experiments demonstrate useful average latency but meaningful temporal variability and intermittent image disturbance/freezing. GEO evidence shows very high delay can sometimes be handled with specialized high-delay control. Therefore mean RTT alone is inadequate; tail latency, outage/freeze events and recovery time matter.

## 11. P0.6 decision for Track C
Track C remains scientifically plausible but is now tightly defined.

A useful study should test:
1. video-only reliability prediction;
2. network/system telemetry-only prediction;
3. fused video + telemetry prediction;
4. whether fusion improves error detection, selective risk/calibration, or warning lead time;
5. whether any improvement survives different shift types or codec settings.

If telemetry provides no incremental value after decoded-video features are known, that would be a meaningful negative result and a reason to narrow/drop Track C.

## 12. P0.6 conclusion
The network→video bridge is now explicit enough to proceed to P0.7. No final impairment parameters or novelty claims are fixed. P0.7 must integrate P0.1–P0.6 and decide which exact task × dataset × shift × reliability × network intersection remains defensible.
