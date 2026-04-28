# Paper 27 — Candidate Claims

## Primary candidate

**Candidate claim:** Reconciliation controllers are commonly specified in terms of convergence (eventually current = desired). This is incomplete. A reconciliation transition may restore desired state while silently degrading the obligations required for later diagnosis, governance, or operator reliance — evidence, causality, custody, authority, continuity, and substrate accountability. Define *transition admissibility* as the dual safety property: ∀ transition τ, all obligations Ω(τ) are accounted for over horizon H(τ). Ephemerality is a transition property, not an object property: an object is ephemeral with respect to a transition under a declared obligation set and retention horizon.

**One-line slide form:** *controller-correct, operator-unsound.*

**Status:** scaffolded — abstract + section outline + Lean skeleton committed; no prose draft, no proof development, no Kubernetes implementation. Queue-jumped per dependency-discovery argument (P27 supplies the constructive endpoint the P22–P26 negative spine demands).

**Imports:**
- **Paper 25** (projection α: B → K; observability null space). P27 specializes B = substrate, K = control-plane visible state. Argues obligations live in or across the null space when not first-class control-plane objects.
- **Paper 26** (retention horizons H : Obligation → Horizon). P27 borrows horizon machinery — evidence horizon, causality horizon, substrate-accusation horizon — but does not absorb the full premature/belated duality.
- **Paper 23** (hidden compensation H_t). One downstream consequence: when reconciliation destroys evidence, the operator carries causal continuity in memory. Cited, not central.
- **Anvil-style controller verification** (Sun et al.). P27 explicitly framed as the dual safety property: Anvil verifies P(eventually current = desired); P27 verifies P(∀τ. Ω accounted for over H(τ)).
- **Refinement / abstraction soundness** (Lamport, Abadi; CEGAR lineage). Obligation-soundness as application-layer refinement constraint.
- **Failure masking** (Schlichting & Schneider). Masked-by-recovery as transition audit state.
- **Causal tracing / provenance** (Dapper, Magpie, PROV-DM, Trio). Retention horizons tied to obligation classes.
- **Forensic readiness** (Rowlingson, Tan). Preserve-evidence-before-disposal integrated with control-loop transition admissibility.
- **K8s NPD + chaos engineering** (Litmus, Chaos Mesh). Surface substrate problems / inject faults; no admissibility framework over reconciliation transitions.

**Depends on:**
- Decision on whether P27 jumps the Δc→Δh persistence model in the Lean dynamic-claims queue.
- P25 lit-differential (P27 cites P25's projection framing; if P25 framing shifts, P27 §3 shifts).
- Three concrete K8s worked examples (§9) — Masked / Orphaned / DegradedWithReceipt scenarios where reconciliation reports recovery and auditor emits non-trivial finding.
- Receipt-recursion scope decision (§7) — full self-governance of audit plane is sibling work, not P27's scope.

**Risk:**
- Becoming a "K8s essay" instead of a formal-controller paper. K8s is the specimen; the target is the general class (orchestrators, autoscalers, rollbacks, agent retries, CI/CD repair, service-mesh retries, DB failover).
- Importing P26's full temporal-seam argument; P27 wants horizons, not the duality.
- Receipt-recursion swallowing the paper (defer to scope-limited §7).
- "Much math, such control theory" prestige fog. Math earns its keep iff it (a) distinguishes cases prose would blur, (b) produces a falsifiable admissibility condition, (c) prevents bad merges with neighboring ideas, (d) gives Lean something small and total to verify. Receipt durability invariant and the Accounting/Outcome split clear all four; receipt-recursion possibly does not.
- Reviewer attack surface: "where's the evaluation?" Mitigated by Lean skeleton + three worked K8s examples; full prototype auditor is sibling work.

**Do not accidentally merge with:**
- Paper 25. P27 is *constructive*; P25 is *necessity-framed negative*. Sibling, not nested.
- Paper 26. P27 imports horizons; P26's full temporal-seam argument stays in P26.
- SRE essay (`working/sre-as-shock-absorption.md`). Methodology critique on a different axis (P23-companion lane). Do not load into P27 introduction.
- "Self-healing systems" and "Kubernetes operator" literature. Adjacent but distinct: those describe recovery; P27 audits recovery transitions for obligation soundness.

## Section outline

1. Introduction — the convergence/testimony gap
2. Related work — six neighborhoods, gap at boundary
3. Model — substrate B, control plane K, projection α, bridge relation R_t
4. Obligation-unsound quotients — formal definition, K8s instances
5. Transition admissibility — obligations × outcomes × horizons
6. Audit states — Observed, Confirmed, Superseded, Masked, Orphaned, DegradedWithReceipt, Resolved, Invalidated, CannotTestify
7. Receipt durability and recursive admissibility — scope-limited
8. Reconciliation auditor — prototype architecture
9. Worked examples — three K8s scenarios
10. Lean formalization (companion: `~/git/lean/LeanProofs/Admissibility.lean`)
11. Generalization beyond K8s
12. Discussion — relation to P25/P26, scope conditions, limits
13. Conclusion

## Contribution bullets

1. Formal model of reconciliation controllers as quotient machines over substrate state.
2. Obligation-unsound quotienting as a structural defect, dual to refinement-unsoundness.
3. Ephemerality redefined as a transition property under declared obligations and horizons.
4. Audit-state vocabulary with Masked, Orphaned, DegradedWithReceipt as machine-readable transition outcomes.
5. Receipt durability invariant: H(receipt) ≥ max(H(ω) for affected obligations); receipt persists *outside* the lifecycle, authority domain, and failure domain of the audited object.
6. Reconciliation auditor architecture sketch.
