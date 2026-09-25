# P0.2 Surgical Computer-Vision Landscape

**Evidence cutoff:** 2026-09-25  
**Status:** Complete focused field reconnaissance

## Executive synthesis
Surgical computer vision is an interconnected stack of temporal workflow understanding, fine-grained activity recognition, instrument localisation, dense scene/anatomy perception, and emerging multimodal reasoning.

The public ecosystem is heavily concentrated in minimally invasive surgery—especially laparoscopic cholecystectomy. Cholec80 established phase/tool tasks; CholecT50 added instrument–verb–target interactions; CholecSeg8k, CholecInstanceSeg and Endoscapes extend the same broad procedure family toward dense scene perception and safety-state assessment.

Robot-assisted resources include JIGSAWS, EndoVis 2017/2018, ESAD, SAR-RARP50 and SurgVU, but their domains differ: training phantoms, porcine data, human surgery and robotic training video should not be treated as interchangeable.

Most importantly, multicentre HeiChole and PhaKIR show that strong single-centre performance does not guarantee cross-centre generalisation. PhaKIR reports poor cross-centre generalisability across phase recognition, keypoint estimation and instrument instance segmentation.

## 1. Workflow / phase recognition
This task predicts coarse procedural context and is intrinsically temporal. Representative progression:
- EndoNet — foundational visual/tool multitask workflow model and Cholec80;
- TeCNO — causal multi-stage temporal convolutions;
- Trans-SVNet — Transformer aggregation;
- LoViT — long-context local/global attention.

**Reliability relevance:** very high for frame loss, irregular sampling, buffering and context truncation.

## 2. Fine-grained actions and gestures
JIGSAWS provides gesture segmentation/recognition with video+kinematics; ESAD localises robotic prostatectomy actions; CholecT50/Rendezvous formalises instrument–verb–target triplets.

These tasks offer rich semantics but class imbalance, multi-label association and annotation ambiguity complicate reliability analysis.

## 3. Instrument perception
The field spans presence classification, boxes, keypoints, semantic masks and instance masks. EndoVis, ROBUST-MIS, CholecInstanceSeg and PhaKIR provide representative benchmarks.

Dense outputs are directly sensitive to blur, smoke, occlusion, compression and small-object visibility, making them strong later reliability candidates.

## 4. Anatomy / scene / safety understanding
CaDIS, AutoLaparo and Endoscapes move from tool localisation toward full scene interpretation. Endoscapes combines hepatocystic anatomy/instruments with expert critical-view-of-safety criteria.

This is clinically meaningful but raises annotation and safety complexity.

## 5. Foundation and video-language models
SurgicalSAM adapts SAM for surgical instruments. SurgVLP uses 1,400 surgical video lectures for video-language pretraining and downstream transfer.

These are important trends, but hidden pretraining distributions, prompting and immature reliability semantics make them less attractive as a first controlled benchmark.

## 6. Benchmark concentration and dependence
Cholecystectomy is overrepresented. Cholec80, CholecT50, CholecSeg8k and CholecInstanceSeg have source relationships/overlap that P0.3 must audit before treating them as independent domains.

## 7. Generalisation evidence
- **HeiChole:** 33 videos from three centres with phase/action/instrument/skill labels; results are substantially harder than commonly quoted single-centre benchmarks.
- **PhaKIR:** multicentre phase/keypoint/instance-segmentation challenge; poor cross-centre generalisability across all three tasks.
- **ROBUST-MIS:** increasing domain-gap stages and observed degradation.

These motivate P0.4 but do not prove a new research gap.

## 8. Evaluation risks
1. random frame splitting can leak procedure context;
2. identical metric names can use different computation protocols;
3. online and offline models are not equivalent for live assistance;
4. FPS depends on hardware/resolution/preprocessing and is not clinical readiness;
5. average metrics can hide rare-tool/small-anatomy failures.

## 9. Candidate families for later reliability research
### Temporal candidate: phase/workflow recognition
Pros: mature literature, public datasets, causal baselines, directly sensitive to temporal/network degradation.  
Cons: coarse labels, metric-protocol variation, cholecystectomy dominance.

### Spatial candidate: instrument/anatomy segmentation or detection
Pros: visually grounded, corruption-sensitive, mature dense metrics, human/robotic datasets, robustness benchmarks.  
Cons: structured-output calibration/conformal methods are more complex; small structures are difficult.

Action triplets, keypoints and CVS are valuable secondary candidates but add label/structured-output complexity.

## 10. P0.2 conclusion
The field is mature enough to provide reproducible predictive tasks and baselines, but not mature enough to equate strong in-distribution benchmark performance with deployment reliability.

**Methodological decision:** reuse established surgical-CV tasks and benchmark conventions; add shift and reliability evaluation later. Final dataset/model/task selection remains open until P0.3–P0.7.
