# Nondegenerate Store Semantics (working note)

**Logged:** 2026-05-06
**Status:** Design / investigation only. Not doctrine, not a P28 draft, not authorization to add code, axioms, typeclasses, or theorem statements.
**Sibling:** `working/boundary-composition-investigation.md` (audit + custody record); `working/boundary-transition-model.md` (candidate object).
**Lives near:** the recorded investigative null `corrective_then_forward_is_not_monotone` at `Corrective.lean` L280-284.

---

## 1. Non-ratification header

This note is a design / investigation document. It identifies what behavioral commitments would be honest, minimal, and non-smuggling — *if* a future decision authorized work toward deciding the recorded null.

Nothing in this note authorizes:

- adding code, axioms, typeclasses, or theorem statements to the Lean kernel;
- minting new primitives;
- drafting P28;
- promoting any candidate commitment into doctrine;
- treating "decide the recorded null" as a goal rather than a question.

The candidate commitments named below are *handles for review*, not authorization to build. The smuggling risks are *constraints on how* any future authorized work would be done, not green-lights to start.

---

## 2. Current kernel truth (restated)

Per AG audit 2026-05-06 (recorded in `boundary-composition-investigation.md`):

- The kernel currently supports **Family-with-composition-lemmas**, fork 2 of 3.
- **Boundary Calculus is not earned.**
- The recorded investigative null `corrective_then_forward_is_not_monotone` (Corrective.lean L280-284) is *stateable in current vocabulary* but *undecided under current commitments*. Its docstring explicitly says: *"This `sorry` is a recorded investigative null, not a deferred proof to be eliminated by axiomatizing `applyUpdate` here."*

The custody decision is unchanged: keep in source as a recorded null with the structured category header. The question this note opens is what would have to be true for the null to *become* decidable, and at what cost.

---

## 3. The three missing commitments — precise definitions

Per `boundary-transition-model.md` §7 nondegeneracy note: deciding the recorded null requires three independent commitments. Each defined precisely in prose below; none currently committed in the kernel.

### 3.1 Nontrivial store effects

**Informal:** the abstract store operations are not all identity functions.

**Precise content (illustrative form, not authorized as a theorem):** for at least one of `appendEvidence`, `appendGap`, `appendRevocation`, `applyUpdate`, there exist inputs producing outputs distinct from the input store. For the recorded null specifically (which involves a forward `amendPolicy` step), `applyUpdate` must be nontrivial: there exist `s : PolicyStore` and `p : PolicyUpdate` such that `applyUpdate s p ≠ s`.

**Why it matters:** under the worst-case axiomatization where every store op is the identity, every `Step` is state-preserving and `decideAuthority env Γ a K = decideAuthority env (applyStep Γ s) a K` for all parameters — the recorded null's existential is then provably FALSE.

**Why it is independent of (3.2) and (3.3):** nontrivial store effects can hold without the verdict computation being sensitive to them (3.2 fails) and without sequence-level non-pre-blockage (3.3 fails).

### 3.2 Verdict-sensitive derivation

**Informal:** at least one `BasisDerivation` (or analogue) reads the affected store in a way that propagates to `decideAuthority`.

**Precise content (illustrative):** there exist `env : DerivationEnv`, `Γ : GovState`, `s : Step`, `a : Actor`, `K : AuthorityClaim` such that

```
decideAuthority env Γ a K ≠ decideAuthority env (applyStep Γ s) a K
```

That is: at least one verdict actually moves when state moves.

**Why it matters:** even with nontrivial store effects (3.1), if every concrete `BasisDerivation` ignores the affected store (e.g., `deriveBasis Γ K = constant`), the verdict is state-blind and the recorded null's existential is undecidable from state-change alone. Abstract `BasisDerivation` permits the constant case.

**Why it is independent of (3.1) and (3.3):** a verdict-sensitive derivation is a structural feature of *which* derivation environments we admit; it does not by itself imply that store ops are nontrivial in any specific way, nor that mixed-class sequences are non-degenerate.

### 3.3 Non-pre-blockage by corrective steps

**Informal:** the corrective step does not revoke or otherwise pre-block the basis the forward step would unlock.

**Precise content (illustrative — this is the recorded null's existential restated):** there exist `env`, `Γ`, `sc`, `sf`, `a`, `K` such that

```
IsCorrective sc ∧ IsForward sf ∧
decideAuthority env Γ a K ≠ AuthorityVerdict.authorized ∧
decideAuthority env (applySteps Γ [sc, sf]) a K = AuthorityVerdict.authorized
```

That is: the mixed sequence creates an authorization that did not hold at Γ, *and* that the corrective step did not pre-empt.

**Why it matters:** even with (3.1) and (3.2), a structurally global `recordRevocation` (revoking every claim) or global `declarePolicyGap` (gapping every scope) would pre-block the forward step's verdict effect. The kernel's `BasisDerivation.basisRevoked : GovState → AuthorityClaim → Prop` is per-claim, which *permits* scope-specific corrections, but the kernel does not exhibit a concrete environment proving non-pre-blockage occurs for some choice of parameters.

**Why it is independent of (3.1) and (3.2):** non-pre-blockage requires a granularity property of the derivation environment (corrective effects do not span all bases) that is orthogonal to nontrivial store effects and to verdict sensitivity. A derivation could be both nontrivial and verdict-sensitive yet have its corrective and forward effects always overlap.

### Combined effect

(3.1) + (3.2) + (3.3) is *almost* the recorded null itself — (3.3) is the existential at the null's core. The role of (3.1) and (3.2) is to make (3.3) discharge-able with a *concrete* witness rather than an axiom. Without (3.1) and (3.2), (3.3) can only be claimed by axiom or by a tautological construction.

---

## 4. Modeling options per commitment

For each commitment, four candidate ways to introduce it. Marked by feasibility against the current kernel.

### 4.1 Nontrivial store effects

| Option | Feasibility | Notes |
|---|---|---|
| Concrete witness model | **Yes.** | E.g., define `PolicyStore := List PolicyUpdate` and `applyUpdate := fun s p => p :: s`. Nontriviality is then provable by example. |
| Structure-with-obligations | **Yes.** | A `StoreEffectful` structure carrying fields like `applyUpdate_nontrivial : ∃ s p, applyUpdate s p ≠ s`. Discharged by concrete instances. |
| Theorem parameter | **Yes.** | Theorems take the witness explicitly. |
| Not currently expressible | N/A | The vocabulary is sufficient. |

### 4.2 Verdict-sensitive derivation

| Option | Feasibility | Notes |
|---|---|---|
| Concrete witness model | **Yes (conditional on 4.1).** | A specific `BasisDerivation` whose `deriveBasis` reads e.g. `RevocationStore` or `PolicyStore`. Requires concrete store types to be useful. |
| Structure-with-obligations | **Yes.** | A `VerdictSensitive` structure (or extension of `BasisDerivation`) carrying a state-sensitivity obligation. |
| Theorem parameter | **Yes.** | |
| Not currently expressible | N/A | |

### 4.3 Non-pre-blockage

| Option | Feasibility | Notes |
|---|---|---|
| Concrete witness model | **Yes (conditional on 4.1 + 4.2).** | A specific (env, Γ, sc, sf, a, K) tuple satisfying the existential, derivable from concrete store + concrete verdict-sensitive derivation. |
| Structure-with-obligations | **Yes, but tautological-adjacent.** | A `MixedClassWitness` structure carrying the existential as a field. Constructing one requires the witness. |
| Theorem parameter | **Yes.** | |
| Not currently expressible | N/A | |

### Summary

All three commitments are expressible in the current vocabulary. The dependency graph is roughly: (4.1) is foundational; (4.2) is foundational for verdict-side reasoning; (4.3) is downstream of both.

The cheapest *honest* path is the **concrete witness model** for all three: a specific `PolicyStore` type, a specific `BasisDerivation` reading it, a specific tuple discharging the recorded null. The structure-with-obligations route is also honest provided the obligations are discharged concretely at construction (per the discipline note in `boundary-transition-model.md` §7).

---

## 5. Smuggling risks

Three categories of dishonesty, each closing a different escape route.

### 5.1 Ambient typeclasses

**Risk:** declaring `class StoreEffectful` (or similar) as a typeclass means downstream `instance` declarations resolve obligations invisibly through instance search. A weak `instance` with under-discharged fields can satisfy theorem requirements without the call site visibly threading the witness; readers see the theorem fire without seeing what was claimed.

**Discipline:** structure-with-obligations as explicit theorem parameter. The kernel-house pattern (`BasisDerivation`, `CorrectiveMonotone`, `RecoveryEnv`) already enforces this. No `[StoreEffectful]` instance arguments; pass `(eff : StoreEffectful)` values.

**Generalization:** this risk extends to *every* candidate primitive — `BoundaryTransition`, `VerdictBridge`, individuation predicates, preservation predicates, crossing predicates. None should become typeclasses while their obligations are load-bearing.

### 5.2 Axiomatizing store effects

**Risk:** writing `axiom applyUpdate_nontrivial : ∃ s p, applyUpdate s p ≠ s` forces the claim without any concrete model exhibiting it. The kernel commits to nontrivial effects without earning the commitment. Future readers cannot audit the axiom against any constructive content.

**Discipline:** provide a *concrete model* — a specific `PolicyStore` definition with a specific `applyUpdate` — and prove nontriviality from the model. The model can live in a sibling module (e.g., `Admissibility/Concrete/PolicyStoreList.lean`) so that the abstract layer remains store-agnostic and the concrete layer is the discharge point.

**Sub-risk:** even concrete models can be over-strong (e.g., `applyUpdate := id` is a concrete model of the abstract type but it falsifies the very nondegeneracy we want). Concrete models must be both *constructive* (built from primitives, not axiomatized) and *witnessing* (provably exhibit the property).

### 5.3 Tautological verdict bridges

**Risk:** defining `BasisDerivation.deriveBasis` such that the recorded null is true *by definition* — e.g., `deriveBasis Γ K := if K ∈ amendmentsOf Γ.policyStore then admissibleBasis else noBasis`, then choosing parameters where this trivially differs across `applyUpdate`. The construction is technically a witness, but it constructs the answer rather than discovering it.

**Discipline:** the verdict bridge should be motivated by a *non-recorded-null reason* — e.g., "this is what AG actually does operationally," "this is what a realistic policy lookup looks like." The recorded null then falls out as a downstream consequence rather than being engineered to fall out.

**Sub-risk:** this is the hardest to detect. A bridge that *happens* to make the recorded null trivially true is hard to distinguish from one that was *engineered* to. The protection is provenance: bridges should be motivated by independent operational requirements documented in the bridge's docstring, not by what theorem they enable.

### 5.4 Cross-cutting smuggling: structure-named-after-conclusion

**Risk:** naming a structure after the property it should imply. E.g., a `MixedClassWitness` structure whose only field is the recorded null's existential. Construction "discharges" the obligation but provides no information beyond "I asserted this."

**Discipline:** structures should bundle *independent* obligations whose conjunction implies the desired conclusion. A `MixedClassWitness` is acceptable only if it carries (3.1) + (3.2) + adequate-granularity fields whose combination *yields* the existential — not if it carries the existential directly.

---

## 6. Scope of what (3.1) + (3.2) + (3.3) decides

**Honest finding:** discharging the three commitments **decides the recorded null** but does **not** by itself earn Calculus.

What discharge gives:

- A concrete environment where mixed-class composition can fail to be monotone.
- A proof of `corrective_then_forward_is_not_monotone` (the existential becomes provable).
- A sharper Family verdict: "Family-with-composition-lemmas, *and* the mixed-class non-monotonicity question is decided in the affirmative."

What discharge does *not* give:

- A *general* characterization of when mixed-class composition fails monotonicity. (We get one witness, not a predicate.)
- A *systematic* theory of how forward and corrective steps interact across longer sequences.
- Composition theorems over arbitrary boundary transitions.
- An algebraic structure (lattice, category, order) over admissibility transitions.

To advance toward Calculus, additional work would be required:

- **Predicate characterization.** A predicate `MixedClassCommutes : Step → Step → ... → Prop` describing *when* `[sc, sf]` preserves `WeaklyLessPermissive`, with a forcing-case-driven derivation.
- **Compositional theorems.** Theorems about how `MixedClassCommutes` behaves under list-composition, including conditions for `[s₁, s₂, ..., sₙ]` to preserve monotonicity.
- **Structural theorem.** A proof that the predicate, taken together with the existing trapdoor / monotonicity / blocking-dimension lemmas, induces an algebraic structure over admissibility transitions.

**None of these is implied by (3.1) + (3.2) + (3.3) alone.** The three commitments are necessary for any Calculus-bearing theorem to even be stateable in non-vacuous form, but they are not sufficient for Calculus to *exist*.

This tightens an earlier framing: chatty's "minimal-typeclass route is the cheapest path to an honest calculus claim" was already qualified to "cheapest first commitment" in `boundary-transition-model.md` §7. This note adds: even after discharge, what is gained is a sharpened Family verdict, *not* a Calculus. The path from "recorded null decided" to "Calculus earned" is itself a further sequence of independent decisions.

---

## 7. Next gates (do not execute)

Three gates of increasing scope. None is authorized. None should be opened without separate decision tied to a forcing case.

### Gate A: Decide the recorded null

Discharge (3.1) + (3.2) + (3.3) via concrete witness model OR structure-with-obligations (per §4 + §5 discipline). Result: `corrective_then_forward_is_not_monotone` becomes a theorem with a concrete proof; the structured-header comment can be replaced with a normal docstring.

*Cost:* concrete `PolicyStore` (or analogue) + concrete `BasisDerivation` + concrete witness tuple. Probably one new sibling module under `Admissibility/Concrete/`.
*Benefit:* recorded null resolved; Family verdict sharper.
*Risk:* if the concrete model is not motivated by an independent operational reason, falls into smuggling risk 5.3 (tautological verdict bridge).

### Gate B: Characterize mixed-class composition

Build the predicate `MixedClassCommutes` (or appropriate analogue) and prove general theorems about when `[s₁, s₂, ..., sₙ]` preserves `WeaklyLessPermissive`. Requires Gate A + structural induction.

*Cost:* substantial — likely a new module with its own composition theorems.
*Benefit:* the Family verdict gets explicit structural content, not just example witnesses.
*Risk:* the predicate could become a vocabulary trap (every interesting case becomes a special case of a too-broad predicate that says nothing).

### Gate C: Compose into Calculus

Prove the predicate from Gate B induces an algebraic structure over admissibility transitions sufficient to earn the Calculus title. Requires Gate B + a structural / categorical / order-theoretic claim.

*Cost:* high; this is the actual calculus work.
*Benefit:* Boundary Calculus earns its name (or — under an obstruction theorem — Calculus is provably out of reach and Family is final).
*Risk:* every smuggling risk in §5 applies, especially 5.4 (structures named after conclusions).

### Note on order

These gates are conditional, not strictly sequential — Gate A could be pursued without Gate B; Gate B without Gate A would be groundless. Gate C requires Gate B. The honest structure is: Gate A first (if at all), then a separate decision about whether to open Gate B, then a separate decision about whether to pursue Gate C.

**None of these should be opened without a forcing case** — a paper claim that depends on the gate's content, an external request that requires it, or a discovered result that makes the gate a small step rather than a leap. Investigative-mode discipline: state the target, accept null results, do not redefine terms mid-search.

---

## What this note is NOT

- **NOT** authorization to add axioms, typeclasses, theorem statements, or kernel code.
- **NOT** a P28 draft, outline, or scaffold.
- **NOT** ratification of `StoreEffectful`, `VerdictSensitive`, `MixedClassWitness`, or any other named structure as a kernel addition. The names appear here to make the design legible; they are not minted vocabulary.
- **NOT** a commitment to opening Gate A. Whether to investigate the missing commitments at all, and in what order, is the open question this note exists to make legible.
- **NOT** a renaming of the synthesis target. The synthesis paper, if it ever happens, remains "Admissibility Boundary Family with composition lemmas" under current verdict.

---

## Pointers

- `working/boundary-composition-investigation.md` — audit record, candidate-theorem audit, Phase 0 inventory, custody decisions.
- `working/boundary-transition-model.md` — candidate object (executable + contextual transitions), §7 nondegeneracy note, smuggling-risk discipline.
- `~/git/lean/LeanProofs/Admissibility/Corrective.lean` L280-284 — recorded investigative null with structured category header.
- `~/git/lean/LeanProofs/Admissibility/StateTransition.lean` — abstract store ops; (3.1) discharge site if Gate A is opened.
- `~/git/lean/LeanProofs/Admissibility/Derivation.lean` — `BasisDerivation`; (3.2) discharge site if Gate A is opened.
- Project memory: `project-authority-kernel.md`, `project-admissibility-family-structure.md`.
