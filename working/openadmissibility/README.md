# OpenAdmissibility — staging directory

**Status:** working drafts. Not published, not promised, not a root
`whitepapers/` directory yet — that becomes earned when a draft actually
ships to a venue, per ratify-lazily. **Filed:** 2026-07-09.

OpenAdmissibility (OA) is the public-facing name for the admissibility ABI:
a small standard surface for profile-scoped reliance decisions, in the
spirit of OpenTelemetry's relationship to telemetry. OTel answers *what
happened*; OA answers *what may be relied on, by whom, under which profile,
for which claim or effect — and what structured refusal follows if not.*

## The publication ladder (whitepaper first, IETF last)

```text
1. Problem statement            → problem-statement.md (THIS PASS)
2. Artifact envelope + refusal ABI + corpus note
                                → substrate EXISTS: openadmissibility-skeleton
                                  (spec/ 000–080, schemas/, corpus/v0.1,
                                  static linter; currently a zip in
                                  ~/git/rrp-notes/)
3. Golden corpus + reference checker
                                → substrate EXISTS: ~/git/rrp (Python
                                  reference checker + Rust parity, 33 local
                                  + 23 bridge corpus cases, obstruction
                                  ABIs) — not yet public
4. Multiple implementations / conformance story
                                → future; the Python/Rust parity pair is
                                  the in-house seed
5. Standards-body draft         → downstream evidence of usefulness, not
                                  the birth canal; explicitly deferred
```

The ladder is currently **inverted**: rungs 2–4 have working substrate and
rung 1 did not exist. This directory fixes rung 1. Do not let the existence
of substrate rush rungs 2–5 — each is a separate minting decision
(publishing the skeleton as a repo, publishing RRP, naming conformance).

## Asset inventory (where the pieces live)

| Piece | Where | Status |
| --- | --- | --- |
| Applicability map (audience-shaped framings, analogues, non-goals) | `working/where-admissibility-fits.md` (+ `-candidates.md`) | working note, the source this compresses |
| Positioning (5th category: admissibility beside authn/authz/accounting/attestation, with the Cedar falsifier) | `working/admissibility-as-pre-authorization-layer.md` | positioning note |
| Prior-art map (representation buckets; *prior art represents, refusal kernels forbid conversions*) | `working/tooltheory/admissibility-related-work-map.md` | working note |
| Spec skeleton (thesis, scope, canonical JSON, core objects, artifacts, obstruction codes, trace model, conformance, OTel relationship; JSON schemas; 1 permit + 10 refusal corpus) | `~/git/rrp-notes/openadmissibility-skeleton.zip` | skeleton, unminted |
| Reference gate prototype | `~/git/rrp` (local only) | prototype; validation green 2026-07-09 |
| Formal specimen laws (ten UNRATIFIED-CANDIDATE specimens incl. `RRPProfileSpecimen`, `ScopedCertification`, `TemporalBasis`) | `~/git/lean/LeanProofs/Admissibility/`, crosswalks in `~/git/lean/docs/` | v9-prepped; specimens do not testify for runtime compliance until cited |

## Discipline

- **The dock, not the law.** OA standardizes artifact shapes, digest
  identity, decisions, refusal codes, and the corpus format. Profiles are
  local law. The moment a draft starts standardizing an ontology of
  authority, the no-unifier discipline has failed and the draft is wrong.
- **Refusal is a first-class output.** Decision artifacts carry structured
  obstructions, never `ok: true` booleans.
- **Carry the falsifier.** The problem statement names what would deprecate
  the positioning (an authz layer that genuinely subsumes the admissibility
  moves without the reification gambit). Boundary objects that can't lose
  are pitches.
- **Adapters may sprawl. The kernel must not. Receipts must remain
  comparable. Fixtures must remain sovereign.**
