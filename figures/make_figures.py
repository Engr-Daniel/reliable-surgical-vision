#!/usr/bin/env python3
"""Generate the programme figures (SVG) used in the README files.

Usage (from repository root):
    python3 figures/make_figures.py

Outputs (overwritten):
    figures/fig1-research-question.svg   - the primary question as a pipeline
    figures/fig2-evidence-landscape.svg  - occupancy of the 26 P0.7 intersection cells
    figures/fig3-track-merge.svg         - Tracks A-C -> integrated study
    figures/fig4-roadmap.svg             - phase roadmap and current position

fig2 is generated from literature/intersection-analysis/intersection-map.csv,
so it stays in sync with the evidence record. All figures are original diagrams.
Palette: blue ordinal ramp for evidence occupancy (validated reference palette),
orange reserved for network/telemetry, ink/grey for structure.
"""
import csv
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "figures")

INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
BLUE, BLUE_D, BLUE_L, BLUE_XL = "#2a78d6", "#1c5cab", "#86b6ef", "#cde2fb"
ORANGE, ORANGE_L = "#eb6834", "#fbe1d6"
AQUA = "#1baf7a"
FONT = "font-family:Inter,Segoe UI,Helvetica,Arial,sans-serif"

STYLE = f"""<style>
 .t{{{FONT};fill:{INK}}} .s{{{FONT};fill:{INK2}}} .m{{{FONT};fill:{MUTED}}}
 .title{{{FONT};font-size:26px;font-weight:700;fill:{INK}}}
 .sub{{{FONT};font-size:15px;fill:{INK2}}}
 .h{{{FONT};font-size:16px;font-weight:700;fill:{INK}}}
 .b{{{FONT};font-size:14px;fill:{INK}}} .bs{{{FONT};font-size:12.5px;fill:{INK2}}}
 .w{{{FONT};font-size:14px;font-weight:700;fill:#ffffff}}
</style>"""


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n{STYLE}\n'
            f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" fill="{INK2}"/></marker>'
            f'<marker id="ao" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" fill="{ORANGE}"/></marker></defs>\n'
            f'<rect width="{w}" height="{h}" fill="{SURF}"/>\n{body}\n</svg>\n')


def text(x, y, s, cls="b", anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" {extra}>{escape(s)}</text>'


def lines(x, y, rows, cls="b", anchor="middle", dy=18):
    return "".join(text(x, y + i * dy, r, cls, anchor) for i, r in enumerate(rows))


def box(x, y, w, h, fill="#ffffff", stroke=INK2, sw=1.5, rx=10, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow(x1, y1, x2, y2, color=INK2, marker="a", dash="", sw=2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{sw}" fill="none" marker-end="url(#{marker})"{d}/>'


# ---------------------------------------------------------------- fig 1
def fig1():
    W, H = 1400, 700
    b = [text(40, 48, "The primary question: does the network know something the pixels don't?", "title"),
         text(40, 76, "Online surgical phase recognition on video delivered through an emulated telesurgical media pipeline (RQ1)", "sub")]
    stages = [("Surgical video", ["Cholec80 / PhaKIR", "native 25 fps"]),
              ("Encoder", ["H.264 (libx264)", "GOP, rate control"]),
              ("Network", ["delay · jitter", "burst loss · capacity"]),
              ("Receiver", ["jitter buffer", "NACK/RTX · FEC"]),
              ("Decoder", ["concealment", "freeze / frame loss"]),
              ("Online phase model", ["causal TCN /", "transformer"])]
    x0, y0, bw, bh, gap = 40, 120, 190, 96, 30
    for i, (name, sub) in enumerate(stages):
        x = x0 + i * (bw + gap)
        net = name == "Network"
        b.append(box(x, y0, bw, bh, fill=ORANGE_L if net else "#ffffff", stroke=ORANGE if net else INK2, sw=2 if net else 1.5))
        b.append(text(x + bw / 2, y0 + 34, name, "h", "middle"))
        b.append(lines(x + bw / 2, y0 + 58, sub, "bs"))
        if i < len(stages) - 1:
            b.append(arrow(x + bw, y0 + bh / 2, x + bw + gap - 2, y0 + bh / 2))
    sx = lambda i: x0 + i * (bw + gap) + bw / 2
    # monitor spans the four source columns (network, receiver, decoder, model)
    mx, my = x0 + 2 * (bw + gap) - 15, 330
    mw, mh = 4 * bw + 3 * gap + 30, 190
    b.append(box(mx, my, mw, mh, fill="#ffffff", stroke=INK, sw=2))
    b.append(text(mx + 20, my + 32, "Reliability monitor", "h"))
    b.append(text(mx + 20, my + 54, "predicts, frame by frame: will the online phase prediction at time t be wrong?", "bs"))
    chips = [(2, "N1", "network telemetry", ORANGE), (3, "N2", "transport / decoder", ORANGE),
             (4, "V1", "decoded frames", BLUE), (5, "V0", "model outputs", BLUE)]
    cw, ch = 150, 54
    for i, code, lab, col in chips:
        cx = sx(i) - cw / 2
        b.append(box(cx, my + 100, cw, ch, fill=col, stroke=col, rx=8))
        b.append(text(cx + cw / 2, my + 123, code, "w", "middle"))
        b.append(f'<text x="{cx + cw / 2}" y="{my + 142}" text-anchor="middle" style="{FONT};font-size:12px;fill:#ffffff">{escape(lab)}</text>')
        orange = col == ORANGE
        b.append(arrow(sx(i), y0 + bh, sx(i), my + 98, col, "ao" if orange else "a", "6 5" if orange else ""))
    b.append(text(sx(2) + (sx(3) - sx(2)) / 2, y0 + bh + 60, "receiver-observable only", "bs", "middle"))
    b.append(text(sx(2) + (sx(3) - sx(2)) / 2, y0 + bh + 78, "(no emulator ground truth)", "bs", "middle"))
    b.append(text(sx(4) + (sx(5) - sx(4)) / 2, y0 + bh + 60, "visible in the received video", "bs", "middle"))
    # outputs
    oy = my + mh + 40
    b.append(arrow(sx(3), my + mh, sx(3), oy - 2))
    b.append(arrow(sx(4), my + mh, sx(4), oy - 2))
    b.append(box(sx(3) - 95, oy, 190, 46, fill=BLUE_XL, stroke=BLUE))
    b.append(text(sx(3), oy + 29, "Accept prediction", "b", "middle"))
    b.append(box(sx(4) - 95, oy, 190, 46, fill="#ffffff", stroke=INK2))
    b.append(text(sx(4), oy + 29, "Defer to surgeon", "b", "middle"))
    # test box
    b.append(box(40, my, 400, mh, fill="#ffffff", stroke=GRID))
    b.append(text(60, my + 34, "The test (H1a / H1b)", "h"))
    b.append(text(60, my + 66, "Video-only monitor:  V0 + V1", "b"))
    b.append(text(60, my + 92, "Full monitor:  V0 + V1 + N1 + N2", "b"))
    b.append(text(60, my + 124, "AUROC gain with CI excluding 0?", "b"))
    b.append(text(60, my + 142 - 4, "(0.02 = smallest effect of interest)", "bs"))
    b.append(text(60, my + 162, "If not → reported as a negative result:", "bs"))
    b.append(text(60, my + 178, "monitor the video, not the network.", "bs"))
    b.append(text(40, H - 40, "Blue: information visible in the received video.  Orange (dashed): network-side information that is not in the pixels.", "bs"))
    b.append(text(40, H - 20, "Secondary questions use the same pipeline: RQ2 conformal/calibration validity, RQ3 degradation mechanism at matched quality.", "bs"))
    return svg(W, H, "\n".join(b), "Pipeline of the primary research question")


# ---------------------------------------------------------------- fig 2
SHORT = {
    "X01": "Segmentation × natural shift", "X02": "Phase × natural shift",
    "X03": "Segmentation × smoke/blood/light", "X04": "Phase × visual corruption",
    "X05": "Compound visual corruption", "X06": "Phase temporal stability",
    "X07": "Packet-loss bursts → surgical VLMs", "X08": "Surgical CV through real codec pipeline",
    "X09": "Network → human operator", "X10": "Compound network → human",
    "X11": "Network → decoded video quality", "X12": "Surgical calibration / UQ",
    "X13": "Surgical OOD / open-set", "X14": "Seg failure monitor + conformal",
    "X15": "Medical selective prediction", "X16": "Phase conformal sets under shift",
    "X17": "Phase risk–coverage under shift", "X18": "Phase calibration across centres",
    "X19": "Phase reliability on network video", "X20": "Network → DNN accuracy (generic)",
    "X21": "Telemetry → QoS forecasting", "X22": "Telemetry → AI failure (any domain)",
    "X23": "Telemetry → surgical AI failure", "X24": "Telemetry-stratified conformal",
    "X25": "Seg failure on network video", "X26": "Real platform telemetry + AI",
}
GROUPS = [("Shift & robustness", ["X01", "X02", "X03", "X04", "X05", "X06", "X07"]),
          ("Reliability methods", ["X12", "X13", "X14", "X15", "X16", "X17", "X18"]),
          ("Network & video", ["X09", "X10", "X11", "X20", "X21", "X08", "X26"]),
          ("Where the programme sits", ["X19", "X22", "X23", "X24", "X25"])]
OCC = {"SATURATED": (BLUE_D, "#ffffff", "Saturated"),
       "OCCUPIED": (BLUE, "#ffffff", "Occupied"),
       "PARTIAL": (BLUE_L, INK, "Partial"),
       "NOT FOUND IN RETAINED EVIDENCE": ("#ffffff", INK, "Not found")}


def fig2():
    rows = {r["cell_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "literature/intersection-analysis/intersection-map.csv")))}
    W, colw, gap, x0 = 1400, 318, 16, 40
    tile_h, y0 = 62, 172
    b = [text(40, 48, "Evidence landscape: 26 intersections, rated against 165 + 14 sources", "title"),
         text(40, 76, "Phase 0 (P0.7) occupancy ratings, updated by the Phase 1 gap-validation search (P1.1). 'Not found' means not found in the retained evidence; it is not a novelty claim.", "sub")]
    # legend
    lx = 40
    for key in ["SATURATED", "OCCUPIED", "PARTIAL", "NOT FOUND IN RETAINED EVIDENCE"]:
        fill, ink, lab = OCC[key]
        stroke = ORANGE if key.startswith("NOT") else fill
        dash = "6 4" if key.startswith("NOT") else ""
        b.append(box(lx, 98, 22, 22, fill=fill, stroke=stroke, sw=2, rx=5, dash=dash))
        b.append(text(lx + 30, 115, lab, "b"))
        lx += 150
    b.append(text(lx + 10, 115, "★ primary question (RQ1)", "b"))
    maxh = 0
    for gi, (gname, ids) in enumerate(GROUPS):
        gx = x0 + gi * (colw + gap)
        b.append(text(gx, y0 - 8, gname, "h"))
        for ti, cid in enumerate(ids):
            r = rows[cid]
            fill, ink, lab = OCC[r["occupancy"]]
            ty = y0 + ti * (tile_h + 10)
            nf = r["occupancy"].startswith("NOT")
            b.append(box(gx, ty, colw, tile_h, fill=fill, stroke=ORANGE if nf else fill, sw=2.5 if cid == "X23" else 2, rx=8, dash="6 4" if nf else ""))
            star = "★ " if cid == "X23" else ""
            b.append(f'<text x="{gx + 14}" y="{ty + 26}" style="{FONT};font-size:14.5px;font-weight:700;fill:{ink}">{escape(star + SHORT[cid])}</text>')
            rr = r["residual_risk"]
            risk = "blocked by data access" if "blocked" in rr else "residual risk " + rr.split(" ")[0]
            meta = f"{cid} · {lab}" + (f" · {risk}" if nf else "")
            b.append(f'<text x="{gx + 14}" y="{ty + 47}" style="{FONT};font-size:12.5px;fill:{ink};opacity:0.85">{escape(meta)}</text>')
            maxh = max(maxh, ty + tile_h)
    b.append(text(40, maxh + 36, "Source: literature/intersection-analysis/intersection-map.csv (full anchors, gaps and implications per cell). Generated by figures/make_figures.py.", "bs"))
    return svg(W, maxh + 60, "\n".join(b), "Occupancy of the 26 research intersections")


# ---------------------------------------------------------------- fig 3
def fig3():
    W, H = 1400, 560
    b = [text(40, 48, "From three provisional tracks to one integrated study", "title"),
         text(40, 76, "Decision of the P0.7 novelty stress-test: no track dropped, none split; one pipeline, one dataset plan, one analysis plan", "sub")]
    tracks = [("Track C · Network-Aware Inference", "PRIMARY", ORANGE,
               ["Open in retained evidence:", "telemetry's incremental value over", "a strong video-only monitor"], "RQ1", "Does telemetry improve failure detection", "and deferral beyond the pixels?"),
              ("Track B · Selective Inference", "NARROWED", BLUE,
               ["Closed: surgical UQ, OOD, abstention,", "conformal as general ideas.", "Survives: reliability audit"], "RQ2", "Do calibration and conformal coverage survive", "network and centre shift?"),
              ("Track A · Compound Shift", "ABSORBED", AQUA,
               ["Closed: smoke/blood, compound,", "packet-loss, multi-network factors.", "Survives: mechanism question"], "RQ3", "Does degradation mechanism matter", "at matched video quality?")]
    for i, (name, status, col, why, rq, q1, q2) in enumerate(tracks):
        y = 120 + i * 140
        b.append(box(40, y, 420, 118, fill="#ffffff", stroke=col, sw=2))
        b.append(text(60, y + 30, name, "h"))
        b.append(box(60, y + 44, 110, 26, fill=col, stroke=col, rx=13))
        b.append(text(115, y + 62, status, "w", "middle"))
        b.append(lines(190, y + 60, why, "bs", "start", 17))
        b.append(arrow(460, y + 59, 568, y + 59, col))
        b.append(box(570, y, 360, 118, fill="#ffffff", stroke=col, sw=2))
        b.append(text(590, y + 36, rq, "title"))
        b.append(text(590, y + 70, q1, "b"))
        b.append(text(590, y + 92, q2, "b"))
        b.append(arrow(930, y + 59, 1006, 330 - 0, INK2))
    b.append(box(1010, 200, 350, 260, fill=BLUE_XL, stroke=BLUE_D, sw=2))
    b.append(text(1185, 240, "Integrated study", "h", "middle"))
    b.append(lines(1185, 272, ["Online surgical phase recognition", "on network-delivered video", "", "Cholec80 · PhaKIR · AutoLaparo (opt.)", "Real encoder → emulator → decoder", "Receiver-observable telemetry", "Pre-registered kill criteria"], "b", "middle", 22))
    b.append(text(40, 540, "Reasons: shared substrate; informative even if RQ1 is negative; standalone A and B are largely occupied; one temporal task avoids dilution.", "bs"))
    return svg(W, H, "\n".join(b), "Track merge decision")


# ---------------------------------------------------------------- fig 4
def fig4():
    W, H = 1400, 420
    b = [text(40, 48, "Roadmap and current position", "title"),
         text(40, 76, "Progress is gated by evidence: each phase exits only when its criteria are met (ROADMAP.md, EXECUTION_BRIEF.md)", "sub")]
    phases = [("0", "Research|foundation", "done"), ("1", "Gap|validation", "now"), ("2", "Dataset & task|feasibility", ""),
              ("3", "Baselines", ""), ("4", "Shift|benchmarking", ""), ("5", "Reliability|methods", ""),
              ("6", "Network-aware|reliability", ""), ("7", "Validation &|publication", "")]
    n, x0, y = len(phases), 40, 130
    w = (W - 80 - (n - 1) * 12) / n
    for i, (num, name, st) in enumerate(phases):
        x = x0 + i * (w + 12)
        fill = BLUE_D if st == "done" else (BLUE_XL if st == "now" else "#ffffff")
        stroke = BLUE_D if st else GRID
        ink = "#ffffff" if st == "done" else INK
        b.append(box(x, y, w, 86, fill=fill, stroke=stroke, sw=2.5 if st == "now" else 1.5))
        b.append(f'<text x="{x + 14}" y="{y + 30}" style="{FONT};font-size:13px;fill:{ink};opacity:0.8">PHASE {num}</text>')
        l1, _, l2 = name.partition("|")
        b.append(f'<text x="{x + 14}" y="{y + 54}" style="{FONT};font-size:15px;font-weight:700;fill:{ink}">{escape(l1)}</text>')
        if l2:
            b.append(f'<text x="{x + 14}" y="{y + 73}" style="{FONT};font-size:15px;font-weight:700;fill:{ink}">{escape(l2)}</text>')
    # phase 0 detail
    b.append(text(40, 262, "Phase 0 — complete (M0)", "h"))
    p0 = ["P0.1 Toumai architecture", "P0.2 Surgical CV landscape", "P0.3 Datasets", "P0.4 Distribution shift",
          "P0.5 Reliable inference", "P0.6 Telesurgery networks", "P0.7 Intersection & stress-test"]
    for i, s in enumerate(p0):
        b.append(text(40 + (i % 2) * 260, 290 + (i // 2) * 22, "✓ " + s, "bs"))
    b.append(text(600, 262, "Phase 1 — deliverables complete", "h"))
    p1 = [("✓", "P1.1 Targeted gap-validation search"), ("✓", "P1.2 Pre-registration (v1.1)"), ("✓", "P1.3 Media-pipeline specification"),
          ("✓", "P1.4 Feature tiers & leakage controls"), ("✓", "P1.5 Dataset desk checks"), ("✓", "P1.6 Feasibility & power"),
          ("✓", "P1.7 Baseline model selection"), ("→", "Author sign-off → M1")]
    for i, (m, s) in enumerate(p1):
        b.append(text(600 + (i % 2) * 330, 290 + (i // 2) * 22, f"{m} {s}", "bs"))
    b.append(text(40, 400, "No data are acquired and no models trained until the pre-registration is signed off; Phase 2 then builds the pipeline and reproduces baselines.", "bs"))
    return svg(W, H, "\n".join(b), "Programme roadmap")


def main():
    for name, fn in [("fig1-research-question.svg", fig1), ("fig2-evidence-landscape.svg", fig2),
                     ("fig3-track-merge.svg", fig3), ("fig4-roadmap.svg", fig4)]:
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(fn())
        print("wrote", name)


if __name__ == "__main__":
    main()
