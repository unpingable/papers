# Provenance Profiles — scratch receipt

**Filed:** 2026-06-08. **Status:** scratch receipt for the fenced Lean spike. **NOT doctrine. NOT a paper. NOT a primitive. NOT promoted.** Companion to `~/git/lean/LeanProofs/Scratch/ProvenanceProfiles.lean` — fenced scratch, Custody-Class: SCRATCH, not imported by `LeanProofs.lean`, no 1.0 surface, no paper anchor, no promotion path. Receipt only.

## What this records

Two slices of a fenced Lean spike on provenance profiles + custody. Two layers, one consistency check between them. The artifact is small, green (569 lines, 717ms build, zero sorries, zero warnings), and useful in a narrow sense. The receipt records what the spike actually proves and what it deliberately does not.

## What landed in Lean

**Static provenance cube** (LicensedTransition layer):

- `Rung`, `StructuralProfile`, `Indices`, `Resource` — types
- `RungStep` — inductive relation (constructors-only, not implication-based)
- `LicensedTransition` — inductive, five positive constructors
- 5 positive existence theorems witnessing the relation is non-empty
- 5 negative refusal theorems (signature ≠ observation; stale ≠ claim; observation ≠ promotion direct; receipt ≠ live event; cross-surface ≠ revocation), each paired with a nearby positive
- Bridge theorem: `licensed_implies_rung_step`

**Custody layer** (operational, separate from the static cube):

- `CustodyHolder`, `CustodyEvent`, `CustodyTrace`
- `hasUnownedGap`, `contractFirst`
- `custody_contraction_admits_unowned_gap` (existence specimen — corpse + witness)

**Lawfulness layer** (added in the second slice):

- `TraceWellOwned` — independent predicate over traces
- `CustodyOpKind` — operations as DATA (noop / handoff / contractFirst)
- `applyCustodyOperation` — interpreter
- `LawfulCustodyOperation` — **syntactic whitelist** (noop_lawful + handoff_lawful constructors; no contractFirst constructor; no `PreservesOwnership` field)
- 3 positive lawfulness witnesses (`noop_is_lawful`, `handoff_to_carol_is_lawful`, `exists_lawful_custody_operation`)
- Preservation theorem: `lawful_preserves_well_owned : LawfulCustodyOperation op → TraceWellOwned t → TraceWellOwned (applyCustodyOperation op t)`
- Bad-operation refusal: `contractFirst_not_lawful`
- Counterexample witness: `contractFirst_creates_unowned_gap`
- Consistency check: `lawfulness_forbids_contractFirst_admission`

## Core claims (the ones the artifact actually supports)

1. **Static provenance refusals are non-vacuous.** Each refusal is paired with a nearby positive existence theorem witnessing the relation is inhabited in the relevant area. The negative theorems are not "lock the door on an empty building."

2. **Custody failures require an operational trace layer beyond the static cube.** The cube refuses single-move category lies. The custody layer refuses structural operations that produce unowned events on otherwise well-owned traces. The two are not redundant: the cube cannot represent operations on traces, and the trace layer cannot represent rung-shape category lies.

3. **Lawfulness is syntactic and nonempty, not defined as preservation.** `LawfulCustodyOperation` is an inductive whitelist with positive constructors. It does not contain `PreservesOwnership` (or `TraceWellOwned`-preserving) as a field. The preservation theorem is a *separate* theorem proven over the whitelist — not a tautology baked into the definition.

4. **`contractFirst` is a counterexample operation.** There exists a well-owned trace whose image under `applyCustodyOperation .contractFirst` is not well-owned (the merge erases handoff and the merged event holds `.unowned`).

5. **`contractFirst` is excluded from `LawfulCustodyOperation` not by taste but by incompatibility with the ownership-preservation obligation.** Specifically: if `.contractFirst` were admitted to the whitelist, the joint discipline of `lawful_preserves_well_owned` and `contractFirst_creates_unowned_gap` would produce False. This is proven inline as `lawfulness_forbids_contractFirst_admission`. The exclusion is not arbitrary *relative to the preservation obligation* — the whitelist is always a chosen surface, but the *chosen surface plus the preservation theorem* leaves no room to silently add `.contractFirst`.

## The two-layer decomposition (recorded, not promoted)

| Layer | Catches | Form of refusal |
|---|---|---|
| Static cube (`LicensedTransition`) | illegal single-move provenance / rung / index transitions | refusal of a single resource-to-resource transition |
| Custody operation layer | trace-level ownership gaps introduced by composition operations | exclusion of a specific operation from the lawful-whitelist |

The two layers operate on different domains. The cube's domain is pairs of resources. The custody layer's domain is operations on traces. A theorem about one does not directly transfer to the other. The decomposition is a small architectural finding; it is not a general claim about how all admissibility should be structured.

## What this does NOT claim

- **Not a theorem about real custody systems.** The corpus consists of named synthetic resources and three named operations. The instrument was sharpened; whether it cuts real meat is untested.
- **Not a proof that ownership preservation is the right invariant.** `TraceWellOwned` was picked because it lets a non-vacuous preservation theorem land. A different invariant might give different lawfulness shapes.
- **Not a generalization to multi-step custody chains, branching custody, or concurrent custody.** Linear list-based traces only.
- **Not a claim that `LawfulCustodyOperation` is the right whitelist.** The whitelist contains the minimum needed to make the preservation theorem land and to refuse the known bad operation. Adding more operations is future work; each one would have to be shown to preserve.
- **Not a generalization beyond `contractFirst`.** Other structural operations on traces might also be unsafe (chain-splicing, history-rewriting, owner-coalescing, etc.) and would need their own counterexample witnesses.
- **Not a paper claim.** Internal scratch only. Custody-Class: SCRATCH preserved in the Lean header.

## Build state

```text
File:       ~/git/lean/LeanProofs/Scratch/ProvenanceProfiles.lean
Lines:      569
Build:      lake build LeanProofs.Scratch.ProvenanceProfiles — 717ms
Sorries:    0
Warnings:   0
Imported:   no (fenced; not in LeanProofs.lean)
Custody:    SCRATCH per header
```

## Cross-references

- Lean file: `~/git/lean/LeanProofs/Scratch/ProvenanceProfiles.lean`
- Sibling scratch spike: `~/git/lean/LeanProofs/Scratch/BridgeInterfaces.lean` (companion receipt at `~/git/papers/working/admissibility/bridge-interface-spike.md`) — the bounded-dependent-factorization spike; this provenance spike is independent but the OWNERSHIP-GAP shape recurs in different vocabulary
- Doctrine adjacency: `working/no-unifier-without-laundering.md` — federation discipline that prevents this from reading as a calculus candidate
- `[[project-lean-custody-state]]` — custody-class discipline honored

## Curdling guard

Fenced scratch only. No Lean module promoted. No primitive minted. No paper-shape motion. The Lean file declares Custody-Class: SCRATCH in its header. The two layers are independent receipts; no synthesis claimed between them.

---

**Two layers, one consistency check, zero promotion. Small, green, fenced, annoyingly honest.**
