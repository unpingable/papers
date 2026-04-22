# Formalization Index

Canonical crosswalk between the preprint series and the Lean formalization work.

Paper-side view lives here. Module-side view lives in the Lean repo at `PAPER-MAP.md`. Claim-level audit (with BROKEN / STALE / SOUND / OPEN status per specific prose location) lives in the Lean repo at `CLAIM-REGISTER.md`. Module-level exposition of what's proved and what each proof kills lives in the Lean repo at `WHAT-THE-LEAN-STACK-PROVES.md`.

This file is the bridge object. It tells you, for any paper, whether Lean has produced a warrant upgrade and what kind.

## Stable identifiers

- `P{N}` — preprint number (e.g., `P18`)
- Lean modules in `~/git/lean/LeanProofs/` are `TaxonomyGraph.lean`, `BranchSelector.lean`, `PersistenceModel.lean`
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
- **Revision candidacy:** Not applicable; P23 is itself v0.1 (not yet pushed to Zenodo) and was drafted concurrently with the Lean module. Cases (ii) (measurement null-space, first-order over horizon $T$) and (iii) (local gain aliasing, $\varepsilon$-resolution) remain paper-level and are not yet Leaned. Formalizing case (ii) is on the §6 / NOTES.md punch-list.

**What Lean underwrites:**

- **Case (i) projection masking, exact.** Two controllers with pointwise-equal projected actions produce identical trajectories under any plant dynamics and measurement map. Paper-form corollary $\Pi(C+H) = \Pi(C)$ pointwise ⇒ outputs coincide exactly.
- **Signature discipline.** The kernel pins the signatures of "controller", "projection", "trajectory", and "observation" so the §3.3 prose claim survives translation. Companion sim `ops_continuity.py` exhibits the case bit-exactly under saturating authority.
- **Open: cases (ii) and (iii) and gate-state-indexed projection.** The current Lean uses a fixed projection $\text{proj} : U \to U$ rather than the paper's $\Pi_{A_t}$; for case (i) this is harmless but a future module carrying $A_t$ explicitly (e.g., to formalize the §2 continuity-budget inequality) would need $\text{proj} : X \to U \to U$.

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

## Sim-only cashout (no Lean module yet)

### P24 — *Shared Vision as Coordinating Prior*

- **Lean module:** None yet. Companion simulation `shared_vision.py` in the Lean repo provides the §4 probe artifacts (aggregation-boundary, alias-compatibility, filter).
- **Paper-ready (sim side):** Yes. The §4 probes are reproducible and the §3 theorems (T1, T3, T4) have proofs / proof sketches in the paper that do not require Lean for soundness.
- **Formalization gap:** Proposition 1 (no-scalar-free-lunch) is currently probe-backed conjecture. Promoting it to theorem requires fixing the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?) and exhibiting the structural trade-off between freeze-freedom and stability within that class. This is the single highest-value Lean target for P24, flagged in P24 §8 item 1 and in `preprint/24-shared-vision-coordinating-prior/NOTES.md`.
- **Revision candidacy:** N/A; P24 is v0.1 (not yet pushed to Zenodo). A future v0.2 fold-in on Proposition 1 would parallel the P18 Appendix A pattern.

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
