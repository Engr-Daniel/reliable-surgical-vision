# P1.1 Gap-Validation Report

**Task:** Phase 1, P1.1: targeted gap-validation search (blocking)  
**Date:** 2026-11-12  
**Inputs:** `literature/intersection-analysis/phase1-direction.md` §P1.1; cells X08, X16, X19, X22–X24 in `intersection-map.csv`  
**Records:** `source-screening-log.csv` (14 retained GV01–GV14; 8 excluded/deferred EX13–EX20)

## 1. What was searched
| Surface | Query families | Purpose |
|---|---|---|
| Video analytics / edge inference (ACM MM, SIGCOMM, MobiCom-indexed, arXiv cs.NI) | accuracy prediction from network conditions; ground-truth-free accuracy estimation; network-aware uncertainty; uncertainty under packet loss | X22 |
| Teleoperated driving / remote AV control | perception failure prediction under network QoS; QoE prediction from network metrics; network-aware teleoperation testbeds | X22 |
| Semantic / task-oriented communication | channel-aware task-accuracy prediction; confidence gating | X22 |
| V2X cooperative perception | perception reliability under packet loss/latency; runtime monitoring | X22 |
| MICCAI 2026 main + satellite proceedings (UNSURE, SafeSurg, EMA) | phase-recognition uncertainty / abstention / conformal; failure detection | X16, X19 |
| Telesurgery video transmission (arXiv, IJCARS-indexed) | AI on transmitted video; network-degraded segmentation/phase; follow-ups of VISTA, Endo-C6, TCSR | X08, X23 |

## 2. Findings that change the picture

### 2.1 Pixel-based AI-accuracy prediction is established outside surgery
DAO (ACM MM 2022) estimates server-side DNN accuracy for offloaded video from the content itself, and flags failure (mAP = 0) cases (GV01). Machine-vision-aware quality metrics and no-reference models that predict detector accuracy are also established (GV06, GV07). Confidence-only accuracy monitors exist too (GV05, GV13).

**Implication:** the V1 "decoded-video" baseline in RQ1 is not a straw man. It must include a learned, task-aware quality-to-accuracy predictor, not only generic NR-IQA scores. This **raises the bar** for H1a.

### 2.2 Network → AI accuracy is established in more fields than P0.7 recorded
Real C-V2X loss/latency degrades cooperative detection (GV09), and robustness methods for packet-drop interruption exist (GV10). Edge recognition under network-limited compression is handled by switching models on image-quality metrics (GV08). In every case the network affects the AI **through the pixels/features**, and the decision uses pixel- or confidence-side information.

### 2.3 Network telemetry is used to predict *human* video quality, not AI reliability
Kafetzis et al. forecast a VMAF-like score from loss, jitter and throughput for remote AV control (GV02), extending P0.7's patent-level observation (EX01). None compares telemetry with video-side features, and none predicts AI behaviour.

### 2.4 The reverse direction is common
AI uncertainty or impact steers transport (retransmission, compression ratio, progressive transmission; IX09, EX14). Transport telemetry predicting AI failure was **not** found.

### 2.5 Surgical side: active neighbouring group, no AI evaluation yet
The VISTA authors have also released LiteSC (Sept 2026), semantic communication for telesurgical video on CholecSeg8k. It reports reconstruction quality only (PSNR/SSIM/LPIPS), with no downstream segmentation or phase evaluation (GV04). TeleSim adds another network-tiered teleoperation testbed without AI (GV03).

**Implication:** this group is the most likely to add downstream-AI evaluation to a surgical network pipeline. **Time-to-result matters** for X08. X23 differs from their trajectory only through the telemetry-incremental-value design.

### 2.6 MICCAI 2026
Additional surgical reliability work exists, all outside network delivery and phase conformal sets: surgical VQA abstention and uncertainty-calibrated tool-pose tracking (GV12). TCSR-Monitor's released code shows LOCO AUROC 0.814 vs 0.481 for entropy (GV11), a reusable baseline design. Two titles could not be resolved to full text and are deferred (EX18).

## 3. Updated verdicts
| Claim / cell | P0.7 verdict | P1.1 verdict | Residual risk | Change |
|---|---|---|---|---|
| C4 / X22: telemetry predicts AI failure (any domain) | Open in retained evidence | **Open in retained evidence** | high → **medium** | Five adjacent fields searched; all occupy neighbouring cells only |
| C5 / X23: surgical telemetry incremental value over video-only monitor | Open | **Open** | high → **medium** | No surgical AI-on-network-pipeline study found; VISTA group on watch list |
| A6 / X08: conventional surgical CV through real pipeline | Open | **Open** | medium | LiteSC/TeleSim do not evaluate AI; timing risk noted |
| B6 / X16, X19: phase conformal / reliability under shift | Open | **Open, pending EX18** | medium | Two MICCAI 2026 titles to read |
| B7 / X24: telemetry-stratified conformal | Open | **Open** | medium | No change |
| V1 baseline strength | "TCSR-style" | **TCSR-style + learned quality→accuracy predictor (DAO/MV-aware metrics)** | — | Baseline strengthened |

**Conclusion:** P1.1 does **not** trigger the pre-experimental kill criterion for Track C. The primary question survives with medium residual risk. One condition is now explicit: the video-only comparator must include a learned predictor of AI accuracy from decoded frames, because that idea is established (DAO, machine-vision-aware metrics).

## 4. Consequences for the study design
1. **V1 extended** (`revised-research-questions.md`): add a learned frame-quality → phase-error predictor trained on the same impairment training tiers as the full monitor. This makes "beyond the pixels" a fair test.
2. **H1a unchanged** (ΔAUROC ≥ 0.02). The stronger baseline makes a positive result more meaningful and a negative result more likely; both are informative.
3. **Watch list** (re-check monthly until Phase 3): VISTA/LiteSC/TAMS authors (Warwick); Endo-C6 authors; TCSR-Monitor authors.
4. **Before Phase 2:** read the full text of the EX18 titles.

## 5. Residual limitations
- Proceedings of SIGCOMM/NSDI/MobiCom were reached through web search, not venue-by-venue table-of-contents review.
- Bibliographic fields for GV07/GV08 and IX09 remain to verify. IX07 venue confirmed as ACM SIGCOMM 2020.
- EX12 (wireless packet loss vs medical-image classification) was not located.

## 6. P1.1 exit
- [x] Targeted search complete across five adjacent fields and 2026 surgical venues.
- [x] C4/C5/B6/B7/A6 verdicts updated; no occupying study found; kill criterion not triggered.
- [x] Design consequence recorded (V1 strengthened).
- [ ] EX18 full-text check (moved to P1.5/P1.7 desk work; non-blocking for P1.2).

**P1.1 status: COMPLETE.** Next: P1.2 pre-registration.
