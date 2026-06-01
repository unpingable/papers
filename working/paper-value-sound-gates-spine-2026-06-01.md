# Paper spine — Value-Sound Gates

**Status:** Outline only (2026-06-01). Filed after the keystone re-framing
(see [axis-2-cross-axis-keystone.md](axis-2-cross-axis-keystone.md)) confirmed
the calculus is value-sound gating, not abstract non-surjectivity. Outline
not prose; do not polish until the spine survives review.

## Working title candidates (decide at draft time)

- **Value-Sound Gates for Authorization and Composition**
- **Witness-Gated Admissibility for Transition and Composition**

Both are dry, accurate, mildly municipal. *That is how we know they are
probably correct.*

## Naming stack — bounded sub-calculus, not maximal calculus

```
Current paper (this one):
  Value-Sound Gates for Authorization and Composition  (or sibling title)
  Scope: Axes 1–2; bounded sub-calculus; ships when ready.

Future synthesis (NOT this paper):
  An Admissibility Calculus
  Scope: opens only when self-amendment / frontier / evaluator-mutation
  forces inclusion. Filed as a slot, not an artifact. See
  [project-cross-axis-keystone].
```

No stolen valor from future-you. Current paper does not claim the maximal
calculus title.

## Thesis

Authorization and local bridge evidence are weak admissibility objects.
Strong admissibility requires boundary witnesses that gate those objects
into value-sound transition or composition families.

The witness **gates** (admits a subset), it does not **enrich** (decorate
within a fiber). The strong family is a strict sub-family of the weak,
characterized by the operation-specific value-soundness the witness
provides.

## Axis 1 — bridge witness gates transition value-soundness

`bridge : σ → α → Prop` is the gate witness. `SafetyEnv.preserves`
(`SafetyBridge.lean`) is the soundness theorem:

```
bridge s a ⟹ value s ≤ value (run s a)
```

`SafeStep.toAuthStep` is the forgetful map; `AuthorizationBridgeGap` /
`gap_blocks_safeStep_lift` exhibit weak objects outside the strong
family.

## Axis 2 — `MergeOk` gates reconciliation value-soundness

`MergeOk` is the gate witness (per-slice: `BudgetMergeOk`, `StaleMergeOk`,
`ConflictMergeOk`). The `*_restores` family (`ParameterizedMerge.lean`)
is the soundness theorem family:

```
MergeOk p a b  ⟹  the merge preserves the value-soundness obligation
                   for that slice.
```

For Budget and Conflict, the obligation is value preservation at the
merged endpoint. For Stale, the obligation is basis / continuation
readiness, shown value-relevant by the guard-collapse probe and the
`useEvidence` chain (`stale_basis_carries_useEvidence_value`); it is
**not** promoted to a second defended observable — the single
defended value (`E.value`) remains the only floor, and basis
conditions are guards.

Negative keepers (`locally_bridged_*_merge_*`) exhibit locally bridged
branches outside the strong family. Necessity verdict per
`ParameterizedMerge.lean`: characterization is schema not single
theorem (Budget/Conflict at value layer, Stale at basis layer).

## Keystone

The shared structure is **value-sound gating, not abstract
non-surjectivity**. The schema (`BoundaryWitness.lean`:
`ForgetfulWitness`, `BoundaryObstruction`, `HasSection`) types both
axes against a shared signature for exposition but is shape, not
content — classically equivalent at image and section levels (the
substrate is classical, so `HasSection ↔ surjective`; one direction
proven constructively as `boundaryObstruction_implies_no_section`,
the converse is the classical equivalence), both equivalent to
non-surjectivity, which is too weak (`Nat.succ` has it).
Value-soundness is what distinguishes the bridge / merge gates from
contentless maps; it lives per-axis because the value floor attaches
to different operations (transition vs. merge).

## Scope fence

> This paper is **not the full admissibility calculus**. It formalizes a
> bounded sub-calculus over transition and composition: weak
> admissibility objects become value-sound only when gated by explicit
> witnesses — and the necessity of that gating is demonstrated per case,
> not as a single universal law. Self-amendment, where the evaluator
> itself mutates, is outside scope and is treated separately when it
> forces inclusion.

Two clauses, both load-bearing. The "only when gated" clause carries the
paper's positive content (the witnesses are what make the gated
operations value-sound). The "per case, not universal" clause matches
what the Lean substrate actually proves: necessity is slice-indexed
(Budget/Conflict at value layer, Stale at basis layer; see the
necessity verdict in `ParameterizedMerge.lean`). The slice-indexedness
is itself one of the paper's findings — the rejection of forced
universality, learned twice (the arity finding, the `Obs` cut). Stating
the fence in matching terms is what keeps abstract and body honest under
review.

Concretely: Axis 3 (self-amendment / frontier mutation) is out. It
mutates the evaluator, not the evaluated transition/composition. The
maximal *An Admissibility Calculus* is the future synthesis that
absorbs Axis 3 when forced; this paper does not preempt it.

## What the paper does NOT do

- Does not propose an abstract keystone theorem. The keystone is
  exposition + per-axis soundness, not a single grand statement.
- Does not collapse the two operations (transition, merge) into one
  abstract "step." Different operations stay different — that
  difference is itself a load-bearing finding.
- Does not promote freshness or other basis-layer predicates into
  parallel defended observables. Single defended value; basis
  conditions are guards.
- Does not anticipate self-amendment.

## Open work to land before drafting

1. **No Lean blockers.** Formal substrate is closed: per-slice
   value-sound gating, necessity-as-schema verdict, basis-layer
   companion, keystone exposition. Remaining work is exposition —
   abstract, contribution list, section ordering, bibliography. "No
   blockers" means substrate-complete, not paper-magically-done.
2. Decide working title at draft time.
3. **Section order (recommended).** Working draft order — subject to
   revision once the abstract drafts:

   ```
   1. Introduction (frames the value-sound gate pattern at the thesis
      altitude; no separate "abstract pattern" section)
   2. Axis 1: authorization gated by bridge evidence
   3. Axis 2: composition gated by merge evidence
   4. The boundary-witness schema, and why it isn't the keystone
   5. Scope: why self-amendment is out
   6. Related work
   7. Conclusion
   ```

   §4 is the load-bearing rhetorical move: it preempts the
   DeepSeek-style attack *"isn't this just non-surjectivity?"* by
   explicitly distinguishing exposition shape (the schema) from
   content (per-axis value-sound gating). Putting it AFTER Axes 1–2
   (Claude-web's correction over ChatGPT's earlier "pattern-first"
   ordering) is deliberate: leading with the schema risks the reader
   forming "this is just non-surjectivity dressed up" before they
   see the concrete value-soundness that rescues it. Arriving at the
   schema *last* lets its thinness be the deliberate deflation move
   rather than a bad first impression to dig out of.
4. **Optional, not blocking.** A third Axis 2 specimen at the schema
   level (Stale or Conflict in `BoundaryWitness.lean`) to confirm the
   BudgetMerge wiring isn't a one-off. Promotion-gate, not blocker.
5. **Abstract + contribution list — DONE 2026-06-01.** First-pass
   draft landed at
   [paper-value-sound-gates-draft-2026-06-01.md](paper-value-sound-gates-draft-2026-06-01.md).
   ChatGPT's sharper variant + Claude-web's four precision edits
   (freshness-basis restoration, `Nat.succ`-as-trivial-witness
   clarification, necessity-clause alignment, scope-mechanism
   sharpening). One controlling version, no model-split at this
   stage. Survival test passed: title and thesis both wrote cleanly.
6. **Next concrete move:** body prose for §2 (Axis 1) and §3 (Axis 2)
   per the recommended section order. Defer §1 (introduction) until
   the body lands — introductions are easier to write against
   complete bodies than against sketches.

## After-action (once the paper ships)

- **Doc / README sweep.** Update Lean `Admissibility/README.md` (if it
  indexes modules) to list `ParameterizedMerge` / `BoundaryWitness`
  with their then-current status (scratch / not-root-wired, or
  promoted if a consumer landed). Update `WHAT-THE-LEAN-STACK-PROVES`
  if the paper draft surfaces a 1.0-surface claim worth advertising.
  Update `PAPER-MAP` with the paper's Zenodo entry once published.
  Top-level papers `README` only if the paper changes the corpus
  positioning. *None of this is forced until the paper ships;
  promoting any of it now is advertising work that isn't done.*

## For the pocket — Axis 3 boundary as seam, not wall

Not for the paper. Carry it in case a reviewer presses on the scope fence.

The fence excludes Axis 3 on the grounds that self-amendment "mutates
the evaluator, not the evaluated transition/composition." Stated as a
clean dichotomy. The honest seam is slightly more nuanced: every gate
in this paper is sound for a value defined *outside* the gate (`value`
is part of the `SafetyEnv`, not part of the mutable state). Axis 3 is
the limit case where the gated action reaches into the value definition
itself — making `value` part of what mutates.

So the boundary is about **whether `value` is in the mutable state**,
not a metaphysical transition-vs-evaluator line. Two consequences worth
holding:

- **Defence under press.** If a reviewer asks "isn't a sufficiently
  powerful composition already able to perturb the value function?",
  the prepared answer is *not* about composition's power — it is
  about what's in the mutable state vs. what isn't. The Axis 2 merges
  perturb branch state; they do not perturb `E.value`. That's the
  fence's actual content.
- **Where the future synthesis genuinely lives.** Not "add a third
  axis" alongside transition and composition. The future synthesis is
  *what happens to value-soundness when `value` is no longer external*
  — when the evaluator and the evaluated share state. That is the
  honest seam this paper closes against, and it is also why "An
  Admissibility Calculus" earns its title only after that seam is
  opened.

This belongs in the paper's pocket, not its body. The current paper's
scope fence stays clean and dichotomous; the spectrum thinking is for
press defence and for naming the future synthesis correctly.

## Verdict

**It is now one paper-shaped object over Axes 1–2.** Not "Admissibility
Suite" (was a cabinet badge); not "Admissibility Calculus" (premature,
future synthesis); current paper is **Value-Sound Gates for
Authorization and Composition** (or sibling). Bounded, accurate,
ship-able.

## Related records

- Keystone verdict: [axis-2-cross-axis-keystone.md](axis-2-cross-axis-keystone.md)
- Axis 2 composition boundary work: [axis-2-composition-boundary.md](axis-2-composition-boundary.md)
- Earlier suite plan (superseded by this spine): [calculus-suite-map.md](calculus-suite-map.md)
- Earlier safety-axis preprint spine (also superseded — this paper subsumes the safety-axis kernel into the broader Axes 1–2 calculus): [calculus-paper-spine-2026-05-28.md](calculus-paper-spine-2026-05-28.md)
