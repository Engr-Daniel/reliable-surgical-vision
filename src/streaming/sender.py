"""RTP/H.264 sender (pipeline-spec §3).

Frames are pushed into ``appsrc`` with PTS = idx / 25 s. ``rtph264pay`` uses
timestamp-offset=0, so the RTP timestamp of frame ``idx`` is ``idx * 3600`` (90 kHz clock).
This is the in-band frame identity the receiver uses to align decoded frames to labels.

Sources: ``synthetic`` (barcoded test video) or a video file (decoded by OpenCV, resized
to 854x480; the dataset's native 25 fps is required).
"""
from __future__ import annotations

import argparse
import json
import os
import time

import gi

gi.require_version("Gst", "1.0")
from gi.repository import Gst  # noqa: E402

import cv2  # noqa: E402
import numpy as np  # noqa: E402

from .synthetic import H, W, make_frame  # noqa: E402

FPS = 25


def frames(source: str, n: int | None):
    if source == "synthetic":
        for i in range(n):
            yield i, make_frame(i)
        return
    cap = cv2.VideoCapture(source)
    if abs(cap.get(cv2.CAP_PROP_FPS) - FPS) > 0.5:
        raise ValueError(f"{source}: expected native {FPS} fps")
    i = 0
    while n is None or i < n:
        ok, f = cap.read()
        if not ok:
            break
        yield i, cv2.resize(f, (W, H), interpolation=cv2.INTER_AREA)
        i += 1


def build(port: int, kbps: int, gop: int):
    desc = (
        f"appsrc name=src is-live=true format=time do-timestamp=false "
        f"caps=video/x-raw,format=BGRx,width={W},height={H},framerate={FPS}/1 ! "
        f"videoconvert ! video/x-raw,format=I420 ! "
        f"x264enc tune=zerolatency speed-preset=veryfast bitrate={kbps} key-int-max={gop} bframes=0 "
        f"option-string=\"nal-hrd=cbr:vbv-maxrate={kbps}:vbv-bufsize={kbps // 2}\" ! "
        f"video/x-h264,profile=constrained-baseline ! "
        f"rtph264pay mtu=1200 config-interval=1 pt=96 timestamp-offset=0 seqnum-offset=0 ! "
        f"identity name=count ! udpsink host=127.0.0.1 port={port} sync=false async=false buffer-size=8388608"
    )
    return Gst.parse_launch(desc)


def run(source: str, port: int, kbps: int, n: int | None, manifest: str, gop: int = 25):
    Gst.init(None)
    pipe = build(port, kbps, gop)
    src = pipe.get_by_name("src")
    n_rtp = [0]

    def _count(pad, info):
        if info.type & Gst.PadProbeType.BUFFER_LIST:
            n_rtp[0] += info.get_buffer_list().length()
        else:
            n_rtp[0] += 1
        return Gst.PadProbeReturn.OK

    pipe.get_by_name("count").get_static_pad("src").add_probe(
        Gst.PadProbeType.BUFFER | Gst.PadProbeType.BUFFER_LIST, _count)
    pipe.set_state(Gst.State.PLAYING)
    t0 = time.monotonic()
    sent = 0
    for i, f in frames(source, n):
        target = t0 + i / FPS
        delay = target - time.monotonic()
        if delay > 0:
            time.sleep(delay)
        # BGRx (4 bytes/pixel): rows are never padded, unlike 3-byte BGR at odd widths
        bgrx = np.empty((H, W, 4), np.uint8)
        bgrx[..., :3] = f
        bgrx[..., 3] = 255
        buf = Gst.Buffer.new_wrapped(bgrx.tobytes())
        buf.pts = i * Gst.SECOND // FPS
        buf.duration = Gst.SECOND // FPS
        src.emit("push-buffer", buf)
        sent += 1
    src.emit("end-of-stream")
    pipe.get_bus().timed_pop_filtered(5 * Gst.SECOND, Gst.MessageType.EOS | Gst.MessageType.ERROR)
    pipe.set_state(Gst.State.NULL)
    os.makedirs(os.path.dirname(os.path.abspath(manifest)), exist_ok=True)
    with open(manifest, "w") as fh:
        json.dump({"sender_t0_monotonic": t0, "frames_sent": sent, "rtp_packets_sent": n_rtp[0], "fps": FPS, "kbps": kbps, "gop": gop,
                   "source": source, "gst": Gst.version_string()}, fh, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="synthetic")
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--kbps", type=int, required=True)
    ap.add_argument("--frames", type=int, default=None)
    ap.add_argument("--gop", type=int, default=25)
    ap.add_argument("--manifest", required=True)
    a = ap.parse_args()
    run(a.source, a.port, a.kbps, a.frames, a.manifest, a.gop)


if __name__ == "__main__":
    main()
