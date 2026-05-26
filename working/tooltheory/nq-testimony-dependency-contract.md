# NQ TESTIMONY_DEPENDENCY — Lean-first contract receipt

**Status:** Working note / contract receipt. Not public Lean surface. Not Calculus 2.0. Not a proof of NQ runtime conformance. Filed 2026-05-26 as the prose receipt for the C.3 binding-use bridge in `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` (namespace `Admissibility.RefusalPropagation.Annex.NQDependency`).

**Posture:** Construction-discipline output. The Lean spike names the contract; NQ runtime is expected to conform but conformance is not proved here. Conformance audit is queued as a separate next file.

---

## Core sentence

> **The NQ TESTIMONY_DEPENDENCY cascade must preserve refusal across declared ancestor dependencies: a finding refused because its ancestor cannot testify must not later mint binding authority through the dependent chain.**

## What Lean now models

Tiny three-finding model in `Admissibility.RefusalPropagation.Annex.NQDependency` (annex, experimental, deletion-eligible, **not imported by `CalculusOne.lean`**):

| Object | Role |
|---|---|
| `Finding` | Three constructors: `device_enumeration_witness`, `smart_witness`, `disk_state` |
| `State` | Binary: `observable` / `refused` (collapses NQ's three refusal states for cascade purposes) |
| `DependsOn` | Inductive `Prop` with two named constructors: `smart_on_device`, `disk_on_smart` |
| `Refused` | Predicate: `state f = State.refused` |
| `CascadeSound` | NQ implementation obligation — declared dependency on a refused ancestor produces a refused dependent |
| `BindingAdmissible` | Predicate: `state f = State.observable` — contract for binding use |
| `refused_blocks_binding` | Single-finding bridge: refusal blocks binding-admissibility |
| `disk_state_refused_when_device_enumeration_refused` | Two-hop cascade theorem |
| `disk_state_cannot_bind_when_device_enumeration_refused` | Full chain: ancestor refusal → downstream cannot bind |

`lake build` green at 8298 jobs. `RefusalPropagation.lean` carries four namespaces total (Narrowing / Composition / NQDependency); none are part of the 1.0 public surface; none are imported by `CalculusOne.lean`. The header explicitly marks the module as *experimental rebar, not public promise, may be deleted/renamed/refactored/absorbed*.

The C.4/C.5 adapter shows that the NQ two-hop binding refusal can be proved both directly and via two applications of the generic `Composition.refusal_composes` theorem; this makes the NQDependency contract an instance of the generic refusal-composition skeleton, not merely a bespoke cascade proof.

The NQ two-hop contract pulled a generic `refusal_composes_two_hop` lemma into `RefusalPropagation.Composition`. The downstream disk-state refusal is now provable via the generic two-hop composition law, not only by a bespoke cascade proof.

## The contract

The full chain the Lean spike pins:

```
device_enumeration_witness  refused
        ↓  (CascadeSound — hop 1)
smart_witness               refused
        ↓  (CascadeSound — hop 2)
disk_state                  refused
        ↓  (refused_blocks_binding)
disk_state                  ¬ BindingAdmissible
```

The shape is canonical refusal composition: *ancestor cannot testify ⇒ downstream cannot bind.*

The discipline that bounds what this proves:

> **The theorem proves the intended suppression-cascade shape has a sound formal analogue. It does NOT prove NQ's runtime cascade is sound.**

NQ's runtime cascade is sound only when NQ's implementation satisfies `CascadeSound`. That is a runtime obligation the contract names, not a theorem the spike discharges.

## NQ runtime obligation

The relevant NQ code path (`crates/nq-core/src/preflight.rs` and the upstream publish pipeline in `crates/nq-db/src/publish.rs` + the admissibility view in migration `043_admissibility_declaration.sql`) must enforce:

> **Every published snapshot that carries a refused ancestor must prevent dependent findings reachable through declared `TESTIMONY_DEPENDENCY` from minting binding/preflight authority.**

This includes re-emitted dependents after an ancestor has transitioned to `cannot_testify`. The contract is single-snapshot: every snapshot, at the moment it is published, must satisfy `CascadeSound` and `refused_blocks_binding`. The cross-snapshot side (whether the publish pipeline preserves the invariant under re-emission) is the audit risk recorded below.

In NQ's existing vocabulary the contract decomposes:

- `warning_state.admissibility.state` ∈ `{cannot_testify, suppressed_by_ancestor, suppressed_by_declaration}` → finding is `Refused`.
- `warning_state.ancestor_finding_key` references the ancestor whose refusal forced the dependent's suppression.
- Per-claim-kind `cannot_testify` lists (e.g. `disk_state_cannot_testify`) must fire whenever the dependent chain from a registered claim reaches a refused ancestor.
- `FindingSnapshot.admissibility` (wire export) must surface the refusal + the ancestor key, not collapse them.

## What is deliberately not modeled

The spike is intentionally narrow. The following are out of scope:

- **No multi-snapshot transition relation.** The contract is single-snapshot; cross-snapshot soundness (publish pipeline preserving `CascadeSound` under re-emission) is not yet captured.
- **No runtime conformance proof.** The contract is what NQ must satisfy; conformance is a separate audit (queued as a follow-up file, not this one).
- **No multi-witness composition.** The latent `WITNESS_COMPOSITION` tripwire in `ARCHITECTURE_NOTES.md` is a separate forcing case; this contract does not address composed-witness findings.
- **No general claim graph.** The model is three concrete findings and two declared edges. There is no scope to graph traversal, indexing, or multi-edge reasoning.
- **No scope / time / use-kind / provenance fields.** The brake stayed holstered. None of these entered the model.
- **No full witness-packet model.** Coverage envelope, freshness, declaration metadata, basis lifecycle (`basis_state`) are all absent. The cascade theorem doesn't need them.
- **No general NQ correctness claim.** This is one cascade in one shape. Nothing else is claimed.

If any of these try to enter a future strengthening of the spike, the breeding criterion fires and the work stops.

## Known audit risk

The Explore-agent audit pass (2026-05-26) found that NQ's publish pipeline at `crates/nq-db/src/publish.rs:980-992` performs the upsert before the masking pass runs. When a finding re-emits in a new generation, the upsert sets `visibility_state = 'observed'` and clears suppression fields without re-checking the ancestor's state. The masking map (built later at lines 1300–1314) re-applies suppression on findings absent from the current emission — but a re-emitted dependent could temporarily be in `observed` state inside the same generation before the masking pass touches it.

This is a cross-snapshot risk the **single-snapshot contract above does not cover**. Capturing it formally would require a transition relation between state assignments (a Lean `Transition : (Finding → State) → (Finding → State) → Prop`), which is explicitly out of scope for this spike.

The audit also found:
- Direct (one-hop) cascade is tested (e.g. `admissibility_view_reports_suppressed_by_ancestor_with_witness_reason` in `publish.rs`).
- Two-hop cascade is **NOT** tested. The TESTIMONY_DEPENDENCY V1 non-goals explicitly defer multi-level dependencies.
- Recovery re-evaluation (ancestor recovers, dependent must update) is **NOT** tested.
- Export field preservation (`ancestor_finding_key` on the wire) is **NOT** directly asserted in tests.

These gaps are recorded here as contract pressure, not as a runtime defect claim. The audit findings will land in a separate conformance file.

## Test implications

The contract suggests (does NOT mandate) future NQ tests:

1. **Direct dependency cascade.** `device_enumeration` `cannot_testify` ⇒ `smart_witness` `suppressed_by_ancestor` with `witness_unobservable` reason. (Partial coverage exists.)
2. **Two-hop dependency cascade.** `device_enumeration` `cannot_testify` ⇒ `disk_state` refused (through `smart_witness`). (Not currently tested per V1 non-goals.)
3. **Binding refusal at chain endpoint.** When the ancestor chain reaches a refused finding, `disk_state` preflight must return `cannot_testify` (or the equivalent non-binding verdict), not authorize.
4. **No re-emission bypass.** A re-emitted dependent inside a single published snapshot must not appear as `observable` while its declared ancestor is still refused. This is the cross-snapshot risk; the test would need to exercise re-emission + masking ordering.
5. **Suppression-reason and ancestor-key preservation on the wire.** `FindingSnapshot.admissibility.ancestor_finding_key` must be present on every refused dependent's exported snapshot.

**No schema fields are proposed in this memo.** If tests reveal that the current wire shape cannot express the contract (e.g. some refusal case needs a field not currently shipped), that lands as a separate NQ gap document — not as an addition here.

## Promotion posture

This memo strengthens Phase C rebar by giving the abstract `refusal_composes` shape a concrete NQ-flavored instantiation plus a binding-use bridge.

It **does not open Phase D by itself.** All five Phase D promotion criteria from `~/.claude/plans/i-want-a-plan-groovy-stardust.md` remain unchanged:

- Criterion 1 (composes between kernels): not satisfied — the chain is single-kernel.
- Criterion 2 (new abstraction count): still within budget.
- Criterion 3 (forcing case): still B — *potential consumer identified, forcing case pending*. NQ has the relation on the wire; no current shipping blocker requires the proof.
- Criterion 4 (slogan-blast-radius): the keeper *"the intended suppression-cascade shape has a sound formal analogue"* passes; *"NQ's cascade is provably sound"* does NOT.
- Criterion 5 (PL/UC stays as working notes): unchanged.

The memo **may become a Phase D input** if future NQ work cites this contract as a required soundness condition. Until then it is contract pressure, not promotion pressure.

## Keeper lines

> **Lean leads by naming the contract; runtime follows by conforming to it.**

> **The proof is not a public promise. It is rebar.**

> **The intended suppression-cascade shape has a sound formal analogue.**

> **A refused ancestor may not launder authority through a dependent finding.**

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — namespace `Admissibility.RefusalPropagation.Annex.NQDependency` (the C.3 spike + binding-use bridge).
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Phase C/D versioning plan; this memo updates Phase D criterion 3 framing but does not open Phase D.
- [[nq-forcing-case-audit]] — the predecessor classification (B: plausible consumer, missing instantiation) — instantiation now exists; conformance audit pending.
- [[refusal-kernel-to-refusal-receipt-seam]] — runtime-vs-formal-layer split; this contract lives on the seam (Lean blocks inference; NQ blocks operational binding-use).
- [[uncertainty-custody]] — sibling working note on the gate side (UC's gate-respecting predicate is what PL's projection must preserve; this NQ contract is a different runtime cascade but inherits the same discipline).
- [[projection-laundering]] — sibling working note on the projection side.
- `~/git/nq/docs/ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md` — NQ's roadmap memo. Headline: *the Lean kernel does not tell NQ to become more powerful. It tells NQ to become more exact.*
- `~/git/nq/docs/WITNESS_PACKET.md` §60 — declared-dependency discipline.
- `~/git/nq/docs/CLAIM_PREFLIGHT.md` §73 — `cannot_testify` as constitutional output, not error.
- `~/git/nq/docs/gaps/TESTIMONY_DEPENDENCY_GAP.md` — V1.0+V1.1+V1.2 shipped; the canonical gap doc.
- `~/git/nq/docs/gaps/GENERALIZED_MASKING_GAP.md` — sibling gap; owns the masking machinery.
- `~/git/nq/docs/gaps/CANNOT_TESTIFY_STATUS.md` — status-layer cash-out (proposed).

## Provenance

- **2026-05-26**, three-pass relay.
  - Phase C rebar pass produced abstract `refusal_composes`.
  - NQ forcing-case audit classified NQ as B (plausible consumer, missing instantiation).
  - Construction-discipline gate opened (per claude-web's correction that conservative-trim was applying public-surface discipline to a scratch module).
  - C.3 spike landed: tiny NQ-shaped model + cascade theorem + binding-use bridge.
  - Explore-agent audit pass surveyed `crates/nq-db/src/publish.rs`, `migrations/039–043`, `crates/nq-core/src/export.rs`, and tests; found direct-cascade implemented and tested, two-hop NOT tested, re-emission risk identified, export preservation present but not asserted in tests.
- **Filed:** claude-code, 2026-05-26, as the prose receipt for the binding-use extension. Conformance audit (a separate file) will land next if requested.

> **Lean leads. Runtime follows. Receipt is filed. The hose remains holstered.**
