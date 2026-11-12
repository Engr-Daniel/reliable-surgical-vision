"""RTP/H.264 receiver with receiver-side logging (pipeline-spec §4–5).

Writes three receiver-observable logs (no emulator ground truth is available here):
  packets.csv  one row per RTP packet arriving at the jitter buffer:
               arrival_s (receiver monotonic), seq, rtp_ts, bytes
  frames.csv   one row per decoded frame: arrival_s, pts_ns, rtp_ts, src_idx (= rtp_ts / 3600),
               barcode_idx (synthetic source only; -1 otherwise)
  jb.csv       jitter-buffer stats sampled every 40 ms
  decoder_events.csv  decoder warnings/errors with time
Optionally saves 160x90 grey thumbnails of decoded frames (thumbs.npy) for V1 features.
"""
from __future__ import annotations

import argparse
import csv
import os
import time

import gi

gi.require_version("Gst", "1.0")
gi.require_version("GstRtp", "1.0")
from gi.repository import GLib, Gst, GstRtp  # noqa: E402

import numpy as np  # noqa: E402
import cv2  # noqa: E402

from .synthetic import H, W, read_barcode  # noqa: E402

RTP_PER_FRAME = 90000 // 25


def run(port: int, outdir: str, duration: float, jb_latency_ms: int = 100, synthetic: bool = True,
        thumbs: bool = True):
    Gst.init(None)
    os.makedirs(outdir, exist_ok=True)
    caps = "application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96"
    pipe = Gst.parse_launch(
        f"udpsrc port={port} caps=\"{caps}\" buffer-size=4194304 ! "
        f"rtpjitterbuffer name=jb latency={jb_latency_ms} drop-on-latency=false ! "
        f"rtph264depay name=depay ! h264parse ! avdec_h264 name=dec ! "
        f"videoconvert ! video/x-raw,format=BGRx,width={W},height={H} ! "
        f"appsink name=sink emit-signals=true sync=false max-buffers=200 drop=false"
    )
    t_ref = time.monotonic()
    pk_f = open(os.path.join(outdir, "packets.csv"), "w", newline="")
    fr_f = open(os.path.join(outdir, "frames.csv"), "w", newline="")
    jb_f = open(os.path.join(outdir, "jb.csv"), "w", newline="")
    ev_f = open(os.path.join(outdir, "decoder_events.csv"), "w", newline="")
    pk, fr, jbw, ev = csv.writer(pk_f), csv.writer(fr_f), csv.writer(jb_f), csv.writer(ev_f)
    pk.writerow(["arrival_s", "seq", "rtp_ts", "bytes"])
    fr.writerow(["arrival_s", "pts_ns", "rtp_ts", "src_idx", "barcode_idx"])
    jbw.writerow(["t_s", "num_pushed", "num_lost", "num_late", "num_duplicates", "avg_jitter_ns",
                  "rtx_count", "rtx_success_count"])
    ev.writerow(["t_s", "type", "source", "message"])
    pts_to_rtp: dict[int, int] = {}
    thumbs_list = []

    def on_packet(pad, info):
        buf = info.get_buffer()
        ok, rtp = GstRtp.RTPBuffer.map(buf, Gst.MapFlags.READ)
        if ok:
            pk.writerow([f"{time.monotonic() - t_ref:.6f}", rtp.get_seq(), rtp.get_timestamp(), buf.get_size()])
            rtp.unmap()
        return Gst.PadProbeReturn.OK

    def on_depay(pad, info):
        buf = info.get_buffer()
        ok, rtp = GstRtp.RTPBuffer.map(buf, Gst.MapFlags.READ)
        if ok:
            pts_to_rtp[buf.pts] = rtp.get_timestamp()
            rtp.unmap()
        return Gst.PadProbeReturn.OK

    jb = pipe.get_by_name("jb")
    jb.get_static_pad("sink").add_probe(Gst.PadProbeType.BUFFER, on_packet)
    pipe.get_by_name("depay").get_static_pad("sink").add_probe(Gst.PadProbeType.BUFFER, on_depay)

    def on_sample(sink):
        s = sink.emit("pull-sample")
        buf = s.get_buffer()
        now = time.monotonic() - t_ref
        rtp_ts = pts_to_rtp.pop(buf.pts, -1)
        ok, m = buf.map(Gst.MapFlags.READ)
        bc = -1
        if ok:
            stride = len(m.data) // H
            img = np.ndarray((H, W, 4), np.uint8, m.data, strides=(stride, 4, 1))[..., :3]
            if synthetic:
                bc = read_barcode(img)
            if thumbs:
                thumbs_list.append(cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (160, 90), interpolation=cv2.INTER_AREA))
            buf.unmap(m)
        fr.writerow([f"{now:.6f}", buf.pts, rtp_ts, rtp_ts // RTP_PER_FRAME if rtp_ts >= 0 else -1, bc])
        return Gst.FlowReturn.OK

    pipe.get_by_name("sink").connect("new-sample", on_sample)

    def sample_jb():
        st = jb.get_property("stats")
        get = lambda k: st.get_value(k) if st.has_field(k) else -1
        jbw.writerow([f"{time.monotonic() - t_ref:.6f}", get("num-pushed"), get("num-lost"), get("num-late"),
                      get("num-duplicates"), get("avg-jitter"), get("rtx-count"), get("rtx-success-count")])
        return True

    def on_msg(bus, msg):
        if msg.type in (Gst.MessageType.WARNING, Gst.MessageType.ERROR):
            err, _ = msg.parse_warning() if msg.type == Gst.MessageType.WARNING else msg.parse_error()
            ev.writerow([f"{time.monotonic() - t_ref:.6f}", msg.type.first_value_nick, msg.src.get_name(), err.message])
        return True

    bus = pipe.get_bus()
    bus.add_signal_watch()
    bus.connect("message", on_msg)
    loop = GLib.MainLoop()
    GLib.timeout_add(40, sample_jb)
    GLib.timeout_add(int(duration * 1000), loop.quit)
    pipe.set_state(Gst.State.PLAYING)
    with open(os.path.join(outdir, "receiver_t_ref.txt"), "w") as fh:
        fh.write(f"{t_ref:.9f}\n")
    loop.run()
    pipe.set_state(Gst.State.NULL)
    for f in (pk_f, fr_f, jb_f, ev_f):
        f.close()
    if thumbs and thumbs_list:
        np.save(os.path.join(outdir, "thumbs.npy"), np.stack(thumbs_list))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--duration", type=float, required=True)
    ap.add_argument("--jb-latency", type=int, default=100)
    ap.add_argument("--real-source", action="store_true", help="disable barcode readout")
    a = ap.parse_args()
    run(a.port, a.out, a.duration, a.jb_latency, synthetic=not a.real_source)


if __name__ == "__main__":
    main()
