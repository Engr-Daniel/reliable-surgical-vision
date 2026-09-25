# P0.2 Source Audit

## Decision
P0.2 is complete at the **focused field-reconnaissance** level, not as an exhaustive systematic review.

## Final audit set
- **33 retained sources/resources**
- **12 excluded/deferred categories**
- **45 total audit records/categories**

## Coverage assessment
| Area | Assessment |
|---|---|
| Workflow/phase | Strong: reviews + foundational/modern models |
| Actions/gestures/triplets | Strong representative coverage |
| Instrument detection/segmentation | Strong: reviews + EndoVis + ROBUST-MIS + CholecInstanceSeg + PhaKIR |
| Anatomy/scene | Strong representative: CaDIS, AutoLaparo, Endoscapes |
| Multicentre/generalisation | Strong: HeiChole, PhaKIR, ROBUST-MIS domain-gap design |
| Benchmark methodology | Strong: BIAS, reviews, Metrics Matter |
| Deployment | Moderate: online/real-time evidence exists; true clinical deployment remains limited |
| Foundation/VLM | Emerging; deliberately representative rather than exhaustive |

## Main caution
The field is highly concentrated around laparoscopic cholecystectomy, and several datasets derive from overlapping source videos. P0.3 must audit provenance/overlap before cross-dataset shift experiments.
