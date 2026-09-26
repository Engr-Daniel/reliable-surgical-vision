# P0.6 Telesurgery Network Architecture

## 1. Logical traffic classes
A remote robotic surgical system can carry several traffic classes with different timing/reliability needs:

1. **Surgeon command / robot control** — master-side pose/button/foot-control information toward the patient-side robot.
2. **Robot/system feedback** — state, alarms, acknowledgements and, where supported, force/haptic feedback.
3. **Surgical video** — typically the largest sustained flow, primarily patient site → surgeon site; often stereoscopic/high-resolution.
4. **Audio / telepresence** — surgeon–bedside communication and situational awareness.
5. **Monitoring / telemetry** — RTT, loss, jitter, throughput, encoder bitrate, display/frame-loss status, device state and safety events.
6. **Security / management** — VPN, authentication, monitoring and network-management traffic.

The exact protocol and prioritization are platform specific. Current technical guidelines require use-case-defined surgical-grade network behavior rather than prescribing one universal architecture.

## 2. Why video and control cannot be reduced to one bandwidth number
Total network load depends on:
- encoded video bitrate and number of views;
- control/feedback frequency;
- audio/telepresence;
- FEC/retransmission/redundant copies;
- encryption/tunnelling overhead;
- monitoring and security traffic.

The Japanese 2026 guideline explicitly states that required bandwidth varies with robot model and video-compression method. Hinotori experiments likewise show different behavior when image bitrate and link capacity are changed.

## 3. Working end-to-end decomposition

```text
surgeon command path:
input sensing
→ local control processing
→ packetization/security
→ network forward path
→ patient-side decode/control
→ robot actuation

visual feedback path:
operative scene
→ camera/sensor
→ image processing
→ video encode/compression
→ packetization/security
→ network reverse path
→ recovery/buffering
→ depacketization/decode/concealment
→ display/model input
```

A telesurgical “delay” may measure only one portion of this path. P0.6 therefore forbids combining reported latency values unless their definitions match.

## 4. QoS and path engineering
Current evidence describes:
- guaranteed/dedicated fiber or OTN;
- 5G dedicated/private/SA links;
- QoS prioritization/network slicing concepts;
- multi-carrier redundancy;
- packet duplication over independent paths;
- VPN/SD-WAN and automatic failover;
- public/best-effort networks where capacity must be verified;
- satellite links for remote areas.

## 5. Safety boundary
Network reliability is only one safety layer. Published clinical programmes also use bedside teams, local takeover/conversion plans, preoperative network stress testing, emergency disconnection drills and safe robot behavior during communication faults.
