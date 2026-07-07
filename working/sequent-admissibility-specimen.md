# The Admissibility Specimen: a kernel-checked sequent calculus with cut

*Status:* CANDIDATE / working note, filed 2026-07-06.
*Lean custody:* `~/git/lean/LeanProofs/Scratch/SequentAdmissibility.lean`
(Custody-Class: SCRATCH, unwired, sorry-free, zero axiom declarations;
`lake env lean` EXIT=0; full `lake build` EXIT=0, 2026-07-06).
*Provenance:* operator-supplied 2026-07-06, downstream of an external ChatGPT
design autopsy (the "adversarial clown show that accidentally became a design
review"). The external session located the correct encoding but had no
compiler; this file is the kernel-checked landing.

## What landed

A single-succedent intuitionistic propositional sequent calculus over
{atom, ⊥, ∧, ∨, →} in which **no structural rule is primitive and all four
are admissible**, proved in Lean 4 core (v4.29.0, Mathlib-free):

| Meta-theorem | Form | Axiom footprint |
|---|---|---|
| `monotone` (Γ ⊆ Δ → Deriv Γ C → Deriv Δ C) | def (transformer) | **none** |
| `weaken` / `contract` / `exchange` / `weakenAppend` | corollaries of monotone | none / none / none / propext |
| `size_monotone` (monotone preserves size *exactly*) | theorem | propext |
| `initGen` (general identity from atomic init) | def, induction on formula | **none** |
| `explode` (ex falso as transformer) | def, structural | propext, Quot.sound |
| **`cut`** | **def (computable transformer)** | propext, Quot.sound |
| `cutAppend` (Γ ++ Δ split-context form) | def | propext, Quot.sound |
| `consistency` (⊬ ⊥ at empty context) | theorem | **none** |
| `disjunction_property` (⊢ A∨B ⇒ ⊢A or ⊢B) | theorem | **none** |
| `mp` (modus ponens via cut) | def | propext, Quot.sound |

No `Classical.choice` anywhere — fully constructive. No `sorry`/`sorryAx`/
`admit`/`unsafe`. The {propext, Quot.sound} footprint is the standard cost of
well-founded recursion in core; it matches the resident kernel footprint.

## Exact scope (per acceptance gate)

```text
Formula:     atom / bot / and / or / imp   (negation = imp A bot)
Context:     List Formula, read by membership/subset only
Succedent:   single
Primitive structural rules: NONE
Admissible:  monotone (⇒ weakening, contraction, exchange; size-preserving),
             general identity, ex falso, CUT
Cut:         YES — primary induction on cut-formula degree, secondary on
             sum of derivation sizes; a def that COMPUTES the cut-free
             derivation
Axiom-clean: zero declarations; footprint ≤ {propext, Quot.sound}
```

## Honest label (operator's caveat, adopted)

**Core-List membership-context G3-style admissibility calculus.** NOT
"canonical multiset G3ip formalization." Left rules keep their principal
formula (Kleene set-style), so contraction is absorbed and exchange is
meaningless at rule level; contexts are Lists read through membership only.
Derivability-equivalence with textbook multiset G3ip is standard math but
**unproved here** → `cannot_testify (a)`. Also unproved: height-preserving
cut (only the structural rules are size-preserving — standard), any
semantics/completeness, and *anything about the governance kernels*.

## The encoding discoveries that made it land (ported as doctrine)

1. **`Deriv : Ctx → Formula → Type`, not Prop.** Derivations are data;
   they carry a size; cut is a recursive transformer, not a fog bank.
2. **Membership-based rules on List, no Multiset.** The seed's
   `Multiset.erase_add` pressure point vanishes entirely: one `monotone`
   theorem over `⊆` subsumes weakening + contraction + exchange at once,
   size-preserving — the "boring lemma" that funds the boss fight.
3. **Two Lean-specific traps found and killed en route:**
   - `fun` binders consume *implicit* binders positionally — `fun n d e hn`
     silently bound `d := Γ`. Cure: explicit `fun n {Γ} {C} d e hn`.
   - `List.Mem` is Prop, so `cases` on a membership proof cannot eliminate
     into Type (the derivation being built). Cure: split on **decidable
     equality with the cut formula** (`if heq : X = A`) — `DecidableEq
     Formula` earns its keep; membership only ever needs Prop-level
     elimination (`Or.resolve_left`).
4. **Recursion architecture:** outer WF recursion on cut-formula degree
   (one trivial decreasing proof), inner recursion on a Nat bound of the
   size sum, with `ihA` (cut at smaller formulas) threaded as a hypothesis.
   All decreasing goals discharged by one `simp only [size, size_monotone];
   omega` — this shape avoids lexicographic-measure hair entirely.

## What this is and is not (register fence)

The word "admissible" here has its literal Gentzen meaning: a rule is
admissible when every sequent derivable with it is derivable without it.
This file is the **literal proof-theoretic referent** that the governance
vocabulary borrows from — cut ("intermediate claims can be eliminated when
their discharge is real"), weakening ("added context does not forge proof"),
contraction ("duplicated assumptions do not multiply authority"). The rhyme
is real and acknowledged; the composition is **refused**: nothing here
imports or exports Tier/Verdict/cap, no typeclass, no unifier. "Admissibility
calculus" as a governance unification target stays dead per the no-unifier
doctrine. This is a sequent calculus that happens to be the pun's spine.

## Downstream candidates (operator's lane, unauthorized from here)

- **Agent-eval harness**: "extend / re-derive this file; forbidden: sorry,
  admit, axiom, unsafe; verdict by grep + lake build + #print axioms." The
  representation choices punish bullshit; failures become corpus.
- **Benchmark ladder**: multiset-G3ip equivalence, height-preserving
  inversion lemmas, textbook G3ip with erasing rules, Dyckhoff LJT
  (terminating proof search) as escalation rungs.
- **Doctrine specimen**: candidate proof narrative → rejected;
  kernel-checked derivation transformer → admitted.
