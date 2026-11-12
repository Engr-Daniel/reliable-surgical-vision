# P0.7 Open Questions Carried Forward to Phase 1

## Resolved by P0.7 (from earlier open-question lists)
| Earlier question | Resolution |
|---|---|
| P0.4 OQ20 / P0.3 OQ15 / P0.2 OQ28: one temporal + one spatial task, or a single task? | Single temporal task (online phase recognition); segmentation is a gated extension (`track-decision.md`) |
| P0.4 OQ22 / P0.6 OQ19: do Endo-C6 and TCSR-Monitor occupy Track C? | They occupy the abstraction and video-only-monitor cells; not the telemetry-incremental-value cell (X23) |
| P0.6 OQ20: does Heemeyer 2026 occupy compound network interaction? | Yes, for human outcomes (X10); Track A is absorbed |
| P0.6 OQ21: benchmark, method, mechanistic study, or multimodal prediction study? | Multimodal prediction study (RQ1) with a reliability audit (RQ2) and a mechanistic secondary (RQ3); no new method |
| P0.6 OQ23: what negative result drops Track C? | Pre-specified in `revised-research-questions.md` (H1a and H1b both fail) |
| P0.5 OQ12: is a separate OOD component needed? | No (X13 occupied) |
| P0.5 OQ13: failure prediction vs generic OOD? | Failure prediction |
| P0.5 OQ18: merge Tracks B and C? | Yes |
| P0.5 OQ19: phase or segmentation for observing a telemetry benefit? | Phase recognition |
| P0.6 OQ12: which task anchors the network experiment? | Online phase recognition |

## Gap validation (Phase 1, blocking)
1. Does networking/video-analytics literature (SIGCOMM, NSDI, MobiCom, MMSys, INFOCOM; 2018–2026) contain telemetry → AI-failure prediction evaluated against a video-only baseline?
2. Do MICCAI 2026 full proceedings or workshops (UNSURE, DEMI) contain conformal or selective phase recognition under corruption?
3. Has VISTA or a follow-up added downstream AI evaluation since May 2026?
4. Is the deferred medical-image packet-loss study (EX12) relevant once located?

## Design (Phase 1)
5. Exact V1 feature set: which no-reference quality metrics are computable at real-time rates on surgical video?
6. Which receiver-side transport/decoder statistics can actually be exposed by FFmpeg/GStreamer (decode errors, concealment flags, jitter-buffer state)?
7. Should NACK/RTX and FEC be on (realistic, hides loss) or off (exposes loss)? Probably both, as a factor.
8. What tier set best spans nominal / degraded-plausible / stress regimes for a 25-fps clinical stream, and does VISTA's 640×480/30-fps envelope transfer?
9. Is the ΔAUROC ≥ 0.02 threshold well calibrated against the expected precision with ~40 test procedures?
10. Minimum Mondrian stratum size for telemetry-stratified calibration.
11. Can online phase models with evidence gating (IX03) hide failures from confidence-based monitors?

## Data (Phase 1 desk checks → Phase 2)
12. PhaKIR phase taxonomy vs Cholec80; source-video independence.
13. Do the Cholec80/PhaKIR/AutoLaparo terms permit storing re-encoded/degraded derivatives?
14. Is HeiChole needed as a larger natural-shift replication if PhaKIR's eight videos are too few?

## Carried unchanged
15. P0.6 OQ24–26: real platform telemetry is unavailable; the abstraction gap must be stated (X26).
16. P0.5 OQ29–30: cost of false alarms and the human-fallback interpretation of deferral for phase-recognition outputs.
