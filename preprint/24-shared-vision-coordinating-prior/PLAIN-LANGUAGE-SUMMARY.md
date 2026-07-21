# Plain-language summary

**Companion to:** *Shared Vision as Coordinating Prior: Aggregation-Layer Masking and the Witness-Filter Pathology* (Δt Paper 24)

**Version/status:** v1.0, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A shared vision can coordinate many people while hiding whether they understand it in the same way. An organization may solicit feedback, preserve formal dissent procedures, and still remain confidently wrong because disagreement disappears before governance sees it.

There are two places this can happen: reports can be compressed into a scalar that erases their structure, or the people carrying disconfirming information can be removed before aggregation.

The paper models differently biased observers updating one shared prior. It shows how balanced disagreement can cancel under simple aggregation even when the underlying reports remain meaningfully opposed. More seriously, if inclusion depends on agreement with the prior, dissenting witnesses are removed before aggregation. No downstream method can recover evidence it never receives, and even a one-time filtering event can leave a persistent error by making the surviving cohort the new equilibrium.

This yields two concrete design requirements: preserve reports per witness rather than immediately collapsing them to one score, and keep witness inclusion independent of agreement with the current shared view. The paper gives governance systems a way to distinguish genuine agreement from cancellation and prior curation. Feedback can exist procedurally while being absent from the state that actually governs decisions.

## Claim boundary

The no-scalar-free-lunch statement is a probe-backed conjecture, not a class-wide theorem. The alias-compatibility result is exact only in its stated equal-gain baseline regime and uses a local approximation for the shift. The joint architecture of per-witness preservation plus open inclusion is argued necessary for the modeled failures, but general sufficiency is not proved. Simulations are existence demonstrations, not organizational calibration. Later claim-indexed formal machinery does not supply the paper’s missing multiplicity or alignment-independent inclusion law.

The local manuscript corrects P23's DOI. The frozen Zenodo v1.0 source and PDF retain the original incorrect citation; this companion links both surfaces but does not silently treat the local correction as part of the published version.

## Read the paper

- [Manuscript source](shared_vision_coordinating_prior.md)
- [PDF](shared_vision_coordinating_prior.pdf)
- [Directory guide](README.md)
- [Version DOI](https://doi.org/10.5281/zenodo.19861996)
- [Concept DOI](https://doi.org/10.5281/zenodo.19861995)
