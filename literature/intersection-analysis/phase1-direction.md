# P0.7 → Phase 1 Direction

## Phase 1 per the roadmap
`ROADMAP.md`: **Phase 1 — Gap Validation.** *Stress-test candidate contributions against primary literature. Define precise hypotheses, tasks, comparison methods, and exclusion criteria.*

P0.7 sets the direction. Phase 1 must verify it before Phase 2 (dataset acquisition) begins. No data are downloaded and no models trained in Phase 1.

## Evidence-backed direction
**One integrated study:** online surgical phase recognition on video delivered through an emulated telesurgical media pipeline, evaluating (RQ1) the incremental value of receiver-observable telemetry for failure detection and selective deferral, (RQ2) the validity of calibration and conformal coverage, and (RQ3) mechanism-dependent degradation. See `revised-research-questions.md`.

Why this direction and not another (traceable to `intersection-map.csv`):
| Choice | Evidence |
|---|---|
| Telemetry-incremental-value question as primary | X22/X23 not found in retained evidence; all neighbouring cells occupied (X07, X11, X14, X20, X21) |
| Online phase recognition, not segmentation | Per-frame labels allow telemetry alignment (P0.3); temporal mechanism (P0.6); X14 (TCSR-Monitor) occupies segmentation monitoring |
| Strong video-only baseline required | RI34 shows multi-cue video monitors far exceed entropy; IX05 shows simple ensemble baselines are strong |
| Real media pipeline, not clip corruption | P0.6 rule "packet loss ≠ frame loss"; X07 (Endo-C6) already covers clip-level abstraction |
| VISTA tiers as starting envelope | IX01 is a published surgical forward-video tier set with released code; NW04 / P0.6 for factor ranges |
| Cholec80 + PhaKIR (+ AutoLaparo) | P0.3 shortlist; full video; independent centres; lineage overlap avoided |
| Reliability ladder, not a new method | X12–X15 occupied; P0.5 protocol |

## Phase 1 work packages

### P1.1 — Targeted gap-validation search (blocking)
The highest-risk cells (X22, X23; residual risk **high**) were only shallowly searched in P0.7.
- **Venues:** ACM SIGCOMM, NSDI, MobiCom, MobiSys, MMSys, IEEE INFOCOM, ICC/Globecom, IEEE TMM/TCSVT, SenSys/IPSN (2018–2026); MICCAI 2026 full proceedings and UNSURE/DEMI workshops, IPCAI 2026, IJCARS, MedIA, IEEE TMI (2024–2026); teleoperated-driving perception literature.
- **Query families:** "network telemetry" / "QoS" / "packet loss" / "transport state" × "DNN accuracy prediction" / "failure prediction" / "model confidence" / "video analytics" / "edge inference"; "accuracy prediction under network conditions"; "network-aware uncertainty"; "telesurgery AI reliability"; "surgical video streaming AI".
- **Also check:** full text of Endo-C6, TCSR-Monitor and VISTA for related-work leads; citing papers of each.
- **Exit:** a screening log in `literature/gap-validation/` and an updated verdict for C4/C5/B6/B7/A6. If an occupying study is found, re-run `novelty-stress-test.md` before P1.2.

### P1.2 — Pre-registration of hypotheses and analysis plan
Freeze, in `research/integrated-study/preregistration.md`: H1–H3 thresholds, failure definitions (*k*, *b*), monitor model families (logistic regression and gradient-boosted trees, chosen in advance), telemetry windows, splits, bootstrap procedure, multiplicity handling (H1a/H1b as co-primary with Holm correction; others secondary), and the stopping/reporting rules for negative results.

### P1.3 — Media-pipeline specification
Specify, without implementing:
- encoder (libx264 baseline; HEVC optional), GOP/keyframe interval, rate control, resolution and frame rate;
- RTP packetisation (RFC 6184), NACK/RTX (RFC 4588) and FEC on/off conditions;
- emulator (Linux NetEm with Gilbert–Elliott; optional NetFI-style trace-driven models, IX02);
- receiver jitter-buffer policy; decoder and concealment behaviour (FFmpeg or GStreamer, versions pinned);
- per-frame log schema: capture timestamp, frame ID, arrival/decode time, decode errors, concealment/freeze flags, and per-window network/transport statistics;
- a check that VISTA code (IX01) can be reused and under what licence. Adapting a published pipeline is preferred to building from scratch.

### P1.4 — Feature-tier and leakage specification
Define V0/V1/N1/N2 exactly (`revised-research-questions.md`). Prove by construction that no feature uses emulator ground truth or the tier identity, and that V1 can detect pixel-visible freezes.

### P1.5 — Dataset gate checks (desk checks only)
- Cholec80: request route, licence, and the canonical procedure-level split to adopt.
- PhaKIR: access, licence, phase-taxonomy compatibility with Cholec80, and confirmation of no source-video overlap with Cholec80.
- AutoLaparo: access and phase-taxonomy handling (cross-procedure: evaluate with its own label set or as reliability-only).
- Re-verify that terms permit re-encoding and storing derived (degraded) video.

### P1.6 — Feasibility and power
- Estimate compute: encoding/decoding passes × tiers × procedures, plus inference.
- Simulate whether 40 Cholec80 test procedures give adequate precision for the ΔAUROC = 0.02 target under procedure-level bootstrap (using published phase-model error rates). Adjust the tier count rather than the threshold if precision is inadequate.
- Fix calibration-set size and the minimum Mondrian stratum size for RQ2.

### P1.7 — Baseline model selection
Choose two online phase models with public code and causal inference: one TCN-based (e.g. TeCNO, SV09) and one transformer-based (e.g. LoViT, SV11). Record the version/commit and whether evidence gating (IX03) is present, because gating may mask failures.

## Phase 1 exit criteria
- [x] P1.1 targeted search complete; C4/C5 verdict confirmed (2026-11-12; `literature/gap-validation/`).
- [x] Pre-registration frozen (v1.1; `research/integrated-study/preregistration.md`).
- [x] Pipeline specification written; reuse decision recorded (VISTA pipeline code not released → independent build). *Author review pending.*
- [x] Feature tiers and leakage controls specified.
- [x] Dataset desk checks passed (PhaKIR taxonomy identical to Cholec80).
- [x] Feasibility/power memo produced (criterion amended as a result).
- [x] Two baseline models selected with pinned versions (TeCNO, Surgformer; LoViT excluded).

## Exclusions carried into Phase 1
- No segmentation, TVLM, command-path or haptic experiments.
- No new UQ/OOD/conformal method development.
- No claims about Toumai or any proprietary codec/network stack; Nigeria/Starlink evidence is used as motivation only (P0.6 OQ26).
- No clinical safety or threshold language.
