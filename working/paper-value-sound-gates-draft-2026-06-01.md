# Paper draft v1 — abstract + contribution list

**Status:** First-pass draft (2026-06-01). Abstract and contribution list
only — no full prose yet. Spine:
[paper-value-sound-gates-spine-2026-06-01.md](paper-value-sound-gates-spine-2026-06-01.md).

**Provenance:** ChatGPT drafted both an "abstract fog" variant and a
sharper variant; operator picked the sharper one. Claude-web reviewed
and proposed four precision edits (three on the abstract, two on the
contribution list, one overlapping). Integrated here as the single
controlling version per operator instruction (no model split at this
stage).

## Working title

**Value-Sound Gates for Authorization and Composition**

## Abstract — draft v1

Authorization is not preservation, and local preservation is not
composition. This paper formalizes both claims in Lean 4 as a bounded
admissibility sub-calculus over transition and merge. The core pattern
is *value-sound gating*: weak admissibility objects may be
constructible without the witness that makes the relevant operation
value-preserving, while strong admissibility objects carry that witness
explicitly.

At the transition layer, an authorized step records permission to act,
while a bridged step additionally carries evidence that the action
preserves an externally supplied defended value. At the composition
layer, locally bridged branches do not by themselves determine whether
reconciliation is value-sound; additional merge-specific evidence is
required. We instantiate this with three merge specimens: shared-budget
overrun, stale-evidence reconciliation, and conflict-policy loss. One
specimen (stale evidence) gates at the level of *basis* for future
value rather than present value; freshness is treated as a guard for
value-preserving continuation, not as a second defended observable.

The paper deliberately does not treat the common forgetful-map
obstruction as the main theorem. Non-surjectivity and no-section
claims — classically equivalent here — are too weak: they hold for
trivial maps such as the successor on the naturals. The substantive
content is that the strong families are value-sound gates for specific
operations. This operation-specificity is itself a finding: transition
and merge cannot be collapsed into one abstract step without losing
the joint conditions that make composition meaningful.

The result is not the maximal admissibility calculus. It closes a
bounded fragment over authorization and composition under a fixed
evaluator. Self-amendment, where the evaluator itself mutates, is
left outside scope.

## Contribution list — draft v1

This paper makes four contributions.

1. **A Lean 4 safety gate for authorized transitions.**
   We formalize a transition-level distinction between authorized
   steps and bridged steps. Authorization supplies permission to act;
   bridge evidence supplies the value-preservation witness. The
   resulting strong family is value-sound by construction through
   `SafetyEnv.preserves`.

2. **A composition gate for locally bridged branches.**
   We show that local bridge evidence does not automatically survive
   reconciliation. Three specimens isolate distinct merge-boundary
   failures: shared-budget overrun, stale evidence at reconciliation
   time, and conflict-policy loss. Each specimen supplies both a
   negative case (the bust) and a restoration condition (the witness
   that blocks it).

3. **A bounded value-sound gating pattern.**
   We identify the shared structure between the transition and
   composition results: weak admissibility objects become value-sound
   only when admitted by explicit witnesses — with necessity
   demonstrated per operation and, for composition, per case rather
   than as a single universal law. The shared boundary-witness schema
   is expository rather than load-bearing; the content lives in the
   operation-specific soundness obligations.

4. **A scope boundary for the larger admissibility calculus.**
   We separate this bounded sub-calculus from future self-amendment
   work. The present paper studies transition and composition under a
   fixed evaluator — every gate is sound relative to an externally
   supplied value, and self-amendment is precisely the regime where
   that externality fails. Mutation of the evaluator itself belongs
   to the later maximal admissibility calculus, not this paper.

## Edits applied (audit trail)

Source: ChatGPT's sharper-variant abstract and contribution list.
Edits per Claude-web review:

- **Abstract paragraph 2 (added).** *"One specimen (stale evidence)
  gates at the level of basis for future value rather than present
  value; freshness is treated as a guard for value-preserving
  continuation, not as a second defended observable."* Restores the
  freshness-collapse finding that the sharper variant had dropped.
- **Abstract paragraph 3 (sharpened).** *"Non-surjectivity and
  no-section claims — classically equivalent here — are too weak:
  they hold for trivial maps such as the successor on the naturals."*
  Makes the weakness demonstrated rather than asserted; a reviewer
  who notices the schema is near-tautological sees the author
  noticed first.
- **Contribution 3 (necessity-clause alignment).** Added *"with
  necessity demonstrated per operation and, for composition, per
  case rather than as a single universal law."* Aligns with the
  `ParameterizedMerge.lean` schema-not-single-theorem necessity
  verdict so abstract and body agree before anyone diffs them.
- **Contribution 4 (scope-mechanism added).** Added *"every gate is
  sound relative to an externally supplied value, and self-amendment
  is precisely the regime where that externality fails."* Makes the
  fence principled rather than stipulated; names the actual seam
  (whether `value` is in the mutable state) rather than a
  metaphysical evaluator-vs-evaluated line.

## What this draft does NOT do yet

- Does not draft any of §1–§7 prose. Abstract + contribution list
  only, per the survival-test discipline (if either of these can't be
  written cleanly, the spine needs more work before drafting).
- Does not commit to a venue or page count. Title and venue posture
  remain per [[feedback-axis-1-venue-posture]] (Zenodo / arXiv-quality
  formal note).
- Does not absorb the "for the pocket" Axis-3 spectrum-vs-dichotomy
  reasoning from the spine into the abstract body. That stays in the
  pocket for press defence.

## Next concrete move

Abstract and contribution list are now the controlling first-pass.
Next step is body prose for §2 (Axis 1) and §3 (Axis 2) per the spine's
recommended ordering. Defer §1 (introduction) until after the body —
introductions are easier to write against complete bodies than against
sketches.

## Related records

- Spine: [paper-value-sound-gates-spine-2026-06-01.md](paper-value-sound-gates-spine-2026-06-01.md)
- Keystone verdict: [axis-2-cross-axis-keystone.md](axis-2-cross-axis-keystone.md)
- Axis 2 composition work: [axis-2-composition-boundary.md](axis-2-composition-boundary.md)
- Lean substrate: `~/git/lean/LeanProofs/Admissibility/` (`SafetyBridge.lean`, `ParameterizedMerge.lean`, `BoundaryWitness.lean`)
