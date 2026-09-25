# phase-task-files/phase0.md — P0.1 status patch


## Active Task

**P0.1 — Toumai Technical Literature & Architecture Reconnaissance**

### Status

`COMPLETE — 2026-09-25`

---

# 1. Purpose

Establish an evidence-backed technical understanding of the **Toumai robotic and tele-robotic surgical system**, with particular attention to the components relevant to reliable visual inference.

This task will reconstruct the publicly documented system architecture from primary research literature, official technical documentation, clinical studies, regulatory information, and other authoritative sources.

The objective is not to propose improvements to Toumai at this stage.

The objective is to determine:

> **What is technically known, what is reported but not independently established, what can reasonably be inferred, and what remains unknown about the Toumai tele-robotic architecture?**

This provides part of the technical foundation for the wider Reliable Surgical Vision research programme.

---

# 2. Research Questions

P0.1 will investigate the following questions.

### RQ1 — System Architecture

What are the principal components of the Toumai robotic surgical system?

Investigate:

- surgeon console;
- patient-side robotic platform;
- robotic arms and instruments;
- vision system;
- imaging hardware;
- computing components;
- communication components;
- control architecture;
- safety mechanisms.

---

### RQ2 — Visual Pipeline

How is surgical visual information acquired, processed, transmitted, and presented?

Investigate:

- endoscopic imaging;
- camera configuration;
- image-processing pipeline;
- video encoding/decoding;
- image enhancement;
- smoke removal where documented;
- vascular enhancement where documented;
- image resolution;
- frame rate;
- imaging latency;
- video transmission.

Particular attention should be given to components that could influence downstream computer-vision inference.

---

### RQ3 — Teleoperation Pipeline

How are surgeon commands transmitted to the patient-side robotic system?

Investigate:

- master–slave control;
- motion sensing;
- command transmission;
- robotic actuation;
- feedback mechanisms;
- control frequency where available;
- command latency;
- motion scaling;
- tremor filtering;
- synchronization.

---

### RQ4 — Communications Architecture

What communication infrastructure has been reported for Toumai telesurgery?

Investigate reported use of:

- dedicated fibre;
- broadband;
- 5G;
- satellite communication;
- hybrid communication architectures;
- redundant links.

Extract reported:

- latency;
- round-trip time;
- jitter;
- packet loss;
- bandwidth;
- frame loss;
- encoding/decoding delay;
- network switching or redundancy behaviour.

---

### RQ5 — Reliability and Safety

How does the system respond to degraded or interrupted communications?

Investigate:

- standby behaviour;
- fail-safe mechanisms;
- communication-loss detection;
- command interruption;
- robotic arm behaviour;
- redundant network paths;
- bedside surgical support;
- conversion procedures;
- recovery mechanisms;
- safety thresholds where publicly documented.

---

### RQ6 — Relevance to Reliable Visual Inference

Which parts of the Toumai architecture could influence the reliability of computer-vision inference?

Potential pathways include:

`Network degradation → video degradation → input distribution shift → model reliability degradation`

and:

`Imaging conditions → visual distribution shift → uncertainty → prediction / abstention`

These relationships are hypotheses to investigate and must not be presented as established Toumai behaviour without evidence.

---

# 3. Evidence Strategy

Sources should be prioritised approximately as follows:

1. peer-reviewed primary research;
2. regulatory or standards documentation;
3. official technical documentation;
4. clinical studies involving Toumai;
5. conference proceedings or technical reports;
6. manufacturer documentation;
7. authoritative institutional reporting;
8. secondary reporting where primary evidence is unavailable.

Manufacturer specifications must be clearly identified as manufacturer-reported unless independently validated.

News reporting may provide context but should not be treated as sufficient evidence for detailed technical claims when stronger sources exist.

---

# 4. Evidence Classification

Important technical claims should be classified as:

### Independently documented

Supported by peer-reviewed or independent technical/clinical evidence.

### Manufacturer-reported

Reported by MicroPort MedBot or another manufacturer-affiliated source.

### Institution-reported

Reported by participating hospitals, universities, research institutions, or clinical teams.

### Inferred

Reasonable engineering inference based on documented architecture but not explicitly confirmed.

### Unknown

Information could not be established from accessible public evidence.

This classification should be preserved in the evidence table.

---

# 5. Work Packages

## WP1 — Literature Discovery

Identify Toumai-related publications covering:

- robotic architecture;
- telesurgery;
- clinical evaluation;
- imaging;
- communication;
- networking;
- safety;
- latency;
- remote control.

### Output

Candidate literature set.

---

## WP2 — Literature Screening

Determine which sources contain technically relevant information.

Exclude or deprioritise:

- duplicate reporting;
- purely promotional material where stronger evidence exists;
- sources without relevant architectural or reliability information.

### Output

Screened Toumai literature set.

---

## WP3 — Technical Evidence Extraction

Extract:

- system component;
- technical claim;
- reported value;
- experimental condition;
- evidence source;
- evidence classification;
- limitations.

### Output

Structured evidence table.

---

## WP4 — Architecture Reconstruction

Reconstruct the documented Toumai system architecture.

The architecture should cover, where evidence permits:

`Surgeon → Console → Communication → Patient-side Robot → Patient`

and the reverse visual pathway:

`Patient → Camera → Image Processing → Encoding → Network → Decoding → Surgeon Display`

Do not add undocumented components as confirmed architecture.

### Output

Evidence-backed architecture diagram.

---

## WP5 — Reliability Analysis

Map documented failure and degradation pathways.

Examples:

- communication interruption;
- latency increase;
- packet loss;
- video degradation;
- synchronization problems;
- network failover.

Determine documented system responses where available.

### Output

Reliability and failure-pathway section of the architecture report.

---

## WP6 — Research-Relevance Mapping

Identify architectural components relevant to later investigation of:

- distribution shift;
- visual corruption;
- uncertainty;
- calibration;
- OOD detection;
- selective prediction;
- conformal prediction;
- network-aware inference.

This work should identify research questions rather than prematurely claim research gaps.

### Output

Research-relevance section and open technical questions.

---

# 6. Required Artifacts

P0.1 should produce the following artifacts.

### A1 — Technical Architecture Report

`docs/architecture/toumai-system-architecture.md`

Contains:

- system overview;
- hardware architecture;
- visual pipeline;
- teleoperation pipeline;
- communications architecture;
- reliability mechanisms;
- safety mechanisms;
- relevance to reliable visual inference;
- limitations of available evidence.

---

### A2 — Architecture Diagram

`docs/architecture/toumai-architecture.svg`

Optional rendered version:

`docs/architecture/toumai-architecture.png`

The diagram must distinguish documented architecture from inferred components where necessary.

---

### A3 — Toumai Literature Map

`literature/toumai/toumai-literature-map.csv`

Recommended fields:

- ID;
- title;
- authors;
- year;
- venue;
- source type;
- DOI/URL;
- technical topic;
- system component;
- network type;
- reported latency;
- reported packet loss;
- reported bandwidth;
- safety information;
- evidence classification;
- relevance;
- notes.

---

### A4 — Toumai Evidence Table

`literature/toumai/toumai-evidence-table.md`

Recommended structure:

| Claim | Component | Evidence | Source | Classification | Limitation |
|---|---|---|---|---|---|

This should become the principal traceability mechanism between the architecture report and its sources.

---

### A5 — Open Technical Questions

`literature/toumai/open-technical-questions.md`

Record information that remains unavailable or insufficiently documented.

Examples may include:

- exact control-loop frequency;
- failover thresholds;
- video codec configuration;
- network switching behaviour;
- detailed visual-processing architecture;
- synchronization mechanisms.

Only include these when the literature reconnaissance confirms that they remain unresolved.

---

### A6 — Global Literature Map Update

`literature/literature-map.csv`

Relevant Toumai/telesurgery publications should also be incorporated into the programme-wide literature map.

---

### A7 — Research Log Update

`RESEARCH_LOG.md`

Record:

- search dates;
- major findings;
- important methodological decisions;
- unexpected observations;
- unresolved questions;
- implications for later phases.

---

### A8 — Task Tracker Update

`TASK.md`

Mark P0.1 subtasks complete only when their corresponding evidence/artifacts exist.

---

# 7. Quality Requirements

P0.1 is not complete merely because several papers have been collected.

The task must demonstrate:

### Traceability

Important technical statements can be traced to evidence.

### Source quality

Primary and authoritative sources are prioritised.

### Evidence separation

Confirmed facts, manufacturer claims, institutional reports, engineering inference, and unknowns are clearly distinguished.

### Technical precision

Latency, bandwidth, packet loss, frame rate, resolution, and related quantities retain their original experimental context.

### Reproducibility

Another researcher should be able to reconstruct the literature search and understand why the architecture was represented as shown.

### Uncertainty

Missing technical information is explicitly reported rather than guessed.

---

# 8. Exit Criteria

P0.1 is complete when:

- [x] Toumai-specific literature has been systematically identified.
- [x] Relevant sources have been screened.
- [x] Technical claims have been extracted.
- [x] Evidence classifications have been assigned.
- [x] The system architecture has been reconstructed from evidence.
- [x] The visual pipeline has been documented.
- [x] The teleoperation pipeline has been documented.
- [x] Communications architecture has been documented where evidence permits.
- [x] Reliability and safety mechanisms have been mapped.
- [x] Unknown technical details have been explicitly recorded.
- [x] Relevance to reliable visual inference has been analysed without unsupported novelty claims.
- [x] All required artifacts have been produced.
- [x] `TASK.md` has been updated.
- [x] `RESEARCH_LOG.md` has been updated.

---

# 9. Completion Milestone

### Completion record

P0.1 completed on 2026-09-25 after a final evidence audit.

Core completion artifacts:
- `docs/architecture/toumai-system-architecture.md`
- `docs/architecture/toumai-architecture.svg`
- `literature/toumai/search-protocol.md`
- `literature/toumai/source-screening-log.csv`
- `literature/toumai/toumai-literature-map.csv`
- `literature/toumai/toumai-network-metrics.csv`
- `literature/toumai/toumai-evidence-table.md`
- `literature/toumai/source-audit.md`
- `literature/toumai/open-technical-questions.md`
- `literature/toumai/references.bib`


The next planned task is:

**P0.2 — Surgical Computer-Vision Landscape Reconnaissance**