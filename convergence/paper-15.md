# Paper 15 — Cybernetic Fault Domains — Convergence Spike

**Full title:** Cybernetic Fault Domains: When Commitment Outruns Verification
**Date:** 2026-02-18
**DOI:** 10.5281/zenodo.18686130

## Status: spiked 2026-03-18

## Claim Cluster
- When irreversible commitments cross a boundary faster than verification can complete, unverified state transitions accumulate and produce recurring loss-of-control signatures
- Cybernetic fault domains are defined by three measurable quantities: commitment boundary (C_k), commitment-verification lag (Δt), and boundary load (σ)
- Nine distinct domain instantiations (organizations, LLMs, censorship, security, safety tuning, platforms, representations, optimization, synthetic coherence) share the same boundary-relative temporal regime
- A dimensionless risk index R_t = PD/E formalizes the gate as a single inequality
- The framework's strongest adversarial target is specified: a system sustaining high Δt and σ without degradation would kill the theory

## Search Terms
- commitment verification lag fault containment
- irreversible state transition unverified governance
- fault domain boundary crossing rate
- commitment boundary load system failure
- verification latency commitment speed mismatch
- dependable computing fault containment temporal
- socio-technical systems commitment outrunning oversight
- governor architecture commitment gating verification

## Expected Convergence Level
hints expected
Fault containment and dependable computing have their own literature, but the specific framing of commitment-verification lag as a universal vulnerability across socio-technical domains, with a dimensionless risk index, is likely distinctive. Some structural overlap with safety engineering concepts of defense in depth.

## Hits

### STRONG STRUCTURAL CONVERGENCE (same problem shape, different formalism)

**1. Zwitter, A. (2024). "Cybernetic governance: implications of technology convergence on governance convergence." *Ethics and Information Technology*, Springer.**
- Match type: **structural**
- Claims supported: C-V lag (general), domain instantiation (governance, platforms)
- Summary: Technology convergence outpaces regulatory frameworks; governance needs adaptive feedback loops from cybernetics. Identifies the *problem* (commitment outrunning oversight) and proposes cybernetics as the solution space, but does not formalize the lag as a measurable quantity or define fault domains. No dimensionless index.
- Gap: Problem-level convergence, not formalism-level.

**2. O'Reilly Radar (2025). "AI, A2A, and the Governance Gap."**
- Match type: **structural** (strongest single hit)
- Claims supported: C-V lag (core), boundary load (σ), domain instantiation (LLMs, platforms, organizations)
- Summary: Agent-to-agent protocols remove the "friction brake" of manual integration; commitments now cross boundaries faster than governance can verify them. Explicitly states: "our ability to connect agents is outpacing our ability to control what they commit us to." Identifies failure signature: not single catastrophic event but accumulating small incidents where dashboards say "green" but outcomes are wrong. Uses "governance gap" where Paper 15 uses "commitment-verification lag."
- Gap: No formal quantities, no dimensionless index, no cross-domain unification.

**3. McKinsey (2025). "Trust in the Age of Agents." Risk & Resilience.**
- Match type: **structural**
- Claims supported: C-V lag, commitment boundary, domain instantiation (organizations, LLMs)
- Summary: "Agency isn't a feature; it's a transfer of decision rights." 80% of organizations have encountered risky agent behavior. Identifies need for: agent inventory, autonomy tiered by risk, verified identity, reconstructible decisions, rollback plans. Governance must match what agents can commit to.
- Gap: Industry framing, no formal model. Practitioner-level convergence.

**4. Matni, Ames, & Doyle (2024). "Towards a Theory of Control Architecture." arXiv:2401.15185 / IEEE Control Systems.**
- Match type: **structural**
- Claims supported: Temporal regime, boundary-relative control, cross-domain universality
- Summary: Formalizes layered control architectures (LCAs) where different layers operate at different temporal rates. Universal framework applicable across power systems, robotics, biology, networks. Shares the structural intuition that temporal rate mismatches across control layers are fundamental.
- Gap: Focuses on *designed* control systems, not on fault domains arising from *uncontrolled* commitment-verification mismatch. No concept of irreversible commitment or accumulating unverified transitions. Formal-methods convergence from the opposite direction (design vs. failure).

### PARTIAL CONVERGENCE (one or two claims overlap)

**5. Safety Gap / Fine-Tuning Bypass Literature (2024-2025)**
- Key papers: "Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency" (arXiv:2506.17209); "Safety Alignment Should Be Made More Than..." (ICLR 2025); FAR AI "Safety-Gap Toolkit"
- Match type: **partial**
- Claims supported: C-V lag (safety tuning domain instantiation), boundary load
- Summary: Safety alignment is "only a few tokens deep." Capability outpaces verification. Fine-tuning on 10 examples at $0.20 collapses safety. Direct instantiation of Paper 15's "safety tuning" domain but does not generalize beyond LLMs.

**6. Future of Life Institute (2025). "AI Safety Index" (Winter & Summer 2025).**
- Match type: **partial**
- Claims supported: C-V lag (general), boundary load (σ as industry-wide load)
- Summary: "Capabilities are accelerating faster than risk management practice, and the gap between firms is widening." No common regulatory floor. Descriptive finding, no formal model. Empirical confirmation of the qualitative claim.

**7. Gupta, N. (2026). "Latency vs Consistency: When Speed Becomes a Lie." Medium.**
- Match type: **partial**
- Claims supported: C-V lag (distributed systems domain), verification lag as systemic risk
- Summary: Systems achieve low latency by avoiding coordination, thereby weakening consistency. "Speed becomes a lie when the system returns an answer that looks authoritative but is no longer accurate." Software-engineering-specific restatement, no cross-domain generalization.

**8. Cybernetics and Institutional Failure: Greenland Fish Markets. Foley et al. (2020). *Marine Policy*.**
- Match type: **partial**
- Claims supported: Domain instantiation (governance/censorship), feedback failure
- Summary: First-order cybernetic (command-and-control) governance failed because it lacked second-order feedback (legitimacy, reflexivity, co-design). Case-study-level convergence, no temporal formalism.

**9. "The Verification Crisis: Expert Perceptions of GenAI Disinformation." arXiv:2602.02100 (2026).**
- Match type: **partial**
- Claims supported: C-V lag (synthetic coherence domain), verification failure
- Summary: GenAI creates "epistemic fragmentation" and "synthetic consensus." The black-box nature of models creates a "reproducibility crisis" where interventions become speculative. Maps to Paper 15's "synthetic coherence" domain instantiation.

**10. "When Deciding Creates Overconfidence." (2025). *Judgment and Decision Making*, Cambridge.**
- Match type: **partial**
- Claims supported: Commitment-verification lag (psychological mechanism), epistemic overcommitment
- Summary: The act of deciding itself distorts subsequent information processing, creating a confidence-distortion-confidence cycle. Commitment creates overconfidence rather than the reverse. Micro-level mechanism that could underlie the macro-level fault domain pattern.

### BACKGROUND CONVERGENCE (related concepts, different framing)

**11. Escalation of Commitment literature (established).** Irrational persistence after irreversible commitments — cognitive bias framing, not temporal-boundary formalism.

**12. Ashby's Law of Requisite Variety.** Controller must match system variety. Compatible but distinct — Paper 15 is about *temporal* mismatch specifically, not variety mismatch.

**13. Stewart Brand's Pace Layering.** Different system layers change at different rates. Descriptive (how things *are*) not diagnostic (when things *fail*).

**14. Reference/Command Governors in control theory.** Gate references through constraint checks. Structurally similar to governor architecture but focused on designed systems with known constraints.

## Notes

**What is well-established prior art:**
- The qualitative problem of commitment outrunning verification (widely recognized across AI governance, organizational theory, platform governance)
- Individual domain-specific observations (LLM safety gaps, AI agent governance gaps, institutional lag)

**What is partially converged (2024-2026 independent work):**
- O'Reilly A2A piece: strongest single convergence hit — uses "governance gap" for the same pattern
- McKinsey agent trust: practitioner-level convergence
- Matni/Ames/Doyle layered control architecture: closest formal competitor (design vs. failure direction)

**What remains novel in Paper 15:**

| Aspect | Status |
|---|---|
| C_k, Δt, σ as three measurable quantities defining a fault domain | **Novel** |
| Dimensionless risk index R_t = PD/E as single inequality gate | **Novel** |
| Nine-domain unification under a single temporal regime | **Novel** |
| Falsification target (sustained high Δt and σ without degradation) | **Novel** |
| The name "cybernetic fault domain" | **Novel** |
| The *problem* of commitment outrunning verification | **NOT novel** — consensus concern across multiple fields |

## Verdict

**Strong hints confirmed, as predicted.** The qualitative insight — that commitment outrunning verification produces system failure — is now a consensus concern across AI governance (O'Reilly, McKinsey, FLI), LLM safety research, platform governance, and organizational theory. Multiple independent streams arrived at the same problem statement between 2024-2026.

What Paper 15 adds that nobody else has: (1) a formal three-quantity characterization making the pattern measurable, (2) a dimensionless risk index reducing it to a single testable inequality, (3) cross-domain unification showing nine failure modes are instances of the same boundary-relative temporal regime, and (4) an explicit falsification condition.

The paper is well-positioned: it arrives when the qualitative problem is urgent and widely recognized, but nobody has formalized it. The AI governance literature is moving fast — the window for theoretical priority on the formalism is narrowing.

**Strongest prior art to cite:** Zwitter (2024), O'Reilly A2A (2025), Matni et al. (2024), LLM safety-gap literature.
