"""Receiver-observable monitor features N1, N2 and pixel-only V1 (feature-spec v1.0).

Every function takes only receiver logs (packets.csv, jb.csv, decoder_events.csv, display
ticks, thumbnails). None of them can read the run manifest or emulator fate table: the
leakage tests in ``tests/test_features.py`` call them with the manifest absent.

All features are causal: the value at tick k depends only on data with time <= t_k.
Windows W are trailing, in seconds.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

FPS = 25
RTP_PER_FRAME = 90000 // FPS


# ---------------------------------------------------------------- N1 (network)
def n1_features(packets: pd.DataFrame, tick_t: np.ndarray, window_s: float = 1.0) -> pd.DataFrame:
    """Loss, burst, inter-arrival jitter and bitrate from packet arrivals only."""
    p = packets.sort_values("arrival_s").reset_index(drop=True)
    t = p["arrival_s"].to_numpy(float)
    seq = p["seq"].to_numpy(np.int64)
    # unwrap 16-bit sequence numbers
    seq = np.r_[seq[0], seq[0] + np.cumsum(((np.diff(seq) + 32768) % 65536) - 32768)] if len(seq) else seq
    # reorder-robust loss accounting: a packet advancing the highest sequence number seen
    # opens a gap of (advance - 1); a late packet (seq below the running maximum) closes one.
    run_max = np.maximum.accumulate(seq) if len(seq) else seq
    prev_max = np.r_[seq[0] - 1, run_max[:-1]] if len(seq) else seq
    opens = np.maximum(seq - prev_max - 1, 0)
    closes = (seq < prev_max).astype(int)
    gap = opens - closes  # net change in outstanding missing packets at this arrival
    # RFC 3550 interarrival jitter (ms), computed causally per packet
    ts = p["rtp_ts"].to_numpy(float) / 90000.0
    d = np.r_[0.0, np.abs(np.diff(t) - np.diff(ts))]
    j = np.zeros(len(t))
    for i in range(1, len(t)):
        j[i] = j[i - 1] + (d[i] - j[i - 1]) / 16.0
    nbytes = p["bytes"].to_numpy(float)
    out = {k: np.zeros(len(tick_t)) for k in ["loss_frac_W", "burst_len_max_W", "burst_count_W", "jitter_ms",
                                               "recv_kbps_W", "ts_since_packet"]}
    for k, tk in enumerate(tick_t):
        hi = np.searchsorted(t, tk, side="right")
        lo = np.searchsorted(t, tk - window_s, side="left")
        g = gap[lo:hi]
        o = opens[lo:hi]
        recv = hi - lo
        missing = max(int(g.sum()), 0)
        out["loss_frac_W"][k] = missing / (recv + missing) if recv + missing > 0 else 0.0
        out["burst_len_max_W"][k] = o.max() if len(o) else 0
        out["burst_count_W"][k] = np.count_nonzero(o)
        out["jitter_ms"][k] = j[hi - 1] * 1000.0 if hi > 0 else 0.0
        out["recv_kbps_W"][k] = nbytes[lo:hi].sum() * 8 / 1000.0 / window_s
        out["ts_since_packet"][k] = tk - t[hi - 1] if hi > 0 else window_s
    return pd.DataFrame(out)


# ---------------------------------------------------------------- N2 (transport / decoder)
def n2_features(ticks: pd.DataFrame, jb: pd.DataFrame, events: pd.DataFrame, packets: pd.DataFrame,
                window_s: float = 1.0) -> pd.DataFrame:
    tick_t = ticks["t_s"].to_numpy(float)
    jt = jb["t_s"].to_numpy(float)
    lost = jb["num_lost"].to_numpy(float)
    late = jb["num_late"].to_numpy(float)
    ev_t = np.sort(events["t_s"].to_numpy(float)) if len(events) else np.zeros(0)
    # keyframes are not visible without parsing; approximate "since keyframe" from the RTP
    # marker-free proxy: largest packet bursts per frame are IDR frames (size >> P frames)
    p = packets.sort_values("arrival_s")
    fsize = p.groupby("rtp_ts")["bytes"].sum()
    farr = p.groupby("rtp_ts")["arrival_s"].min()
    big = fsize > 3 * fsize.rolling(50, min_periods=5).median().shift(1).bfill()
    key_t = np.sort(farr[big[big].index].to_numpy()) if big.any() else np.zeros(0)
    out = {k: np.zeros(len(tick_t)) for k in ["jb_lost_W", "jb_late_W", "decode_err_W", "since_keyframe_s"]}
    for k, tk in enumerate(tick_t):
        i_hi = np.searchsorted(jt, tk, side="right") - 1
        i_lo = np.searchsorted(jt, tk - window_s, side="right") - 1
        if i_hi >= 0:
            base = 0 if i_lo < 0 else i_lo
            out["jb_lost_W"][k] = lost[i_hi] - lost[base]
            out["jb_late_W"][k] = late[i_hi] - late[base]
        out["decode_err_W"][k] = np.searchsorted(ev_t, tk, "right") - np.searchsorted(ev_t, tk - window_s, "left")
        kk = np.searchsorted(key_t, tk, "right") - 1
        out["since_keyframe_s"][k] = tk - key_t[kk] if kk >= 0 else tk
    df = pd.DataFrame(out)
    df["frames_since_new"] = ticks["frames_since_new"].to_numpy()
    df["freeze_frac_W_decoder"] = (ticks["is_freeze_decoder"].astype(float)
                                   .rolling(int(window_s * FPS), min_periods=1).mean().to_numpy())
    if "e2e_delay_ms" in ticks:
        df["e2e_delay_ms"] = ticks["e2e_delay_ms"].to_numpy()
    return df


# ---------------------------------------------------------------- V1 (pixels only)
def v1_features(thumbs_per_tick: np.ndarray, window_s: float = 1.0) -> pd.DataFrame:
    """Pixel-only cues from grey thumbnails of the displayed frame at each tick."""
    import cv2

    n = len(thumbs_per_tick)
    x = thumbs_per_tick.astype(np.float32)
    mad = np.r_[np.inf, np.abs(np.diff(x, axis=0)).mean(axis=(1, 2))]
    freeze_px = mad < 0.5
    blur = np.array([cv2.Laplacian(f, cv2.CV_32F).var() for f in x])

    def blockiness(f):
        # mean abs step across 8-px boundaries relative to within-block steps (thumbnail scale ~ 1/5)
        dh = np.abs(np.diff(f, axis=1))
        return float(dh.mean())

    blk = np.array([blockiness(f) for f in x])
    df = pd.DataFrame({"freeze_px": freeze_px.astype(float), "mad_prev": np.where(np.isfinite(mad), mad, 0.0),
                       "blur_lap_var": blur, "grad_energy": blk})
    df["freeze_px_W"] = df["freeze_px"].rolling(int(window_s * FPS), min_periods=1).mean()
    return df
