# P0.7 Track Decision

## Decision
**Merge the three tracks into one integrated study with a single primary question and two secondary questions.** Each track directory stays as a work package (tracks are directories; see `MEMORY.md`), but there is one experimental pipeline, one dataset plan and one analysis plan.

| Former track | New role | Status | Research question |
|---|---|---|---|
| **C — Network-Aware Inference** | Primary hypothesis | **PRIMARY** | RQ1: incremental value of telemetry for failure prediction / selective deferral |
| **B — Selective Inference** | Reliability-evaluation layer (WP-B) | **NARROWED** | RQ2: do calibration / risk–coverage / conformal coverage survive decoder-mediated and natural shift; does telemetry-stratified calibration help |
| **A — Compound Shift** | Shift-construction and degradation-characterisation layer (WP-A) | **ABSORBED** | RQ3: does degradation mechanism matter at matched video quality |

No track is discontinued. Nothing is split.

## Rationale
1. **Shared substrate.** All three surviving claims (A6, B6/B7, C5) need the same encoder→transport→emulator→decoder pipeline, the same online phase model, the same telemetry logs and the same held-out procedures. Separate studies would triplicate infrastructure and invite inconsistent configurations.
2. **Robustness to a negative primary result.** RQ1 has a pre-specified kill criterion. RQ2 and RQ3 produce informative results whatever RQ1 shows, so the programme does not depend on a single positive finding.
3. **Overlap pressure.** Standalone A and B are largely occupied (`novelty-stress-test.md`). They are defensible only as the evaluation context for the telemetry question.
4. **Task choice favours a single temporal task.** Network-induced effects are temporal (freezes, frame loss, error propagation across GOPs). Online phase recognition is intrinsically temporal, has per-frame labels for telemetry alignment, and has no direct analogue of TCSR-Monitor. A dual-task benchmark would dilute the contribution (P0.4 OQ20).

## Scope locked by this decision
**In scope**
- online/causal surgical phase recognition;
- Cholec80 (development), PhaKIR (external natural-shift replication), AutoLaparo (optional cross-procedure replication);
- emulated network impairment through a real media pipeline (P0.6 Level B), with decoded-video abstractions (Level A) as controls;
- receiver-observable telemetry only;
- reliability ladder from P0.5; failure detection, risk–coverage, calibration and conformal coverage.

**Out of scope (until a gate reopens it)**
- segmentation (X25), retained only as a pre-registered extension after RQ1 is answered;
- temporal VLMs (occupied by Endo-C6);
- new UQ architectures;
- command/control-path impairment and haptics;
- proprietary platform telemetry (X26) unless a collaborator provides it;
- any clinical-safety or threshold claim.

## Conditions that would reopen this decision
- The Phase 1 targeted search finds occupying work for C4/C5 → re-run the stress test; if C5 falls, promote RQ2 to primary.
- Phase 2 shows that PhaKIR or AutoLaparo is inaccessible or that its phase taxonomy cannot be mapped to Cholec80 → replace the replication dataset (HeiChole candidate).
- RQ1 is rejected → report it, then run the segmentation extension only if RQ2/RQ3 results justify it.
