# Formalization Backfill Notes

A working journal of formalization deltas — what changed in the Lean stack, what paper-side updates are pending, what's deliberately out of scope. **This file captures deltas, it is not the backfill.** Canon backfill (cross-paper appendix updates, audit-doc reorganization) waits until the local paper cluster (P25–P27 currently) stops moving.

Working principle: *Write down what changed. Don't remodel the house while the concrete truck is still in the driveway.*

**Policy correction (2026-07-14):** Entries below were written across an earlier workflow and sometimes use *forcing case*, *live consumer*, or *downstream theorem* as if consumers admitted formal work. That rule is superseded. Formalization may precede and lead implementation. Theorem shape, stable semantics, overlap, proof, and anti-vacuity govern formal development; promotion is a separate custody/compatibility decision; runtime conformance requires an explicit mapping plus evidence or refinement. Citation alone is not conformance. Historical wording is retained only where the history itself matters and is annotated accordingly.

## Status taxonomy

Restrained vocabulary, used per-paper to avoid inflating everything into "formally proved":

| Status | Meaning |
|---|---|
| **No Lean support** | No formal artifact. Prose stands alone. |
| **Local lemma support** | One or two specific algebraic shards, not the spine. |
| **Formal model fragment** | A coherent piece of the paper formalized; other pieces remain prose. |
| **Formal spine** | The structural-refusal core or load-bearing claims formalized; quantitative or constructive layers remain open. |
| **Companion model** | Full formalization at the model layer; sim/empirical layer separately reproducible. |

Canon docs (`PAPER-MAP.md`, `CLAIM-REGISTER.md`, `docs/formalization-index.md`) currently use a richer cashout-class vocabulary (certify / sharpen / expose looseness / bridge artifact). The taxonomy here is the lighter status summary — appropriate for journal entries, not for full audit-doc edits.

---

## Per-paper deltas

### P15 — *Cybernetic Fault Domains*

**Lean status:** Formal spine. `TaxonomyGraph.lean` (primary), `BranchSelector.lean` (secondary).

**Paper updates pending:** None currently. Closure topology and three-terminal-families result are reflected in working notes; no v1.1 push planned beyond what's already noted in `formalization-index.md`.

**Out of scope (intentional):** Temporal-attractor framing of Δh; role-label semantic correctness beyond structural coherence; edge-weight or directionality completeness.

---

### P18 — *Unauthorized Durability*

**Lean status:** Formal spine. `PersistenceModel.lean` (primary), `BranchSelector.lean` (secondary). Five-state dynamics, three-way recovery distinction, seven verified invariants.

**Paper updates pending:**
- Appendix A drafted 2026-04-20; not yet pushed to Zenodo. Verify appendix language still matches current Lean scope before push (spot-checked 2026-05-03 — appears current).
- Mark dynamic-claims roadmap memory as "shipped, not queued" — DONE 2026-05-03.

**Out of scope (intentional):** Pre-breach dynamics; observer-integrity modeling; tier-escalation paths; empirical capacity-decrement calibration.

---

### P22 — *No Universal Plant Clock*

**Lean status:** Local lemma support. `PersistenceModel.lean` `persistence_normalizes` axiom serves as the static/temporal boundary marker for P22's scope-fence discipline. §6.4 paragraph already acknowledges this.

**Paper updates pending:**
- Source `metadata.yaml` shows `version: "0.9"`; v1.1 push to Zenodo pending. Per `formalization-index.md`, requires bumping metadata and rebuilding PDF.
- §6.4 paragraph still accurate against current stack (spot-checked 2026-05-03).

**Potential next formal target:** Four-layer ratio admissibility / threshold violation. P22 §4 introduces ratios `T_o/T_p`, `T_u/T_p`, `(T_o+T_u)/T_p`, `T_s/T_p`, `T_contract/T_c` with critical thresholds. A Lean theorem of shape *"a system is temporally admissible only if all four layer ratios remain within bound; one layer violation suffices to deny global admissibility"* is reachable. Would change math flavor (arithmetic / ratio thresholds) from the current kernel/observability lane. **Scheduling hold until P25–P27 settle** per the cluster-stability discipline; this is prioritization, not a consumer or paper-promotion prerequisite.

**Out of scope (intentional, current):** Empirical calibration of threshold values; cross-domain ratio inventory beyond the worked examples.

---

### P23 — *Ops Is Control with a Non-Self-Identical Controller*

**Lean status:** Formal model fragment. `OpsMasking.lean` covers case (i) projection masking, exact. Cases (ii) (measurement null-space, first-order) and (iii) (local gain aliasing, ε-resolution) remain paper-level.

**Paper updates pending:** None currently. P23 v1.0 published 2026-04-24 with formalization status block already accurate.

**Potential next formal target:** Case (ii) measurement null-space masking. *Hold-for-later* per ChatGPT's pushback (2026-05-03): formalizing case (ii) keeps the work inside the P25/P23 null-space corridor and risks cathedral-mode. Better next move is P22 ratios for flavor change.

**Out of scope (intentional, current):** Cases (ii), (iii); gate-state-indexed projection $\Pi_{A_t}$ (current Lean uses fixed `proj : U → U`).

---

### P24 — *Shared Vision as Coordinating Prior*

**Lean status:** Formal model fragment. `Paper24SharedVision.lean` covers §4 metric algebra and Theorems 3–4 kernels (algebraic shard discipline — "stupid on purpose"). Companion sim `shared_vision.py` covers the §4 probes.

**Paper updates pending:**
- Proposition 2 sign correction. Lean caught: formal pairwise difference is `(φᵢ − φⱼ)·V`; paper statement currently has the opposite sign. Metric claims unaffected. Candidate prose correction in any v1.1 push.
- v1.0 already published 2026-04-28; Lean shard landed same day.

**Potential next formal target:** Proposition 1 (no-scalar-free-lunch) — the single highest-value future Lean target. Moving from probe-backed conjecture to theorem requires fixing the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?). **Scheduling hold until P25–P27 settle; the unresolved aggregator class is the intrinsic theorem-shape gate.**

**Out of scope (intentional):** Conjecture 1 / Proposition 1 (current); agile case study; closed-loop dynamics; witness-filter institutional prose; aggregator-in-the-abstract operator theory.

---

### P25 — *Epistemic Border Control as Proxy Regulation Under Partial Observability*

**Lean status:** Formal spine. `Paper25EpistemicBorderControl.lean` (added 2026-05-03). Five theorems: row-replication operator; kernel preservation under stacking; Gramian scaling identity; observation-equivalence implies policy-equivalence; target-distinct-but-policy-same corollary (with intentionally-unused target hypothesis).

**Paper updates pending:**
- §5 clarifying paragraph added 2026-05-03 (subspace-vs-vector precision; explicit Gramian identity; companion-Lean pointer). Landed in v0.1 draft body.
- v0.1 → Zenodo push deferred per drafting-vs-publishing discipline; possibly waits for P27 to congeal in case downstream phrasing affects which §-level claims are load-bearing.

**Out of scope (intentional):**
- Proposition 1 quantitative substitution scaling (paper-marked open).
- Closed-loop dynamics, Kalman, LQR (cathedral risk; ChatGPT fence).
- Explicit `obsMatrix A C T` as a single matrix object (mechanical instantiation; current abstract `replicateRows N M` carries the load-bearing claim).
- SVD / least-observable-direction quantitative claims (Mathlib coverage limited).

**Future polish (eventually, not urgently):** Sharpen the `target_distinct_policy_same` docstring so the trivial `rw [hObs]` proof isn't misread as empty. Suggested language (ChatGPT, 2026-05-03): the trivial proof *is* the theorem's content — once the policy is defined only over observations, observation-equivalence is sufficient for policy-equivalence; the unused target-distinction hypothesis marks the structural refusal, not a missing proof obligation. Hold until P25-P27 cluster settles per the notes-now-backfill-later discipline.

---

### P26 — *Premature Commitment and Belated Consequence (candidate)*

**Lean status:** No Lean support. Scaffold only.

**Paper updates pending:** Empty-window promotion gate material added to `NOTES.md` 2026-05-03 (four-type taxonomy: natural-latency / procedural / manufactured / ontological; four-condition promotion test). Status: candidate gate material, not promoted into draft. Gating decision still deferred.

**Out of scope (intentional):** No Lean formalization is currently scheduled because the candidate's curve semantics and theorem boundary are not settled. Paper promotion is not a prerequisite: a coherent `m(t)/c(t)` formalism may precede and lead later prose or implementation once its statement and anti-vacuity controls are clear.

---

### P27 — *Obligation-Unsound Reconciliation (published v1.0 2026-05-18)*

**Lean status:** Local lemma support. `Admissibility.lean` skeleton sorry-free as of 2026-05-01: three real proofs against the local `admissible` definition (`unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`); two `True`-placeholder discharges with deferred-real-statement docstrings (pending substrate-accusation / causal-binding predicates). Intentionally unwired into `LeanProofs.lean` umbrella — sorry-elimination does not imply wiring. Paper §8 explicitly scopes Lean as local accounting core; distributed admissibility, three-horizon durability, and non-subordination constraint are carried by the paper model.

**Paper updates pending:** None — v1.0 published 2026-05-18, DOI `10.5281/zenodo.20275071`. Future v1.1 candidates: TLA-disjointness one-liner in §2; abstract sentence adding non-subordination alongside the three-horizon framing; §5 table footnote distinguishing kernel-`openFinding` from deferred-eligible predicates.

**Discipline note:** Do not mint vocabulary merely to make placeholders look substantive. The `True` placeholders are deliberate; "kill the sorrys, don't let the sorrys design the constitution" remains the active rule. Formalization may lead code, but each predicate still needs stable semantics and a non-vacuous theorem-shaped use. Worked cases can test that shape; they do not grant permission. The two predicates (`substrateAccusation`, `receiptOutlives`) had two pressure specimens but were not promoted in v1.0 because no stable composing statement had yet distinguished them from constitution-by-typechecker.

**Out of scope (intentional):** Concrete substrate-accusation and causal-binding predicates (deferred until their semantics and a non-vacuous composing theorem are precise); wiring into `LeanProofs.lean` (a separate promotion decision after the predicates land).

---

### Admissibility kernel (no paper anchor)

**Lean status:** Companion model — five modules (`Authority` / `StateTransition` / `Derivation` / `Execution` / `Corrective`) under `LeanProofs/Admissibility/`. `lake build` green, no `sorry`. Companion working note: `working/admissible-recovery-semantics.md`.

**Paper updates pending:** No paper anchored yet. Slot decision (P27 fold-in vs standalone P28) deferred per `working/admissible-recovery-semantics.md` §8.

**Out of scope (intentional):** Concrete `claimForStep` resolvers (the abstract kernel intentionally leaves policy open; a formal instance may precede Governor code once resolver semantics are selected); `AuthorityClaim` schema commitments (kept abstract). Governor remains a correspondence target, not a prerequisite.

---

### AxisSkew — directional comparison kernel (added 2026-05-20)

**Lean status:** Formal model fragment. `LeanProofs/Admissibility/AxisSkew.lean`. `lake build` green, no `sorry`. Three theorems:

1. `not_lagging_and_leading_same_axis` — classification is functional; no single (prior, observed) pair is both lagging and leading.
2. `classify_self` — comparing a value to itself classifies as `matched`, given irreflexivity at that point.
3. `reverse_lagging_is_leading` — swapping (prior, observed) argument order swaps lagging ↔ leading; the classification is orientation, not verdict (requires asymmetry of the supplied relation).

The comparison relation is consumer-supplied; the kernel keeps the underlying order opaque so partial, preorder, lattice, and total orderings can each be its argument. No `ClaimAxis` enum in kernel.

**Companion working primitive:** `working/primitives/memory-skew.md` (candidate, Kind: Axis). Operator-facing application; carries the five candidate axes (recency / completeness / authority / capability / integration) which are explicitly not kernel-pinned.

**Formal residue:** Stale Binding is the substrate-rich primitive for the *lagging direction* (caches, hat-x estimates, briefings, P23–P27). The *leading direction* — prior overclaims observed state — had no equivalent general primitive before this. Time-axis bidirectional was already in `Freshness.lean` (NotYetValid / Expired). The new module supplies the substrate-general bidirectional kernel.

**Discipline note:** This module is the *positive* counterpart to the AWP audit's null result two days prior. Same gate (kernel-overlap audit before any new module), opposite outcome — the audit surfaced residue that did *not* collapse into existing substrate. Specifically the leading direction generally + the orientation theorem (reverse_lagging_is_leading) had no formal home. Strict scope discipline applied throughout: no `ClaimAxis` enum, no `Corrective` import, no operational authorization theorem, no calculus naming.

**Out of scope (intentional):**
- Five-axis `ClaimAxis` enum (operator-facing taxonomy, lives in `memory-skew.md` not kernel).
- Operational bridge theorem *"lagging may support correction, not authorize mutation"* — would compose with `Corrective` / `Authority`; deferred until the bridge hypotheses and non-overlap claim are precise. A live consumer may test correspondence but is not required.
- Symmetric leading-direction bridge *"leading may support refusal of binding, not authorize forward mutation"* — same theorem-shape deferral.
- Subsumption of Stale Binding into AxisSkew (parallel relationship preserved; stale-binding's consequence-window machinery is substrate detail the kernel does not absorb).
- Trichotomy theorem in cleaner LinearOrder form — held because the current orientation theorems cover the selected formal scope; it may be added on intrinsic theorem value without waiting for a consumer.

---

### AuthorizedNotSafe — Phase 1 frontier specimen for Admissibility ≠ Safety Bridge (added 2026-05-24)

**Lean status:** Formal model fragment. `LeanProofs/Admissibility/AuthorizedNotSafe.lean`. Root-wired via `LeanProofs.lean`. `lake build` green, no `sorry`. One theorem (`authorized_not_safe`): exhibits a `StepAllowed` witness and a `Nat`-valued defended-value function such that the defended value strictly decreases across the authorized step. `WHAT-THE-LEAN-STACK-PROVES.md` updated with the non-claim disclosure.

**Scope clause:** Wound is at the `StepAllowed` layer only. The full `AuthorizedStep` structure (Execution.lean) requires both `stepAllowed` and a claim-side `stepAuthorityVerdict = authorized` witness, so its inhabitants form a *subset* of `StepAllowed`'s; a witness at the superset does not, on its own, exhibit one at the subset. Transfer to `AuthorizedStep` is explicitly *not settled* by this file.

**Consistency caveat:** The two value axioms (`defendedValue_initial = 1`, `defendedValue_after = 0`) jointly imply `scenarioState ≠ applyStep scenarioState scenarioStep`; the 1.0 surface does not establish this distinction either way. The file is therefore an *axiomatically-inhabited counter-scenario*, not a concrete model. A witnessing model (e.g. `EvidenceStore := List Receipt`, `appendEvidence := cons`) is straightforward but unwitnessed here.

**Companion working notes (papers repo):**

- `working/kernel-to-body-map.md` — dependency-ordered slice inventory; Slice A houses Phase 1.
- `working/calculus-2-exit-criteria.md` — six conditions under which "Calculus 2.0" is a thing that exists, under this map.
- `working/frontier-proof-obligations.md` — five-step proof pattern and per-frontier ledger.

These remain working orientation, not a 2.0 roadmap commitment.

**Deferred questions:**

1. Can the wound be made concrete rather than axiom-backed (e.g. `AuthorizedNotSafeConcrete.lean` with `EvidenceStore := List Receipt`)?
2. Does the wound lift cleanly from `StepAllowed` to full `AuthorizedStep`?
3. What minimal safety predicate, if any, does the specimen actually force — strict ≥ / bounded loss / recoverable loss / no irreversible loss / no loss without receipt / no loss to protected class?
4. What extra hypotheses would a future safety bridge have to carry (analogue of `Corrective.RecoveryEnv`)?

**Discipline note:** Phase 1 is intentionally one file. The map does not itself supply theorem statements or hypotheses for `DefendedValue.lean`, `SafetyPreserving.lean`, `SafetyEnv` bundles, or `SafetyBridge.lean`; each requires its own intrinsic review. Root-wired means build-covered; it does not mean public-surface-promised. `CalculusOne.lean` and the 1.0 compatibility surface remain untouched.

**Out of scope (intentional):**

- `AuthorizedStep`-layer wound construction (would require axiomatizing `ExecutionEnv` + verdict witness; deferred).
- Concrete witnessing model `AuthorizedNotSafeConcrete.lean` (would reduce axiom budget; currently a low-priority scope choice, not blocked on a challenger or consumer).
- Any Slice A bridge work (`DefendedValue`, `SafetyPreserving`, `SafetyEnv`, `SafetyBridge`); the Phase 1 stop sign holds until the bridge statement and its necessary hypotheses are selected.
- Slice B/C/D modules; each requires its own theorem-shape, overlap, proof-scope, and anti-vacuity review. None requires a runtime forcing case.

---

### Adversarial Witness Protocol — kernel-overlap audit (no module warranted)

**Lean status:** No new Lean support. AWP working note at `working/adversarial-witness-protocol.md` is a protocol-level articulation of existing no-attribution and witness-discipline kernels; no new module added.

**Audit performed:** 2026-05-19. Three proposed Lean claims tested against `FiatAdmissibility`, `PublicReceiptRefinement`, `WitnessInvariance`, `SurfaceAuthorization`:

1. *Observation can refute declared operational consistency* — collapsed into existing artifact-classification substrate (`FiatAdmissibility.classify` already refuses spurious support claims by artifact kind). Observational variant would be bare modus tollens, no kernel content beyond schema-as-prose.
2. *Refutation does not imply causal attribution* — **already directly covered** by `CollapsedSurface.collapsed_surface_not_identified` + `PublicReceiptRefinement.refines_without_identification` + `SurfaceAuthorization` keeper line (*"A collapsed surface may authorize inquiry. It may not authorize attribution."*). This is the strongest finding: AWP's §0 motive-claim guardrail is the prose articulation of theorems the kernel has carried since Paper 25 / CollapsedSurface landed.
3. *A witness artifact cannot certify legitimacy without changing type* — enforced by structural type discipline (no `Witness → Verdict` constructor anywhere in the kernel). Not theorem-shaped; Lean's type system carries this without explicit statement.

**Candidate handles surfaced — held as named-not-promoted:**

- *Advance tombstone / pre-committed voluntary admissibility revocation* — sibling to admissibility-decay family. It remains held because no non-redundant theorem shape has yet survived the overlap audit; further recurrence may sharpen that shape but is not permission to formalize.
- *Aggregation-as-authority-laundering* — `ContradictionLog ↛ HealthScore` is consumer-side prohibition (doctrinal-rule shape), not kernel claim. Lean can refuse to provide such a constructor but cannot prevent downstream consumers from writing one. Hold.

**Discipline note:** This audit is the kernel-overlap-audit memory rule (`feedback-kernel-overlap-audit`) working as designed. The closure-standing precedent (2026-05-14, ~30k words collapsed into existing substrate) is the cautionary scar; the AWP case is the same shape at smaller scale. AWP's structural residue is zero modules; the doctrine residue lives in the working note. Tiny goblin version per the working note: *AWP is not a tool. It is a refusal pattern with YAML tendencies.*

**Out of scope (intentional):** `ObservedDecoupling.lean` (would be true-but-redundant); `Tombstone.lean` (no non-redundant theorem shape has survived the overlap audit; the single instance is weak promotion evidence but not a permission gate); aggregation-as-laundering theorem (not kernel-shape, deferred); docstring cross-references inside `SurfaceAuthorization.lean` or `CollapsedSurface.lean` (held — risk of staple-receipt-to-receipt without future-reader benefit).

---

## Change log

- **2026-05-03** — File created. Initial seed entries for P15, P18, P22, P23, P24, P25, P26, P27, and the Admissibility kernel. Captures current deltas after P25 Lean spine completion. Subsequent entries land here as deltas accumulate; canon backfill (per-paper appendix updates, audit-doc reorganization) deferred until P25–P27 cluster stabilizes.
- **2026-05-19** — AWP kernel-overlap audit entry added. Null result: no new module warranted. AWP backed by existing CollapsedSurface / PublicReceiptRefinement / SurfaceAuthorization theorems. Two candidate handles (advance tombstone, aggregation-as-authority-laundering) held as named-not-promoted.
- **2026-05-20** — `AxisSkew.lean` added. Three theorems, lake build green. First positive Lean addition since the AWP-audit null result two days prior — same audit gate, opposite outcome. Companion primitive `memory-skew.md` filed as candidate (Kind: Axis); parallel-not-subsumed relationship with Stale Binding preserved.
- **2026-05-24** — `AuthorizedNotSafe.lean` added. Phase 1 frontier specimen for `FRONTIERS.md` Frontier 1 (Admissibility ≠ Safety Bridge). Negative model at the `StepAllowed` layer; `AuthorizedStep`-layer transfer explicitly deferred; axiomatically-inhabited counter-scenario (concrete witnessing model deferred). Three orientation notes filed in papers `working/` (kernel-to-body map, calculus-2 exit criteria, frontier proof obligations). The then-current staging note said no Slice A bridge work was licensed by this landing; under the corrected policy, the operative hold is the absence of selected bridge statements and hypotheses, not a missing consumer.
- **2026-07-14** — Formalization-first policy correction applied. Earlier consumer/forcing-case gates are historical, not operative: formal development may lead code; promotion and runtime conformance remain separate; intrinsic theorem-shape, overlap, proof, and anti-vacuity controls remain in force.
