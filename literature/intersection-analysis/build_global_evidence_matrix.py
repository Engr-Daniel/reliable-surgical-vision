#!/usr/bin/env python3
"""Build the P0.7 global evidence matrix from the P0.1-P0.6 maps plus the P0.7 refresh.

Every retained source is coded on six programme dimensions. Codes are assigned
manually, source by source, in the CODES table below (not by keyword matching),
so that the occupancy judgements in intersection-map.csv can be traced to an
explicit, reviewable coding decision.

Usage (from repository root):
    python3 literature/intersection-analysis/build_global_evidence_matrix.py

Outputs (overwritten):
    literature/intersection-analysis/global-evidence-matrix.csv
    literature/intersection-analysis/coverage-summary.md

Code book
---------
evidence_level : PR peer-reviewed | PP preprint (incl. accepted-not-yet-published)
                 | DS dataset/challenge resource | GL guideline/consensus | STD standard
                 | REG regulatory | MFR manufacturer | SEC secondary/institutional
directness     : SURG surgical CV | TELESURG telesurgery system/clinical
                 | MED-ADJ adjacent medical | GENERIC non-medical/general ML or networking
task_family    : PH phase/workflow | SEG segmentation | DET detection/keypoint/presence
                 | ACT action/gesture/triplet | VLM video-language/VQA | TRAJ trajectory
                 | CLS generic classification | HUM human teleoperation performance
                 | SYS system/network (no CV task) | GEN multiple/field-level
shift_class    : NAT natural (centre/device/procedure/sim2real) | VIS controlled visual
                 | TEMP temporal/video | NET network-emulated or real network condition
                 | COMP explicitly compound | none
reliability    : CAL calibration | UQ uncertainty estimation | OOD OOD/open-set
                 | FAIL failure detection/prediction | SEL selective prediction/abstention
                 | CP conformal/risk control | STAB temporal-prediction stability | none
network_layer  : NETQOS network QoS | TRANSPORT transport/codec/recovery mechanism
                 | DECODED decoded/received-video effect | HUMAN-OUT human operator / clinical outcome | none
downstream_ai  : Y if an AI/CV model is evaluated on the (shifted) input
telemetry_ai   : Y if network/system telemetry is used to predict or gate AI reliability
"""
import csv
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "literature", "intersection-analysis")

SUBMAPS = [
    ("P0.1", "literature/toumai/toumai-literature-map.csv", "source_id", "title", "year"),
    ("P0.2", "literature/surgical-vision/surgical-cv-literature-map.csv", "source_id", "title", "year"),
    ("P0.3", "datasets/dataset-registry.csv", "id", "name", None),
    ("P0.4", "literature/distribution-shift/distribution-shift-literature-map.csv", "id", "title", "year"),
    ("P0.5", "literature/uncertainty-reliability/reliable-inference-literature-map.csv", "id", "title", "year"),
    ("P0.6", "literature/telesurgery-networking/telesurgery-network-literature-map.csv", "source_id", "title", "year"),
]

# id: (level, directness, task, shift, reliability, network_layer, downstream_ai, telemetry_ai)
CODES = {
    # ---- P0.1 Toumai / telesurgery system evidence
    "S01": ("REG", "TELESURG", "SYS", "none", "none", "NETQOS", "N", "N"),
    "S02": ("MFR", "TELESURG", "SYS", "none", "none", "none", "N", "N"),
    "S03": ("PR", "TELESURG", "SYS", "none", "none", "none", "N", "N"),
    **{f"S{i:02d}": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;HUMAN-OUT", "N", "N") for i in range(4, 12)},
    "S12": ("PR", "TELESURG", "SYS", "none", "none", "none", "N", "N"),
    "S13": ("MFR", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "S14": ("MFR", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "S15": ("SEC", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "S16": ("MFR", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    # ---- P0.2 surgical CV landscape
    "SV01": ("PR", "SURG", "GEN", "none", "none", "none", "N", "N"),
    "SV02": ("PR", "SURG", "PH", "none", "none", "none", "N", "N"),
    "SV03": ("PR", "SURG", "PH", "none", "none", "none", "N", "N"),
    "SV04": ("PR", "SURG", "GEN", "none", "none", "none", "N", "N"),
    "SV05": ("PR", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "SV06": ("PR", "SURG", "SEG;DET", "none", "none", "none", "N", "N"),
    "SV07": ("PR", "MED-ADJ", "GEN", "none", "none", "none", "N", "N"),
    "SV08": ("PR", "SURG", "PH;DET", "none", "none", "none", "Y", "N"),
    "SV09": ("PR", "SURG", "PH", "none", "none", "none", "Y", "N"),
    "SV10": ("PR", "SURG", "PH", "none", "none", "none", "Y", "N"),
    "SV11": ("PR", "SURG", "PH", "none", "none", "none", "Y", "N"),
    "SV12": ("DS", "SURG", "PH;SEG", "none", "none", "none", "Y", "N"),
    "SV13": ("DS", "SURG", "PH;ACT;DET", "NAT", "none", "none", "Y", "N"),
    "SV14": ("DS", "SURG", "PH;DET;SEG", "NAT", "none", "none", "Y", "N"),
    "SV15": ("DS", "SURG", "PH;DET;SEG", "NAT", "none", "none", "N", "N"),
    "SV16": ("DS", "SURG", "ACT", "none", "none", "none", "Y", "N"),
    "SV17": ("PR", "SURG", "ACT", "none", "none", "none", "Y", "N"),
    "SV18": ("DS", "SURG", "ACT", "none", "none", "none", "Y", "N"),
    "SV19": ("DS", "SURG", "SEG;ACT", "none", "none", "none", "Y", "N"),
    "SV20": ("DS", "SURG", "SEG", "none", "none", "none", "Y", "N"),
    "SV21": ("DS", "SURG", "SEG", "none", "none", "none", "Y", "N"),
    "SV22": ("DS", "SURG", "SEG;DET", "NAT", "none", "none", "Y", "N"),
    "SV23": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "SV24": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "SV25": ("DS", "SURG", "DET;SEG", "none", "none", "none", "Y", "N"),
    "SV26": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "SV27": ("PR", "SURG", "SEG", "none", "none", "none", "Y", "N"),
    "SV28": ("PR", "SURG", "VLM", "none", "none", "none", "Y", "N"),
    "SV29": ("DS", "SURG", "DET;ACT", "none", "none", "none", "Y", "N"),
    "SV30": ("DS", "SURG", "PH", "none", "none", "none", "N", "N"),
    "SV31": ("DS", "SURG", "DET", "none", "none", "none", "Y", "N"),
    "SV32": ("PR", "SURG", "PH", "none", "none", "none", "Y", "N"),
    "SV33": ("DS", "SURG", "GEN", "none", "none", "none", "N", "N"),
    # ---- P0.3 datasets (resources, not findings)
    "DS01": ("DS", "SURG", "PH;DET", "none", "none", "none", "N", "N"),
    "DS02": ("DS", "SURG", "ACT;PH", "none", "none", "none", "N", "N"),
    "DS03": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "DS04": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "DS05": ("DS", "SURG", "DET;SEG", "none", "none", "none", "N", "N"),
    "DS06": ("DS", "SURG", "PH;DET;SEG", "NAT", "none", "none", "N", "N"),
    "DS07": ("DS", "SURG", "PH;ACT;DET", "NAT", "none", "none", "N", "N"),
    "DS08": ("DS", "SURG", "PH", "NAT", "none", "none", "N", "N"),
    "DS09": ("DS", "SURG", "PH;SEG", "none", "none", "none", "N", "N"),
    "DS10": ("DS", "SURG", "SEG;ACT", "none", "none", "none", "N", "N"),
    "DS11": ("DS", "SURG", "ACT", "none", "none", "none", "N", "N"),
    "DS12": ("DS", "SURG", "ACT", "none", "none", "none", "N", "N"),
    "DS13": ("DS", "SURG", "SEG;DET", "NAT", "none", "none", "N", "N"),
    "DS14": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "DS15": ("DS", "SURG", "DET", "none", "none", "none", "N", "N"),
    "DS16": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "DS17": ("DS", "SURG", "SEG", "none", "none", "none", "N", "N"),
    "DS18": ("DS", "SURG", "DET;ACT", "none", "none", "none", "N", "N"),
    # ---- P0.4 distribution shift
    "SH01": ("PR", "SURG", "SEG;DET", "NAT", "none", "none", "Y", "N"),
    "SH02": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH03": ("PR", "SURG", "PH", "NAT", "none", "none", "Y", "N"),
    "SH04": ("PR", "SURG", "PH;DET;SEG", "NAT", "none", "none", "Y", "N"),
    "SH05": ("PR", "SURG", "PH", "NAT", "none", "none", "Y", "N"),
    "SH06": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH07": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH08": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH09": ("PP", "SURG", "SEG", "VIS", "none", "none", "Y", "N"),
    "SH10": ("PR", "SURG", "SEG", "VIS", "none", "none", "Y", "N"),
    "SH11": ("PR", "SURG", "SEG", "VIS;TEMP", "none", "none", "Y", "N"),
    "SH12": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH13": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH14": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH15": ("PR", "SURG", "ACT", "NAT", "none", "none", "Y", "N"),
    "SH16": ("PR", "SURG", "PH", "NAT", "none", "none", "Y", "N"),
    "SH17": ("PR", "MED-ADJ", "CLS", "VIS;COMP", "none", "none", "Y", "N"),
    "SH18": ("PP", "SURG", "VLM", "VIS;TEMP", "none", "DECODED", "Y", "N"),
    "SH19": ("PP", "SURG", "SEG", "VIS", "none", "none", "Y", "N"),
    "SH20": ("PR", "SURG", "PH", "TEMP", "STAB", "none", "Y", "N"),
    "SH21": ("PR", "SURG", "PH", "TEMP", "STAB", "none", "Y", "N"),
    "SH22": ("DS", "SURG", "DET;SEG", "NAT", "none", "none", "Y", "N"),
    "SH23": ("PR", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH24": ("PP", "SURG", "SEG", "NAT", "none", "none", "Y", "N"),
    "SH25": ("DS", "SURG", "SEG", "VIS", "none", "none", "N", "N"),
    # ---- P0.5 reliable inference
    "RI01": ("PR", "GENERIC", "CLS", "none", "CAL", "none", "Y", "N"),
    "RI02": ("PR", "GENERIC", "CLS", "VIS;NAT", "CAL;UQ", "none", "Y", "N"),
    "RI03": ("PR", "GENERIC", "CLS", "none", "UQ", "none", "Y", "N"),
    "RI04": ("PR", "GENERIC", "CLS", "none", "UQ", "none", "Y", "N"),
    "RI05": ("PR", "GENERIC", "SEG", "none", "UQ", "none", "Y", "N"),
    "RI06": ("PR", "MED-ADJ", "CLS", "none", "UQ", "none", "N", "N"),
    "RI07": ("PR", "MED-ADJ", "GEN", "none", "UQ", "none", "N", "N"),
    "RI08": ("PR", "MED-ADJ", "GEN", "none", "UQ", "none", "N", "N"),
    "RI09": ("PR", "MED-ADJ", "SEG", "none", "CAL;UQ", "none", "Y", "N"),
    "RI10": ("PR", "MED-ADJ", "SEG", "NAT", "CAL;OOD", "none", "Y", "N"),
    "RI11": ("PR", "MED-ADJ", "CLS", "none", "FAIL", "none", "Y", "N"),
    "RI12": ("PR", "SURG", "SEG", "none", "CAL;UQ", "none", "Y", "N"),
    "RI13": ("PR", "SURG", "PH", "none", "CAL", "none", "Y", "N"),
    "RI14": ("PR", "SURG", "PH", "NAT", "OOD", "none", "Y", "N"),
    "RI15": ("PR", "SURG", "VLM", "none", "CAL;SEL", "none", "Y", "N"),
    "RI16": ("PP", "SURG", "PH", "none", "UQ", "none", "Y", "N"),
    "RI17": ("PR", "SURG", "CLS", "VIS;NAT", "OOD", "none", "Y", "N"),
    "RI18": ("PR", "GENERIC", "CLS", "NAT", "OOD;FAIL", "none", "Y", "N"),
    "RI19": ("PR", "GENERIC", "CLS", "NAT", "OOD", "none", "Y", "N"),
    "RI20": ("PR", "GENERIC", "CLS", "none", "SEL", "none", "Y", "N"),
    "RI21": ("PR", "GENERIC", "CLS", "none", "SEL", "none", "Y", "N"),
    "RI22": ("PR", "MED-ADJ", "SEG", "NAT", "SEL", "none", "Y", "N"),
    "RI23": ("PR", "MED-ADJ", "SEG", "NAT", "SEL", "none", "Y", "N"),
    "RI24": ("PR", "MED-ADJ", "SEG", "none", "SEL", "none", "Y", "N"),
    "RI25": ("PR", "MED-ADJ", "CLS", "NAT", "CAL;CP;SEL", "none", "Y", "N"),
    "RI26": ("PR", "GENERIC", "CLS", "none", "CP", "none", "Y", "N"),
    "RI27": ("PR", "GENERIC", "GEN", "NAT", "CP", "none", "N", "N"),
    "RI28": ("PR", "GENERIC", "GEN", "TEMP", "CP", "none", "N", "N"),
    "RI29": ("PR", "GENERIC", "GEN", "none", "CP", "none", "Y", "N"),
    "RI30": ("PR", "MED-ADJ", "SEG", "none", "CP", "none", "Y", "N"),
    "RI31": ("PR", "SURG", "TRAJ", "none", "CP", "none", "Y", "N"),
    "RI32": ("PR", "MED-ADJ", "CLS", "none", "CP", "none", "Y", "N"),
    "RI33": ("PR", "MED-ADJ", "CLS", "NAT", "CP", "none", "Y", "N"),
    "RI34": ("PP", "SURG", "SEG", "VIS", "FAIL;CP", "none", "Y", "N"),
    "RI35": ("PR", "GENERIC", "CLS", "none", "CAL", "none", "N", "N"),
    "RI36": ("PR", "GENERIC", "CLS", "none", "SEL", "none", "N", "N"),
    # ---- P0.6 telesurgery networking
    "NW01": ("GL", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "NW02": ("GL", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "NW03": ("GL", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "NW04": ("PR", "TELESURG", "HUM", "NET;COMP", "none", "NETQOS;HUMAN-OUT", "N", "N"),
    "NW05": ("PR", "TELESURG", "HUM", "NET", "none", "NETQOS;DECODED;HUMAN-OUT", "N", "N"),
    "NW06": ("PR", "TELESURG", "HUM", "NET", "none", "NETQOS;DECODED;HUMAN-OUT", "N", "N"),
    "NW07": ("PR", "TELESURG", "HUM", "NET", "none", "NETQOS;HUMAN-OUT", "N", "N"),
    "NW08": ("PR", "TELESURG", "HUM", "NET", "none", "HUMAN-OUT", "N", "N"),
    "NW09": ("PR", "TELESURG", "HUM", "NET", "none", "NETQOS;DECODED;HUMAN-OUT", "N", "N"),
    "NW10": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    "NW11": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    "NW12": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    "NW13": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "NW14": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    "NW15": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    **{f"NW{i}": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS", "N", "N") for i in (16, 17, 20, 21, 22, 23, 24, 25)},
    "NW18": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    "NW19": ("PR", "TELESURG", "SYS", "NET", "none", "NETQOS;DECODED", "N", "N"),
    **{f"NW{i}": ("STD", "GENERIC", "SYS", "NET", "none", "TRANSPORT", "N", "N") for i in range(26, 33)},
    "NW33": ("PR", "GENERIC", "SYS", "NET", "none", "TRANSPORT;DECODED", "N", "N"),
    "NW34": ("PR", "GENERIC", "SYS", "NET", "none", "TRANSPORT;DECODED", "N", "N"),
    "NW35": ("PP", "SURG", "VLM", "VIS;TEMP", "none", "DECODED", "Y", "N"),
    # ---- P0.7 refresh (see source-index.md)
    "IX01": ("PP", "TELESURG", "HUM", "NET;COMP", "none", "NETQOS;TRANSPORT;DECODED;HUMAN-OUT", "N", "N"),
    "IX02": ("PP", "TELESURG", "HUM", "NET", "none", "NETQOS;HUMAN-OUT", "N", "N"),
    "IX03": ("PP", "SURG", "PH", "none", "STAB", "none", "Y", "N"),
    "IX04": ("PP", "SURG", "PH", "VIS;NAT", "none", "none", "Y", "N"),
    "IX05": ("PR", "MED-ADJ", "SEG", "NAT", "FAIL;SEL", "none", "Y", "N"),
    "IX06": ("PR", "SURG", "SEG", "NET", "none", "NETQOS", "Y", "N"),
    "IX07": ("PR", "GENERIC", "DET;SEG", "NET", "none", "TRANSPORT;DECODED", "Y", "N"),
    "IX08": ("PP", "GENERIC", "DET;SEG", "NET", "none", "TRANSPORT;DECODED", "Y", "N"),
    "IX09": ("PR", "GENERIC", "DET", "NET", "none", "TRANSPORT", "Y", "N"),
    "IX10": ("PR", "GENERIC", "DET", "NET", "none", "NETQOS", "Y", "N"),
    "IX11": ("PP", "GENERIC", "SYS", "NET", "none", "NETQOS", "N", "N"),
    "IX12": ("PR", "SURG", "PH", "NAT", "none", "none", "Y", "N"),
}

IX_ROWS = [
    ("IX01", "VISTA: A Benchmark for Real-Time Video Streaming under Network Impairments in Surgical Teleoperation", "2026"),
    ("IX02", "A Comprehensive Analysis of the Effects of Network Quality of Service on Robotic Telesurgery", "2026"),
    ("IX03", "Stabilizing Temporal Inference Dynamics for Online Surgical Phase Recognition", "2026"),
    ("IX04", "Towards Robust Algorithms for Surgical Phase Recognition via Digital Twin Representation", "2024"),
    ("IX05", "Comparative benchmarking of failure detection methods in medical image segmentation: Unveiling the role of confidence aggregation", "2025"),
    ("IX06", "Development, deployment and scaling of operating room-ready artificial intelligence for real-time surgical decision support", "2024"),
    ("IX07", "Server-Driven Video Streaming for Deep Learning Inference (DDS)", "2020"),
    ("IX08", "AccMPEG: Optimizing Video Encoding for Video Analytics", "2022"),
    ("IX09", "Minimizing packet retransmission for real-time video analytics", "2022"),
    ("IX10", "VANET Meets Deep Learning: The Effect of Packet Loss on the Object Detection Performance", "2019"),
    ("IX11", "System Modeling and Performance Evaluation of Predictive QoS for Future Tele-Operated Driving", "2022"),
    ("IX12", "Recognizing Surgical Phases Anywhere: Few-Shot Test-time Adaptation and Task-graph Guided Refinement", "2025"),
]


def norm(t):
    t = re.sub(r"^(the|a|an)\s+", "", t.strip().lower())
    return re.sub(r"[^a-z0-9]", "", t)[:80]


def tracks(shift, rel, net):
    out = []
    if shift != "none":
        out.append("A")
    if rel != "none":
        out.append("B")
    if net != "none":
        out.append("C")
    return ";".join(out) or "foundation"


def main():
    rows = []
    for task, path, idk, titlek, yeark in SUBMAPS:
        with open(os.path.join(ROOT, path), newline="") as fh:
            for r in csv.DictReader(fh):
                rows.append((r[idk], task, r[titlek], r[yeark] if yeark else "", path))
    for i, t, y in IX_ROWS:
        rows.append((i, "P0.7", t, y, "literature/intersection-analysis/source-index.md"))

    missing = [r[0] for r in rows if r[0] not in CODES]
    extra = sorted(set(CODES) - {r[0] for r in rows})
    if missing or extra:
        raise SystemExit(f"coding table mismatch: uncoded={missing} unknown={extra}")

    first_by_title = {}
    out = []
    for sid, task, title, year, path in rows:
        lvl, direct, tf, sh, rel, net, ai, tel = CODES[sid]
        key = norm(title)
        dup = first_by_title.get(key, "")
        first_by_title.setdefault(key, sid)
        out.append({
            "evidence_id": sid, "origin_task": task, "title": title, "year": year,
            "evidence_level": lvl, "directness": direct, "task_family": tf,
            "shift_class": sh, "reliability_concept": rel, "network_layer": net,
            "downstream_ai_evaluated": ai, "telemetry_for_ai_reliability": tel,
            "track_relevance": tracks(sh, rel, net), "duplicate_of": dup, "source_file": path,
        })

    fields = list(out[0].keys())
    with open(os.path.join(OUT_DIR, "global-evidence-matrix.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    uniq = [r for r in out if not r["duplicate_of"]]

    def has(r, col, code):
        return code in r[col].split(";")

    def count(pred):
        return sum(1 for r in uniq if pred(r))

    lines = ["# P0.7 Coverage Summary (generated)", "",
             "Generated by `build_global_evidence_matrix.py`. Counts are over **unique** sources "
             "(cross-task duplicates collapsed by normalised title). They describe the programme's "
             "retained evidence base, not the whole literature.", "",
             f"- Rows in matrix: **{len(out)}**",
             f"- Unique sources: **{len(uniq)}**",
             f"- Cross-task duplicates: **{len(out) - len(uniq)}**", ""]

    def table(title, col, codes):
        lines.extend([f"## {title}", "", "| Code | Unique sources |", "|---|---|"])
        for c in codes:
            lines.append(f"| {c} | {count(lambda r, c=c: has(r, col, c))} |")
        lines.append("")

    table("Evidence level", "evidence_level", ["PR", "PP", "DS", "GL", "STD", "REG", "MFR", "SEC"])
    table("Directness", "directness", ["SURG", "TELESURG", "MED-ADJ", "GENERIC"])
    table("Task family", "task_family", ["PH", "SEG", "DET", "ACT", "VLM", "TRAJ", "CLS", "HUM", "SYS", "GEN"])
    table("Shift class", "shift_class", ["NAT", "VIS", "TEMP", "NET", "COMP", "none"])
    table("Reliability concept", "reliability_concept", ["CAL", "UQ", "OOD", "FAIL", "SEL", "CP", "STAB", "none"])
    table("Network layer", "network_layer", ["NETQOS", "TRANSPORT", "DECODED", "HUMAN-OUT", "none"])

    surg_ai = lambda r: r["directness"] == "SURG" and r["downstream_ai_evaluated"] == "Y"
    probes = [
        ("Surgical CV evaluated under natural shift", lambda r: surg_ai(r) and has(r, "shift_class", "NAT")),
        ("Surgical CV evaluated under controlled visual shift", lambda r: surg_ai(r) and has(r, "shift_class", "VIS")),
        ("Surgical CV evaluated under temporal/video shift", lambda r: surg_ai(r) and has(r, "shift_class", "TEMP")),
        ("Surgical CV with any reliability concept", lambda r: surg_ai(r) and r["reliability_concept"] != "none"),
        ("Surgical CV with reliability concept AND any shift", lambda r: surg_ai(r) and r["reliability_concept"] != "none" and r["shift_class"] != "none"),
        ("Surgical CV with reliability concept AND temporal/network shift", lambda r: surg_ai(r) and r["reliability_concept"] != "none" and (has(r, "shift_class", "TEMP") or has(r, "shift_class", "NET"))),
        ("Surgical phase recognition with conformal/selective reliability", lambda r: surg_ai(r) and has(r, "task_family", "PH") and (has(r, "reliability_concept", "CP") or has(r, "reliability_concept", "SEL"))),
        ("Surgical CV evaluated on decoded/network-affected video", lambda r: surg_ai(r) and (has(r, "network_layer", "DECODED") or has(r, "shift_class", "NET"))),
        ("Telesurgery network studies with human-operator outcome only", lambda r: r["directness"] == "TELESURG" and has(r, "network_layer", "HUMAN-OUT") and r["downstream_ai_evaluated"] == "N"),
        ("Any source: AI evaluated under network conditions (any domain)", lambda r: r["downstream_ai_evaluated"] == "Y" and has(r, "shift_class", "NET")),
        ("Any source: network/system telemetry used to predict AI reliability", lambda r: r["telemetry_for_ai_reliability"] == "Y"),
    ]
    lines.extend(["## Intersection probes", "", "| Probe | Unique sources | IDs |", "|---|---|---|"])
    for name, p in probes:
        ids = [r["evidence_id"] for r in uniq if p(r)]
        lines.append(f"| {name} | {len(ids)} | {', '.join(ids) if ids else '—'} |")
    lines.append("")
    lines.append("A zero in the last probe is a statement about the retained evidence base only; "
                 "it is **not** evidence that no such work exists (see `novelty-stress-test.md`).")
    with open(os.path.join(OUT_DIR, "coverage-summary.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {len(out)} rows ({len(uniq)} unique)")


if __name__ == "__main__":
    main()
