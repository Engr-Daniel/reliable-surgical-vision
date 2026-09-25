# P0.3 Dataset Reconnaissance Protocol

## Identity
- **Programme:** Reliable Surgical Vision
- **Phase:** Phase 0 — Research Foundation
- **Task:** P0.3 — Dataset Reconnaissance
- **Audit date:** 2026-09-25
- **Evidence cutoff:** 2026-09-25
- **Type:** focused dataset feasibility and provenance audit

## Objective
Determine which surgical-video datasets can credibly support later experiments on visual, temporal and network-induced distribution shift and reliable inference.

P0.3 is not a popularity survey. A dataset is useful only if its provenance, access, split integrity, annotation structure and technical feasibility are understood.

## Candidate discovery
Candidates were seeded from P0.2 and then re-checked against:
- official dataset/project pages;
- canonical repositories;
- peer-reviewed dataset/benchmark papers;
- official challenge pages;
- institutional data repositories;
- current issue trackers only when they affect present-day access feasibility.

## Research questions
1. Which datasets support the candidate temporal/spatial surgical-CV tasks?
2. What are their access, licence, redistribution and commercial-use constraints?
3. Which datasets share source videos or derived frames?
4. Are splits procedure/patient/site safe, and what leakage risks exist?
5. What annotation coverage and ground-truth limitations matter?
6. Which datasets support controlled visual corruption and temporal/network degradation?
7. What storage/download/compute constraints affect immediate feasibility?
8. Which datasets remain on the working shortlist, and why?

## Eligibility
Retain candidates that contribute at least one of:
- human surgical video;
- robot-assisted surgical video;
- established surgical-CV benchmark;
- dense spatial annotation;
- full temporal workflow annotation;
- multicentre/domain-shift structure;
- explicit robustness benchmark;
- directly relevant robotic training data useful as a secondary domain.

## Evidence rules
1. **Official access terms override assumptions from papers or mirrors.**
2. **Article licence ≠ dataset licence.**
3. **Code licence ≠ dataset licence.**
4. **A dataset name ≠ an independent patient/video domain.**
5. Derived datasets are traced back to source video IDs where documented.
6. Random frame splitting is unacceptable for later experiments unless the source benchmark explicitly defines it and leakage is understood.
7. Full-video availability is required for high-fidelity frame-loss/jitter/temporal-degradation experiments.
8. Sparse-frame datasets remain useful for visual corruption but cannot automatically support network-timing experiments.
9. Controlled-access data are still feasible, but access and redistribution obligations must be recorded.
10. Current download failures are treated as operational evidence, not proof that a dataset is permanently unavailable.

## Search/query families
Representative queries included:
- `"Cholec80" official license request 25 fps`
- `"CholecT50" 45 Cholec80 5 Cholec120 license`
- `"CholecSeg8k" 8080 17 Cholec80`
- `"CholecInstanceSeg" source Cholec80 CholecT50 CholecSeg8k`
- `"Endoscapes2023" official splits license PhysioNet`
- `"PhaKIR" three centres controlled access CC BY-NC-SA`
- `"HeiChole" OPARA three centres license`
- `"MultiBypass140" official split license download`
- `"MultiBypass140" multibypass03 corrupted`
- `"AutoLaparo" request form license 25 fps`
- `"SAR-RARP50" UCL train test CC BY-NC-SA`
- `"ESAD" Grand Challenge dataset`
- `"JIGSAWS" official access academic research`
- `"ROBUST-MIS" 10040 30 procedures Synapse`
- `"CaDIS" official split download`
- `"CATARACTS" official data commercial use`
- `"EndoVis 2017" official challenge data`
- `"SurgVU" official dataset license 840 hours`

## Screening accounting
- **18 dataset candidates retained for detailed feasibility audit**
- **36 evidence sources retained**
- **8 categories excluded/deferred**
This is a targeted candidate audit, not an exhaustive catalogue of every surgical dataset.

## Update requirement
Before experiments begin:
- re-check access URLs and licence terms;
- hash/record the exact dataset version;
- preserve source-video IDs;
- verify split files;
- record any dataset-provider updates after this audit date.
