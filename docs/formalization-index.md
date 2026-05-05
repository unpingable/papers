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
    - P27 skeleton (sorry-free as of 2026-05-01, intentionally unwired): `Admissibility.lean`
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

Chatty's pushback (2026-04-19): calling a revision "v2.0" oversignals rupture when the underlying move is sharpening + correction. Default to v1.x unless the abstract itself has to change.

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
- **Revision candidacy:** P25 is v0.1 draft (2026-05-01), not yet pushed to Zenodo. §5 has a clarifying paragraph (added 2026-05-03) that names the Gramian identity $(\mathbf{1}_N \otimes O_T)^\top (\mathbf{1}_N \otimes O_T) = N \cdot O_T^\top O_T$, distinguishes subspace-preservation from individual-vector preservation, and points at the companion Lean module. v1.0 push will incorporate this; no separate fold-in revision needed.

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

Existing P27 `Admissibility.lean` (namespace `P27`) sits alongside but independent: P27 is post-transition obligation accounting; the kernel is pre-action authorization. Complementary, not duplicate. As of 2026-05-01 the P27 skeleton is sorry-free (three real proofs against the local `admissible` definition; two `True`-placeholder discharges with deferred-real-statement docstrings pending substrate-accusation / causal-binding predicates). Intentionally unwired — sorry-elimination does not imply wiring. The kernel does not subsume P27 and P27 does not cover the kernel's authority-gate question.

See `LeanProofs/Admissibility/README.md` in the Lean repo for the five-module breakdown and an explicit "what it warrants vs what it does not warrant" list.

## Priority ordering if revisions proceed

1. **P22** — pre-release incorporation; cheapest to fold in before v1.0 ships.
2. **P18** — biggest value-left-on-table; Lean directly underwrites the central mechanism.
3. **P15** — cleanest legitimacy move; natural extension of verification-forward posture.
4. **P9** — clean certification plus slogan correction.
5. Tier 3 — bundle opportunistically, don't reopen papers just for these.

## Change log

- **2026-04-19** — Index created. Based on Lean inventory as of commits `cfc612f` (misc tex) / `d6adbbc` (lean proofs) / `6bc8037` (lean work integration) / `18c1f7c` (phase 1 baby river lean kernel).
- **2026-04-20** — P22 formalization fold-in complete in local source (v1.1 candidate, not yet pushed to Zenodo). §6.4 paragraph added, README created, NOTES.md changelog entry added. Reclassified P22 cashout to drop the too-forced `TaxonomyGraph.lean` coupling-family tie-in; kept `PersistenceModel.lean` `persistence_normalizes` axiom as the primary anchor plus three-terminal-families as structural resonance. Corrected earlier working-memory assumption that P22 was still pre-release — it has been on Zenodo since March 19, 2026.
- **2026-04-20** — P18 Appendix A drafted in local source (v1.1 candidate, not yet pushed to Zenodo). Appendix structure: A.1–A.6 per-claim entries in chatty's four-field format (formal object / prose claim sharpened / what it does not prove / pointer), plus A.7 (relation to the paper's framework) and A.8 (scope fences — pre-breach dynamics, observer-integrity, tier escalation, empirical calibration not covered). Abstract, introduction, and conclusion left unchanged; v1.2 (abstract reframe) deferred.
- **2026-04-22** — Added P23 entry under Tier 2 (`OpsMasking.lean`, case (i) projection masking, bridge artifact + certify; cases (ii) and (iii) deferred). Added P24 entry under new "Sim-only cashout" section — no Lean module yet, only `shared_vision.py` companion sim; Proposition 1 (no-scalar-free-lunch) flagged as the single highest-value Lean target. Both papers are v0.1, not yet pushed to Zenodo. Mirrors the `PAPER-MAP.md` update in the Lean repo.
- **2026-04-30** — Added "Infrastructure substrate (no paper anchor)" section for the Admissibility kernel (four modules: `Authority.lean`, `StateTransition.lean`, `Derivation.lean`, `Execution.lean`). Kernel is Governor-neutral; substrate for future Governor (`agent_gov`) implementation citation, not paper-claim cashout. All four wired into `LeanProofs.lean` root. Updated "Stable identifiers" to reflect the full module set (paper-anchored, no-paper-anchor, P27 skeleton, infrastructure substrate). Mirrors `PAPER-MAP.md` update in the Lean repo.
- **2026-05-03** — Added P25 entry under Tier 2 (`Paper25EpistemicBorderControl.lean`, certify + bridge artifact + sharpen). Five theorems covering §5 sibling-vs-§N adjudication (kernel preservation under homogeneous stacking; Gramian scaling identity $(\mathbf{1}_N \otimes M)^\top (\mathbf{1}_N \otimes M) = N \cdot M^\top M$) and §3.1 Theorem 1 epistemic-access core (observation-equivalence ⇒ policy-equivalence; target-distinct-but-policy-same corollary with intentionally-unused target hypothesis). Companion §5 clarifying paragraph added to `epistemic_border_control.md` (subspace-vs-vector precision; explicit Gramian identity; Lean repository pointer). Promoted P24 out of "Sim-only cashout" section to its own Tier 2 entry: `Paper24SharedVision.lean` was added 2026-04-28 (same day as P24 v1.0 publication) and the index had not yet been patched. Stable identifiers updated to include `Paper25EpistemicBorderControl.lean`. Mirrors `PAPER-MAP.md` and `CLAIM-REGISTER.md` entries (#11, #12) in the Lean repo.
- **2026-05-01** — Added `Corrective.lean` as fifth Admissibility kernel module (Layer 5: corrective monotonicity). Pinned thesis: corrective recovery transitions cannot increase the authorized action set; authority-increasing recovery requires a separately classified forward transition with fresh basis. `classify : Step → StepClassification` is the enforcement surface; `RecoveryEnv` bundles `DerivationEnv` with a `CorrectiveMonotone` witness and is the type-level gate at which monotonicity becomes operationally required. Companion working note `working/admissible-recovery-semantics.md` (slot decision deferred between P27 fold-in and standalone P28 pending the seven-path audit named in working-note §8). Same-day, P27 skeleton (`Admissibility.lean`) sorry-eliminated: three real proofs against the local `admissible` definition (`unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`) and two `True`-placeholder discharges with deferred-real-statement docstrings (pending substrate-accusation / causal-binding predicates). House rule: kill the sorrys, do not let the sorrys design the constitution; sorry-elimination does not imply wiring. Mirrors `PAPER-MAP.md` update in the Lean repo.
