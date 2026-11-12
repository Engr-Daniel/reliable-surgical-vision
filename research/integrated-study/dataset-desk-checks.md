# Dataset Desk Checks (P1.5)

**Date:** 2026-11-12. Desk checks only; no data downloaded. Terms must be re-verified at the moment of download (P0.3 rule).

| Check | Cholec80 (DS01) | PhaKIR (DS06) | AutoLaparo (DS09) |
|---|---|---|---|
| Role | Development + primary test | External natural-shift replication (descriptive) | Optional cross-procedure replication |
| Access | CAMMA request form | Controlled Zenodo access by request | Request form |
| Licence | CC BY-NC-SA 4.0 | CC BY-NC-SA | CC BY-NC-SA 4.0 |
| Full video, native fps | Yes, 25 fps | Yes, 25 fps, 1920×1080 | Yes, 25 fps, 1920×1080 |
| Phase taxonomy | 7 phases | **Same 7 phases** as Cholec80 (preparation, Calot triangle dissection, clipping & cutting, gallbladder dissection, gallbladder packaging, cleaning & coagulation, gallbladder retraction). Verified from the PhaKIR challenge report | 7 hysterectomy phases; **not** mappable. Use its own phase model and split |
| Size | 80 videos | **8 public videos** from 3 centres (the challenge used 13; extras hidden) | 21 videos (10/4/7 split) |
| Overlap with Cholec80 | — | Independent German multicentre collection; no shared source videos | Different procedure and hospital |
| Re-encoding / derived video | Permitted for non-commercial research under CC terms; store privately; do not redistribute | Same, plus controlled-access handling obligations | Same |
| Split | Pinned: 1–32 train, 33–40 val/cal, 41–80 test | All 8 as external test; report per centre | Published 10/4/7 |
| Status | **Pass** (request at Phase 2 start) | **Pass**, taxonomy compatible; n = 8 makes it descriptive only | **Pass, gated:** only if RQ1 is completed on Cholec80 |

## Decisions
1. PhaKIR's identical phase labels allow the Cholec80-trained models to be evaluated directly, with no label mapping. This is the external natural-shift arm (H2c and descriptive RQ1 replication).
2. HeiChole (~156 GB, 3 centres) is the fallback if PhaKIR access fails. It is **not** needed while PhaKIR is available.
3. Derived artefacts (archived received streams, decoded-frame features) inherit the source licences. They stay in private storage, and only aggregate results and code are published. **Nothing derived from the datasets is committed to this repository.**

## Open items
- Confirm Cholec80 request-form terms permit storing re-encoded derivatives (expected under CC BY-NC-SA).
- Confirm PhaKIR controlled-access conditions on derived data.
- Read the full text of the deferred MICCAI 2026 titles (P1.1 EX18) before Phase 2.
