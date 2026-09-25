# P0.3 Working Dataset Shortlist

## Status

This is a **working feasibility shortlist**, not the final experimental selection.

P0.4–P0.7 may remove, merge or change these choices after the distribution-shift, reliable-inference, networking and novelty evidence is complete.

---

## 1. Working candidates for immediate prototyping

### Cholec80 — temporal/workflow backbone

**Why it remains useful**
- complete clinical videos;
- mature phase-recognition benchmark;
- dense phase labels;
- 25-fps source video;
- widely reproducible baseline ecosystem;
- clear suitability for frame drop, irregular sampling, compression/re-encoding and temporal-context experiments.

**Constraint**
It is single-centre and has extensive lineage overlap with later CAMMA datasets. It should not be used to claim broad external generalization on its own.

**Likely P0.4/P0.5 role**
Controlled temporal-shift and reliability-method development for phase recognition.

---

### SAR-RARP50 — direct robot-assisted spatial/action backbone

**Why it remains useful**
- human robot-assisted radical prostatectomy;
- official UCL train/test archives;
- CC BY-NC-SA 4.0;
- manageable published archive size (~31.25 GB train + test);
- instrument segmentation and action recognition in the same robotic setting.

**Constraint**
The benchmark focuses on prostatectomy suturing/DVC-phase segments rather than complete procedure workflow.

**Likely role**
Robot-assisted segmentation/action reliability experiments and platform-relevant visual degradation.

---

### Endoscapes2023 — anatomy/instrument/safety-state spatial backbone

**Why it remains useful**
- 201 source procedures;
- anatomy + instrument detection/segmentation;
- expert Critical View of Safety labels;
- official procedure-level splits;
- clinically meaningful high-stakes scene perception.

**Constraint**
Current PhysioNet-hosted files are governed by restricted access + DUA. The release is annotation/frame-centric, so full-video temporal/network experiments must not be assumed without verifying the available sequence files.

**Likely role**
Spatial corruption, dense reliability and safety-state experiments.

---

### PhaKIR — multicentre bridge dataset

**Why it remains useful**
- complete videos from three medical centres;
- 25-fps 1080p source;
- phases for every frame;
- instrument keypoints + instance masks at 1 fps;
- controlled access under CC BY-NC-SA;
- combines temporal and spatial tasks in the same procedures.

**Constraint**
Only eight complete videos are in the public release, making it better suited to external/multicentre validation than large-model training.

**Likely role**
Cross-centre external validation and task-consistent shift testing.

---

## 2. High-value natural-shift / validation datasets

### HeiChole
Strong multicentre human workflow benchmark: 33 videos from three centres with phase/action/instrument/skill labels.

Use case: natural centre/device shift validation.

Constraint: ~156 GB public bundle and original benchmark hidden-test protocol must be reconciled.

### HeiCo / ROBUST-MIS
Strong spatial robustness resource with three colorectal procedure types and staged increasing domain gap.

Use case: test whether conclusions survive a naturally harder procedure-domain shift.

### AutoLaparo
Full hysterectomy videos with workflow and spatial labels.

Use case: cross-procedure validation outside cholecystectomy.

### MultiBypass140
Scientifically excellent for temporal cross-centre generalization: 140 videos, 70 per centre.

**Operational hold as of 2026-09-25:** an open repository issue reports that one required archive (`multibypass03.zip`) currently contains metadata but no videos, while other archive parts are hundreds of gigabytes in total. Re-check before use.

---

## 3. Secondary / specialized resources

- **CholecT50** — valuable for fine-grained action triplets, but 45/50 videos are Cholec80.
- **CholecInstanceSeg** — excellent dense tool labels; composite provenance prevents independent-domain interpretation.
- **CholecSeg8k** — useful segmentation subset; derived directly from 17 Cholec80 videos.
- **ESAD** — directly robotic, but only four complete sessions and test data remain restricted/unreleased on the current challenge page.
- **JIGSAWS** — excellent synchronized video/kinematics and gesture labels, but bench-top training rather than clinical surgery.
- **CaDIS** — strong dense segmentation labels, but current official download route is unresolved.
- **CATARACTS** — complete videos and different optical domain; label/task compatibility is limited.
- **EndoVis 2017/2018** — useful legacy robotic segmentation data, but porcine rather than human.
- **SurgVU** — massive robotic-training corpus; potentially useful for pretraining, but porcine training exercises and very high storage/compute burden.

---

## 4. Why P0.3 does not choose one final dataset

A single dataset would create avoidable blind spots.

The programme currently needs to preserve at least four axes:

| Need | Candidate type |
|---|---|
| Temporal workflow reliability | Cholec80 / later MultiBypass140 or HeiChole |
| Robot-assisted perception | SAR-RARP50 |
| Dense anatomy/instrument perception | Endoscapes / ROBUST-MIS |
| Multicentre external validation | PhaKIR / HeiChole |

The final experiment may still use fewer datasets. That decision is deliberately delayed until P0.4–P0.7 establish:
- what shift has already been studied;
- what reliability method is valid for the selected output;
- what network degradation can be simulated defensibly;
- what combination remains scientifically useful.

---

## 5. Dataset selection gate for Phase 1

A dataset may become an experimental dataset only if:

- access has been successfully obtained;
- current licence/DUA is stored/documented;
- source-video provenance is available;
- procedure-level splits are defined;
- overlap with other selected datasets is resolved;
- task label space is compatible with the experiment;
- storage/compute requirements are feasible;
- the P0.4 shift protocol can be applied;
- the P0.5 reliability metric is meaningful for the task;
- P0.7 finds the experiment scientifically justified.
