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

### P1.1 Targeted gap-validation search — READY TO START (blocking)
- [ ] Search networking/video-analytics venues (SIGCOMM, NSDI, MobiCom, MobiSys, MMSys, INFOCOM, ICC/Globecom; 2018–2026) for telemetry → AI-failure prediction (cells X22/X23).
- [ ] Search MICCAI 2026 proceedings/workshops, IPCAI, IJCARS, MedIA, TMI (2024–2026) for phase-recognition conformal/selective reliability under corruption or network delivery (X16/X19).
- [ ] Check related work and citing papers of Endo-C6, TCSR-Monitor and VISTA.
- [ ] Locate deferred record EX12; verify bibliographic fields marked "verify" in P0.7 sources.
- [ ] Record results in `literature/gap-validation/` and update C4/C5/B6/B7/A6 verdicts.

### P1.2 Pre-registration — PENDING P1.1
- [ ] Freeze H1–H3 thresholds, failure definitions, monitors, windows, splits, bootstrap and multiplicity rules in `research/integrated-study/preregistration.md`.

### P1.3 Media-pipeline specification — PENDING
- [ ] Encoder/RTP/NACK-FEC/emulator/jitter-buffer/decoder specification and per-frame log schema; VISTA reuse and licence decision.

### P1.4 Feature-tier and leakage specification — PENDING
- [ ] Define V0/V1/N1/N2; prove no emulator ground truth or tier identity leaks; V1 detects pixel-visible freezes.

### P1.5 Dataset desk checks — PENDING
- [ ] Cholec80, PhaKIR (taxonomy, overlap), AutoLaparo; derivative-storage terms.

### P1.6 Feasibility and power — PENDING
- [ ] Compute estimate; precision simulation for ΔAUROC = 0.02 with ~40 test procedures; calibration and stratum sizes.

### P1.7 Baseline model selection — PENDING
- [ ] One TCN-based and one transformer-based online phase model with pinned versions; note evidence gating.

## Phase milestone
**M1 — Validated, pre-registered study design**
