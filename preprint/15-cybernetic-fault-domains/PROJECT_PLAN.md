# Cybernetic Fault Domains: Project Plan (v0.1 → v1.0)

The project paper (`cybernetic_fault_domains-project.md`) contains the full-scope vision. The published MVP (`cybernetic-fault-domains-v0.1.md`) covers core definitions, measurement protocol, a summary instantiation table, and a BLI sketch. This plan breaks the remaining material into incremental writing sessions.

## Version Map

| Version | Content | Status |
|---------|---------|--------|
| v0.1 | Core definitions, measurement protocol, summary table, BLI sketch | **Published** |
| v0.2 | Expanded domain instantiations | Planned |
| v0.3 | Governor architecture & threat model | Planned |
| v0.4 | Appendix C (dimensionless risk index) — or paper 16 | Planned |
| v0.5 | Falsifiability, related work, discussion | Planned |
| v0.6 | Appendix B (paradox reframings) — optional | Planned |
| v1.0 | Integrated paper with all sections | Planned |

---

## v0.2 — Expanded Domain Instantiations

**Source material:** Project paper sections 3.1–3.9

**What's new:** The 9 full domain write-ups, each with fast/slow layer identification, canonical instantiation template (C_k, H, T_commit, W_j, A_j, σ method, κ estimate, failure label), and failure signatures. The MVP compresses these into one table row each.

**Split into two sessions by affinity:**

### Session 2A — Institutional / Sociotechnical Cluster

Domains:
- Organizational Systems (§3.1) — decisions outpace evidence, Second Law
- Scalar Reward Collapse (§3.8) — optimization outruns multi-objective balance, Goodhart
- Platform Dynamics (§3.6) — virality outruns moderation, eigenstructure collapse

Workflow:
1. For each domain, expand the summary table row into a full canonical instantiation
2. Cross-reference the cited source papers ([2], [3], [4], [6], [9]) for parameter values
3. Ensure failure signatures are concrete and falsifiable, not just restating Δt

### Session 2B — Computational / Technical Cluster

Domains:
- LLM Hallucination (§3.2) — generation outruns verification, temporal debt
- AI Safety Tuning (§3.5) — classification outruns intent analysis, false positives
- DPI Bypass (§3.3) — packets outrun inspection, bypass inequality
- Async Security (§3.4) — attacks outpace detection, MTTD/MTTR
- Representational Coherence (§3.7) — transformation outruns preservation, ΔR
- Temporal Closure (§3.9) — simulation outruns reality check, simulator gap

Workflow:
1. Same canonical instantiation expansion as 2A
2. LLM and AI Safety sections need careful handling of the C0/C1/C2 commitment taxonomy — the nuance about token generation (C0) NOT being T_commit is load-bearing
3. Security sections (DPI, async) have the most concrete measurables — lean into that

**Session protocol:**
- ChatGPT: draft prose and parameter narratives
- Claude: audit consistency with v0.1 formalism and cross-paper references
- Driver: merge, resolve, version

**Done when:** Each domain has a concrete failure signature not reducible to restating "Δt > 0," and each canonical instantiation template is filled with measurable (or boundable) parameter values, not placeholders.

**Output:** Updated paper with full §3 replacing the summary table (table stays as §3.10 summary)

---

## v0.3 — Governor Architecture & Threat Model

**Source material:** Project paper sections 4.1–4.3, including 4.1.1 and 4.1.2

**What's new:**
- Governor pattern (proposal/commit separation, temporal ordering enforcement, decoupling visibility, invariant maintenance)
- Framing in Ashby/Laprie/Leveson terms
- Developmental tradeoff (§4.1.1) — when decoupling is fine, phase-appropriate coupling, coupling costs
- Selective coupling for real-time domains (the R_t ≤ τ preview)
- BLI as exemplar with three nested fault domains (temporal, authority, contradiction)
- Generalization to other domains (organizations, security, AI safety, platforms)
- Governor failure modes / threat model (§4.1.2) — bypass channels, evidence laundering, rubber-stamping, backlog starvation, availability collapse, adversarial timing

**Single session.**

Workflow:
1. §4.1.1 (developmental tradeoff) is important — it prevents the paper from reading as "all decoupling is bad"
2. §4.1.2 (threat model) is what makes the governor pattern credible — governors shift the control problem, they don't eliminate it
3. Cross-reference paper 12 (BLI) to avoid redundancy — this section should frame BLI as exemplar, not re-derive it
4. The "governor vs process" distinction is load-bearing — architectural enforcement vs advisory process

**Session protocol:**
- Claude: strong on the architectural/formal content, threat model rigor
- ChatGPT: strong on making the developmental tradeoff readable and the domain generalizations concrete
- Driver: merge, check that the BLI references don't duplicate paper 12

**Done when:** The governor pattern is architecturally specified (not just described), the developmental tradeoff makes clear when decoupling is acceptable, and the threat model enumerates at least 4 concrete governor failure modes with mitigations. BLI is referenced as exemplar, not re-derived.

**Output:** Updated paper with full §4

---

## v0.4 — Dimensionless Risk Index (Appendix C)

**Source material:** Project paper Appendix C (§C.1–C.11)

**What's new:**
- Tool Power (P_t) — privilege × blast radius × irreversibility
- Normalized Feedback Delay (D_t)
- Evidence Integrity (E_t) — vector with policy projection, operationalization
- Agent Risk Index: R_t = (P_t · D_t) / E_t
- Regime classification (SAFE / ELASTIC / DANGEROUS / RUNAWAY)
- Binding policy: P_max = (τ · E_t) / D_t
- Evidence minimums (fail-closed gates)
- Open-loop detection (Γ_t)
- Receipts as currency (algebraic equivalence to R_t bound)
- Governor loop pseudocode
- Glass cannon sensitivity analysis

**Decision point:** This is substantial enough to be paper 16. Advantages of splitting:
- Paper 15 stays tighter (fault domains + governors)
- Paper 16 becomes "Runtime Governance for Actuator-Bearing Agents" or similar
- Natural citation dependency: 16 extends 15's governor into quantitative runtime policy

Advantages of keeping as appendix:
- Self-contained within one paper
- The R_t inequality is the governor expressed as a single formula — it's the payoff of §4

**Recommend: decide after v0.3 is done.** If §4 feels complete without C, split it out. If §4 feels like it needs the punchline, keep it.

**Single session, possibly two** (the math is dense).

Workflow:
1. The Reynolds number analogy is a design heuristic, not a physical isomorphism — the text already caveats this but it needs to stay prominent
2. Evidence integrity (E_t) operationalization is the hardest part — Q_t, PV_t, Rep_t, I_t need concrete examples per domain
3. Glass cannon sensitivity (§C.11) is the "oh shit" moment — 10x evidence degradation + 10x delay spike = 100x risk. Make it visceral.

**Session protocol:**
- Claude: math verification, dimensional analysis, checking the algebraic equivalences
- ChatGPT: exposition, the intuition sections ("why evidence is the denominator"), concrete examples
- Driver: decide paper 15 appendix vs paper 16

**Done when:** R_t = P·D/E is fully derived with dimensional analysis checked, E_t components have at least one concrete operationalization per domain studied, and the binding policy inequality is shown to be algebraically equivalent to the receipts-as-currency formulation.

**Output:** Either updated Appendix C in paper 15, or draft of paper 16

---

## v0.5 — Falsifiability, Related Work, & Discussion

**Source material:** Project paper sections 5.1–5.3 and 6.1–6.5

**What's new:**
- Falsifiable claims (4 claims with explicit falsification conditions and status)
- Testable predictions (4 predictions)
- How to falsify the framework (3 methods + strongest adversarial target)
- External validation opportunities (incident response, CI/CD, content moderation)
- Related work positioning (Ashby/Beer/Wiener, Laprie, Leveson, Ramadge/Wonham, Boyd/OODA, Hollnagel, queueing theory)
- External corroborations (decision cycles, metric collapse, safety engineering drift, queueing distinction)
- Limitations and "doesn't apply" examples
- Why this matters (theoretical, practical, methodological)

**Single session.**

Workflow:
1. Related work (§6.2–6.3) is the most politically sensitive section — this is where the paper positions itself relative to established fields. Claims need to be precise: "we formalize what they gestured at" is fine, "we supersede Leveson" is not
2. Limitations (§6.4) should be prominent, not buried — "doesn't apply" examples (PID controllers, pure scratch simulation, bribery, resource exhaustion) are important for credibility
3. The "why this took so long to discover" section (§6.1) is interesting but optional — decide if it adds or distracts
4. Falsification section needs to stay honest — "consistent with all fifteen case studies" is not "proven across all domains"

**Session protocol:**
- ChatGPT: good at related work synthesis and readable discussion prose
- Claude: good at checking that falsification claims are actually falsifiable and predictions are actually testable
- Driver: tone calibration — confident but not overclaiming

**Done when:** Every falsifiable claim has a concrete falsification method that an adversarial reviewer could execute, related work positions the framework without overclaiming ("formalizes" not "supersedes"), and limitations section names at least 4 system types where the framework does not apply.

**Output:** Updated paper with full §5 and §6

---

## v0.6 (Optional) — Paradox Reframings (Appendix B)

**Source material:** Project paper Appendix B (§B.1–B.5)

**What's new:**
- Sorites Paradox — classification granularity vs change granularity
- Ship of Theseus — underspecified commitment boundary
- Zeno's Paradox — frame rate mismatch
- Liar's Paradox — temporal ordering violation in self-reference
- Grandfather Paradox — contradictory temporal commitments

**Decision point:** Include, cut, or spin off as separate essay.

Arguments for including:
- Demonstrates framework reach beyond engineering domains
- The Ship of Theseus reframing (different C_k → different stable answers) is genuinely illuminating
- Already flagged as illustrative and non-essential — the caveats are in place

Arguments against:
- Invites philosophical objections that distract from the engineering contribution
- "Guy who published 15 preprints now explains Zeno" is a look
- The project paper already labels it as omitted from evaluation claims

**Recommend: write it, park it, decide at v1.0 integration time.**

**Single session if pursued.**

**Session protocol:**
- ChatGPT: strong on the philosophical exposition
- Claude: check that each reframing actually uses the formalism (C_k, Δt, fast/slow) and isn't just hand-waving
- Driver: taste call on whether this helps or hurts the paper

**Done when:** Each paradox reframing uses at least two formal elements (C_k, Δt, fast/slow, σ) and isn't just a prose analogy. If a reframing can't be grounded in the formalism, cut it.

**Output:** Draft Appendix B, held separately until v1.0 decision

---

## v1.0 — Integration

**Input:** v0.5 (or v0.6) paper + all session outputs

**Tasks:**
1. Integrate all sections into coherent flow
2. Ensure cross-references are consistent (section numbers, citation numbers)
3. Verify the abstract still accurately describes the paper
4. Update the introduction (§1.4 scope/claims) to match what's actually delivered
5. Final consistency audit: every Δt, σ, C_k usage matches definitions
6. Reconcile any redundancy between domain instantiations and the summary table
7. Decision: Appendix C in or out? Appendix B in or out?
8. PDF conversion (pandoc, xelatex, Libertinus fonts — known working pipeline)
9. Publish on Zenodo, mint DOI, update README

**Done when:** The paper reads as one coherent document (not stapled-together sessions), the abstract matches the delivered content, and a cold reader could follow the argument from Definition 1 through to the governor pattern without referring to external papers.

---

## Empirical Note: Internal Telemetry vs External Measurement

**Context:** The delta-t-detector reference implementation (see `git/detector/`) found that temporal-coherence features (confidence slope, entropy trajectory) are useful as triage telemetry but do not function as reliable standalone gates. Internal dynamics saturate on fluent generation regardless of truthfulness; the dominant signal comes from external measurement (resolver-backed anchor validation — citation DOIs, URLs, arXiv IDs).

**Implication for the paper:** This *supports* the framework's central claim — failure arises when commitment closes the loop without an external reference. The meaningful clock is the verification layer, not internal dynamics.

**Where it lands:**
- **v0.2 Session 2B (§3.2 LLM Hallucination):** The canonical instantiation should note that T_commit for LLMs is not the confidence slope but the communicative closure (C1). Internal timing proxies saturate; the measurable Δt is between output commitment and external verification.
- **v0.3/v0.4 (Governor / Risk Index):** Evidence integrity (E_t) operationalization should explicitly distinguish internal telemetry (triage-grade, conditional) from external measurement (gate-grade, resolver-backed). This motivates the evidence minimum / fail-closed gate design.
- **v0.5 (Falsifiability):** One falsifiable prediction: "TC as standalone detector will underperform resolver-backed measurement in fluent-generation regimes." Status: confirmed by detector implementation.

**Insert for the paper** (engineering register, not book register):

> *Note on internal telemetry vs external measurement.* Temporal-coherence features (e.g., confidence slope, entropy trajectory) are useful as triage telemetry but do not function as reliable standalone gates. Empirical evaluation shows internal dynamics saturate within the generator; the meaningful clock is the verification layer. This supports the framework's central claim: failure arises when commitment closes the loop without an external reference.

**Keep the institutional/temporal narrative version for the chronopolitics book, not here.**

---

## Session Protocol (All Sessions)

1. **Input**: current published version + relevant project-paper section + any prior session outputs
2. **Draft**: one model drafts the new section
3. **Audit**: other model checks consistency with existing formalism and prior papers
4. **Integration**: driver merges into the versioned paper, resolves conflicts
5. **Review**: quick read-through for tone, overclaiming, and internal consistency
6. **Publish**: mint new version on Zenodo when the increment is clean

## Role Guidance

- **ChatGPT**: prose drafting, exposition, readable narratives, related work synthesis, philosophical content
- **Claude**: formalism verification, cross-paper consistency, threat model rigor, math checking, PDF pipeline
- **Driver (you)**: architectural decisions, tone calibration, what stays/goes, version gating, Zenodo publishing
