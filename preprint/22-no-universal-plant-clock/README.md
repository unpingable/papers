# No Universal Plant Clock: Temporal Failure Geometry in Distributed Control Systems

**Author:** James Beck
**Status:** Published (Zenodo v1.1, 2026-04-20). Initial release: 2026-03-19 (v1.0).
**DOI (concept, resolves to latest):** [10.5281/zenodo.19119617](https://doi.org/10.5281/zenodo.19119617)
**DOI (v1.1 version):** [10.5281/zenodo.19671885](https://doi.org/10.5281/zenodo.19671885)

## Abstract

Modern distributed systems routinely behave as though they possess a shared present, interchangeable clocks, fresh state observations, and timely control channels. In practice, none of these assumptions is guaranteed. This paper introduces a four-layer model of temporal failure in distributed control systems: (1) gauge mismatch in the construction of shared temporal reference frames, (2) clock divergence in the accumulation of local elapsed time, (3) retarded-state estimation under delayed observation, and (4) delayed actuation in closed-loop control. The framework treats temporal coherence not as a metaphysical property but as an operational constraint and, in many systems, a scarce control resource. We introduce characteristic timescale ratios and show that the dominant failure mode in a given system is determined by which ratio has the least remaining margin to its critical threshold.

## Formalization Status

A parallel Lean formalization of the Δt framework applies the same scope discipline this paper polices in prose. Cashout classes: **certify** + **bridge artifact**.

Formalized anchors relevant to this paper:

- `persistence_normalizes` axiom in `TaxonomyGraph.lean` — explicitly marks where static formalization ends and temporal/dynamic claims would require different machinery. Paper 22 occupies the temporal-claim side of that boundary.
- Three-terminal-families result in `TaxonomyGraph.lean` — structurally analogous "no universal X, multiple families" pattern at the failure-taxonomy layer (not a direct warrant for this paper's specific claims, but consistent with the anti-universalism framing).

v1.1 release: §6.4 Lean-formalization paragraph added; references [1] and [3] corrected. No abstract or conclusion changes. Published to Zenodo 2026-04-20 (version DOI [10.5281/zenodo.19671885](https://doi.org/10.5281/zenodo.19671885)). See [`docs/formalization-index.md`](../../docs/formalization-index.md) for the full crosswalk and `NOTES.md` for the 2026-04-20 changelog entries.

## Key Contributions

1. Four-layer decomposition of temporal failure (gauge / clock / estimation / actuation) as operationally distinct engineering constraints with different detection signatures, consequences, and mitigations.
2. Timescale ratio analysis as a diagnostic: observation latency, actuation latency, synchronization uncertainty, and contract duration, all relative to plant dynamics. The ratio with the least margin to its critical threshold determines the dominant failure mode.
3. Temporal coherence as a scarce control resource — budgeted, measured, allocated, and governed — rather than an assumed property.

## Files

| File | Description |
|------|-------------|
| `no_universal_plant_clock.md` | Paper source (Markdown) |
| `no_universal_plant_clock.pdf` | Compiled PDF |
| `metadata.yaml` | Paper metadata |
| `NOTES.md` | Working notes, outline, and pre-release changelog |

## Build

```bash
pandoc no_universal_plant_clock.md -o no_universal_plant_clock.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Libertinus Serif" \
  -V mathfont="Libertinus Math" \
  -V monofont="Libertinus Mono" \
  -V geometry:margin=1in \
  --toc -V colorlinks=true
```

## Related Papers

- **Paper 6** — Temporal Closure Requirements for Synthetic Coherence ([doi:10.5281/zenodo.17849277](https://doi.org/10.5281/zenodo.17849277))
- **Paper 7** — Δt-Constrained Inference
- **Paper 14** — The Temporal Attack Surface ([doi:10.5281/zenodo.18680816](https://doi.org/10.5281/zenodo.18680816))
- **Paper 15** — Cybernetic Fault Domains ([doi:10.5281/zenodo.18686130](https://doi.org/10.5281/zenodo.18686130))
- **Paper 16** — The Gain Geometry of Temporal Mismatch ([doi:10.5281/zenodo.18717619](https://doi.org/10.5281/zenodo.18717619))
