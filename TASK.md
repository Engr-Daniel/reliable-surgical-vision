# TASK.md — Active Research Tasks

This file is the concise execution queue. Keep completed work in the Research Log rather than allowing this file to become a historical archive.

## Phase 0 — Research Foundation

### P0.1 Toumai architecture reconnaissance — COMPLETE
- [x] Identify primary Toumai system/technical publications.
- [x] Map surgeon console, patient cart, vision platform, communications, and safety mechanisms.
- [x] Separate independent/regulatory evidence from manufacturer claims.
- [x] Extract reported latency, bandwidth, jitter, packet-loss, fail-safe, and video-processing information.
- [x] Document unknown or proprietary components.
- [x] Produce reproducible search/screening protocol and claim-level evidence audit.

**Milestone:** `v0.0.1 — Toumai Architecture Reconnaissance`

**Next:** P0.2 — Surgical computer-vision landscape.

### P0.2 Surgical computer-vision landscape
- [ ] Map major tasks: phase recognition, instrument detection/segmentation, anatomy recognition, semantic segmentation, action recognition, and related tasks.
- [ ] Identify representative baselines and benchmark practices.

### P0.3 Dataset reconnaissance
- [ ] Map candidate public datasets.
- [ ] Record procedure, modality, annotations, task suitability, licence, access restrictions, and dataset size.
- [ ] Identify datasets appropriate for controlled corruption/shift experiments.

### P0.4 Distribution-shift literature
- [ ] Review surgical-CV domain shift, domain generalisation, robustness, corruption, and OOD literature.
- [ ] Record shift definitions and evaluation protocols.

### P0.5 Reliable-inference literature
- [ ] Review calibration, uncertainty quantification, OOD detection, selective prediction, and conformal prediction in surgical/medical vision.
- [ ] Record reliability metrics and assumptions.

### P0.6 Telesurgery/network literature
- [ ] Map latency, jitter, packet loss, bandwidth, compression, adaptive bitrate, frame loss, and redundancy literature.
- [ ] Identify work connecting network conditions to downstream visual inference.

### P0.7 Intersection analysis
- [ ] Build literature evidence matrix.
- [ ] Identify well-studied intersections.
- [ ] Identify under-studied intersections.
- [ ] Stress-test Track A–C novelty.
- [ ] Update research questions before experimental commitments.

## Next milestone

**M0 — Evidence-backed Research Map**

Exit criteria:
- literature map populated;
- Toumai architecture note completed;
- dataset shortlist completed;
- Track A–C questions revised from evidence;
- no novelty claim remains unsupported.
