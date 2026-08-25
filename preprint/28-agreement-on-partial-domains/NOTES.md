# Paper 28 — Working notes

## Status

**v0.1 draft — 2026-08-25.** The manuscript has been extracted from the closed
formal result and paper-triage records. No new theorem was proved during this
drafting pass. An 11-page local review PDF exists; no DOI, Zenodo deposit,
release tag, or portable Lean artifact exists yet.

## Frozen novelty calibration

The intended classification is:

> **known combination, novel formal monitoring formulation**

Do not promote this into “new combinatorics.” The closest established
neighborhoods are:

- compatibility of partial functions as agreement on common domains;
- tolerance/compatibility relations and maximal blocks;
- compatibility classes in incompletely specified machines;
- compatibility of partial words;
- classical Δ-system/common-root set families;
- Myhill–Nerode-shaped future equivalence;
- local-to-global agreement testing.

The exact uniformly quantified biconditional was not located in the bounded
prior-art search, but its proof is an elementary mediator-hole argument. The
paper must remain useful if a reviewer identifies it as folklore.

## Formal custody

The manuscript reconstructs theorem statements from development evidence
commit:

```text
45015037ac78650c29a74ca7a3558ad3b972d0e8
```

The paper-triage record was frozen at:

```text
869cd538830663a704510537de6e378caa98dc41
```

The portable Lean artifact has not yet been extracted or tagged. Until that is
done, the paper is a prose draft backed by verified development evidence, not a
self-contained release artifact.

## Deliberate exclusions

- signed-walk exactness;
- empirical activation/operator studies;
- corroboration and custody repairs;
- obligation-tag and aliasing campaigns;
- campaign/governor chronology;
- fixed-decision-label characterization outside the Δ-system regime.

The frozen empirical standing is not changed by this paper:

```text
FORMAL-ROLE-PREEXPOSURE-VERIFIER-CUSTODY-FAILED
```

## Release checklist

- [ ] Cold mathematical edit against the exact Lean declarations.
- [ ] Extract the minimal portable Lean module and its dependencies.
- [ ] Add a replay script with pinned Lean/Mathlib revisions.
- [ ] Run the replay from a fresh clone or release bundle.
- [ ] Resolve or reserve a Zenodo DOI.
- [ ] Replace null DOI/Zenodo metadata.
- [x] Render and inspect the v0.1 draft PDF (11 pages, XeLaTeX via Pandoc).
- [ ] Re-render the release PDF after DOI/artifact links are frozen.
- [ ] Re-run DOI and citation checks.
- [ ] Regenerate the corpus index without overwriting unrelated work.
- [ ] Add the public artifact URL and release/tag hash.
- [ ] Upload the paper and artifact, then freeze v1.0 source metadata.

Human review is welcome but is not a release gate for a Zenodo preprint.

## External review corrections

The 2026-08-25 review pass produced four bounded corrections:

- corrected the authors of Bartol et al., “On the coverings by tolerance
  classes”;
- exposed the operational Lean definition of `FutureSufficient` before giving
  its quotient-kernel characterization;
- clarified the static `ProfileCompatible` and native finite-word
  `CommonCompatible` roles;
- added one sentence explaining the Paper 28 series number.

The review examined an earlier staging snapshot. Its math-spacing and
“kernel” spelling reports had already been corrected before the first PDF
render. The portable artifact remains the only substantive release blocker.

## Draft conformance stops

Two repository-wide checks are intentionally not green at v0.1:

1. `tools/metadata_schema.py` requires a Zenodo-form DOI and record URL for
   every numbered preprint. It reports only the two intentionally null P28
   publication fields. Inventing placeholders would be less conformant than
   retaining the stop until a record is reserved.
2. `tools/build_corpus_index.py --check` reports the generated corpus index as
   stale because P28 is not registered there yet. The existing index already
   carries unrelated in-progress edits, so this drafting pass did not
   regenerate or overwrite it.

The v0.1 manuscript itself renders successfully to an 11-page PDF, and the
PDF-freshness checker reports both the manuscript and formal-artifact companion
as current. Repository-wide stale PDFs inherited from other papers are outside
this draft's custody.
