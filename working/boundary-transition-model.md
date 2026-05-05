# Boundary Transition Model (working note)

**Logged:** 2026-05-06
**Status:** Design / investigation only. Not doctrine, not a P28 draft, not authorization to add code.
**Sibling:** `working/boundary-composition-investigation.md` (audit record + custody decisions).
**Lives near:** P28 candidate territory; specifies the candidate object that would have to exist before "Boundary Calculus" could be earned.

---

## 1. Non-ratification header

Boundary Calculus remains provisional. The current Lean kernel supports **Family-with-composition-lemmas** (verified by AG audit 2026-05-06; recorded in `boundary-composition-investigation.md`). The title "Boundary Calculus" is **not earned**. This note defines what would need to be true for the title to earn itself.

Nothing in this note ratifies a primitive, names a kernel addition, or commits to a P28 draft. The candidate fields, moves, and theorem-shapes recorded below are *handles for review*, not authorization to build.

### Reframe

Earlier framing treated the five-sibling-module decomposition (Authority / StateTransition / Derivation / Execution / Corrective) as **boundaries-as-objects** — static layers being crossed. This note adopts the reframe:

> Boundary Calculus, if it exists, is not the study of boundaries as objects. It is the study of **admissibility changes induced by boundary transitions**.

The reframe converges with action-indexing discipline. An action in the kernel is a `Step`; a `Step` is already an *executable* transition Γ → Γ' via `applyStep`. The candidate transition object is broader: it includes **contextual transitions** (environment mutation, clock advancement, scope rebinding, cohort change) that the Step inductive does not realize. Step is one class of admissibility transitions, not the full class. The reframe makes the transition — in this broader sense — the primary object, not the layer.

This is a *conceptual* shift, not a kernel change. The kernel already has the transition vocabulary; the reframe just renames what we are studying.

---

## 2. Mapping to existing kernel

| Concept | Kernel realization | Reality of mapping |
|---|---|---|
| Γ (state) | `GovState` (partitioned: PolicyStore / EvidenceStore / GapStore / RevocationStore) | **Real** |
| B : Γ → Γ' (executable transition) | `applyStep : GovState → Step → GovState` | **Partial.** Step realizes the executable / Step-shaped class. Contextual transitions (env mutation, clock advancement, scope rebinding, cohort change) are not Step-realizable. See "Executable vs contextual transitions" below. |
| Sequenced transition | `applySteps : GovState → List Step → GovState` | **Real** |
| Adm(action, Γ) — verdict side | `decideAuthority env Γ actor (claimForStep ...) = authorized` | **Real** (per-claim) |
| Adm(action, Γ) — witness side | Existence of `AuthorizedStep env Γ actor` with `.step = s` | **Real** (per-step, action-indexed) |
| Non-laundering / no-new-authorization under B | `WeaklyLessPermissive env Γ' Γ` (corrective direction only) | **Partial.** What is proved is Adm(a, Γ′) → Adm(a, Γ): the post-state has no authorizations the pre-state lacked. This is the *no-new-authorization* direction. *Survival* in the natural sense (Adm(a, Γ) → Adm(a, Γ′)) is the **opposite** direction and is not a corollary; the survival direction is the recorded null. |
| Boundary as typed object | (none — implicit in Step constructors) | **Speculative.** Boundary individuation is not first-class. |
| Carried / discarded authority | (none) | **Speculative.** `BasisDerivation.basisRevoked` names invalidity but not "this transition discards basis B." |
| Carried / discarded evidence | (none) | **Speculative.** Receipts go into EvidenceStore via `appendEvidence` (axiom); no notion of "discarded evidence." |
| Required revalidation | (none — implicit in re-entry doctrine) | **Speculative.** `Corrective.lean` describes re-entry as *replacement*, not revalidation. |
| Affected scope | (none) | **Speculative.** No `Scope` type. |
| Consequence horizon | `Receipt.durability` + `H : Obligation → Horizon` (P27 skeleton) | **Partial.** Exists in P27; not connected to admissibility-family kernel. |
| Mutation / effect witness | `StepAllowed` (permission) + structural trapdoors | **Partial.** Permission-witness is real; behavioral effect-witness (what the mutation does to store contents) is missing. |
| Recorded investigative null | `corrective_then_forward_is_not_monotone` (Corrective.lean L280-284) | **Real**, with structured category marker. |

The mapping is *substantially real* on the state / transition / verdict / witness axis. It is *speculative* on the boundary-individuation, scope, temporal, and effect-witness axes.

### Step as descriptor, applyStep as interpretation

`Step` is a *descriptor* — a data type whose constructors name intended mutations. `applyStep : GovState → Step → GovState` is the *interpretation* function that turns a Step descriptor into a Γ → Γ' transition. `applySteps` composes Step *descriptors* (a list), not arbitrary transition functions; the composed transition is the iterated interpretation, not a free composition over `GovState → GovState`.

This matters for any future calculus that needs to distinguish, e.g., *revalidation* from *fresh establishment*. The current Step inductive (`recordReceipt | declarePolicyGap | recordRevocation | amendPolicy`) carries no path information: an `amendPolicy p` Step looks the same whether it is establishing a fresh basis or re-establishing a previously revoked one. Path-sensitive semantics — distinguishing transitions by what came before — would require either richer descriptors or a path-tracking layer over `applySteps`. Neither is in the kernel.

### Executable vs contextual transitions

An *executable* transition is one realizable by the kernel's mutation algebra — a `Step` applied via `applyStep`. The kernel's Family-with-composition-lemmas verdict applies to this class.

A *contextual* (or *admissibility*) transition is broader — any change to the conditions under which authorization holds. Four sub-classes, none currently Step-realizable:

- **Environment mutation.** Replacing a `BasisDerivation` (or any field of `DerivationEnv`) changes verdict computation without touching `GovState`. `Corrective.lean` §5 open question explicitly flags this as a separate laundering vector — `WeaklyLessPermissive` fixes `env`, so env-mutation is out of its current scope.
- **Clock advancement.** TTL-driven basis expiry: a basis admissible at time `t` may be inadmissible at `t' > t` without any Step having been applied. Requires a temporal model not in the kernel; partial scaffolding exists in P27 (`Receipt.durability`, `Horizon`) but is not connected to the admissibility-family kernel.
- **Scope rebinding.** A claim evaluated under a different scope `S'` than its original scope `S` may produce a different verdict. No `Scope` type yet; `AuthorityClaim` is opaque.
- **Cohort change.** Heterogeneous-witness cases (P25 §8): the witness population changes, affecting which claims are observable. The single-agent kernel does not model cohort.

The candidate Boundary Calculus would have to reason about both classes (executable + contextual). The kernel currently reasons about the executable class with `env` fixed and no temporal / scope / cohort vocabulary.

### Composition spaces are not unified

Executable and contextual transitions currently live in **different composition spaces**:

- **Step composition** acts over `GovState` — two Steps compose via `applySteps`, with both interpreted as `applyStep`-functions on the same state space.
- **Environment mutation** acts over `DerivationEnv` — two env-changes compose by sequential field replacement; `WeaklyLessPermissive` does not range over this dimension.
- **Clock advancement, scope rebinding, cohort change** require vocabulary not in the kernel and have no current composition.

A future calculus must either (a) define a *combined context state* — Γ + env + clock + scope + cohort — with composition rules over the product, or (b) prove composition rules per transition class with explicit cross-class interaction theorems. Neither route is cheap; the choice is structural and has to be made before any calculus claim is honest about what it composes over.

---

## 3. Candidate transition fields

A boundary transition, if eventually formalized, would need to declare or accommodate:

- **Source state** Γ — currently `GovState`, structurally adequate.
- **Target state** Γ' — currently `applyStep Γ s`, structurally adequate.
- **Carried authority** — what authority claims remain admissible under the same basis after the transition.
- **Discarded authority** — what authority claims become inadmissible (revoked, expired, scope-narrowed).
- **Carried evidence** — what evidence remains in EvidenceStore *and* remains tied to admissible bases.
- **Discarded evidence** — what evidence is invalidated, expired, or made inaccessible.
- **Required revalidation** — what bases must be re-established before claims dependent on them can re-authorize.
- **Affected scope** — what scope of claims the transition touches (vs leaves untouched).
- **Consequence horizon** — over what time / step-count window the transition's effects are durable.
- **Mutation / effect witness** — proof that the transition actually does what its classification says it does (e.g., `recordRevocation` actually appends to RevocationStore, not just permits the call).

Mark these as **candidate fields**, not ratified primitives. None should be promoted to a kernel structure without (a) a concrete forcing case where the field is load-bearing for a theorem, and (b) the primitive-ratification gate (generator / kind / seven-supporting tests) being run.

The current kernel realizes a *projection* of these fields: `Step` constructor + `StepAllowed` proof + `classify : Step → StepClassification`. That projection is enough for the Family verdict; it is not enough for a calculus over transitions.

---

## 4. Candidate moves

Six operations on transitions. Described operationally; failure modes named; current Lean expressibility noted.

**Restriction.** A transition that narrows admissibility — strictly removes claims from the authorized set without adding any.
- *Operationally:* revoke a basis, declare a gap, narrow scope.
- *What can go wrong:* over-revocation; scope collapse; restriction in a way that breaks downstream reasoning that depended on the dropped claims.
- *Lean expressibility:* **real** for the corrective Step subset (`recordRevocation`, `declarePolicyGap`); proved by `corrective_monotone` under the `CorrectiveMonotone env` obligation. Sequence form: `corrective_sequence_monotone`.

**Expansion.** A transition that broadens admissibility — adds claims to the authorized set.
- *Operationally:* amend policy to admit a previously inadmissible class of action; install new standing.
- *What can go wrong:* unauthorized expansion (laundering); expansion in violation of obligations; scope leakage; the "we now permit this" silently treating prior-prohibited acts as retroactively permitted.
- *Lean expressibility:* `amendPolicy` is the only forward Step constructor. **No preservation theorem** is currently proved; expansion's well-behavedness is the territory the recorded null points at.

**Projection.** Reading off or restricting attention to a sub-state — e.g., the PolicyStore-only projection of a transition.
- *Operationally:* prove that a transition leaves a particular component of state unchanged; restrict a verdict to its component dimensions.
- *What can go wrong:* projection that hides a relevant change; projection that loses dimensional content needed for downstream verdict.
- *Lean expressibility:* **real** for individual stores via the trapdoor invariants (`record_receipt_does_not_amend_policy`, etc.) and `executeAuthorizedStep`-lifted siblings. The verdict-component projection (`Authority.authorized_iff_all_green`) is the same shape on the verdict layer.

**Revocation / invalidation.** Marking a basis as revoked or invalid for future verdict computation.
- *Operationally:* append to RevocationStore; flip `basisRevoked` for a claim.
- *What can go wrong:* revocation that doesn't propagate to dependent claims; ghost-revocation (recorded but not effective in derivation); revocation laundering (revoke then re-derive the same claim under nominally new basis).
- *Lean expressibility:* **real** via `recordRevocation` Step + `BasisDerivation.basisRevoked` predicate + `revoked_never_admissible` obligation. Connected through `decideAuthority` to verdict consequences via `revoked_basis_never_authorized` and to execution consequences via `revoked_basis_cannot_be_authorized_step`.

**Revalidation.** Re-establishing a previously revoked or absent basis.
- *Operationally:* establishment of a fresh basis K' that supersedes a revoked K.
- *What can go wrong:* treating revalidation as evidence the original basis was always valid ("we revalidated therefore old K is fine"); blurring replacement into restoration.
- *Lean expressibility:* **speculative as a single move.** Current `Corrective.lean` doctrine treats re-entry as a *sequence* (corrective Step that marks revocation, then forward Step that establishes K' through ordinary admissibility). Revalidation as a first-class transition is not in the kernel and would require careful handling to prevent laundering.

**Composition.** Sequencing of transitions.
- *Operationally:* `applySteps Γ [s₁, s₂, …]`.
- *What can go wrong:* silent re-entry (forward-after-corrective producing apparent recovery without the doctrinally-required fresh basis); composition that is verdict-monotone for individual claims but breaks at the cohort level.
- *Lean expressibility:* **real** via `applySteps` + transitivity of `WeaklyLessPermissive`. All-corrective composition is well-behaved (`corrective_sequence_monotone`); mixed-class composition is the recorded null.

The consistent shape across all six moves: **corrective-side composition is well-handled, forward-side composition is undeveloped, mixed-class composition is the open question.**

---

## 5. Survival / non-survival — candidate rules

### Candidate invariant — necessity, not sufficiency

> **Loss of basis blocks survival; preserved basis does not imply survival.**

Two clauses, asymmetric:

1. **Loss of basis blocks survival.** Any authorization that depended on basis B at Γ does not survive a transition that revokes or invalidates B at Γ'. Basis preservation is *necessary* for survival. This direction is partially proved by:
   - `revoked_basis_never_authorized` (Derivation layer) — if basis is revoked at Γ', no authorization holds at Γ' regardless of pre-state.
   - `revoked_basis_cannot_be_authorized_step` (Execution layer) — same, lifted through `AuthorizedStep`.

2. **Basis preservation is not sufficient for survival.** Even if basis B is preserved across Γ → Γ', survival is not guaranteed. The *verdict bridge* (basis → verdict computation), *standing* (actor's standing for the claim), *scope* (claim evaluated in matching scope), *temporal conditions* (TTL not expired), and *consequence horizon* must also survive. Failure of any single condition can block survival even when basis is preserved.

Adjacent but distinct: `corrective_no_authority_laundering` (Corrective layer) proves *no-laundering* — corrective steps do not *create* authorization where none existed. This is the opposite-direction theorem (post-state has no new authorizations), not a survival theorem (pre-state authorizations carry forward). They are related by their shared kernel object (`WeaklyLessPermissive`) but make opposite-direction claims.

The *positive* form of clause 2's contrapositive ("if all five conditions are preserved, then survival") is **not proved** and would require behavioral laws on store ops + concrete `BasisDerivation` + temporal vocabulary + scope vocabulary + cohort vocabulary to even state, let alone prove. Each missing piece per §6.

### Candidate theorem-shapes (do not formalize yet)

1. **Authorization does not generally commute with boundary transition.**
   Stated as `corrective_then_forward_is_not_monotone` (Corrective.lean L280-284) — recorded investigative null. Stateable in current vocabulary; truth value undecided under current commitments.

2. **Projection is admissible only if omitted dimensions are irrelevant to the verdict.**
   Trapdoor-shape: a transition that doesn't touch a verdict dimension cannot change the verdict's value on that dimension. Partially expressed by existing trapdoor invariants and `authorized_iff_all_green`.

3. **Composed boundary transitions preserve admissibility only when each transition preserves the basis required by the next.**
   Vertical slice (Authority → Derivation → Execution): partially proved via the revoked-basis chains. Horizontal slice (Step sequences): proved for all-corrective; open for mixed-class.

These are **shapes**, not theorems. None should be added to the kernel without (a) the missing commitments listed in §6 being addressed deliberately, and (b) ratification through the existing primitive gate.

---

## Basis-indexed admissibility (candidate refinement)

DeepSeek / chatty refinement of how the admissibility judgment should be indexed. Records pressure for a sharper indexing than `Adm(a, Γ)`. Candidate, non-binding; does not earn Boundary Calculus.

### Core shift

The current note (and the kernel) treats admissibility as state-indexed: `Adm(a, Γ)`. This is too coarse. The candidate refinement is **basis-indexed admissibility**:

> Γ ⊢_κ Adm_r(a)

Read: action `a` is admissible in state `Γ`, for role / effect `r`, on basis `κ`.

The shift: from "is `a` admissible in Γ?" to "*on what basis* is `a` admissible in Γ for *what role*?" Bases become first-class; verdicts are the output of basis-evaluation, not the only object.

### Why this matters: the lost-but-not-forbidden case

Bases can be lost or degraded without making the action permanently forbidden. Loss of an old basis means the *old authorization cannot be inherited* — but `Γ'` may still derive `Adm_r(a)` by producing a fresh `κ_new` valid in `Γ'`.

This distinction is invisible in state-indexed `Adm(a, Γ)`. The state-indexed reading conflates:

- "the basis that authorized `a` in Γ does not survive into Γ'" (non-inheritance), and
- "no basis authorizes `a` in Γ'" (prohibition).

These are not the same. Basis-indexing makes the distinction visible.

### Transport as relation, not function

Treat basis transport as a relation:

> B ⊢ κ ↦ κ'

Read: under transition B, basis κ may be transported to basis κ'. Do **not** assume transport is total, single-valued, or authority-preserving. Transport may be:

- **undefined** — κ does not transport at all.
- **one-to-one** — κ ↦ unique κ'.
- **many-to-one** — multiple bases collapse to one.
- **one-to-many** — κ may transport to several κ' (non-deterministic).
- **degraded** — κ' weaker than κ in role.
- **narrowed** — κ' scope strictly contained in κ scope.
- **role / kind changing** — κ transports as a different basis kind in Γ'.
- **advisory-only after transition** — κ' may witness but not authorize.

The current kernel has `BasisDerivation.basisRevoked : GovState → AuthorityClaim → Prop` — a per-claim revocation predicate. This is relation-shaped but binary (revoked / not), too coarse for transport that needs role and degradation distinctions.

### Candidate basis roles / kinds (not ratified)

Basis kinds are **not ratified primitives** — but the note records the pressure for a basis role / kind distinction. Illustrative examples:

- **Authorization basis** — directly grants the action its authority.
- **Evidence basis** — supports a derivation but does not by itself authorize.
- **Observation basis** — supports a verdict input but is not a derivation premise.
- **Recommendation basis** — non-binding suggestion, advisory only.
- **Revocation basis** — supports a `basisRevoked` claim.
- **Exception basis** — supports a one-off departure from policy with separate accounting.

These roles are not currently kernel objects. Whether they should ever become so is a separate decision; this section records the pressure, not the answer.

### Core anti-laundering rule

> Transport may **degrade** authority. It may **not upgrade** a weaker basis into a stronger basis without an explicit fresh-basis derivation.

Examples:

- **Allowed:** `authorization_basis → evidence_basis` under transition. The authorization is no longer effective; the historical witness remains and can be cited as evidence in a future derivation.
- **Forbidden:** `evidence_basis → authorization_basis` under transition. Evidence does not become authorization through transition alone. A fresh authorization derivation, drawing on the evidence as one input among others, is required.

This rule is the candidate-refinement form of the existing `corrective_no_authority_laundering` theorem — generalized from "corrective steps do not create authorization" to "transitions do not upgrade basis kind."

### Candidate laws (non-formal)

The following are **candidate** statements about transport and basis-indexed admissibility. Stated in prose, not formalized; should not be promoted to theorem statements without a forcing case.

1. **Identity.** The identity transition transports κ to κ. (`id ⊢ κ ↦ κ`.)
2. **Composition.** If `B₁ ⊢ κ ↦ κ'` and `B₂ ⊢ κ' ↦ κ''`, then `(B₂ ∘ B₁) ⊢ κ ↦ κ''`, subject to validity of `κ'` at the intermediate state.
3. **Non-inheritance.** If no κ' exists such that `B ⊢ κ ↦ κ'` and κ' is valid for role r in Γ', then the old κ cannot authorize `a` in Γ'.
4. **Fresh basis.** Γ' may still derive `Adm_r(a)`, but only from some `κ_new` valid in Γ' — independent of the failed transport of the old κ.
5. **Role degradation.** Basis may transport into a weaker kind without preserving stronger authority. (Authorization → evidence is admissible degradation; the evidence retains witness value but no authorization power.)
6. **No role escalation.** Transport cannot upgrade a weaker basis into a stronger basis without an explicit fresh derivation. (Anti-laundering core rule, restated.)

### Concrete test example

To check the refinement, work through a concrete case.

**Γ:**
- deploy approved
- maintenance window open
- operator standing valid
- evidence fresh

**Action `a`:** deploy service.

**Old basis κ:** approval receipt + fresh health check + open maintenance window. Role: authorization.

**Transition B:** time crosses past maintenance window.

**Γ':**
- approval receipt still exists
- health check stale
- maintenance window closed

**Result under basis-indexed admissibility:**

- κ transports as **historical / evidence basis only**, not authorization basis. (Approval receipt persists; health check expired; maintenance window closed.)
- Deploy authorization is **not inherited**. The action is not authorized at Γ' on basis κ.
- A **fresh κ_new** is required for `Adm_authorization(deploy)` to hold at Γ'. New approval, new health check, or new maintenance window — derived through ordinary admissibility paths.
- The action is **not permanently forbidden** at Γ'. It is *not authorized on the old basis*. The distinction is exactly what state-indexed `Adm(a, Γ)` cannot express.

This example exercises role degradation (authorization → evidence), non-inheritance (old κ does not authorize at Γ'), the fresh-basis requirement (Adm at Γ' requires new κ), and anti-laundering (the persisting approval receipt does not by itself re-authorize — that would be evidence → authorization escalation).

### Warnings

- **Do not collapse κ into the current `BasisVerdict`.** `BasisVerdict` (`noBasis | advisoryBasis | admissibleBasis`) is verdict *output*; κ is the *reason / witness / basis* being evaluated. They are different objects. A future kernel addition might compute `BasisVerdict` from a κ-indexed input, but the input and the output should not be conflated.
- **Do not introduce basis kinds as code or doctrine.** The role list (authorization / evidence / observation / recommendation / revocation / exception) is illustrative pressure, not minted vocabulary. Promoting it to kernel types or doctrinal categories without a forcing case is exactly the inflation the discipline notes warn against.
- **Do not use a typeclass to hide transport, role degradation, verdict bridge, or basis validity obligations.** Per the smuggling-risk discipline (§7 below; also `nondegenerate-store-semantics.md` §5): any future structure carrying these obligations must keep them explicit at theorem sites. Ambient typeclass resolution would launder all of them at once.
- **This refinement strengthens the transition model but does not earn Boundary Calculus.** Basis-indexed admissibility is a richer *indexing*, not a *calculus*. The Family-with-composition-lemmas verdict stands. The section sharpens what would have to be indexed correctly for any future calculus claim to be honest.

---

## 6. Missing commitments

The kernel currently lacks:

- **Behavioral laws for abstract store ops.** `appendEvidence`, `appendGap`, `appendRevocation`, `applyUpdate` are unconstrained `axiom`-typed declarations in `StateTransition.lean`. Under worst-case axiomatization (everything identity), every Step is state-preserving. This is the deficit named in the recorded null's docstring.

- **Nondegenerate state-transition semantics.** The kernel is *consistent* with the worst-case identity axiomatization. A nondegenerate semantics — even a minimal one — would make existential statements about state change winnable.

- **Temporal model for TTL.** Revocation is currently boolean (`basisRevoked : GovState → AuthorityClaim → Prop`). Time-based revocation requires a clock or step-count model. P27's `Receipt.durability` and `Horizon` exist but are not connected to the admissibility-family kernel.

- **Derivation provenance.** `BasisDerivation` is a strategy structure (function + obligations), not a derivation-with-provenance. Stating "derivation `d` used receipt `r`" requires a trace object that does not exist (candidate #2 strong-form blocker).

- **Boundary individuation principle (blocking, not merely missing).** Whether two boundaries are "the same" or "different" is currently determined by the five-sibling-module decomposition and the Step constructor set. A principled individuation that *justifies* the chosen decomposition vs alternatives is not stated. This is **blocking**: any future boundary-crossing theorem requires (a) **non-vacuous crossing semantics** — a `crosses(action, boundary)` predicate that is provably non-trivial, not always-false or always-true on the cases of interest — and (b) a **load-bearing individuation** that distinguishes "boundary B" from "boundary B in different costume." Without both, crossing predicates can be silently degenerate, and any composition theorem over them is vacuous in a way that does not show up at the type level. (The Phase 0 inventory's "individuation load-bearing in this theorem?" column is the operational foothold; it does not yet supply the principle.)

- **Bridge from transition effects to verdicts.** `BasisDerivation.deriveBasis : GovState → AuthorityClaim → BasisVerdict` is abstract; no concrete derivation reads `RevocationStore`. The bridge from store contents to verdict outputs is currently mediated by structure obligations, not concrete computations.

Each missing commitment would, if added, narrow the kernel's worst-case consistency in specific ways. None should be added speculatively. Each requires its own forcing case.

---

## 7. Next decision gates

The Family-vs-Calculus question becomes more decided only if one of the following becomes real. Three of the four gates point toward calculus; the fourth (obstruction theorem) points toward Family-final. None is currently in motion. None should be started without separate authorization.

- **Concrete nondegenerate store model.** Specific commitment to behavioral laws on `applyUpdate` etc. — e.g., "applyUpdate is a function whose codomain strictly distinguishes its image from its argument on at least one input." Would make `corrective_then_forward_is_not_monotone` decidable (likely TRUE under reasonable laws). *Cost:* kernel strengthening. *Benefit:* the recorded null gets resolved.

- **Minimal structure-obligation for store effects.** Lighter-weight version: rather than committing the kernel globally, define a `StoreEffectful` *structure* carrying proof obligations as fields, in the pattern of `BasisDerivation.revoked_never_admissible` and `CorrectiveMonotone.monotone`. Theorems take a `StoreEffectful` value as an explicit parameter; constructing one requires discharging the obligations directly at the call site. A typeclass version is structurally similar — instances also require their fields be proven — but operationally riskier: typeclass instances make proof obligations *ambient* and easy to smuggle through instance resolution. A downstream `instance` declaration with weak commitments can satisfy the requirement without the call site visibly threading the witness; later readers see the theorem fire without seeing what was claimed. Explicit structure-with-obligations as a theorem parameter or construction requirement keeps the witness threading visible at every use. *Cost:* new abstraction. *Benefit:* opt-in behavior without global commitment, and visible discharge.

- **Composition theorem over boundary transitions.** A theorem of shape "composed transitions preserve admissibility iff each preserves the basis required by the next" — *proved*, not just stated. Would require the missing commitments above. *If achieved:* this is the calculus content.

- **Principled obstruction theorem showing only Family, not Calculus, is possible.** The *positive* version of the recorded null: a theorem proving the kernel cannot be a calculus under any reasonable strengthening, with precise characterization of why. Itself a calculus-shaped result, but with content "the calculus does not exist." *Would require:* the missing commitments to be at least stateable. *If achieved:* the Family verdict becomes formally final, not just empirical.

### Note on the weakest honest nondegeneracy

Discharging store-op nondegeneracy alone does not decide the recorded null. The null hypothesizes a mixed-class composition that produces an authorization the original state lacked. Deciding it requires three independent commitments:

1. **Nontrivial store effects** — e.g., `applyUpdate Γ.policyStore p ≠ Γ.policyStore` for some `(Γ, p)`. The minimal store-effect obligation.
2. **Verdict-sensitive derivation** — a `BasisDerivation` (or analogue) whose `deriveBasis` reads the affected store in a way that propagates to `decideAuthority`. Abstract derivations may ignore state and produce constant verdicts; nondegeneracy of stores does not by itself force verdict variation.
3. **Non-pre-blockage by corrective steps** — a parameter regime where the corrective step `sc` does not revoke or otherwise pre-block the basis the forward step `sf` would unlock. Without this, the mixed sequence may still be `WeaklyLessPermissive` even when (1) and (2) both hold.

Each is independent. Discharging the first does not discharge the others. A `StoreEffectful` obligation enables stating the recorded null in stronger form; it does not by itself decide it.

### Comparative cost

The four gates are not mutually exclusive but are differently expensive. The minimal-structure-obligation route is the lowest-cost *first commitment* but probably not the lowest-cost *complete* path: it satisfies (1) and enables stating the recorded null in stronger form, but does not by itself decide it (per the nondegeneracy note above). The full calculus path requires (1) + (2) + (3) discharged together. The obstruction-theorem route is the highest-cost path, and it points the other direction — toward an honest *non-*calculus claim.

### Discipline: smuggling risk extends to all candidate primitives

The structure-obligation discipline named for `StoreEffectful` applies generally. Any candidate primitive that carries proof obligations — `BoundaryTransition`, `VerdictBridge`, boundary individuation predicates, preservation predicates, crossing predicates — must not become an ambient typeclass whose obligations are resolved invisibly through instance search. The discipline:

- Define the candidate as an explicit *structure* with proof obligations as fields.
- Have theorems take it as an *explicit parameter*, not a `[Class]` instance.
- Make construction the discharge point — the call site provides a value and therefore proves the obligations directly.

Typeclasses are appropriate where the obligations are conventionally trivial (decidable equality, ordering, etc.). They are inappropriate where the obligation *is* the load-bearing claim of a theorem — which is the case for every candidate primitive named above. Ambient resolution makes the load-bearing claim ambient; explicit-parameter discipline keeps it visible at every theorem site.

This generalizes the warning in the second gate above. It is not a doctrine promotion; it is a discipline note that follows from the kernel-house pattern (`BasisDerivation`, `CorrectiveMonotone`) and from the smuggling-visibility argument. Future candidate primitives should default to this pattern and only escape it under specific argument tied to a forcing case.

---

## What this note is NOT

- **NOT** a P28 draft, outline, or scaffold.
- **NOT** authorization to add code, axioms, theorem statements, namespaces, or Phase 0 lemmas.
- **NOT** a renaming of `boundary-composition-investigation.md`. Both notes are sibling working records; this one defines the candidate object; the other records the audit + custody.
- **NOT** ratification of "boundary transition" as a primitive. The candidate fields, moves, and theorem-shapes are handles for review, not minted vocabulary.
- **NOT** a synthesis-paper outline. Synthesis paper, if it ever happens, is "Admissibility Boundary Family with composition lemmas" (current verdict), not the calculus described here.

---

## Pointers

- `working/boundary-composition-investigation.md` — audit record, candidate-theorem audit (#1–#5), Phase 0 inventory, custody decisions.
- `~/git/lean/LeanProofs/Admissibility/Corrective.lean` L280-284 — recorded investigative null with structured category header.
- `~/git/lean/LeanProofs/Admissibility/StateTransition.lean` — abstract store ops; the missing-behavioral-laws site.
- `~/git/lean/LeanProofs/Admissibility/Derivation.lean` — `BasisDerivation` structure; the missing-provenance site.
- Project memory: `project-authority-kernel.md`, `project-admissibility-family-structure.md` for kernel architecture.
