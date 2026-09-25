# Research Log

Use dated entries. Record questions, evidence, decisions, failed attempts, unexpected observations, and next actions.

## 2026-09-25 — Repository foundation

### Decision
Created a single research repository with three provisional research tracks rather than three long-lived paper branches.

### Rationale
The tracks share literature, datasets, reliability methods, evaluation infrastructure, and likely code. Their eventual publication boundaries should be determined by evidence rather than repository structure.

### Current state
Phase 0 — Research Foundation.

### Next action
Conduct Toumai technical-literature and architecture reconnaissance.

## 2026-09-25 — P0.2 Surgical Computer-Vision Landscape Reconnaissance completed

### Method
Focused evidence-backed field reconnaissance across peer-reviewed reviews, primary model/dataset papers, EndoVis/MICCAI challenge reports and official benchmark resources. Final audit: 45 records/categories, 33 retained and 12 excluded/deferred.

### Key findings
- The field spans workflow/phase, action/gesture/triplets, instrument presence/detection/keypoints/segmentation, anatomy/scene perception, safety state, skill and emerging video-language models.
- Public benchmarks are heavily concentrated in laparoscopic cholecystectomy; derived datasets may share source procedures.
- Workflow is intrinsically temporal; segmentation/detection provide complementary spatial failure modes.
- HeiChole and PhaKIR show important cross-centre generalisation limitations; PhaKIR reports poor cross-centre generalisability across all three of its tasks.
- ROBUST-MIS explicitly evaluates increasing domain gap and observes degradation.
- Metric implementations/protocols must be pinned; identical metric names do not ensure comparable results.
- Online/high-FPS benchmark capability is not clinical reliability.

### Decision
Phase/workflow recognition and instrument/anatomy segmentation/detection remain credible candidate task families. Final selection is deferred to P0.3–P0.7.

### Status
P0.2 passes its exit criteria. Suggested tag after commit/review: `v0.0.2`.

### Next
P0.3 — Dataset Reconnaissance.
