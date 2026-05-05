# Boundary Composition Investigation

**Logged:** 2026-05-05 (late session, multi-model: claude-code + chatty + deepseek)
**Updated:** 2026-05-06 (AG audit completed)
**Status:** Audit completed 2026-05-06 (AG). Result: **Family-with-composition-lemmas (fork 2 of 3).** Boundary Calculus title not earned; working hypothesis is **Admissibility Boundary Family with composition lemmas.** No P28 draft, no namespace promotion, no new doctrine.
**Lives near:** P28 candidate territory (synthesis question for the P22→P27 spine).

---

## What this is

A handle for the move from **formalization-as-validation** to **formalization-as-investigation** on the admissibility kernel. Triggered by the P25 citation-debt audit (2026-05-05), which surfaced the admissibility-binding seam between P25's substitution-forcing theorem and `AuthorizedStep` ("stale basis cannot bind at mutation layer"). That seam plus the P22→P27 spine raised the synthesis question: do the admissibility boundaries actually *compose*, or are they only a family resemblance?

This note exists to keep the question crisp for tomorrow without re-deriving it from the conversation.

---

## The methodological pivot

**Before:** prose discovers claim → Lean validates / audits. Bottom-up. The Lean kernel records what's already known; sorries get classified per the existing discipline (proof / vocabulary-deficient / placeholder).

**Now (proposed):** named target proposes structure → Lean investigates whether the structure exists. Top-down. Success = a composition theorem with sharp content. Failure = a null result with *also* sharp content (here are the obstructions; the boundaries do not compose in this way).

The discipline the new mode requires that the old one didn't:

1. **State the target before searching.** Theorem statements written explicitly enough to fail honestly.
2. **Accept null results as content.** "Family, not Calculus" is publishable.
3. **Don't redefine terms mid-search.** Primitive-ratification gate applies harder in investigative mode than in validation mode.

---

## The named object

**Working title (provisional):** Boundary Calculus / `BoundaryCompositionExperiments`

**Slogan (load-bearing):**

> A system's ability to execute is not evidence of its authority to act.

**The research question, in its sharpest form:**

> Can two action-indexed boundary theorems be composed to produce a third action-indexed boundary theorem about a composite action, without redefining either input?
>
> If yes, repeatedly: that's a calculus.
> If only sometimes and conditionally: that's a Family with composition lemmas.
> If never cleanly: that's "related refusals, not an algebra."

**Three-fork outcome map:**

- **Composition laws emerge cleanly:** P28 honestly = "Boundary Calculus." Title earns itself.
- **Composition partially works with obstructions:** P28 = "Admissibility Boundary Family," with a strong null-result section.
- **No meaningful composition:** finding is "these are related refusals, not an algebra." Still publishable; prevents synthesis fraud.

---

## The discipline package (DeepSeek + chatty + claude lint)

### Action-indexing

**Every theorem must be indexed by the action under scrutiny.** No free-floating invalidity. No system-wide taint. No "one rotten receipt poisons the universe." DeepSeek caught two specific failures:

- The boundary theorem was globally poisonous (existence of *some* inadmissible boundary anywhere couldn't deny authorization for *any* composite action — the bad boundary has to be one *the action actually crosses*).
- The receipt theorem forgot to connect the derivation to the action (`¬ Authorized a` for arbitrary `a` from a bad receipt-derived derivation `d` is absurd; the derivation has to target the specific action, or one wants `¬ authorized_by d a`, not `¬ authorized a`).

**Structural consequence:** composition is stated at the **action level**, not on free-floating boundary objects. Boundary Calculus is a calculus of *action composition under boundary constraints*, not a calculus of boundary objects in the abstract. Latter is universal-solvent territory; former has teeth.

### Locked-ish definitions before the search

Required commitments (chatty's six + one):

1. What counts as a boundary?
2. What counts as crossing?
3. What counts as binding?
4. What counts as authorization?
5. What counts as composition?
6. What failure is allowed to block the whole composite?
7. **What counts as the same boundary twice vs two different boundaries?** (individuation principle — without this, "do they compose?" can be silently answered by changing what counts as separate)

If "boundary" gets quietly broadened mid-search to make a theorem go through, the result is post-hoc rather than discovery — fake calculus / formal puppet show. The locked definitions are the protection.

---

## First deliverable: audit, not theorem

**The investigative branch's first commit is the audit, not a theorem.** Before stating new targets, inspect what the existing kernel already commits to about composition.

Live-audit-over-cached-roadmap discipline: verify against actual repo state, not against memory of what the roadmap said weeks ago.

**Existing kernel objects to audit** (under `~/git/lean/LeanProofs/Admissibility/`):

- `Authority` module
- `StateTransition` module (mutation algebra, `StepAllowed`)
- `Derivation` module
- `Execution` module
- `Corrective` module (corrective monotonicity; corrective steps as down-edges; re-entry as replacement)
- `AuthorizedStep` (stale basis cannot bind at mutation layer)
- `classify : Step → StepClassification` (the enforcement surface)

**Audit columns (per object):**

| Column | Question |
|---|---|
| Object | Name of theorem / definition / module |
| Boundary kind involved | Authority / StateTransition / Derivation / Execution / Corrective / other |
| What composes? | What does this theorem combine? |
| What blocks composition? | Under what conditions does it fail? |
| Action-indexed? | Is the theorem indexed by the action under scrutiny, or free-floating? |
| Derivation-indexed? | Is the conclusion `¬ authorized a` or `¬ authorized_by d a`? |
| Global-state-indexed? | Does it reach into ambient state? |
| Already a composition theorem? | Or just a single-step property? |
| **Individuation load-bearing?** | If you collapsed the involved boundaries into a single predicate, would the theorem still go through? (Yes = decoration; No = kernel committed to that split) |
| Could this generalize? | Without broadening definitions? |

The "individuation load-bearing" column is the operational form of question 7 above.

---

## Candidate theorem shapes (for after the audit)

These are sketches, not commitments. Stated to mark the territory; the audit may show some are already proved, others are vocabulary-deficient.

**1. Denial composition (boundary violation blocks authorization, action-indexed):**

> **Status (2026-05-06 AG audit): Stateable but unwarranted under current kernel.** Abstract store ops lack behavioral commitments needed to prove this as stated. Do **not** strengthen the kernel mid-search to make it go through. Whether to develop the missing behavioral commitments deliberately, as their own object, is a separate decision — not a calculus-rescue move.

```lean
theorem boundary_violation_blocks_authorization
  (a : Action) (b : Boundary) :
  crosses_boundary a b →
  required_for_action a b →
  ¬ admissible_crossing a b →
  ¬ authorized a
```

**2. Receipt non-laundering (action-indexed, derivation-indexed):**

```lean
theorem receipt_does_not_authorize_without_basis
  (a : Action) (r : Receipt) (d : Derivation) :
  valid_receipt r →
  uses_receipt d r →
  derives_authorization_for d a →
  ¬ authorization_basis d →
  ¬ authorized_by d a
```

Note: conclusion is `¬ authorized_by d a`, not `¬ authorized a` — another derivation could still authorize `a`. (DeepSeek catch.)

**3. TTL / revocation breaks composition:** likely already substantially in `AuthorizedStep`.

**4. Kind separation:** policy / evidence / gap / receipt / corrective stores do not collapse into each other under transition. Likely partially in the five-sibling-module decomposition.

**5. Possible null result:** boundaries may not form a lattice or clean algebra because authority, evidence, time, scope, execution are different *kinds*, not elements of one neat order. → Family, not Calculus. **(Effectively the audited outcome; see Status.)**

---

## Audit extension (2026-05-06): candidates #2–#5

Same commitments check as #1, applied to the remaining candidates. **Audit-extension only — no theorem changes, no kernel strengthening, no calculus rescue.**

### Compact verdicts

| # | Candidate | Stateable? | Warrantable? | Missing semantic commitment | New vocabulary needed | Family / Calculus / null |
|---|---|---|---|---|---|---|
| 2 | Receipt non-laundering | Weak form: yes (already proved). Strong form (with derivation-trace): no | Weak: yes. Strong: no | For strong form: derivation provenance + behavioral law on `appendEvidence` + receipt→basis bridge | Yes — `uses_receipt` predicate, derivation-trace object | Family-shape after vocabulary additions; weak form already a composition lemma |
| 3 | TTL / revocation breaks composition | **Yes (static case)** / partial (TTL aspect) | **Yes (static)** — already proved | None for static; temporal model for TTL | None for static; clock + expiry-horizon for TTL | **Family with composition lemma — already partially in kernel** |
| 4 | Kind separation (store partitioning) | **Yes** | **Yes** — mechanical extensions of existing trapdoors | None (purely structural) | None | **Family with mechanical projection lemmas — Phase 0 territory** |
| 5 | Possible null result (no clean algebra) | Yes (as meta-claim); partial as Lean theorem | Not under current axioms | Behavioral laws on `applyUpdate` / `appendGap` / `appendRevocation` / `appendEvidence` | Definitions / axioms on the abstract store ops | **Empirically the kernel's current shape; recorded as `sorry` in `Corrective.corrective_then_forward_is_not_monotone`** |

### Per-candidate detail

**#2 Receipt non-laundering.** The kernel has `Receipt`, `appendEvidence`, `EvidenceStore`, and `BasisDerivation` with the `revoked_never_admissible` obligation.

A *weak* version of #2 — "if the basis verdict is not `admissibleBasis`, the action is not authorized" — is *already proved* as the contrapositive of `Authority.authorized_iff_all_green`, projecting through `Derivation.decide_authorized_requires_all_green` to `decideAuthority`. That covers the "no admissible basis ⇒ no authorization" content.

The *strong* version as originally drafted (with a derivation `d` that uses receipt `r`) requires a derivation-trace object the kernel does not have. `BasisDerivation` is a *strategy* structure (function + proof obligations), not a *derivation-with-provenance*. Stating the strong form requires a new `uses_receipt` predicate plus a behavioral law tying receipt-presence-in-`EvidenceStore` to the `BasisVerdict` a concrete `BasisDerivation` returns. Both are speculative; do not add.

Verdict: weak form is already a Family composition lemma; strong form requires new vocabulary at the same layer as #1, plus an additional missing concept (derivation provenance).

**#3 TTL / revocation breaks composition.** **Already partially proved.** Static revocation is captured by:

- `Derivation.revoked_basis_never_authorized` — `BasisDerivation.basisRevoked` projects through the verdict gate.
- `Execution.revoked_basis_cannot_be_authorized_step` — same projection lifted through the `AuthorizedStep` bridge ("stale basis cannot bind at execution layer").

These are vertical composition lemmas. The TTL aspect — *time-based* revocation — is not yet in the kernel; revocation is currently boolean (`basisRevoked : GovState → AuthorityClaim → Prop`), not temporal. Adding TTL requires a clock / expiry-horizon model and is its own object, not a calculus rescue.

Verdict: composition-lemma status confirmed for static revocation; TTL extension is a separate future investigation requiring temporal vocabulary.

**#4 Kind separation.** **Stateable and warrantable mechanically.** The four-store partition is the existing structural commitment. The PolicyStore-isolation case is already proved by `record_receipt_does_not_amend_policy`, `declare_policy_gap_does_not_amend_policy`, `record_revocation_does_not_amend_policy` (raw layer) and their `executeAuthorizedStep`-lifted siblings (Execution layer). Symmetric statements for the other three stores ("recordReceipt does not mutate GapStore", "declarePolicyGap does not mutate EvidenceStore", etc.) are pattern-match-and-`rfl` proofs in the same shape. These are Phase 0 projection lemmas in their cleanest form — purely structural, no behavioral commitments needed.

Verdict: cleanest Family-with-composition-lemma candidate; lemmas are already half-present in PolicyStore-shape and the other stores follow mechanically.

**#5 Possible null result.** Empirically the kernel's current state. The recorded `sorry` at `Corrective.corrective_then_forward_is_not_monotone` (lines 280-284) names the precise vocabulary deficit: under the worst-case axiomatization where the abstract store ops are identity, every Step is state-preserving and the existential is *provably FALSE*. Until a behavioral law on the abstract store ops is committed, the kernel is consistent with both the existential and its negation. The kernel docstring itself says: *"This `sorry` is a recorded investigative null, not a deferred proof to be eliminated by axiomatizing `applyUpdate` here."*

That is Family-not-Calculus visible in the kernel's own source. The AG audit verdict is what the kernel already documents.

Verdict: confirmed empirically; the null-shape is the current truth-value-assignment under the kernel's current commitments.

### What the audit extension does *not* claim

- That candidates #2 and #5 are unprovable forever. They are unprovable *under current commitments*. Whether to develop the missing commitments deliberately, as their own object, is a separate decision.
- That candidate #3 (static revocation) is "the calculus." It is one composition lemma in a Family with composition lemmas. Title still not earned.
- That candidate #4's mechanical extensions should be added now. They are isolated and mechanical, but adding them was outside this audit's scope. See Phase 0 inventory below for landing locations.

---

## Harvestables (post-audit, 2026-05-06)

From the AG audit and the over-architectural overnight roadmap, two pieces are worth keeping forward; the rest is dropped.

- **Phase 0 projection lemmas.** Composition results that hold by *projection* between boundaries — a property of one boundary projects through a morphism onto a related property of another. Likely the cheapest place where composition lemmas can land cleanly without strengthening the kernel.
- **Vertical / horizontal composition distinction.** Sequential composition (one action after another) vs parallel composition (actions composed across the same temporal slice). Standard categorical distinction; worth keeping as the framing language for any composition lemma the warranted theorems eventually carry.

Everything else from the overnight roadmap is over-architectural for current kernel state and dropped. No `BoundaryCompositionExperiments` namespace until the kernel earns it.

---

## Phase 0 projection lemma inventory (2026-05-06)

Phase 0 projection lemmas: composition results that hold by projection between boundaries, without strengthening kernel commitments. Two compositional axes, per the harvestable distinction:

- **Vertical** (layer-to-layer): Authority ← Derivation ← Execution ← Corrective.
- **Horizontal** (within-layer, sequential): `applySteps`, transitivity of `WeaklyLessPermissive`.

### Existing projection lemmas already in the kernel

**Vertical:**
- `Derivation.decide_authorized_requires_all_green` — component verdicts → `AuthorityVerdict`. Direct corollary of `Authority.authorized_iff_all_green`; the bridge layer's load-bearing composition theorem.
- `Derivation.revoked_basis_never_authorized` — `BasisDerivation.basisRevoked` projects through the verdict gate.
- `Execution.revoked_basis_cannot_be_authorized_step` — same projection, lifted through the `AuthorizedStep` bridge.
- `Execution.authorized_record_receipt_does_not_amend_policy` and three siblings — structural trapdoor invariants from StateTransition lifted through `StepAllowed` + `AuthorizedStep`.
- `Execution.authorized_amend_policy_targets_policy_store` — positive witness lifted through the bridge.

**Horizontal:**
- `Corrective.weakly_less_permissive_trans` — transitivity of the authorized-set preorder.
- `Corrective.corrective_sequence_monotone` — single-step monotonicity composes into list-step monotonicity by induction.
- `Corrective.recovery_monotone` — bundled-environment projection through the recovery applier.

The kernel is already meaningfully populated with projection lemmas in both axes. The Family verdict is supported by what's there.

### Where new Phase 0 lemmas would land (not added)

**Mechanical and isolated (candidate #4 territory):**

Symmetric kind-separation trapdoors. For each of the four stores, three trapdoor theorems analogous to the existing PolicyStore-isolation set. Twelve theorems total in raw + lifted forms; pattern-match-and-`rfl` in every case. Landing sites:

- `LeanProofs/Admissibility/StateTransition.lean` — raw layer (analogous to existing `record_receipt_does_not_amend_policy` etc.).
- `LeanProofs/Admissibility/Execution.lean` — lifted layer (analogous to existing `authorized_record_receipt_does_not_amend_policy` etc.).

**Mechanical-but-derivative (Derivation-layer symmetrics):**

`Authority.lean` has five "no-* never authorized" theorems (`no_basis_never_authorized`, `advisory_basis_never_authorized`, `incomparable_precedence_never_authorized`, `conflicting_precedence_never_authorized`, `no_standing_never_authorized`). Currently only the `revoked_basis_never_authorized` analogue is lifted into `Derivation.lean`. Symmetric forms — e.g. `incomparable_precedence_never_authorized_in_decide`, `conflicting_precedence_never_authorized_in_decide`, `no_standing_never_authorized_in_decide` — would project the existing Authority-layer no-* theorems through `decideAuthority`, paralleling the revocation case. Each is a one-line proof: `unfold decideAuthority; exact <Authority-layer theorem>`. Landing site: `LeanProofs/Admissibility/Derivation.lean`.

**Not Phase 0 (out of scope):**

- TTL-extended revocation (candidate #3 TTL aspect) — requires temporal vocabulary; not mechanical, not isolated.
- Derivation-trace / receipt-provenance (candidate #2 strong form) — requires new structural concept.
- Behavioral laws on abstract store ops (candidate #5 enabler) — strengthens kernel commitments; explicitly out of audit scope.

### Decision

The audit-extension does not propose adding any Phase 0 lemmas in this pass. The inventory exists so the next move (whoever takes it, whenever) can choose between:

a) Adding the mechanical symmetrics as a one-shot Family fold-in pass (twelve store-isolation theorems + three Derivation-layer no-* lifts ≈ fifteen one-line proofs).
b) Deferring and treating them as a separate "Family fold-in" investigation, possibly tied to a specific paper need.
c) Leaving the kernel as-is and treating the existing projection lemmas as sufficient evidence for the Family verdict.

Each is honest. None rescues the calculus. The Family verdict — the kernel proves Family-with-composition-lemmas, not Calculus — is already supported by what's in the kernel without any of (a)/(b)/(c).

---

## Three promotion errors (the compression target if synthesis lands)

If the synthesis paper happens, the operator vocabulary should compress to one slogan and a small number of promotion errors. Chatty's compressed list (after self-correcting from a 14-operator overshoot):

1. **Evidence promoted to authority.** "We observed something, therefore we may act."
2. **Proxy promoted to target.** "We can measure V′, therefore we are governing V." (P25 case.)
3. **Mechanism promoted to legitimacy.** "The system can execute the transition, therefore the transition is authorized." (`AuthorizedStep` case.)

Everything else — testify, interpret, recommend, authorize, act, bind, revalidate, revoke — stays *background grammar*, not minted primitives. Adding more requires the ratification gate.

---

## What this is NOT

- **NOT** an authorization to draft P28. The audit comes first; the title comes last; the theorem statements come in between.
- **NOT** a license to mint operators. Every primitive that gets added must replace more than it adds.
- **NOT** a framework-launch. Books + Zenodo is the venue; "named admissibility discipline" is a temptation, not a goal.
- **NOT** event-triggered control adjacent. That neighborhood belongs to P22 actuation / Δt timing, not P25 or the synthesis question. Recorded here to prevent re-confusion.

---

## The case atlas (separate, parallel object)

Mentioned for completeness; not part of the Lean investigation. Could be book / Substack / appendix-shaped, not necessarily a preprint. Format:

> Many cases, one grammar (the three promotion errors), no new theorem unless cases break the grammar. **Includes contrast cases** — failures that look adjacent but aren't promotion errors — to demonstrate the framework's edges. Without contrast cases the atlas is a confirmation parade.

Each case answers: What was promoted? Into what authority? What boundary failed? What consequence followed? What refusal rule would have blocked it?

The atlas is the anti-universal-solvent companion to the synthesis paper. It can exist whether or not the calculus exists.

---

## Original "tomorrow's first move" (retired 2026-05-06)

This plan was the prospective audit protocol on 2026-05-05. The AG audit completed it overnight; result is recorded in the Status header at top and detailed in the "Audit extension" section. Preserved here as history of the original investigative move.

1. Open `~/git/lean/`.
2. Walk the five admissibility modules + `AuthorizedStep` + `classify`.
3. Fill the audit table per existing object.
4. Mark which objects are already composition theorems vs single-step properties.
5. Mark which boundary individuations are load-bearing vs cosmetic.
6. From the audit, decide which candidate theorems are already (partially) proved, which are vocabulary-deficient, and which are next-target-shaped.
7. *Then* state targets in `BoundaryCompositionExperiments`.

The audit is not a theorem. The audit is the precondition for honest theorem-stating.

## Current state (2026-05-06)

- AG audit complete; verdict **Family-with-composition-lemmas** (fork 2 of 3).
- Audit extension to candidates #2–#5 complete; detailed in "Audit extension" section above.
- Phase 0 projection lemma inventory documented; no new theorems added.
- No P28 draft. No `BoundaryCompositionExperiments` namespace promotion. No new doctrine. Kernel earns the calculus or it doesn't.
- Open separate decisions, none made: (a) develop missing behavioral commitments on store ops as their own object; (b) add mechanical Phase 0 symmetrics as a one-shot Family fold-in; (c) leave kernel as-is and treat existing projection lemmas as sufficient evidence for the Family verdict.

---

## Pointers

- P25 paper: `preprint/25-epistemic-border-control/epistemic_border_control.md`
- P25 citation-debt note: `preprint/25-epistemic-border-control/NOTES.md` (last section)
- Lean repo: `~/git/lean/LeanProofs/Admissibility/`
- Project memory pointers: `project-authority-kernel.md`, `project-admissibility-family-structure.md`, `project-paper25-candidate.md`
