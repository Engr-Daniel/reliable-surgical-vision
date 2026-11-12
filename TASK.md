# TASK.md — Active Research Tasks

## Phase 0 — Research Foundation

### P0.1 Toumai architecture reconnaissance — COMPLETE
**Milestone:** `v0.0.1 — Toumai Architecture Reconnaissance`

### P0.2 Surgical computer-vision landscape — COMPLETE
**Milestone:** `v0.0.2 — Surgical Computer-Vision Landscape`

### P0.3 Dataset reconnaissance — COMPLETE
**Milestone:** `v0.0.3 — Dataset Feasibility Map`

### P0.4 Distribution-shift literature — COMPLETE
**Milestone:** `v0.0.4 — Distribution-Shift Evidence Map`

### P0.5 Reliable-inference literature — COMPLETE
**Milestone:** `v0.0.5 — Reliable-Inference Evidence Map`

### P0.6 Telesurgery / network literature — COMPLETE
- [x] Map network architecture and traffic classes.
- [x] Distinguish RTT, processing/display delay, jitter, packet loss, frame loss, capacity and bitrate.
- [x] Compare guideline/experimental threshold evidence.
- [x] Map transport/codec/recovery/buffering mechanisms.
- [x] Map redundancy/failover/QoS.
- [x] Map fiber, 5G, best-effort and satellite evidence.
- [x] Audit direct downstream surgical-AI evidence.
- [x] Produce candidate network/codec impairment protocol.
- [x] Produce `literature/telesurgery-networking/rq-answer-matrix.md`.
- [x] Produce `task-completion-report/P0.6_COMPLETION_REPORT.md`.

**Suggested milestone after commit/review:** `v0.0.6 — Telesurgery / Network Evidence Map`

### P0.7 Intersection Analysis & Novelty Stress-Test — COMPLETE
- [x] Integrate P0.1–P0.6 into one evidence matrix.
- [x] Build task × dataset × shift × reliability × network intersection map.
- [x] Stress-test Tracks A–C against the complete literature base.
- [x] Identify saturated, partially occupied and defensible intersections.
- [x] Decide whether tracks remain separate, merge, narrow or are dropped. → **Merged** (C primary; B narrowed; A absorbed).
- [x] Revise final candidate research questions.
- [x] Define the evidence-backed Phase 1 experimental direction.
- [x] Remove unsupported novelty/“first” claims. → None present; prohibitions recorded.
- [x] Produce `literature/intersection-analysis/rq-answer-matrix.md`.
- [x] Produce `task-completion-report/P0.7_COMPLETION_REPORT.md`.

**Suggested milestone after commit/review:** `v0.0.7 — Intersection Analysis & Novelty Stress-Test`

## Phase milestone
**M0 — Evidence-backed Research Map** — **reached 2026-11-12.**

---

## Phase 1 — Gap Validation

Plan: `literature/intersection-analysis/phase1-direction.md`. No data acquisition or training until Phase 1 exits.

### P1.1 Targeted gap-validation search — COMPLETE (2026-11-12)
- [x] Search networking/video-analytics venues (SIGCOMM, NSDI, MobiCom, MobiSys, MMSys, INFOCOM, ICC/Globecom; 2018–2026) for telemetry → AI-failure prediction (cells X22/X23).
- [x] Search MICCAI 2026 proceedings/workshops, IPCAI, IJCARS, MedIA, TMI (2024–2026) for phase-recognition conformal/selective reliability under corruption or network delivery (X16/X19).
- [x] Check related work and citing papers of Endo-C6, TCSR-Monitor and VISTA.
- [~] Locate deferred record EX12; verify bibliographic fields marked "verify" (IX07 confirmed; others still open).
- [ ] Read full text of deferred MICCAI 2026 titles (EX18) before Phase 2.

**Outcome:** no occupying study; X22/X23 residual risk high → medium; V1 baseline strengthened with a learned pixel→error predictor.
- [x] Record results in `literature/gap-validation/` and update C4/C5/B6/B7/A6 verdicts.

### P1.2 Pre-registration — COMPLETE (2026-11-12)
- [x] `research/integrated-study/preregistration.md` v1.1 (H1a amended before any data; see amendment log).

### P1.3 Media-pipeline specification — COMPLETE
- [x] `research/integrated-study/pipeline-spec.md`: GStreamer/x264/RTP/NetEm/jitter buffer/decoder, receiver log schema, "capture once, decode deterministically", compute/storage.
- [x] Reuse decision: VISTA repository (MIT) contains no pipeline code, so tier parameters are reused and the pipeline is built independently.

### P1.4 Feature-tier and leakage specification — COMPLETE
- [x] `research/integrated-study/feature-spec.md`: V0/V1 (incl. learned pixel→error predictor)/N1/N2; six leakage controls with tests.

### P1.5 Dataset desk checks — COMPLETE
- [x] `research/integrated-study/dataset-desk-checks.md`: Cholec80 / PhaKIR (same 7 phases) / AutoLaparo (gated).

### P1.6 Feasibility and power — COMPLETE
- [x] `research/integrated-study/feasibility/`: 40 procedures × 5 tiers adequate under stated (optimistic) assumptions; v1.0 joint criterion had 0.33 power, so it was amended.

### P1.7 Baseline model selection — COMPLETE
- [x] `research/integrated-study/baseline-selection.md`: TeCNO @0c4313f (GPL-3.0), Surgformer @5d57e46 (CC BY-NC 4.0); LoViT and Trans-SVNet excluded.

### Phase 1 open items (non-blocking)
- [ ] **Author review and sign-off** of the pre-registration and specs (marks M1).
- [ ] Choose a LICENSE for this repository compatible with GPL-3.0 / CC BY-NC dependencies (not vendored).
- [ ] Read full text of deferred MICCAI 2026 titles (P1.1 EX18).
- [ ] Verify remaining "to verify" bibliographic fields (IX02, IX08, IX09, IX11, GV02–GV10, GV13–GV14).

## Phase milestone
**M1 — Validated, pre-registered study design** — deliverables complete 2026-11-12; **pending author sign-off.**

---

## Phase 2 — Dataset & Task Feasibility (next)
- [ ] P2.1 Request Cholec80, PhaKIR (and AutoLaparo if gated in); re-verify terms at download.
- [ ] P2.2 Build and validate the media pipeline (pipeline-spec §6 checks).
- [ ] P2.3 Reproduce TeCNO and Surgformer Cholec80 baselines on the pinned split.
- [ ] P2.4 Implement feature extraction with the leakage unit tests (feature-spec §5).
- [ ] P2.5 Pilot: stream 2 calibration videos (33–34) through all tiers; check logs, alignment and realised loss.
