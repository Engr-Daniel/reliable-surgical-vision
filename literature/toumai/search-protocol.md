# P0.1 Search and Review Protocol

## Identity
- **Programme:** Reliable Surgical Vision
- **Phase:** Phase 0 — Research Foundation
- **Task:** P0.1 — Toumai Technical Literature & Architecture Reconnaissance
- **Final audit date:** 2026-09-25
- **Evidence cutoff:** 2026-09-25
- **Review type:** focused technical reconnaissance with reproducible search and claim-level evidence extraction
- **Not claimed as:** PRISMA systematic review, meta-analysis, or exhaustive bibliographic census

## Objective
Reconstruct the publicly documented Toumai MT-1000/tele-robotic system architecture, with emphasis on:
1. system composition;
2. master–slave control;
3. visual acquisition/processing;
4. remote communication architectures;
5. measured latency/jitter/loss/bandwidth;
6. redundancy/fallback/safety;
7. technical unknowns relevant to reliable computer-vision inference.

## Search surfaces
The reconnaissance used public web discovery and direct inspection of:
- PubMed and PubMed Central;
- Scientific Reports / Nature;
- SpringerLink (Journal of Robotic Surgery; Surgical Endoscopy);
- ScienceDirect (Urology; European Journal of Surgical Oncology);
- Wiley Online Library (International Journal of Medical Robotics and Computer Assisted Surgery);
- official MicroPort / MicroPort MedBot product and technical news pages;
- public copies/mirrors of the NMPA/CMDE technical review for acceptance no. CQZ2100611;
- current Nigerian reporting and manufacturer/institutional reporting for the September 2026 RHV–Nisa case.

## Representative exact query families
The final audit used the following strings or direct close variants:

- `"Toumai" 4000 Hz 250 μs FPGA dual-fiber imaging latency smoke removal vascular enhancement`
- `"Toumai" telecholecystectomy 43.4 ms jitter 4 ms 98.3 Mbps 213 Mbps packet loss`
- `"Toumai" 181.4 ms RTT Shanghai Kuwait RARP`
- `"Toumai" 20 ms jitter <10 ms Belgium hysterectomy`
- `"Toumai" 37.7 5.6 ms jitter 2.2 packet loss redundant 5G 3700 km`
- `"Toumai" 12 ms fiber 46 ms 5G hybrid network partial nephrectomy prostatectomy`
- `"Toumai MT-1000" MSS810 SSS800 VSS820 NMPA technical review`
- `"CQZ2100611" Toumai`
- `"图迈" MT-1000 技术审评报告 MSS810 SSS800 VSS820`
- `"Toumai" signal interruption standby 3 seconds master slave safety mechanism`
- `"Toumai" radical gastrectomy 226 32 ms packet loss 0.1%`
- `"Application of 5G Remote Robotic-assisted Laparoscopy in Urological Surgery" Toumai`
- `"Current perspectives of telesurgery applications among different specialties" Toumai`
- `"Feasibility and Safety of Cross-Regional 5G-Enabled Remote Robot-Assisted Laparoscopic Surgery" jitter`
- `"Feasibility and Safety of Cross-Regional 5G-Enabled Remote Robot-Assisted Laparoscopic Surgery" 100 Mbps`
- `"Toumai" LEO satellite <60 ms MicroPort`
- `"Toumai Tele-Robotic Surgical System" fiber broadband 5G satellite sub-50 ms sub-150 ms`
- `"Redeemer's Health Village" Nisa Premier Toumai Starlink MTN September 2026`

## Screening method
Two passes were used.

### Pass 1 — relevance
Candidate records were kept if they contained Toumai-specific:
- architecture;
- imaging/control details;
- human telesurgery;
- measured network performance;
- network redundancy;
- interruption/fallback/safety behavior;
- deployment context relevant to later research.

### Pass 2 — evidence utility
Retained sources had to support at least one claim with sufficient specificity for the evidence table. Duplicate mirrors, secondary rewrites, non-Toumai remote systems, and purely promotional duplicates were excluded/deprioritized.

The **final audit screening set contains 25 unique records/categories: 16 retained and 9 excluded/deprioritized**. This is a documented final screening set, not a claim about the total number of raw search-engine hits encountered.

See `source-screening-log.csv`.

## Evidence classes
- **Peer-reviewed primary** — direct clinical/technical observation.
- **Peer-reviewed synthesis** — systematic/review evidence used for triangulation.
- **Regulatory technical review** — device composition/working principle from regulatory review material.
- **Manufacturer documentation** — product identity or claimed capabilities; not independent validation.
- **Institutional/secondary deployment evidence** — contextual deployment facts not yet peer-reviewed.
- **Inference** — engineering interpretation based on documented components.
- **Unknown** — public evidence insufficient.

## Extraction rules
1. Preserve the source's definition of each timing metric.
2. Never combine **network RTT**, **one-way network latency**, **imaging latency**, **total delay**, **master–slave response time**, or **motion-to-photon latency**.
3. Record distance and network topology with each metric.
4. Record packet loss, jitter and throughput when available.
5. Record whether redundancy and bedside takeover were part of the deployment.
6. Manufacturer claims remain labelled as manufacturer claims even when plausible.
7. Missing values are `NR` (not reported) or `Unknown`; they are not estimated.
8. Deployment-specific security/network choices are not universalized into Toumai's intrinsic architecture.
9. The relationship `network state → received-video distribution → CV reliability` is treated as a research hypothesis, not an established Toumai mechanism.

## Reproducibility
A future researcher can reproduce the reconnaissance by:
1. rerunning the query families above;
2. resolving records by DOI/PMID/source ID;
3. applying the stated inclusion/exclusion rules;
4. comparing against `source-screening-log.csv`;
5. re-extracting claims in `toumai-evidence-table.md`;
6. comparing network values against `toumai-network-metrics.csv`.

Before manuscript submission, the search should be rerun and forward citations of the core peer-reviewed studies checked.

## Known limitations
- Search-engine indexing/ranking changes with time.
- Some full texts are paywalled; when only abstract-level details were accessible, this is stated.
- The regulatory report was found as a faithful public mirror bearing the NMPA/CMDE identity; the official CMDE URL was not rediscovered in the final audit.
- Proprietary controller, codec and failover details remain inaccessible.
