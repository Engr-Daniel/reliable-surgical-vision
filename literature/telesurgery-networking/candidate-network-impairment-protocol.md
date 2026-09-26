# P0.6 Candidate Network / Video Impairment Protocol

## Status
**Working protocol for P0.7 only — no final experiment is authorized yet.**

## 1. Two-level experiment design
P0.6 recommends separating:

### Level A — decoded-video stress test
Manipulate received video directly:
- bitrate/compression;
- resolution;
- frame-rate/sampling;
- single missing frames;
- burst missing frames;
- freeze/last-frame hold;
- temporal context truncation.

This is reproducible and useful for AI sensitivity analysis, but must be called a **decoded-video abstraction**, not a network experiment.

### Level B — network+codec mechanistic test
Use a real media pipeline:

`source video → encoder → RTP/transport → network emulator → recovery/buffer → decoder → AI`

Record both network and decoded-video telemetry.

This is the preferred level for Track C if feasible.

## 2. Working network factors
Candidate factors, subject to P0.7 feasibility:
- added RTT/one-way delay;
- jitter distribution;
- random packet loss;
- burst packet loss;
- bottleneck bandwidth/capacity;
- outage/path-switch event.

**Do not finalize numeric levels from a single paper.** Use broad evidence to define a system-specific experimental envelope.

## 3. Working codec/video state
Record:
- codec and encoder implementation/version;
- target/actual video bitrate;
- resolution;
- nominal/decoded frame rate;
- keyframe/GOP interval;
- packetization mode/MTU;
- FEC enabled/disabled;
- NACK/RTX enabled/disabled;
- jitter-buffer target/current delay;
- decoder concealment behavior if exposed;
- decoded missing/duplicate/corrupt frame count;
- per-frame timestamps.

## 4. Minimum network telemetry carried to P0.7
Per analysis window:
- RTT: median/p95/p99/max;
- jitter: defined estimator + p95/max;
- packet loss rate;
- burst-loss length/count;
- available/bottleneck capacity if controlled;
- delivered throughput;
- path/failover state;
- retransmission count;
- FEC recovery count if available;
- sender queue/buffer delay;
- encoded bitrate;
- decoded frame-loss/freeze state.

## 5. Candidate impairment envelope — descriptive only
Literature spans from tens of milliseconds in stable clinical dedicated/5G links to hundreds of milliseconds in long-haul/satellite or intentionally stressed systems. Packet-loss experiments range from near-zero clinical operation to a few percent in stress studies; Heemeyer 2026 explicitly explores up to 2.5% packet loss and 0–140-ms jitter in a multidimensional in-vitro space.

P0.7 should define levels based on the chosen platform/emulator and distinguish:
- **nominal clinical range**;
- **degraded but plausible range**;
- **stress-test range**.

## 6. Factorial strategy
Do not immediately run a full dense Cartesian grid.
Recommended progression:
1. clean network baseline;
2. one-factor sensitivity curves;
3. select interaction pairs based on evidence;
4. response-surface/factorial design for compound network impairments;
5. add a visual shift only after network interactions are understood.

The latest 2026 telesurgery study already demonstrates that network factors interact, especially latency and packet loss, so a future contribution cannot be simply “test multiple network variables together.”

## 7. Track C test
The decisive Track C question should compare:
- **video-only reliability model**, versus
- **network/system telemetry-only model**, versus
- **video + network/system telemetry model**.

Evaluation should be against actual downstream AI error/reliability events, not surgeon subjective ratings alone.

A network-aware model is useful only if telemetry provides incremental information, earlier warning, or more stable failure detection after controlling for what is already observable in decoded video.

## 8. Safety wording
This research evaluates AI reliability and video/network mechanisms. It does not establish a clinically safe telesurgical network threshold or authorize autonomous intervention.
