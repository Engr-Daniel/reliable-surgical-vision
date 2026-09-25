# P0.4 Source Audit

## Audit decision

P0.4 is **complete at the focused distribution-shift reconnaissance level**.

The literature is sufficient to answer:
- what natural shifts are documented;
- what controlled corruptions have direct surgical precedent;
- what mitigation families exist;
- what evaluation practices are defensible;
- where temporal/network-style evidence is mature versus emerging.

P0.4 does not claim an exhaustive systematic review and does not authorize a final novelty statement.

## Final audit set

- **25 retained sources/resources**
- **10 excluded/deferred categories**
- **35 audit records/categories**

## Coverage assessment

| Area | Coverage | Assessment |
|---|---|---|
| Natural multicentre shift | ROBUST-MIS, MultiBypass140, PhaKIR, hospital transfer, spine external cohorts | Strong |
| Device/instrument/procedure shift | Kitaguchi + recent external cohorts | Strong |
| Surgical visual corruption | SegSTRONG-C, CaRTS/TC-CaRTS | Strong for smoke/blood/low-light; less standardized for other factors |
| Severity calibration | Jaspers adjacent GI endoscopy | Strong methodology precedent, but surgical re-calibration required |
| UDA | teacher–student, graph-based, video-text | Strong representative coverage |
| DG | object-centric, synthetic, single-domain/preprint, diverse training | Strong representative coverage |
| Foundation-model domain robustness | SAM2/domain-agnostic and deployment-realistic detector limits | Emerging–Strong |
| Temporal consistency | workflow volatility/consistency + TC-CaRTS | Strong as temporal modeling evidence |
| Controlled frame-loss/jitter for conventional surgical CV | sparse | Important gap for P0.6 |
| Packet-loss corruption in surgical/endoscopy CV | Endo-C6 2026 | Emerging direct precedent |
| Compound image corruption | adjacent calibrated endoscopy | Existing precedent |
| Visual + mechanistic network/decoded-video compound shift | not established by retained evidence | Must be re-tested in P0.6/P0.7 |

## Key scope correction

Before P0.4, Track A could be read too broadly as “robust surgical vision under visual/network shift.”

P0.4 shows that broad framing is not defensible as a novelty claim:
- cross-centre generalization is already actively benchmarked;
- smoke/blood/low-light robustness is directly benchmarked;
- UDA/DG methods are established;
- compound image corruption already has precedent;
- recent temporal VLM work includes packet-loss corruption.

The research question must therefore survive a **narrower intersection test** in P0.7.

## Negative evidence rule

“No mature standardized benchmark identified” means:
- none was found in the retained P0.4 evidence under the documented search protocol.

It does **not** mean no such paper exists anywhere.

## Gate recommendation

P0.4 can be closed.

Next: **P0.5 — Reliable-Inference Literature Reconnaissance**.
