# Intersection Analysis & Novelty Stress-Test — P0.7

P0.7 integrates P0.1–P0.6, rates where the programme's question space is occupied, stress-tests Tracks A–C, and sets the evidence-backed Phase 1 direction.

## Start here
1. `rq-answer-matrix.md`: concise answers to all P0.7 questions
2. `track-decision.md`: merge decision and locked scope
3. `revised-research-questions.md`: RQ1–RQ3 with falsifiable hypotheses
4. `phase1-direction.md`: Phase 1 (Gap Validation) work packages and exit criteria
5. `novelty-stress-test.md`: claim-by-claim verdicts for Tracks A–C
6. `intersection-map.csv` and `intersection-analysis.md`: 26 rated intersection cells
7. `global-evidence-matrix.csv` and `coverage-summary.md`: coded evidence base (generated)
8. `claim-audit.md`: novelty/"first" language audit
9. `open-questions.md`
10. `search-protocol.md`, `source-screening-log.csv`, `source-index.md`, `references.bib`: P0.7 refresh records

## Reproducing the matrix
```bash
python3 literature/intersection-analysis/build_global_evidence_matrix.py
```
Codes are assigned manually per source in the script's `CODES` table. The script fails if any retained source is uncoded.

## Non-negotiable rule
**An intersection rated "not found in retained evidence" is not a novelty claim.** Every such cell carries a residual-risk rating. The high-risk cells (X22, X23) must pass the Phase 1 targeted search before any experiment is committed.

## Status
**P0.7 complete — 2026-11-12.**
