# MEMORY.md — Persistent Research Context

This file preserves durable project context for researchers and AI-assisted research sessions. It should contain stable decisions and validated context—not transient task lists.

## Project identity

**Repository:** `reliable-surgical-vision`

**Programme:** Reliable Visual Inference Under Distribution Shift for Robot-Assisted and Tele-Robotic Surgery.

## Umbrella question

How can computer-vision systems used in robot-assisted and tele-robotic surgery maintain reliable inference—or safely abstain—when visual, clinical, hardware, and communication conditions differ from those encountered during development?

## Current tracks

### Track A — Compound Shift
Study performance and reliability degradation under individual and compound visual/network-induced shifts.

### Track B — Selective Inference
Study uncertainty, calibration, conformal prediction, selective prediction, and abstention under surgical distribution shift.

### Track C — Network-Aware Inference
Study reliability estimation using both visual evidence and network/system telemetry.

## Key conceptual hypothesis

Network degradation can alter the visual input distribution through compression, frame loss, resolution adaptation, corruption, temporal irregularity, or related mechanisms. Therefore, network state may be relevant to downstream computer-vision reliability.

This is a hypothesis to investigate, not an established project conclusion.

## Research status

The programme is in **Phase 0: Research Foundation**. No paper title, novelty claim, dataset choice, model architecture, or experimental conclusion is final.

## Durable decisions

- One repository contains all three tracks.
- `main` is the canonical research record.
- Tracks are directories rather than long-lived branches.
- Feature/experiment branches are created only for bounded implementation work.
- Literature and dataset reconnaissance precede major experimentation.
- Research tracks may merge, split, change direction, or be abandoned based on evidence.
- Reproducibility, provenance, and negative-result reporting are first-class requirements.

- **P0.2 Surgical Computer-Vision Landscape Reconnaissance completed (2026-09-25).**
- Keep workflow/phase, action/gesture/triplets, detection/keypoints, semantic/instance segmentation, anatomy/scene and skill as distinct task structures.
- Workflow recognition is intrinsically temporal; segmentation/detection provide complementary spatial failure modes.
- Surgical-CV public data are concentrated in laparoscopic cholecystectomy; dataset provenance/overlap must be audited before cross-dataset claims.
- Multicentre HeiChole and PhaKIR show that strong single-centre/i.i.d. scores do not imply cross-centre generalisation.
- Metric implementation/protocol details must be pinned; identical metric names do not guarantee comparable results.
- Phase/workflow recognition and instrument/anatomy segmentation/detection are candidate families only; final selection remains gated by P0.3–P0.7.
- Every completed Phase 0 task should include an `rq-answer-matrix.md`.

## Update rule

Only add information here when it is expected to remain useful across many future research sessions. Put current actions in `TASK.md` and dated observations in `RESEARCH_LOG.md`.
