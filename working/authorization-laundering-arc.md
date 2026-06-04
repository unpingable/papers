# Authorization-laundering arc (candidate)

**Status:** candidate compression, not promoted. Scratch/annex material only.
**Filed:** 2026-06-02
**Trigger:** cross-Claude reconnaissance after the three formal specimens shipped
2026-06-02 (AmendmentFragment / ContractionHinge / RetroactiveLegitimation) —
NQ-side review, AG-side gap-spec drafting, and ChatGPT review surfaced a
four-part topology not yet named in the public kernel docs.

## The candidate arc

A possible four-part arc, all naming distinct failure modes of the
authorization → consequence pipeline:

1. **Safety bridge** — authorized does not imply safe. A separate bridge
   predicate is required. *(Frontier 1; SafetyBridge family.)*
2. **Retroactive legitimation** — post-state validation does not imply
   pre-state authority. The forbidden move is dependency on the post-state
   produced by the operation, not late receipt generation in wall-clock time.
   *(RetroactiveLegitimation specimen.)*
3. **Amendment fragment** — policy mutation does not self-authorize.
   Authorization evidence must be typed at the source policy, not the
   post-amendment policy. *(AmendmentFragment specimen.)*
4. **Contraction hinge** — warrant reuse is a substructural / resource issue,
   not a free duplicate. *(ContractionHinge specimen.)*

Numbers 1–3 are "authorization ≠ X" cuts. Number 4 is a structural underlay
beneath all three.

## Why this is worth catching

The cabinet composed an arc the kernel docs do not yet name. The compression
is emergent — it surfaced across consumer-side review (NQ confirming nothing
to build), governor-side review (AG drafting GOV_GAP_RETROACTIVE_LEGITIMATION
+ AmendmentFragment pointer), and external review (ChatGPT tightening the
retroactive-legitimation framing).

The arc is not yet a theorem. It is not yet promoted to the public 1.0
surface. It is a candidate way the four boundaries compose.

## The load-bearing keeper

The retroactive-legitimation framing correction is the part most worth
locking down before it drifts:

> **The forbidden move is not late receipt generation in wall-clock time. It
> is dependency on the post-state produced by the operation.**

Compact form:

> **Post-state witness is not pre-state authority.**

The wall-clock framing ("witness must precede the act") will keep
regenerating itself because it sounds like obvious common sense — which is
exactly why it would quietly false-block legitimate late receipts that
testify to pre-state basis.

## What this is NOT

- Not a theorem. The four specimens are individually formal; the arc across
  them is a description, not a proof.
- Not a public promotion. Belongs in working notes until the kernel-overlap
  audit, exit criteria, and forcing-case gates all clear.
- Not authorization to grow a "Ministry of Policy Mutation." The
  AmendmentFragment cut refuses self-authorizing mutation; it does not
  authorize building a policy-amendment calculus.
- Not a Calculus 2.0 label. Safety-bridge family already explicitly disclaims
  that label; the arc inherits the same restraint.

## Promotion gates

Conditions under which this would be worth promoting from candidate to a
named compression in `WHAT-THIS-PROVES.md` or equivalent:

- Kernel-overlap audit confirms the arc is not already covered by an
  existing primitive under different vocabulary.
- A consumer cites the arc as the load-bearing structure (rather than citing
  the four specimens individually).
- A fifth boundary candidate either fits the arc or breaks it cleanly —
  current four feels suspiciously tidy; structural validation needs at least
  one stress test.

Until then: cite-don't-extract. The specimens stand on their own; the arc
sits in working notes.

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean` and family
- `~/git/lean/LeanProofs/Admissibility/RetroactiveLegitimation.lean`
- `~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`
- `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- `working/maximal-calculus-refused-map.md` — axis map containing the three June
  2026 specimens
- `working/maximal-calculus-amendment-cut.md` — case #3 promotion record
  carrying the (A1) candidate axiom that the AmendmentFragment specimen
  formalized
