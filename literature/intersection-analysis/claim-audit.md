# P0.7 Claim Audit — Novelty / "First" Language

## Scope
Every Markdown file in the repository outside `literature/intersection-analysis/` was searched on 2026-11-12 for: *first, novel/novelty, unique, unprecedented, no prior, never been, untouched, state of the art, solves, proves*. Each hit was classified.

## Result
**No affirmative novelty or "first" claim was found in programme-authored text.** Every hit falls into one of three classes:

| Class | Example locations | Action |
|---|---|---|
| Negative/guard statements ("not novel", "no novelty claim is final", "no longer untouched") | `MEMORY.md`, `RESEARCH_LOG.md`, `literature/distribution-shift/*`, `literature/uncertainty-reliability/reliable-inference-landscape.md`, `literature/telesurgery-networking/*`, track READMEs | Keep; consistent with P0.7 |
| Titles of external sources containing "first" (manufacturer/institutional claims) | `literature/toumai/source-index.md` S07, S08, S13, S14, S15, S16; `literature/telesurgery-networking/source-index.md` NW17 | Keep verbatim as titles. P0.1 already classifies S13/S14/S16 as manufacturer-reported and S15 as secondary. These are **not** programme claims and must not be repeated as fact |
| Methodological instructions (AGENT.md "avoid 'proves', 'solves'...") | `AGENT.md` | Keep |

The one external self-description of priority that P0.7 encountered, RI31's statement that it was the first application of conformal prediction to surgical guidance, belongs to that source. It is recorded nowhere in the programme as a programme claim.

## Claims now explicitly prohibited
Restated in `novelty-stress-test.md` ("Cross-track claim hygiene"); summarised here:
1. "first" network/packet-loss/compression study of surgical AI;
2. "first" uncertainty/calibration/conformal/selective work in surgical CV;
3. "first" compound-shift or multi-network-factor study;
4. "telemetry-based AI-failure prediction is new" (unverified; high residual risk until P1.1);
5. any clinical-safety, safe-threshold or deployment-readiness claim from emulated experiments.

## Permitted framing
- "not found in the programme's retained evidence (search dated …; residual risk …)";
- "we measure whether …", "we test the incremental value of …";
- "an empirical audit of …".

## Re-audit rule
Re-run this audit before any manuscript draft, and after Phase 1 (P1.1). Re-use the same search terms and add any new superlatives found in drafts ("pioneering", "unique", "groundbreaking").
