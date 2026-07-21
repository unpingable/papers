# Plain-language summary

**Companion to:** *Representational Invariance and the Observer Problem in Language Model Alignment* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Information can remain internally consistent while losing important commitments as it changes form. A detailed operating policy may become a summary that keeps the purpose but drops edge cases, prohibitions, logging duties, or dependencies. Nothing in the summary need be an explicit contradiction. The control surface has nevertheless changed.

The paper calls this representational incoherence and proposes measuring it at the level of commitments. Each commitment is described by its claim, force, type, and dependencies; a transformation may preserve, weaken, drop, contradict, or inject one. In a worked cache-policy study, aggressive compression and formalization lose substantial operational detail while translation preserves nearly all tracked commitments. The paper calls the resulting measurable loss “commitment shear.”

This gives specification and policy authors a stronger review standard than topical similarity or fluent restatement. A consequential transformation needs an explicit preservation contract: what must survive, what loss is permitted, and how omissions or additions will be detected. It also makes the observer part of the system: some checking process must decide what counts as equivalent and notice losses that the generator does not report.

## Claim boundary

The measurements come from one technical specification, same-model two-pass commitment extraction, three transform types, and three runs per type. The results are a specimen, not a general rate for all models or domains.

The manuscript’s categorical explanation also requires correction. A lossy map can still be functorial: functoriality, faithfulness, exact recovery, and preservation of the selected commitment relation are different properties. The reported loss measurements do not establish that the transformations are “generally not functors.” That passage should not be used as the warrant for the paper’s empirical finding.

## Read the paper

- [Manuscript source](delta_r_paper.md)
- [Rendered PDF](delta_r_paper.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18071264)
- [Zenodo record](https://zenodo.org/records/18071265)
