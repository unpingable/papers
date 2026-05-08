# Witness Invariance Failure

**Status:** candidate
**Kind:** boundary condition (with attractor flavor — interpretability and audit work fall into this state by default when invariance is not explicitly tested)
**Originated:** 2026-05-08 (multi-model: paper-claude/web summary of McGee, Zhang, Blank 2026 *Cognitive Science* 50(3); chatty control-theory translation; DeepSeek invariance-test sharpening; chatty operator-side reframe + spike-strip discipline; Lean spike skeleton)
**Primary home (paper):** none yet. Candidate destinations: methodological cross-pointer in P25 §5; sibling §-insert in admissibility-family work; standalone primitive entry.
**Lean formalization:** `~/git/lean/LeanProofs/Admissibility/WitnessInvariance.lean` — abstract `Encapsulated` / `MovesUnderExcludedPerturbation` definitions + `moves_implies_not_encapsulated` boundary theorem + toy counterexample showing selectivity ↛ encapsulation.

## Aphorism (keeper)

> *Specialization is a gain pattern. Encapsulation is an invariance claim. Modularity is an earned boundary.*

Operational corollary:

> *A witness that moves when the wrong variable moves is not lying. It is unqualified.*

## Kernel

A witness can be highly sensitive to a target variable while still being inadmissible as independent testimony about that variable. **Sensitivity is not independence.** Independence is an invariance property under perturbation of variables the witness is claimed not to depend on.

The substitution is *interpretive*, not internal. The failure does not live "inside" the component — there is no goblin agency in the transformer attic. The failure lives at the **admissibility boundary** where the operator/researcher admits a contaminated proxy as if it were a clean witness:

> The component did not substitute X for Y. The observer admitted contaminated testimony as if it were uncontaminated.

This is the laundering shape that admissibility apparatus (NQ / Cadence / Continuity / Custody / Standing / Governor) is built to refuse, but did not have explicit invariance vocabulary for. The primitive supplies the missing rung.

## The four-tier ladder

Mechanistic interpretability and audit work routinely conflate four things:

1. **Selectivity** — the witness responds strongly to X under some regime.
2. **Specialization** — the witness's *dominant observed role* is X-tracking under that regime.
3. **Encapsulation** — the witness's X-testimony is *invariant* under perturbation of non-X variables.
4. **Modularity** — the encapsulated boundary survives enough perturbation to be treated as a *construction boundary*, not just an observed gain pattern.

The laundering chain:

> observable selectivity → inferred specialization → assumed encapsulation → admitted module

Each arrow is a credible inferential move. None of them is *forced*. Selectivity is empirical; specialization is descriptive under regime; encapsulation requires perturbation evidence; modularity requires the boundary to survive enough perturbations to be load-bearing for downstream construction.

## Formal object

Let `World` be the set of states the witness is observed against, `Output` the witness's testimony type, and `sameAdmittedBasis : World → World → Prop` the equivalence relation that holds between worlds equivalent under the witness's *claimed* admitted basis (i.e., differing only in variables claimed-excluded).

**Encapsulation (the invariance claim):**

```
Encapsulated(sameAdmittedBasis, witness) :=
  ∀ a b. sameAdmittedBasis(a, b) → witness(a) = witness(b)
```

**Movement under excluded perturbation (the empirical failure shape):**

```
MovesUnderExcludedPerturbation(sameAdmittedBasis, witness) :=
  ∃ a b. sameAdmittedBasis(a, b) ∧ witness(a) ≠ witness(b)
```

**Boundary theorem:**

```
MovesUnderExcludedPerturbation(R, w) → ¬ Encapsulated(R, w)
```

Mechanized in `LeanProofs/Admissibility/WitnessInvariance.lean`. Toy counterexample (`ToyState` with `syntax`, `semantics` fields; `ToyWitness := syntax && semantics`) proves selectivity ↛ encapsulation.

## Failure predicate

Witness invariance failure occurs when:

1. A witness or component is named by its dominant observed role (e.g., "syntax head," "fact circuit," "sentiment neuron").
2. The role label implies independence from variables outside that role.
3. Perturbation of an excluded variable moves the witness's output.
4. The role label continues to be used as if independence were established.

Compactly: **the witness is admitted over a basis it does not survive.**

The four conditions are jointly required. (3) without (4) is honest characterization; (4) without (3) is just routine labeling under a regime; (1)+(2) without (3) is conjecture awaiting test.

## Diagnostic test (operator-facing)

For any witness/probe/component admitted as testimony about variable X:

1. What is the *claimed admitted basis* — the set of variables the witness is supposedly tracking?
2. What variables are *excluded from the basis* — i.e., the witness is implicitly claimed independent of them?
3. Pick the most plausible excluded variable. Perturb it.
4. Does the witness's output move?
5. If yes: the encapsulation claim fails. The witness is selectivity-positive but encapsulation-negative.
6. If no across multiple excluded perturbations: the boundary may be earnable as modularity.

Without the invariance test, "specialization" is a license plate, not an inspection sticker.

## Adjacency map

- **P25 (Epistemic Border Control)** — strongest formal connection, but phrase carefully. P25's Theorem 1 is the *formal* version: observation-equivalent states force policy-equivalence regardless of target. The interpretability paper is the *empirical* version: implausibility-equivalent states should force attention-equivalence if the syntax head is encapsulated; they don't. Same invariance-failure shape, formal vs empirical. **Do not** claim "same as Theorem 1" without first formalizing the equivalence relation that makes the analogy precise — projection/invariance kinship is real, direct theorem reuse requires explicit work.
- **Admissibility apparatus** — gap fill. NQ / Cadence / Continuity / Custody / Standing / Governor check construction discipline, freshness, authority — but do not have explicit *invariance under perturbation of variables outside the claimed basis* vocabulary. Witness invariance failure supplies the missing rung.
- **Admissibility-Control move taxonomy** (`working/admissibility-control.md`) — captured-substitution sibling. The interpretability finding exhibits captured substitution at the mechanistic-interpretability layer: observable proxy stays fixed (head behaves syntactically) while actual content drifts (semantics modulates). Different laundering surface than the prestige-discourse instances; same structural failure.
- **Authority debt / 5a-5b methodological rule** (`working/authority-debt-and-revocation.md`) — adjacent methodological discipline. The 5a/5b split was earned by row pressure; the four-tier ladder is earned by perturbation pressure. Both: *don't pre-stipulate boundaries the rows haven't forced.*
- **Boundary composition investigation** (`working/boundary-composition-investigation.md`) — consistent. The kernel's family-with-composition-lemmas verdict is unaffected: boundaries are real (selective, specialized) but encapsulation/modularity-as-invariance is a separate question requiring perturbation tests, not a free corollary of the trapdoor lemmas.

## Do not confuse with

- **Mixed-selectivity neuron / messy implementation.** Mixed-selectivity says "this component does many things" — true and useful but undersells the structural bite. Witness invariance failure says "this component fails an invariance test against its *claimed* basis." The structural form admits a sharper contrapositive: it is *the claim* that fails, not the component.
- **Distributional fragility / out-of-distribution behavior.** OOD: the component behaves differently on inputs outside its training regime. Witness invariance failure: inside the regime, the component fails invariance under perturbation of variables claimed excluded. Different failure family.
- **P25 substitution under observability constraint.** P25: witness *cannot reach* target (target is null-space-of-observation). Witness invariance failure: witness *can reach* target *and* a contaminated variable simultaneously, and the contamination is laundered into "tracking the target." Both are admissibility-narrowness failures; different mechanism.
- **Routine experimental confounding.** Confounding: an unmeasured variable creates a spurious correlation. Witness invariance failure: a *measured but excluded-by-claim* variable creates a contaminated witness. The variable is named in the model; what fails is the independence claim about it.
- **Sensitivity analysis.** Sensitivity: how much does the output change when an input changes? Witness invariance failure: the witness's claim of independence is empirically falsified, not just numerically modulated. Sensitivity is the measurement; invariance failure is the verdict.
- **Stale Binding.** Stale binding: target still exists; basis is old. Witness invariance failure: basis is current but contaminated by variables claimed excluded. Different decay shape.

## Three-layer guardrail (anti-universal-acid)

Not every witness that responds to multiple variables is exhibiting invariance failure:

1. **Honest characterization.** "This component is gain-scheduled by X, Y, Z." No invariance claim was made; no invariance was violated. Routine descriptive interpretability.
2. **Regime-bounded label.** "Under regime R, this component's dominant role is X-tracking." A specialization claim, scoped to R. Encapsulation is not asserted; the boundary is not claimed earned. Acceptable as an honest mode-label.
3. **Invariance failure (the primitive).** A component is labeled in a way that implies independence from a variable, the variable is perturbed, the component's output moves. The label is now downstream of an admitted invariance claim that has been refuted.

Diagnostic discipline: before invoking the primitive, rule out (1) and (2). Most "the head does X" statements are mode-labels, not encapsulation claims. The primitive earns its keep when a downstream construction or audit move *depends* on the independence the label implied.

## Worked instance (origin)

**McGee, Zhang, Blank 2026.** *Evidence Against Syntactic Encapsulation in Large Language Models.* Cognitive Science 50(3). https://philpapers.org/rec/MCGEAS-6

Authors identify attention heads in BERT, GPT-2, and Llama 2 that track syntactic dependencies. They perturb semantic plausibility of sentences and measure whether the attention pattern across the syntactic dependency link survives. It does not — implausible semantics generally reduce attention between syntactically linked words. Specialization confirmed; encapsulation rejected; modularity unearnable. Across all three models.

The paper's finding maps cleanly onto the four-tier ladder: heads are selective for syntactic dependencies (1), specialized for syntax-tracking under typical regime (2), but not encapsulated against semantic plausibility (3 fails), so cannot be admitted as syntax modules (4 unclaimable).

## Architectural rules

- **Witness labels name observed testimony roles. They do not name construction boundaries.**
- **Construction boundaries require invariance tests.** Not just consistency checks, not just functional ablation — explicit perturbation of variables claimed excluded.
- **Independence is an empirical commitment, not an inferential bonus.** It must be tested against the variables the witness is claimed not to depend on.
- **Selectivity is the cheapest signal; modularity is the most expensive.** Don't promote across the ladder without perturbation evidence at each step.

## Promotion guardrail (candidate → working)

Hold as candidate until at least one of:

1. A paper-side citation slot in P25 (or a paper sibling) actually uses the four-tier ladder vocabulary in prose.
2. An audit failure in NQ / Governor / agent_gov is diagnosed using the witness-invariance-failure shape, with the diagnosis surviving review.
3. A second worked-instance from a different domain (not LLM interpretability) exhibits the same four-tier ladder + invariance test, confirming the primitive is cross-domain rather than cog-sci-specific.

Until any of those land, the keeper stays in primitives, not in main doctrine.

## Provenance

- **2026-05-08 origin.** Paper: McGee, Zhang, Blank 2026 *Cognitive Science* 50(3), surfaced via paper-claude/web channel.
- **Multi-model lineage:** chatty (control-theory translation: gain-scheduling, MIMO, invariance-as-disturbance-decoupling), DeepSeek (invariance-test methodology + mixed-selectivity sharpening), chatty (operator-side reframe — interpretive substitution at admissibility boundary, not internal goblin theater; P25-as-projection-not-direct-theorem-reuse spike strip; Lean spike skeleton).
- claude-code-papers (this primitive entry; Lean formalization at `LeanProofs/Admissibility/WitnessInvariance.lean`).
- Filed candidate / default-density per `feedback-note-density-subtypes.md`. Not rich-staging; not promoted.
