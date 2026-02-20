# The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems

**Author:** James Beck
**Published:** February 20 2026
**DOI:** 10.5281/zenodo.18717619
**Zenodo Record:** https://zenodo.org/records/18717619

## Abstract

The first fifteen papers in the Δt framework treat temporal mismatch as monotonically harmful: larger Δt produces more shear, more fragility, more collapse. This paper identifies a missing sign. Δt separation is not a monotone hazard; it is a baseline whose effect is signed by correlator properties, yielding three regimes: shear, leverage, and capture. The same temporal separation that produces destructive shear under weak coupling produces constructive leverage under strong coupling — higher epistemic resolution through structured disagreement across timescales. The critical variables are the system baseline B (timescale separation) and correlator quality **K** = (throughput T, fidelity F, authority A, cost budget C), which together determine whether mismatch becomes stress, power, or false coherence. Capture can inflate apparent fidelity by narrowing the representational alphabet — the metric is compromised by the same mechanism it is meant to detect. The paper reinterprets prior results as shear containment and capture dynamics, identifies the Paper 12 governor architecture as a correlator (not merely a brake), and derives a design principle: maximize baseline subject to correlator integrity.

## Key Contributions

1. Redefines Δt as a signed quantity (baseline, not cost) whose effect is determined by correlator quality, yielding three regimes: shear, leverage, and capture.
2. Introduces the correlator quality vector **K** = (T, F, A, C) as the determinant of regime membership.
3. Identifies capture (false leverage) as the shared primitive behind scalar reward collapse, platform enshittification, RLHF mode collapse, and institutional rigidity.
4. Reinterprets Papers 1–15 as instances of shear containment and capture dynamics within the gain geometry.
5. Reframes the BLI governor (Paper 12) as a correlator — an instrument that extracts epistemic resolution from the baseline between proposal speed and verification speed.

## File Guide

| File | Description |
|------|-------------|
| `signed_geometry.md` | Manuscript (markdown source) |
| `metadata.yaml` | Zenodo metadata |

## Build

```bash
pandoc signed_geometry.md -o signed_geometry.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Libertinus Serif" \
  -V mathfont="Libertinus Math" \
  -V monofont="Libertinus Mono" \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  --toc \
  -V colorlinks=true
```

Requires: pandoc 3.1+, xelatex, Libertinus fonts.

## Citation
```bibtex
@article{beck2026signed-geometry,
  author = {Beck, James},
  title = {The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems},
  year = {2026}
}
```

## Related Papers

- [The Coherence Criterion](../01-coherence-criterion/README.md) — spectral stability boundary reframed as leverage/shear boundary
- [Scalar Reward Collapse](../03-scalar-reward-collapse/README.md) — T-operator as capture-mode correlator
- [Control Laws for Hierarchical Kinetics](../05-control-laws-hierarchical-kinetics/README.md) — anti-patterns reinterpreted as baseline destruction
- [Temporal Closure Requirements](../06-temporal-closure-requirements/README.md) — RLHF mode collapse reframed in correlator terms
- [Bounded Lattice Inference](../12-bounded-lattice-inference/README.md) — governor as correlator (not merely a brake)
- [Cybernetic Fault Domains](../15-cybernetic-fault-domains/README.md) — shear condition at commitment boundary; gain geometry adds the leverage case

## Keywords

temporal coherence, interferometry, multi-timescale systems, translation bandwidth, reconciliation, cybernetics, control theory, epistemic systems, gain geometry, scalar reward collapse, institutional dynamics
