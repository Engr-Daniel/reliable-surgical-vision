#!/usr/bin/env python3
"""P2.2 pipeline validation pilot on synthetic barcoded video (no clinical data).

For each condition: start receiver, impairment relay and sender (real GStreamer RTP/H.264
over localhost UDP), then reconstruct the 25 Hz display and compute the pipeline-spec §6
validation checks plus descriptive degradation statistics.

Usage (repo root, inside the project venv):
    python scripts/run_pipeline_pilot.py --conds T0,T1,T2,T3,T4,T5 --seconds 40 \
        --raw /tmp/pilot_raw --out experiments/pilots/pipeline-synthetic
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

import cv2
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.features.receiver_features import n1_features, n2_features, v1_features  # noqa: E402
from src.network.gilbert_elliott import burst_lengths  # noqa: E402
from src.network.tiers import ALL  # noqa: E402
from src.streaming.display import display_ticks  # noqa: E402
from src.streaming.synthetic import make_frame  # noqa: E402

PY = sys.executable
PLAYOUT_MS = 80.0  # fixed display playout margin (pipeline-spec §4), calibrated on T0


def run_condition(cid: str, seconds: int, raw: str, seed: int, base_port: int) -> str:
    cond = ALL[cid]
    d = os.path.join(raw, cid)
    os.makedirs(d, exist_ok=True)
    frames = seconds * 25
    tail = 4 + (cond.delay_ms + 4 * cond.jitter_ms) / 1000.0
    dur = seconds + tail + 2
    lp, rp = base_port, base_port + 2
    env = dict(os.environ, PYTHONPATH=ROOT)
    rx = subprocess.Popen([PY, "-m", "src.streaming.receiver", "--port", str(rp), "--out", os.path.join(d, "rx"),
                           "--duration", f"{dur:.1f}"], cwd=ROOT, env=env)
    relay = subprocess.Popen([PY, "-m", "src.network.relay", "--cond", cid, "--seed", str(seed), "--listen", str(lp),
                              "--target", str(rp), "--fate-csv", os.path.join(d, "manifest", "fate.csv"),
                              "--duration", f"{dur:.1f}"], cwd=ROOT, env=env)
    time.sleep(1.5)
    subprocess.run([PY, "-m", "src.streaming.sender", "--port", str(lp), "--kbps", str(cond.encoder_kbps),
                    "--frames", str(frames), "--manifest", os.path.join(d, "manifest", "sender.json")],
                   cwd=ROOT, env=env, check=True)
    rx.wait()
    relay.wait()
    return d


def psnr(a, b):
    mse = np.mean((a.astype(float) - b.astype(float)) ** 2)
    return 99.0 if mse == 0 else 10 * np.log10(255 ** 2 / mse)


def analyse(cid: str, d: str, src_thumbs: np.ndarray) -> dict:
    cond = ALL[cid]
    fate = pd.read_csv(os.path.join(d, "manifest", "fate.csv"))
    sender = json.load(open(os.path.join(d, "manifest", "sender.json")))
    rxd = os.path.join(d, "rx")
    frames = pd.read_csv(os.path.join(rxd, "frames.csv"))
    packets = pd.read_csv(os.path.join(rxd, "packets.csv"))
    jb = pd.read_csv(os.path.join(rxd, "jb.csv"))
    ev = pd.read_csv(os.path.join(rxd, "decoder_events.csv"))
    t_ref = float(open(os.path.join(rxd, "receiver_t_ref.txt")).read())
    thumbs = np.load(os.path.join(rxd, "thumbs.npy"))
    n_sent = sender["frames_sent"]
    # analysis window ends at the last decoded frame: the final frames still inside the
    # decoder when the receiver stops are an end-of-stream artefact, not a network effect
    ticks = display_ticks(frames, n_ticks=None, playout_ms=PLAYOUT_MS,
                          sender_t0=sender["sender_t0_monotonic"], receiver_t_ref=t_ref)
    shown = ticks["decoded_row"].to_numpy()
    th_tick = thumbs[np.maximum(shown, 0)]
    # manifest-side ground truth (validation only; never a feature)
    lost = fate["lost_ge"].to_numpy(bool)
    bl = burst_lengths(lost)
    # alignment / stale content
    aligned = (frames["barcode_idx"] == frames["src_idx"]).to_numpy()
    # quality of each displayed frame vs its own source frame (spatial), and vs the frame
    # the tick should show if the stream were on time (spatial + temporal)
    k = ticks["tick"].to_numpy()
    src = ticks["src_idx"].to_numpy()
    psnr_own = np.array([psnr(th_tick[i], src_thumbs[src[i]]) for i in range(len(k)) if src[i] >= 0])
    lag = int(np.nanmedian(k - src))
    ideal = np.clip(k - lag, 0, len(src_thumbs) - 1)
    psnr_ontime = np.array([psnr(th_tick[i], src_thumbs[ideal[i]]) for i in range(len(k)) if src[i] >= 0])
    freeze = ticks["is_freeze_decoder"].to_numpy()
    episodes = int(np.sum(freeze[1:] & ~freeze[:-1]))
    # receiver-side features (sanity: they respond to impairment)
    n1 = n1_features(packets, ticks["t_s"].to_numpy())
    n2 = n2_features(ticks, jb, ev, packets)
    v1 = v1_features(th_tick)
    return {
        "condition": cid, "label": cond.label,
        "cfg_loss_pct": 100 * cond.loss_pe, "realised_ge_loss_pct": 100 * lost.mean(),
        "cfg_burst": cond.loss_burst, "realised_mean_burst": float(bl.mean()) if len(bl) else 0.0,
        "queue_drops": int(fate["dropped_queue"].sum()), "rtp_sent": sender.get("rtp_packets_sent", -1),
        "relay_received": len(fate), "pre_emulator_loss": sender.get("rtp_packets_sent", -1) - len(fate),
        "frames_sent": n_sent, "frames_decoded": len(frames),
        "alignment_pct": 100 * aligned.mean(), "stale_content_pct": 100 * (1 - aligned.mean()),
        "freeze_tick_pct": 100 * freeze.mean(), "freeze_episodes_per_min": episodes / (len(freeze) / 25 / 60),
        "e2e_delay_median_ms": float(np.nanmedian(ticks["e2e_delay_ms"])),
        "e2e_delay_p95_ms": float(np.nanpercentile(ticks["e2e_delay_ms"], 95)),
        "psnr_own_frame_db": float(np.median(psnr_own)), "psnr_on_time_db": float(np.median(psnr_ontime)),
        "decoder_events": len(ev),
        "n1_loss_frac_mean": float(n1["loss_frac_W"].mean()), "n2_jb_lost_mean": float(n2["jb_lost_W"].mean()),
        "v1_freeze_px_mean": float(v1["freeze_px"].mean()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conds", default="T0,T1,T2,T3,T4,T5")
    ap.add_argument("--seconds", type=int, default=40)
    ap.add_argument("--raw", default="/tmp/pilot_raw")
    ap.add_argument("--out", default=os.path.join(ROOT, "experiments", "pilots", "pipeline-synthetic"))
    ap.add_argument("--seed", type=int, default=20261112)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    n = a.seconds * 25
    src_thumbs = np.stack([cv2.resize(cv2.cvtColor(make_frame(i), cv2.COLOR_BGR2GRAY), (160, 90),
                                      interpolation=cv2.INTER_AREA) for i in range(n)])
    rows = []
    for j, cid in enumerate(a.conds.split(",")):
        d = run_condition(cid, a.seconds, a.raw, a.seed + j, 6000 + 10 * j)
        rows.append(analyse(cid, d, src_thumbs))
        print(json.dumps(rows[-1]), flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(a.out, "summary.csv"), index=False, float_format="%.4g")
    print("wrote", os.path.join(a.out, "summary.csv"))


if __name__ == "__main__":
    main()
