# P0.3 Dataset Provenance and Overlap Map

## Why this artifact exists

Dataset names are not equivalent to independent patient/video domains.

A model can appear to generalize across “datasets” while actually seeing frames from the same source procedures in training and evaluation. This is especially important in the CAMMA cholecystectomy ecosystem.

---

## 1. Confirmed CAMMA lineage

```text
Cholec80 (80 source videos)
├── CholecT50
│   ├── 45 videos from Cholec80
│   └── 5 additional videos from in-house Cholec120
│
├── CholecSeg8k
│   └── 8,080 annotated frames from 17 Cholec80 videos
│
└── contributes source imagery to CholecInstanceSeg
    ├── CholecT50-derived partitions
    ├── CholecSeg8k-derived partition
    └── additional Cholec80-derived sparse partition
```

The CholecInstanceSeg paper explicitly reports that CholecSeg8k and CholecT50 share **10 image sequences by source sequence**; the authors found no exact frame matches in those shared sequences because the extraction procedures differed.

**Experimental implication:** “not the exact same frame” does not mean “independent patient/video domain.” The source surgery remains shared.

---

## 2. Endoscapes relationship

CAMMA now explicitly links to a **Dataset Overlaps** analysis from the official Cholec80, CholecT50 and Endoscapes repositories.

P0.3 confirms that overlap is important enough to be treated as a blocking provenance check, but does **not** invent pairwise counts that were not extracted into this audit.

Before any experiment such as:

`train on Cholec80 → test on Endoscapes`

the exact source-video overlap mapping must be retrieved from CAMMA and used to remove shared procedures.

---

## 3. Cataract lineage

```text
CATARACTS
└── CaDIS
    └── 4,670 segmentation images sampled from the 25 CATARACTS training videos
```

Therefore CaDIS cannot be treated as an independent external dataset relative to CATARACTS.

---

## 4. CholecInstanceSeg is an annotation unification resource, not an independent domain

CholecInstanceSeg is scientifically valuable because it adds dense tool-instance labels across a larger set of sequences.

For reliability/generalization experiments, however, the correct unit of provenance is the **source surgical video**, not the CholecInstanceSeg partition name.

Required metadata for any future loader:

```text
dataset_name
source_dataset
source_video_id
source_procedure_id (if available)
centre_id (if available)
frame_index
timestamp (if available)
annotation_source
split
```

---

## 5. Independent-domain candidates

The following candidates are not derived from the Cholec80 family and therefore provide stronger external-domain possibilities, subject to task-label compatibility:

- PhaKIR — three German centres;
- HeiChole — three German centres;
- MultiBypass140 — gastric bypass, Strasbourg + Bern;
- AutoLaparo — hysterectomy, Hong Kong;
- SAR-RARP50 — robot-assisted radical prostatectomy;
- ESAD — robot-assisted radical prostatectomy;
- JIGSAWS — robotic training tasks;
- HeiCo / ROBUST-MIS — colorectal surgery;
- CATARACTS — cataract surgery;
- EndoVis robotic challenges — porcine robotic domain;
- SurgVU — porcine robotic training exercises.

“Independent domain” here means no documented derivation from the CAMMA Cholec80 lineage. It does **not** imply identical label spaces or direct comparability.

---

## 6. Non-negotiable split rule

For all later experiments:

> **No source surgical procedure may contribute frames to more than one of train, calibration/validation, and test unless a benchmark explicitly requires otherwise and the leakage implication is documented.**

For cross-dataset evaluation:

> **Cross-dataset ≠ cross-domain until source-video overlap has been ruled out.**

---

## 7. Provenance gate before experiments

Before a dataset enters an experiment configuration:

- [ ] canonical dataset/version recorded;
- [ ] source video IDs available or reconstructed;
- [ ] derived-dataset lineage recorded;
- [ ] centre/procedure metadata preserved where available;
- [ ] train/val/test split checked at procedure level;
- [ ] cross-dataset overlap checked;
- [ ] no frame-level leakage;
- [ ] corruption outputs retain source provenance.
