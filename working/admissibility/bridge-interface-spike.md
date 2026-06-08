# Bridge Interfaces — fenced scratch spike receipt

**Filed:** 2026-06-07. **Status:** scratch spike + companion receipt. **NOT doctrine. NOT a paper. NOT a primitive. NOT promoted.** Lean file is in `~/git/lean/LeanProofs/Scratch/BridgeInterfaces.lean` — fenced scratch, not imported by `LeanProofs.lean`, no 1.0 surface, no paper anchor.

## What this spike tests

> Can admissibility refusals be assigned to *unique* bridge owners when each bridge may consult only a *declared narrow dependency interface*, not the full State?

The probe is the inverse of irreducibility: if specimens factor cleanly under bounded bridges, prior "irreducible" framings are dependent-factorized, not genuinely indecomposable.

Hard constraints (user-supplied, honored throughout):

- Do NOT build a grand calculus.
- Do NOT use full-read bridge predicates.
- Do NOT claim irreducible non-factorization unless a specimen survives all declared bridge owners.
- Do NOT use geometry language.

## Defined columns

Four enumeration columns + one composite State record.

| Column | Type | Inhabitants |
|---|---|---|
| `ResourceClass` | enum | `linear_event`, `affine_budgeted`, `copyable_record`, `reusable_standing`, `counted_token` |
| `Modality` | enum | `witnessed_live`, `receipt_of_witnessing`, `authorized`, `observed`, `justified`, `obligated`, `advisory`, `enforcement` |
| `ClaimKind` | enum | `revocation`, `observation`, `authorization`, `risk_score`, `enforcement_action`, `obligation_claim` |
| `Index` | structure | `actor : String`, `surface : String`, `time : Nat`, `scope : String` |
| `State` | structure | `resource`, `modality`, `claimKind`, `index` |

All enums derive `DecidableEq, Repr`. `Index` and `State` derive `DecidableEq, Repr`.

## Declared dependency interfaces

The architectural constraint: each bridge owns one column and may consult only a *declared narrow interface* to peek at other columns. The interface is realized as named policy functions in `Policies`. Each bridge function calls only the policy names listed in its interface. *No bridge pattern-matches on State directly; each consults only column-typed inputs.*

| Bridge | Owns | Declared interface (named policy functions) | Inspected State fields (source / target) |
|---|---|---|---|
| **ResourceBridge** | `ResourceClass` | `requiredResourceClass : Modality → ClaimKind → ResourceClass → Bool` | source: `modality, claimKind, resource`; target: `modality, claimKind, resource` |
| **IndexBridge** | `Index` | `surfaceScopePolicy : Modality → ClaimKind → String → String → Bool` | source: `modality, claimKind, index.surface`; target: `modality, claimKind, index.surface` |
| **ModalityBridge** | `Modality` | `allowedModalTransition : ClaimKind → ResourceClass → Modality → Modality → Bool`; `isDemotionPolicy : Modality → Modality → Bool` | source: `modality, claimKind, resource`; target: `modality` |
| **ProtocolBridge** | (cross-column protocol invariants) | `custodyRequirement : Modality → ClaimKind → Bool` (stub) | none (no specimen forces it) |

**No bridge inspects:**
- `Index.actor`, `Index.time`, `Index.scope` — these columns are not exercised by any specimen. Candidate for future bridge interfaces.
- The "whole State" — by construction, each bridge function pattern-matches on the named subset only. Verified by code inspection in the Lean file's docstrings.

**Interface deliberately stubbed (not authorized to build):**
- `freshnessKey : Index → ClaimKind → FreshnessKey` (ResourceBridge candidate)
- `budgetPolicy : Modality → ClaimKind → BudgetPolicy` (ResourceBridge candidate)
- `temporalPolicy : Modality → ClaimKind → TemporalPolicy` (IndexBridge candidate)
- `actorScopePolicy : Modality → ClaimKind → ActorScopePolicy` (IndexBridge candidate)
- `authorizationEvidencePolicy : ClaimKind → Index → Bool` (ModalityBridge candidate)
- `terminalStatePolicy : Modality → ClaimKind → TerminalPolicy` (ProtocolBridge candidate)

None of these are forced by the five specimens. They are named here for traceability; the discipline is *interfaces grow with forcing specimens, not by anticipation.*

## Cascade ordering and ownership assignment

```
ResourceBridge → IndexBridge → ModalityBridge → ProtocolBridge
                first refusal wins
```

The cascade is `def cascade (s t : State) : CascadeOutcome`. Outcomes:

- `.accept` — no bridge refused
- `.acceptWithDemotion rule owner` — a bridge accepted via an explicit lawful demotion (records owner)
- `.refuse receipt` — first bridge to refuse; downstream bridges' opinions are not authoritative for ownership

**Ownership is unique by construction:** the cascade returns at most one `.refuse` (the first), so every refused specimen has exactly one primary owner. No "Resource OR Modality" ownership in any final outcome.

## Specimen results

All five specimens build green with zero `sorry`. Verification is done via extractor functions on `CascadeOutcome` (`refusedBy`, `refusalRule`, `refusalDeps`, `demotedBy`, `demotionRule`). Each proof is `rfl`.

### Specimen 1 — witnessed_live source/target, copyable_record at target

- **Source:** `linear_event, witnessed_live, observation, S1`
- **Target:** `copyable_record, witnessed_live, observation, S1`
- **Expected:** Refused by ResourceBridge.
- **Result:** REFUSED by ResourceBridge.
  - **Rule:** `target_resource_invalid_for_modality`
  - **Dependencies consulted:** `[requiredResourceClass]`
  - **Receipt verified by:** `(cascade s1_source s1_target).refusedBy = some .resource := by rfl`
- **Verdict on irreducibility:** *Not irreducible.* ResourceBridge handles it via one named policy. The original "witness becoming copyable while staying live" framing is dependent-factorized.

### Specimen 2 — witnessed_live → receipt_of_witnessing with copyable_record at target

- **Source:** `linear_event, witnessed_live, observation, S1`
- **Target:** `copyable_record, receipt_of_witnessing, observation, S1`
- **Expected:** Accepted with explicit demotion by ModalityBridge.
- **Result:** ACCEPTED WITH DEMOTION by ModalityBridge.
  - **Rule:** `lawful_demotion`
  - **Owner of the demotion:** `.modality`
  - **Path:** ResourceBridge accepts (target `(receipt_of_witnessing, copyable_record)` is admissible per `requiredResourceClass`); IndexBridge declines to own (cross-modality transition not its territory); ModalityBridge sees `isDemotionPolicy witnessed_live receipt_of_witnessing = true`, returns `.acceptWithDemotion`.
  - **Verified by:** `(cascade s2_source s2_target).demotedBy = some .modality := by rfl`
- **Verdict on irreducibility:** *Not irreducible.* This is the lawful emission/demotion path: a witness becoming its own receipt is an explicit modality-altering transition, owned by ModalityBridge.

### Specimen 3 — authorized revocation, cross-surface

- **Source:** `copyable_record, authorized, revocation, Asurf`
- **Target:** `copyable_record, authorized, revocation, Bsurf`
- **Expected:** Refused by IndexBridge.
- **Result:** REFUSED by IndexBridge.
  - **Rule:** `surface_scope_violation`
  - **Dependencies consulted:** `[surfaceScopePolicy]`
  - **Verified by:** `(cascade s3_source s3_target).refusedBy = some .index := by rfl`
- **Verdict on irreducibility:** *Not irreducible.* Surface scope is owned by IndexBridge under a named policy.

### Specimen 4 — authorized → observed (signature as observation)

- **Source:** `copyable_record, authorized, authorization, S1`
- **Target:** `copyable_record, observed, observation, S1`
- **Expected:** Refused by ModalityBridge.
- **Result:** REFUSED by ModalityBridge.
  - **Rule:** `modality_transition_not_authorized`
  - **Dependencies consulted:** `[allowedModalTransition, isDemotionPolicy]`
  - **Verified by:** `(cascade s4_source s4_target).refusedBy = some .modality := by rfl`
- **Verdict on irreducibility:** *Not irreducible.* The `authorized → observed` transition is not in the allowed-transitions table and is not a lawful demotion. ModalityBridge owns this refusal cleanly.

### Specimen 6 — advisory gradient (added 2026-06-07, deliberate harder probe)

Three-state chain: `advisory/risk_score → advisory/visibility_constraint → enforcement/enforcement_action`.

A new ClaimKind `visibility_constraint` was added to model the "platform visibility-affecting" intermediate state. The gradient is split into two transitions (Specimen 6a and 6b) so each leg can be audited under bounded interfaces independently.

#### Specimen 6a — intra-modality claim-kind drift

- **Source:** `copyable_record, advisory, risk_score, S1`
- **Target:** `copyable_record, advisory, visibility_constraint, S1`
- **Expected under current bounded interfaces:** ACCEPT (probe: does anything catch claim-kind drift within a stable modality?).
- **Result:** ACCEPT.
  - **Verified by:** `cascade s6a_source s6a_target = .accept := by rfl`
- **Bridge-by-bridge:**
  - ResourceBridge: `advisory` is unconstrained on resource under `requiredResourceClass`; accept.
  - IndexBridge: requires modality AND claimKind to be stable before firing on `surfaceScopePolicy`; claimKind changes, so the bridge declines ownership; accept.
  - ModalityBridge: `allowedModalTransition` checks `m1 = m2` only — claimKind-blind. Identity modality → accept.
  - ProtocolBridge: stub; accept.
- **Verdict on irreducibility:** *Not applicable yet — this is a discovery, not a refusal.*
- **DISCOVERY:** No current bridge owns claim-kind transitions when modality is stable. `ClaimKind` is currently a *parameter* to other bridges' interfaces, but no bridge *owns* its column. Intra-modality claim-kind drift is unowned.

#### Specimen 6b — cross-modality escalation with new origin

- **Source:** `copyable_record, advisory, visibility_constraint, S1`
- **Target:** `copyable_record, enforcement, enforcement_action, S1`
- **Expected:** REFUSED by ModalityBridge (similar to Specimen 5, different origin claimKind).
- **Result:** REFUSED by ModalityBridge.
  - **Rule:** `modality_transition_not_authorized`
  - **Verified by:** `(cascade s6b_source s6b_target).refusedBy = some .modality := by rfl`
- **Verdict:** *Not irreducible.* ModalityBridge owns the cross-modality refusal cleanly.

#### Gradient-level observation

The chain `advisory/risk_score → advisory/visibility_constraint → enforcement/enforcement_action` passes the cross-modality gate (Step 2 / S6b) *only because Step 1 (S6a) silently smuggled the claim-kind escalation into the advisory column.* The first leg is the laundering surface; the second leg is where the existing instrument fires.

This is exactly the kind of finding the bounded-interface design exists to expose: **an under-owned column visible by the order in which refusals land along a multi-step chain.**

#### Candidate missing-interface analyses (recorded, not authorized to build)

Three candidate resolutions for the S6a gap. None is built; the spike records the discovery, not the fix.

| Candidate | Shape | Cost | Caveat |
|---|---|---|---|
| **(α) Extend ModalityBridge** | Make `allowedModalTransition` claimKind-sensitive (e.g., `_, _, m1, m2, c1, c2 => decide (m1 = m2 ∧ c1 = c2)`); add policy-level allowance for specific claim-kind transitions. | Lowest — extends an existing interface. | Crowds ModalityBridge with two distinct responsibilities (modality ownership + claim-kind ownership). Ownership ambiguity may follow if a transition changes both. |
| **(β) New ClaimKindBridge** | Add a fifth bridge owning the `ClaimKind` column with its own interface (e.g., `allowedClaimKindTransition : Modality → ClaimKind → ClaimKind → Bool`). | Medium — new bridge + new cascade slot. | Cleanest separation. Requires deciding cascade position: before or after ModalityBridge? |
| **(γ) Extend ProtocolBridge** | Treat claim-kind transitions as cross-column protocol invariants and own them in ProtocolBridge (currently stubbed). | Medium — populates the stub with first real content. | Loads ProtocolBridge with protocol-shaped invariants it was reserved for; risks ProtocolBridge becoming a kitchen sink for "things no other bridge owns." |

**Operator's reading (recorded, not adjudicated):** (β) is structurally cleanest; (γ) is most parsimonious; (α) is the slippery one (combines responsibilities and may produce the ownership ambiguity the user warned against).

No selection authorized. Each candidate is named so the next specimen forcing this gap finds the menu rather than having to re-derive it.

#### What this discovery does NOT claim

- Not a candidate irreducible result. The S6a accept is *unowned*, not *unrefutable*. A future bridge addition (α / β / γ) could own it.
- Not a method failure. The spike exists to surface such gaps; S6a is the spike doing its job.
- Not authorization to add a new column. ClaimKind already exists as a column-typed field; the question is whether it needs its own *owner* (bridge), not whether the column is missing.
- Not a paper claim. The discovery is methodological; no public artifact updated.

### Specimen 5 — advisory risk_score → enforcement enforcement_action (ambiguity probe)

- **Source:** `copyable_record, advisory, risk_score, S1`
- **Target:** `copyable_record, enforcement, enforcement_action, S1`
- **Expected:** Attempt to classify; if multiple bridges want ownership, refine until exactly one owns.
- **Result:** REFUSED by ModalityBridge.
  - **Rule:** `modality_transition_not_authorized`
  - **Dependencies consulted:** `[allowedModalTransition, isDemotionPolicy]`
- **Ambiguity check:** Each non-firing bridge verified to return `.accept` in isolation:
  - `(ResourceBridge.decide s5_source s5_target).isAccept = true := by rfl`
  - `(IndexBridge.decide s5_source s5_target).isAccept = true := by rfl`
  - `(ProtocolBridge.decide s5_source s5_target).isAccept = true := by rfl`
- **Verdict on ownership:** Unambiguous. The risk-score-to-enforcement-instruction transition is owned by ModalityBridge. IndexBridge does not fire (same surface). ResourceBridge does not fire (target resource is admissible for `enforcement` per the current `requiredResourceClass` table, which is unconstrained on non-witnessed modalities). ProtocolBridge is a stub.
- **Caveat (recorded, not promoted to candidate-irreducible):** The current `requiredResourceClass` table is permissive on `enforcement`. A stricter policy would force `enforcement` to require `linear_event` or `counted_token` (matching the audit-trail discipline of enforcement-altitude actions); that policy refinement would cause ResourceBridge to also fire, *introducing* the ownership ambiguity the user warned about. The fact that no ambiguity arises *under the current bounded interfaces* is not evidence that no ambiguity could arise under stricter ones. This is a calibration note, not a finding.

## Acceptance criteria check

| Criterion | Status |
|---|---|
| Lean builds | ✓ `lake build LeanProofs.Scratch.BridgeInterfaces` — 853ms, success |
| Each specimen → accepted with explicit receipt/demotion OR refused with exactly one primary owner | ✓ 6/7 (S6a's accept is unowned-by-design, see Discovery; counts as accept-without-demotion within the cascade contract) |
| Every refusal receipt lists bounded dependencies consulted | ✓ 5/5 refusals (S1, S3, S4, S5, S6b) carry explicit dependency lists; S2's demotion records the owner; S6a has no refusal to record |
| No bridge inspects entire State directly | ✓ Verified by inspection: docstrings on each bridge function declare the inspected fields; no bridge pattern-matches on the full State record |
| No "Resource OR Modality" ownership in final table | ✓ Each refusal has exactly one `owner` |
| Prior dead specimens classified as dependent-factorized | ✓ Specimens 1, 3, 4, 5, 6b are all dependent-factorized — refused by bounded bridges with named interface dependencies |
| Candidate irreducible cases enumerated with bounded owner attempts, why each fails, what dependency would be needed | N/A — no candidate irreducible specimen emerged. **Specimen 6a surfaced a candidate missing-owner gap (intra-modality claim-kind drift); three resolution candidates (α/β/γ) are recorded but none built.** |

## No irreducible result yet — but the boundary moved

> *No specimen in this spike survived all four declared bridge owners as a refusal candidate.* Specimens 1–5 are dependent-factorized under bounded interfaces. **Specimen 6a is *unowned* — accepted under current bounded interfaces because no bridge owns intra-modality claim-kind drift.** This is a different shape than irreducibility: a candidate-irreducible specimen would survive all bridges *as a refusal*; S6a *passes* all bridges trivially because none claims ownership.

The strongest claim available after the gradient probe:

> Under the current bounded interfaces — `requiredResourceClass`, `surfaceScopePolicy`, `allowedModalTransition`, `isDemotionPolicy`, `custodyRequirement` (stub) — five of seven tested specimens factor cleanly into single-owner refusals or lawful demotions; one (Specimen 6a, intra-advisory claim-kind drift) passes unowned, revealing a missing-owner gap in the current bridge set.

The S6a gap is *not* irreducibility. It is *under-coverage*: a transition class for which no current bridge has claimed ownership. The fix is one of three named candidates (α extend ModalityBridge / β new ClaimKindBridge / γ extend ProtocolBridge), none authorized to build in this spike.

Future specimens may force one of those candidates to be built; alternatively, a stricter policy on existing interfaces may also force ambiguity (per the S5 calibration note). Either route is consistent with the spike's purpose: *measure interface width and ownership coverage by what specimens force.*

## Candidate new columns / interfaces (named, not authorized)

Each of the following would be motivated by a specimen that the current interfaces cannot cleanly own. None is built; all are recorded for traceability:

- **freshnessKey** (ResourceBridge): forced by any specimen where the *time-since-witness* matters for resource admissibility (e.g., stale witness becoming inadmissible). Not exercised.
- **budgetPolicy** (ResourceBridge): forced by any specimen involving `affine_budgeted` or `counted_token` consumption. Not exercised.
- **temporalPolicy** (IndexBridge): forced by any specimen where target's `Index.time` must be strictly later than source's. Not exercised.
- **actorScopePolicy** (IndexBridge): forced by any specimen where actor identity is load-bearing for admissibility (cross-actor transitions). Not exercised.
- **authorizationEvidencePolicy** (ModalityBridge): forced by any specimen where the `authorized` modality requires explicit evidence at the Index altitude. Not exercised in current spike — the modality-table is currently structural.
- **terminalStatePolicy** (ProtocolBridge): forced by any specimen where terminal-state custody matters (e.g., enforcement-action records must be terminal-state-bound). Not exercised; ProtocolBridge is a stub.
- **Candidate fifth column: Provenance / Evidence-Origin** — currently encoded implicitly in `ClaimKind`; a specimen where two transitions agree on (resource, modality, claimKind, index) but differ on *evidence origin* would force a fifth column. Not exercised.

## Implementation notes

- All proofs use `rfl`. No `decide`, no `native_decide`, no `simp`, no `sorry`.
- The initial draft used `match` patterns inside `decide`-tactic verifications; that failed Decidable-instance synthesis. Replaced with extractor functions (`refusedBy`, `refusalRule`, `refusalDeps`, `demotedBy`, `demotionRule`) that return `Option`-wrapped values amenable to `rfl`. Same content, no instance-synthesis pain.
- Policies use `decide (a = b)` for String comparison; reduces on concrete literals.
- The cascade is a pure `def` over concrete inductives; every specimen reduces to a normal form, so `rfl` is the right proof.
- Build time: 841ms cold. Sorry-free per `[[feedback-lean-debt-discipline]]`.
- Custody-Class: `SCRATCH`. Header declares non-import-by-LeanProofs, no paper anchor, no promotion path, no discharge use.

## What this spike does NOT do

- Does NOT claim a calculus. The four-bridge cascade is a *specimen carrier*, not a unification target. Adding more bridges or more interfaces does not bring this closer to a calculus.
- Does NOT promote any of the named-but-unstubbed interfaces. Each is recorded only.
- Does NOT prove admissibility is decomposable. The set of five specimens is small; the policies are permissive in places (e.g., `enforcement` is unconstrained on resource); the absence of irreducible specimens here is consistent with their existence elsewhere.
- Does NOT claim ownership uniqueness is preserved under interface refinement. The S5 calibration note explicitly flags that stricter policies could produce ambiguity.
- Does NOT use geometry language. The bridges are named for the column they own, not for any spatial / metric / topological structure.
- Does NOT discharge anything in the public corpus. The Scratch file is fenced.

## Curdling guard

This spike operates at fenced-scratch altitude only. No Lean module promoted. No bridge-obligation-lattice atom added. No new primitive minted. No paper-shape motion. The companion Lean file declares Custody-Class: SCRATCH, no-import, no-paper-anchor, no-promotion-path, no-discharge-use.

If a future forcing specimen produces a candidate irreducible result, the corresponding spike would need:
- all bounded owner attempts enumerated
- the failure mode of each enumerated
- the missing interface, column, or genuine-irreducibility verdict named explicitly
- a separate fenced file (not this one), per the per-promotion-gate discipline

## Cross-references

- Lean file: `~/git/lean/LeanProofs/Scratch/BridgeInterfaces.lean`
- Sibling scratch kernels in `~/git/lean/LeanProofs/Scratch/`: `NoSilentProjection.lean`, `BoundaryTransit.lean`, `SurfaceDeformationRequiresCoupling.lean`, `AggregateWitnessRequiresJoin.lean`, `LogOnlyProvesEmission.lean`
- Doctrine sibling: [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) — the spike's cousin at the obligation-set altitude (a different cut on the same territory)
- Doctrine sibling: [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — the federation discipline that prevents this spike from being read as a calculus candidate
- [[project-lean-custody-state]] — custody-class discipline this file honors
- [[feedback-lean-debt-discipline]] — sorry-free build requirement honored

---

**No method change. No promotion. No paper-shape motion. Five specimens factor cleanly under bounded interfaces; no candidate irreducible result. Build green; sorry-free; receipt filed.**
