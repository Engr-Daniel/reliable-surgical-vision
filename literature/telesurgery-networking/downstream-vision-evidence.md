# P0.6 Downstream Surgical-Vision Evidence

## Question
What evidence connects telesurgical network conditions to downstream **computer-vision inference**, rather than only surgeon operability or image quality?

## Direct evidence found
### Endo-C6 / temporal surgical VLMs
The accepted MICCAI 2026 Endo-C6 work includes **packet-loss bursts** as one of six controlled endoscopy/video corruptions and shows that temporal VLMs can fail severely under corruption.

This is important prior art: broad claims that packet-loss-like video corruption has never been studied in surgical AI are no longer defensible.

### Boundary
Endo-C6 applies controlled clip corruptions. It does not establish that a given network packet-loss rate under a specified RTP/H.264/HEVC stack produces the same decoded-video corruption.

## Strong indirect evidence
Telesurgery studies repeatedly show network conditions can alter the video/operator experience:
- insufficient bandwidth can produce packet loss and image degradation;
- congestion can produce video freezing/degradation;
- adaptive compression can preserve operation at lower bandwidth by trading image clarity;
- satellite links can exhibit transient image disturbance/freezing;
- frame loss is measured in human clinical trials.

These observations support the **mechanistic plausibility** of a network→video→AI pathway but do not quantify downstream CV failure.

## What P0.6 did not establish
The retained evidence does not establish a mature benchmark that jointly provides:
1. measured or emulated network telemetry;
2. a real codec/transport/decoder path;
3. decoded surgical video;
4. a standard surgical-CV task such as phase recognition or tool/anatomy segmentation;
5. calibration/error/abstention outcomes;
6. a test of whether network telemetry adds predictive value beyond the received video.

This is the central P0.7 intersection to stress-test. It is **not yet a novelty claim**.
