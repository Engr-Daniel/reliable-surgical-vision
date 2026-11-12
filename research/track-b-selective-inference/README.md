# Track B — Selective Inference

## Status after P0.7 (2026-11-12)
**NARROWED** to **WP-B: reliability-evaluation layer** of the integrated study. See `../../literature/intersection-analysis/track-decision.md`.

## Original provisional question
Can uncertainty-aware, selective and/or conformal methods improve the reliability of surgical visual inference under distribution shift?

## Why narrowed
Surgical calibration, UQ, OOD/open-set, abstention, conformal prediction and degradation-aware failure monitoring are occupied (X12–X15). What survives is an empirical audit of phase-recognition reliability under decoder-mediated and natural shift (B6), and telemetry-stratified conformal calibration as a design choice (B7).

## Work-package responsibilities
- reliability ladder (P0.5): MSP/entropy, temperature scaling, ensembles/MC dropout, failure detection, risk–coverage/AURC, APS/RAPS conformal sets;
- metrics: AUROC/AUPRC, AURC, ECE/NLL/Brier, coverage and set size (marginal and per-stratum), TFI;
- RQ2 analysis; the evaluation harness for RQ1.
