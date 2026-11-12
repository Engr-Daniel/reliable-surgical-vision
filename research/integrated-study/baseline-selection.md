# Baseline Model Selection (P1.7)

**Date:** 2026-11-12. Candidates were checked by cloning the official repositories, without running any code.

| Model | Repository / commit | Licence | Online / causal | Datasets supported | Decision |
|---|---|---|---|---|---|
| **TeCNO** (MICCAI 2020; SV09) | `tobiascz/TeCNO` @ `0c4313f` (2021-07-23) | **GPL-3.0** | Causal multi-stage TCN | Cholec80 | **Selected (M1, primary)** |
| **Surgformer** | `isyangshu/Surgformer` @ `5d57e46` (2025-08-28) | **CC BY-NC 4.0** | Online data strategy in code | Cholec80, AutoLaparo | **Selected (M2, replication)** |
| LoViT (SV11) | `MRUIL/LoViT` | none stated | Online | Cholec80, AutoLaparo | **Excluded:** README states full code is unavailable (patent/review); only features and weights are released |
| Trans-SVNet (SV10) | `xjgaocs/Trans-SVNet` | **no licence file** | — | Cholec80 | **Excluded:** no licence grants reuse rights |

## Rationale
- One TCN-based and one transformer-based online model, both with public code, causal inference and Cholec80 support (P0.2 SV09/SV11 lineage).
- M1 is primary because it is light enough to train cheaply. Its 5-seed TCN heads give the V0 `ens_disagree` feature.
- Evidence gating (IX03) is **absent** from both models, so failures are not masked by transition gating. If a gated variant is later added, it is an exploratory arm.

## Licensing consequences for this repository
- TeCNO is GPL-3.0. Its code is used as an **external, unmodified dependency** (pinned commit, installed at run time) and is **not vendored** into this repository. Any modified TeCNO code would have to be released under GPL-3.0.
- Surgformer is CC BY-NC 4.0: non-commercial use with attribution. It is likewise not vendored.
- **This repository currently has no LICENSE file.** Before implementation code is added in Phase 2, the author must choose a licence compatible with these dependencies. Recorded as an open decision; it is not made here.

## Reproduction targets (Phase 2 gate)
Each model must reproduce its published Cholec80 performance on the pinned split, within tolerance, before any impairment experiment. The tolerance is the video-level accuracy reported in the respective paper, with the metric implementation pinned per SV32.
