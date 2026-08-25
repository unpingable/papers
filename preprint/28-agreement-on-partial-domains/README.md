# Paper 28: Agreement on Partial Domains — Canonical Abstraction and a Δ-System Criterion

> [Read the plain-language summary](PLAIN-LANGUAGE-SUMMARY.md) — an explanatory companion to the draft.

**Author:** James Beck
**Affiliation:** Independent Researcher
**Status:** v0.1 draft; not yet published
**Version:** 0.1
**Published:** not yet published
**DOI:** not yet assigned
**Zenodo record:** not yet created

## Center of gravity

When two partially informed states are called compatible because they agree on
every query both can answer, compatibility is reflexive and symmetric but need
not be transitive. The draft isolates two routes back to canonical abstraction:
preserve answerability itself in the semantics, or constrain answerability
domains to Δ-system/common-root geometry. In the static proposition-valued
profile model, that geometry is exactly what forces common-domain compatibility
to be transitive for every decision labeling.

The ingredients are classical. The proposed contribution is their
machine-checked formal-methods synthesis and the resulting architecture
boundary, not a claim of new combinatorics.

## Claim boundary

The draft does not establish a general theory of monitoring, distributed-system
safety, bisimulation, cardinality-minimal observation, or necessity of
Δ-system geometry for a single fixed decision model. It does not validate or
repair any empirical neural-model campaign.

The formal results were checked in the development environment, but the minimal
portable Lean artifact has not yet been extracted into this repository. See
[FORMAL-ARTIFACT.md](FORMAL-ARTIFACT.md).

## Files

| File | Role |
|---|---|
| `agreement_on_partial_domains.md` | Main manuscript draft |
| `agreement_on_partial_domains.pdf` | Rendered v0.1 draft PDF |
| `PLAIN-LANGUAGE-SUMMARY.md` | Reader-oriented companion; introduces no new claims |
| `FORMAL-ARTIFACT.md` | Theorem inventory, verification standing, and extraction boundary |
| `metadata.yaml` | Draft metadata; DOI and Zenodo fields intentionally null |
| `NOTES.md` | Drafting, novelty, and release checklist |
| `README.md` | This route sign |

## Citation

No citation is frozen before publication. A Zenodo citation block will be added
after the record and DOI exist.

## Keywords

Partial functions; compatibility relations; tolerance relations; partial
observations; canonical abstraction; Δ-systems; continuation semantics; Lean 4;
formal methods.
