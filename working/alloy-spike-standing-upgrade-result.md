# Alloy spike: standing-upgrade probe (result)

**Status:** spike complete 2026-06-03. Result note. Not doctrine.
**Plan:** `working/alloy-spike-standing-upgrade-plan.md`
**Spec:** `working/standing_upgrade_probe.als`
**Alloy run output:** `working/standing_upgrade_probe/` (receipt.json + per-probe solution files)

## Exportable lessons (the keeper lines)

> **Authority refusal is local; bootstrap prevention is architectural.**

> **The gate can refuse only what the surrounding transition system makes
> visible.**

Both compact forms point at the same finding: the Lean authority gate
(`Authority.lean`) refuses individual ill-formed verdicts locally and
mechanically; preventing an actor from bootstrapping the inputs to the gate
requires a discipline that lives *outside* the gate, across the execution
wrapper, derivation environment, and an implicit standing-grant invariant.
Both pieces are necessary; neither alone is sufficient. Haunted middleware,
formalized.

## What was modeled

Five `run` probes on a minimal relational encoding of the
**standing-upgrade-block** specimen
(`~/git/lean/docs/worked-examples/standing-upgrade-block.md`) crossed with
the **Authority verdict kernel** (`~/git/lean/LeanProofs/Admissibility/Authority.lean`).

The signature vocabulary:

- `Actor`, `Claim` (with `author: one Actor`)
- `State` with three verdict-component relations: `hasStanding: set Actor`,
  `hasAdmissibleBasis: set Claim`, `hasResolvedPrecedence: set Claim`
- `Op` with `by: one Actor`, `using: one Claim`, `pre: one State`,
  `post: one State`

The kernel rule (`kernelAuthorized`) was encoded as: `by ∈ pre.hasStanding ∧
using ∈ pre.hasAdmissibleBasis ∧ using ∈ pre.hasResolvedPrecedence`, all
checked at the pre-state. This mirrors `Authority.authorityVerdict` +
`Execution.AuthorizedStep`'s pre-state semantics.

ChatGPT-sharpened test (target): can an actor acquire the standing needed
to authorize an operation by means of the same operation whose authorization
depends on that standing?

## Raw results

| Probe                                         | Result      | Time  |
|-----------------------------------------------|-------------|-------|
| probe1_direct (single-op retroactive)         | UNSAT       | ~ms   |
| probe2_allowed_shape (prior-standing chain)   | SAT (1/1)   | 21 ms |
| probe3_chain_bootstrap_unconstrained (2-op)   | UNSAT       | ~ms   |
| probe4_chain_bootstrap_with_independence      | UNSAT       | ~ms   |
| probe5_independence_allows_legitimate_grant   | SAT (1/1)   | 30 ms |

## Honest classification

The four-outcome scheme from the plan:

1. **No instance** — Lean/prose kernel survives a relational sanity check.
   **Partial yes.** Probe1 UNSAT and Probe2 SAT together exhibit the shape
   ChatGPT predicted: "the relation snaps into place." But see the
   tautology caveat below.
2. **Counterexample matches known failure** — n/a, no counterexample found.
3. **Counterexample is new** — **no.** Alloy did not find a configuration-
   shaped hole the existing Lean kernel doesn't already block.
4. **Spec becomes awkward to encode** — *most underrated outcome per the
   plan, pre-committed to reporting honestly even if no goblin appears.*
   **Yes, partially.** See encoding-friction notes below.

The honest verdict: **mostly (4) with a partial (1) at the algebraic-gate
altitude.** Alloy ruled out the direct retroactive shape, but the ruling
out is encoding-tautological. The encoding friction is where the real
information lives.

## The tautology caveat (load-bearing)

Probe1 UNSAT is not a deep proof; it is a direct logical contradiction at
the encoding level. The two conjuncts of probe1 are:

```
kernelAuthorized[o]      ≡   o.by ∈ o.pre.hasStanding ∧ ...
selfStandingUpgrade[o]   ≡   o.by ∉ o.pre.hasStanding ∧ o.by ∈ o.post.hasStanding
```

The first conjunct contains `o.by ∈ o.pre.hasStanding`; the second
contains its negation. The SAT solver is concluding `x ∧ ¬x` is
unsatisfiable. This is *correct* but adds no information beyond what the
Lean proof already establishes by `authorityVerdict`'s definition.

Probe3 and Probe4 (multi-op chains by a single self-cert actor) are
UNSAT for the same trivial reason: their chains require the first op's
actor to lack standing at the chain-initial state, but `kernelAuthorized`
on that op demands the opposite. The chains can't start.

This means:

- The kernel rule, when expressed relationally, mechanically rules out the
  bad shape. ✓ (encoding preserves algebraic-gate behavior)
- Alloy did not provide independent evidence beyond what the Lean theorem
  states. The "snap" is at the encoding level, not at a deeper structural
  level.

The only non-tautological positive results are Probe2 (allowed shape is
constructible) and Probe5 (legitimate inter-actor grant is constructible
even with the `independentStandingGrant` fact).

## Encoding friction (the actual finding)

Four pieces of friction surfaced, all worth recording:

### A. The kernel's algebra has no state-transition structure

`Authority.lean` is purely algebraic — three input verdicts, one output
verdict, no notion of "pre" or "post" states. To express ChatGPT's
retroactive-standing-upgrade question, I had to add `pre` and `post`
state fields to the `Op` signature. **That structure is not in the
kernel layer.** It lives in `Execution.lean` and the `AuthorizedStep`
wrapper.

This is not a defect; it is a clarification of where the load-bearing
state-transition semantics actually live. The Alloy probe surfaced it
because expressing a temporal question forced explicit modeling of the
temporal substrate.

### B. Standing is an unconstrained state-indexed predicate at the kernel level

> **Update 2026-06-03:** This finding triggered a Lean-side change. The
> standing-grant invariant is no longer implicit — `StandingDerivation`
> in `LeanProofs/Admissibility/Derivation.lean` now carries
> `standingRevoked` + `revoked_standing_never_standing` as required
> structural fields, with chained theorem `revoked_standing_never_authorized`.
> See `working/source-basis-discipline-synthesis.md` § "Closure of
> blocker 3" for the full edit list and the lake-build receipt.
> The description below is preserved as the *original* finding; the gap
> it identifies has been closed.

`Authority.lean` does not say "standing can only be granted through a
prior authorized operation by some other actor." It says "if the input
`StandingVerdict` is `standing`, that input contributes to the conjunction
that produces `authorized`." Whether the actor *should* have standing in
state S is determined by upstream derivation logic that is not in the
kernel module.

In Alloy, this meant `hasStanding` was free to be anything Alloy needed it
to be in order to satisfy other constraints. To block compositional
bootstrapping, I had to write `fact independentStandingGrant` — a
constraint that the worked example's prose narrative carries but
`Authority.lean` does not formalize.

**This is a real architectural finding.** The kernel verdict-gate alone
is not load-bearing for bootstrap-blocking. The bootstrap-blocking comes
from the conjunction of:

1. The kernel rule (`Authority.lean`'s from-state check)
2. The execution wrapper (`Execution.lean`'s `AuthorizedStep` structure)
3. The derivation environment's discipline on basis admissibility (e.g.,
   `BasisDerivation.revoked_never_admissible` in `Derivation.lean`)
4. An implicit invariant that standing is not freely settable — which
   lives in *how* `StandingVerdict` gets produced upstream, not in any
   single named theorem I have seen.

The fourth item is the one Alloy made visible. The worked example assumes
it; the kernel module does not encode it.

### C. The two-axis caveat from source-basis-discipline was not touched

The source-basis-discipline synthesis note carries an open caveat: the
three specimens split into a temporal/source pair (AmendmentFragment +
RetroactiveLegitimation) and a multiplicity/resource case
(ContractionHinge). This spike covered only the temporal/source axis
(standing-upgrade is a temporal/source-style retroactive shape).
ContractionHinge's resource-accounting question was not modeled at all.

**Therefore this spike does not resolve the synthesis question.** It
provides evidence on one axis only. The pickup point in
`source-basis-discipline-synthesis.md` remains open. If a second spike
is justified, it should target the multiplicity/resource axis on
ContractionHinge to see whether *that* axis also snaps into place
relationally or whether it requires a structurally distinct encoding.

### D. The probes I wrote were less informative than they looked

Probe1, Probe3, and Probe4 all carry the same tautology. The version that
would non-tautologically test compositional bootstrap requires modeling
inter-actor standing transfer chains where the kernel rule and a real
upstream-grant constraint both apply. Probe5 sketched that shape and was
satisfiable, which is the right behavior — legitimate chains exist — but
the *blocking* version (chain that bootstraps despite the independence
fact) would require a more careful encoding than I wrote here. A future
spike could target that.

## Adoption verdict (the keeper rule)

The plan's keeper rule:

> **Alloy earns adoption only by finding or ruling out a configuration-
> shaped hole in an existing kernel specimen.**

Did it find a hole? **No.**

Did it rule out a hole? **Partially.** The relational encoding confirms
the kernel's algebraic-gate structure rules out the direct retroactive
shape. But the ruling-out is at the encoding level (tautological in the
sense above), not at a deeper proof level the Lean theorem doesn't
already establish.

The encoding friction did produce useful clarification — Finding B above
(standing-acquisition constraint lives upstream of the kernel, not in
it) is genuinely new framing, even if not a new hole. Worth carrying
into paper-writing and synthesis: when the prose says "the kernel blocks
standing bootstrap," the load-bearing piece is the *conjunction* of the
kernel rule with the upstream derivation discipline, not the kernel rule
alone.

**Recommendation:** Alloy does not earn ongoing adoption on the strength
of this single probe. It earned a small, real clarification of where the
load-bearing constraint lives, which justifies the cost of this single
spike. It did not earn a calculus-companion role.

A second spike on the **multiplicity/resource axis (ContractionHinge)**
would be a reasonable next probe IF the source-basis-discipline pickup
point becomes a live question again. Otherwise: Alloy goes on the
checked-off branch.

## What this is NOT

- Not a verification of the Lean kernel. The kernel's correctness comes
  from the Lean proofs, not from this spike.
- Not a falsification of the kernel. Alloy did not find a hole.
- Not authorization to build "AlloyAdmissibilityCalculus." Columbus stays
  home, per the plan's disposable-naming discipline.
- Not a resolution of the source-basis-discipline synthesis question.
  This spike covered one axis only.
- Not new doctrine. Findings A and B are *clarifications of existing
  architecture*, not new primitives.

## What this IS

- A bounded probe ran, classified, and written up.
- A real (small) clarification: the standing-bootstrap-blocking is a
  conjunction across four layers (kernel rule + execution wrapper +
  derivation discipline + implicit standing-grant invariant), not a
  single-layer property of `Authority.lean`.
- Two exportable phrasings of the finding (see top of this note):
  *Authority refusal is local; bootstrap prevention is architectural.*
  *The gate can refuse only what the surrounding transition system makes
  visible.*
- A directional verdict on Alloy adoption: not yet, single-probe-only
  cost paid, second probe optional and gated on the multiplicity/resource
  axis becoming live.
- An honest negative-result spike. The cathedral does not get built.

## Recommended next move

Narrowed codex pass on this result + the source-basis-discipline synthesis
note. **Not** "review my theory." The specific question to put to codex:

> Does the four-layer-conjunction finding (Authority gate + execution
> wrapper + derivation discipline + standing-grant invariant) constitute
> evidence that "source-basis discipline" names a real common calculus
> layer, or does it instead expose that the temporal/source specimens and
> the multiplicity/resource specimen (ContractionHinge) are being bundled
> as one layer when they are structurally distinct refusal families?

Codex now has concrete substrate to push against (the Alloy run + this
result note + the synthesis note), not just prose. Per the synthesis
note's common-mode warning, this is exactly the non-Claude adversarial
pass it was filed pending.

## Cross-references

- Plan: [`alloy-spike-standing-upgrade-plan.md`](alloy-spike-standing-upgrade-plan.md)
- Spec: [`standing_upgrade_probe.als`](standing_upgrade_probe.als)
- Alloy output: `standing_upgrade_probe/` (receipt.json + solution files)
- Specimen: `~/git/lean/docs/worked-examples/standing-upgrade-block.md`
- Kernel substrate: `~/git/lean/LeanProofs/Admissibility/Authority.lean`,
  `~/git/lean/LeanProofs/Admissibility/Derivation.lean`,
  `~/git/lean/LeanProofs/Admissibility/Execution.lean`
- Open synthesis question (not resolved by this spike):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Sibling working notes: [`authorization-laundering-arc.md`](authorization-laundering-arc.md),
  [`boundary-by-asymmetry-pattern.md`](boundary-by-asymmetry-pattern.md)
