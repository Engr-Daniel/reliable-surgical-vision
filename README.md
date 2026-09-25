# Reliable Surgical Vision

**Reliable Visual Inference Under Distribution Shift for Robot-Assisted and Tele-Robotic Surgery**

This repository is a research programme investigating how computer-vision systems used in robot-assisted and tele-robotic surgery can maintain reliable inference—or safely abstain—when visual, clinical, hardware, and communication conditions differ from those encountered during development.

## Research programme

The repository currently contains three provisional research tracks:

- **Track A — Compound Shift:** quantify how individual and compound visual/network-induced shifts affect surgical computer-vision performance and reliability.
- **Track B — Selective Inference:** investigate uncertainty quantification, calibration, conformal prediction, and selective prediction under surgical distribution shift.
- **Track C — Network-Aware Inference:** investigate whether visual evidence and network telemetry can jointly identify unreliable inference in telesurgical settings.

These are research tracks, not predetermined publications. Tracks may be refined, combined, divided, or discontinued as evidence accumulates.

## Core research question

> How can computer-vision systems used in robot-assisted and tele-robotic surgery maintain reliable inference—or safely abstain—when deployment conditions differ from those encountered during development?

## Current research status

**Phase 0 — Research Foundation**

- P0.1 Toumai architecture reconnaissance — **complete** (`v0.0.1`)
- P0.2 Surgical computer-vision landscape — **complete** (`v0.0.2`)
- P0.3 Dataset reconnaissance — **complete** (`v0.0.3`)
- P0.4 Distribution-shift literature reconnaissance — **complete** (`v0.0.4`)
- P0.5 Reliable-inference literature reconnaissance — **complete**
- P0.6 Telesurgery / network literature reconnaissance — **next**

P0.5 narrows Track B substantially: surgical uncertainty, calibration, OOD/open-set recognition, abstention, conformal trajectory forecasting, and recent conformal failure monitoring already have direct precedents. The remaining question is reliability **under the programme's specific natural, visual and mechanistically grounded network/video shifts**, not generic uncertainty estimation.

## Research principles

1. Evidence before novelty claims.
2. Reproducibility by design.
3. Clear separation of observation, hypothesis, experiment, and conclusion.
4. Reliability evaluation beyond headline predictive performance.
5. Transparent reporting of negative and inconclusive results.
6. Safety-aware interpretation of medical-AI research.
7. Version-controlled experiments, configurations, results, and decisions.

See `EXECUTION_BRIEF.md`, `ROADMAP.md`, `AGENT.md`, `TASK.md`, and `MEMORY.md`.
