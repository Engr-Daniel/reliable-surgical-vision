# P0.3 Research Question Answer Matrix

## RQ1 — Which datasets are viable for the candidate surgical-CV tasks?

**Answer:** No single dataset covers the programme's temporal, spatial, robotic and multicentre needs. Cholec80 is a strong temporal/workflow development resource; SAR-RARP50 directly represents human robot-assisted segmentation/action; Endoscapes supplies rich anatomy/instrument/safety labels; PhaKIR provides unusually valuable multicentre full-video phase + instrument annotations. HeiChole, ROBUST-MIS, AutoLaparo and MultiBypass140 add natural-shift validation value.

**Evidence:** DS01, DS05–DS10, DS13.  
**Detailed:** `dataset-registry.csv`, `dataset-shortlist.md`.

---

## RQ2 — What are the access, licence and redistribution constraints?

**Answer:** Most mature candidates are restricted to non-commercial research, frequently under CC BY-NC-SA 4.0. Access models vary substantially: direct public archives (SAR-RARP50, SurgVU), request forms (Cholec80, AutoLaparo, JIGSAWS), controlled access (PhaKIR), registered challenge platforms (ESAD, ROBUST-MIS), and signed DUA (current PhysioNet Endoscapes files). Article or code licences must not be substituted for data licences.

**Evidence:** D01–D02, D04, D08–D09, D12, D14, D16, D19, D22–D25, D28–D29, D32, D35.  
**Detailed:** `access-license-audit.csv`.

---

## RQ3 — Which datasets share source videos or derived frames?

**Answer:** The major leakage cluster is the CAMMA cholecystectomy lineage. CholecT50 includes 45 Cholec80 videos; CholecSeg8k uses 17 Cholec80 videos; CholecInstanceSeg combines CholecT50-, CholecSeg8k- and Cholec80-derived imagery. CAMMA also explicitly warns researchers to inspect overlap among Cholec80, CholecT50 and Endoscapes. CaDIS is derived from the CATARACTS training videos.

**Evidence:** D04, D06–D08, D29–D31.  
**Detailed:** `provenance-overlap-map.md`.

---

## RQ4 — Are the split/site structures suitable for leakage-safe and natural-shift evaluation?

**Answer:** Yes for several candidates, if the canonical unit of separation is the procedure/video rather than the frame. PhaKIR and HeiChole expose three-centre structure; MultiBypass140 has 70 videos from each of two centres and explicit cross-centre protocols; ROBUST-MIS has increasing procedure-domain gap with no reported patient overlap. Cholec80 remains single-centre and therefore requires external data for natural shift.

**Evidence:** D11–D17, D27–D28.  
**Detailed:** `split-leakage-audit.csv`.

---

## RQ5 — How strong is the annotation/ground-truth coverage?

**Answer:** Annotation density is task dependent. Phase datasets can provide framewise labels across full procedures (Cholec80, PhaKIR), while segmentation datasets usually annotate sparse frames/subsets (Endoscapes Seg50, CholecSeg8k, PhaKIR 1-fps masks, ROBUST-MIS final frames of short clips). Dense masks are therefore excellent for visual reliability but do not automatically provide dense temporal ground truth. PhaKIR is unusually valuable because its full videos combine framewise phases with 1-fps instrument keypoints/masks.

**Evidence:** D01, D06–D12, D27–D30.  
**Detailed:** `dataset-registry.csv`, `temporal-network-suitability.csv`.

---

## RQ6 — Which datasets can support visual corruption and temporal/network degradation experiments?

**Answer:** Full-video datasets are required for realistic temporal manipulations such as frame dropping, irregular sampling, re-encoding or jitter-inspired delivery schedules. Cholec80, PhaKIR, HeiChole, MultiBypass140, AutoLaparo, SAR-RARP50, JIGSAWS, CATARACTS and SurgVU provide complete/sequence video suitable in principle. Frame-centric CholecSeg8k and CaDIS are primarily visual-corruption resources. Endoscapes is strong for spatial corruption; arbitrary full-video network emulation should wait until exact sequence availability is confirmed.

**Evidence:** dataset official pages and descriptors D01, D08–D36.  
**Detailed:** `temporal-network-suitability.csv`.

---

## RQ7 — What practical storage/access constraints matter?

**Answer:** Immediate feasibility differs sharply. SAR-RARP50 is comparatively manageable at about 31.25 GB across official train/test archives. Cholec80 is roughly 85 GB after extraction in the CAMMA TensorFlow packaging and recommends ~166 GB free during preparation. HeiChole's OPARA bundle is ~156 GB. MultiBypass140 requires hundreds of GB and currently has an unresolved archive-integrity issue. SurgVU contains >840 h of 60-fps video and is a high-storage/high-compute resource.

**Evidence:** D02, D14, D18, D22–D23, D35–D36.  
**Detailed:** `compute-access-feasibility.csv`.

---

## RQ8 — What is the evidence-backed working shortlist?

**Answer:** The working shortlist is complementary rather than a rank order:

- **Cholec80** — temporal/workflow development;
- **SAR-RARP50** — direct human robot-assisted action/segmentation;
- **Endoscapes2023** — anatomy/instrument/CVS spatial reliability;
- **PhaKIR** — multicentre temporal + spatial validation.

High-value validation resources include **HeiChole**, **HeiCo/ROBUST-MIS**, **AutoLaparo**, and **MultiBypass140** once its current download issue is resolved.

This is not the final Phase 1 dataset selection. P0.4–P0.7 remain mandatory gates.

**Detailed:** `dataset-shortlist.md`, `dataset-decision-matrix.csv`.

---

# P0.3 Overall Conclusion

Dataset availability is sufficient to support the research programme, but **provenance and access discipline are as important as model choice**.

The programme should proceed with a multi-dataset strategy in which:
1. development uses a mature task benchmark;
2. source-video overlap is explicitly excluded;
3. natural shift is tested using independent centre/procedure domains;
4. temporal/network experiments are performed only on genuine video sequences;
5. all licence/DUA terms are re-verified at the moment of download.

No final dataset or novelty claim is made at P0.3.
