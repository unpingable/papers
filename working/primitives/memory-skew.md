# Memory Skew

**Status:** candidate
**Kind:** Axis
**Originated:** 2026-05-20 (paper-Claude / ChatGPT cross-model session, generated from AWP kernel-overlap audit residue)
**Primary home:** no paper yet — operator-facing application of `Admissibility/AxisSkew.lean`

## Keeper

> Staleness says the map is old. Skew says which way it lies.

Adjacent line:

> A prior cannot both underclaim and overclaim the same observed state along the same comparison surface.

## What this names

The directional relationship between a *prior* claim and an *observed* claim along an ordered comparison surface. Three cases:

- **Lagging.** Prior underclaims observed state. Substrate-rich instance already named: stale-binding.
- **Matched.** Prior and observed indistinguishable under the surface's ordering.
- **Leading.** Prior overclaims observed state. *No previously-named primitive covers this generally.*

The leading direction is the load-bearing addition. Lagging has substrate-rich coverage already (stale-binding, used across P23–P27). Leading is the missing general primitive — completion hallucination, authority projected ahead of evidence, capability claimed before verification, integration declared before connectors land.

> Lagging has stale-binding ancestry. Leading is the missing general primitive.

## Family relationship

Four entities, distinct roles:

```
stale-binding   — substrate-rich lagging primitive (caches, hat-x, briefings)
AxisSkew.lean   — abstract bidirectional comparison kernel
Freshness.lean  — time-axis instance (NotYetValid = leading; Expired = lagging)
Memory Skew     — current operator-facing application
```

**Stale-binding does not become an instance of Memory Skew.** Stale-binding has consequence-window machinery (δ vs t_c, base-rate decay, write-through receipt lineage, dual-cache divergence detection) that the abstract kernel should not absorb. The relationship is parallel: stale-binding stays the substrate-detailed lagging primitive; AxisSkew supplies the orientation kernel; Memory Skew is the operator-facing pattern that uses both.

## Formal object

Kernel module: `LeanProofs/Admissibility/AxisSkew.lean`.

Core inductive:

```lean
inductive Skew where
  | lagging   -- prior underclaims observed: lt prior observed
  | matched   -- prior and observed indistinguishable under lt
  | leading   -- prior overclaims observed: lt observed prior
```

Classification function:

```lean
def classifyBy (lt : α → α → Prop) [DecidableRel lt]
    (prior observed : α) : Skew
```

Three kernel theorems (built green 2026-05-20, no `sorry`):

1. **`not_lagging_and_leading_same_axis`** — classification is functional: cannot be both directions on the same surface.
2. **`classify_self`** (with irreflexivity hypothesis) — comparing a value to itself yields `matched`.
3. **`reverse_lagging_is_leading`** (with asymmetry hypothesis) — swapping (prior, observed) swaps lagging ↔ leading; classification is orientation, not verdict.

The relation `lt` is consumer-supplied. The kernel keeps the comparison opaque so partial, preorder, lattice, and total orderings can each be its argument.

## Failure predicate

The general predicate: *binding to a prior whose classification against current observation is not `matched`, without a discriminator that explains the divergence.*

The two directions decompose:

- **Lagging-direction failure** — stale-binding's predicate. Prior bound to a value that has already moved. Substrate detail and architectural rules at `working/primitives/stale-binding.md`.
- **Leading-direction failure** — *new* general predicate. Prior asserts capability / authority / completeness / integration / recency at a level the observed state does not support, *and* a decision binds to the prior without independent verification against the observation.

## Five candidate axes (operator-facing, not kernel-pinned)

Axes where the bidirectional split changes diagnosis. The kernel does *not* pin this taxonomy — it lives in this prose primitive. Each consumer picks the comparison relation that fits its substrate.

- **Recency.** Already covered by `Freshness.lean` (NotYetValid = leading, Expired = lagging on the temporal axis).
- **Completeness.** "I have full data" vs partial coverage. Leading: hallucinated complete-set claims. Lagging: partial set treated as complete because earlier data is missed.
- **Authority.** Claimed standing vs operational standing. Leading: standing claimed before bestowal. Lagging: standing rescinded but still acted on (composes with FiatAdmissibility).
- **Capability.** Claimed ability vs demonstrated ability. Leading: capability projected ahead of evidence — the AI-deployment failure class. Lagging: deprecated capability still relied on.
- **Integration.** Claimed composition state vs actual composition. Leading: integration declared before connectors land. Lagging: deprecated integration paths still wired.

## Do not confuse with

- **Stale-binding** — substrate-rich lagging primitive. Memory Skew is the abstract bidirectional sibling that names what stale-binding's missing twin would be. Stale-binding stays substrate-rich; Memory Skew stays substrate-general. Stale-binding owns consequence-window machinery; Memory Skew owns directional classification.
- **Freshness (kernel module)** — time-axis instance of the bidirectional split. Freshness already encodes both directions on time; Memory Skew is the generalization to non-time axes.
- **Witness invariance failure** — a witness that moves when irrelevant variables move. Different shape: that primitive is about *invariance under perturbation*; Memory Skew is about *directional comparison between prior and observed*.
- **Prose-state inversion** — prose claims X, code does not-X. Substrate instance that may sit in either skew direction (prose ahead of fixes = leading; prose behind fixes = lagging). Memory Skew is the relational kernel; PSI is one substrate (prose).
- **Pre-emptive naming** — meta-doctrine about *when* to name an architectural surface. Not a state-comparison primitive.
- **Numerical admissibility** — about score/rank/confidence × imply_magnitude/value/truth admissibility. Different axis: that classifies what a numerical artifact can claim; Memory Skew classifies the direction of mismatch between prior and observed claims on any axis.

## Operational theorems (deferred, not authorized)

Candidate bridge theorem, *not yet formalized and not yet authorized*:

> Lagging may support correction of a claim, but it does not itself authorize mutation.

This would compose AxisSkew with `Corrective` / `Authority` / `CorrectiveBoundary`. The composition is natural — `Corrective` already proves corrective transitions are authority-non-increasing — but writing the bridge before a live consumer needs it would be cosplay architecture. Held.

A symmetric candidate for the leading direction:

> Leading may support refusal of a binding, but it does not itself authorize forward mutation.

Same deferral. Same reason.

## Used by

Current consumers (named-not-built):

- `Freshness.lean` — pre-existing time-axis instance (does not import AxisSkew; conceptual sibling)
- `stale-binding.md` — pre-existing lagging-direction substrate primitive (parallel, not subsumed)

The candidate becomes *working* (per primitives README promotion criteria) when a second non-time substrate instance forces the directional split independently — most likely the AI-capability-overclaim case or the AWP vocabulary-convergence case (lexical leading).

## Open questions

- **Leading-direction substrate instances.** Stale-binding is the worked lagging primitive across five papers. Are there equally well-worked leading-direction instances already in the corpus that the field notebook hasn't recognized as one family? Candidate scans: AWP §3.F vocabulary convergence (lexical leading); AGI capability-overclaim cases (capability leading); preemptive-naming surfaces (architectural leading, but meta-doctrine kind).
- **Composition with stale-binding.** When a single binding exhibits both lagging *and* leading skew across two different axes (cache lagging on truth, prior leading on capability), does Memory Skew say anything composite, or is the right answer "two findings, two axes"?
- **Operational theorem timing.** What forcing case would justify writing the *"lagging may support correction, not mutation"* bridge theorem? Probably a live consumer in `~/git/standing` or governor-side code that needs to distinguish corrective-from-stale vs forward-from-fresh.
- **Per-axis decidability.** The kernel requires `DecidableRel lt`. Some operator-facing axes (capability, completeness) may not have decidable orderings on a given substrate. Whether that forces a fallback `Skew.unknown` constructor or is properly a consumer-side problem is open.

## Cross-references

- `LeanProofs/Admissibility/AxisSkew.lean` — kernel module (3 theorems, lake build green 2026-05-20)
- `LeanProofs/Admissibility/Freshness.lean` — time-axis instance
- `working/primitives/stale-binding.md` — substrate-rich lagging sibling
- `working/primitives/witness-invariance-failure.md` — adjacent (perturbation, not comparison)
- `working/primitives/prose-state-inversion.md` — substrate instance candidate
- `working/adversarial-witness-protocol.md` §3.F — vocabulary convergence as candidate leading-direction instance

## Provenance

Generated 2026-05-20 from a cross-model session that started by asking whether the AWP audit's null result left any Lean residue elsewhere. The directional-skew shape emerged when comparing stale-binding (substrate-rich, lagging only) to Freshness (kernel, both directions, time only) and noticing the missing diagonal: substrate-general leading direction. The keeper line *"Staleness says the map is old. Skew says which way it lies."* came from ChatGPT-side compression; the *"Lagging has stale-binding ancestry. Leading is the missing general primitive."* framing came from operator-side filing discipline.

Strict scope discipline applied throughout: no `ClaimAxis` enum in kernel, no `Corrective` import, no operational authorization theorem, no calculus naming. Three theorems, opaque comparison, parallel relationship to stale-binding preserved.
