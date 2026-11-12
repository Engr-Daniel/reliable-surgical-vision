# Source code

Implementation of the integrated study's pipeline and analysis (Phase 2). Specification: [`research/integrated-study/`](../research/integrated-study/).

| Package | Contents | Spec |
|---|---|---|
| `network/` | Gilbert–Elliott loss (`gilbert_elliott.py`), pre-registered conditions T0–T5 + RQ3 (`tiers.py`), seeded impairment model (`impairment.py`), live UDP relay (`relay.py`), kernel NetEm command builder (`netem.py`) | pipeline-spec §2 |
| `streaming/` | GStreamer RTP/H.264 sender and receiver with receiver-side logging; offline 25 Hz display clock; synthetic barcoded test video | pipeline-spec §3–5 |
| `features/` | Receiver-observable monitor features N1, N2 and pixel-only V1 (V0 and the learned V1 predictor need the phase models) | feature-spec |
| `evaluation/` | AUROC (weighted, tie-exact), AURC, ECE/NLL/Brier, sustained-failure events, procedure-level BCa bootstrap, Holm, pre-registered interpretation bands, cross-fitting folds | preregistration §6–8 |
| `uncertainty/` | Split conformal APS/RAPS and Mondrian (stratum-conditional) calibration; stratum merging rule | preregistration §7.2 |
| `models/`, `shifts/` | Reserved: phase-model wrappers (P2.3) and Level-A visual shifts | — |

## Environment
```bash
# system packages: see the header of ../requirements.txt
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q tests/          # 38 tests, ~3 s, no data needed
```

## Rules enforced in code
- Feature functions accept only receiver logs. Emulator ground truth (`manifest/fate.csv`) and tier labels cannot be passed to them, and tests check this (`tests/test_features.py`).
- Every feature at tick *k* is causal. A truncation test checks this.
- Impairment is a pure function of (seed, arrival times, packet sizes); a determinism test checks this.
- Tier parameters in `network/tiers.py` mirror the pre-registration; a test pins them.
- External model code (TeCNO, GPL-3.0; Surgformer, CC BY-NC 4.0) is **not vendored** here.
