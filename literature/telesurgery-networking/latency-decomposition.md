# P0.6 Latency Decomposition and Threshold Evidence

## Core rule
**There is no single latency number that can be transferred safely between studies unless the measured endpoints are the same.**

A working decomposition is:

`T_total = T_capture + T_encode + T_forward + T_control/actuation + T_reverse + T_recovery/buffer + T_decode + T_display`

Some papers report only `T_network_RTT`; others report an added video/control delay or a broader total latency.

## Evidence showing why definitions matter
- Nankaku et al. deliberately separated a ~20-ms network RTT from ~50 ms encode/decode to create a 70-ms delayed condition.
- FUTURE-04 reported network RTT 31.6±3.8 ms but total delay 226.2±4.4 ms.
- The 2025 China phase-I clinical trial separately reports network RTT, encode/decode latency and display latency.

## Thresholds are not universal
Different evidence supports different operating targets because platforms, tasks, controllers and definitions differ:
- **Japan Surgical Society 2026 guideline:** network RTT + newly introduced information-processing delay should be within 100 ms maximum for telesurgical support.
- **CRSA 2026 consensus:** optimal total teleoperation latency <300 ms, ideally <200 ms.
- **Nankaku 2022:** dynamic-task performance increasingly worsened above ~100 ms in that setup.
- **Takahashi 2023:** 30–50 ms rated feasible; 100–150 ms lower in a hinotori pig experiment.
- **Chinese preclinical study:** operations were completed at total latency up to 320 ms with increased workload.
- **GEO satellite clinical report:** specialized high-delay control was used at ~632 ms in two liver cases.

Therefore P0.6 records **system-specific operating regions**, not one universal “safe latency.”

## Experimental implication
A future network experiment should report at least:
- network RTT distribution (median, p95/p99, max);
- one-way delay if synchronized measurement is possible;
- encoder and decoder processing latency;
- buffer/playout delay;
- decoded frame/display latency;
- control-loop delay if relevant;
- time-varying traces, not mean alone.
