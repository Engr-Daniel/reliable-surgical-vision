# Monitor Feature and Leakage Specification (P1.4)

**Status:** v1.0 (2026-11-12). Pre-registered with [`preregistration.md`](preregistration.md).  
All features are computed **causally**: at 1-fps step *t*, only information available at the receiver up to display tick *t*. Window *W* ∈ {0.5, 1, 2} s, trailing.

## 1. V0 — model-internal (computed from the phase model's outputs)
| Feature | Definition |
|---|---|
| `msp` | max softmax probability at *t* (temperature-scaled on Cholec80 33–40, clean) |
| `entropy` | predictive entropy at *t* |
| `margin` | top-1 minus top-2 probability |
| `change_rate_W` | fraction of steps in *W* where the argmax changed |
| `run_len` | steps since last argmax change |
| `kl_prev` | KL(p_t ‖ p_{t−1}) |
| `ens_disagree` | for M1 only: pairwise disagreement across 5 TCN heads trained with different seeds (cheap ensemble) |

## 2. V1 — decoded-video (pixels only, no metadata)
| Feature | Definition |
|---|---|
| `freeze_px` | 1 if the frame at *t* is pixel-identical (or mean abs diff < 0.5 grey levels) to the previous display tick; and `freeze_px_W`, its fraction over *W* at 25 Hz |
| `blockiness`, `blur_lap_var`, `niqe` | no-reference quality: 8×8 blocking measure, variance of Laplacian, NIQE |
| `flow_mag`, `flow_residual` | Farnebäck optical-flow magnitude and warping residual between consecutive ticks (temporal discontinuity) |
| `feat_drift` | cosine distance between consecutive phase-model backbone embeddings |
| `q2err` | **learned frame-quality → error predictor:** a small CNN (MobileNetV3-S) trained on training folds to predict `F_t` from the decoded frame and its predecessor alone. Added after P1.1, because learned pixel→AI-accuracy predictors are established (DAO, machine-vision-aware quality metrics) |

**Requirement:** V1 must detect pixel-visible freezes (`freeze_px`). This prevents the network side from "winning" merely by reporting something already visible.

## 3. N1 — network (receiver-side transport statistics)
| Feature | Definition |
|---|---|
| `loss_frac_W` | RTP sequence gaps / expected packets over *W* |
| `burst_len_max_W`, `burst_count_W` | from sequence-number gap runs |
| `jitter_ms` | RFC 3550 inter-arrival jitter (RTCP) |
| `rtt_ms` | RTCP RTT estimate (last report) |
| `recv_kbps_W` | received payload bitrate over *W* |
| `ts_since_rtcp` | time since last RTCP report (staleness) |

## 4. N2 — transport / decoder state
| Feature | Definition |
|---|---|
| `jb_latency_ms`, `jb_late_W`, `jb_lost_W` | jitter-buffer state |
| `rtx_req_W`, `rtx_ok_frac_W` | NACK/RTX requests and recovery rate |
| `decode_err_W`, `concealed_frac` | decoder error/concealment indicators |
| `frames_since_new` | display ticks since the last newly decoded frame (decoder-reported) |
| `e2e_delay_ms` | display − capture timestamp |
| `since_keyframe` | ticks since the last received IDR frame (error-propagation horizon) |

## 5. Leakage controls (verified by unit tests in Phase 2)
1. **No emulator ground truth.** Features may read only the receiver log (`pipeline-spec.md` §5). The run manifest (`netem_*`, tier ID) is stored separately, and the feature code has no path to it. Test: the feature extractor runs with the manifest directory absent.
2. **No tier identity.** Neither `condition_id` nor any constant-per-tier value configured by the experimenter is a feature. Test: permuting tier labels leaves every feature unchanged.
3. **No future information.** Every feature at *t* uses ticks ≤ *t*. Test: truncating the log at *t* yields identical features at *t*.
4. **No label leakage across folds.** Monitors, the `q2err` predictor and Mondrian strata thresholds are fit on training folds only. Test: fold IDs per procedure are asserted disjoint.
5. **No source-frame leakage.** `src_frame_idx` is used only to join labels. Test: removing it from the feature table changes no feature.
6. **Mondrian strata (RQ2):** tertile cut-points of `loss_frac_W` and `frames_since_new` are fit on training folds. Strata with < 1,500 frames or < 4 procedures are merged with the adjacent stratum in loss-first order.

## 6. Monitor inputs per comparison
| Monitor | Inputs |
|---|---|
| A (video-only) | V0 + V1 |
| B (full) | V0 + V1 + N1 + N2 |
| Ablations | V0 only; V0+N1; V0+N2; N1+N2 only |

All continuous features are standardised on training folds. Missing RTCP-derived values (no report yet) are carried forward, with an indicator.
