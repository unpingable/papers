# Bridge Interfaces — fenced scratch spike receipt

**Filed:** 2026-06-07. **Last updated:** 2026-06-08 (β patch: ClaimKindBridge added in response to Specimen 6a OWNERSHIP-GAP). **Status:** scratch spike + companion receipt. **NOT doctrine. NOT a paper. NOT a primitive. NOT promoted.** Lean file is in `~/git/lean/LeanProofs/Scratch/BridgeInterfaces.lean` — fenced scratch, not imported by `LeanProofs.lean`, no 1.0 surface, no paper anchor.

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
| **ClaimKindBridge** *(added 2026-06-08, flat β patch)* | `ClaimKind` | `allowedClaimKindTransition : ClaimKind → ClaimKind → Bool` *(no Modality parameter — deliberately flat)* | source: `claimKind`; target: `claimKind`. **Does NOT read modality, resource, index, or any other column.** Fires on every claim-kind transition. Cascade order (ClaimKindBridge after ModalityBridge) handles overlap with cross-modality cases. |
| **ProtocolBridge** | (cross-column protocol invariants) | `custodyRequirement : Modality → ClaimKind → Bool` (stub) | none in the current spike; a coherent protocol specification may precede a specimen |

**No bridge inspects:**
- `Index.actor`, `Index.time`, `Index.scope` — these columns are not exercised by any specimen. Candidate for future bridge interfaces.
- The "whole State" — by construction, each bridge function pattern-matches on the named subset only. Verified by code inspection in the Lean file's docstrings.

**Interfaces deliberately stubbed in this spike's scope:**
- `freshnessKey : Index → ClaimKind → FreshnessKey` (ResourceBridge candidate)
- `budgetPolicy : Modality → ClaimKind → BudgetPolicy` (ResourceBridge candidate)
- `temporalPolicy : Modality → ClaimKind → TemporalPolicy` (IndexBridge candidate)
- `actorScopePolicy : Modality → ClaimKind → ActorScopePolicy` (IndexBridge candidate)
- `authorizationEvidencePolicy : ClaimKind → Index → Bool` (ModalityBridge candidate)
- `terminalStatePolicy : Modality → ClaimKind → TerminalPolicy` (ProtocolBridge candidate)

None of these is exercised by the five specimens. They are named here for traceability. A coherent interface specification may be formalized in Scratch before a specimen exists and may lead later code; specimens remain useful for priority and stress testing, not permission. Public promotion and runtime conformance remain separate.

## Cascade ordering and ownership assignment

```
ResourceBridge → IndexBridge → ModalityBridge → ClaimKindBridge → ProtocolBridge
                       first refusal wins
```

(ClaimKindBridge inserted 2026-06-08 between Modality and Protocol. The bridge is **flat** — it consults only its own column (claim-kind transition pair). Cascade order does the disambiguation work for cross-modality cases: in S4, S5, S6b the flat ClaimKindBridge would also refuse in isolation, but ModalityBridge fires first in the cascade and ClaimKindBridge never runs. Ownership of those specimens is therefore *single-owner-after-cascade-order*, not *single-owner-as-the-only-bridge-that-could-have-fired*. Recorded honestly; verified in Lean via explicit isolation proofs (`(ClaimKindBridge.decide s4_source s4_target).isAccept = false := by rfl`, and similarly for S5, S6b).)

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

**Original probe (2026-06-07):**

- **Source:** `copyable_record, advisory, risk_score, S1`
- **Target:** `copyable_record, advisory, visibility_constraint, S1`
- **Expected under pre-β bounded interfaces:** ACCEPT (probe: does anything catch claim-kind drift within a stable modality?).
- **Result (pre-β):** ACCEPT.
- **DISCOVERY:** No bridge owned claim-kind transitions when modality was stable. `ClaimKind` was a *parameter* to other bridges' interfaces; no bridge *owned* its column. Intra-modality claim-kind drift was unowned. **OWNERSHIP-GAP** — distinct from irreducibility (a transition that no bounded owner can refuse) and from ambiguity (multiple bridges fire). The cascade silently accepts because no bridge claims jurisdiction.

**Post-flat-β patch (2026-06-08):**

- **Result:** REFUSED by ClaimKindBridge (flat).
  - **Rule:** `claim_kind_transition_not_authorized`
  - **Dependencies consulted:** `[allowedClaimKindTransition]`
  - **Verified by:** `(cascade s6a_source s6a_target).refusedBy = some .claim_kind := by rfl`
- **Bridge-by-bridge (post-flat-β):**
  - ResourceBridge: accept (`advisory` unconstrained on resource).
  - IndexBridge: accept (requires modality AND claimKind stability before firing on its surface rule; claimKind drift declines ownership).
  - ModalityBridge: accept (identity modality).
  - ClaimKindBridge: REFUSES — consults `allowedClaimKindTransition risk_score visibility_constraint` which returns `false` under the identity-only baseline policy. **The bridge reads ONLY the claim-kind transition pair.** No modality read; no resource read; no index read.
  - ProtocolBridge: not reached.
- **Verdict transition:** the original OWNERSHIP-GAP has been captured. The discovery has converted from *"gap found"* to *"gap captured."*
- **Why flat:** the design choice was deliberate, per claude-web's diagnostic suggestion. If ClaimKind genuinely owns its column, a bridge consulting only that column should suffice. If ClaimKind needs to read modality or `forceOf` to distinguish licensed transitions from laundering, the flat bridge would have failed — and the failure would have surfaced a *bounded coupling* between ClaimKind and Modality. For the current specimen set, the flat bridge passes; the coupling question is *deferred*, not resolved (see § Force-coupling question).
- **Regression check:** all five pre-existing specimens (S1, S2, S3, S4, S5) verified unchanged under the new cascade — proofs added inline in the Lean file. The flat-β patch is cascade-order-additive: it captures S6a without disturbing prior single-owner cascade outcomes.

#### Honest-accounting diagnostic: would-fire overlap

The flat ClaimKindBridge fires on **every** claim-kind transition, not only intra-modality ones. For S4, S5, S6b — cross-modality transitions where claimKind also drifts — the flat bridge would refuse in isolation. The cascade outcome is ModalityBridge only because ModalityBridge fires earlier in the cascade. Lean proofs verify this in isolation:

```
(ClaimKindBridge.decide s4_source s4_target).isAccept = false  -- would refuse
(ClaimKindBridge.decide s5_source s5_target).isAccept = false  -- would refuse
(ClaimKindBridge.decide s6b_source s6b_target).isAccept = false  -- would refuse
```

This is honest about the trade-off: the flat bridge has **bridge-firing overlap** with ModalityBridge on cross-modality+cross-claimKind cases, resolved only by cascade position. A stricter design (e.g., the original non-flat ClaimKindBridge with `s.modality = t.modality` guard) avoids the overlap but couples ClaimKindBridge to the modality column. The trade-off is: *bridge purity (flat) vs ownership purity (guarded).* The current spike chooses bridge purity; cascade-order is the disambiguator.

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

#### Candidate missing-interface analyses (resolved 2026-06-08)

Three candidates were originally recorded:

| Candidate | Shape | Outcome |
|---|---|---|
| **(α) Extend ModalityBridge** | Make `allowedModalTransition` claimKind-sensitive. | *Rejected.* Would crowd ModalityBridge with two responsibilities and risk reintroducing ownership ambiguity on cross-modality + cross-claimKind transitions. |
| **(β) New ClaimKindBridge** | Add a fifth bridge owning `ClaimKind` with its own interface. | **Selected and built.** Cleanest separation; intra-modality-only firing rule preserves unique ownership. |
| **(γ) Extend ProtocolBridge** | Treat claim-kind transitions as protocol invariants in ProtocolBridge. | *Held.* Plausible later for multi-step workflows where claim-kind transitions are protocol-trace-shaped. Risks ProtocolBridge becoming a junk drawer if used preemptively. |

β implementation choices:
- **Position in cascade:** between ModalityBridge and ProtocolBridge.
- **Firing guard:** `s.modality = t.modality` — ClaimKindBridge only owns intra-modality claim-kind transitions. Cross-modality drift remains ModalityBridge's territory. This preserves the uniqueness-of-ownership invariant.
- **Policy:** identity-only baseline (`allowedClaimKindTransition _ c1 c2 = decide (c1 = c2)`). No transitions licensed. A future coherent policy or specimen can introduce licensed transitions explicitly (e.g., `risk_score → obligation_claim` if such a lawful escalation needs to be modeled).
- **Interface name:** `allowedClaimKindTransition : Modality → ClaimKind → ClaimKind → Bool`.

#### What this discovery does NOT claim

- Not a candidate irreducible result. The S6a accept is *unowned*, not *unrefutable*. A future bridge addition (α / β / γ) could own it.
- Not a method failure. The spike exists to surface such gaps; S6a is the spike doing its job.
- Not evidence that a new column is needed. ClaimKind already exists as a column-typed field; the question is whether it needs its own *owner* (bridge), not whether the column is missing.
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
| Lean builds | ✓ `lake build LeanProofs.Scratch.BridgeInterfaces` — 1.1s, success |
| Each specimen → accepted with explicit receipt/demotion OR refused with exactly one primary owner | ✓ 7/7 (post-β): S1, S3, S4, S5, S6a, S6b are single-owner refusals; S2 is a lawful demotion |
| Every refusal receipt lists bounded dependencies consulted | ✓ 6/6 refusals carry explicit dependency lists; S2's demotion records the owner |
| No bridge inspects entire State directly | ✓ Verified by inspection: docstrings on each bridge function declare the inspected fields; no bridge pattern-matches on the full State record. ClaimKindBridge inspects only `modality` and `claimKind` (source + target) per its declared interface. |
| No "Resource OR Modality" ownership in final table | ✓ Each refusal has exactly one `owner` |
| Prior dead specimens classified as dependent-factorized | ✓ Specimens 1, 3, 4, 5, 6b are all dependent-factorized — refused by bounded bridges with named interface dependencies. Specimen 6a is now also dependent-factorized post-β. |
| Candidate irreducible cases enumerated with bounded owner attempts, why each fails, what dependency would be needed | N/A — no candidate irreducible specimen emerged. **Specimen 6a's OWNERSHIP-GAP was resolved by the β patch (new ClaimKindBridge); the discovery converted from "gap found" to "gap captured."** |

## Verdict-family vocabulary (transition classifications)

Per claude-web's correction (2026-06-08): a *verdict family* classifies a transition given a *total bridge set.* The verdict families form a closed taxonomy of how a transition can land under a well-formed model:

| Verdict family | Definition | Status in this spike |
|---|---|---|
| **single-owner refusal** | Exactly one bridge fires `.refuse` for a specimen, given the cascade order. May coexist with would-fire overlap from a downstream bridge (see honest-accounting note). | Demonstrated by S1, S3, S4, S5, S6a (post-flat-β), S6b. |
| **lawful demotion** | An accept-with-demotion outcome carries an explicit rule and owner; the transition is legal but signals a modality shift. | Demonstrated by S2. |
| **ambiguous ownership (in-isolation)** | Two or more bridges would fire on the same specimen under bounded interfaces; cascade order is the only disambiguator. Distinct from a single-owner refusal because *multiple bridges register refusal in isolation*. | Demonstrated by S4, S5, S6b under the flat-β interfaces (ClaimKindBridge would also refuse; ModalityBridge fires first per cascade order). *Not* observed under a guarded-β variant. The presence of this family is a calibration signal, not a fault. |
| **candidate irreducible** | A specimen survives all declared bridge owners *as a refusal candidate* — each bounded owner attempts and fails to refuse, recording why and what dependency would have been needed. | *Not observed* in this spike. |

## Architectural well-formedness diagnostic (NOT a verdict family)

Per claude-web's correction: *OWNERSHIP-GAP is not a verdict family.* It is a property of the bridge architecture, not of the transition. It manifests as `∃ column changing, ∀ bridge, ¬owns`. It is *temporary*: repair coverage and the gap converts a transition's verdict back into one of the four families above.

| Architectural diagnostic | Definition | Status in this spike |
|---|---|---|
| **OWNERSHIP-GAP** | Some column changes between source and target, and no bridge in the current set claims jurisdiction. The cascade accepts trivially. Resolves once the bridge set is total. **Not a Verdict constructor in Lean** — putting it in the `Verdict` sum type would reify a temporary architectural defect as domain ontology. | Surfaced by S6a under the pre-β bridge set (4 bridges); resolved by adding ClaimKindBridge. After repair, S6a's verdict is single-owner-refusal. |

The bounded-interface design's *purpose* is to surface OWNERSHIP-GAPs — visible by *which column changed* and *which bridge didn't fire*. Once exposed, the gap is patched and disappears from the verdict landscape.

## Effect grounding (added 2026-06-08)

The earlier deferral named a `ForceGrade` diagnostic but flagged the risk: *forceOf : ClaimKind → ForceGrade* is just another unsigned authority surface, forged in the parking lot unless something witnesses it. The correction (operator + claude-web, 2026-06-08):

> **Force is not a property of the name. Force is a property of what acting on the claim does.**

So the diagnostic chain stops at *effect*, not at force labels. Implemented:

```text
ClaimKind
  → EffectSignature   (asserted, per-claim-kind operational declaration)
  → EffectSeverity    (derived, mechanical projection)
```

### EffectSignature

A 6-axis boolean record. Each axis is operational, not a severity grade:

```lean
structure EffectSignature where
  changesVisibility  : Bool
  changesAccess      : Bool
  changesStanding    : Bool
  changesObligation  : Bool
  changesRecordOnly  : Bool
  requiresActor      : Bool
```

### effectOfClaimKind (asserted)

| ClaimKind | Effect signature | Derived severity |
|---|---|---|
| `risk_score` | `changesRecordOnly` | `.record_only` |
| `observation` | `changesRecordOnly` | `.record_only` |
| `visibility_constraint` | `changesVisibility` | `.constraining` |
| `authorization` | `changesAccess, requiresActor` | `.constraining` |
| `revocation` | `changesStanding, requiresActor` | `.binding` |
| `obligation_claim` | `changesObligation, requiresActor` | `.binding` |
| `enforcement_action` | `changesAccess, changesStanding, requiresActor` | `.force_bearing` |

Each claim-kind's signature is asserted **once** per claim-kind: a deliberate per-claim-kind operational declaration of what the claim does. Adding a new claim-kind requires declaring its signature.

### severityOfEffect (derived)

```lean
def severityOfEffect (e : EffectSignature) : EffectSeverity :=
  if e.changesAccess && e.changesStanding && e.requiresActor then .force_bearing
  else if e.changesStanding || e.changesObligation then .binding
  else if e.changesVisibility || e.changesAccess then .constraining
  else .record_only
```

The hierarchy is asserted once as the legitimate floor (defensible, finite, four levels):

```
record_only < constraining < binding < force_bearing
```

The claim-kind-to-severity mapping is *derived*, not hand-graded. Adding a new claim-kind requires declaring its effect signature (which is operational evidence), not its severity grade (which is mechanically projected). This stops the laundering route of "creative enum naming."

### Asserted vs derived split (the discipline)

| Asserted (defended once) | Derived (mechanical from asserted) |
|---|---|
| Effect axes (the 6 boolean fields) | `severityOfEffect : EffectSignature → EffectSeverity` |
| Severity hierarchy (4 levels, ordered) | `claimKindSeverity : ClaimKind → EffectSeverity` |
| `effectOfClaimKind` per-claim-kind table | Receipt's `severityDelta` extractor |
| Cascade order (Resource→Index→Modality→ClaimKind→Protocol) | Bridge ownership of any given transition |

### Receipts now carry effect evidence

`RefusalReceipt` augmented (2026-06-08) with two fields:

```lean
sourceEffect : EffectSignature
targetEffect : EffectSignature
```

Each bridge's refusal construction populates these via `Policies.effectOfClaimKind`. The bridge's *decision logic* is unchanged — it still consults only its declared narrow interface. The effect evidence is appended for receipt richness, not consulted for the refusal decision.

Cascade extractor `severityDelta : CascadeOutcome → Option (EffectSeverity × EffectSeverity)` reads (sourceSeverity, targetSeverity) from any refusal receipt.

### Effect-witness per specimen (Lean-verified)

| Specimen | Owner | source effect | target effect | severity delta |
|---|---|---|---|---|
| S1 | ResourceBridge | record_only (observation) | record_only (observation) | `(.record_only, .record_only)` — flat in severity; refusal is resource-shape, not effect-shape |
| S2 | ModalityBridge (demotion) | record_only | record_only | not applicable (demotion, not refusal) |
| S3 | IndexBridge | binding (revocation) | binding (revocation) | `(.binding, .binding)` — surface-scope violation, severity flat |
| S4 | ModalityBridge | constraining (authorization) | record_only (observation) | `(.constraining, .record_only)` — **severity DOWN, modality refusal anyway**; this is the useful negative observation: a refusal can be high-cascade-priority without target effect being force-bearing |
| S5 | ModalityBridge | record_only (risk_score) | force_bearing (enforcement_action) | `(.record_only, .force_bearing)` — top-tier escalation; ModalityBridge owns the cross-modality refusal |
| S6a | ClaimKindBridge | record_only (risk_score) | constraining (visibility_constraint) | `(.record_only, .constraining)` — force escalation that *previously laundered through advisory*; now caught by ClaimKindBridge with real severity evidence |
| S6b | ModalityBridge | constraining (visibility_constraint) | force_bearing (enforcement_action) | `(.constraining, .force_bearing)` — cross-tier escalation; ModalityBridge owns |

The S6a row is the **central result of the effect-grounding pass.** Pre-grounding, S6a's refusal was justified only by ruleName `claim_kind_transition_not_authorized` — a flat-table verdict. Post-grounding, the receipt carries operational evidence: the source effect is record-only; the target effect changes platform visibility; severity escalates from `.record_only` to `.constraining`. The refusal now cites *what doing this does*, not *what we named it*.

### Force-coupling question — status

**Reframed, not closed.** The original deferral framed the question as "does ClaimKind need a `forceOf` consult into Modality?" The effect-grounding pass replaces that question with:

> *Force* is not a separate axis; it is a *severity* read from the effect signature. The question is no longer "is there a force ledger" but "is there ever a claim-kind transition that the flat policy refuses but the effect-severity discipline would license?"

If a future specimen wants `risk_score → risk_score_v2` (hypothetical force-neutral refinement, both `.record_only` severity), the flat policy refuses it (claim-kinds differ) while the severity discipline would have no severity objection. That specimen would provide a useful instantiation and stress test for either:

- a richer policy that allows licensed equi-severity transitions, or
- a deeper question about whether equi-severity-but-different-claim-kind is meaningful at all.

Recorded as the next stress-test shape. The richer policy is currently parked by priority, not blocked on the specimen: a coherent specification or countermodel may be formalized in Scratch first and may lead later bridge code. Scratch cannot testify for production; adopting this contract would still require an explicit runtime mapping plus evidence or a refinement proof.

## Strongest claim available after flat-β

> *No specimen in this spike survived all declared bridge owners as a refusal candidate.* After the flat β patch, seven specimens (S1–S5, S6a, S6b) all produce either single-owner cascade outcomes or lawful demotions. The original OWNERSHIP-GAP at S6a has been captured by the flat ClaimKindBridge. No candidate irreducible result is proposed.

This is *not* a claim that admissibility is globally factorizable; it is a claim that *these seven specimens* factor under *these five bridges* with bounded interfaces. The flat policy is provisional pending a force-distinguishing specimen.

Future specimens may force:

- another OWNERSHIP-GAP (a column that changes but isn't yet owned)
- an interface widening (an existing bridge needs a richer dependency function)
- a bounded coupling (e.g., ClaimKindBridge must consult `forceOf` to distinguish legitimate from laundering transitions — claim-kind/modality force ledger)
- a candidate irreducible (no bounded owner can refuse, even with extension)

The first three are routine spike findings; the fourth would be a substantive result worth its own analysis.

## Candidate new columns / interfaces (named, outside this spike's scope)

Each of the following could be motivated by a coherent specification or by a specimen that the current interfaces cannot cleanly own. None is built in this spike; all are recorded for traceability:

- **freshnessKey** (ResourceBridge): exercised by a case where the *time-since-witness* matters for resource admissibility (e.g., stale witness becoming inadmissible).
- **budgetPolicy** (ResourceBridge): exercised by a case involving `affine_budgeted` or `counted_token` consumption.
- **temporalPolicy** (IndexBridge): exercised by a case where target's `Index.time` must be strictly later than source's.
- **actorScopePolicy** (IndexBridge): exercised by a case where actor identity is load-bearing for admissibility (cross-actor transitions).
- **authorizationEvidencePolicy** (ModalityBridge): exercised by a case where the `authorized` modality requires explicit evidence at the Index altitude. The current modality table is structural.
- **terminalStatePolicy** (ProtocolBridge): exercised by a case where terminal-state custody matters (e.g., enforcement-action records must be terminal-state-bound). ProtocolBridge is currently a stub.
- **Candidate fifth column: Provenance / Evidence-Origin** — currently encoded implicitly in `ClaimKind`; a case where two transitions agree on (resource, modality, claimKind, index) but differ on *evidence origin* would expose the need for a fifth column.

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
