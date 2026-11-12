import inspect

import numpy as np
import pandas as pd
import pytest

from src.features import receiver_features as rf
from src.streaming.display import display_ticks


def _frames(arrivals, src):
    return pd.DataFrame({"arrival_s": arrivals, "src_idx": src})


def test_display_clock_freeze_and_hold():
    # frames 0..4 arrive on time, frame 5 is 120 ms late, 6.. on time again
    arr = np.array([0.00, 0.04, 0.08, 0.12, 0.16, 0.32, 0.33, 0.36])
    src = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    d = display_ticks(_frames(arr, src), n_ticks=10)
    assert d["src_idx"].tolist()[:6] == [0, 1, 2, 3, 4, 4]          # tick 5 holds frame 4
    assert d["is_freeze_decoder"].tolist()[5:8] == [True, True, True]
    assert d["frames_since_new"].tolist()[5:9] == [1, 2, 3, 0]
    assert d.loc[8, "src_idx"] == 5 and d.loc[9, "src_idx"] == 7     # newest available frame shown (6 skipped)


def test_e2e_delay():
    arr = np.arange(10) * 0.04 + 0.2
    d = display_ticks(_frames(arr, np.arange(10)), sender_t0=100.0, receiver_t_ref=100.0)
    assert np.allclose(d["e2e_delay_ms"], 200.0)


def _packets(n_frames=250, per_frame=4, lose=()):
    rows, seq = [], 0
    for f in range(n_frames):
        for k in range(per_frame):
            if seq not in lose:
                rows.append((f / 25 + k * 1e-4 + 0.05, seq % 65536, f * 3600, 1200))
            seq += 1
    return pd.DataFrame(rows, columns=["arrival_s", "seq", "rtp_ts", "bytes"])


def test_n1_loss_and_bursts():
    lose = set(range(400, 405)) | {600}
    p = _packets(lose=lose)
    tick_t = np.array([9.0])
    f = rf.n1_features(p, tick_t, window_s=10.0)
    expected_total = int(np.floor((9.0 - 0.05) * 25) + 1) * 4  # packets sent by t = 9 s
    assert f.loc[0, "loss_frac_W"] == pytest.approx(6 / expected_total, rel=1e-6)
    assert f.loc[0, "burst_len_max_W"] == 5 and f.loc[0, "burst_count_W"] == 2


def test_n1_sequence_wraparound():
    p = _packets(n_frames=20000, per_frame=4)
    f = rf.n1_features(p, np.array([799.0]), window_s=5.0)
    assert f.loc[0, "loss_frac_W"] == 0.0


def test_features_are_causal():
    """Leakage control 3: truncating logs at t_k leaves the features at tick k unchanged."""
    p = _packets(lose=set(range(300, 310)))
    arr = np.arange(250) / 25 + 0.1
    ticks = display_ticks(_frames(arr, np.arange(250)))
    jb = pd.DataFrame({"t_s": np.arange(0, 10, 0.04), "num_lost": np.arange(250) // 50, "num_late": 0})
    ev = pd.DataFrame({"t_s": [3.0, 6.0]})
    full_n1 = rf.n1_features(p, ticks["t_s"].to_numpy())
    full_n2 = rf.n2_features(ticks, jb, ev, p)
    k = 120
    tk = ticks.loc[k, "t_s"]
    cut = lambda df, col="arrival_s": df[df[col] <= tk]
    n1_k = rf.n1_features(cut(p), ticks["t_s"].to_numpy()[: k + 1])
    n2_k = rf.n2_features(ticks.iloc[: k + 1], cut(jb, "t_s"), cut(ev, "t_s"), cut(p))
    pd.testing.assert_series_equal(full_n1.iloc[k], n1_k.iloc[k], check_names=False)
    cols = [c for c in full_n2.columns if c != "since_keyframe_s"]  # keyframe proxy uses a trailing median
    pd.testing.assert_series_equal(full_n2.loc[k, cols], n2_k.loc[k, cols], check_names=False)


def test_no_manifest_or_tier_inputs():
    """Leakage controls 1–2: feature functions cannot receive emulator ground truth or tier labels."""
    banned = {"fate", "manifest", "cond", "condition", "tier", "netem", "lost_ge", "depart"}
    for fn in (rf.n1_features, rf.n2_features, rf.v1_features):
        params = set(inspect.signature(fn).parameters)
        assert not params & banned, fn.__name__
        src = inspect.getsource(fn)
        assert "fate" not in src and "manifest" not in src


def test_v1_detects_pixel_freeze():
    rng = np.random.default_rng(0)
    th = rng.integers(0, 255, (50, 90, 160)).astype(np.uint8)
    th[20:25] = th[19]  # held frame
    v = rf.v1_features(th)
    assert v["freeze_px"].iloc[20:25].tolist() == [1.0] * 5
    assert v["freeze_px"].iloc[1:19].sum() == 0


def test_n1_reordering_is_not_loss():
    p = _packets(n_frames=100)
    # swap two blocks of packets (reordering only, nothing lost)
    p = pd.concat([p.iloc[:200], p.iloc[210:220], p.iloc[200:210], p.iloc[220:]]).reset_index(drop=True)
    p["arrival_s"] = np.sort(p["arrival_s"].to_numpy())
    f = rf.n1_features(p, np.array([3.9]), window_s=5.0)
    assert f.loc[0, "loss_frac_W"] == 0.0
