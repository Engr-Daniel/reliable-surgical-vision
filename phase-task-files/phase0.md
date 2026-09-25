# Phase 0 — Research Foundation

## Phase Objective

Phase 0 establishes the evidence base needed to define defensible, technically feasible, and reproducible research questions for reliable visual inference in robot-assisted and tele-robotic surgery.

The phase proceeds from system understanding to field mapping, datasets, distribution shift, reliable inference, networking, and finally intersection analysis.

The phase is complete only when the provisional research tracks have been stress-tested against the literature and revised into evidence-backed candidate research questions.

---

# Phase Status

| Task | Title | Status |
|---|---|---|
| P0.1 | Toumai Technical Literature & Architecture Reconnaissance | **COMPLETE — 2026-09-25** |
| P0.2 | Surgical Computer-Vision Landscape Reconnaissance | **READY TO START** |
| P0.3 | Dataset Reconnaissance | Not started |
| P0.4 | Distribution-Shift Literature Reconnaissance | Not started |
| P0.5 | Reliable-Inference Literature Reconnaissance | Not started |
| P0.6 | Telesurgery / Network Literature Reconnaissance | Not started |
| P0.7 | Intersection Analysis & Novelty Stress-Test | Not started |

---

# P0.1 — Toumai Technical Literature & Architecture Reconnaissance

## Status

`COMPLETE — 2026-09-25`

## 1. Purpose

Establish an evidence-backed technical understanding of the **Toumai robotic and tele-robotic surgical system**, with particular attention to the components relevant to reliable visual inference.

The task reconstructs the publicly documented system architecture from peer-reviewed literature, regulatory technical-review material, official technical documentation, clinical studies, and authoritative deployment reporting.

The objective is to determine:

> **What is technically known, what is reported but not independently established, what can reasonably be inferred, and what remains unknown about the Toumai tele-robotic architecture?**

## 2. Research Questions

### RQ1 — System Architecture
What are the principal components of the Toumai robotic surgical system?

Investigate surgeon console, patient-side robotic platform, robotic arms and instruments, vision system, imaging hardware, computing components, communication components, control architecture, and safety mechanisms.

### RQ2 — Visual Pipeline
How is surgical visual information acquired, processed, transmitted, and presented?

Investigate endoscopic imaging, image-processing pipeline, enhancement, smoke removal, vascular enhancement, imaging latency, and remote video transport.

### RQ3 — Teleoperation Pipeline
How are surgeon commands transmitted to the patient-side robotic system?

Investigate master–slave control, motion sensing, kinematic mapping, command transmission, actuation, feedback, response frequency, motion scaling, tremor filtering, and synchronization.

### RQ4 — Communications Architecture
What communication infrastructure has been reported for Toumai telesurgery?

Investigate dedicated fiber, broadband, 5G, satellite communication, hybrid architectures, redundant links, latency, RTT, jitter, packet loss, bandwidth, QoS, and failover behaviour.

### RQ5 — Reliability and Safety
How does the system respond to degraded or interrupted communication?

Investigate standby behaviour, fail-safe mechanisms, communication-loss detection, command interruption, redundant links, bedside support, local takeover, conversion procedures, recovery mechanisms, and publicly documented thresholds.

### RQ6 — Relevance to Reliable Visual Inference
Which parts of the architecture could influence the reliability of downstream computer-vision inference?

Candidate pathways include:

`Network degradation → video degradation → input distribution shift → model reliability degradation`

and:

`Imaging conditions / platform processing → visual distribution shift → uncertainty → prediction / abstention`

These relationships are hypotheses, not assumed Toumai behaviour.

## 3. P0.1 Evidence Standard

Sources were prioritised as:

1. peer-reviewed primary research;
2. regulatory technical-review material;
3. official technical documentation;
4. peer-reviewed evidence synthesis;
5. manufacturer documentation;
6. authoritative institutional/deployment reporting;
7. secondary reporting where primary evidence was unavailable.

Claims were classified as independently documented, regulatory technical-review evidence, manufacturer-reported, institution/secondary reported, inferred, or unknown.

## 4. P0.1 Work Packages

- **WP1 — Literature Discovery:** identify Toumai-specific technical and clinical literature.
- **WP2 — Literature Screening:** screen for architecture, imaging, control, networking, safety, reliability, and deployment relevance.
- **WP3 — Technical Evidence Extraction:** extract claims, reported values, evidence class, context, and limitations.
- **WP4 — Architecture Reconstruction:** reconstruct the documented system architecture.
- **WP5 — Reliability Analysis:** map documented network, safety, fallback, and degradation pathways.
- **WP6 — Research-Relevance Mapping:** identify interfaces relevant to later reliable-vision research without asserting novelty.

## 5. P0.1 Final Artifacts

### Architecture
- `docs/architecture/toumai-system-architecture.md`
- `docs/architecture/toumai-architecture.svg`
- `docs/architecture/toumai-architecture.png`

### Toumai Evidence Base
- `literature/toumai/search-protocol.md`
- `literature/toumai/source-screening-log.csv`
- `literature/toumai/toumai-literature-map.csv`
- `literature/toumai/toumai-network-metrics.csv`
- `literature/toumai/toumai-evidence-table.md`
- `literature/toumai/source-audit.md`
- `literature/toumai/source-index.md`
- `literature/toumai/open-technical-questions.md`
- `literature/toumai/references.bib`

### Programme Updates
- `literature/literature-map.csv`
- `literature/references.bib`
- `P0.1_COMPLETION_REPORT.md`
- `TASK.md`
- `RESEARCH_LOG.md`
- `MEMORY.md`

## 6. P0.1 Exit Criteria

- [x] Toumai-specific literature systematically identified.
- [x] Relevant sources screened.
- [x] Technical claims extracted.
- [x] Evidence classifications assigned.
- [x] System architecture reconstructed.
- [x] Visual pipeline documented.
- [x] Teleoperation pipeline documented.
- [x] Communications architecture documented where evidence permits.
- [x] Reliability and safety mechanisms mapped.
- [x] Quantitative network evidence extracted where public.
- [x] Unknown technical details explicitly recorded.
- [x] Reliable-visual-inference relevance analysed without unsupported novelty claims.
- [x] Required reproducibility artifacts produced.
- [x] Programme records updated.

### P0.1 Milestone

**`v0.0.1 — Toumai Architecture Reconnaissance`**

---

# P0.2 — Surgical Computer-Vision Landscape Reconnaissance

## Status

`READY TO START`

## 1. Purpose

Establish a structured, evidence-backed map of the **surgical computer-vision field** most relevant to robot-assisted and tele-robotic surgery.

P0.2 will determine:

- what major surgical-CV tasks exist;
- how those tasks are defined;
- which input modalities and temporal granularities they use;
- what model families and baselines are commonly used;
- what datasets and benchmarks are associated with the tasks;
- which evaluation metrics and validation practices dominate the field;
- how close existing work is to real-time robotic or telesurgical deployment;
- which task families are most suitable for later reliability-under-shift research.

The purpose is **field reconnaissance**, not yet a dataset-selection study, distribution-shift review, or reliability-method review.

P0.2 should answer:

> **What does the current surgical computer-vision research landscape look like, and which task families provide credible foundations for later study of reliability under distribution shift?**

## 2. Scope Boundaries

### In scope
- surgical phase/workflow recognition;
- surgical action/activity recognition;
- gesture recognition where relevant;
- instrument detection;
- instrument segmentation;
- instrument tracking;
- anatomy/structure detection;
- anatomy/structure segmentation;
- semantic segmentation;
- scene understanding;
- bleeding/adverse-event or critical-event detection where relevant;
- temporal surgical-video modelling;
- image-based and video-based benchmarks;
- representative baseline and current model families;
- evaluation metrics and benchmark practices;
- real-time/deployment considerations reported in the literature.

### Out of scope for P0.2
These belong primarily to later tasks:

- exhaustive dataset licensing/access audit → **P0.3**;
- comprehensive domain shift/domain generalisation/corruption literature → **P0.4**;
- calibration/OOD/conformal/selective prediction literature → **P0.5**;
- detailed telesurgery communication/network literature → **P0.6**;
- final novelty claims and Track A–C selection → **P0.7**.

P0.2 may record these topics when encountered, but should not become their full review.

## 3. Research Questions

### RQ1 — Task Taxonomy
What are the major computer-vision tasks used in surgical video and robot-assisted surgery?

For each task, determine:
- input;
- prediction target;
- spatial/temporal granularity;
- clinical/workflow purpose;
- common annotation type;
- representative datasets;
- representative evaluation metrics.

### RQ2 — Input and Temporal Structure
How are surgical-CV problems formulated?

Investigate:
- single-frame classification;
- framewise segmentation;
- object detection;
- temporal sequence modelling;
- clip-level recognition;
- full-video modelling;
- multi-view/stereo inputs;
- multimodal inputs where relevant;
- real-time vs offline inference.

Determine which tasks inherently depend on temporal continuity and which can be evaluated frame-by-frame.

### RQ3 — Model Families and Baselines
What model families are representative of the field?

Map:
- CNN approaches;
- encoder–decoder segmentation networks;
- object detectors;
- recurrent temporal models;
- temporal convolutional models;
- transformer architectures;
- vision transformers;
- video transformers;
- CNN–transformer hybrids;
- foundation/promptable segmentation methods where established;
- multimodal systems where relevant.

The goal is not an exhaustive leaderboard. It is to identify credible representative baselines and benchmark conventions.

### RQ4 — Benchmark and Dataset Relationships
Which datasets are repeatedly associated with each task?

Record at reconnaissance level:
- dataset name;
- procedure type;
- supported task;
- annotation type;
- video/still-image modality;
- single-centre/multi-centre status where clearly documented;
- benchmark role.

Detailed licensing, access restrictions, dataset size auditing, and final selection belong to P0.3.

### RQ5 — Evaluation Metrics
What metrics are standard for each task?

Examples:

**Classification/recognition**
- accuracy;
- precision;
- recall;
- F1;
- AUROC;
- average precision;
- balanced accuracy.

**Detection**
- mAP;
- AP at IoU thresholds;
- precision/recall.

**Segmentation**
- Dice;
- IoU/Jaccard;
- mean IoU;
- boundary metrics where used.

**Temporal/workflow**
- framewise accuracy;
- F1;
- edit score;
- segmental F1;
- temporal consistency metrics.

Metric definitions should be preserved where conventions differ.

### RQ6 — Benchmark Practice and Reproducibility
How are surgical-CV studies commonly evaluated?

Investigate:
- patient/video-level splits;
- random vs predefined splits;
- cross-validation;
- train/validation/test conventions;
- held-out subjects/sites;
- seed reporting;
- code/checkpoint availability;
- preprocessing;
- augmentation;
- throughput/latency reporting;
- external validation.

### RQ7 — Deployment Proximity
Which task families are closest to practical robot-assisted or telesurgical use?

Assess evidence for:
- online inference;
- real-time processing;
- robotic integration;
- operating-room deployment;
- intraoperative visual overlays;
- surgeon-facing assistance;
- human-in-the-loop use.

Benchmark performance must not be equated with clinical readiness.

### RQ8 — Suitability for Later Reliability Research
Which task families are technically suitable for later study of:
- visual corruption;
- distribution shift;
- OOD behaviour;
- calibration;
- uncertainty;
- selective prediction;
- conformal prediction;
- network-induced video degradation?

The output should be a **task suitability assessment**, not a novelty claim.

## 4. Evidence Strategy

P0.2 should prioritise:

1. peer-reviewed benchmark and dataset papers;
2. peer-reviewed method papers with strong benchmark relevance;
3. high-quality systematic/scoping reviews;
4. challenge/workshop benchmark papers;
5. official dataset/challenge documentation;
6. authoritative project repositories where needed to verify benchmark practice.

Search surfaces may include:
- PubMed / PubMed Central;
- IEEE Xplore;
- SpringerLink;
- ScienceDirect;
- Wiley;
- ACM Digital Library;
- arXiv for influential work without peer-reviewed versions;
- MICCAI / EndoVis challenge records;
- CVPR / ICCV / ECCV;
- official dataset and benchmark pages.

Primary benchmark/dataset papers should be preferred over secondary summaries.

## 5. Search and Reproducibility Requirements

A dedicated protocol must document:
- search date;
- evidence cutoff;
- databases/search surfaces;
- exact query families;
- inclusion criteria;
- exclusion criteria;
- deduplication logic;
- screening method;
- evidence-classification method;
- extraction fields;
- limitations.

P0.2 should not claim PRISMA-level systematic-review completeness unless the methodology actually meets that standard.

## 6. Work Packages

### WP1 — Field Discovery
Identify major task families, foundational reviews, recent reviews, challenge ecosystems, and canonical terminology.

**Output:** candidate literature set and provisional task taxonomy.

### WP2 — Task Taxonomy Validation
For each task family, confirm:
- task definition;
- input/output structure;
- annotation type;
- representative datasets;
- standard metrics;
- representative model families.

**Output:** validated surgical-CV task taxonomy.

### WP3 — Model and Baseline Mapping
Identify representative modelling approaches for each task.

The objective is to answer:

> **What would a credible baseline look like if this task were later selected for reliability experiments?**

Avoid building an exhaustive leaderboard.

**Output:** model/baseline map.

### WP4 — Benchmark Practice Mapping
Extract:
- split strategy;
- metric conventions;
- validation design;
- code availability;
- real-time reporting;
- external/generalisation testing where present.

**Output:** benchmark-practice report.

### WP5 — Task–Dataset Crosswalk
Map tasks to commonly used datasets without performing the full P0.3 dataset audit.

**Output:** task–dataset crosswalk.

### WP6 — Reliability-Relevance Assessment
Assess each task family using criteria such as:
- public-data availability;
- ground-truth clarity;
- computational feasibility;
- suitability for controlled corruption;
- suitability for temporal/network degradation;
- meaningful uncertainty/abstention formulation;
- relevance to robotic/telesurgical workflows;
- evaluation maturity.

Do **not** make final paper selections in P0.2.

**Output:** reliability-relevance matrix.

### WP7 — Evidence Synthesis
Produce a narrative field map explaining:
- how the field is structured;
- which tasks dominate;
- which benchmarks are mature;
- what evaluation practices are common;
- where deployment-facing research exists;
- what questions must be carried into P0.3–P0.7.

**Output:** surgical-CV landscape report.

## 7. Required Artifacts

### A1 — Search Protocol
`literature/surgical-vision/search-protocol.md`

### A2 — Source Screening Log
`literature/surgical-vision/source-screening-log.csv`

Recommended fields:
- record ID;
- title;
- year;
- source;
- task family;
- decision;
- reason;
- DOI/URL;
- notes.

### A3 — Surgical-CV Literature Map
`literature/surgical-vision/surgical-cv-literature-map.csv`

Recommended fields:
- source ID;
- title;
- year;
- venue;
- task;
- modality;
- procedure;
- dataset;
- model family;
- metric;
- real-time status;
- code availability;
- benchmark role;
- relevance;
- notes;
- DOI/URL.

### A4 — Surgical-CV Landscape Report
`literature/surgical-vision/surgical-cv-landscape.md`

Must cover:
- field overview;
- task taxonomy;
- input/output formulations;
- representative model families;
- benchmark ecosystems;
- evaluation practices;
- real-time/deployment proximity;
- methodological limitations;
- implications for later reliable-inference work.

### A5 — Task Taxonomy
`literature/surgical-vision/task-taxonomy.md`

Recommended structure:

| Task | Input | Output | Temporal? | Annotation | Typical metrics | Representative datasets | Deployment relevance |
|---|---|---|---|---|---|---|---|

### A6 — Model / Baseline Map
`literature/surgical-vision/model-baseline-map.csv`

Recommended fields:
- task;
- model family;
- representative model;
- year;
- input type;
- temporal modelling;
- dataset;
- metric;
- code/checkpoint availability;
- baseline rationale;
- source.

### A7 — Task–Dataset Crosswalk
`literature/surgical-vision/task-dataset-crosswalk.csv`

Recommended fields:
- dataset;
- procedure;
- modality;
- supported tasks;
- annotation type;
- benchmark role;
- notes;
- source.

### A8 — Benchmark and Metrics Guide
`literature/surgical-vision/benchmark-practices.md`

Must document:
- common split designs;
- task-specific metrics;
- temporal evaluation conventions;
- reproducibility practices;
- real-time reporting;
- external validation;
- common methodological pitfalls.

### A9 — Reliability-Relevance Matrix
`literature/surgical-vision/reliability-relevance-matrix.csv`

Recommended fields:
- task;
- public-data availability;
- ground-truth clarity;
- framewise suitability;
- temporal dependence;
- corruption-test suitability;
- network-degradation suitability;
- uncertainty suitability;
- abstention suitability;
- conformal suitability;
- likely compute burden;
- clinical/telesurgical relevance;
- evidence notes.

### A10 — Open Questions
`literature/surgical-vision/open-questions.md`

Record unresolved questions that should be carried to P0.3–P0.7.

### A11 — References
`literature/surgical-vision/references.bib`

Relevant entries should also be merged into:

`literature/references.bib`

### A12 — Global Literature Map Update
Update:

`literature/literature-map.csv`

with retained P0.2 sources.

### A13 — Research Log Update
Update:

`RESEARCH_LOG.md`

Record search date, screening counts, major field-structure findings, methodological decisions, unresolved questions, and implications for later Phase 0 tasks.

### A14 — Task Tracker Update
Update:

`TASK.md`

Mark P0.2 complete only when its exit criteria are satisfied.

### A15 — P0.2 Completion Report
`P0.2_COMPLETION_REPORT.md`

Must document:
- scope;
- completion standard;
- core findings;
- artifacts;
- exit-criteria audit;
- scientific boundary;
- next task.

## 8. Quality Requirements

P0.2 is not complete merely because papers have been collected.

### Taxonomic clarity
Distinguish:
- classification vs detection;
- detection vs segmentation;
- framewise vs temporal prediction;
- workflow/phase vs action/gesture;
- anatomy vs instrument segmentation.

### Evidence traceability
Claims about benchmark dominance, model families, metrics, and dataset use must be traceable.

### Benchmark fidelity
Do not compare metrics across different datasets/tasks as if directly comparable.

### Reproducibility
Another researcher should be able to reproduce the search, screening, taxonomy, literature map, and baseline-selection logic.

### Scope discipline
Do not prematurely turn P0.2 into P0.3–P0.7.

### Clinical caution
Benchmark performance is not evidence of clinical safety or deployment readiness.

### Negative evidence
Weak data availability, poor annotation quality, limited reproducibility, or lack of deployment evidence should be recorded explicitly.

## 9. P0.2 Exit Criteria

P0.2 is complete when:

- [ ] major surgical-CV task families have been identified and clearly defined;
- [ ] foundational and representative recent literature has been screened;
- [ ] a reproducible P0.2 search protocol has been documented;
- [ ] source-screening decisions have been recorded;
- [ ] representative datasets have been mapped to tasks at reconnaissance level;
- [ ] representative model/baseline families have been mapped;
- [ ] standard task-specific evaluation metrics have been documented;
- [ ] common benchmark/evaluation practices have been documented;
- [ ] real-time/deployment-facing evidence has been identified where available;
- [ ] task suitability for later reliability research has been assessed without making final paper selections;
- [ ] unresolved questions for P0.3–P0.7 have been recorded;
- [ ] `literature/references.bib` has been updated;
- [ ] `literature/literature-map.csv` has been updated;
- [ ] `RESEARCH_LOG.md` has been updated;
- [ ] `TASK.md` has been updated;
- [ ] all required P0.2 artifacts have been produced;
- [ ] `P0.2_COMPLETION_REPORT.md` has been produced.

## 10. P0.2 Completion Milestone

Successful completion of P0.2 will establish the surgical-computer-vision field map needed for dataset and reliability-method decisions.

Suggested repository milestone:

**`v0.0.2 — Surgical Computer-Vision Landscape`**

The next planned task is:

**P0.3 — Dataset Reconnaissance**

P0.3 should begin only after the P0.2 landscape artifacts have been reviewed for completeness and evidence quality.

---

# Remaining Phase 0 Tasks

## P0.3 — Dataset Reconnaissance

Identify and rigorously assess candidate datasets for later experimental work, including access, licensing, annotations, domain/site structure, task suitability, and distribution-shift potential.

## P0.4 — Distribution-Shift Literature Reconnaissance

Map surgical-CV robustness, domain shift, domain generalisation, corruption, and OOD evaluation literature.

## P0.5 — Reliable-Inference Literature Reconnaissance

Map uncertainty, calibration, OOD detection, selective prediction, conformal prediction, and abstention in surgical/medical visual inference.

## P0.6 — Telesurgery / Network Literature Reconnaissance

Map communication and video-transport factors relevant to remote surgical systems, including latency, jitter, packet loss, bandwidth, compression, temporal/frame degradation, redundancy, failover, and links to downstream vision.

## P0.7 — Intersection Analysis & Novelty Stress-Test

Integrate P0.1–P0.6 and determine which research questions remain defensible.

Expected outputs include:
- global evidence matrix;
- task × dataset × shift × reliability-method × network intersection map;
- well-studied vs under-studied combinations;
- novelty stress-test for Tracks A–C;
- revised research questions;
- decision on whether tracks remain separate, merge, split, or are discontinued.

---

# Phase 0 Completion Gate

Phase 0 is complete when:

- [x] Toumai architecture reconnaissance is complete;
- [ ] surgical-CV landscape is mapped;
- [ ] candidate datasets are mapped and feasibility-audited;
- [ ] distribution-shift literature is mapped;
- [ ] reliable-inference literature is mapped;
- [ ] telesurgery/network literature is mapped;
- [ ] the intersection evidence matrix is complete;
- [ ] Track A–C novelty has been stress-tested;
- [ ] candidate research questions have been revised from evidence;
- [ ] unsupported novelty claims have been removed;
- [ ] the next experimental/research phase is justified by the evidence.

## Phase 0 Programme Milestone

**M0 — Evidence-Backed Research Map**
