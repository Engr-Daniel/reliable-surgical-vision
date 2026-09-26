# P0.6 Network → Transport/Codec → Received-Video Mechanism

## Central result
A network impairment does **not** directly specify what an AI model sees.

The causal chain is:

```text
network state
(latency, capacity, jitter, loss, reordering, outage)
        ↓
transport / path response
(queueing, late packets, lost packets, path switch)
        ↓
protection / recovery
(jitter buffer, FEC, NACK/RTX, redundant path)
        ↓
encoder / congestion response
(bitrate/QP, resolution, frame rate/layer changes where supported)
        ↓
codec packet dependency
(NAL units, frames, reference dependencies, GOP/keyframes)
        ↓
decoder behavior
(recovered packet, concealment, partial corruption, frame skip/freeze, delayed playout)
        ↓
received video state
(spatial quality, temporal continuity, timing, resolution, bitrate history)
        ↓
AI input distribution and temporal context
        ↓
prediction / calibration / uncertainty / abstention
```

## 1. Packet loss is not frame loss
H.264 over RTP can fragment a NAL unit across multiple packets. RFC 6184 states that if a fragmentation unit is lost, later fragments of that same NAL should be discarded. The resulting decoder effect depends on:
- which NAL/frame was affected;
- reference-frame dependency;
- recovery mechanisms;
- decoder concealment;
- playout deadline.

Thus “5% packet loss” cannot be simulated as “randomly drop 5% of frames” and still be called a packet-loss experiment.

## 2. Retransmission can convert loss into delay
RTP retransmission can recover selected packets, but a retransmitted packet is useful only if it arrives before the media deadline. This creates a latency–reliability trade-off.

## 3. FEC converts bandwidth into resilience
Forward-error correction proactively sends redundant information. It can reduce visible loss without waiting a round trip but consumes bandwidth; under congestion, excess redundancy can worsen network load.

## 4. Jitter buffers convert timing variation into playout delay
Moderate packet-arrival jitter can be absorbed by a buffer, making model-input timing smoother than raw network timing. A larger buffer can reduce late loss but increases end-to-end delay.

Therefore **network jitter ≠ AI input jitter** unless the buffering layer is defined.

## 5. Congestion can alter encoder state
Interactive media congestion control may lower target bitrate when queueing/loss increases. HEVC/RTP guidance also allows rate reduction through quantization or temporal-layer removal. Telesurgical systems may use proprietary adaptive bitrate/resolution/frame-rate logic.

Hence low capacity can appear to the AI as:
- stronger compression;
- reduced spatial detail;
- resolution change;
- frame-rate/temporal-layer change;
- or higher delay if adaptation is insufficient.

## 6. Redundancy can hide network faults
Dual paths, packet duplication and automatic failover can prevent a network fault from becoming a visible video fault. The monitoring system may observe severe path degradation while the AI sees an intact stream.

This is exactly why Track C must test whether network telemetry adds information beyond received-video evidence rather than assuming it does.

## 7. Experiment labels required later
A P0.7/P1 experiment must label its impairment as one of:
- **network-layer emulation** — packets traverse an emulator and real codec/decoder;
- **codec-layer manipulation** — bitrate/QP/resolution/frame-rate is directly changed;
- **decoded-video abstraction** — frames are dropped/frozen/compressed after decode;
- **natural trace replay** — actual measured network/video state is replayed.

Only the first (or a validated trace-driven equivalent) should be described as mechanistic network impairment without qualification.
