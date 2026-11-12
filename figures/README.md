# Figures

Original diagrams used in the README files. Regenerate with:

```bash
python3 figures/make_figures.py
```

| File | Shows | Data source |
|---|---|---|
| `fig1-research-question.svg` | The primary question (RQ1) as a pipeline: video → encoder → network → receiver → decoder → phase model → reliability monitor (V0/V1 vs N1/N2) | `literature/intersection-analysis/revised-research-questions.md` |
| `fig2-evidence-landscape.svg` | Occupancy of the 26 rated intersections (saturated / occupied / partial / not found) | **generated from** `literature/intersection-analysis/intersection-map.csv` |
| `fig3-track-merge.svg` | How Tracks A–C became RQ1–RQ3 of one integrated study | `literature/intersection-analysis/track-decision.md` |
| `fig4-roadmap.svg` | Phases 0–7 and task-level progress | `TASK.md`, `ROADMAP.md` |

**Design notes.** The figures use a blue ordinal ramp for evidence occupancy and reserve orange for network/telemetry information. Every tile and arrow also carries a text label, so no meaning depends on colour alone. "Not found" tiles use a dashed outline. The underlying data are always available as CSV/Markdown tables.
