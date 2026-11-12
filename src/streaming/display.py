"""Offline display-clock reconstruction (pipeline-spec §4).

The receiver logs when each decoded frame became available. A display running at a fixed
25 Hz shows, at tick k, the newest decoded frame available by the tick time. If no new
frame arrived since the previous tick, the previous frame is held (a freeze).

Doing this offline from the decode log is deterministic and testable, and identical to a
live 25 Hz display that always shows the newest available frame.

Tick 0 is placed at the arrival time of the first decoded frame plus ``playout_ms``.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

FPS = 25


def display_ticks(frames: pd.DataFrame, n_ticks: int | None = None, playout_ms: float = 0.0,
                  sender_t0: float | None = None, receiver_t_ref: float | None = None) -> pd.DataFrame:
    """Return one row per display tick.

    Columns: tick, t_s, src_idx (displayed frame; -1 before first frame), new_frame,
    is_freeze_decoder, frames_since_new, e2e_delay_ms (if clocks given), decoded_row
    (row index into ``frames``, -1 if none).
    """
    f = frames.reset_index(drop=True)
    arr = f["arrival_s"].to_numpy(float)
    if len(arr) == 0:
        raise ValueError("no decoded frames")
    t0 = arr[0] + playout_ms / 1000.0
    if n_ticks is None:
        n_ticks = int(np.floor((arr[-1] - t0) * FPS)) + 1
    t = t0 + np.arange(n_ticks) / FPS
    # newest decoded frame with arrival <= tick time
    row = np.searchsorted(arr, t, side="right") - 1
    src = np.where(row >= 0, f["src_idx"].to_numpy()[np.maximum(row, 0)], -1)
    new = np.r_[row[0] >= 0, row[1:] != row[:-1]]
    since = np.zeros(n_ticks, int)
    for k in range(1, n_ticks):
        since[k] = 0 if new[k] else since[k - 1] + 1
    out = pd.DataFrame({"tick": np.arange(n_ticks), "t_s": t, "src_idx": src, "new_frame": new,
                        "is_freeze_decoder": ~new, "frames_since_new": since, "decoded_row": row})
    if sender_t0 is not None and receiver_t_ref is not None:
        capture_abs = sender_t0 + out["src_idx"].to_numpy() / FPS
        display_abs = receiver_t_ref + t
        out["e2e_delay_ms"] = np.where(src >= 0, (display_abs - capture_abs) * 1000.0, np.nan)
    return out
