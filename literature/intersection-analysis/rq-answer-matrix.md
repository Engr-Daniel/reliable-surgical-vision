# P0.7 Research Question Answer Matrix

## RQ1 — What does the integrated P0.1–P0.6 evidence base contain?
**Answer:** 175 coded rows / **165 unique sources** after collapsing 10 cross-task duplicates (e.g. ROBUST-MIS, PhaKIR challenge, Endo-C6, Toumai clinical series). The base consists of 152 P0.1–P0.6 entries already in the global map, 11 entries present in task maps but missing from the global map (now restored), and 12 P0.7 refresh sources. The surgical-CV and telesurgery-network literatures are almost disjoint. No telesurgery source evaluates an AI model, and only two surgical-CV evaluations touch networks (Endo-C6's clip-level abstraction and a delivery-latency study).  
**Evidence:** all retained IDs; IX01–IX12.  
**Detailed:** `global-evidence-matrix.csv`, `coverage-summary.md`, `build_global_evidence_matrix.py`.

## RQ2 — Which intersections are saturated, occupied, partial, or not found?
**Answer:** Of 26 rated cells, 3 are SATURATED, 11 OCCUPIED, 4 PARTIAL and 8 NOT FOUND IN RETAINED EVIDENCE.
- Closed areas: segmentation under natural/visual shift; phase recognition under natural shift; phase temporal stability; packet-loss corruption of surgical TVLMs; network effects on human operators (including compound); network→decoded-video quality; surgical UQ/OOD; segmentation failure monitoring with conformal calibration; generic network→DNN accuracy; telemetry→QoS forecasting.
- The not-found cells all share one structure: *network → transport → decoder → online surgical model → reliability decision*, centred on whether telemetry adds information beyond the pixels (X23; X22 for any domain).  
**Evidence:** cell anchors in `intersection-map.csv`.  
**Detailed:** `intersection-map.csv`, `intersection-analysis.md`.

## RQ3 — Does Track A survive the stress test?
**Answer:** Only narrowly. Broad compound-shift, visual-corruption, packet-loss and multi-network-factor claims are closed (X03, X05, X07, X10). What survives is a mechanism question: does phase error depend on the degradation mechanism at matched decoded-video quality? This is motivated by VISTA's finding for human operators. Track A is **absorbed** as the shift-construction work package.  
**Evidence:** SH09–SH11, SH17, SH18, NW04, IX01, IX04.  
**Detailed:** `novelty-stress-test.md` §Track A.

## RQ4 — Does Track B survive the stress test?
**Answer:** Only narrowly. Surgical calibration, UQ, OOD, abstention, conformal prediction and degradation-aware failure monitoring are closed (X12–X15). What survives is an empirical audit of phase-recognition calibration and conformal coverage under decoder-mediated and natural shift (X16/X19), plus telemetry-stratified Mondrian calibration as a design choice (X24). Track B is **narrowed** to the reliability-evaluation layer.  
**Evidence:** RI12–RI17, RI22–RI34, IX05.  
**Detailed:** `novelty-stress-test.md` §Track B.

## RQ5 — Does Track C survive the stress test?
**Answer:** Yes, in a narrowed form, with **high residual risk**. Network→DNN accuracy, network→surgical video quality and telemetry→QoS forecasting are closed (X20, X11, X21). No retained source in any domain tests whether network/transport telemetry improves AI-failure prediction beyond a strong video-only monitor (X22/X23). Generic networking venues were searched only shallowly, so this must be confirmed by the Phase 1 targeted search before commitment. Track C becomes the **primary** question.  
**Evidence:** IX01, IX07–IX11, RI34, SH18.  
**Detailed:** `novelty-stress-test.md` §Track C.

## RQ6 — Should the tracks remain separate, merge, split, or be dropped?
**Answer:** **Merge** into one integrated study: C primary (RQ1), B as the reliability layer (RQ2), A as the shift substrate (RQ3). None is dropped or split. Reasons: a shared pipeline, data and analysis; robustness to a negative primary result; and the overlap pressure on standalone A and B. Track directories remain as work packages.  
**Detailed:** `track-decision.md`.

## RQ7 — What are the revised candidate research questions?
**Answer:** RQ1 asks whether receiver-observable telemetry improves failure detection (ΔAUROC with CI excluding 0; 0.02 = smallest effect of interest, final wording in pre-registration v1.1) and selective deferral (AURC) beyond a V0+V1 video-only monitor in online phase recognition on network-delivered video. RQ2 asks whether clean-calibrated APS/RAPS coverage and calibration survive impairment and centre shift, and whether telemetry-stratified Mondrian calibration restores per-stratum coverage. RQ3 asks whether degradation mechanism matters at matched VMAF. Each question has explicit rejection criteria.  
**Detailed:** `revised-research-questions.md`.

## RQ8 — What Phase 1 direction does the evidence justify?
**Answer:** Phase 1 (Gap Validation) runs a blocking targeted search of networking/video-analytics and 2026 surgical venues for X22/X23, followed by pre-registration, a media-pipeline specification (reusing VISTA where licensing permits), feature-tier and leakage specification, dataset desk checks (Cholec80, PhaKIR, AutoLaparo), a feasibility/power memo and baseline model selection (one TCN-based and one transformer-based online phase model). No data acquisition or training happens before Phase 1 exits.  
**Detailed:** `phase1-direction.md`.

## RQ9 — Have unsupported novelty/"first" claims been removed?
**Answer:** None were present in programme-authored text. All "first" occurrences are titles of external (mostly manufacturer) sources, already classified in P0.1. The prohibited claim list and permitted framing are now recorded, and a re-audit is required before any manuscript and after P1.1.  
**Detailed:** `claim-audit.md`.

# P0.7 Overall Conclusion
The programme's provisional tracks overlap heavily with existing work when taken one at a time. Together they point to one question not found in the retained evidence: **does a surgical video model's reliability layer gain anything from network-side information that is not visible in the received frames?** The question can be answered informatively whether the result is positive or negative. It needs a real media pipeline, a strong video-only baseline and a temporal task with dense labels. Its main risk is unretrieved work in generic networking venues, so it is carried into Phase 1 as a **candidate** pending targeted gap validation, not as a novelty claim.
