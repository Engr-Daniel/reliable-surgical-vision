# P0.3 Dataset Evidence Audit

## Audit decision

P0.3 is **complete at the dataset-feasibility reconnaissance level**.

The audit answers whether the programme has viable data pathways and what constraints must be carried into later phases. It does not authorize a final Phase 1 dataset choice before P0.4–P0.7.

## Audit population

- 18 candidate datasets audited in depth
- 36 retained evidence sources
- 8 excluded/deferred resource categories

The candidate set intentionally spans:
- temporal workflow;
- dense spatial perception;
- human robot-assisted surgery;
- multicentre natural shift;
- procedure-domain shift;
- robotic training resources.

## Confidence by audit dimension

| Dimension | Assessment | Main limitation |
|---|---|---|
| Dataset identity/task mapping | High | Some challenge resources change over time |
| Access route | High for working shortlist | Request/registration approval still must be obtained |
| Licence/DUA | High where official terms are explicit | CholecSeg8k/CaDIS/legacy EndoVis require re-verification before use |
| Provenance overlap | High for major CAMMA lineage | Exact Endoscapes pairwise overlap IDs still need provider overlap map at experiment setup |
| Split integrity | High for official benchmark splits | Custom splits must preserve procedures and centres |
| Temporal suitability | High | Frame-only releases cannot support true video-timing experiments |
| Compute/storage feasibility | Moderate–High | Download sizes/links can change; MultiBypass currently has an open archive issue |
| Final dataset choice | Intentionally unresolved | Requires P0.4–P0.7 |

## Major corrections enforced by P0.3

1. **Cross-dataset is not automatically cross-domain.**
2. CholecT50, CholecSeg8k and CholecInstanceSeg cannot be treated as independent of Cholec80.
3. Dataset/article/code licences are tracked separately.
4. Endoscapes access is treated according to the actual route used; PhysioNet-hosted files require DUA.
5. MultiBypass140 is scientifically valuable but currently placed on operational hold until archive integrity is verified.
6. CaDIS is not called “immediately available” while the official page still shows a pending download link.
7. Only genuine sequence/full-video datasets are considered suitable for later temporal/network manipulation.
8. Final selection is deferred, despite a working shortlist.

## Gate recommendation

P0.3 can be closed and marked complete. P0.4 may begin.

Before any dataset is downloaded for experiments, the `dataset selection gate` in `dataset-shortlist.md` must be rechecked.
