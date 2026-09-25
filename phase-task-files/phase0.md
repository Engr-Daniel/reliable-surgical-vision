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
| P0.2 | Surgical Computer-Vision Landscape Reconnaissance | **COMPLETE — 2026-09-25** |
| P0.3 | Dataset Reconnaissance | **COMPLETE — 2026-09-25** |
| P0.4 | Distribution-Shift Literature Reconnaissance | **COMPLETE — 2026-09-25** |
| P0.5 | Reliable-Inference Literature Reconnaissance | **READY TO START** |
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
- `literature/toumai/rq-answer-matrix.md`

### Programme Updates
- `literature/literature-map.csv`
- `literature/references.bib`
- `task-completion-report/P0.1_COMPLETION_REPORT.md`
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

`COMPLETE — 2026-09-25`

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
`task-completion-report/P0.2_COMPLETION_REPORT.md`

Must document:
- scope;
- completion standard;
- core findings;
- artifacts;
- exit-criteria audit;
- scientific boundary;
- next task.

### A16 — Research Question Answer Matrix
`literature/surgical-vision/rq-answer-matrix.md`

For every P0.2 research question, this file contains:
- a concise evidence-backed answer;
- supporting source IDs;
- links to detailed artifacts;
- remaining uncertainty;
- explicit separation of conclusion from hypothesis.

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

- [x] major surgical-CV task families have been identified and clearly defined;
- [x] foundational and representative recent literature has been screened;
- [x] a reproducible P0.2 search protocol has been documented;
- [x] source-screening decisions have been recorded;
- [x] representative datasets have been mapped to tasks at reconnaissance level;
- [x] representative model/baseline families have been mapped;
- [x] standard task-specific evaluation metrics have been documented;
- [x] common benchmark/evaluation practices have been documented;
- [x] real-time/deployment-facing evidence has been identified where available;
- [x] task suitability for later reliability research has been assessed without making final paper selections;
- [x] unresolved questions for P0.3–P0.7 have been recorded;
- [x] `literature/references.bib` has been updated;
- [x] `literature/literature-map.csv` has been updated;
- [x] `RESEARCH_LOG.md` has been updated;
- [x] `TASK.md` has been updated;
- [x] all required P0.2 artifacts have been produced;
- [x] `task-completion-report/P0.2_COMPLETION_REPORT.md` has been produced.

- [x] all P0.2 RQs have evidence-linked answers in `literature/surgical-vision/rq-answer-matrix.md`.

## 10. P0.2 Completion Milestone

P0.2 completed on **2026-09-25** after a final evidence audit.

Suggested repository milestone after commit/review:

**`v0.0.2 — Surgical Computer-Vision Landscape`**

The next active task is:

**P0.3 — Dataset Reconnaissance**

P0.3 should audit dataset access, licensing, provenance, source-video overlap, split integrity, domain/site structure and experimental feasibility before any final dataset selection.

---

# P0.3 — Dataset Reconnaissance

## Status

`COMPLETE — 2026-09-25`

## 1. Purpose

Identify and rigorously assess candidate surgical-video datasets for later experiments on **distribution shift, uncertainty, selective inference, conformal prediction, and network/temporal degradation**.

P0.3 is not a dataset popularity survey and does not make the final Phase 1 dataset choice.

It asks:

> **Which datasets can support scientifically valid, reproducible reliability experiments without hidden provenance leakage, access/licensing mistakes, or incompatible task assumptions?**

The task explicitly audits:

- access and current availability;
- dataset/data-use licence;
- redistribution/derivative constraints;
- procedure and modality;
- full-video vs frame-only release;
- annotation coverage;
- centre/site structure;
- procedure/video-level splits;
- source-video overlap and derived-dataset lineage;
- temporal/network-degradation suitability;
- visual-corruption suitability;
- storage/download/compute burden;
- working experimental role.

---

## 2. Scope Boundaries

### In scope

- candidate datasets identified during P0.2;
- human laparoscopic/endoscopic datasets;
- human robot-assisted surgery datasets;
- multicentre datasets;
- robustness/domain-gap datasets;
- robotic training datasets when they provide unique technical value;
- official challenge/test structures;
- access/licence/DUA status;
- provenance overlap;
- leakage risk;
- operational feasibility.

### Out of scope

- final synthetic-corruption taxonomy → **P0.4**;
- calibration/conformal/selective-prediction method choice → **P0.5**;
- exact network impairment emulator → **P0.6**;
- final task/dataset/paper selection → **P0.7**;
- downloading or redistributing restricted raw surgical video during Phase 0.

---

## 3. Research Questions

### RQ1 — Dataset Viability

Which public or controlled-access datasets can support the candidate surgical-CV tasks identified in P0.2?

Determine:

- procedure;
- modality;
- clinical vs training/porcine domain;
- task;
- scale;
- annotation type;
- raw/full video availability;
- centre structure.

### RQ2 — Access, Licence and Redistribution

For each candidate:

- where is the canonical access route?
- is registration/request approval required?
- what is the data licence?
- is commercial use restricted?
- may data or derived data be redistributed?
- is a DUA required?
- does the hosted data route impose stricter terms than the code/project repository?

**Article licences and code licences must not be substituted for dataset licences.**

### RQ3 — Provenance and Overlap

Which datasets:

- derive from the same source videos?
- share patient/procedure/video identities?
- contain re-extracted frames from the same surgery?
- combine annotations from earlier datasets?

The objective is to prevent false “external” evaluation caused by hidden source-video overlap.

### RQ4 — Split Integrity and Natural Domains

For each dataset:

- what is the official split?
- is the split procedure/video level?
- is centre/site metadata available?
- can centre, procedure or device define a natural shift?
- is patient/video overlap excluded?
- is the challenge test set public or hidden?

### RQ5 — Annotation Coverage and Ground Truth

Audit:

- phase/action annotation frequency;
- semantic/instance masks;
- bounding boxes;
- keypoints;
- expert review;
- multi-rater labels where available;
- sparse vs dense annotation;
- annotation quality limitations.

### RQ6 — Shift and Network/Temporal Suitability

Which datasets can support:

- visual corruptions;
- codec/re-encoding experiments;
- frame loss;
- duplicated frames;
- irregular sampling;
- temporal gaps;
- jitter-inspired scheduling;
- temporal-context truncation;
- natural cross-centre/procedure shift?

Full-video availability must be distinguished from frame-only releases.

### RQ7 — Operational Feasibility

What practical constraints affect use?

Audit:

- storage;
- download size;
- access friction;
- current broken links/archive issues;
- compute burden;
- annotation preparation;
- video extraction requirements.

### RQ8 — Working Shortlist

Which datasets should remain on the **working feasibility shortlist** for later Phase 0 tasks?

This is not a ranking and is not the final Phase 1 selection.

---

## 4. Evidence Strategy

Priority:

1. official dataset repositories/pages;
2. institutional data repositories;
3. peer-reviewed dataset/benchmark papers;
4. official challenge documentation;
5. current issue trackers where an issue directly affects dataset availability;
6. high-quality reviews only for metadata not exposed by the primary source.

A current access-status claim must not be based solely on an old paper if the live official data page contradicts it.

---

## 5. Work Packages

### WP1 — Candidate Registry

Seed candidates from P0.2 and confirm canonical identities.

**Output:** `dataset-registry.csv`

### WP2 — Access / Licence Audit

Verify current access routes, restrictions and data-use terms.

**Output:** `access-license-audit.csv`

### WP3 — Provenance / Overlap Audit

Trace datasets to their source procedures/videos and identify derived-data relationships.

**Output:** `provenance-overlap-map.md`

### WP4 — Split / Leakage Audit

Assess procedure-level split integrity, hidden tests and natural site/domain structure.

**Output:** `split-leakage-audit.csv`

### WP5 — Temporal / Network Suitability

Determine whether genuine sequence data exist and whether labels can remain synchronized after controlled temporal/video degradation.

**Output:** `temporal-network-suitability.csv`

### WP6 — Operational Feasibility

Record storage, access friction and currently broken/incomplete resources.

**Output:** `compute-access-feasibility.csv`

### WP7 — Decision Synthesis

Map each dataset to an experimental role without prematurely choosing the final experiment.

**Outputs:**
- `dataset-decision-matrix.csv`
- `dataset-shortlist.md`

### WP8 — RQ and Evidence Closure

Answer every P0.3 RQ and preserve unresolved questions for P0.4–P0.7.

**Outputs:**
- `rq-answer-matrix.md`
- `open-questions.md`

---

## 6. Required Artifacts

### A1 — Search Protocol
`datasets/search-protocol.md`

### A2 — Source Screening Log
`datasets/source-screening-log.csv`

### A3 — Dataset Registry
`datasets/dataset-registry.csv`

### A4 — Access and Licence Audit
`datasets/access-license-audit.csv`

### A5 — Provenance and Overlap Map
`datasets/provenance-overlap-map.md`

### A6 — Split and Leakage Audit
`datasets/split-leakage-audit.csv`

### A7 — Temporal / Network Suitability Map
`datasets/temporal-network-suitability.csv`

### A8 — Compute / Access Feasibility Map
`datasets/compute-access-feasibility.csv`

### A9 — Dataset Decision Matrix
`datasets/dataset-decision-matrix.csv`

### A10 — Working Dataset Shortlist
`datasets/dataset-shortlist.md`

### A11 — Research Question Answer Matrix
`datasets/rq-answer-matrix.md`

### A12 — Open Questions
`datasets/open-questions.md`

### A13 — Evidence Traceability
- `datasets/source-index.md`
- `datasets/source-audit.md`
- `datasets/references.bib`

### A14 — Programme Updates
- `literature/literature-map.csv`
- `literature/references.bib`
- `TASK.md`
- `RESEARCH_LOG.md`
- `MEMORY.md`
- `README.md`
- `task-completion-report/P0.3_COMPLETION_REPORT.md`

---

## 7. Quality Requirements

### Provenance before convenience
A convenient dataset must not be treated as external validation if it contains procedures used in training.

### Procedure-level integrity
Frames from the same source procedure must not cross train/calibration/test boundaries.

### Licence fidelity
Record the licence attached to the **data actually downloaded**, not just the paper or GitHub code.

### Access-state fidelity
Broken or pending download routes must be recorded as operational limitations.

### Domain fidelity
Human clinical, porcine, ex-vivo, simulation and training domains must remain explicitly separated.

### Temporal fidelity
Frame-only datasets cannot be used to claim realistic network/frame-timing experiments.

### No final-selection overreach
P0.3 may identify a working shortlist, but P0.4–P0.7 remain mandatory before final experimental commitment.

---

## 8. P0.3 Exit Criteria

P0.3 is complete when:

- [x] candidate datasets have been identified and audited;
- [x] procedure/modality/task/annotation structure has been recorded;
- [x] current access routes have been checked;
- [x] licence/DUA/commercial-use constraints have been recorded;
- [x] source-video overlap and derived-data lineage have been mapped;
- [x] procedure/video-level split and leakage risks have been documented;
- [x] multicentre/procedure/device natural-shift structure has been recorded where available;
- [x] visual-corruption suitability has been assessed;
- [x] temporal/network-degradation suitability has been assessed;
- [x] storage/download/compute constraints have been assessed;
- [x] current access failures have been recorded rather than ignored;
- [x] a working, non-final dataset shortlist has been produced;
- [x] all P0.3 RQs have evidence-linked answers;
- [x] unresolved questions for P0.4–P0.7 have been recorded;
- [x] global literature/reference records have been updated;
- [x] `TASK.md`, `RESEARCH_LOG.md`, `MEMORY.md`, and `README.md` have been updated;
- [x] `task-completion-report/P0.3_COMPLETION_REPORT.md` has been produced.

---

## 9. P0.3 Completion Milestone

P0.3 completed on **2026-09-25** after access, provenance, split, licence and feasibility audit.

Suggested repository milestone after commit/review:

**`v0.0.3 — Dataset Feasibility Map`**

The next active task is:

**P0.4 — Distribution-Shift Literature Reconnaissance**

P0.4 should determine which natural/synthetic shifts have already been studied and which corruption protocols are scientifically defensible before any experimental shift generator is fixed.

---

# Remaining Phase 0 Tasks

## P0.4 — Distribution-Shift Literature Reconnaissance

## Status

`COMPLETE — 2026-09-25`

## 1. Purpose

Establish an evidence-backed map of **distribution shift and robustness in surgical computer vision** before fixing any experimental shift protocol or novelty claim.

P0.4 separates:

- natural external-domain shift;
- controlled visual corruption;
- temporal/video degradation;
- compound shift;
- domain adaptation;
- domain generalization;
- robustness mitigation and evaluation.

The task asks:

> **What kinds of distribution shift have already been demonstrated in surgical CV, how are they evaluated and mitigated, and which shift families remain scientifically justified for later reliable-inference experiments?**

P0.4 does **not** determine the final novelty of Track A, B or C.

---

## 2. Scope Boundaries

### In scope

- hospital/centre shift;
- acquisition/device shift;
- instrument morphology/vendor shift;
- procedure/workflow shift;
- temporal/calendar external cohorts;
- modality and sim-to-real shift;
- smoke, blood, illumination, blur and colour corruption;
- compression/resolution as visual robustness factors;
- temporal/video instability and controlled temporal corruption where directly studied;
- UDA, DG, augmentation, synthetic data and multimodal robustness methods;
- compound natural or synthetic shift;
- shift-evaluation methodology.

### Out of scope

- calibration/conformal/selective-prediction method review → **P0.5**;
- detailed network/QoS/codec transport mechanisms → **P0.6**;
- final novelty judgement → **P0.7**;
- adversarial attacks as the principal deployment shift;
- non-surgical medical-imaging shift except clearly labelled adjacent methodological evidence.

---

## 3. Research Questions

### RQ1 — Shift Taxonomy
What natural, synthetic, temporal and compound shifts are documented in surgical computer vision?

### RQ2 — Natural Shift Evaluation
How are real deployment shifts operationalized?

Investigate:

- centre/institution;
- camera/recording system;
- instrument vendor/version;
- procedure;
- workflow;
- temporal external cohort;
- imaging modality;
- simulation/VR-to-clinical.

### RQ3 — Controlled Corruption
Which controlled non-adversarial corruptions have been used?

Investigate:

- low illumination / exposure;
- smoke;
- blood / bleeding;
- motion blur;
- defocus;
- colour / white balance / contrast;
- noise;
- haze;
- compression;
- resolution;
- optical obstruction / lens contamination;
- background/style changes.

Determine whether severity is arbitrary, challenge-defined, clinically calibrated or physically defined.

### RQ4 — Task / Dataset Coverage
Which surgical-CV tasks and benchmark ecosystems have actually been evaluated under shift?

### RQ5 — Mitigation Methods
Which robustness, augmentation, UDA and DG strategies are already established?

### RQ6 — Evaluation Practice
How should clean vs shifted performance, severity, external validation and worst-case robustness be reported?

### RQ7 — Temporal and Compound Shift
What evidence exists for:

- temporal prediction instability;
- missing frames;
- packet-loss-like corruption;
- frame-rate/sampling changes;
- compound image corruption;
- visual + temporal/network combinations?

### RQ8 — Working Shift Set
Which shift families should be carried forward to P0.5–P0.7 without prematurely fixing exact experimental parameters?

---

## 4. Evidence Strategy

Priority:

1. peer-reviewed surgical robustness/generalization benchmarks;
2. multicentre external-validation studies;
3. peer-reviewed surgical UDA/DG studies;
4. EndoVis/MICCAI robustness challenges;
5. recent peer-reviewed 2026 external-domain evidence;
6. accepted/preprint evidence where it materially changes the current landscape;
7. adjacent GI-endoscopy robustness methodology, explicitly labelled as adjacent.

A paper was not retained merely because it used the word “robust.” It had to evaluate a changed distribution or propose a method specifically tested across domains/corruptions.

---

## 5. Work Packages

### WP1 — Shift-Literature Discovery
Identify natural-shift, corruption, robustness, UDA/DG and temporal-robustness evidence.

**Output:** source registry and screening trail.

### WP2 — Shift Taxonomy
Construct a surgical-CV taxonomy separating natural, controlled visual, temporal/video and compound shift.

**Output:** `shift-taxonomy.md`

### WP3 — Natural-Shift Mapping
Map external centre/device/procedure/modality evidence.

**Output:** `natural-shift-map.csv`

### WP4 — Controlled-Corruption Mapping
Map visual corruption operators, severity conventions and direct surgical precedent.

**Output:** `synthetic-corruption-map.csv`

### WP5 — Temporal / Video Shift Mapping
Separate ordinary temporal modelling from actual temporal-input degradation.

**Output:** `temporal-video-shift-map.csv`

### WP6 — Mitigation / Method Mapping
Map augmentation, adaptation, DG, causal/multimodal and foundation-model strategies.

**Output:** `method-baseline-map.csv`

### WP7 — Evaluation and Compound-Shift Analysis
Document defensible evaluation practice and stress-test the broad Track A framing.

**Outputs:**
- `evaluation-practices.md`
- `compound-shift-evidence.md`
- `quantitative-evidence.csv`

### WP8 — Working Protocol and RQ Closure
Produce a non-final shift protocol and answer every RQ.

**Outputs:**
- `candidate-shift-protocol.md`
- `rq-answer-matrix.md`
- `open-questions.md`

---

## 6. Required Artifacts

### A1 — Search Protocol
`literature/distribution-shift/search-protocol.md`

### A2 — Source Screening Log
`literature/distribution-shift/source-screening-log.csv`

### A3 — Source Index / Audit
- `literature/distribution-shift/source-index.md`
- `literature/distribution-shift/source-audit.md`

### A4 — Distribution-Shift Literature Map
`literature/distribution-shift/distribution-shift-literature-map.csv`

### A5 — Narrative Landscape
`literature/distribution-shift/distribution-shift-landscape.md`

### A6 — Shift Taxonomy
`literature/distribution-shift/shift-taxonomy.md`

### A7 — Natural Shift Map
`literature/distribution-shift/natural-shift-map.csv`

### A8 — Controlled Corruption Map
`literature/distribution-shift/synthetic-corruption-map.csv`

### A9 — Temporal / Video Shift Map
`literature/distribution-shift/temporal-video-shift-map.csv`

### A10 — Method / Baseline Map
`literature/distribution-shift/method-baseline-map.csv`

### A11 — Quantitative Evidence
`literature/distribution-shift/quantitative-evidence.csv`

### A12 — Evaluation Practices
`literature/distribution-shift/evaluation-practices.md`

### A13 — Compound-Shift Evidence
`literature/distribution-shift/compound-shift-evidence.md`

### A14 — Working Shift Protocol
`literature/distribution-shift/candidate-shift-protocol.md`

### A15 — Research Question Answer Matrix
`literature/distribution-shift/rq-answer-matrix.md`

### A16 — Open Questions
`literature/distribution-shift/open-questions.md`

### A17 — References
`literature/distribution-shift/references.bib`

Relevant non-duplicate entries are also merged into:

`literature/references.bib`

### A18 — Programme Updates
- `literature/literature-map.csv`
- `TASK.md`
- `RESEARCH_LOG.md`
- `MEMORY.md`
- `README.md`
- `phase-task-files/phase0.md`
- `task-completion-report/P0.4_COMPLETION_REPORT.md`

---

## 7. Quality Requirements

### Shift specificity
Do not use “OOD” as a substitute for naming the changed factor/domain.

### Natural vs controlled
A real external centre and a synthetic brightness transform answer different questions and must be reported separately.

### Adaptation-setting fidelity
Distinguish:

- DG — no target data;
- UDA — unlabeled target data;
- supervised/few-shot adaptation — labeled target data;
- test-time adaptation — target deployment stream affects the model.

### Network-mechanism fidelity
Do not call frame dropping or compression “network-induced” until P0.6 establishes the network/codec/decoder mechanism.

### Severity fidelity
Do not copy ImageNet-C or adjacent GI-endoscopy severity values and label them clinically realistic for surgery without surgical calibration.

### Provenance integrity
P0.3 source-video overlap rules remain active for all cross-dataset shift claims.

### No novelty overreach
Existing evidence for:
- multicentre generalization;
- smoke/blood/low-light robustness;
- UDA/DG;
- compound image corruption;
- emerging packet-loss video corruption

must be reflected when later formulating novelty.

---

## 8. P0.4 Exit Criteria

P0.4 is complete when:

- [x] natural shift types are mapped;
- [x] controlled surgical visual corruptions are mapped;
- [x] temporal/video shift evidence and negative evidence are mapped;
- [x] compound-shift precedent is documented;
- [x] representative UDA/DG/robustness methods are mapped;
- [x] multicentre/device/procedure shift evidence is documented;
- [x] direct surgical corruption evidence is distinguished from adjacent endoscopy evidence;
- [x] severity-calibration practices are documented;
- [x] shift evaluation/reporting rules are documented;
- [x] selected quantitative evidence is extracted;
- [x] all P0.4 RQs have evidence-linked answers;
- [x] a non-final candidate shift protocol has been produced;
- [x] P0.5/P0.6/P0.7 open questions have been recorded;
- [x] global literature/reference records are updated;
- [x] programme status files are updated;
- [x] `task-completion-report/P0.4_COMPLETION_REPORT.md` is produced.

---

## 9. P0.4 Completion Milestone

P0.4 completed on **2026-09-25** after final evidence audit.

Suggested repository milestone after commit/review:

**`v0.0.4 — Distribution-Shift Evidence Map`**

The next active task is:

**P0.5 — Reliable-Inference Literature Reconnaissance**

P0.5 must determine whether calibration, uncertainty, selective prediction and conformal methods remain reliable under the shift families retained by P0.4.

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
- [x] surgical-CV landscape is mapped;
- [x] candidate datasets are mapped and feasibility-audited;
- [x] distribution-shift literature is mapped;
- [ ] reliable-inference literature is mapped;
- [ ] telesurgery/network literature is mapped;
- [ ] the intersection evidence matrix is complete;
- [ ] Track A–C novelty has been stress-tested;
- [ ] candidate research questions have been revised from evidence;
- [ ] unsupported novelty claims have been removed;
- [ ] the next experimental/research phase is justified by the evidence.

## Phase 0 Programme Milestone

**M0 — Evidence-Backed Research Map**
