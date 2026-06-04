# Locality and Boundary Merge

Status: scratch / non-doctrinal / aperture diagnostic
Logged: 2026-05-21
Lives near: P28 candidate territory, downstream of [boundary-composition-investigation](../../../boundary-composition-investigation.md) → [boundary-composition-audit](../../../boundary-composition-audit.md). Direct continuation of the audit's "calculus question" thread.
Repo witnesses: `~/git/lean/LeanProofs/Admissibility/Composition.lean` (Slice 0, diagnostic) and `~/git/lean/LeanProofs/Admissibility/LocalBoundary.lean` (Slice 1 aperture, experimental). Neither file is imported into `LeanProofs.lean`; both sit alongside the `CrossBoundary*` sibling family outside the no-sorry kernel chain.
Program handle: candidate under `working/boundary-kernels-program-candidate.md`; this note is one specimen, not the program.

## Keeper

If the merged boundary authorizes the component step, locality has already been lost.

## Diagnostic sequence

Slice 0 introduced process syntax over the exposure-mint kernel: stop, expose-prefix, and parallel composition. The resulting composition theorem was intentionally vacuous: under a sealed global boundary, every process is safe, because every config mutation still passes through the existing kernel `Step` relation.

This is useful. It proves that process syntax is not yet composition.

The first attempted Slice 1 introduced local boundaries, but its `LocalDiscipline` predicate quantified over arbitrary ambient boundaries:

```lean
∀ (B : Boundary Domain), ...
```

That reintroduced the global oracle through the side door. A component was required to remain disciplined under any boundary whatsoever, rather than being authorized by its own local boundary and then judged against the merged/global view.

## Correct aperture

The first nontrivial calculus theorem should separate:

1. raw process capability,
2. local authorization,
3. composed execution,
4. global/merged safety judgment.

Minimal Slice 1 shape:

```lean
RawStep
LocalAllows
ComponentStep
MergeAdmissible.left_sound
MergeAdmissible.right_sound
composition_preserves_global_safety
```

A component step must be checked against the component's own local boundary:

```lean
RawStep P α P' →
LocalAllows lb₁ α →
ComponentStep (P | Q, c) (P' | Q, apply α c)
```

The merged boundary may judge global safety after the fact, but it must not authorize the local step.

## Non-goal

Do not encode the five bad cases yet:

- boundary collision
- authority widening
- projection laundering
- containment inversion
- ambient authority leak

Those are paper-shaped until the theorem aperture forces them into Lean preconditions.

## Doctrine

Process syntax alone does not create a calculus.

A calculus begins when component-local admissibility can compose without being replaced by ambient authority.

## Generator-test outcome (2026-05-21)

`composition_preserves_global_safety_aperture` in `LocalBoundary.lean` closed without `sorry`. The `MergeAdmissible.{left_sound, right_sound}` predicate, specified minimally as "locally authorized → globally safe under the merged partition," turned out to be exactly the obligation the theorem demands. Proof collapsed through it: `cases hStep` on `ComponentStep`, then `Finset.mem_insert.mp` and one application of the matching `left_sound` / `right_sound` field. The predicate was load-bearing, not decorative.

Keeper:

> The minimal merge predicate closed the first local-boundary composition theorem. This suggests the calculus aperture is not process syntax itself, but the soundness bridge from locally authorized component actions to globally safe merged observations.

Calibration:

> Do not generalize from closure too quickly. The theorem proves the aperture is well-shaped, not that the merge doctrine is complete.

The closure is a generator-test tick *for* the program-name candidate's compression value — it forced the right structure on the first honest try. It is not ratification, and it is not a license to start summoning calculus machinery on the assumption that the aperture will scale. The five bad cases and the necessity-by-counterexample obligation remain unspent.

## Status fence

- Not promotion. Not a ratified primitive.
- Working artifact for the boundary-calculus program candidate.
- Sibling specimen to the per-layer audit; the audit names *what can be called a boundary*, this note names *what would make composition non-trivial*.
- Necessity claim (each `MergeAdmissible` field is load-bearing under a counterexample) is the next obligation if this aperture survives further contact.
