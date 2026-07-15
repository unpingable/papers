# Reachability insufficiency — candidate primitive (2026-05-30)

**Status:** Candidate refusal-kernel residue. Spun out 2026-05-30 from [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md) §"Five candidate theorems" #1 (the anti-laundering theorem) and §"Audit summary" Q7 (the load-bearing five-clause predicate). The desynchronized-horizons note remains the doctrine source; this note carries the compile-probe scope statement so reachability-insufficiency has its own gate distinct from the Conductance hygiene fragment.

**Policy correction (2026-07-14):** the operator-endorsement, forcing-case, and downstream-consumer “licenses” recorded below are superseded as build permissions. A coherent claim, model, countermodel, or specification may be formalized in Scratch before any consumer exists, and the formalization may lead later code. The theorem-shape, quantifier, non-vacuity, and axiom questions in this note remain intrinsic checks on what the artifact honestly proves. Scratch still cannot testify for or pin production; public promotion and runtime conformance remain separate.

**Superseding context (2026-05-30 update):** this scope statement is now Artifact-1-prep-work inside the [recovery-topology build ladder](recovery-topology-build-ladder-2026-05-30.md). The ladder reframes reachability as substrate (not a clause), splits the predicate into `Reachable + five admissibility clauses`, and historically sequenced the Lean cut after a candidate note. Under the 2026-07-14 correction, that sequence is a workflow preference: Scratch compile probes may help settle the four open shape questions, while the intended theorem still cannot be claimed until its quantifiers and assumptions are coherent. Read the ladder before this note when returning.

**Posture:** The scope statement is an intrinsic design checklist, not a permission receipt. A compile probe may proceed without a runtime consumer; any resulting theorem must still match the stated scope, expose its assumptions, avoid the placeholder form below, and remain Scratch until separately promoted.

**Family:** *recovery-graph / admissibility-dynamics* (same as parent). **Not** projection-erases-distinction.

---

## What this theorem says (one paragraph)

A path to a carrier does not imply recoverability. The recovery-path predicate has five clauses (`Admissible ∧ Timely ∧ Typed ∧ NonContagious ∧ CapacitySufficient`), and the absence of any one of them turns a graph-reachable carrier into not-actually-a-recovery-path. The theorem blocks the "graph exists, therefore resilience" laundering move: a system where every dying subsystem can be drawn an arrow to some non-exhausted node is *not* by that fact resilient; the arrows must carry all five clauses.

The doctrine sentence (from parent §Q7):

> `ReachableCarrier(src, carrier) ∧ ¬AdmissibleRecoveryPath(src, carrier) ⇒ ¬Recoverable(src, via carrier)`

where

```text
AdmissibleRecoveryPath(src, carrier) :=
  ReachableCarrier(src, carrier) ∧
  AdmissibleAtCarrier(carrier) ∧
  TimelyForSrc(carrier, src) ∧
  TypedForSrc(carrier, src) ∧
  NonContagiousEdge(src, carrier) ∧
  CapacitySufficient(carrier, src)
```

---

## Compile-probe scope statement (2026-05-30)

Three questions, three answers. They bound the claim and keep the probe honest. The [annex-probe queue](annex-probe-queue-2026-05-29.md)'s former five-criterion “license” is a historical quality/priority rubric, not a prerequisite supplied by a consumer.

### 1. What bounded question does the compile probe answer?

> Does the five-clause `AdmissibleRecoveryPath` predicate type-check as a kernel-level compositional joint — naming each clause as an abstract predicate, *not* discharging any of them — and does the reachability-insufficiency theorem follow as a non-trivial refusal of the "graph exists therefore resilience" move, *without* the kernel collapsing into either (a) the full `Surface`/`Trajectory` machinery or (b) a tautology of the form "if you have a recovery path, then you have a recovery path"?

Green confirms three things:

- The five clauses elaborate as a flat conjunction (no clause silently subsumed by another at type level).
- The two genuinely-new atoms — `TypedForSrc` (typed-capacity match) and `CapacitySufficient` (capacity bound, carrier renews faster than it exhausts) — are stateable as abstract predicates at the kernel layer without requiring numeric / typed-capacity machinery.
- The theorem `ReachableCarrier ∧ ¬AdmissibleRecoveryPath ⇒ ¬Recoverable` type-checks under an abstract `Recoverable` predicate where `Recoverable` is *not* defined as "there exists an `AdmissibleRecoveryPath`" — that would collapse the theorem into definitional unfolding. Instead, `Recoverable` is carried as an abstract predicate with a single **bridge axiom**: `Recoverable(src) → ∃ carrier, AdmissibleRecoveryPath(src, carrier)`. The contrapositive of the bridge axiom is the theorem.

Red surfaces two distinct gaps:

- If the only way to make the theorem type-check is to define `Recoverable` *as* "exists `AdmissibleRecoveryPath`", the theorem is a definitional unfolding and not a kernel-level refusal. The audit (parent §Q2(b)) flagged this directly: "the theorem becomes a one-liner trivially derived from definitions." That outcome counts as **gap, not green** — the kernel-level refusal claim hasn't been earned.
- If `Recoverable` cannot be stated abstractly without dragging in `Surface` / `Trajectory` machinery, the annex has crossed into the bounded-`Surface` debt category. See §3.

### 2. What is deliberately undischarged, and what carries the obligation?

Three layers, each undischarged for distinct reasons:

| Layer | Item | Undischarged because | Carried by |
|---|---|---|---|
| Atoms | `AdmissibleAtCarrier`, `TimelyForSrc`, `TypedForSrc`, `NonContagiousEdge`, `CapacitySufficient` | Five abstract predicates. Three (Admissible, Timely, NonContagious) have built-kernel cousins (`Authority`/`Derivation`, `Freshness`, `Conductance`); two (Typed, CapacitySufficient) are new atoms with no kernel cousin. The annex states them; it does not discharge or define them. | Downstream theory may later define them, and an NQ finding, Wicket classification, Governor verdict, or other consumer may supply concrete instances. Neither is permission to state the abstract kernel. Per `[[feedback-lean-debt-discipline]]`, the two new atoms are *vocabulary-deficient* claims and would get a `True`-placeholder if forced into definitional shape; the kernel form is *abstract predicates*, which is the honest carrier. |
| Bridge axiom | `Recoverable(src) → ∃ carrier, AdmissibleRecoveryPath(src, carrier)` | This is the **load-bearing axiom** of the slice. It says: any actual recovery has to factor through an `AdmissibleRecoveryPath`. The annex assumes this; it does not justify it. | Downstream theory that defines `Recoverable` in terms of trajectory / surface / state-transition machinery. The bridge axiom is the kernel's promise that any such definition will respect the five-clause structure. |
| `Recoverable` itself | `Recoverable : Subsystem → Prop` | Abstract predicate; no kernel definition. | The whole `Surface` / `Trajectory` machinery, OR an empirical-bridge consumer that provides observed instances. Either way, *not the annex.* |

**Anti-discharge discipline:** the annex must NOT provide any of:

- `Recoverable := ∃ carrier, AdmissibleRecoveryPath src carrier` — would collapse the theorem.
- `True`-placeholders for any of the five atoms — would launder kernel-level vocabulary-deficient gaps into apparent discharge.
- Concrete instances of `Subsystem` or example recovery graphs — would cross into linter territory (see §3).
- A `Decidable` instance for `AdmissibleRecoveryPath` — same reason.

### 3. Where does this annex stop being a slice probe and start being an architecture linter / a `Surface` retrofit — and is that boundary intentional?

The boundary is **two-sided** here, and both sides are load-bearing:

| Slice probe (in scope) | Architecture linter (out of scope) | `Surface` / `Trajectory` retrofit (out of scope) |
|---|---|---|
| State five abstract atom predicates | Decide them for a concrete recovery graph | Define them in terms of `Surface.feasible`, `SafetyTrajectory.lift`, etc. |
| State `Recoverable` and the bridge axiom | Provide a concrete `Recoverable` instance | Define `Recoverable` in terms of `Trajectory` / `Surface` machinery |
| Prove the theorem as the bridge axiom's contrapositive applied to a witness of the five-clause conjunction's negation | Run the theorem against an instantiated graph | Cite the theorem from `SafetyTrajectory.lean` or `Execution.lean` |
| Namespace under `Admissibility.ReachabilityInsufficiency`; no `LeanProofs.lean` import | Public-surface preprint claim, doctrine mint, CLI verdict | Import into existing `LeanProofs.lean` modules |
| No example architectures, no example carriers | Concrete examples | Concrete trajectory bindings |

**The two boundaries differ in kind:**

- *Linter* boundary is the same as CPI: deciding concrete instances belongs to a separate artifact.
- *`Surface` retrofit* boundary is new to this candidate: the temptation here is to "make `Recoverable` concrete by pulling in the trajectory machinery." That would (a) explode the annex's blast radius, (b) couple the candidate to specific kernel modules without an explicit interface mapping, and (c) make the bridge-axiom-as-load-bearing-discipline structurally invisible.

Crossing either line turns the candidate into a different artifact. If the build's natural slope pulls toward `Surface` retrofit, **stop and refile**. If it pulls toward linter decidability, **stop and refile**. The current probe's declared scope is the bridge-axiom-skeleton form; another coherent artifact may be formalized separately without waiting for a consumer.

### Why scope-first (not optional)

Parent §Q2(b) explicitly flagged: "the theorem becomes a one-liner trivially derived from definitions" if `Recoverable` is concrete-defined as five-clause existence. That outcome is the failure mode under test — it is the "is this composition discipline made explicit, or is it a kernel-level refusal" question from §Q7. Without this scope statement, the compile drifts:

- Drift mode A: define `Recoverable` concretely → theorem is `rfl`-shaped → no kernel-level refusal earned.
- Drift mode B: try to make atoms more concrete → couple to numeric / typed-capacity machinery → blast radius.
- Drift mode C: provide example graph instances → linter.

This statement holds the bridge-axiom-skeleton boundary that the queue's five-criterion test cannot hold alone.

### Recommended build session

A compile-probe session can proceed from the bounded statement itself:

1. Declare abstract types `Subsystem` (the only `Type` parameter).
2. Declare five abstract predicates as `Subsystem → Subsystem → Prop` or `Subsystem → Prop` per the audit's typing (TODO: confirm arities in §"Predicate typing details" below before drop).
3. Define `AdmissibleRecoveryPath` as the five-clause conjunction.
4. Declare `Recoverable : Subsystem → Prop` as an abstract predicate.
5. Declare the bridge axiom as an `axiom` (or, more honestly, as a hypothesis the theorem takes as an explicit argument — which avoids minting a kernel-level axiom and surfaces the assumption at the theorem's site).
6. Prove `reachability_insufficiency : ReachableCarrier src carrier ∧ ¬AdmissibleRecoveryPath src carrier ⇒ ¬Recoverable src` by contrapositive of the bridge hypothesis.
7. Confirm no Mathlib, no `LeanProofs.lean` import, no concrete `Subsystem` instance, no `Recoverable` definition, no `Decidable` instance.
8. `lake build LeanProofs.Admissibility.ReachabilityInsufficiency`. Green is contact; not promotion.
9. Update this note's §"Lean annex — built status" (new section) with the compile date, build time, and any deltas from the sketch.

The build should remain faithful to this statement. If the answers to §1–§3 above no longer match the candidate's actual shape, **rewrite the scope before claiming the result.** This is an intrinsic claim-shape check, not a forcing-case or runtime-consumer gate.

### Predicate typing details (drop-in skeleton, not yet a build)

Honest typing pass — to confirm before any compile:

```lean
-- Abstract subsystem space; no concrete instances.
variable (Subsystem : Type)

-- Five abstract atom predicates. Arities reflect parent §Q7.
variable (ReachableCarrier      : Subsystem → Subsystem → Prop)
variable (AdmissibleAtCarrier   : Subsystem → Prop)
variable (TimelyForSrc          : Subsystem → Subsystem → Prop)
variable (TypedForSrc           : Subsystem → Subsystem → Prop)
variable (NonContagiousEdge     : Subsystem → Subsystem → Prop)
variable (CapacitySufficient    : Subsystem → Subsystem → Prop)

-- The compositional joint.
def AdmissibleRecoveryPath (src carrier : Subsystem) : Prop :=
  ReachableCarrier src carrier ∧
  AdmissibleAtCarrier carrier ∧
  TimelyForSrc carrier src ∧
  TypedForSrc carrier src ∧
  NonContagiousEdge src carrier ∧
  CapacitySufficient carrier src

-- Abstract recoverability. NOT defined; carried by downstream.
variable (Recoverable : Subsystem → Prop)

-- Bridge hypothesis as theorem-local, NOT a kernel axiom.
theorem reachability_insufficiency
    (h_bridge :
      ∀ s, Recoverable s →
        ∃ c, AdmissibleRecoveryPath
                Subsystem ReachableCarrier AdmissibleAtCarrier
                TimelyForSrc TypedForSrc NonContagiousEdge
                CapacitySufficient s c)
    {src carrier : Subsystem}
    (_h_reach : ReachableCarrier src carrier)
    (h_notpath : ¬ AdmissibleRecoveryPath
                   Subsystem ReachableCarrier AdmissibleAtCarrier
                   TimelyForSrc TypedForSrc NonContagiousEdge
                   CapacitySufficient src carrier) :
    True := by trivial
    -- ^^^ PLACEHOLDER. The actual theorem statement needs the
    -- right quantifier shape over `carrier` — this is sketch,
    -- not the final form.
```

The skeleton above is **deliberately not a final theorem statement**. The honest theorem requires care about: (a) which `carrier` the conclusion quantifies over, (b) whether the bridge is "exists carrier" or "this specific carrier," (c) whether the negation of the path can be split per-clause for downstream consumers. Resolve them before claiming a final theorem; bounded Scratch compile probes may be used to discover and test the right shape.

### Open scope-statement questions (to resolve before claiming the intended theorem)

1. **Bridge axiom vs. theorem hypothesis.** If as an `axiom`, the annex mints a kernel-level claim about what `Recoverable` means. If as a theorem hypothesis, the assumption is surfaced at every callsite. The latter is the more honest form for a slice probe; the former is more convenient for downstream consumers. Default: **hypothesis form**, with a comment naming the axiom-form alternative.

2. **Per-source vs. per-pair quantification.** The audit's predicate is `AdmissibleRecoveryPath(src, carrier)` (per-pair). The bridge axiom is `Recoverable(src) → ∃ carrier, ...` (per-source). The theorem connects them: ¬path(src, carrier) for *this* carrier does not refute `Recoverable(src)` unless we know `carrier` is *the* carrier the bridge would produce. The honest form is: `¬ Recoverable(src) ↔ ∀ carrier, ¬AdmissibleRecoveryPath(src, carrier)`, with the theorem being one direction. Confirm this before build.

3. **Per-clause negation split.** Downstream consumers may want to refuse based on a *specific* missing clause (e.g., "the carrier is reachable, admissible, timely, typed, non-contagious, but capacity-insufficient — refused on capacity"). The theorem could expose per-clause refusal explicitly. Decision: **defer per-clause split to a separate theorem**, keep the master form clean.

4. **Should `AdmissibleRecoveryPath` be a `structure` instead of a conjunction?** The parent's empirical bridge for `ObservedNonRefinement` (see `ConsequencePartition.lean`) uses `structure` for empirical Type-level data. Reachability-insufficiency is `Prop`-level, so conjunction is correct. A later witness-carrying refinement may use a `structure`; it may be formalized before a concrete consumer if its own specification is coherent. Default: **conjunction for this theorem**, with the `structure` form kept as a separate refinement.

These four are intrinsic shape checks on top of the three §1–§3 questions. The intended theorem is honestly specified when all seven are answered consistently. Currently §1 has an answer; §2 has an answer; §3 has an answer; questions 1–4 above are *not yet answered* — only defaulted with notes. Scratch exploration may help answer them, but the `True` placeholder cannot testify as the claimed theorem.

---

## What this candidate does NOT claim

- **Not a definition of resilience.** The five clauses are necessary at the per-pair layer; resilience requires a per-source claim (at least one admissible recovery path exists) plus the desynchronization claim (no shared lock across sources). Both are out of scope here.
- **Not a graph-theoretic optimization.** The theorem says nothing about how to *increase* `AdmissibleRecoveryPath` density. Design discipline, not theorem.
- **Not a paper claim.** Per parent §Anti-goals: "NO promotion of the five candidate theorems to built status without per-candidate audit." This is the audit; the paper claim is still upstream.
- **Not a `Surface` retrofit.** Bridge axiom or hypothesis form; not coupled to existing kernel modules.
- **Not a deciders' specification.** Linter is a different artifact.

---

## Adjacent records

- Parent: [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md) (the doctrine source; this note is the scope-statement spinoff).
- Sibling scope statement: [control-path-independence-candidate-2026-05-29.md](control-path-independence-candidate-2026-05-29.md) §"Compile-probe scope statement (2026-05-30)" — same gate discipline.
- Built sibling (same family): `~/git/lean/LeanProofs/Admissibility/Conductance.lean` — covers `NonContagiousEdge`'s receiver-side hygiene; reachability-insufficiency's `NonContagiousEdge` clause is the per-edge specialization of the Conductance fragment's `¬ ContagionCapableEdge` shape.
- Queue: [annex-probe-queue-2026-05-29.md](annex-probe-queue-2026-05-29.md) §"Everything else: per-candidate audit, no sweep" — this candidate gets its own queue entry once the four open scope-statement questions are answered.

## Provenance

- **2026-05-30.** Spun out from desynchronized-horizons-candidate-2026-05-30.md as part of the annex-probe queue's "PL → CPI scope → Conductance → reachability-insufficiency scope → governor non-sovereignty deferred" cycle.
- Scope statement modeled on CPI's three-question form (§1 bounded question, §2 deliberately undischarged, §3 slice/linter boundary), extended with §"Open scope-statement questions" because reachability-insufficiency has more open shape decisions than CPI did at the same gate.

## Park state

> The scope statement is filed. The four open shape questions still prevent the placeholder skeleton from testifying as the intended theorem, but they do not impose “prose only”: Scratch formalization may be used to resolve them and may lead later code. Operator endorsement, a forcing case, and a runtime consumer are not prerequisites for that development.

Anti-sweep posture remains a custody rule, not a build-permission rule: each artifact must expose its own assumptions and scope; Scratch cannot mint doctrine, enter the public surface, or pin production merely because it compiles. Promotion and conformance require their own evidence.
