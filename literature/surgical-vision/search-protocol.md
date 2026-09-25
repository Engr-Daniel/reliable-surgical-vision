# P0.2 Search and Review Protocol

- **Task:** P0.2 — Surgical Computer-Vision Landscape Reconnaissance
- **Search/final audit date:** 2026-09-25
- **Evidence cutoff:** 2026-09-25
- **Type:** focused field reconnaissance with reproducible search and screening; not claimed as a PRISMA systematic review.

## Objective
Map the surgical-CV field relevant to robot-assisted/telerobotic surgery: task definitions, temporal structure, representative datasets, model families, metrics, benchmark practice, deployment proximity, and suitability for later reliability-under-shift work.

## Search surfaces
PubMed/PubMed Central; Medical Image Analysis/ScienceDirect; Springer/MICCAI; IEEE-indexed literature; AAAI; ACM; arXiv for influential non-replaced preprints; MICCAI EndoVis/Grand Challenge; official dataset/project pages.

## Representative query families
- `"surgical computer vision" review workflow instrument anatomy segmentation`
- `"surgical workflow analysis" phase recognition review`
- `"EndoNet" Cholec80`; `"TeCNO"`; `"Trans-SVNet"`; `"LoViT"`
- `"AutoLaparo"`; `"HeiChole"`; `"PhaKIR"`
- `"JIGSAWS"`; `"CholecT50" Rendezvous`; `"ESAD"`; `"SAR-RARP50"`
- `"EndoVis 2017" instrument segmentation`; `"EndoVis 2018" scene segmentation`
- `"ROBUST-MIS"`; `"CaDIS"`; `"CholecSeg8k"`
- `"Endoscapes"`; `"CholecInstanceSeg"`; `"SurgicalSAM"`
- `"SurgVLP"`; `"SurgVU"`
- `"CATARACTS"`; `"Metrics Matter in Surgical Phase Recognition"`; `"BIAS"`

## Inclusion
Retain sources that define a major surgical-CV task, introduce a representative dataset/benchmark, represent an influential model family, document benchmark methodology, provide multicentre/generalisation evidence, or map the field through a strong review.

## Exclusion/defer
Non-surgical imaging; pure robot control; pure networking (P0.6); comprehensive shift work (P0.4); calibration/OOD/conformal work (P0.5); duplicate preprints; unstable secondary summaries.

## Screening accounting
Final audit set: **45 records/categories** — **33 retained**, **12 excluded/deferred**. This is not a count of all search-engine hits.

## Synthesis rules
1. Do not compare metrics across different datasets/protocols as if directly comparable.
2. Preserve framewise vs clip/video and online/causal vs offline formulation.
3. Keep presence, detection, keypoints, semantic segmentation and instance segmentation distinct.
4. Keep phase/step/action/gesture/triplet tasks distinct.
5. Treat FPS as hardware/protocol dependent.
6. Preserve human vs porcine/ex-vivo vs training/simulation domains.
7. Do not equate benchmark performance with clinical safety/readiness.
8. Do not make final task/dataset/novelty choices before P0.3–P0.7.

## Reproducibility
Re-run query families, resolve sources by DOI/URL, apply the screening rules, compare with `source-screening-log.csv`, and re-extract the task/model/dataset relationships before publication.
