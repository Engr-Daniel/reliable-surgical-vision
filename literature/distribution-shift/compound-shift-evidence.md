# P0.4 Compound-Shift Evidence

## Question

Has “compound shift” already been studied, and what remains unresolved?

## 1. Natural compound shift is common

Multicentre evaluation is inherently compound.

When a model moves from one hospital to another, the deployment domain may change in:
- camera system;
- image processing;
- workflow;
- instrument vendor;
- surgeon;
- patient population;
- lighting;
- procedure timing.

MultiBypass140, PhaKIR and inter-hospital transfer studies therefore already test **aggregate compound natural shift**, although they generally cannot attribute the performance drop to one factor.

## 2. Controlled compound image corruption already has precedent

Jaspers et al. (GI endoscopy, adjacent to surgical video) provide a clinically calibrated robustness framework that generates test variants using combinations of multiple image distortions.

Therefore:

> **“Combining several image corruptions” is not by itself a novel methodological contribution.**

Any Track A contribution must be more specific.

## 3. Surgical-specific visual corruption is also established

SegSTRONG-C directly benchmarks:
- smoke;
- over-bleeding;
- low brightness

for robot-tool segmentation.

CaRTS/TC-CaRTS evaluate counterfactual surgical visual domains including smoke, blood, low brightness and background alteration.

Thus, a paper framed simply as “surgical AI under smoke/blood/low-light” would overlap existing literature.

## 4. Visual + temporal/network evidence is emerging

Endo-C6 (accepted MICCAI 2026 / arXiv) explicitly includes both:
- visual/acquisition corruptions (defocus, haze, motion blur, noise, smoke), and
- packet-loss bursts

within a temporal VLM robustness benchmark.

This is important because it means even “packet loss in surgical-video AI” can no longer be treated as untouched territory in the broadest sense.

However, P0.4 does **not** find a mature, conventional surgical-CV benchmark that systematically crosses:
- clinically plausible visual degradation severity,
with
- measured network/decoder temporal degradation severity,
for
- standard phase recognition / instrument or anatomy segmentation,
while also evaluating calibrated/selective reliability.

That narrower intersection remains **unresolved**, not “novel.”

## 5. Interaction effects

A compound-shift study becomes scientifically stronger when it asks:

`Does performance under A+B equal what would be expected from A and B separately?`

Potential analyses:
- additive vs super-additive degradation;
- robustness ranking reversals;
- interaction terms;
- failure threshold surfaces;
- recovery time under burst + visual degradation.

This is more informative than merely averaging multiple corruption scores.

## 6. P0.4 boundary

No novelty claim is authorized here.

P0.6 must determine:
- realistic network→decoded-video mappings;
- codec/buffering/recovery behavior;
- plausible packet-loss/jitter regimes.

P0.7 must then stress-test the final intersection against all retained literature.
