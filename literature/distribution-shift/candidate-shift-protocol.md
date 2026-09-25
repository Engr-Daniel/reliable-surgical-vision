# P0.4 Working Shift Protocol

## Status

**Working protocol only — not yet an experimental commitment.**

P0.4 identifies which shift families are scientifically justified by existing evidence. P0.5 must establish reliability metrics/methods, P0.6 must establish network-to-video mechanisms, and P0.7 must perform the final novelty/intersection stress-test.

---

# 1. Design principle

Later experiments should not use one undifferentiated “OOD” test.

The working hierarchy is:

```text
S0  Clean / source-domain reference

S1  Natural external shift
    ├─ centre / institution
    ├─ device / recording system
    └─ procedure / workflow

S2  Controlled single visual shift
    ├─ illumination
    ├─ smoke / haze
    ├─ blood / occlusion
    ├─ blur
    ├─ colour / white balance
    └─ compression / resolution

S3  Controlled temporal/video shift
    ├─ sampling reduction
    ├─ missing-frame events
    ├─ burst loss / freeze
    └─ irregular delivery
        [parameters blocked until P0.6]

S4  Compound shift
    ├─ visual + visual
    ├─ natural + controlled
    └─ visual + temporal/network
        [final design blocked until P0.6/P0.7]
```

---

# 2. S0 — clean reference

For every task/model:

- preserve the canonical clean test set;
- preserve original resolution/frame rate unless the baseline benchmark mandates preprocessing;
- report the clean task metric;
- record all preprocessing.

All robustness results must be interpretable relative to S0.

---

# 3. S1 — natural external shift

## S1-A — centre shift

### Strong candidates from the current programme
- **PhaKIR** — multicentre cholecystectomy with temporal + instrument labels;
- **HeiChole** — multicentre workflow/action/instrument labels;
- **MultiBypass140** — explicit two-centre phase/step design, subject to current data-access repair.

### Rule
No target-centre procedures may influence model selection in a true DG test.

If target data are used, label the experiment as adaptation, not domain generalization.

## S1-B — procedure/domain shift

For spatial perception, ROBUST-MIS/HeiCo provides an established staged domain-gap benchmark.

For cross-procedure use of P0.3 datasets, label compatibility must be checked before any metric is interpreted.

## S1-C — acquisition/device shift

Where metadata permit:
- camera/recording-system holdout;
- temporal external cohort;
- instrument-version/vendor shift.

This is supported by Kitaguchi and recent endoscopic-spine evidence.

---

# 4. S2 — controlled single visual shifts

## Core surgical-specific set

These have direct surgical robustness precedent and should be carried forward:

### V1 — low illumination
Evidence: SegSTRONG-C, CaRTS.

### V2 — smoke / cautery smoke
Evidence: SegSTRONG-C, CaRTS, Endo-C6.

### V3 — blood / bleeding / partial occlusion
Evidence: SegSTRONG-C, CaRTS; observed real hard cases in CholecInstanceSeg.

## Additional clinically plausible set

### V4 — motion blur
Evidence: Endo-C6 + real surgical hard cases + adjacent calibrated endoscopy literature.

### V5 — defocus
Evidence: Endo-C6 + adjacent calibrated endoscopy literature.

### V6 — colour / white-balance / photometric shift
Evidence: natural inter-institutional endoscopic-spine colour shift; adjacent controlled robustness protocols.

### V7 — compression
Evidence: adjacent endoscopy robustness. Exact **video** codec/bitrate implementation must wait for P0.6.

### V8 — resolution reduction
Evidence: adjacent endoscopy robustness; plausible video-pipeline effect but not assumed to be network-caused.

---

# 5. Severity policy

Do **not** use arbitrary “1–5” labels with undocumented parameters.

For every operator save:

```text
operator_name
implementation_version
parameter_value
severity_label
example_frame_ids
random_seed
source_video_id
```

A working severity structure may use:

- `0` clean;
- `1` mild / high-quality plausible;
- `2` moderate / deployment plausible;
- `3` strong / deployment-edge;
- `4` stress-test extreme.

But exact parameter boundaries are **not fixed in P0.4**.

They should be calibrated using:
1. direct surgical challenge parameters where available;
2. observed distributions in natural external datasets;
3. adjacent clinically calibrated endoscopy protocols as methodological guidance;
4. surgical-domain expert review if a publication will call a level “clinically plausible.”

Stress-test levels must be reported separately from deployment-plausible levels.

---

# 6. S3 — controlled temporal/video shifts

P0.4 authorizes the **research questions**, not the final parameters.

Candidate mechanisms:

### T1 — deterministic reduced sampling
Useful baseline for understanding temporal-context dependence.

### T2 — independent missing-frame events
Only after P0.6 establishes how this relates to decoded stream behavior.

### T3 — burst missing frames
Potential analogue of burst packet-loss consequences; Endo-C6 establishes emerging precedent.

### T4 — freeze / last-frame hold
Candidate decoded-stream behavior; requires network/codec justification.

### T5 — irregular timing / jitter-inspired sampling
Requires P0.6 mapping.

### T6 — context truncation
Useful for temporal phase/VLM models independent of networking.

## Non-negotiable wording

Do not write:

> “5% packet loss = drop 5% of video frames.”

unless the transport/codec model actually supports that mapping.

Network packet loss, decoder concealment, retransmission, GOP structure and output-frame loss are different variables.

---

# 7. S4 — compound shifts

## C-A — visual + visual
Allowed after single-factor baselines are established.

Examples:
- smoke + low illumination;
- blood + motion blur;
- colour shift + compression.

## C-B — natural + controlled
Example:
- unseen centre + smoke perturbation.

This tests whether a synthetic stressor has a larger effect after an already-existing natural shift.

## C-C — visual + temporal/network
Potential Track A focus, but **blocked until P0.6/P0.7**.

Examples to consider later:
- smoke × burst frame loss;
- low light × bitrate/compression degradation;
- natural centre shift × temporal delivery degradation.

---

# 8. Interaction analysis

A compound study should test interaction, not merely list combined scores.

For a task loss function \(L\):

```text
interaction(A,B) =
    [L(A+B) - L(clean)]
    - [L(A) - L(clean)]
    - [L(B) - L(clean)]
```

This simple additive reference is not a universal statistical model, but it illustrates the question:

> Is the joint degradation worse (or different) than expected from each factor alone?

A final analysis can use regression/ANOVA/mixed effects depending on the experimental structure.

---

# 9. Candidate task alignment

## Phase/workflow recognition
Most informative shifts:
- centre/workflow;
- reduced sampling/context;
- burst missing frames;
- compression/low visibility when visual features matter.

## Instrument/anatomy segmentation
Most informative shifts:
- smoke;
- blood;
- low illumination;
- blur;
- colour/device;
- compression/resolution;
- natural procedure/site shift.

## Temporal VLM
Endo-C6 already covers several visual corruptions + packet loss, so a future project using this task must justify a substantially different question.

---

# 10. Gate to P0.7

The final shift protocol may be approved only when:

- P0.5 identifies reliability metrics that are valid for the selected task;
- P0.6 supplies defensible network/codec/temporal mappings;
- P0.7 confirms the task × dataset × shift × reliability intersection is not already saturated.

P0.4 therefore narrows the candidate space without freezing it.
