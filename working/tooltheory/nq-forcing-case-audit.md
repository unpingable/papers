# NQ forcing-case audit for `RefusalPropagation.Composition.refusal_composes`

**Status:** Consumer-forcing audit. Filed 2026-05-26 after Phase C rebar pass identified `refusal_composes` as a statable abstract theorem requiring a downstream consumer to earn Phase D consideration. NQ is the candidate consumer per its `~/git/nq/docs/ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md` memo.

**Posture:** Memo only. No Lean instantiation written. No `CalculusOne.lean` change. No promotion to 2.0.

**Verdict (classification B):** Plausible consumer; the relation NQ would expose already exists on the wire; the missing piece is the Lean-side instantiation that bridges `refusal_composes` to NQ's existing vocabulary. NQ does not currently *need* the formal proof to ship; the bridge would land as a soundness witness for existing runtime behavior, not as an unlock for new NQ capability.

---

## Keeper

> **A potential consumer is not a forcing case until it can name the statement it cannot currently prove.** NQ can name it; NQ has no concrete blocker requiring it.

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

**Nothing is missing on the NQ side.** NQ already implements the runtime equivalent.

## What is missing

What's missing is the *Lean-side instantiation* that proves NQ's runtime behavior is sound:

1. A small abstract model of NQ's witness/claim graph in Lean (NOT a full claim ontology — minimal `Claim` type + `dependsOn` relation).
2. An instantiation of `requiredFor` over NQ's witness-dependency-declaration relation.
3. A proof of `BasisInheriting` from the suppression-by-ancestor cascade rules.
4. Application of `refusal_composes` to derive: ancestor `cannot_testify` propagates to dependent `cannot_testify` for binding use.

Steps 1–4 are the bridge work. They are **NOT currently authorized**. They are in scope for a future Phase C.3 probe if any of the trigger conditions below fire.

## Forcing-case test

NQ can name the statement: *"NQ's ancestor-suppression cascade is sound — if A is `cannot_testify` and B's standing depends on A, then B's `cannot_testify` (`suppressed_by_ancestor`) propagates correctly to every C that requires B."*

NQ cannot currently *formally* prove this (no proof assistant on the NQ side). NQ also does not currently *need* to prove it — the runtime behavior ships without the formal proof.

- ✅ NQ can name an unprovable statement.
- ✅ Lean's `refusal_composes`, if instantiated, would prove it.
- ❌ NQ has no concrete blocker requiring the proof for shipping.

This is **B (plausible consumer, missing instantiation)**, not **A (active forcing case)**. The relation exists; the formal bridge does not; the urgency is precision-pressure, not capability-pressure.

The NQ headline is the boundary discipline: *"the Lean kernel does not tell NQ to become more powerful. It tells NQ to become more exact about what its testimony can and cannot support."* The bridge work would make NQ's existing testimony shape *more exact*, not give it new capability — which fits the NQ posture but does not constitute an unblocking forcing case.

## What this updates in the Phase D gate

Phase D criterion 3 ("second forcing case exists") moves from:

> ❌ None

to:

> ⚠️ Potential consumer identified: NQ ancestor-suppression / TESTIMONY_DEPENDENCY cascade. Forcing case **not yet proven** — NQ has no current shipping blocker that requires the formal proof. Bridge work (Lean-side instantiation of `requiredFor` over NQ's `ancestor_finding_key`) is queued, not authorized.

This does NOT open Phase D. It updates the gate's third criterion from "no consumer" to "consumer named, forcing case pending." All other Phase D criteria (composition between kernels, abstraction count, slogan-blast-radius, PL/UC stays as working notes) remain unchanged.

## What would convert B → A

A concrete forcing case fires when at least one of these is true:

1. **WITNESS_COMPOSITION cashes out.** NQ ships its first multi-witness composition rule (per `ARCHITECTURE_NOTES.md` latent tripwire). The roadmap memo names four queued sub-triggers: first multi-witness Prom-backed finding, second exporter profile composing with an existing witness, DURABLE_ARTIFACT_SUBSTRATE V1 real-producer overlap, or ZFS+SMART disagreement on disk-level state with no composition rule. Any of these would force NQ to formally reason about whether the composition rule preserved standing.
2. **`composition_rule` and `contributing_witnesses` wire fields land.** A downstream consumer (Governor, Wicket, another agent) needs to formally reason about whether the rule's standing exceeds or weakens individual witness standings. Per the negative-standing case named in the roadmap memo: *"the rule's standing is weaker than any individual witness's standing — finding cannot support claim X even though witness A could in isolation."*
3. **A registered-claim audit produces a soundness question NQ cannot answer at the runtime layer.** Example: an auditor asks whether `disk_state`'s preflight correctly refuses when device-enumeration is `cannot_testify`. NQ can demonstrate the runtime behavior but not prove it sound across all dependency chains.

Until one of those fires: memo stays the memo.

## Recommendation

**Defer 2.0. Continue 1.x annex. Do NOT instantiate `refusal_composes` over NQ vocabulary yet.**

The instantiation is a clean future Phase C.3 probe but does not earn its keep without a concrete NQ blocker. Once a blocker fires (per the three trigger conditions above), Phase C.3 opens with the bridge work scoped tightly (≤30 lines of Lean: minimal Claim type, instantiated `requiredFor`, proved `BasisInheriting`, applied `refusal_composes`). That probe itself does not open Phase D — Phase D still requires the other criteria (composition between kernels, slogan-blast-radius, PL/UC discipline).

The discipline:

> **A potential consumer is not a forcing case until it can name the statement it cannot currently prove. NQ can name it; NQ has no concrete blocker requiring it.**

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — the abstract `refusal_composes` rebar (Phase C output).
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Phase C/D gate this audit updates.
- `~/git/nq/docs/ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md` — NQ's roadmap memo. Headline: *the Lean kernel tells NQ to become more exact, not more powerful.* WITNESS_COMPOSITION section names the multi-witness forcing-case triggers.
- `~/git/nq/docs/WITNESS_PACKET.md` §60 — declared-dependency discipline (single-witness ancestor case).
- `~/git/nq/docs/CLAIM_PREFLIGHT.md` §73 — `cannot_testify` as constitutional output, not error.
- `~/git/nq/docs/VERDICTS.md`, `~/git/nq/docs/CLAIM_CATALOG.md` — registered claim kinds and verdict vocabulary.
- [[refusal-kernel-to-refusal-receipt-seam]] — runtime-vs-formal-layer split; the bridge work falls on this seam (Lean blocks inference; NQ blocks operational basis-use).

## Provenance

- **2026-05-26** — audit triggered by ChatGPT's correction that the Phase C rebar report's Phase D table read "❌ None" in criterion 3, when NQ's roadmap memo (`ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md`) names NQ as a likely consumer.
- Audit performed by claude-code against the NQ roadmap memo + `WITNESS_PACKET.md` + `CLAIM_PREFLIGHT.md`.
- Honest finding: NQ has the relation operationally; the bridge work is Lean-side, not authorized; no shipping blocker on either side. Memo classification: **B**.

> **The relation is on the wire. The proof is not on the kernel. The urgency is precision-pressure, not capability-pressure. The bridge work is queued, not authorized.**
