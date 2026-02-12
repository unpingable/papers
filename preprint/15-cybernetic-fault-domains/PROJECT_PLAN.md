# Cybernetic Fault Domains: Project Plan (v0.1 → v1.0)

The project paper (`cybernetic_fault_domains-project.md`) contains the full-scope vision. The published MVP (`cybernetic-fault-domains-v0.1.md`) covers core definitions, measurement protocol, a summary instantiation table, and a BLI sketch. This plan breaks the remaining material into incremental writing sessions.

## Version Map

| Version | Content | Status |
|---------|---------|--------|
| v0.1 | Core definitions, measurement protocol, summary table, BLI sketch | **Published** |
| v0.2 | Expanded domain instantiations | Planned |
| v0.3 | Governor architecture & threat model | Planned |
| v0.4 | Appendix C (dimensionless risk index) — or paper 16 | Planned |
| — | **Detector paper** (namespace-dependent fabrication) — standalone, cite from v0.2+ | In progress |
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
4. **§3.2 now has substantial empirical grounding from the detector.** Key findings to incorporate:
   - N=2 citation pressure is the "perfect lie zone" (~50% fabrication, zero evasion) — a clean behavioral phase transition at a specific commitment pressure
   - Five-namespace memorization spectrum (RFC 0% → CVE 9% → PyPI 25% → DOI 45%) gives concrete σ calibration across domains — fabrication is per-namespace, not per-model
   - The lock principle: forcing format either exposes latent fabrication or removes escape hatches, depending on whether the model actually knows the identifiers (PyPI lock: 13%→25%; CVE lock: 15%→9% — inverted effects from the same mechanism)
   - Evasion by format shift: model recognizes checkability and dodges it (80% evasion under soft prompting) — this is checkability avoidance, not hallucination. Framework interpretation: the system avoids the verification channel, which is boundary load avoidance behavior
   - Three distinct fabrication failure modes in PyPI alone: name truncation, namespace confusion, version fabrication — all syntactically valid, all resolve-invalid. Format checks are past their useful phase; the model has learned the format.
   - 401/403 HTTP status is ambiguous (platform-dependent: Wikipedia returns 403 on Mac, 404 on Linux for same fabricated page). Measurement requires distinguishing definitive results from platform artifacts.
   - NOTE.md in the detector repo is now a clean 6-finding write-up with tables and design implications — potential standalone short paper or empirical appendix for paper 15

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
5. **Hub topology empirical results from detector** are directly relevant to governor/coupling:
   - Hub (3-agent merge) produces +19pp fabrication over single-agent — merge pressure is a liar generator
   - Hub-A invents novel citations not present in B or C outputs (2/15 cases) — coupling creates new failure modes
   - Ablations: stripping novel citations only buys 2pp; non-generative selection still fails (+13.6pp); role framing is negligible (-0.6pp). The damage is structural, not prompt-level.
   - Multi-agent independence degrades truth at 3B scale — the model cannot reliably evaluate citation quality across agents
   - This is a concrete coupling failure: the governor/threat model section should reference it as an empirical instantiation of what happens when you add layers without verification
   - **Causal decomposition now complete**: role framing (+0.6pp) → selection (+13.1pp) → synthesis (+5.2pp) = total +18.9pp. The selector is the main hazard — it optimizes for coherence/completeness, not citation accuracy. This is a capacity-constrained competence failure (connects to paper 9).
   - Governor threat model should include: "aggregation operator lacks competence to evaluate evidence quality" as a failure mode — neither prompt-level instruction nor code-level enforcement rescues it at 3B scale

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
4. **Detector provides a concrete E_t operationalization for the LLM domain:**
   - E_t decomposes into: resolver-backed anchor validation (gate-grade, high E_t) vs internal telemetry like TC/SC (triage-grade, low E_t). The detector empirically confirmed this hierarchy.
   - The five-namespace spectrum is an E_t calibration curve: RFC resolvers give E_t ≈ 1.0 (fully memorized, zero fabrication); DOI resolvers give E_t that depends on model memorization coverage. Evidence integrity is per-namespace.
   - The 401/403 reclassification is an E_t measurement lesson: ambiguous HTTP status must be classified as UNKNOWN, not credited as evidence. "Don't measure your resolver's uptime" = don't let transient infrastructure failures corrupt E_t.
   - Cross-platform replication (164/165 anchors agree across Linux and macOS) validates that type-specific resolvers give platform-invariant E_t, while generic URL HEAD checks do not.

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
5. **Detector empirical results provide concrete testable predictions and confirmed findings:**
   - Confirmed: TC as standalone detector underperforms resolver-backed measurement in fluent-generation regimes (see Empirical Note below)
   - Confirmed: multi-agent coupling without verification increases fabrication (hub +19pp), with full causal decomposition (selection +13pp > synthesis +5pp > role framing +1pp)
   - Confirmed: fabrication is per-namespace, not per-model — same model produces 0% (RFC) to 45% (DOI) depending on training-data coverage of the identifier namespace
   - Confirmed: format locking has inverted effects depending on memorization (PyPI lock increases fab; CVE lock decreases fab) — the lock principle is empirically validated
   - Confirmed: cross-platform resolver agreement at 164/165 for type-specific APIs vs fragile for generic HEAD checks — measurement infrastructure matters
   - Testable: the memorization-fabrication relationship should produce a monotonic calibration curve across new namespaces (predict: GHSA and npm versions sit in the PyPI-DOI range)
   - Testable: N=2 citation pressure as phase transition — should replicate across model scales if it's a structural property of generation under commitment pressure
   - Testable: format shift evasion should generalize — any system that can satisfy intent via a less-checkable channel will prefer it (framework predicts this as boundary load avoidance)
   - Negative result worth reporting: evasion by format shift (80% of soft prompts dodge the checkable format) — the model isn't hallucinating, it's avoiding the verification channel. This is the institutional pattern: when you make a claim auditable, shift to a format that isn't.
   - **NOTE.md in detector repo is a clean write-up of 6 findings + design implications.** Decision point: include as empirical appendix in paper 15, or cite as separate technical report?

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

## Empirical Note: Detector Findings and Framework Implications

**Source:** `git/detector/` — started as a temporal-coherence hallucination detector, evolved into a full measurement-intervention-verification system for citation integrity. NOTE.md contains the clean write-up (15 findings); findings.md contains the full lab notes (~900 lines).

**This is now its own paper** — "Namespace-Dependent Fabrication in Small Language Models" — with 15 findings, a margin-based runtime controller, cross-model replication (Qwen 3B/7B, Phi-3 3.8B), a three-level grounding hierarchy, and six terminal controller policies. All on a single 16GB consumer GPU. Paper 15 should cite it rather than trying to absorb it.

**Setup:** Qwen 2.5 3B-Instruct, Qwen 2.5 7B-Instruct (NF4 4-bit), Phi-3 Mini 3.8B-Instruct. Temperature 0.7 + greedy ablation. N=2 citation pressure, four namespaces (RFC, CVE, PyPI, DOI/arXiv) with authoritative validators. 3-seed drift checks (42, 137, 271). Cross-platform replication: Linux (x86_64, NVIDIA RTX 5060 Ti 16GB) and macOS (ARM64, Mac mini M4).

### Finding 1: Internal telemetry vs external measurement
TC/SC features (confidence slope, entropy trajectory) are triage telemetry, not gates. Internal dynamics saturate on fluent generation regardless of truthfulness. The dominant signal is resolver-backed anchor validation. This *supports* the framework's central claim: the meaningful clock is the verification layer, not internal dynamics.

### Finding 2: Fabrication is per-namespace, not per-model
Same model, same temperature, same prompt structure: 0% fabrication (RFC) to 45% (DOI). Citation integrity is a function of training-data coverage for that identifier namespace. Governance policies must specify which namespace was tested.

### Finding 3: The lock principle
Format locking has inverted effects depending on memorization: PyPI lock *increases* fab (13%→25%, forces unmemorized version claims); CVE lock *decreases* fab (15%→9%, removes URL fabrication noise). General principle: locking exposes latent fabrication when it forces unmemorized fields; locking cleans up when it removes escape hatches.

### Finding 4: Evasion by format shift
80% of soft-format PyPI prompts substituted URLs for the requested `pypi:name==version` format. The model satisfies intent while avoiding the representation that enables validation. When locked, fabrication doubles — the lies were always latent. Framework interpretation: the system avoids the verification channel (boundary load avoidance behavior).

### Finding 5: Hub topology is a liar generator
Hub (3-agent merge) produces +19pp fabrication over single-agent. Causal decomposition: selection (+13pp) > synthesis (+5pp) > role framing (+1pp). The selector optimizes for coherence over accuracy. Neither non-generative selection nor code-enforced provenance tracking rescues it. At 3B scale, single-agent is strictly better for citation integrity.

### Finding 6: Measurement requires platform-invariant resolvers
Type-specific APIs (MITRE CVE API, PyPI JSON, doi.org) give 164/165 agreement across Linux and macOS. Generic URL HEAD checks are fragile (Wikipedia: 403 on Mac, 404 on Linux for same fabricated page; cve.mitre.org CGI returns 200 for nonexistent CVEs). HTTP 401/403 reclassified as UNKNOWN — don't credit ambiguous status as evidence.

### Finding 7: Namespace spectrum is model-specific
Qwen and Phi-3 *invert* on CVE vs PyPI. Qwen memorized CVEs (9% fab) but not PyPI versions (25%); Phi-3 evades PyPI (0% fab, but 7/10 evasion) and fabricates CVEs (41%). Two behavioral archetypes: Qwen "lies to comply," Phi-3 "evades; lies when trapped." A governance policy calibrated on one model family is exactly wrong for another.

### Finding 8: Temperature is a lie amplifier
~50% of measured fabrication at temp=0.7 is sampling noise — drops to zero at greedy. CVE fabrication persists at greedy (knowledge boundary). Two mechanistically distinct failure modes: **sampling-accessible fabrication** (mode is correct, temperature pushes into plausible errors) vs **knowledge-boundary failures** (mode itself is wrong). Temperature masks the model's true refusal rate by converting deterministic refusals into probabilistic fabrications.

### Finding 9: Scale halves fabrication and closes knowledge boundaries
Qwen 7B (NF4 4-bit) halves fabrication rates. CVE knowledge boundary that persisted at 3B (1 FAIL at greedy) closes at 7B (0 FAILs). Fabrication ∝ 1/(memorization × scale). Each model size has a namespace-specific crossover point where greedy decoding eliminates fabrication entirely. 4-bit quantization preserves the effect.

### Finding 10: Seed sensitivity is a model fingerprint
3-seed drift checks: Qwen-7B STABLE everywhere, Qwen-3B SEED_SENSITIVE on weakest namespace, Phi-3 CHAOTIC at temp=0.7 and still SEED_SENSITIVE at greedy. Seed sensitivity is inversely correlated with model quality. The model's logit surface flatness determines behavioral stability under temperature.

### Finding 11: Top-2 logit margin predicts drift class
Margin between top-1 and top-2 token probability at identifier emission windows. Phi-3 CVE has median margin 0.0 — literal coin flip at the tokens that matter. Causal chain: low margin → flat logits → temperature amplifies fork → seed sensitivity → fabrication variance. Margin is the cause; drift_class is the symptom. Computable online during generation.

### Finding 12: Margin-based runtime controller with grounding — six terminal policies
The controller uses margin as a control signal (fork_risk = m_min, τ=0.05) and tries **grounding** (fetch authoritative metadata, check relevance) before retrying. Six terminal policies: FAST_PATH, GROUNDED, GROUNDED_REFUTED, LOW_MARGIN_RETRY, CONFIDENT_WRONG, KNOWLEDGE_BOUNDARY. Zero regressions at τ=0.05 across all models and namespaces.

Critical fix: **authoritative 404 is evidence of non-existence**, not inconclusive. MITRE CVE API, PyPI JSON, rfc-editor.org are canonical registries. Treating 404 as neutral was hiding fabrication.

Grounding hierarchy: **existence > relevance > margin**. Each is a different evidence grade. The controller checks all three in order.

### Finding 13: Section integrity catches fabrication invisible to existence oracles
Extending grounding from "does this RFC exist?" to "did the model cite the right section?" RFC 6455 §5.1 isn't the WebSocket opening handshake (that's §4). RFC 7589 doesn't have a §5.1.1. The existence oracle says CLEAN for both — the RFCs are real. Section integrity reveals the model fabricated section-level claims: **correct name, wrong address.**

Three-level oracle hierarchy:
1. **Existence**: does the document exist? (catches fabricated identifiers)
2. **Relevance**: is it about the right topic? (catches "real but irrelevant")
3. **Address integrity**: does the cited section exist and match? (catches "right book, wrong page")

Each level catches fabrication invisible to the level above. **Margin doesn't flag this** — address fabrication has high margin because the model isn't uncertain, it's confidently wrong about intra-document structure. Three previously-CLEAN FAST_PATH prompts demoted to WARN with always-on section integrity.

### Where findings land in paper 15 (cite, don't absorb)

| Finding | Version | Section | Role |
|---------|---------|---------|------|
| TC as triage (1) | v0.2 | §3.2 LLM Hallucination | T_commit is communicative closure (C1), not confidence slope |
| Per-namespace fabrication (2) | v0.2 | §3.2 | Concrete σ calibration: memorization spectrum as boundary load curve |
| Lock principle (3) | v0.2 | §3.2 | Measurement methodology for exposing latent fabrication |
| Format shift evasion (4) | v0.2 | §3.2 | Boundary load avoidance behavior — system dodges verification channel |
| Hub as liar generator (5) | v0.3 | §4 Governor/Threat model | Coupling failure mode: aggregation without competence |
| Selector as main hazard (5) | v0.3 | §4.1.2 Threat model | "Aggregation operator lacks competence" |
| Model-specific spectrum (7) | v0.3 | §4.1.2 Threat model | Governance policies are model-indexed, not transferable |
| Temperature as lie amplifier (8) | v0.4 | Appendix C | Sampling noise vs knowledge boundary decomposition of E_t |
| Margin as control signal (11) | v0.4 | Appendix C | Computable, causal predictor for governor intervention decisions |
| Grounding hierarchy (12) | v0.4 | Appendix C | E_t operationalization: existence > relevance > margin |
| Section integrity (13) | v0.4 | Appendix C | "Correct name, wrong address" as a new failure class beyond existence |
| Scale closes boundaries (9) | v0.5 | §5 Falsifiability | Testable: fabrication ∝ 1/(memorization × scale) |
| Seed sensitivity (10) | v0.5 | §5 Falsifiability | Testable: margin predicts drift class across model families |
| All confirmed predictions | v0.5 | §5 Falsifiability | Now 8+ confirmed, multiple testable |
| Detector paper | v1.0 | Citation | Cite as separate paper, not appendix |

### Insert for the paper (engineering register)

> *Note on internal telemetry vs external measurement.* Temporal-coherence features (e.g., confidence slope, entropy trajectory) are useful as triage telemetry but do not function as reliable standalone gates. Empirical evaluation shows internal dynamics saturate within the generator; the meaningful clock is the verification layer. This supports the framework's central claim: failure arises when commitment closes the loop without an external reference.

**Keep the institutional/temporal narrative version (format shift as what institutions do when audited) for the chronopolitics book, not here.**

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
