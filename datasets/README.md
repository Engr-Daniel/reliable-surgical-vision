# Dataset Registry — P0.3

P0.3 audits candidate datasets for **access, provenance, leakage, annotations, temporal structure, compute feasibility, and suitability for later reliability experiments**.

Do not commit raw/restricted surgical data to this repository.

## Start here

1. `rq-answer-matrix.md` — concise answers to the P0.3 research questions.
2. `dataset-shortlist.md` — working candidate set and why each remains relevant.
3. `dataset-registry.csv` — full 18-dataset audit.
4. `access-license-audit.csv` — current access/licensing constraints.
5. `provenance-overlap-map.md` — source-video lineage and leakage rules.
6. `split-leakage-audit.csv` — split/site/procedure integrity.
7. `temporal-network-suitability.csv` — whether data can support visual vs temporal/network degradation.
8. `compute-access-feasibility.csv` — operational burden.
9. `dataset-decision-matrix.csv` — evidence synthesis by experimental role.
10. `search-protocol.md`, `source-screening-log.csv`, `source-index.md` — reproducibility trail.

## Non-negotiable rule

**Cross-dataset does not mean cross-domain until source-video overlap is ruled out.**

All experiments must preserve source procedure/video IDs and use procedure-level split integrity.

## Status

**P0.3 complete — 2026-09-25.**

Final dataset selection remains deferred to P0.4–P0.7.
