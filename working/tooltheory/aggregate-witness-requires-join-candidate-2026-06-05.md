# Aggregate-Witness-Requires-Join — candidate kernel

**Filed:** 2026-06-05. **Status:** named, unbuilt, awaiting consumer. Workflow-layer sibling to [`log-only-proves-emission-candidate-2026-06-05.md`](log-only-proves-emission-candidate-2026-06-05.md). Layer tag: **`NoSilentJoin`** (per anti-laundering doctrine map's layer map).

## Claim

> **A bundle of partial witnesses is not admissible as a unified witness unless accompanied by a join witness that is indexed to that exact bundle and requirement set, and that proves both coverage (every required property is satisfied somewhere in the bundle) and preservation (the unified witness carries every required property forward).**

Short form:

> **The bundle is not the join.**

## Sibling positioning

| Layer tag | Candidate kernel | Atomic shape |
|---|---|---|
| `NoLift` (atomic) | [[log-only-proves-emission-candidate-2026-06-05]] | log ≠ truth |
| `NoSilentJoin` (workflow) | this candidate | bundle ≠ unified witness |

Atomic epistemology refuses single illicit promotions. Workflow epistemology refuses distributed-satisfaction-passed-as-unified. Same meta-discipline (*indexed or it didn't happen*), different layer.

## Why this is a workflow-layer kernel (not atomic)

Atomic `NoLift` kernels refuse single promotions (`Receipt ↛ Authority`, `Log ↛ Truth`) — the corpus has these scattered across the `Admissibility/` family. The `NoSilentJoin` workflow kernel refuses a different shape: distributed satisfaction across multiple partial witnesses being treated as unified admissibility without a join. The hops can all be locally valid; the partial witnesses can each satisfy their slice; the join is the missing mediating object. The lie is not in any one sentence — it's in the unspoken assumption that someone else verified the composition.

## Why candidate, not built

The 2026-06-05 workflow-layer extension audit found the existing corpus formalizes composition at the *calculus / federation* altitude (`no-unifier-without-laundering` doctrine; `Composition.lean`; the control-flow-laundering meta-pattern in the anti-laundering doctrine map) but does *not* formalize the specific organizational-process shape: a *bundle* of partial witnesses, each from a different source, each satisfying one slice of the requirement set, being passed off as a single admissible witness for the composite claim. This is the compliance-audit / promotion-packet / AI-eval-safety-bundle / incident-response-postmortem pattern. The kernel that formalizes it is missing.

## Family classification

Per [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md): would sharpen the **composition / unification** row from "local refusal composes ⇒ unified judgment form" (current atomic-altitude doctrine) to "distributed partial witnesses ⇒ unified admissible witness" (workflow-altitude formal instance). Sits one altitude above the family rows; under the master frame's `NoSilentJoin` layer tag.

## Forcing case (absent)

No downstream consumer currently needs this. Build trigger would be one of:

- A compliance-audit context asking the corpus to formalize what makes a multi-source evidence bundle inadmissible.
- An AI-eval safety-bundle context where partial witnesses (benchmark scores, calibration metrics, rater agreement, red-team results) are passed off as a unified safety claim.
- A receipt-substrate consumer (NQ, Wicket, AG) needing typed-refusal at the bundle layer.
- An incident-response / SRE consumer needing "dashboards-green + logs-normal + alerts-quiet + on-call-staffed ≠ system-healthy" formalized.
- An external pitch needing one concrete artifact at the workflow / organizational-process layer.

Until one of these fires, the kernel stays named-not-built per name-early discipline.

## Sketch shape (NOT a build spec — name-early only)

`WitnessBundle` carries a list of `PartialWitness` (each with a per-source satisfaction predicate over `Requirement`). `JoinWitness b reqs` is **indexed** to the exact bundle and requirement set, carrying *two* fields:

- `covers : ∀ r, reqs r → bundleSatisfies b r` — every required property is satisfied somewhere in the bundle (no phantom requirements).
- `preserves : ∀ r, reqs r → unified.satisfiesAll r` — the unified witness carries every required property forward (no preserved-but-never-required claims).

Both fields together close the gap that either alone leaves open. Core API-boundary refusal: `admissibleAsUnified b reqs (join : JoinWitness b reqs)` — the missing join is **not a bad value**, it is **an uninhabited argument position**. The corresponding negative theorem is one line; the indexed type structure is the argument.

The sketch above is candidate shape only. The actual build, if it happens, will be designed against existing kernel conventions and reviewed for overlap with `Composition.lean` and the `CrossBoundary*` family.

## The two-field discipline

`covers` alone is insufficient (someone could "preserve" requirements the bundle never actually satisfied, because implication is cheap and reality is expensive). `preserves` alone is insufficient (someone could "satisfy" requirements that were never required, then claim preservation of those instead of the actual reqs). Both fields together close the gap. The pattern generalizes: any mediating object that translates from a bundle to a unified claim needs BOTH a coverage proof (bundle satisfies what reqs ask) AND a preservation proof (unified witness carries those satisfactions forward).

## Non-claims

- **Not a build spec.** The sketch is candidate shape; the actual module would be designed against existing kernel conventions.
- **Not authorization to build.** Name-early per [[feedback-name-early]]; build only on forcing case.
- **Not a position** on whether this should ever join the Lean tree.
- **Not part of any `NoSilentJoin/` parallel directory.** The 2026-06-04 audit refused a parallel `NoLift/` module surface; the same refusal extends to `NoSilentJoin/` and `NoChainMagic/`. These are *layer tags* in the doctrine map, NOT a module/directory hierarchy. If this candidate is ever built, it joins `LeanProofs/Admissibility/` under its existing namespace, not under a new roof.
- **Not a replacement for atomic-layer kernels.** Atomic `NoLift` kernels are a finite-ish enumeration of single illicit promotions; this workflow `NoSilentJoin` kernel sits one altitude above and applies to *bundles* of valid atomic witnesses.

## Cross-references

- [`log-only-proves-emission-candidate-2026-06-05.md`](log-only-proves-emission-candidate-2026-06-05.md) — atomic-layer sibling (`NoLift`); same name-early discipline.
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The master frame + § The layer map (workflow row).
- [[documentation-keepers]] — keeper phrases: *"Indexed or it didn't happen"* (meta-discipline); *"Existential laundry"* (genus name for unindexed-witness laundering); *"The bundle is not the join"* (this candidate's short-form doctrine); *"The theorem is less important than the type you cannot construct"* (type-level lesson).
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — composition / federation doctrine at calculus altitude; this candidate is the workflow-layer formal instance under that doctrine.
- `~/git/lean/LeanProofs/Admissibility/Composition.lean` — existing composition-layer module; review for overlap before any build.

## Provenance

Surfaced in multi-model exchange 2026-06-05 (ChatGPT extending the workflow-layer-not-more-Pokémon idea → DeepSeek sketching workflow kernels with code → ChatGPT correcting the unindexed-join trap → DeepSeek refining with the two-field discipline → ChatGPT promoting the meta-rule to *"indexed or it didn't happen"* and naming *"existential laundry"* → Claude Code kernel-overlap audit confirming workflow-layer kernel as genuine gap, sibling to `LogOnlyProvesEmission`). Side-quest yield per the 2026-06-05 workflow-layer closing ledger: *named, unbuilt, high-value workflow-layer gap.*
