# Toumai Technical Literature & Architecture Reconnaissance

**Phase:** 0 — Research Foundation  
**Task:** P0.1  
**Final audit date:** 25 September 2026  
**Evidence cutoff:** 25 September 2026  
**Conclusion status:** **P0.1 complete at the public-evidence reconnaissance level**

## Executive summary

The public record supports an evidence-backed systems reconstruction of the Toumai MT-1000 and its tele-robotic use. The platform is a human-controlled master–slave surgical robot comprising a surgeon console (MSS810), patient surgical platform (SSS800), vision platform (VSS820), 3D endoscopy/image-processing components, and surgical instruments. Regulatory review material describes a master-side sensing and kinematic mapping chain feeding patient-side closed-loop joint-position control. [S01]

Peer-reviewed technical literature adds a four-arm patient cart, closed surgeon console, 7-DoF instruments, force feedback, a reported 4000 Hz master–slave response characteristic, FPGA image processing, dual-fiber visual transport and reported imaging latency below 50 ms. It also describes vascular-enhancement and intelligent smoke-removal algorithms. However, the same study explicitly states that force-feedback precision and algorithm reliability were **not objectively quantified**, so their presence is documented without treating their performance as independently validated. [S03]

Human telesurgery studies show Toumai operating over multiple deployment architectures rather than one universal network topology: 5G, dedicated fiber, hybrid fiber/5G, standard institutional networks, and multi-carrier redundant 5G have all been reported. Manufacturer sources additionally report broadband and satellite compatibility. Measured network conditions vary substantially by deployment, and timing definitions differ; P0.1 therefore preserves network RTT, study-reported “delay,” total system delay, imaging latency and master–slave response time as separate quantities.

The most technically detailed remote series currently available is Pan et al. (2026): a 3700-km collaboration using a China Telecom 5G dedicated line as primary link with China Mobile and China Unicom dedicated-line backups, QoS for video/control traffic, explicit preoperative stress/disconnection drills, a local takeover plan, and detailed latency/jitter/loss monitoring. [S11]

For the September 2026 Nigerian RHV–Nisa deployment, public reporting supports a >500-km Toumai right radical nephrectomy with Starlink as primary connectivity and MTN as backup. No raw RTT, jitter, loss, throughput, codec or failover telemetry was identified by the evidence cutoff. [S15–S16]

P0.1 therefore closes with a defensible architectural basis and a clearly bounded set of unknowns. It does **not** claim a novel research gap. That requires P0.2–P0.7.

---

## 1. Device composition

The NMPA/CMDE technical review for MT-1000 identifies:
- **MSS810** — surgeon/physician console;
- **SSS800** — patient surgical platform;
- **VSS820** — vision/imaging platform;
- 3D electronic endoscope;
- endoscopic image processor;
- passive and high-frequency surgical instruments;
- accessories. [S01]

The current official MicroPort product page corroborates the MSS810/SSS800/VSS820 model structure. [S02]

### Evidence interpretation
This component structure is high-confidence because it is supported by regulatory and manufacturer product documentation. It should be distinguished from tele-surgery add-on/network infrastructure, which varies by deployment.

---

## 2. Master–slave control architecture

The strongest public description of the control logic is regulatory:

1. the surgeon manipulates the master control arms;
2. sensors measure master-joint angles;
3. master forward kinematics is computed;
4. master–slave mapping is applied;
5. slave inverse kinematics determines reference joint positions and velocities;
6. the patient-side system performs closed-loop joint-position control;
7. instrument motion reproduces the surgeon's intended master-side motion. [S01]

This yields the evidence-backed abstraction:

`surgeon → master manipulators/sensors → kinematics + master–slave mapping → reference joint states → communications/control path → patient-side joint controller → robotic instruments`

What is **not** public:
- controller gains;
- exact servo-loop scheduling;
- command packet format;
- clock/synchronisation design;
- command-buffer semantics;
- remote failover state machine.

### Reported response/haptics
Pokhrel et al. report:
- master–slave frequency: **4000 Hz**;
- response time: **250 μs**;
- force-feedback sensitivity down to **0.1 N**. [S03]

These values are recorded exactly as reported. They are **not** interpreted as an end-to-end remote control loop or network latency. The paper itself states that advanced-feature technical performance was not objectively quantified. [S03]

---

## 3. Patient-side mechanical architecture

Peer-reviewed literature reports:
- four-arm patient cart;
- 7-DoF wrist articulation;
- instrument diameter ≤8.4 mm;
- up to 540° instrument rotation;
- automated collision detection. [S03]

The architecture is therefore suitable for conventional multi-port robotic laparoscopy with remote master control, but public literature does not disclose the complete actuator/sensor/control design.

---

## 4. Visual architecture

### 4.1 Documented local imaging path
Toumai is reported to use:
- integrated 3D electronic endoscopy;
- FPGA real-time image processing;
- dual-fiber optical transmission;
- Vascular Enhancement Algorithm;
- Intelligent Smoke Removal Algorithm;
- reported imaging latency **<50 ms**. [S03]

Evidence-backed local pathway:

`operative scene → 3D endoscope → image acquisition → FPGA processing / optional enhancement → optical transmission → surgeon display`

### 4.2 Reliability caveat
The same study explicitly states that the technical performance of advanced features—including force-feedback precision and **algorithm reliability**—was not objectively quantified. [S03]

Therefore:
- existence of enhancement functions = supported;
- accuracy/robustness of enhancement functions = **not established**;
- effects of enhancement on downstream learned CV = **unknown**.

### 4.3 Remote visual path
Telesurgery necessarily adds remote transport between image generation and remote presentation. Manufacturer material claims ultra-low-latency image compression and adaptive network optimisation, but the public record does not reveal:
- codec(s);
- profile/bitrate;
- frame rate adaptation;
- resolution adaptation;
- GOP/keyframe strategy;
- packet-loss concealment;
- jitter-buffer policy;
- exact encode/decode delay.

Those remain explicit P0.1 unknowns.

---

## 5. Safety and fallback architecture

Public evidence supports a layered safety model.

### Device layer
Reported Toumai safety features include:
- automatic collision detection;
- foot-pedal safeguards;
- protective lock behavior tied to operator viewing/head position. [S03]

### Communication layer
Published remote programmes use:
- primary/backup links;
- redundant carriers;
- QoS policies;
- preoperative stress testing;
- monitoring of latency/jitter/loss;
- emergency-disconnection drills. [S06, S11]

### Human layer
Published cases/series repeatedly retain patient-side capability:
- bedside robotic surgeon or surgical team;
- emergency takeover;
- conversion to conventional laparoscopy/open surgery if required. [S06, S08, S11]

### Demonstrated interruption response
The 2026 systematic review reports that a roughly **3-second signal interruption** during the Yang telecholecystectomy experience automatically triggered the master–slave safety mechanism, placing the robot in standby; the operation subsequently continued. [S12]

This is important real-world evidence of a safe-state response, but it does **not** disclose the precise network threshold, timer or internal state machine.

---

## 6. Quantitative communication evidence

A dedicated machine-readable table is provided in `toumai-network-metrics.csv`.

### Zhou et al. — 52 km, 14 urologic cases
Reported:
- average download: **216.5 Mbps**;
- average upload: **86.6 Mbps**;
- average maximum latency: **129.3 ms**;
- average minimum latency: **20.7 ms**;
- packet loss: **0%**. [S04]

### Yang et al. — 70 km, 20 remote cholecystectomies
Reported:
- average network delay: **43.4 ms**;
- jitter: **4 ms**;
- upload: **98.3 Mbps**;
- download: **213 Mbps**;
- packet loss: **<1%**. [S05]

### Aldousari et al. — ~7000 km international RARP
Reported:
- average RTT: **181.4 ms**;
- fiber broadband primary;
- 5G patient-side backup;
- two wired surgeon-side backup networks;
- experienced bedside robotic surgeon able to take over. [S06]

That specific deployment also used a cloud relay/VPN and firewalls; AWS Mumbai was chosen. This is deployment architecture, not a universal Toumai requirement. [S06]

### Sighinolfi et al. — 66 multispecialty operations
Reported mean delays:
- urology: **65 ms**;
- general surgery: **34 ms**;
- gynecology: **61 ms**;
with no conversion to local surgery. [S07]

### Pazzaglia et al. — ~20 km Belgium hysterectomy
Reported:
- mean latency: **20 ms**;
- jitter: **<10 ms**;
- high image quality;
- no connection issues;
- on-site standby surgeon. [S08]

### Guo et al. FUTURE-04 — 15 km, 27 gastrectomies
Reported:
- total delay: **226.2 ± 4.4 ms**;
- round-trip network delay: **31.6 ± 3.8 ms**;
- packet loss: **<0.1%**. [S09]

This is a particularly valuable example because it demonstrates why network RTT and total delay cannot be treated as interchangeable.

### Pokhrel et al. 2026 — 25 km hybrid network
Reported median latency:
- fiber: **12 ms**;
- 5G: **46 ms**;
with no major network disruptions. [S10]

### Pan et al. — ~3700 km, 21 operations
Network architecture:
- China Telecom 5G dedicated line = primary;
- China Mobile + China Unicom dedicated lines = backup;
- dedicated QoS for surgical control and video. [S11]

Preset programme requirements:
- RTT <100 ms; minimum safe threshold <200 ms;
- bandwidth >100 Mbps;
- packet loss <1%; minimum safe threshold <2%;
- jitter <10 ms. [S11]

Preoperative safeguards:
- system integration testing;
- network stress testing;
- audiovisual testing;
- emergency disconnection drills. [S11]

Observed:
- mean RTT **37.7 ± 5.6 ms**;
- mean maximum latency **47.5 ± 5.4 ms**;
- mean jitter **2.2 ± 0.5 ms**;
- packet loss **0%**;
- network interruptions **0**. [S11]

These thresholds are the protocol of this clinical programme; P0.1 does not elevate them to universal Toumai manufacturer safety limits.

---

## 7. Manufacturer-reported tele-surgical stack

MicroPort states that the commercially approved tele-surgical platform supports:
- 5G;
- broadband;
- dedicated fiber;
- satellite communication;
- ultra-low-latency image compression;
- multidimensional encryption;
- adaptive network optimisation;
- safety assurance protocols. [S13]

It also reports bidirectional network latency:
- **<50 ms** in inter-provincial procedures;
- **<150 ms** across telecom carriers/countries/continents. [S13]

A separate LEO satellite demonstration is reported with one-way latency **<60 ms**. [S14]

These are useful engineering clues, but are retained as **manufacturer claims**, not independent pooled performance estimates.

---

## 8. Nigerian RHV–Nisa deployment

Public reporting of the 19 September 2026 case supports:
- Toumai remote console at Redeemer's Health Village, Mowe/Redemption City, Ogun State;
- patient and bedside team at Nisa Premier Hospital, Abuja;
- >500 km separation;
- robot-assisted right radical nephrectomy;
- Starlink as primary connectivity;
- MTN as backup;
- approximately three-hour operation in some reports. [S15–S16]

### What P0.1 did not find
No public raw values were identified for:
- RTT;
- one-way latency;
- jitter;
- packet loss;
- throughput;
- video codec/bitrate;
- adaptive video state;
- primary→backup switchover time;
- whether backup was bonded, hot standby, warm standby or cold standby;
- frame-level degradation;
- archived network telemetry.

Therefore none of these is inferred from Chinese/European Toumai studies.

---

## 9. Relevance to reliable visual inference

The architecture suggests three distinct sources of deployment shift for future investigation.

### Clinical/optical
Smoke, blood, fluid, lens contamination, illumination, motion and anatomical variability.

### Platform-processing
Endoscopic sensor characteristics, FPGA processing, vascular enhancement, smoke removal, and any other image transformation.

### Communication-induced
If remote transport changes image quality or timing through compression, missing frames, buffering, temporal irregularity, resolution/framerate adaptation or corruption, the distribution seen by a downstream CV model may change.

The defensible research hypothesis is:

`network/system state → received video characteristics → input distribution → model performance/calibration/uncertainty → predict or abstain`

P0.1 does **not** establish that Toumai uses specific adaptive video behaviors, nor that network impairment has already been shown to degrade a Toumai-integrated AI model.

---

## 10. What is known vs unknown

### Strongly supported
- system component structure;
- master–slave kinematic/control principle at a high level;
- presence of 3D endoscopy, FPGA processing and enhancement algorithms;
- reported response/haptic/instrument characteristics;
- multiple clinical remote-network deployments;
- redundancy and bedside takeover as recurring safety layers;
- detailed network metrics in several studies.

### Not publicly established
- full end-to-end motion-to-photon latency budget;
- exact remote command transport protocol;
- codec and adaptive streaming logic;
- synchronization details;
- failover thresholds/state machine;
- full cybersecurity architecture intrinsic to the commercial product;
- objective reliability of smoke-removal/vascular-enhancement algorithms;
- frame-aligned network telemetry API;
- Nigerian case telemetry.

---

## 11. P0.1 conclusion

P0.1 is complete for its intended purpose: an evidence-backed technical reconnaissance, not a full product reverse-engineering exercise.

Toumai can be represented as a **human-in-the-loop, master–slave cyber-physical surgical system** with coupled control, imaging, networking and bedside-safety layers. The public evidence is sufficient to proceed to P0.2 while preserving a rigorous boundary around proprietary or unverified details.

No paper-level novelty claim is made here.

See:
- `literature/toumai/search-protocol.md`
- `literature/toumai/source-screening-log.csv`
- `literature/toumai/toumai-evidence-table.md`
- `literature/toumai/toumai-network-metrics.csv`
- `literature/toumai/open-technical-questions.md`
- `literature/toumai/references.bib`
