# Plain-language summary

**Companion to:** *Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems*

**Artifact:** version 1.0 · preprint

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

An inference system can increase the certainty of its claims faster than its evidence improves. It may continue to look orderly and productive while becoming increasingly fragile: small changes in input expose that upper-level confidence has outrun lower-level support. The paper asks how to describe this “working until disturbed” condition.

The paper treats confidence and evidence as quantities that change over time. Its basic constraint says that confidence should not grow faster than a domain-specific multiple of the supporting evidence. When it does, the positive mismatch accumulates as “temporal debt.” Combined with a support cap and sensitivity to perturbation, this yields three proposed regimes: coherent inference, metastable inference that still looks plausible but has become fragile, and collapse where support disappears or small changes produce large swings.

The new capability is a diagnostic for the dangerous middle state. A pipeline need not be obviously wrong to be poorly supported; smooth output may conceal commitments that have outrun their basis. The paper suggests comparing the rate of commitment with the rate of evidential improvement and then perturbing the result. That makes “working until disturbed” a condition that can be investigated rather than dismissed as ordinary uncertainty.

## Claim boundary

The manuscript's paydown language is under mathematical correction. As currently defined,

`D(t) = ∫ max(0, dC/dτ - k·dE/dτ) dτ`

can only stay constant or increase. A period in which evidence catches up stops new accrual; it cannot reduce this `D(t)`. Until a separate discharge state or signed flow is defined, read `D` as cumulative gross violation mass, not an outstanding balance that can be repaid.

The confidence/evidence scalars, thresholds, and cross-domain substitutions also require calibration. They are diagnostic abstractions, not proof of factual correctness, claim-specific evidence, standing, authority, custody, or a universal collapse mechanism.

## Read the paper

- [Manuscript source](delta_t_theory_paper_updated.md)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.17857541](https://doi.org/10.5281/zenodo.17857541)
- [Zenodo record](https://zenodo.org/records/17857542)
