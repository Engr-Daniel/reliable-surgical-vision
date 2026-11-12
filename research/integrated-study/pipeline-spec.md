# Media-Pipeline Specification (P1.3)

**Status:** specification v1.0 (2026-11-12). Not yet implemented; implementation is a Phase 2 task.  
**Principle:** expose the full network → transport → codec → decoder pathway (P0.6 "Level B"), and log at the **receiver** only what a deployed system could observe.

## 1. Reuse decision
| Candidate | Finding (2026-11-12) | Decision |
|---|---|---|
| VISTA (IX01) | Repository `Dzxx623/VISTA` (MIT, commit `7029edd`, 2026-04-16) contains only a README and CAD files for a tool mount. **The streaming pipeline is not released**, although the paper says it is | Reuse VISTA's **published tier parameters and design choices** (forward-path-only impairment, Gilbert–Elliott loss, per-frame IDs/timestamps, freeze logging) with citation. Build the pipeline independently |
| NetFI (IX02) | Command-path fault injector; video not impaired | Borrow trace-informed loss/delay model ideas for a sensitivity factor only |
| Generic WebRTC stacks | Congestion control and adaptive bitrate add confounds; harder to instrument | Not used in the primary analysis |

## 2. Topology
```
[sender ns]                        [netem link]                   [receiver ns]
file → decode → x264enc → RTP pay → veth0 ──tc netem (fwd)──► veth1 → rtpbin/jitterbuffer → RTP depay → avdec_h264 → frame clock → logger/model tap
                     ▲  RTCP/NACK ◄──────── reverse path (unimpaired) ◄─────────┘
```
- Two Linux network namespaces joined by a veth pair. `tc qdisc ... netem` is applied on the **sender-side egress** only (forward video path). The reverse RTCP/NACK path is unimpaired, matching VISTA's control-path isolation.
- Bandwidth: `tc tbf` (or netem `rate`) chained before netem delay/loss.
- Loss: netem `loss gemodel p r [1-h [1-k]]`, with p and r derived from (pE, mean burst) via the Gilbert–Elliott relations, as in VISTA.
- Delay/jitter: netem `delay D J distribution normal`. Reordering is disabled unless explicitly a factor.

## 3. Sender
| Item | Setting (primary) | Notes |
|---|---|---|
| Source | Original dataset video, native 25 fps; resolution normalised to 854×480 for Cholec80 (its common release size), PhaKIR downscaled from 1080p to 854×480 | Resolution fixed so that bitrate tiers mean the same thing across datasets |
| Encoder | GStreamer `x264enc` (libx264), `tune=zerolatency`, `speed-preset=veryfast`, CBR at min(tier bandwidth × 0.8, 8 Mbps) | Encoder rate follows the bandwidth cap. ABR is **disabled** (fixed per tier) to avoid controller confounds |
| GOP | `key-int-max=25` (1 s), no B-frames | Primary. GOP 50 is a sensitivity factor (P0.6 OQ3) |
| Packetisation | `rtph264pay mtu=1200 config-interval=1` (RFC 6184) | Matches VISTA's 1,200-byte payload |
| Frame identity | RTP header extension carrying a 32-bit source frame index + 64-bit capture timestamp (`rtphdrext`) | Lets each decoded frame be mapped to its source frame and ground-truth label |
| Recovery | NACK/RTX on (`rtprtxsend`, RFC 4588); FEC off (primary); ULP-FEC on (secondary factor) | |

## 4. Receiver
| Item | Setting |
|---|---|
| Jitter buffer | `rtpjitterbuffer latency=100 ms do-retransmission=true` (primary); latency 50/200 ms as sensitivity |
| Depay/decode | `rtph264depay ! avdec_h264` (FFmpeg/libavcodec), error concealment default |
| Display clock | Fixed 25 fps output clock. If no new decoded frame is ready at a tick, the **last frame is held** and the tick is flagged as a freeze |
| Model tap | Every 25th display tick (1 fps) goes to the phase model. All ticks go to the V1 feature extractor |

## 5. Per-frame log schema (receiver side)
One row per **display tick** (25 Hz), Parquet, one file per procedure × condition.

| Column | Type | Source | Feature tier |
|---|---|---|---|
| `proc_id`, `condition_id`, `tick` | str/int | run metadata | key (never a feature) |
| `src_frame_idx` | int | RTP header extension of the displayed frame | key / label alignment |
| `capture_ts_ns`, `display_ts_ns` | int | header ext / receiver clock | derives `e2e_delay_ms` (N2) |
| `is_freeze` | bool | display clock: frame repeated | V1 (pixel-detectable) **and** N2 (decoder-reported); see feature-spec |
| `frames_since_new` | int | display clock | N2 |
| `decode_error`, `concealed_mb_frac` | bool/float | decoder callbacks (libavcodec error flags; concealment if exposed) | N2 |
| `jb_latency_ms`, `jb_lost`, `jb_late`, `jb_rtx_requests`, `jb_rtx_success` | float/int | `rtpjitterbuffer` stats (sampled per tick) | N2 |
| `rtp_loss_frac_win`, `rtp_jitter_ms`, `rtt_ms`, `recv_bitrate_kbps` | float | RTCP receiver reports / `rtpbin` session stats (≥ 1 Hz) | N1 |
| `burst_len_cur`, `burst_count_win` | int | receiver sequence-number gaps | N1 |
| `netem_*` | — | emulator configuration | **never logged in this table**. Kept in a separate run manifest that features cannot read |

Ground-truth labels are joined offline on `(proc_id, src_frame_idx)`, never on `tick`.

## 6. Reproducibility
- **Capture once, decode deterministically.** For every run the received RTP packet stream is archived (pcap at the receiver veth). Re-decoding the pcap with pinned decoder versions reproduces the decoded frames bit-exactly. NetEm's random draws are therefore not a reproducibility risk for any analysis downstream of the receiver.
- Each run manifest stores: tier parameters, `tc` command lines, kernel, GStreamer/FFmpeg/x264 versions, git commit, seed, start/end time and the realised loss/burst statistics.
- Container: pinned base image (Phase 2) with GStreamer 1.24.x, FFmpeg 7.x, x264 stable. Exact versions are recorded at implementation.
- Validation checks before any model run: (a) T0 passthrough reproduces source frames up to codec quantisation; (b) realised loss and burst length are within 10% of configured values per tier; (c) frame-index alignment is 100% for non-freeze ticks.

## 7. Compute and storage (estimate)
| Item | Estimate | Basis |
|---|---|---|
| Streaming is real time | 40 test procedures (~38 min mean, ~25 h) × 6 tiers ≈ 150 h stream time | Cholec80 mean duration |
| RQ3 one-factor conditions | 11 conditions × 25 h ≈ 275 h | §7.3 of pre-registration |
| Phase 1 dev / calibration videos 33–40 (clean + tiers for CP) | ≈ 30 h | |
| PhaKIR (8 videos) × 6 tiers | ≈ 40–60 h | |
| **Total stream time** | **≈ 500 h** | |
| Wall-clock with 16 parallel namespace pairs | ≈ 32 h | x264 veryfast at 854×480 ≈ 0.3 core per stream |
| Archived received streams | ≈ 500 h × ≤ 8 Mbps ≈ ≤ 1.8 TB (much less for low tiers) | pcap; decoded frames are not stored |
| Model inference at 1 fps | ≈ 1.8 M frames per model | ResNet-50 / Surgformer; GPU-hours modest |

Real-time streaming is the binding constraint, not GPU compute. Parallel namespaces must be checked for CPU contention, since contention could itself cause late frames. The check: run T0 in parallel and require zero freezes.

## 8. Out of scope
Adaptive bitrate controllers, congestion control (GCC/SCReAM), multipath/failover, command-path impairment, haptics.

---

## 9. Implementation notes (Phase 2, P2.2 — 2026-11-12)
Code: `src/network/`, `src/streaming/`, `src/features/`, `scripts/run_pipeline_pilot.py`; tests in `tests/`.

| Spec item | As implemented | Reason / status |
|---|---|---|
| NetEm backend (§2) | Kept as the production backend (`src/network/netem.py` builds the `tc` commands). **Added a seeded user-space UDP relay** (`src/network/relay.py`), the default for development and CI | The development sandbox has no `sch_netem` kernel module. The relay is bit-reproducible from its seed. The two backends must be cross-checked on one machine with NetEm before production runs |
| Jitter model | Time-correlated: AR(1) per 20 ms slot (φ = 0.8) with the configured SD; FIFO order kept | Independent per-packet jitter with FIFO ordering inflated median delay by about +105 ms at T5 (caught by `tests/test_network.py`) |
| Frame identity (§3) | RTP timestamp with `timestamp-offset=0`: frame *i* ↔ RTP ts *i* × 3600. The RTP header extension is not needed | Simpler and standard. Verified with a pixel barcode: 100% alignment at T0 |
| Raw frame format | `BGRx` into `appsrc` / out of `appsink` | 3-byte BGR rows at 854 px are padded by GStreamer; unpadded pushes produced flat grey video |
| Pre-emulator loss | Sender counts RTP packets (buffer-list aware); the relay socket uses 8 MB buffers; **new validation (d): relay-received = sender-sent** | Python relay socket overflow during keyframe bursts silently dropped about 1.5% of packets *before* the emulator, corrupting the ground-truth fate table |
| N1 loss | Reorder-robust: late packets close earlier gaps | Gap counting alone treated reordering as loss |
| Display clock (§4) | Reconstructed offline from the decode log (`src/streaming/display.py`); **fixed playout margin 80 ms**; analysis window ends at the last decoded frame | Without a margin, normal decode-time jitter produced 10.8% freeze ticks at T0. With it, T0 has none apart from end-of-stream flush |
| Stale content | Measured on synthetic video as the fraction of decoded frames whose barcode ≠ their RTP index | Decoder concealment shows older pixels under loss. This is a pipeline property to report, not an alignment failure |

### Not yet implemented (open P2.2 items)
- **NACK/RTX** (`rtprtxsend`/`rtprtxreceive` via `rtpbin` with RTCP feedback). The primary condition in the pre-registration has RTX on, so **this must be done before any study run.** Current pilot results are RTX-off.
- ULP-FEC secondary factor; jitter-buffer stats for RTX (`rtx-count`, `rtx-success-count` columns exist but stay 0).
- V1: NIQE, optical flow, backbone `feat_drift` and the learned `q2err` predictor (needs the phase model). Implemented so far: `freeze_px`, frame difference, Laplacian variance, gradient energy.
- V0 (needs the phase models, P2.3). N2 decoder concealment fraction (libavcodec does not expose it through `avdec_h264`; decoder warnings are logged instead).
- NetEm cross-check on a host with `sch_netem`.
