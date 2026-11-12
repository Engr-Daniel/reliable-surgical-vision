# P0.7 Intersection Analysis

## Question
> Across task × dataset × shift × reliability concept × network layer, which combinations are already established, which are partially addressed, and which were not found in the programme's evidence base?

## Inputs
- `global-evidence-matrix.csv`: 175 rows / 165 unique sources from P0.1–P0.7, each coded manually on common dimensions (code book in `build_global_evidence_matrix.py`).
- `coverage-summary.md`: generated counts and intersection probes.
- `intersection-map.csv`: 26 hand-rated intersection cells with anchors, residual risk and implications.
- P0.3 dataset evidence (`datasets/`) for the dataset axis.

## 1. What the integrated evidence base looks like
The coded matrix reveals three structural facts.

1. **The literatures barely touch.** None of the 37 unique telesurgery sources evaluates an AI model; the 16 that report an outcome report **human operator or clinical** outcomes. Of the 53 surgical-CV sources that evaluate a model, only two touch networks at all: Endo-C6's clip-level packet-loss abstraction (SH18) and a delivery-latency deployment study (IX06).
2. **Reliability and shift are mostly studied apart in surgery.** Of those 53, 11 involve a reliability concept. Only 5 of those also involve a shift, and only 2 (prediction-volatility work, SH20/SH21) involve a temporal factor. Neither of those applies an external temporal degradation.
3. **The network→AI relationship is established outside medicine.** Every retained source in which an AI model is evaluated under network conditions is either generic video analytics/VANET (IX07–IX10) or a surgical delivery-latency study (IX06). **No** retained source in any domain uses network or system telemetry to predict AI reliability.

These counts describe the retained evidence base only. Residual-risk ratings in `intersection-map.csv` express how likely it is that unretrieved work occupies a cell.

## 2. Occupancy by layer

### 2.1 Saturated or occupied: do not build contributions here
| Area | Cells | Why it is closed |
|---|---|---|
| Segmentation under natural shift | X01 | Many benchmarks and DA/DG methods |
| Segmentation under smoke/blood/low light | X03 | SegSTRONG-C, CaRTS, SAM2 robustness |
| Phase recognition under natural shift | X02 | HeiChole, PhaKIR, inter-hospital transfer, SPA |
| Phase temporal stability | X06 | Volatility, consistency, TFI/evidence gating (MICCAI 2026) |
| Packet-loss-burst corruption of surgical TVLMs | X07 | Endo-C6 (MICCAI 2026) |
| Network effects on human operators, incl. compound | X09, X10 | Clinical trials, Heemeyer 2026 response surface, VISTA, NetFI |
| Network → decoded surgical-video quality | X11 | Telesurgery system studies; VISTA PSNR/SSIM/VMAF/freeze per tier |
| Surgical calibration/UQ, OOD/open-set | X12, X13 | FGRM, calibrated phase, open-set phase, OpenMIBOOD |
| Surgical segmentation failure monitoring under degradation with conformal calibration | X14 | TCSR-Monitor |
| Medical segmentation selective prediction/failure detection | X15 | SDC, learning-to-abstain, failure-detection benchmark |
| Network/codec → DNN accuracy (generic) | X20 | DDS, AccMPEG, DNN-aware retransmission, VANET |
| Telemetry → future QoS (generic) | X21 | Predictive QoS for teleoperated driving |

### 2.2 Partially addressed: baseline layers, not contributions
- **X04:** phase recognition under controlled visual corruption (combined photometric corruption only).
- **X05:** compound visual corruption (adjacent GI endoscopy; combined photometric).
- **X17:** selective/risk–coverage evaluation of phase recognition under shift.
- **X18:** cross-centre calibration transfer for phase models.

### 2.3 Not found in retained evidence: candidate contribution space
| Cell | Description | Residual risk |
|---|---|---|
| **X23** | Surgical CV failure prediction / selective deferral using **receiver-observable network + transport + decoder telemetry**, tested for incremental value over video-only cues | **high** |
| **X22** | Same question in **any** domain | **high** |
| X19 | Phase-recognition calibration / selective / conformal behaviour under **decoder-mediated** network impairment | medium |
| X16 | Phase-recognition conformal prediction sets under any shift | medium |
| X24 | Conformal calibration **stratified by deployment-observable network state** | medium |
| X08 | Conventional surgical CV evaluated on video passed through a **real encoder/transport/emulator/decoder** pipeline | medium |
| X25 | Segmentation failure monitoring under decoder-mediated impairment | medium (high overlap pressure from TCSR) |
| X26 | Real clinical platform telemetry aligned to AI output | blocked by data access |

## 3. Dataset axis
P0.3 fixes several constraints that apply regardless of which cell is pursued:
- network/temporal experiments require **complete video** at native frame rate (Cholec80, PhaKIR, AutoLaparo, HeiChole, MultiBypass140, SAR-RARP50);
- dense **per-frame** labels are needed to align a per-frame error label with a telemetry window. Phase datasets provide them (Cholec80 at 25 fps; PhaKIR phases on every frame). Segmentation labels are sparse (e.g. PhaKIR masks at 1 fps; Endoscapes subsets);
- CAMMA lineage overlap (Cholec80 / CholecT50 / CholecSeg8k / CholecInstanceSeg / Endoscapes) rules out combining these as independent domains;
- natural external shift with independent procedures is available via PhaKIR (3 centres; only 8 public videos), HeiChole (3 centres; ~156 GB) and AutoLaparo (different procedure).

**Implication.** The not-found cells X19/X23/X24 are best instantiated with **online phase recognition on Cholec80** (development) plus **PhaKIR** (external natural-shift replication), with AutoLaparo as optional cross-procedure replication. Segmentation (X25) loses on two counts: label density for telemetry alignment, and overlap pressure from TCSR-Monitor.

## 4. Where the contribution space actually is
Section 2.3 cells share one structure:

`network state → transport/recovery → decoder → received frames → online phase model → reliability decision`

with the key empirical question being **what the reliability layer gains from information that is not in the pixels** (X23). X19/X16/X24 are the reliability-audit side of the same experiment. X08 is the substrate that all of them need, but it is not a sufficient contribution on its own.

Ingredients from adjacent cells must be reused, not reinvented:
- pipeline and tier design: VISTA (IX01), NetFI (IX02), P0.6 Level B protocol;
- video-only failure cues: TCSR-Monitor (RI34) cue families, ensemble disagreement (IX05);
- reliability ladder and metrics: P0.5 protocol, risk–coverage (IX05, RI36), TFI (IX03);
- telemetry features: P0.6 minimum telemetry list, pQoS literature (IX11).

## 5. Boundary
This analysis does not establish novelty. It identifies where the programme's evidence base contains no occupying work, rates the risk that such work exists elsewhere, and passes the highest-risk cells (X22/X23) to a targeted Phase 1 search before any experimental commitment.
