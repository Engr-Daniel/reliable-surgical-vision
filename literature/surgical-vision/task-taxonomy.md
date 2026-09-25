# P0.2 Surgical Computer-Vision Task Taxonomy

| Task family | Typical input | Output | Temporal dependence | Annotation | Typical metrics | Representative datasets | Deployment relevance |
|---|---|---|---|---|---|---|---|
| Phase / workflow recognition | streaming/full video | phase per frame/time | High | phase intervals/frame labels | accuracy, F1, precision/recall, Jaccard; sometimes segmental metrics | Cholec80, M2CAI16, HeiChole, AutoLaparo, PhaKIR | Context-aware assistance/workflow monitoring |
| Step recognition | video | fine procedural step | High | step intervals | accuracy/F1/Jaccard/segmental | procedure-specific workflow sets | Fine contextual assistance |
| Action / gesture recognition | clips/video, sometimes kinematics | action/gesture | High | temporal segments | accuracy/F1/edit/segmental | JIGSAWS, HeiChole, SAR-RARP50 | Context/skill understanding |
| Instrument–verb–target triplets | frames/video | multi-label triplets | Medium–High | triplet labels | AP/mAP | CholecT50 | Fine tool–tissue interaction |
| Instrument presence | frame/video | multi-label tool presence | Low–Medium | presence labels | AP/mAP, precision, recall, F1 | Cholec80, CATARACTS, HeiChole | Workflow/context cue |
| Instrument detection | frames | boxes/classes | Low; tracking can add time | boxes | AP/mAP | ESAD/MESAD, Endoscapes | Localisation/AR/automation |
| Instrument semantic segmentation | frames/video | per-pixel class | Low–Medium | masks | Dice, IoU/mIoU, boundary metrics | EndoVis, CaDIS, CholecSeg8k | Precise localisation |
| Instrument instance segmentation | frames/video | separate instance masks | Low–Medium | instance masks | mask AP, Dice/IoU, challenge metrics | ROBUST-MIS, CholecInstanceSeg, PhaKIR | Multi-tool scene understanding |
| Instrument keypoint / pose | frames/video | tool keypoints | Medium | keypoints | benchmark-specific distance/PCK-like metrics | PhaKIR | Pose/localisation |
| Anatomy / scene segmentation | frames/video | anatomical/object masks | Low–Medium | semantic/instance masks | Dice, IoU/mIoU, boundary | CaDIS, AutoLaparo, Endoscapes | Navigation/overlays/safety |
| Safety-state assessment | frames/video | structured safety criteria | Medium | expert criteria + scene labels | accuracy/F1/AUROC + component metrics | Endoscapes-CVS | High-value surgeon-facing support |
| Skill assessment | video/kinematics | score/class | High | skill ratings | classification/regression/correlation | JIGSAWS, HeiChole | Training/assessment |
| Video-language representation / VQA | video + language | retrieval/text/zero-shot output | Medium–High | language paired with clips | task-specific | SurgVLP downstream sets | Emerging foundation-model direction |

## Important distinctions

- **Phase is not action:** phases are coarse, long procedural states; actions/gestures are finer and repeat within phases.
- **Presence is not detection is not segmentation:** these require different labels, metrics and uncertainty semantics.
- **Framewise prediction does not remove temporal reliability concerns:** segmentation/detection can flicker across frames or fail under dropped/irregular video.
- **Workflow is intrinsically temporal:** phase/action models are especially relevant to frame loss, irregular sampling and buffering.
