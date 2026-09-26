# P0.6 Source Index

## NW01 — Clinical practice guidelines for telesurgery, 2nd Edition
- **Authors:** Mori M et al.
- **Year / venue:** 2026 — Surgery Today 56:1047–1065
- **Evidence type:** Guideline
- **DOI/URL:** https://doi.org/10.1007/s00595-026-03295-z
- **Network focus:** Network requirements; latency; jitter; loss; bandwidth; redundancy
- **Main finding:** Guideline states required bandwidth is robot/codec-specific; calls for no large delay/significant jitter/loss; recommends network+new encode/decode processing delay within 100 ms maximum; redundancy should be tested through failure/switch/recovery.
- **Boundary:** Consensus/guideline threshold, not a universal physical limit.

## NW02 — Expert Consensus-Based Technical Guidelines for Remote Robotic-Assisted Surgery and Procedures
- **Authors:** Wang Y et al.
- **Year / venue:** 2025 — World Journal of Surgery 49:1708–1721
- **Evidence type:** Technical guideline
- **DOI/URL:** https://doi.org/10.1002/wjs.12653
- **Network focus:** Surgical-grade networks; QoS; redundancy; failover; security
- **Main finding:** Defines fundamental requirements for reliable surgical-grade networking and explicitly avoids universal numeric latency/jitter/bandwidth specifications because use cases differ.
- **Boundary:** Industry/clinical expert consensus; does not evaluate a single clinical system.

## NW03 — Clinical Recommendations for Remote Robotic Assisted Surgery From the CRSA 2025 International Consensus Conference
- **Authors:** Fong Y et al.
- **Year / venue:** 2026 — World Journal of Surgery
- **Evidence type:** Clinical consensus
- **DOI/URL:** https://doi.org/10.1002/wjs.70468
- **Network focus:** Uptime; bandwidth; latency; jitter; packet loss
- **Main finding:** Consensus recommends 99.999% uptime, guaranteed bandwidth, total teleoperation latency <300 ms and ideally <200 ms, minimal/no jitter and zero/near-zero loss.
- **Boundary:** Consensus target differs from Japanese guideline definition; not evidence of one universal safe threshold.

## NW04 — A Multidimensional Perspective on Network Conditions in Telesurgery
- **Authors:** Heemeyer C et al.
- **Year / venue:** 2026 — Advanced Intelligent Systems
- **Evidence type:** Peer-reviewed experimental study
- **DOI/URL:** https://doi.org/10.1002/aisy.70546
- **Network focus:** Latency × bandwidth × jitter × packet loss interactions
- **Main finding:** Pilot in-vitro navigation study treats network state as a 4D space; worsening conditions reduced feasibility and performance; latency and packet loss were dominant and interactions were significant.
- **Boundary:** In-vitro neurovascular task and system-specific network stack; downstream CV reliability not studied.

## NW05 — Tele-assessment of bandwidth limitation for remote robotics surgery
- **Authors:** Ebihara Y et al.
- **Year / venue:** 2022 — Surgery Today 52:1653–1659
- **Evidence type:** Peer-reviewed experimental study
- **DOI/URL:** https://doi.org/10.1007/s00595-022-02497-5
- **Network focus:** Bandwidth; packet loss; image degradation; video compression
- **Main finding:** At 145 Mbps available bandwidth, 3–7% packet loss and visible image degradation occurred; 120-Mbps video setting performed worse than 40/20 Mbps under that constrained condition; authors concluded ≥150 Mbps for their hinotori setup.
- **Boundary:** System-specific requirement; video/control/audio overhead and codec settings differ across platforms.

## NW06 — Verification of delay time and image compression thresholds for telesurgery
- **Authors:** Takahashi Y et al.
- **Year / venue:** 2023 — Asian Journal of Endoscopic Surgery 16:255–261
- **Evidence type:** Peer-reviewed animal/experimental study
- **DOI/URL:** https://doi.org/10.1111/ases.13150
- **Network focus:** Added delay; video bitrate/compression
- **Main finding:** Eight robotic surgeons tested 30/50/100/150-ms delay and 120/60/30/20/10-Mbps video; 30–50 ms were rated feasible while 100–150 ms were rated lower; compression down to 10 Mbps remained usable in that setup.
- **Boundary:** Subjective/animal-model validation and hinotori-specific encoder; delay definition is experiment-specific.

## NW07 — Maximum acceptable communication delay for the realization of telesurgery
- **Authors:** Nankaku A et al.
- **Year / venue:** 2022 — PLOS ONE 17:e0274328
- **Evidence type:** Peer-reviewed simulator/dynamic-task study
- **DOI/URL:** https://doi.org/10.1371/journal.pone.0274328
- **Network focus:** Network + encode/decode delay; task performance
- **Main finding:** 34 participants tested 0–300 ms; performance worsened as delay increased; experienced surgeons remained comparable to less-experienced no-delay performance at ≤100 ms in this setup.
- **Boundary:** Prototype/simulated tasks; fixed latency with no jitter/loss; ~50 ms encoder/decoder contribution in delayed conditions.

## NW08 — Effect of video lag on laparoscopic surgery: correlation between performance and usability at low latencies
- **Authors:** Kumcu A et al.
- **Year / venue:** 2017 — International Journal of Medical Robotics and Computer Assisted Surgery 13
- **Evidence type:** Peer-reviewed human simulator study
- **DOI/URL:** https://doi.org/10.1002/rcs.1758
- **Network focus:** Video/display latency
- **Main finding:** 15 trainees and 14 surgeons showed significant performance and usability deterioration at 105 ms added video latency; surgeons were more negatively affected.
- **Boundary:** Laparoscopic trainer, not complete teleoperation loop; added-latency definition differs from RTT.

## NW09 — Influence of network latency and bandwidth on robot-assisted laparoscopic telesurgery: A pre-clinical experiment
- **Authors:** Wang Y et al.
- **Year / venue:** 2024 — Chinese Medical Journal
- **Evidence type:** Peer-reviewed preclinical study
- **DOI/URL:** https://doi.org/10.1097/CM9.0000000000003257
- **Network focus:** Latency; bandwidth; adaptive image compression; frame loss
- **Main finding:** 108 animal operations over 3000 km explored 170–320-ms total latency and bandwidth down to <1 Mbps; image clarity was adaptively reduced as bandwidth narrowed; latency increased workload more than image-clarity reduction.
- **Boundary:** Authors call 320 ms acceptable for their system/tasks; should not be generalized as universal limit.

## NW10 — Impact of data compression and security devices on telesurgery systems
- **Authors:** Morohashi H et al.
- **Year / venue:** 2026 — Surgery Today 56:359–368
- **Evidence type:** Peer-reviewed experimental study
- **DOI/URL:** https://doi.org/10.1007/s00595-025-03142-7
- **Network focus:** Video bitrate; available bandwidth; security-device overhead
- **Main finding:** hinotori tests used 120–20 Mbps image bitrates across 1-Gbps best-effort/IOWN and 100-Mbps guaranteed links; stable operation depended on adequate headroom; security devices added ≤2 ms in tested conditions.
- **Boundary:** Artificial-organ task and specific security/network devices.

## NW11 — Toward safe clinical deployment of remote robotic surgery in Japan: five-year validation of the hinotori system using 5G wireless communication
- **Authors:** Hara T et al.
- **Year / venue:** 2025 — International Journal of Clinical Oncology 30:2389–2398
- **Evidence type:** Peer-reviewed technical/operational synthesis
- **DOI/URL:** https://doi.org/10.1007/s10147-025-02874-3
- **Network focus:** 5G SA/NSA; QoS; congestion; video continuity; failover
- **Main finding:** Summarizes >30 validations: QoS prevented packet loss/video degradation under heavy competing traffic; redundancy testing showed VPN reconnection in 5–11 s after simulated failures; Sub6 SA produced more predictable behavior than some alternatives.
- **Boundary:** Synthesis around one platform and Japanese deployment programme.

## NW12 — System-level evaluation of 5G standalone communication infrastructure for robotic telesurgery
- **Authors:** Hara T et al.
- **Year / venue:** 2026 — International Journal of Computer Assisted Radiology and Surgery
- **Evidence type:** Peer-reviewed feasibility study
- **DOI/URL:** https://doi.org/10.1007/s11548-026-03738-5
- **Network focus:** 4G/5G NSA/SA; RTT; buffers; congestion; video freezes
- **Main finding:** 5G SA configurations achieved sub-120-ms latency with stable video in controlled tests; 4G/high-bitrate NSA produced higher latency/freezes; SA Sub6 degraded beyond heavy background traffic (>400 Mbps in the reported setup).
- **Boundary:** Controlled system test; not a clinical trial and results are configuration-specific.

## NW13 — Construction of redundant communications to enhance safety against communication interruptions during robotic remote surgery
- **Authors:** Morohashi H et al.
- **Year / venue:** 2023 — Scientific Reports 13
- **Evidence type:** Peer-reviewed experimental study
- **DOI/URL:** https://doi.org/10.1038/s41598-023-37730-9
- **Network focus:** Dual links; packet duplication; failover
- **Main finding:** Two commercial lines and redundant encoder interfaces were used; across 16 pig surgeries, 175 line switches were induced and no surgeon-detected abnormalities coincided with switching.
- **Boundary:** Animal study and specific redundancy design; brief switching-gap behavior can depend on path delay asymmetry.

## NW14 — Safety and reliability of telesurgery in China: a multicenter, single-arm, phase I clinical trial
- **Authors:** Tai S et al.
- **Year / venue:** 2025 — International Journal of Surgery
- **Evidence type:** Peer-reviewed clinical trial
- **DOI/URL:** https://doi.org/10.1097/JS9.0000000000002792
- **Network focus:** Clinical network metrics; codec; frame loss; seamless switching
- **Main finding:** 18 patients across four hospitals: mean RTT 38.38±13.25 ms, jitter 0.39±0.29 ms, encode/decode latency 20.02±0.06 ms, code rate 12.77±0.57 Mbps, display latency 21.35±3.42 ms; no frame loss.
- **Boundary:** Single-arm clinical feasibility; system-specific network/video optimization.

## NW15 — Reliability of urological telesurgery compared with local surgery: multicentre randomised controlled trial
- **Authors:** Wang Y et al.
- **Year / venue:** 2026 — BMJ 392:e083588
- **Evidence type:** Peer-reviewed randomized controlled trial
- **DOI/URL:** https://doi.org/10.1136/bmj-2024-083588
- **Network focus:** Clinical network latency; display latency; frame loss; system malfunction
- **Main finding:** 72 participants randomized; telesurgery was non-inferior to local surgery under trial conditions; telesurgery distances 1000–2800 km, mean RTT 20.1–47.5 ms and 0–1.5 lost frames per telesurgery.
- **Boundary:** Trial conditions were well-controlled; does not establish tolerance to degraded networks.

## NW16 — Feasibility and Safety of Cross-Regional 5G-Enabled Remote Robot-Assisted Laparoscopic Surgery: A Retrospective Case Series of 21 Patients
- **Authors:** Pan Y et al.
- **Year / venue:** 2026 — International Journal of Medical Robotics and Computer Assisted Surgery 22:e70214
- **Evidence type:** Peer-reviewed clinical case series
- **DOI/URL:** https://doi.org/10.1002/rcs.70214
- **Network focus:** Redundant 5G; RTT; jitter; loss; protocol thresholds
- **Main finding:** 21 Toumai procedures over ~3700 km: mean RTT 37.7±5.6 ms, jitter 2.2±0.5 ms, no packet loss/interruption; preset local network criteria and backup carriers were used.
- **Boundary:** Retrospective; observed stable range does not validate failure thresholds.

## NW17 — Establishing an international clinical framework for telesurgery: the first bidirectional transatlantic procedure across a world-record distance
- **Authors:** Almazeedi S et al.
- **Year / venue:** 2026 — Journal of Robotic Surgery
- **Evidence type:** Peer-reviewed clinical report
- **DOI/URL:** https://doi.org/10.1007/s11701-026-03367-9
- **Network focus:** Transatlantic latency; jitter; loss; uptime
- **Main finding:** Bidirectional procedures across >12,000 km reported mean latency ~196 ms, jitter 1 ms, packet loss 0.19%, and 100% connection uptime.
- **Boundary:** Small clinical report; platform/control architecture and delay definition matter.

## NW18 — A New Technological Approach to Robotic Telesurgery with Starlink: Safe Telesurgery
- **Authors:** Ueda K et al.
- **Year / venue:** 2025 — Annals of Thoracic Surgery Short Reports 3:867–871
- **Evidence type:** Peer-reviewed animal study
- **DOI/URL:** https://doi.org/10.1016/j.atssr.2025.04.018
- **Network focus:** LEO satellite; RTT variability; image disturbance
- **Main finding:** Swine lung telesurgery over ~1000 km via Starlink reported average RTT ~130 ms and brief image/operation disturbances about every five minutes, possibly related to switching/weather.
- **Boundary:** Animal experiment; satellite conditions can vary temporally and causality of disturbances was not proven.

## NW19 — Real-world evaluation of low-earth-orbit satellite communication for surgical telementoring: implications for future robotic surgery
- **Authors:** Oki E et al.
- **Year / venue:** 2026 — Journal of Robotic Surgery
- **Evidence type:** Peer-reviewed field evaluation
- **DOI/URL:** https://doi.org/10.1007/s11701-026-03936-y
- **Network focus:** LEO temporal variability; bitrate; freezing
- **Main finding:** One session averaged 34.4 ms latency and 2.51 Mbps, but the same setup next day reached 765-ms maximum latency and low-bitrate periods with marked quality deterioration; other configurations had intermittent freezing.
- **Boundary:** Telementoring rather than robot control; nonetheless strong evidence of LEO temporal variability.

## NW20 — Feasibility and safety evaluation of remote robotic surgery under high latency conditions based on satellite communication
- **Authors:** Zhang G et al.
- **Year / venue:** 2025 — Intelligent Surgery
- **Evidence type:** Peer-reviewed clinical report
- **DOI/URL:** https://doi.org/10.1016/j.isurg.2025.05.001
- **Network focus:** GEO satellite; high-latency control
- **Main finding:** Two human liver resections used APSTAR-6D with average end-to-end latency 632 ms and low Mbps links; specialized high-delay control enabled completion.
- **Boundary:** Two cases and specialized control system; not evidence that ordinary telesurgery tolerates 632 ms.

## NW21 — The era of telesurgery: insights from ultra-long-distance Asia to Middle East human telesurgery robotic assisted radical prostatectomy
- **Authors:** Aldousari S et al.
- **Year / venue:** 2025 — Journal of Robotic Surgery 19:108
- **Evidence type:** Peer-reviewed clinical report
- **DOI/URL:** https://doi.org/10.1007/s11701-025-02274-9
- **Network focus:** ~7000-km fiber; backups; cloud/VPN; RTT
- **Main finding:** Shanghai–Kuwait Toumai case reported average RTT 181.4 ms; fiber primary with 5G/wired backups and bedside robotic-surgeon takeover capability.
- **Boundary:** Single international case; deployment-specific cloud/routing architecture.

## NW22 — Safety and feasibility of telerobotic cholecystectomy via a 5G network: a prospective controlled clinical trial
- **Authors:** Yang X et al.
- **Year / venue:** 2025 — Surgical Endoscopy 39:7336–7346
- **Evidence type:** Peer-reviewed clinical trial
- **DOI/URL:** https://doi.org/10.1007/s00464-025-12005-8
- **Network focus:** 5G delay; jitter; loss; bandwidth; standby
- **Main finding:** 20 remote cases over ~70 km reported average network delay 43.4 ms, jitter 4 ms, packet loss <1%, upload 98.3 Mbps and download 213 Mbps; later synthesis reports a ~3-s signal interruption triggering robot standby.
- **Boundary:** Delay terminology is study-specific; standby detail comes from later review.

## NW23 — Safety and feasibility of robot-assisted remote radical gastrectomy for gastric cancer based on 5G communication technology (FUTURE-04)
- **Authors:** Guo Y et al.
- **Year / venue:** 2026 — Gastric Cancer 29:238–249
- **Evidence type:** Peer-reviewed prospective clinical trial
- **DOI/URL:** https://doi.org/10.1007/s10120-025-01687-7
- **Network focus:** Network RTT vs total delay; packet loss
- **Main finding:** 27 cases over 15 km reported network RTT 31.6±3.8 ms but total delay 226.2±4.4 ms, showing that network RTT is not total teleoperation latency; packet loss <0.1%.
- **Boundary:** Short distance; total-delay decomposition is platform-specific.

## NW24 — Telerobotic partial nephrectomy and radical prostatectomy using a hybrid network: A single-center prospective experience
- **Authors:** Pokhrel A et al.
- **Year / venue:** 2026 — European Journal of Surgical Oncology 52:111963
- **Evidence type:** Peer-reviewed clinical study
- **DOI/URL:** https://doi.org/10.1016/j.ejso.2026.111963
- **Network focus:** Fiber vs 5G hybrid network latency
- **Main finding:** 13 cases over ~25 km reported median latency 12 ms over fiber and 46 ms over 5G with no major network disruptions.
- **Boundary:** Single centre and short distance.

## NW25 — Application of 5G Remote Robotic-assisted Laparoscopy in Urological Surgery: A Small Sample Analysis
- **Authors:** Zhou H et al.
- **Year / venue:** 2025 — Urology 197:110–114
- **Evidence type:** Peer-reviewed clinical series
- **DOI/URL:** https://doi.org/10.1016/j.urology.2024.11.019
- **Network focus:** 5G latency; loss; throughput
- **Main finding:** 14 cases over 52 km reported 0% packet loss, 216.5 Mbps down/86.6 Mbps up, and study-defined minimum/maximum latency measures.
- **Boundary:** Small cohort; reported latency terms are not RTT.

## NW26 — RTP: A Transport Protocol for Real-Time Applications (RFC 3550)
- **Authors:** Schulzrinne H et al.
- **Year / venue:** 2003 — IETF RFC 3550
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc3550
- **Network focus:** RTP sequence/timestamps; RTCP loss/jitter measurement
- **Main finding:** Defines RTP interarrival jitter from packet spacing relative to RTP timestamps and distinguishes transient congestion/jitter from persistent loss indicators.
- **Boundary:** Generic real-time media standard, not telesurgery-specific.

## NW27 — RTP Payload Format for H.264 Video (RFC 6184)
- **Authors:** Wang Y-K et al.
- **Year / venue:** 2011 — IETF RFC 6184
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc6184
- **Network focus:** H.264 NAL packetization; fragmentation-loss effects
- **Main finding:** A lost fragment can invalidate the remaining fragments of the same NAL unit; loss therefore does not map one-to-one to a dropped video frame.
- **Boundary:** Codec payload standard; actual decoder concealment is implementation-dependent.

## NW28 — RTP Payload Format for High Efficiency Video Coding (HEVC) (RFC 7798)
- **Authors:** Wang Y-K et al.
- **Year / venue:** 2016 — IETF RFC 7798
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc7798
- **Network focus:** HEVC packetization; congestion/loss; bitrate adaptation
- **Main finding:** Requires congestion responsiveness; real-time encoders can adapt bitrate via quantization, while scalable streams may drop enhancement-layer NAL units.
- **Boundary:** Generic media transport; telesurgical systems may use proprietary codecs.

## NW29 — RTP Retransmission Payload Format (RFC 4588)
- **Authors:** Rey J et al.
- **Year / venue:** 2006 — IETF RFC 4588
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc4588
- **Network focus:** NACK/retransmission trade-off
- **Main finding:** Retransmission can recover selected lost media packets but consumes bandwidth and time; it is useful only when retransmitted data can arrive before its playout deadline.
- **Boundary:** Generic RTP recovery mechanism.

## NW30 — WebRTC Forward Error Correction Requirements (RFC 8854)
- **Authors:** Uberti J et al.
- **Year / venue:** 2021 — IETF RFC 8854
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc8854
- **Network focus:** FEC vs retransmission; latency/bandwidth trade-off
- **Main finding:** FEC proactively spends bandwidth; RTX/FEC retransmission is preferred when RTT fits the latency budget, while proactive FEC may be useful when waiting a round trip is too slow.
- **Boundary:** WebRTC guidance; not proof of a particular telesurgical implementation.

## NW31 — Congestion Control Requirements for Interactive Real-Time Media (RFC 8836)
- **Authors:** Jesup R, Sarker Z
- **Year / venue:** 2021 — IETF RFC 8836
- **Evidence type:** Internet standard
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc8836
- **Network focus:** Low-delay media; jitter buffers; late data
- **Main finding:** Interactive media needs low delay; moderate jitter can be absorbed by jitter buffers, but late real-time media may become useless.
- **Boundary:** Generic interactive-media requirements.

## NW32 — Self-Clocked Rate Adaptation for Multimedia (RFC 8298)
- **Authors:** Johansson I, Sarker Z
- **Year / venue:** 2017 — IETF RFC 8298
- **Evidence type:** Experimental RFC
- **DOI/URL:** https://www.rfc-editor.org/rfc/rfc8298
- **Network focus:** Congestion-controlled media rate adaptation
- **Main finding:** SCReAM links congestion signals, RTP queue delay and loss events to a target media bitrate, illustrating how network conditions can drive encoder-rate changes.
- **Boundary:** One generic RTP congestion-control design, not a telesurgery requirement.

## NW33 — Error concealment schemes for H.264/AVC and H.265/HEVC video decoders
- **Authors:** Usman M et al.
- **Year / venue:** 2015 — Picture Coding Symposium
- **Evidence type:** Peer-reviewed video coding study
- **DOI/URL:** https://doi.org/10.1109/PCS.2015.7170081
- **Network focus:** Decoder error concealment
- **Main finding:** Reviews/spans spatial, temporal and hybrid concealment strategies showing that decoded output after packet loss depends on concealment, not just loss rate.
- **Boundary:** Generic video coding evidence.

## NW34 — A study of packet loss effects on H.264 video quality
- **Authors:** Tommasi F et al.
- **Year / venue:** 2015 — Journal of Visual Communication and Image Representation
- **Evidence type:** Peer-reviewed video quality study
- **DOI/URL:** https://doi.org/10.1016/j.jvcir.2014.12.003
- **Network focus:** H.264 packet loss; bitrate; visual quality
- **Main finding:** Shows packet-loss impact depends on coding/bitrate and video-quality measurement; lower bitrate can sometimes trade source quality for improved loss resilience.
- **Boundary:** Non-surgical video; used only for codec-mechanism context.

## NW35 — On the Robustness of Temporal Vision-Language Models for Surgical Endoscopy Videos
- **Authors:** Rashid D et al.
- **Year / venue:** 2026 — MICCAI 2026
- **Evidence type:** Accepted peer-reviewed conference paper
- **DOI/URL:** https://papers.miccai.org/miccai-2026/0726-Paper4661.html
- **Network focus:** Downstream surgical AI under visual/packet-loss corruption
- **Main finding:** Endo-C6 includes packet-loss bursts alongside defocus, haze, motion blur, shot noise and cautery smoke for temporal surgical/endoscopy VLM evaluation.
- **Boundary:** Corruption is applied at clip level; it does not establish a physical packet→codec→decoder mapping for a telesurgical stream.
