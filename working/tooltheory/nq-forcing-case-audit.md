# NQ formal-correspondence audit for `RefusalPropagation.Composition.refusal_composes`

**Status:** Filed 2026-05-26 as a consumer-forcing audit after the Phase C rebar pass identified `refusal_composes` as a statable abstract theorem and NQ as a candidate correspondence target. **Policy correction, 2026-07-14:** the original requirement that a downstream consumer "earn" further formal work is superseded. Formalization leads code; consumer demand affects priority and runtime rollout, not permission to state or prove the theorem.

**Posture:** The 2026-05-26 audit wrote no Lean instantiation, made no `CalculusOne.lean` change, and did not promote anything to 2.0. Those are dated facts, not a continuing prohibition. A checked Scratch instantiation was subsequently added under `Admissibility.RefusalPropagation.Annex.NQDependency`; it remains experimental and outside `CalculusOne.lean`. Public 2.0 promotion remains a separate custody and release decision.

**Current verdict:** NQ supplies a concrete correspondence target, and the relation the theorem abstracts already appears on the wire. The Lean-side `NQDependency` model now gives the cascade a direct proof and a re-derivation through generic `refusal_composes_two_hop`. This proves the model's conditional contract, not NQ runtime soundness. A conformance claim still requires an explicit abstract-to-runtime mapping plus runtime evidence or a refinement proof.

---

## Keeper

> **Formalization does not wait for a consumer or shipping blocker. Runtime code does not earn a conformance claim merely by resembling the theorem.**

## The scenario, mapped onto NQ vocabulary

NQ already enforces, at runtime, the pattern the abstract theorem describes. Per `~/git/nq/docs/WITNESS_PACKET.md` §60:

> *A witness whose standing depends on another witness (e.g. a SMART witness that depends on the device being enumerable; a ZFS witness that depends on the pool being importable) must declare that dependency. Existing NQ machinery already enforces suppression-by-ancestor under `TESTIMONY_DEPENDENCY` and `COVERAGE_HONESTY` semantics.*

Concrete instantiation (single-witness ancestor-dependency case):

| Abstract (`RefusalPropagation.Composition`) | Concrete (NQ) |
|---|---|
| `A : Claim` | upstream witness, e.g. `device_enumeration_witness` |
| `B : Claim` | downstream witness depending on A, e.g. `smart_witness` (depends on device-enumeration) |
| `C : Claim` | a registered claim, e.g. `disk_state` |
| `witnesses A B` | A's standing supports B's — encoded via declared witness dependency / `ancestor_finding_key` |
| `requiredFor B C` | B is admissible evidence for C — encoded via the witness→claim mapping in `nq-core::preflight` |
| binding use | preflight authorizing C; the relevant verdict is the `cannot_testify` reserved value |

The composition shape, in NQ idiom:

> If `device_enumeration_witness.admissibility.state = cannot_testify` (A cannot witness B), and the SMART witness's standing depends on device enumeration (`witnesses A B` via declared dependency), and `disk_state` preflight requires the SMART witness as basis (`requiredFor B C`), then `disk_state` preflight must return `cannot_testify` for binding use (¬ witnesses A C).

This is exactly the canonical `refusal_composes` shape, instantiated over NQ's existing single-witness ancestor-dependency vocabulary.

## What NQ already has on the wire

- `warning_state.admissibility.state ∈ {observable, suppressed_by_ancestor, suppressed_by_declaration, cannot_testify, stale}` — TESTIMONY_DEPENDENCY V1.0+V1.1+V1.2 shipped.
- `ancestor_finding_key` — encodes the basis chain for `suppressed_by_ancestor` cases.
- `basis_state ∈ {live, stale, retired, invalidated, unknown}` — evidence lifecycle; feeds Layer-0 Authority.
- Per-claim-kind `cannot_testify` lists (`disk_state_cannot_testify`, `ingest_state_cannot_testify`, `dns_state_cannot_testify`) — each registered claim names its non-mintable consequences explicitly.
- Suppression-by-ancestor cascade at runtime: when ancestor → `cannot_testify`, dependent → `suppressed_by_ancestor`.

The relation `requiredFor` is operationally present in NQ as the witness-dependency-declaration plus the witness→claim mapping. The relation `witnesses` is operationally present as the admissibility-state cascade. The structural property `BasisInheriting` is operationally enforced by the suppression-by-ancestor cascade.

**The runtime pattern is present on the NQ side.** Calling it an implementation of the formal contract still requires an explicit mapping and runtime evidence; this memo identifies the target but does not itself discharge conformance.

## What exists, and what remains

`Admissibility.RefusalPropagation.Annex.NQDependency` now contains the bounded Lean bridge this audit proposed:

1. `Finding` and `DependsOn` give the three-finding, two-edge abstract graph.
2. `CascadeSound DependsOn state` states the runtime obligation at the model boundary.
3. `disk_state_refused_when_device_enumeration_refused` proves the direct two-hop cascade.
4. `disk_state_cannot_bind_when_device_enumeration_refused` composes the cascade with `refused_blocks_binding`.
5. `disk_state_cannot_bind_via_refusal_composes` re-derives the result through the generic `refusal_composes_two_hop` law and `cascade_implies_basis_inheriting`.

What remains is not permission to formalize and not another abstract theorem merely for symmetry. It is the correspondence work: show that the concrete NQ dependency declarations, publish behavior, and binding-use checks instantiate `DependsOn`, `CascadeSound`, and `BindingAdmissible`. That requires an explicit mapping plus runtime evidence or a refinement proof. Public promotion of the Scratch result is separately governed by proof, scope, overlap, custody, compatibility, and release review.

## Formal target and runtime correspondence

NQ can name the statement: *"NQ's ancestor-suppression cascade is sound — if A is `cannot_testify` and B's standing depends on A, then B's `cannot_testify` (`suppressed_by_ancestor`) propagates correctly to every C that requires B."*

The checked Lean model proves the conditional cascade contract. It does not prove that NQ's implementation satisfies the model's premises. Runtime behavior can ship independently, but neither shipping nor structural resemblance discharges correspondence.

- ✅ The NQ-shaped Lean model states and proves the conditional contract.
- ✅ The concrete model is connected to the generic `refusal_composes_two_hop` law.
- ⚠️ The abstract-to-runtime mapping and conformance evidence remain to be established.

Under the audit's historical A/B vocabulary this was classified **B (plausible consumer, missing instantiation)** rather than **A (active forcing case)**. That label describes the 2026-05-26 priority assessment, not the current artifact status and not admission to formal work. The relation exists on the wire and the conditional formal bridge now exists in checked Scratch; runtime correspondence remains open.

The NQ headline is the boundary discipline: *"the Lean kernel does not tell NQ to become more powerful. It tells NQ to become more exact about what its testimony can and cannot support."* The bridge work makes NQ's testimony shape more exact and may therefore lead subsequent implementation or audit changes; it need not unlock a new capability to be legitimate formal work.

## Effect on the historical Phase D gate

Phase D criterion 3 ("second forcing case exists") moves from:

> ❌ None

to:

> ⚠️ Potential consumer identified: NQ ancestor-suppression / TESTIMONY_DEPENDENCY cascade. At filing time, the absence of a shipping blocker left the bridge queued under the then-current forcing-case policy.

That paragraph records the 2026-05-26 disposition. The 2026-07-14 correction retires criterion 3 as a formalization gate: "no consumer" and "consumer named" are priority/correspondence facts, not permission states. The other Phase D criteria — composition scope, abstraction count, slogan blast radius, and PL/UC remaining working notes — may still govern 2.0 promotion and custody, but they do not prohibit theorem development.

## Runtime validation scenarios

The following scenarios would raise priority, pressure-test the model, or supply runtime correspondence evidence. They are not prerequisites for the Lean bridge:

1. **WITNESS_COMPOSITION cashes out.** NQ ships its first multi-witness composition rule (per `ARCHITECTURE_NOTES.md` latent tripwire). The roadmap memo names four queued observations: first multi-witness Prom-backed finding, second exporter profile composing with an existing witness, DURABLE_ARTIFACT_SUBSTRATE V1 real-producer overlap, or ZFS+SMART disagreement on disk-level state with no composition rule. Any of these would provide a concrete test of whether the composition rule preserved standing.
2. **`composition_rule` and `contributing_witnesses` wire fields land.** A downstream consumer (Governor, Wicket, another agent) needs to formally reason about whether the rule's standing exceeds or weakens individual witness standings. Per the negative-standing case named in the roadmap memo: *"the rule's standing is weaker than any individual witness's standing — finding cannot support claim X even though witness A could in isolation."*
3. **A registered-claim audit produces a soundness question NQ cannot answer at the runtime layer.** Example: an auditor asks whether `disk_state`'s preflight correctly refuses when device-enumeration is `cannot_testify`. NQ can demonstrate the runtime behavior but not prove it sound across all dependency chains.

The memo remains useful before any scenario occurs: it already names a coherent formal target.

## Recommendation

**Keep 2.0 promotion separate. Retain the bounded NQ instantiation as checked Scratch, and evaluate any next strengthening on theorem-shape and proof merits.**

The Phase C.3 probe is complete at its declared three-finding, single-snapshot scope. Its existence does not automatically promote a 2.0 public surface; promotion retains the other custody criteria, including composition scope, slogan blast radius, and PL/UC discipline. Conversely, existing runtime behavior should not be called conformant solely because the probe is proved. The next distinct task is a correspondence audit or refinement argument, not retroactive authorization of the formal work.

The discipline:

> **State and prove the contract when its formal shape is ready. Let it lead code. Establish runtime conformance with a mapping and evidence, not with consumer demand.**

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — the abstract `refusal_composes_two_hop` rebar and the checked `Annex.NQDependency` instantiation.
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Phase C/D gate this audit updates.
- `~/git/nq/docs/ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md` — NQ's roadmap memo. Headline: *the Lean kernel tells NQ to become more exact, not more powerful.* WITNESS_COMPOSITION names the multi-witness runtime validation scenarios historically called forcing-case triggers.
- `~/git/nq/docs/WITNESS_PACKET.md` §60 — declared-dependency discipline (single-witness ancestor case).
- `~/git/nq/docs/CLAIM_PREFLIGHT.md` §73 — `cannot_testify` as constitutional output, not error.
- `~/git/nq/docs/VERDICTS.md`, `~/git/nq/docs/CLAIM_CATALOG.md` — registered claim kinds and verdict vocabulary.
- [[refusal-kernel-to-refusal-receipt-seam]] — runtime-vs-formal-layer split; the bridge work falls on this seam (Lean blocks inference; NQ blocks operational basis-use).

## Provenance

- **2026-05-26** — audit triggered by ChatGPT's correction that the Phase C rebar report's Phase D table read "❌ None" in criterion 3, when NQ's roadmap memo (`ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md`) names NQ as a likely consumer.
- Audit performed by claude-code against the NQ roadmap memo + `WITNESS_PACKET.md` + `CLAIM_PREFLIGHT.md`.
- Honest 2026-05-26 finding: NQ had the relation operationally; the bridge work was Lean-side and was then recorded as not authorized because neither side had a shipping blocker. Memo classification: **B**. The 2026-07-14 correction preserves that finding as provenance while superseding the consumer-gated authorization rule.

> **The relation is on the wire. The conditional contract is proved in Scratch. Runtime conformance remains a separate evidentiary claim.**
