# Formalization Backfill Notes

A working journal of formalization deltas — what changed in the Lean stack, what paper-side updates are pending, what's deliberately out of scope. **This file captures deltas, it is not the backfill.** Canon backfill (cross-paper appendix updates, audit-doc reorganization) waits until the local paper cluster (P25–P27 currently) stops moving.

Working principle: *Write down what changed. Don't remodel the house while the concrete truck is still in the driveway.*

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

**Potential next formal target:** Four-layer ratio admissibility / threshold violation. P22 §4 introduces ratios `T_o/T_p`, `T_u/T_p`, `(T_o+T_u)/T_p`, `T_s/T_p`, `T_contract/T_c` with critical thresholds. A Lean theorem of shape *"a system is temporally admissible only if all four layer ratios remain within bound; one layer violation suffices to deny global admissibility"* is reachable. Would change math flavor (arithmetic / ratio thresholds) from the current kernel/observability lane. **Held until P25–P27 settle** per the cluster-stability discipline.

**Out of scope (intentional, current):** Empirical calibration of threshold values; cross-domain ratio inventory beyond the worked examples.

---

### P23 — *Ops Is Control with a Non-Self-Identical Controller*

**Lean status:** Formal model fragment. `OpsMasking.lean` covers case (i) projection masking, exact. Cases (ii) (measurement null-space, first-order) and (iii) (local gain aliasing, ε-resolution) remain paper-level.

**Paper updates pending:** None currently. P23 v1.0 published 2026-04-24 with formalization status block already accurate.

**Potential next formal target:** Case (ii) measurement null-space masking. *Hold-for-later* per chatty's pushback (2026-05-03): formalizing case (ii) keeps the work inside the P25/P23 null-space corridor and risks cathedral-mode. Better next move is P22 ratios for flavor change.

**Out of scope (intentional, current):** Cases (ii), (iii); gate-state-indexed projection $\Pi_{A_t}$ (current Lean uses fixed `proj : U → U`).

---

### P24 — *Shared Vision as Coordinating Prior*

**Lean status:** Formal model fragment. `Paper24SharedVision.lean` covers §4 metric algebra and Theorems 3–4 kernels (algebraic shard discipline — "stupid on purpose"). Companion sim `shared_vision.py` covers the §4 probes.

**Paper updates pending:**
- Proposition 2 sign correction. Lean caught: formal pairwise difference is `(φᵢ − φⱼ)·V`; paper statement currently has the opposite sign. Metric claims unaffected. Candidate prose correction in any v1.1 push.
- v1.0 already published 2026-04-28; Lean shard landed same day.

**Potential next formal target:** Proposition 1 (no-scalar-free-lunch) — the single highest-value future Lean target. Promoting from probe-backed conjecture to theorem requires fixing the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?). **Held until P25–P27 settle.**

**Out of scope (intentional):** Conjecture 1 / Proposition 1 (current); agile case study; closed-loop dynamics; witness-filter institutional prose; aggregator-in-the-abstract operator theory.

---

### P25 — *Epistemic Border Control as Proxy Regulation Under Partial Observability*

**Lean status:** Formal spine. `Paper25EpistemicBorderControl.lean` (added 2026-05-03). Five theorems: row-replication operator; kernel preservation under stacking; Gramian scaling identity; observation-equivalence implies policy-equivalence; target-distinct-but-policy-same corollary (with intentionally-unused target hypothesis).

**Paper updates pending:**
- §5 clarifying paragraph added 2026-05-03 (subspace-vs-vector precision; explicit Gramian identity; companion-Lean pointer). Landed in v0.1 draft body.
- v0.1 → Zenodo push deferred per drafting-vs-publishing discipline; possibly waits for P27 to congeal in case downstream phrasing affects which §-level claims are load-bearing.

**Out of scope (intentional):**
- Proposition 1 quantitative substitution scaling (paper-marked open).
- Closed-loop dynamics, Kalman, LQR (cathedral risk; chatty fence).
- Explicit `obsMatrix A C T` as a single matrix object (mechanical instantiation; current abstract `replicateRows N M` carries the load-bearing claim).
- SVD / least-observable-direction quantitative claims (Mathlib coverage limited).

**Future polish (eventually, not urgently):** Sharpen the `target_distinct_policy_same` docstring so the trivial `rw [hObs]` proof isn't misread as empty. Suggested language (chatty, 2026-05-03): the trivial proof *is* the theorem's content — once the policy is defined only over observations, observation-equivalence is sufficient for policy-equivalence; the unused target-distinction hypothesis marks the structural refusal, not a missing proof obligation. Hold until P25-P27 cluster settles per the notes-now-backfill-later discipline.

---

### P26 — *Premature Commitment and Belated Consequence (candidate)*

**Lean status:** No Lean support. Scaffold only.

**Paper updates pending:** Empty-window promotion gate material added to `NOTES.md` 2026-05-03 (four-type taxonomy: natural-latency / procedural / manufactured / ontological; four-condition promotion test). Status: candidate gate material, not promoted into draft. Gating decision still deferred.

**Out of scope (intentional):** Lean formalization deferred until paper promotes from candidate. Kernel `m(t)/c(t)` curve formalism would be possible but premature.

---

### P27 — *Obligation-Unsound Reconciliation (candidate)*

**Lean status:** Local lemma support. `Admissibility.lean` skeleton sorry-free as of 2026-05-01: three real proofs against the local `admissible` definition; two `True`-placeholder discharges with deferred-real-statement docstrings (pending substrate-accusation / causal-binding predicates). Intentionally unwired into `LeanProofs.lean` umbrella — sorry-elimination does not imply wiring.

**Paper updates pending:** P27 is candidate/scaffold. Substantive work happens in working notes; preprint paper.md not yet drafted.

**Discipline note:** Do not vocabulary-design through Lean until worked cases force the predicates. The `True` placeholders are deliberate; "kill the sorrys, don't let the sorrys design the constitution" is the active rule.

**Out of scope (intentional):** Concrete substrate-accusation and causal-binding predicates (deferred until P27 working notes force them); wiring into `LeanProofs.lean` (deferred until predicates land).

---

### Admissibility kernel (no paper anchor)

**Lean status:** Companion model — five modules (`Authority` / `StateTransition` / `Derivation` / `Execution` / `Corrective`) under `LeanProofs/Admissibility/`. `lake build` green, no `sorry`. Companion working note: `working/admissible-recovery-semantics.md`.

**Paper updates pending:** No paper anchored yet. Slot decision (P27 fold-in vs standalone P28) deferred per `working/admissible-recovery-semantics.md` §8.

**Out of scope (intentional):** Concrete `claimForStep` resolvers (deferred to Governor instantiation); `AuthorityClaim` schema commitments (kept abstract).

---

## Change log

- **2026-05-03** — File created. Initial seed entries for P15, P18, P22, P23, P24, P25, P26, P27, and the Admissibility kernel. Captures current deltas after P25 Lean spine completion. Subsequent entries land here as deltas accumulate; canon backfill (per-paper appendix updates, audit-doc reorganization) deferred until P25–P27 cluster stabilizes.
