# Formalization Index

Canonical crosswalk between the preprint series and the Lean formalization work.

Paper-side view lives here. Module-side view lives in the Lean repo at `PAPER-MAP.md`. Claim-level audit (with BROKEN / STALE / SOUND / OPEN status per specific prose location) lives in the Lean repo at `CLAIM-REGISTER.md`. Module-level exposition of what's proved and what each proof kills lives in the Lean repo at `WHAT-THE-LEAN-STACK-PROVES.md`.

This file is the bridge object. It tells you, for any paper, whether Lean has produced a warrant upgrade and what kind.

## Source of truth and reader's entry point

The Lean repository at `~/git/lean` (public: <https://github.com/unpingable/lean>) is the canonical formal source. Citations in this index point at module paths and theorem/declaration names within that repo, not at rendered HTML or doc-gen4 output. The Lean repo's own `README.md`, `PAPER-MAP.md`, `CLAIM-REGISTER.md`, and `WHAT-THE-LEAN-STACK-PROVES.md` together form the human-readable proof reader's portal — currently surfaced at <https://unpingable.github.io/lean/> via classic GitHub Pages rendering of the README. Generated doc-gen4 API HTML is not part of that portal today; if it is added later it will sit as a secondary reference layer beneath the human-readable index, not as the front door. Identifier-drift between this index and the Lean source is checked by `tools/formalization_crosswalk.py`.

## Stable identifiers

- `P{N}` — preprint number (e.g., `P18`)
- Lean modules in `~/git/lean/LeanProofs/`:
    - Paper-anchored: `TaxonomyGraph.lean`, `BranchSelector.lean`, `PersistenceModel.lean`, `OpsMasking.lean`, `Paper24SharedVision.lean`, `Paper25EpistemicBorderControl.lean`
    - No paper anchor: `RepairOperator.lean`
    - P27 anchored (sorry-free as of 2026-05-01, intentionally unwired; paper v1.0 published 2026-05-18 DOI `10.5281/zenodo.20275071`): `Admissibility.lean`
    - Infrastructure substrate kernel: `Admissibility/Authority.lean`, `Admissibility/StateTransition.lean`, `Admissibility/Derivation.lean`, `Admissibility/Execution.lean`, `Admissibility/Corrective.lean`
- Lean modules in `~/git/babyriver/lean/BabyRiver/` are kernel modules for Phase 1 population dynamics

## Cashout classes

Following the distinction used when deciding whether a paper revision is warranted:

1. **Certify** — Lean proves a claim the paper already makes. Appendix or footnote; no content change.
2. **Sharpen** — Lean narrows, constrains, or corrects a prose claim. Content change; reframed sentence or subsection.
3. **Expose looseness** — Lean shows the prose was doing multiple jobs in one sentence. Defensive maintenance; prose revision.
4. **Bridge artifact** — Lean creates a clean prose → formal statement → proof path. Reader navigation upgrade; usually pairs with one of the other classes.

## Formalized vs paper-ready

*Formalized* means a Lean theorem exists for the claim. *Paper-ready* means the prose-to-formal mapping is clean enough to cite without interpretive fog. A claim can be formalized without being paper-ready — that's why this index tracks both.

## Versioning convention

- **Appendix note** — no DOI bump; prose remains as-is, formalization noted in an appendix or footnote.
- **v1.1 / v1.2** — minor version bump on Zenodo. Prose sharpened or a slogan corrected, but the paper's main claims are unchanged in structure.
- **v2.0** — major version bump. Reserved for cases where the formalization changed what the paper is saying at the level of its abstract. Rare.

ChatGPT's pushback (2026-04-19): calling a revision "v2.0" oversignals rupture when the underlying move is sharpening + correction. Default to v1.x unless the abstract itself has to change.

### Lean-repo / scratch versioning (distinct from the paper-DOI bumps above)

The section above is **paper** versioning (Zenodo DOI). The **Lean repo** (`AdmissibilityKernels`) versions separately, keyed to **public theorem surface, not amount of work** (operator, 2026-06-14; full policy in memory `project-admissibility-kernels-versioning`):

- **patch** — docs / specimen / audit corrections; no new public theorem.
- **minor** — new public annex / theorem family; compatible vocabulary.
- **major** — shared foundation vocabulary minted, or the public claim frame changes.

> **Doctrine: scratch can be indexed and committed; only wired/public theorem surfaces version the repo.**

So the entire 2026-06-14 scratch run logged below (temporal no-go packet, observer foundation incl. `ConsumerRelativeVerdict`, deadlock/escalation/sharded-custody, `QuorumCustody`) is **NO repo bump** — all `SCRATCH`, none wired into `LeanProofs.lean`, no public module, no claim-register promotion. Internal recovery tag (e.g. `scratch-2026-06-14`) only if wanted, never semver. Graduation ladder when/if wired: temporal annex → v1.1.0; observer generic annex → v1.2.0; observer foundation module / shared `Consumer→Artifact→Verdict` vocabulary → v2.0.0 candidate (gated by the vocabulary-foundation subgate + the parked noun decision).

---

## Tier 1 — Strongest cashout

### P18 — *Unauthorized Durability*

- **Lean modules:** `PersistenceModel.lean` (primary), `BranchSelector.lean` (secondary, for closure-family selection context)
- **Cashout classes:** 2 (sharpen) + 4 (bridge artifact)
- **Paper-ready:** Yes. `PersistenceModel.lean` is the formalization of Paper 18's central mechanism.
- **Revision candidacy:** *v1.1 candidate — Appendix A drafted in local source 2026-04-20; not yet pushed to Zenodo.* Paper is published v1.0 on Zenodo (March 10, 2026). Appendix A uses a fixed four-field per-claim structure (formal object / prose claim sharpened / what it does not prove / repo pointer). Abstract, introduction, and conclusion untouched. v1.2 deferred — that would be the move if "cumulative commitment, not duration" and "recovery is restructuring" are promoted into the abstract or key contributions list.

**What Lean underwrites:**

- **Detached commits (not idle time) burn rollback capacity.** Sharpens what "unauthorized durability" actually costs. Paper prose can drop any "long enough" framing in favor of cumulative-commitment framing.
- **Episode recoverability ≠ lifetime recoverability.** Individually-recoverable detachment episodes accumulate into irrecoverability. This is implicit in Paper 18 but not formally stated; Lean makes it explicit.
- **Hysteretic is absorbing for internal events.** Lock-in is machine-verifiable; no internal reattach exits hysteretic.
- **External repair produces RESTRUCTURED, not ALIGNED.** Novel claim. Not in Paper 18's prose. Repair restores operability without restoring resilience. Candidate for its own subsection.
- **Restructured systems can fail again, faster.** Second-chance with reduced budget. Also novel relative to Paper 18's prose.
- **Three-way recovery taxonomy:** internally recoverable / externally repairable / locked in.

### P15 — *Cybernetic Fault Domains*

- **Lean modules:** `TaxonomyGraph.lean` (primary), `BranchSelector.lean` (secondary)
- **Cashout classes:** 2 (sharpen) + 3 (expose looseness)
- **Paper-ready:** Yes. The paper already claims "37 verifiable claims" in the enforcement kernel; Lean is a natural extension of that verification-forward posture.
- **Revision candidacy:** v1.1 with a "Formal Verification" subsection.

**What Lean underwrites:**

- **Terminal set exactness (exactly 4: Δg, Δa, Δx, Δh).** Certifies the closure taxonomy.
- **Three terminal families, not one.** Reorganizes the structural view. Δs/Δm → gain/actuation; Δk → scale; Δw/Δc/Δe → hysteresis; branching precursors reach both gain/actuation and hysteresis.
- **"Δh is the universal sink" falsified as pipeline reachability.** Δs and Δk cannot reach Δh through any pipeline path. See `CLAIM-REGISTER.md` entry #1; priority rewrites 1-4 already applied to taxonomy working notes on 2026-04-03.
- **Coupling family graph-isolated.** Δk/Δx partition. Novel structural finding.
- **Role coherence proved for 10/11 domains** (Δx flagged as structural mismatch).
- **Identity failure decomposition (Δi = Δn + Δr + Δw).** Formalizes the syndrome claim.

## Tier 2 — Meaningful cashout

### P22 — *No Universal Plant Clock*

- **Lean modules:** `PersistenceModel.lean` (`persistence_normalizes` axiomatic boundary)
- **Cashout classes:** 1 (certify) + 4 (bridge artifact)
- **Paper-ready:** Yes, for the scope-fence point. The earlier draft index also listed `TaxonomyGraph.lean`'s coupling-family isolation as a secondary tie-in; on closer reading that mapping was too forced and has been dropped.
- **Revision candidacy:** *v1.1 candidate — local source edits complete 2026-04-20; not yet pushed to Zenodo.* P22 is already published on Zenodo (March 19, 2026; the earlier memory calling it "v0.9 with DOI reserved" was stale). One paragraph added to §6.4 acknowledging the Lean formalization's scope-fence discipline, README created, changelog entry in `NOTES.md`. Source `metadata.yaml` still shows `version: "0.9"`; a Zenodo push would require bumping metadata and rebuilding the PDF.

**What Lean underwrites:**

- **`persistence_normalizes` as axiomatic boundary marker.** The axiom explicitly states where static formalization ends and temporal logic would begin. This aligns with Paper 22's scope-fence discipline (gauge / clock / estimation / actuation as operational constraints, not metaphysics).
- **Three-terminal-families result** is structurally analogous (anti-universalism at the failure-taxonomy layer) but not a direct warrant for Paper 22's specific claims. Mentioned in the README's Formalization Status block as resonance, not as warrant.

### P23 — *Ops Is Control with a Non-Self-Identical Controller*

- **Lean module:** `OpsMasking.lean` (case (i) only)
- **Cashout classes:** 4 (bridge artifact) + 1 (certify), case (i) projection masking only
- **Paper-ready:** Yes for the kernel theorem. The general lemma `trajectory_eq_of_projected_eq` and the paper-form corollary `projection_masking` are both verified and cited in the paper's Formalization Status block.
- **Revision candidacy:** P23 was drafted concurrently with the Lean module and went out at v1.0 with the formalization already in the Status block, so no retroactive revision is needed. v1.0 published to Zenodo 2026-04-24 (DOI `10.5281/zenodo.19055415`). Cases (ii) (measurement null-space, first-order over horizon $T$) and (iii) (local gain aliasing, $\varepsilon$-resolution) remain paper-level and are not yet Leaned. Formalizing case (ii) is on the §6 / NOTES.md punch-list and is a candidate v1.x fold-in.

**What Lean underwrites:**

- **Case (i) projection masking, exact.** Two controllers with pointwise-equal projected actions produce identical trajectories under any plant dynamics and measurement map. Paper-form corollary $\Pi(C+H) = \Pi(C)$ pointwise ⇒ outputs coincide exactly.
- **Signature discipline.** The kernel pins the signatures of "controller", "projection", "trajectory", and "observation" so the §3.3 prose claim survives translation. Companion sim `ops_continuity.py` exhibits the case bit-exactly under saturating authority.
- **Open: cases (ii) and (iii) and gate-state-indexed projection.** The current Lean uses a fixed projection $\text{proj} : U \to U$ rather than the paper's $\Pi_{A_t}$; for case (i) this is harmless but a future module carrying $A_t$ explicitly (e.g., to formalize the §2 continuity-budget inequality) would need $\text{proj} : X \to U \to U$.

### P25 — *Epistemic Border Control as Proxy Regulation Under Partial Observability*

- **Lean module:** `Paper25EpistemicBorderControl.lean`
- **Cashout classes:** 1 (certify) + 4 (bridge artifact) + 2 (sharpen)
- **Paper-ready:** Yes for the structural-refusal core. Five theorems cover §5's sibling-vs-§N algebraic adjudication and §3.1's Theorem 1 epistemic-access core. Diagnostic 1 (Gramian-conditioning, regime-specific substitution-magnitude scaling) is paper-marked open and intentionally not Leaned; closed-loop induction is fenced as cathedral risk.
- **Revision candidacy:** P25 v1.0 (2026-05-12) published to Zenodo: [10.5281/zenodo.20145155](https://doi.org/10.5281/zenodo.20145155). §5 has a clarifying paragraph (added 2026-05-03) that names the Gramian identity $(\mathbf{1}_N \otimes O_T)^\top (\mathbf{1}_N \otimes O_T) = N \cdot O_T^\top O_T$, distinguishes subspace-preservation from individual-vector preservation, and points at the companion Lean module.

**What Lean underwrites:**

- **§5 sibling-vs-§N adjudication: kernel preservation under homogeneous stacking** (`ker_replicateRows_eq_ker`). Stacking $N$ homogeneous witnesses preserves the observability kernel: $\ker(\mathbf{1}_N \otimes M) = \ker(M)$ for $N > 0$. Paper 24's clean-aggregation-open-witness fix therefore cannot by itself solve P25's substitution problem.
- **§5 quantitative companion: Gramian scaling identity** (`replicateRows_transpose_mul`). $(\mathbf{1}_N \otimes M)^\top (\mathbf{1}_N \otimes M) = N \cdot M^\top M$. Eigenspaces are invariant; eigenvalues (and squared singular values) scale by $N$. The qualitative kernel statement is the special case at eigenvalue zero; the quantitative identity exposes the subspace-vs-vector precision the paper now reflects.
- **§3.1 Theorem 1 epistemic-access core** (`obsEquiv_policy_same`). Any policy that depends only on the observation trace is constant on observation-equivalence classes. The structural refusal: observation geometry forecloses target regulation regardless of controller sincerity.
- **§3.1 corollary — target-distinct-but-policy-same** (`target_distinct_policy_same`). Even when nominal target values differ between observation-equivalent states, the policy assigns the same control sequence. The target-inequality hypothesis is intentionally unused in the proof — that is the point: the policy never sees the target. The unused-hypothesis posture is the formal echo of the paper's Goodhart firewall.

**What it does not prove (intentional):**

- Diagnostic 1's quantitative substitution scaling for general $A$, $B$, noise structures (paper-marked open; partial result is paper-sequel territory, not gap-closure).
- Closed-loop dynamics, Kalman filtering, LQR. The paper's §3.1 prose proof hand-waves a closed-loop induction; that vindication is correct but separable from the structural refusal. Formalizing it would import machinery the paper deliberately does not need.
- Explicit finite-horizon observability matrix $O_T$ as a single matrix object. The §5 corollary is mechanical once $O_T$ is in scope; the abstract `replicateRows N M` already proves the load-bearing claim.
- SVD or least-observable-direction quantitative claims. Mathlib coverage limited; the qualitative kernel + Gramian results here are the qualitative substrate the paper actually needs.

**Companion artifacts (simulation):**

The §4 simulation results are produced by a single Python script in the Lean repo. The script is a mechanism check in one correctly-specified Kalman-LQR regime, not a derived scaling law; see §4.1 for scope conditions.

- **`paper25_substitution.py`** (`~/git/lean/`) — single-agent Kalman-LQR simulation of the §2 two-latent model with Poisson crank-shock innovations on $C$. Produces the §4.2 phase-transition sweep, the §4.6 Gramian-conditioning bridge, and the four figures below.
- **`paper25_phase_transition.png`** — §4.2 sweep of $T_\text{rms}^\text{asym} / T_\text{rms}^\text{clean}$ across $\alpha_T/\alpha_C \in [0.01, 10]$. Source of the table at §4.2.
- **`paper25_counterfactual.png`** — §4.3 effort-without-effect diagnostic: tracking-ratio and mean $|U|$ for asymmetric-sensor vs clean-$T$-sensor controllers across the same sweep.
- **`paper25_trajectory.png`** — §4.4 mechanism confirmation: single trajectory showing $T$, $\hat T$, $C$, $\hat C$, $U$ at a chosen $(\alpha_T, \alpha_C)$. Visualizes how $\hat T$ is pulled by $C$ through the Kalman posterior despite $q_C = 0$ in the LQR cost.
- **`paper25_gramian_bridge.png`** — §4.6 / §3.2 Diagnostic 1: finite-horizon observability Gramian $W_o = O_T^\top O_T$, smallest singular value $\sigma_\text{min}(O_T)$, and $T$-axis alignment $|\langle v_\text{min}, e_T \rangle|$ across the sweep. Operationalizes the Paper 23 §3.3 case (ii) bridge.

The script is the single source of truth for §4 numbers; the table at §4.2 is a representative readout of one parameter sweep (five seeds per ratio, 3000 steps, 500-step burn-in), not a derived bound.

**Adjacent formal work (not Paper 25 dependencies):**

The `LeanProofs/Admissibility/` modules (FiatAdmissibility, SurfaceAuthorization, NumericalAdmissibility, RecoveryMargin, ClosureEligibility, PublicReceiptRefinement, CorrectiveBoundary, WitnessInvariance, etc., built out 2026-05-11/12) develop the broader admissibility family that Paper 25's §8 nods toward via "Governor / admissibility working track." They are not part of Paper 25's proof dependency chain; the four theorems in `Paper25EpistemicBorderControl.lean` are the load-bearing formal spine, and §8's architectural sketch is paper-marked open. Folding receipt-lineage vocabulary into §8 is deferred per `preprint/25-epistemic-border-control/NOTES.md` ("§8 edit pin — receipt-lineage as architectural enforcement … deferred until after P27 stabilizes").

### P9 — *Capacity-Constrained Stability*

- **Lean module:** `BranchSelector.lean`
- **Cashout classes:** 1 (certify) + 2 (sharpen)
- **Paper-ready:** Yes.
- **Revision candidacy:** v1.1 with formalization appendix.

**What Lean underwrites:**

- **Budget asymmetry selects closure family (susceptibility/priming).** Directly formalizes Paper 9's claim that collapse is structurally predictable despite appearing sudden. Pre-existing budget asymmetry determines the closure family even under the same burn profile.
- **Dual-channel budget depletion race.** Mechanism for "metastable operating regime."
- **Precursor type does NOT determine closure family.** Slogan correction.
- Relevant `CLAIM-REGISTER.md` entry: #10 (claim on p.279-285 marked SOUND; no prose rewrite needed).

## Tier 3 — Moderate cashout

### P8 — *Detecting Temporal Debt*

- **Lean module:** `PersistenceModel.lean` (partial)
- **Cashout class:** 2 (sharpen)
- **Paper-ready:** Yes, narrow.
- **Revision candidacy:** Appendix note or footnote. Not worth a standalone version bump; bundle with other edits if Paper 8 is ever reopened.

**What Lean underwrites:**

- **What "temporal debt" accumulates to:** cumulative commitment, not elapsed duration. One-paragraph clarification.

### P16 — *The Gain Geometry of Temporal Mismatch*

- **Lean module:** `TaxonomyGraph.lean` (therapeutic inversions)
- **Cashout class:** 1 (certify)
- **Paper-ready:** Partial. Inversion count (13/15 domains have beneficial form under sign inversion; Δa and Δe lack one) is clean; mapping to shear / leverage / capture regimes needs interpretive work.
- **Revision candidacy:** Appendix note with inversion table.

### P19 — *Shadow Governance*

- **Lean module:** Inherited downstream from `PersistenceModel.lean` via Paper 18.
- **Cashout class:** 1 (certify, inherited)
- **Paper-ready:** Depends on Paper 18 revision.
- **Revision candidacy:** If Paper 18 gets v1.1/v1.2, Paper 19 gets a citation update pointing at the new formalization. No independent revision motivation.

### P6 — *Temporal Closure Requirements*

- **Lean module:** None direct, but see `CLAIM-REGISTER.md` entry #4 (SI-C "long enough" framing marked STALE).
- **Cashout class:** 3 (expose looseness)
- **Paper-ready:** Partial.
- **Revision candidacy:** Prose tightening in SI-C ("long enough" → coexistence framing). Not a version bump on the main paper; supplementary document edit.

#### Formalization warrant (filed 2026-06-11) — historical hold; Scratch kernel compiled the same day

This warrant began as a handle for review, not a build order, and was queued **behind the demo/slab**. That scheduling note did not constitute a formalization gate and was overtaken the same day by the bounded Scratch kernel recorded below. Current policy is explicit: a coherent claim or countermodel may be formalized before a paper, consumer, or runtime implementation; promotion remains separate.

- **Target claim:** the README abstract's "three architectural operators (timescale separation, endogenous state, adaptive control) are **necessary and sufficient** for maintaining coherent identity across perturbations." This is broader than the SI-C "long enough" looseness already in CLAIM-REGISTER #4.
- **Free finding, registerable now without any spike:** the *abstract* asserts necessary-and-sufficient; the *body* only derives the necessity half plus an impossibility result (stateless transformers cannot satisfy the requirements — main file §3, conclusion §"minimal architectural requirements"). Sufficiency (having the three operators ⇒ coherent identity) is asserted, not established. §154's "memory may be necessary… but it is not sufficient" is an adjacent caution, not the crux. Honest register status: **abstract overclaims relative to body** (expose-looseness), independent of Lean.
- **Claim shape / cost:** "necessary and sufficient over an open class of systems" is the most expensive formalization shape. Sufficiency = build the model class and prove the property. Necessity = prove *every* coherent system has all three operators, universally quantified over systems not yet defined. This is a dynamical-systems modeling campaign with a Lean skin — months-shaped, the kind of object that eats launches. Do **not** open it pre-slab.
- **Cashout class (predicted):** 2 (sharpen) / 3 (expose looseness). Predicted outcome is narrowing, not certification: *"within model class M, the three operators are necessary and sufficient for property P\*,"* where P\* is tighter than "coherent identity."
- **Foothold spike (refute-first, one weekend, post-slab):** the narrowing is established by **counterexample, not proof**. Necessity dies the moment one degenerate system maintains trivial coherence while missing an operator. Spike question: *state "coherent identity under perturbation" in the existing kernel vocabulary for a toy two-layer system, and mine for a necessity counterexample* (Alloy bounded search or a hand-built degenerate case — same refutation-first muscles as the BoundaryTransit spike). If the counterexample drops, that alone transitions the register entry (BROKEN at stated strength, narrowing warranted) and earns the v2 with the corrected claim — without the swamp.
- **Disposition:** bounded kernel compiled as recorded below; the larger dynamical campaign remains a separate scope decision. Its next step is governed by the narrowed claim's model-theoretic value and cost, not by consumer permission. Refute before certify remains the highest-assurance-per-hour ordering for a necessary-and-sufficient claim.

#### Kernel compiled (2026-06-11) — `Scratch/Paper6TemporalClosureKernel.lean`

A v0.1 type-boundary kernel was drafted (with ChatGPT + a second Claude), refined here, and **compiled green** by Lean Claude. Custody: scratch-checked (`lake env lean` clean, 2026-06-11), `sorry`-free, no `native_decide`; axiom audit of the load-bearing theorems = `[propext]` only (`accumulator_not_autonomous`, `clock_not_unbounded` depend on *no* axioms). Not imported by `LeanProofs.lean`; no paper fold-in authorized.

- **What turned green (necessity side, structural — not label algebra):** a `Sys` state machine with input-driven `step` and autonomous `tick`. `EndogenousTrajectory := UnboundedHistoryDependence ∧ AutonomousTick`. The knife — `context_wrapper_not_endogenous` — rests on `wrap_is_kBounded` (a *real induction*: a stateless core in a size-`k` context window is finite-context-bounded at `k`, so finite context cannot manufacture unbounded history dependence). The earlier bare-`Prop` sketch was `¬B → ¬(A∧B∧C)`; this version makes the predicate inspect structure, and the witnesses **discriminate**: `Accumulator` (unbounded, tick=id → *not* autonomous; the named booby trap), `Clock` (autonomous, input-ignoring → finite-context-bounded), `AccumulatorClock` (both → the lone endogenous witness). That answers "does it rule out anything the definitions didn't already?" — yes, it separates three concrete systems.
- **Register honesty (the load-bearing line):** v0.1 is **bridge artifact + partial structural sharpen on the NECESSITY/type-boundary side only.** Necessity is rendered structurally for one operator (endogenous trajectory); `temporalSeparation` and `adaptiveControl` are deliberately *not* modeled (the `tick` field is the seam; deferring them also dodges the SI-A ε paper-cut). **Sufficiency is OPEN and circular-by-construction** in any kernel that defines closure as having the operators — it becomes a theorem only if "coherence under perturbation" gets an *independent* definition and the implication is proven across the gap (the deferred dynamical campaign). The kernel itself does not repair the abstract overclaim (a kernel cannot — it only proves the necessity side). **That overclaim was retired separately in v1.1-candidate source on 2026-06-11** (abstract + README + conclusion + SI-A §8.2 reworded; "necessary and sufficient"/"minimal architectural requirements" → "necessary architectural roles" + an explicit "general sufficiency … remains an open formalization target" blast door; SI-A ε=0.05-as-O(10²) corrected). Zenodo v1.0 left as historical artifact; the corrected claim surface ships on the next bump. The standing rule still holds: do not let "now formalized in Lean" imply the *sufficiency* side is proven — it is not.
- **Erratum rider (errata basket, not formalized):** SI-A bills `ε = 0.05` (≈ 20×) as `O(10²)`. Keep `temporalSeparation` propositional until a numeric-invariant module exists; the magnitude does not get smuggled in at v0.
- **Foothold unchanged:** the Alloy/hand-built necessity counterexample hunt was always aimed at the *real* (dynamical) claim, not this label/structure boundary. Still the cheap half, still post-slab.

### P24 — *Shared Vision as Coordinating Prior*

- **Lean module:** `Paper24SharedVision.lean` (added 2026-04-28). Algebraic shard for §4 metric probes and Theorems 3–4. Companion simulation `shared_vision.py` in the Lean repo provides the §4 probe artifacts (aggregation-boundary, alias-compatibility, filter).
- **Cashout classes:** 2 (sharpen) + 1 (certify)
- **Paper-ready:** Yes for the algebraic shard. The §4 metric algebra, the η-step bound, and the survivor-cohort centered-mean-zero algebra are formalized. Lean correction landed: the formal pairwise difference is $(\varphi_i - \varphi_j) \cdot V$; the paper's Proposition 2 statement currently has the opposite sign. Metric claims (absolute value, square) are unaffected.
- **Formalization gap:** Proposition 1 (no-scalar-free-lunch) is currently probe-backed conjecture, intentionally not Leaned. Promoting it to theorem requires fixing the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?) and exhibiting the structural trade-off between freeze-freedom and stability within that class. This is the single highest-value future Lean target for P24, flagged in P24 §8 item 1 and in `preprint/24-shared-vision-coordinating-prior/NOTES.md`.
- **Revision candidacy:** P24 is v1.0 (published 2026-04-28; concept DOI `10.5281/zenodo.19861995`, version DOI `10.5281/zenodo.19861996`). The Lean module landed the same day as v1.0 publication; the paper text already reflects the algebraic shard. A future v1.1 fold-in on Proposition 1 would parallel the P18 Appendix A / P22 Lean fold-in patterns. The Proposition 2 sign is a candidate prose correction in any v1.1 push.

**What Lean underwrites:**

- **§4 metric algebra** (`alias_baseline_zero`, `alias_shift_pairwise_difference`, `two_agent_absdiff_scales_linear`, `two_agent_variance_scales_quadratic`). Pairwise difference identity, baseline-zero, two-agent absolute-difference linear scaling, two-agent variance quadratic scaling.
- **Theorem 3 kernel — sup-norm bound** (`filtered_supnorm_bound`). Stated with witness-filter retention as hypotheses ($|\Phi(E^F)| \le \text{maxRetained} \le \tau$), not as operator-theoretic abstraction over arbitrary aggregators.
- **η-step bound** (`step_bound`). $|V_{t+1} - V_t| \le \eta \cdot \tau$ given the sup-norm bound.
- **Theorem 4 kernel — survivor-cohort centered-mean-zero** (`survivor_centered_errors_mean_zero`). The cohort first-moment-zero algebra.

**What it does not prove (intentional):**

- Conjecture 1 / Proposition 1 (no-scalar-free-lunch). Probe-backed only; promoting requires the aggregator-class precision noted above.
- The agile case study, closed-loop dynamics, witness-filter institutional prose.
- Big-O / noise-floor falsifiability hooks.
- Aggregator-in-the-abstract operator theory.

## No clean cashout

Papers with no current Lean mapping worth attaching as a warrant:

- **P1–P5** — foundational Δt series; Lean work postdates them and doesn't directly underwrite their claims.
- **P7** — Δt-constrained inference (synthesis paper; Lean machinery is downstream of it, not within it).
- **P10, P11** — invariant requirements; observer problem. No direct mapping.
- **P12** — bounded lattice inference. The governor architecture Paper 12 describes is related to the validator work in `agent_gov`, not to the Lean proofs. Separate bridge.
- **P13, P14** — censorship / attack surface. Domain-specific applications; no Lean mapping.
- **P17** — receipt compiler / epistemic policy. Conceptually adjacent to the `agent_gov` / `continuity` doctrine, not to Lean proofs.
- **P20, P21** — frame capture / observer integrity. No Lean mapping.

These are not "never" candidates — just not current. If the Lean stack grows dynamic-claim formalizations per the roadmap, some of these may pick up warrants.

## BabyRiver (separate track)

`~/git/babyriver/lean/BabyRiver/*.lean` — state preservation invariants, Kaplan-Meier survival monotonicity, log-rank bookkeeping. Sits outside the current 22-paper scope. Candidate warrant for a future paper on biological/population-level Δt dynamics (not yet written). Not a current-paper revision question.

## Infrastructure substrate (no paper anchor)

### Admissibility kernel — Authority + StateTransition + Derivation + Execution + Corrective

- **Lean modules:** `LeanProofs/Admissibility/Authority.lean`, `StateTransition.lean`, `Derivation.lean`, `Execution.lean` (Layers 0–4, 2026-04-30), `Corrective.lean` (Layer 5, 2026-05-01). All under namespace `Admissibility.*`, all wired into `LeanProofs.lean` root, all `sorry`-free.
- **Cashout class:** N/A — infrastructure substrate, not paper-claim cashout
- **Paper-ready:** N/A
- **Revision candidacy:** N/A — no paper anchored to this kernel yet
- **Companion working note:** `working/admissible-recovery-semantics.md` (2026-05-01). Corrective monotonicity / non-laundering recovery semantics. Slot decision (P27 fold-in vs standalone P28) deferred pending the seven-path audit named in §8 of the working note.

**What Lean underwrites:**

- Verdict algebra (`Authority.lean`): `authorized ⇔ admissible basis ∧ resolved precedence ∧ standing`. Pure gate — direct parameters, no half-evaluated `Transition` struct.
- Store-partitioned mutation (`StateTransition.lean`): governance state split into `PolicyStore` / `EvidenceStore` / `GapStore` / `RevocationStore`. Only `Step.amendPolicy` mutates `PolicyStore`. `StepAllowed` predicate gates raw mutation by per-step standing predicates.
- Read-side bridge (`Derivation.lean`): `decideAuthority : GovState × Actor × AuthorityClaim → AuthorityVerdict` composes derivations through the verdict gate. Bundled-structure design (`BasisDerivation` etc. carry function + spec obligations). One revocation-shaped safety consequence: `revoked_basis_never_authorized`.
- Closed bridge (`Execution.lean`): `AuthorizedStep` requires both mutation standing and claim verdict by construction. Load-bearing theorem: `revoked_basis_cannot_be_authorized_step` — a revoked basis cannot bind at the mutation layer.
- Corrective monotonicity (`Corrective.lean`): `classify : Step → StepClassification` (corrective / forward / neutral) is total — adding a new `Step` constructor without an arm is a Lean non-exhaustive-match error, which is the enforcement surface against silently-corrective-and-authority-granting transitions. `WeaklyLessPermissive env Γ' Γ` is the preorder; `CorrectiveMonotone env` carries the proof obligation as a structure field (no global axiom). `RecoveryEnv` bundles env + obligation; recovery-facing APIs take `RecoveryEnv`, not raw `DerivationEnv` — the kernel makes monotonicity expressible, the type signature makes it operationally required at the recovery boundary. Load-bearing corollary: `corrective_no_authority_laundering` rules out same-basis laundering.

The kernel is **Governor-neutral**: it pins the algebraic skeleton so a concrete Governor (`agent_gov`) instantiation can cite "no laundering" with a formal warrant rather than a slogan. Concrete `claimForStep` resolvers and `AuthorityClaim` schema commitments are deferred to Governor's instantiation, not the kernel itself; pre-committing the resolver here would be ontology bait.

Existing P27 `Admissibility.lean` (namespace `P27`) sits alongside but independent: P27 is post-transition obligation accounting; the kernel is pre-action authorization. Complementary, not duplicate. The P27 skeleton is sorry-free (three real proofs against the local `admissible` definition: `unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`; two `True`-placeholder discharges with deferred-real-statement docstrings pending substrate-accusation / causal-binding predicates). Intentionally unwired — sorry-elimination does not imply wiring. Paper v1.0 published 2026-05-18; P27 §8 explicitly scopes the Lean kernel as local accounting core, with distributed admissibility and three-horizon durability carried by the paper model rather than the kernel. The kernel does not subsume P27 and P27 does not cover the kernel's authority-gate question.

See `LeanProofs/Admissibility/README.md` in the Lean repo for the five-module breakdown and an explicit "what it warrants vs what it does not warrant" list.

## Scratch packets (warrant-tier, NOT promoted)

Fenced Lean scratch establishing a no-go *shape*. These are warrants, not
ratified claims: not wired into `LeanProofs.lean`, no shared foundation module,
no public vocabulary frozen. Promotion is a separate ratification-tier act.

### Observer foundation — DRAFTED, NOT RATIFIED (pinned 2026-06-14)

- **Status:** observer foundation **drafted, not ratified**. Warrant-tier scratch.
- **Mathematical center:** *a consumer-independent force predicate exists iff all
  consumers agree* (`has_global_section_iff_consumers_agree`, axiom-free).
- **Ladder:** consumer-relative freshness → consumer-relative force →
  absolute-stamp bridge-price → global-section iff agreement. Files:
  `~/git/lean/LeanProofs/Scratch/{ConsumerRelativeFreshness, ConsumerRelativeForce,
  AbsoluteForceStampBridgePrice, NoUniversalRoot}.lean` (all `lake env lean` green,
  `sorry`-free).
- **Universal root:** demoted to a *positive exception / single-root governance
  model* (`universal_root_licenses_stamp`), NOT the foundation's no-go.
- **Empty-root caveat:** a root that forces nothing is vacuously universal and
  licenses only the empty stamp; the genuine no-go is the agreement-iff, not "no
  universal root."
- **Consolidation is ratification-tier and is NOT part of this slice.** Defining
  shared `Consumer`/`Force` vocabulary, a foundation module, register promotion of
  the center theorem — all deferred. Graduation preflight (candidate nucleus,
  exclusions, open taxonomy questions) parked at
  `working/observer-foundation-promotion-preflight.md`.
- **Codomain correction (2026-06-14, seven-system excavation).** The "no consumer"
  blocker is **discharged**: NQ, nightshift, wicket, continuity, standing, verifier,
  WLP all ship consumer-relative verdict production. The nucleus codomain is abstract
  `Verdict` (`Force : Consumer → Artifact → Verdict`) — **not** `Prop` (degenerate,
  2/7) and **not** `Strength` (0/7). The four slices above are the `Verdict := Prop`
  special case (fossils, NOT rewritten); the generic nucleus is added additively as
  `Scratch/ConsumerRelativeVerdict.lean`. Full excavation table + five invariants +
  verifier-as-negative-control in `working/observer-foundation-promotion-preflight.md`.
  Still warrant-tier: no wiring, no shared module, no claim-register promotion.

## Priority ordering if revisions proceed

1. **P22** — pre-release incorporation; cheapest to fold in before v1.0 ships.
2. **P18** — biggest value-left-on-table; Lean directly underwrites the central mechanism.
3. **P15** — cleanest legitimacy move; natural extension of verification-forward posture.
4. **P9** — clean certification plus slogan correction.
5. Tier 3 — bundle opportunistically, don't reopen papers just for these.

## Change log

- **2026-04-19** — Index created. Based on Lean inventory as of commits `cfc612f` (misc tex) / `d6adbbc` (lean proofs) / `6bc8037` (lean work integration) / `18c1f7c` (phase 1 baby river lean kernel).
- **2026-04-20** — P22 formalization fold-in complete in local source (v1.1 candidate, not yet pushed to Zenodo). §6.4 paragraph added, README created, NOTES.md changelog entry added. Reclassified P22 cashout to drop the too-forced `TaxonomyGraph.lean` coupling-family tie-in; kept `PersistenceModel.lean` `persistence_normalizes` axiom as the primary anchor plus three-terminal-families as structural resonance. Corrected earlier working-memory assumption that P22 was still pre-release — it has been on Zenodo since March 19, 2026.
- **2026-04-20** — P18 Appendix A drafted in local source (v1.1 candidate, not yet pushed to Zenodo). Appendix structure: A.1–A.6 per-claim entries in ChatGPT's four-field format (formal object / prose claim sharpened / what it does not prove / pointer), plus A.7 (relation to the paper's framework) and A.8 (scope fences — pre-breach dynamics, observer-integrity, tier escalation, empirical calibration not covered). Abstract, introduction, and conclusion left unchanged; v1.2 (abstract reframe) deferred.
- **2026-04-22** — Added P23 entry under Tier 2 (`OpsMasking.lean`, case (i) projection masking, bridge artifact + certify; cases (ii) and (iii) deferred). Added P24 entry under new "Sim-only cashout" section — no Lean module yet, only `shared_vision.py` companion sim; Proposition 1 (no-scalar-free-lunch) flagged as the single highest-value Lean target. Both papers are v0.1, not yet pushed to Zenodo. Mirrors the `PAPER-MAP.md` update in the Lean repo.
- **2026-04-30** — Added "Infrastructure substrate (no paper anchor)" section for the Admissibility kernel (four modules: `Authority.lean`, `StateTransition.lean`, `Derivation.lean`, `Execution.lean`). Kernel is Governor-neutral; substrate for future Governor (`agent_gov`) implementation citation, not paper-claim cashout. All four wired into `LeanProofs.lean` root. Updated "Stable identifiers" to reflect the full module set (paper-anchored, no-paper-anchor, P27 skeleton, infrastructure substrate). Mirrors `PAPER-MAP.md` update in the Lean repo.
- **2026-05-03** — Added P25 entry under Tier 2 (`Paper25EpistemicBorderControl.lean`, certify + bridge artifact + sharpen). Five theorems covering §5 sibling-vs-§N adjudication (kernel preservation under homogeneous stacking; Gramian scaling identity $(\mathbf{1}_N \otimes M)^\top (\mathbf{1}_N \otimes M) = N \cdot M^\top M$) and §3.1 Theorem 1 epistemic-access core (observation-equivalence ⇒ policy-equivalence; target-distinct-but-policy-same corollary with intentionally-unused target hypothesis). Companion §5 clarifying paragraph added to `epistemic_border_control.md` (subspace-vs-vector precision; explicit Gramian identity; Lean repository pointer). Promoted P24 out of "Sim-only cashout" section to its own Tier 2 entry: `Paper24SharedVision.lean` was added 2026-04-28 (same day as P24 v1.0 publication) and the index had not yet been patched. Stable identifiers updated to include `Paper25EpistemicBorderControl.lean`. Mirrors `PAPER-MAP.md` and `CLAIM-REGISTER.md` entries (#11, #12) in the Lean repo.
- **2026-06-11** — P6 overclaim retired in v1.1-candidate source (Zenodo v1.0 unchanged): abstract (main + README), conclusion, and SI-A §8.2 reworded from "necessary and sufficient" / "minimal architectural requirements" / "Sufficiency" to "necessary architectural roles" / "Constructive Feasibility" + explicit "general sufficiency remains an open formalization target" blast door; SI-A `ε=0.05`-as-`O(10²)` corrected to qualitative-separation framing. Changelog at `preprint/06-temporal-closure-requirements/NOTES.md`. The abstract no longer implies the sufficiency side the Lean kernel does not prove.
- **2026-06-11** — P6 v0.1 type-boundary kernel compiled green: `~/git/lean/LeanProofs/Scratch/Paper6TemporalClosureKernel.lean`, scratch-checked, `sorry`-free, axioms `[propext]`. Structural necessity-side knife (`context_wrapper_not_endogenous` via the `wrap_is_kBounded` induction) with discriminating accumulator/clock/product witnesses. Sufficiency OPEN/circular-by-construction; abstract-overclaim finding unrepaired; SI-A ε=0.05-as-O(10²) parked in errata. See the P6 "Kernel compiled" subsection.
- **2026-06-14** — **Schema doctrine note filed** (warrant-tier, no Lean, no bump): `working/no-free-standing-bridge-schema.md`. Names the family resemblance across the day's slices — *`NoFreeStandingBridge` as schema, not file*: **local validity does not lift across a boundary without an explicit, authorized bridge** (corollary: *a free bridge collapses the gate it crosses*). Five independently-proved ⇏ rows: temporal (`hopwise_fresh_not_trajectory_fresh`), observer (`no_global_section_when_consumers_disagree`), deadlock (`valid_deferrals_can_deadlock`), custody/multigov (`no_conflicting_quorum_certificates` / `atomic_lease_gives_unique_winner`), reflexive/amendment (`founding_does_not_bless`, `no_transition_without_pre_authorization` — already in the `AmendmentFragment` annex). Engine/root: `NoFreeStandingBridge.lean`'s price theorem. **Closes the buried-calculus loop:** the hunted "unifier" was never a positive calculus — the positive calculus IS the FreeStandingBridge that opens every gate; the honest form is this negative table. **Load-bearing fence:** schema = family resemblance, NOT a Lean meta-theorem; a unifier subsuming all five would itself be the laundering the corpus refuses ([[project-no-unifier-without-laundering]]). Math lineage (relayed, verify before paper): local-to-global obstruction / descent-gluing failure / absence of a global section; indexed-fibered categories; obstruction theory; BFT quorum intersection; rely/guarantee compositionality. **Honest status (per-row column in the note):** only the observer row is a *literal* global-section theorem (`HasGlobalSection ↔ ConsumersAgree`); the other four are formally-verified no-lift specimens that are *schema-aligned, NOT reduced* to sheaf/global-section form. **Meta-bridge guard:** claiming the others are sheaf corollaries without building the translation would itself be a free-standing bridge in the meta-theory (and three-model "schema" agreement is common-mode, not proof — observer is the tie-breaking artifact; the rest await their own excavation). Promotes (if ever) as doctrine/paper named for the negative result, NEVER a unifying kernel.
- **2026-06-14** — Quorum-custody BFT spine compiled green (no paper anchor; **agent_gov-purposed**, forward-looking; the BFT-clothes twin of `DeadlockEscalation`'s singular custody): `~/git/lean/LeanProofs/Scratch/QuorumCustody.lean`, scratch-checked. **First observer/custody slice to use Mathlib** (`Finset` card combinatorics) — so its theorems carry the full Mathlib trio `[propext, Classical.choice, Quot.sound]` (honest departure from the zero-axiom pure-logic slices; genuine finite combinatorics). Resolves a multi-model *median* detour: a model stated a FALSE `median allVals = median honestVals` "BFT" theorem (refuted n=7,f=2); median is a robust *aggregator*, not an exact-consensus object. The real object: `quorum_intersection_large` (two 2f+1 quorums overlap in >f, via inclusion-exclusion + `n≤3f+1`) → `quorum_intersection_contains_honest` (pigeonhole: overlap has ≥1 honest node) → `no_conflicting_quorum_certificates` (with the **`HonestNoDoubleCertify` LOCK** as hypothesis — ChatGPT's guardrail: intersection is the substrate, the lock is what blocks conflict) → `conflict_representable_without_lock` (negative control: drop the lock, conflict is representable). Doctrine: *plural observation may be quorum-shaped; custody advancement must be singular or quorum-certified — median aggregates values, quorum custody constrains authority.* Conceptually the same custody theorem as `atomic_lease_gives_unique_winner` (BFT clothes vs lease clothes) — flagged as a reading, no formal transport proved. Codex pre-check: clean on all five substantive targets (arithmetic real, pigeonhole genuine, lock load-bearing, negative control non-vacuous); two prose overclaims softened (the `≡` → conceptual correspondence; `>f` ≡ `f+1≤card`). NOT modeled: full PBFT/Raft, network/adversary, rounds, median. Not wired, not promoted.
- **2026-06-14** — Sharded-custody jurisdiction sidecar compiled green (no paper anchor; **agent_gov-purposed** doctrine sidecar, **NOT a P4 dependency**; the lawful-exception that keeps the multigov/no-global-section results from overstating): `~/git/lean/LeanProofs/Scratch/ShardedCustody.lean`, scratch-checked, `sorry`-free. Models the sharding discriminator only (jurisdiction theorem, **no consensus mechanics** — no Paxos/Raft): `Owner : Shard → Root`, `Admissible owner t := every shard t touches is owned by t.driver`. `contested_shard_requires_same_root` (contested shard + both admissible ⇒ same driver — singular custody/sequencing; **zero-axiom**); `different_roots_on_contested_shard_not_both_admissible` (different drivers on a contested shard ⇒ ¬both-admissible — the shard-instance of the no-global-section pattern, arbitration the *unmodeled* escape; **zero-axiom**); `disjoint_shards_allow_parallel_custody` (distinct roots, disjoint shards, both admissible — the lawful plural-custody exception, witnessed; `[propext]`). Codex pre-check caught a name-vs-content overclaim (`..._no_global_section` proved only ¬both-admissible → renamed) → fixed. Keeper: *plural custody is admissible over disjoint jurisdiction, not shared contested state.* Not wired, not promoted.
- **2026-06-14** — Deadlock *escalation* (multi-governor) slice compiled green (no paper anchor; **agent_gov-purposed**, forward-looking — multigov Q2; sibling of `DeadlockTrajectory`): `~/git/lean/LeanProofs/Scratch/DeadlockEscalation.lean`, scratch-checked, `sorry`-free. Models the deadlock-AMONG-governors axis (concurrent observers of the same stuck state): `concurrent_observations_coalesce` + `distinct_issues_do_not_merge` (key stable across observers, injective across issues — both **zero-axiom**), with `chain_tip_in_key_splits_same_issue` / `coarse_key_merges_distinct_issues` witnessing the too-fine (stampede) and too-coarse (fail-open merge) failure modes; `resolved_does_not_suppress_recurrence` (occurrence = key×epoch; real suppression-rule check, backs the name) vs `content_only_suppresses_recurrence` (the ABA swallow); `decision_survives_lease_rotation` (decision binds occurrence not lease token) vs `token_bound_decision_dies_on_rotation`; options deterministic-from-basis (structural — no leaseholder argument; race-winner-authored options unrepresentable); and the footgun pair `atomic_lease_gives_unique_winner` / `fake_cas_admits_two_winners` (≤1 winner is conditional on a linearizable lease — fake CAS = confident stampede; **zero-axiom**). The marquee `at_most_one_active_resolver` (decorative, ≤1-by-type) deliberately omitted — risk lives in the above. NOT modeled (governor's Python, AG-owned): CAS/lease impl, operator sink, store, retry, normalization heuristics; distributed multigov HELD until a linearizable-lease substrate exists. Axioms: coalescing/injectivity/CAS-pair zero-axiom; recurrence + decision-rotation `[propext]`. Codex pre-check caught a name-vs-content overclaim (recurrence proved bare inequality → re-modeled as an actual suppression rule) + a sufficiency/necessity naming fix (`atomic_lease_gives_unique_winner`) → fixed. Not wired, not promoted.
- **2026-06-14** — Deadlock classification-boundary slice compiled green (no paper anchor; **agent_gov-purposed**, composition-family sibling of the temporal packet): `~/git/lean/LeanProofs/Scratch/DeadlockTrajectory.lean`, scratch-checked, `sorry`-free. Models *permitted nonterminal deferrals ⇏ global progress* — the deadlock analog of `hopwise_fresh ⇏ trajectory_fresh`. `LocalOutcome {progress,refuse,exhaust,defer}` → `globalOf` → `GlobalOutcome {progressed,refused,exhausted,operatorRequired}`; `valid_deferrals_can_deadlock` (composed = operatorRequired), `ownerless_deferral_requires_operator` (general), `deadlock_is_not_refusal_or_exhaustion` (distinct outcome, **zero-axiom**). Lean proves the *boundary*; the runtime detector (repeated deferral / no artifact delta / circular ownership → DeadlockReceipt, halt retry) is the **governor's Python**, owned by the AG session, deliberately NOT modeled here. Axioms: distinctness zero-axiom; list-composition theorems `[propext]` only. Codex pre-check caught two real overclaims pre-handoff (the "circular" name proved no cycle → renamed `ownerless_deferral_requires_operator`; the defer-dominates precedence was unstated → pinned + witnessed via `mixedDeferral`) and a doc axiom-label error → all fixed. Not wired, not promoted.
- **2026-06-14** — **Observer foundation opened** — four green fenced scratch slices (no paper anchor; doctrine, the observer axis previously parked as a warrant across the temporal packet). All `lake env lean` clean, `sorry`-free. The axis is now consumer-indexed: judgment is `f consumer artifact`, never bare `f artifact`. (1) `ConsumerRelativeFreshness.lean` — the time→observer adapter; `FreshFor : Consumer → Evidence → Time → Prop` with a per-consumer clock (the N-consumer generalization of `Freshness.DivergenceAcceptable`'s verifier/issuer); `fresh_for_verifier_not_fresh_for_consumer` (axiom-free). (2) `ConsumerRelativeForce.lean` — `Force : Consumer → Artifact → Prop` (list-recognized policy); `force_for_A_does_not_imply_force_for_B`, `no_consumer_independent_force`. (3) `AbsoluteForceStampBridgePrice.lean` — the observer bridge-price: `AllowsAbsoluteForceStamp` (abstract `Stamp`/`F`, never inhabited); `absolute_stamp_collapses_consumer_boundary` (stamp forces an unwilling consumer) + `honest_force_gate_refuses_absolute_stamp` (load-bearing control). Doctrine: *a stamp on the envelope cannot create force for every catcher* (the PCAA/receipt-stamping category error as a price theorem). (4) `NoUniversalRoot.lean` — **the publishable theorem**, abstract over any `Force`. Center (post-ChatGPT-review): `has_global_section_iff_consumers_agree` — *a consumer-independent force predicate exists IFF all consumers agree on every artifact* (**axiom-free**); `no_global_section_when_consumers_disagree` is the no-go corollary (**axiom-free**); `stamped_disagreement_refutes_absolute_stamp` (no-go for the stamp); `universal_root_licenses_stamp` (positive *exception* for closed/rooted systems — a universal root licenses AN honest stamp, the root-tracking one; **not** the only sound stamp); concrete `no_forcing_root_for_disputed_artifact` (an *open* consumer world has no *forcing* root that is universal for a disputed artifact). **Empty-root caveat** (ChatGPT raccoon): `UniversalRoot` is vacuously satisfied by a root that forces nothing — which licenses only the empty stamp (sound, useless), so the genuine no-go is the agreement-iff, not "no universal root." Axioms: abstract theorems (the iff + disagreement no-go) depend on **none**; concrete list-model specimens carry `[propext, Quot.sound]` (standard `List.mem`/`decide` footprint, not `Classical.choice`, no `sorry`). Ties to `OperatorBasisGateInput`'s warrant: agent_gov's qualified-operator = genesis root → single-rooted, `universal_root_licenses_stamp` makes its absolute stamp legitimate; **federate it and `no_global_section…` reopens the observer axis.** No further temporal-foundation work — the time packet stays closed; this extracts its one lesson (validity is artifact × consumer × witness-context).
- **2026-06-14** — Operator-basis gate-input specimen compiled green (no paper anchor; **agent_gov-purposed**, informs P4.0g — canonical pointer belongs in `~/git/agent_gov/working/P4.0g-operator-basis-lean-spike-2026-06-14.md`, which is operator's to edit, not mine): `~/git/lean/LeanProofs/Scratch/OperatorBasisGateInput.lean`, scratch-checked (`lake env lean` clean), `sorry`-free, headline theorems depend on **no axioms**. Settles the seam web-Claude flagged: the spike's gate input `operator_basis_present : bool` is "checked, not typed," which fails the spike's *own* target (make bad states unrepresentable). Models `gateBool : Bool → Bundle → Verdict` vs `gateTyped : OperatorBasisReceipt → Bundle → Verdict`. Proves `bare_bool_ignores_bundle` (bool verdict independent of consumed bundle, by `rfl` — binding structurally inexpressible, not merely unchecked), `bare_bool_gate_collapses_binding` (detached `true` admits a bundle the honest typed binding refuses), `typed_gate_admits_iff_bound` / `typed_gate_refuses_iff_mismatch` (both directions — admit/refuse exactly track the bundle-hash binding; detached-admit unrepresentable), `typed_gate_depends_on_bundle`, plus the self-contained collapse `bare_bool_gate_collapses_reviewed_bundle_binding`. Carries Chatty's custody-location caveat (does *not* prove bool+mandatory-revalidation unsound — proves the gate *input* has no custody; if another layer restores binding, that layer is the real gate). Rule: *no bare `operator_basis_present` bool at the gate; the gate consumes the receipt(-hash), presence is the binding* — `AmendmentFragment` type-move applied to the gate input. Carries the observer WARRANT (qualified-operator = genesis root, single-rooted today; federated agent_gov → foreign consumer doesn't share the root → multi-root is the observer extension). Did **not** write into agent_gov (read-only). **Observer axis still a warrant.**
- **2026-06-14** — Post-hoc legitimation bridge-price compiled green (no paper anchor; doctrine slice, **closes the retroactive family**): `~/git/lean/LeanProofs/Scratch/PostHocLegitimationBridgePrice.lean`, scratch-checked (`lake env lean` clean), `sorry`-free, headline theorems depend on **no axioms**. Not imported by `LeanProofs.lean`; standalone (`Decision.occursAt`/`Evidence.availableAt` vocab mirroring `RetroactiveFigLeaf`, no sibling import). The true fig-leaf case promoted to `NoFreeStandingBridge` price form: `AllowsPostHocLegitimation` over an *abstract* legitimation verdict (named, never inhabited); `posthoc_bridge_collapses_legitimation_gate` proves admitting it legitimates an early decision (made at 10) by evidence available only later (at 20, strictly after — `decision_strictly_before_late_evidence`), evidence that was *not available at decision time*; `honest_gate_refuses_posthoc_bridge` is the load-bearing control. Does **not** prove the bridge globally false (a declared reopening/appeal/new-evidence-review is a *different* gate — re-adjudication, not authorized-at-decision). Doctrine: *archaeology is not authorization — later availability of evidence does not authorize an earlier decision made without it.* Discriminator vs siblings = bridge antecedent: stale-at-consumption (`ValidAt e decisionT` carried forward) / not-yet-valid (future validity borrowed back) / **post-hoc (absent at decision, present in hindsight)**. Also: anticipatory slice gained a strict-before sharpening (`anticipatory_bridge_clears_strictly_not_yet_valid`, `50 < validFrom`) — bridge kept broad at `≤`, strict fact added as a named theorem for prose alignment. **Temporal no-go packet now complete:** trajectory composition failure + three carried-validity bridge-prices (retroactive / anticipatory / post-hoc). **Observer axis still a warrant**, untouched.
- **2026-06-14** — Anticipatory bridge-price compiled green (no paper anchor; doctrine slice, temporal dual of the retroactive slice): `~/git/lean/LeanProofs/Scratch/AnticipatoryBridgePrice.lean`, scratch-checked (`lake env lean` clean), `sorry`-free, headline theorems depend on **no axioms**. Not imported by `LeanProofs.lean`; standalone (does *not* import the retroactive slice — its `ValidAt` is the dual lower-edge `validFrom ≤ t`; duplication in scratch over accidental coupling). Promotes `Freshness.not_yet_valid_not_fresh` (single-moment) into `NoFreeStandingBridge` **price form**: `AllowsAnticipatoryClearance` is a candidate predicate over an *abstract* clearance verdict (named, never inhabited); `anticipatory_bridge_collapses_clearance_gate` proves admitting it clears a not-yet-valid witness at decision time while it is *not* valid then (gate-collapse); `honest_gate_refuses_anticipatory_bridge` is the load-bearing control. Does **not** prove the bridge globally false (a legitimate pre-clearance/escrow semantics could model it). Doctrine: *"approval is coming" is not approval — expected future validity does not clear present action.* With this, the **temporal bridge stack is complete for the two carried-validity directions** (trajectory composition failure + retroactive stale-at-consumption + anticipatory not-yet-valid). The fig-leaf *evidence-appears-after-decision* case (`RetroactiveFigLeaf`'s `PostValidatedAt`) remains a distinct **sibling, not yet built**. **Observer axis still a warrant**, untouched.
- **2026-06-14** — Retroactive bridge-price compiled green (no paper anchor; doctrine slice, follows the trajectory slice): `~/git/lean/LeanProofs/Scratch/RetroactiveBridgePrice.lean`, scratch-checked (`lake env lean` clean), `sorry`-free, headline theorems depend on **no axioms**. Not imported by `LeanProofs.lean`; no promotion. Promotes the **stale-at-consumption** small negative (the `TemporalCustody` line — citation/decision-time validity ⇏ execution-time admissibility) into `NoFreeStandingBridge` **price form**: the bridge `AllowsRetroactiveDischarge` is a candidate predicate over an *abstract* discharge verdict (named, never inhabited); `retroactive_bridge_collapses_freshness_gate` proves admitting it discharges a concretely stale witness while it is *not* admissible-at-consumption (the gate-collapse); `honest_gate_refuses_retroactive_bridge` is the load-bearing control (the honest freshness gate is not a model of the bridge — analogue of the engine's TRIPWIRE, stated positively). Per engine discipline, does **not** prove the bridge globally false (`∀ discharges, ¬…` would be overclaim). Doctrine: *fresh-at-decision is not admissible-at-consumption — having once been valid does not discharge staleness at the point of use.* **Scope (do not over-read):** the bridge antecedent is `ValidAt e decisionT` carried forward — evidence existed and was fresh at decision, then went stale. It does **not** cover the fig-leaf case where evidence did not exist at decision time and only appeared afterward (`RetroactiveFigLeaf`'s `PostValidatedAt`, `decision.occursAt < evidence.availableAt`); that "evidence appears after the decision" price theorem is a distinct **sibling, not yet built**. **Anticipatory bridge (`AllowsAnticipatoryClearance`, "approval is coming" ≠ approval) remains queued** — header comment only, not built (one temporal demon per PR). **Observer axis still a warrant**, untouched.
- **2026-06-14** — Temporal-composition seam compiled green (no paper anchor; doctrine slice): `~/git/lean/LeanProofs/Scratch/TemporalTrajectory.lean`, scratch-checked (`lake env lean` clean), `sorry`-free, headline theorems depend on **no axioms at all**. Not imported by `LeanProofs.lean`; no promotion path. Theorem: **hopwise admissibility is not trajectory admissibility**, specialized to freshness — `hopwise_fresh_not_trajectory_fresh` and the post-completion-strengthened `hopwise_fresh_not_completed_trajectory_fresh` (`t' ≤ T`, closing the "what does *consumed* mean" weasel). Slogan: *freshness does not compose by default* — every hop passes its local check, the composed run is stale at the consume point. Reuses the `Admissibility/SafetyTrajectory.lean` induction *shape* (state-threading → clock-threading; hop payload "authorized" → "fresh at its own local time") but stays import-free like the sibling scratch kernels; adjacency to `SafetyTrajectory`/`Freshness`/`TemporalCustody`/`RetroactiveFigLeaf`/`RetroactiveLegitimation` is advisory, no correspondence claim. **Queued, NOT built** (named in the file header so the seam is legible): two NoFreeStandingBridge-form bridge-price theorems — *retroactive* ("it worked later" ⇏ authorized-then) and *anticipatory* ("approval is coming" ≠ approval) — each pricing the forbidden discharge to gate-collapse; that is the next slice. **Observer axis is a WARRANT, not a slice** — `Freshness.DivergenceAcceptable (verifier issuer maxDiv)` is the two-frame nucleus; eventual `Force : Consumer → Artifact → Prop` with no-absolute-force-without-universal-root; `Scratch/MultiConsumerAdoption.lean` is the only beachhead and models adoption, not force. Held back so the practical theorem is not hijacked by the sexier one.
- **2026-06-11** — Filed P6 formalization warrant under the then-current "name-early, not authorized to build" wording: target is the abstract's "necessary and sufficient" claim over an open system class; free finding is abstract-overclaims-relative-to-body (registerable now, expose-looseness, no Lean needed); refute-first foothold spike (necessity counterexample on a toy two-layer system) queued post-slab; larger formalization scoped on spike outcome. The authorization wording is historical and superseded; the Scratch kernel compiled later that day, and current policy permits formalization to lead. Also flagged two STALE index entries surfaced by a 2026-06-11 live audit of the implementation/data repos (not yet edited into the entries above, pending operator decision): **P18** — the Tier 1 entry tracks only `PersistenceModel.lean`; it does not capture the *running implementations* (`wicket`/`standing`/`wlp` + `Admissibility/` kernel) that are now field-evidence warrants for the six invariants / five barriers / promotion ceremony (B1/B2/B4 + INV1/INV3/INV5 shipped; B3/B5 + L3 recursive governance + explicit predicate trace + observer-integrity monitoring not built; tiers reframed as evidence-tiers; 5-phase ceremony collapsed to ~3). **P8** — the Tier 3 "not worth a standalone version bump" disposition predates ~100 real `temporal_debt` measurements found in `graveyard/detector/data/` (Feb 2026 eval epoch; spans coherent/metastable/collapse regimes; detector faithful to the `debt = confidence − f_support` formula; one-off eval, not time-series, not live deployment).
- **2026-05-01** — Added `Corrective.lean` as fifth Admissibility kernel module (Layer 5: corrective monotonicity). Pinned thesis: corrective recovery transitions cannot increase the authorized action set; authority-increasing recovery requires a separately classified forward transition with fresh basis. `classify : Step → StepClassification` is the enforcement surface; `RecoveryEnv` bundles `DerivationEnv` with a `CorrectiveMonotone` witness and is the type-level gate at which monotonicity becomes operationally required. Companion working note `working/admissible-recovery-semantics.md` (slot decision deferred between P27 fold-in and standalone P28 pending the seven-path audit named in working-note §8). Same-day, P27 skeleton (`Admissibility.lean`) sorry-eliminated: three real proofs against the local `admissible` definition (`unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`) and two `True`-placeholder discharges with deferred-real-statement docstrings (pending substrate-accusation / causal-binding predicates). House rule: kill the sorrys, do not let the sorrys design the constitution; sorry-elimination does not imply wiring. Mirrors `PAPER-MAP.md` update in the Lean repo.
