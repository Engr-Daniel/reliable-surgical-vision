# AGENT.md — Research Agent Instructions

## Mission

Support rigorous, reproducible research on reliable surgical computer vision under distribution shift, with particular interest in robot-assisted and tele-robotic surgery.

## Operating principles

- Do not invent citations, results, datasets, metrics, implementation details, or claims of novelty.
- Distinguish confirmed evidence from inference and open hypotheses.
- Trace substantive literature claims to primary sources whenever possible.
- Prefer peer-reviewed papers, official technical documentation, dataset papers, standards, and authoritative sources.
- Treat manufacturer claims as manufacturer claims unless independently validated.
- Never convert preliminary observations into conclusions without supporting experiments.
- Record important research decisions and their rationale.
- Preserve negative results.
- Prefer reproducible scripts/configurations over undocumented notebook-only experiments.
- Fix random seeds where appropriate and record software/hardware environments.
- Keep raw data immutable where licensing permits local storage.
- Never commit restricted datasets, credentials, secrets, patient information, or personally identifiable data.
- Verify dataset licences and permitted uses before acquisition or redistribution.
- Treat all medical implications cautiously; this repository is research, not clinical decision support.

## Research workflow

For each substantive question:

1. Define the question precisely.
2. Search and map prior work.
3. Identify what is established, disputed, and unknown.
4. Form a falsifiable hypothesis where appropriate.
5. Define datasets, baselines, shifts, metrics, and controls.
6. Predefine evaluation logic before inspecting final results when practical.
7. Run the smallest experiment capable of testing the hypothesis.
8. Record configuration and provenance.
9. Analyse uncertainty and failure cases.
10. Update the research log and relevant track documents.

## Git practice

`main` is the canonical research record. Use short-lived branches for concrete implementation or experiments, e.g.:

- `feature/smoke-corruption`
- `feature/network-emulator`
- `experiment/segmentation-baseline`
- `experiment/conformal-baseline`

Research tracks are directories, not long-lived Git branches.

## Scientific writing

Use precise language. Avoid “proves,” “solves,” “safe,” “robust,” or “state of the art” unless the evidence justifies the wording. State the evaluated population, dataset, task, shift, and conditions when reporting performance.

## Repository hygiene

Before merging work:
- tests should pass where tests exist;
- configurations should be saved;
- results should be reproducible or their nondeterminism documented;
- relevant documentation should be updated;
- generated artefacts should not replace source data or source code.
