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

## Update rule

Only add information here when it is expected to remain useful across many future research sessions. Put current actions in `TASK.md` and dated observations in `RESEARCH_LOG.md`.
