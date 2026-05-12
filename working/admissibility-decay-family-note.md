# Admissibility Decay Under Representational Persistence
## Family-level note for the stale-license primitives

**Status:** Candidate *family designation*, not ratified. Surfaced 2026-05-11 from cross-primitive audit triggered by the five-in-48-hours candidate pile. Names a structural commonality that runs across five admissibility-family candidates filed 2026-05-09 → 2026-05-11. Filed because not naming it would force re-discovery in future cross-primitive work.

**This note is not itself a primitive.** It is a taxonomic claim about a family. The primitives are the points; the family is the line that runs through them.

## The family invariant

```
At time/condition t₀ (Γ₀):  X licenses use U.
At time/condition t₁ (Γ₁):  the licensing relation X → U no longer holds.
Failure mode:                The system continues behaving as if X still licenses U.
```

The "license" is whatever conditional relation grants X the standing to authorize, support, or sanction U. Different domains have different licensing structures (kind-based, signal-based, witness-based, commitment-based, scope-based). The pattern is the same: licensing condition lapses while representational layer continues operating undisturbed.

## Five axes (one primitive each)

| Axis | Primitive | X licenses U | Failure costume |
|---|---|---|---|
| Artifact kind | **FiatAdmissibility** (built) | artifact category licenses a use | prestige token "supporting" what only theorem could support |
| Signal shape | **Signal Authority** (candidate) | signal-shape licenses a standing change | silence "revoking" what only explicit refusal could revoke |
| Witness standing | **Testimony vs. self-theory** (candidate) | testimony licenses claims about its own state | phenomenology "explaining" what only substrate-mechanics could explain |
| Commitment scale | **Commitment Standing Decay** (candidate) | speech-act licenses operational obligation | rhetoric "binding" what only viability-admissible action could bind |
| Composition / scope | **Local-Global Validity Gap** (candidate) | local validity licenses global validity | locally-valid operations "composing into" what only obstruction-free composition could compose into |

All five say the same thing in different domains: *the relation that would license the use is missing, and the system continues acting as if it isn't.*

## Basis audit (anti-collapse check)

For each candidate primitive, answer:

1. **What is being misclassified?**
2. **What relation originally licensed the use?**
3. **What condition changed, or never held?**
4. **What rhetoric / interface persisted unchanged?**
5. **What consequence follows from continuing to act as if the license holds?**

If two candidates answer with the same objects across all five questions, they are costumes of one primitive in two outfits.

**Audit run 2026-05-11.** The five candidates above each answer with structurally distinct objects:

- FiatAdmissibility's X is an *artifact kind*; Signal Authority's X is a *signal shape*; these are not the same kind of thing.
- Testimony vs. self-theory's X is a *witness's report about itself*; this is not collapsible into artifact kind or signal shape — the witness is the artifact, but the report is the use, and the licensing question is whether testimony's self-knowledge extends to substrate-knowledge.
- Commitment Standing Decay's X is a *speech-act under viability constraints*; the licensing relation is time-indexed and depends on an external state vector (admissible action set), which makes it materially different from the structural cases.
- Local-Global Validity Gap's X is a *local property*; the licensing relation is scope-conditional rather than time-conditional, and the obstruction is composition-theoretic.

**Conclusion:** five distinct primitives, one shared family.

## Sub-axis: structural vs. conditional

The family invariant covers two regimes that probably deserve naming:

- **Structural failures.** Γ₀ = Γ₁; the licensing relation never held. The failure is invariant over time. FiatAdmissibility and testimony-vs-self-theory live here — prestige tokens never license theorem-use; testimony never licenses substrate-theory.
- **Conditional failures.** Γ₀ ≠ Γ₁; the licensing relation held under some conditions and stopped holding under others. The failure is condition-dependent. Commitment Standing Decay lives here cleanly (viability conditions); Signal Authority bifurcates (unauthorized protocol extension is structural; protocol-clause decay over time is conditional); Local-Global Validity Gap is scope-conditional rather than time-conditional but in the same regime.

**Caveat on the family name:** "decay" implies the conditional regime more than the structural regime. The honest reading is that "decay" covers conditional cases; structural cases are *failure of the license to ever have been held*, which is admissibility *absence*, not admissibility *decay*. The family name covers both because the *representational persistence* part is the same — rhetoric outlives whatever licensing relation was supposed to be there, whether it was there transiently or never.

A more accurate family name would be *License persistence after admissibility failure* — covers both never-held and held-then-lost. *Admissibility decay under representational persistence* is the catchier phrase but slightly under-covers the structural cases. Both can co-exist: one for prose, one for formal use.

The repair operators differ between regimes:

- **Structural cases:** refuse the inference outright. The license never existed; no recovery move available; the only honest path is denial.
- **Conditional cases:** detect staleness; consider whether to re-bind under new conditions or acknowledge revocation. Re-binding may be possible (the original commitment can be renewed under updated viability); explicit revocation may be required.

## Adjacent candidate observations (named, not promoted)

The five-axis family has neighbors worth naming without filing as primitives. Each surfaced from a separate forcing case; none has the second-domain forcing case required for primitive ratification.

- **Regime-conditioned admissibility.** The same action may invert admissibility across regimes — normally inadmissible under nominal conditions, uniquely admissible under specific sensor-certified critical conditions. Extension request for the existing kernel's `classify`-shaped functions to take a regime parameter; not yet a primitive on its own axis. Surfaced 2026-05-11.

- **Selectorate mutation.** Tactical admission can mutate the future authority surface. Distinct axis from Commitment Standing Decay (which is commitment-standing-over-time): this is *authority-surface mutation by admission* — the body authorized to decide changes as a result of prior admissions. Generalizes beyond electoral politics (open-source captured by corporate contributors, standards bodies captured by large implementers, platforms captured by engagement-maximizing users, etc.). Candidate handle; not promoted. Surfaced 2026-05-11.

- **Register-as-admissibility-filter.** (See `register-capture-admissibility.md`.) Style operating as an admissibility prior on claim-emission. Currently a working-note analytical synthesis; primitive ratification awaits a second forcing case in a non-LLM domain (academic publishing, legal precedent, regulatory framework). Surfaced 2026-05-11.

All three are watch-list items: forcing-case + cross-domain instance required for primitive promotion.

## What this is NOT

- **Not a license to mint a sixth primitive just because it would "fit."** The family is descriptive of what's already been surfaced through independent forcing cases. New primitives still need their own forcing cases and basis audits.
- **Not a justification for collapsing the five into one.** The basis audit affirmed distinctness. The family is a *line through points*, not a *single point* the five are projections of.
- **Not a Lean module.** Too premature. The existing kernels (Authority, StateTransition, Derivation, Execution, Corrective, FiatAdmissibility) each pin a specific axis. A higher-order "stale license" construct in Lean is only worth building if a single theorem actually composes two of the primitives — and none does yet.
- **Not a primitive in its own right.** The family resemblance is itself a structural observation, not a doctrine that licenses moves. Promoting *Admissibility decay* to a primitive would be a category mistake.

## Lean implications (deferred)

If the family is real and earns ratification, the existing admissibility kernels may want a higher-order construct expressing "license under conditions Γ." The minimal sketch:

```lean
class LicenseRelation (X U Γ : Type) where
  licenses : X → U → Γ → Prop

def licensePersistsAfterFailure
    {X U Γ : Type} [LicenseRelation X U Γ]
    (x : X) (u : U) (γ₀ γ₁ : Γ) : Prop :=
  LicenseRelation.licenses x u γ₀ ∧ ¬ LicenseRelation.licenses x u γ₁
```

But this is way beyond v0. The argument for building it requires:
- A theorem that genuinely composes two of the five primitives
- Demonstration that the abstraction *forces* a useful refusal (rather than just describing existing refusals)
- Resolution of the structural vs. conditional sub-axis

Until then: the existing kernels remain the load-bearing Lean artifacts. This family note is conceptual scaffolding for the prose layer.

## Ratification gate (for the family designation itself)

The family is itself subject to the primitive-ratification gate, one level up:

- [ ] Sixth admissibility-family primitive surfaces from an independent forcing case and fits cleanly (without strain) into the five-axis frame
- [ ] Generator test at family level: does the family description disqualify candidate "primitives" that don't fit? (Anti-collapse — the family must be able to *refuse* membership, not just admit it.)
- [ ] Structural-vs-conditional sub-axis resolved as either two families or one with two regimes
- [ ] Decision on whether "Admissibility decay under representational persistence" or "License persistence after admissibility failure" is the durable name (or whether both coexist by register: prose vs. formal)
- [ ] Composition test: does at least one cross-primitive theorem in Lean force the higher-order construct?

If the family gate doesn't clear in 6–12 months and no sixth primitive surfaces, the family note remains as descriptive cross-reference and the primitives stand independently. The family isn't load-bearing; it's a useful frame that becomes load-bearing only if a future theorem requires it.

Not promoted. Filed as descriptive working framing.

---

**Cross-references (member primitives):**

- [commitment-standing-decay-candidate.md](commitment-standing-decay-candidate.md) — commitment-scale axis
- [signal-authority-candidate.md](signal-authority-candidate.md) — signal-shape axis
- [testimony-vs-self-theory.md](testimony-vs-self-theory.md) — witness-standing axis
- [local-global-validity-gap.md](local-global-validity-gap.md) — composition/scope axis
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — artifact-kind axis (built)

**Sibling-but-distinct (broader laundering family):**

- `project-admissibility-doctrine-stubs.md` (memory) — declared-substitution stubs; the *intractability-driven* sibling of this family. Different mechanism (formally hostile target forces proxy substitution); same superclass of "the wrong thing wearing the name of the right thing." Likely a separate but adjacent family.
- attack-surface-laundering, control-set-laundering, scope-laundering — the *evidentiary-exclusion* and *actuator-narrowing* siblings. Same superclass of "convenience promoted to ontology"; different axis again.
