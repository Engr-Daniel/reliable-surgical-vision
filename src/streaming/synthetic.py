"""Synthetic test video with a frame-index barcode (pipeline validation only).

Each frame carries its source index as a 16-bit barcode of large black/white blocks in
the top band. The blocks survive H.264 compression and downscaling, so the receiver can
read the true source index from pixels and check the RTP-timestamp-based mapping that
is used for real surgical video (pipeline-spec §6, validation (c)).
"""
from __future__ import annotations

import numpy as np

W, H = 854, 480
BITS = 16
BLOCK = 40  # px
BAND_Y0, BAND_Y1 = 8, 8 + BLOCK
X0 = 107  # centres 16 blocks of 40 px in 854 px


def make_frame(idx: int, rng_seed: int = 0) -> np.ndarray:
    """BGR uint8 frame: moving textured background + barcode band."""
    yy, xx = np.mgrid[0:H, 0:W]
    t = idx / 25.0
    bg = (127 + 60 * np.sin(2 * np.pi * (xx / 97.0 + t * 0.7)) * np.cos(2 * np.pi * (yy / 71.0 - t * 0.4)))
    blob = 80 * np.exp(-(((xx - (W / 2 + 250 * np.sin(t))) ** 2 + (yy - (H / 2 + 120 * np.cos(1.3 * t))) ** 2) / (2 * 45.0 ** 2)))
    g = np.clip(bg + blob, 0, 255).astype(np.uint8)
    frame = np.stack([g, np.roll(g, 7, 1), np.roll(g, 13, 0)], axis=2)
    frame[0:BAND_Y1 + 8, :] = 128
    for b in range(BITS):
        bit = (idx >> (BITS - 1 - b)) & 1
        x = X0 + b * BLOCK
        frame[BAND_Y0:BAND_Y1, x:x + BLOCK] = 255 if bit else 0
    return frame


def read_barcode(frame_bgr: np.ndarray) -> int:
    """Recover the source index from a decoded frame (full 854x480 resolution)."""
    g = frame_bgr[..., 0] if frame_bgr.ndim == 3 else frame_bgr
    val = 0
    for b in range(BITS):
        x = X0 + b * BLOCK
        cell = g[BAND_Y0 + 8:BAND_Y1 - 8, x + 8:x + BLOCK - 8]
        val = (val << 1) | int(cell.mean() > 128)
    return val
