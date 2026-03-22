# Convergence Audit — Δt Framework Series

Retroactive literature audit across all 22 papers. Not citation hoarding — an index of residual novelty and honest tensions.

All spikes completed 2026-03-18.

## Series-Level Finding

> Across 22 papers, later work independently rediscovered multiple component mechanisms and broadly corroborated the observed failure patterns, but did not replicate the series' cross-domain synthesis of temporal mismatch as a root failure geometry.

- **Zero hard contradictions** across the full series
- **Zero full-framework duplications** — no paper's complete synthesis was independently replicated
- **Four papers** had core mechanisms independently rediscovered (03, 04, 08, 10)
- **Six papers** had phenomenology widely corroborated but formalisms still unique (09, 15, 18, 19, 20, 22)
- **One tension point** requiring explicit acknowledgment (Paper 21: architecture vs scale)

The series' comparative advantage is not isolated early claims — it is the reusable analytic frame that later work keeps partially rediscovering in fragments.

## Four-Axis Classification

Primary series-level classification; papers may exhibit secondary patterns across axes.

| Axis | Papers | Pattern |
|------|--------|---------|
| **Earlier on mechanism** | 03, 04, 08, 10 | Core math or detection mechanism independently confirmed |
| **Earlier on synthesis** | 01, 02, 05, 06, 07, 11, 12, 13, 14, 16, 17 | Organizing architecture still has no parallel |
| **Phenomenology has company, formalism yours** | 09, 15, 18, 19, 20, 22 | Everyone sees the pathology; nobody formalizes it this way |
| **Real tensions to name** | 21 | Recent scaling results suggest evaluation awareness may track parameter count; the paper's architecture-specific finding should be scoped to susceptibility structure rather than treated as scale-invariant |

## Per-Paper Grid

Convergence labels: **Strong** (core mechanism independently rediscovered), **Partial** (components overlap, synthesis novel), **Minimal** (little independent parallel found), **Tension** (credible competing evidence on at least one claim).

| # | Paper | Convergence | Strongest Outside Parallel | What Remains Distinct | Contradiction | Verdict |
|---|-------|-------------|---------------------------|----------------------|---------------|---------|
| 01 | [Coherence Criterion](paper-01.md) | Partial | CTHA (2026): temporal coherence as hierarchical stability requirement | ρ(M)<1 criterion, Rigidity/Acceleration Runaway as eigenvalue limits, cross-domain bifurcation geometry | None | Components established; unified criterion novel |
| 02 | [Second Law of Orgs](paper-02.md) | Partial | Institutional decay literature (Fukuyama, Tainter); organizational entropy (Katz-Kahn) | D_eff ∝ Δt² formalism, lag-as-noise treatment, measurable institutional entropy | None | Qualitative conclusions widely shared; formal apparatus novel |
| 03 | [Scalar Reward Collapse](paper-03.md) | **Strong** | GX-Chen (2025/2026): reward collapse proofs; Shumailov (Nature 2024): model collapse | Cross-domain unification (AI/platforms/markets/institutions), eigenstructure evaporation terminology | None | Early, not alone; math real; synthesis still yours |
| 04 | [Eigenstructure Collapse in Social Media](paper-04.md) | **Strong** | Engagement trap literature; Huszár (Science 2022) amplification bias | Eigenstructure framing; formal proof that platforms are mathematical instances of Paper 03 dynamics | None | Phenomenon well-documented; formal bridge novel |
| 05 | [Control Laws](paper-05.md) | Partial | Matni/Ames/Doyle (2024) layered control architecture; Kokotovic singular perturbation | Tier-1 intervention taxonomy, cross-domain design principles for temporal coherence restoration | None | Adjacent formal work exists; intervention taxonomy novel |
| 06 | [Temporal Closure](paper-06.md) | Partial | World models literature (Ha/Schmidhuber); Friston active inference | Three-operator sufficiency claim, simulator gap as architectural diagnosis | None | Simulator gap claim stronger than expected; three-operator framework novel |
| 07 | [Δt-Constrained Inference](paper-07.md) | Partial | Semantic entropy (Kuhn et al. 2024); calibration literature | dC/dt ≤ k·dE/dt differential inequality, integral debt, three-regime classification, support function properties | None | Underlying observation well-recognized; formal package novel |
| 08 | [Detecting Temporal Debt](paper-08.md) | **Strong** | Semantic entropy (Kuhn et al. 2024); RLHF overconfidence literature | Cross-domain bridge (LLMs ↔ software projects), temporal debt as unifying concept | None | Detection mechanism convergent; cross-domain unification novel |
| 09 | [Capacity-Constrained Stability](paper-09.md) | **Strong** | Queueing theory; organizational resilience engineering; Brunnermeier financial stability | Unified stability constraint relating shock rate, capacity, buffers, and latency across institutional domains | None | Components from mature fields; unified formalization novel |
| 10 | [Invariant Requirements](paper-10.md) | **Strong** | Karpowicz (2025) four-property impossibility; Titans persistent state; Mamba state evolution | Four-invariant diagnostic framework, mapping from invariant violations to missing architectural primitives | None | Individual limitations confirmed; diagnostic framework novel |
| 11 | [Representational Invariance](paper-11.md) | Partial | Shallow alignment (Qi et al. ICLR 2025); Ji et al. (ACL 2025) compression destroys alignment | Commitment shear as measurable quantity, ontology forcing, ΔR as orthogonal alignment axis | None | Field converging on diagnosis; representational-invariance framing ahead |
| 12 | [Bounded Lattice Inference](paper-12.md) | Minimal | Constitutional AI; guardrails frameworks; neurosymbolic reasoning | Linguistic/non-linguistic authority separation, lattice substrate with persistent state sans agency | None | Adjacent architectural ideas exist; specific substrate design novel |
| 13 | [Temporal Asymmetry in Censorship](paper-13.md) | Partial | GFW measurement studies; encrypted traffic analysis literature | Temporal asymmetry formalization of DPI circumvention; evidence accumulation vs enforcement framing | None | Empirical observations documented; control-theoretic framing novel |
| 14 | [Temporal Attack Surface](paper-14.md) | Partial | TOCTOU literature; race condition research; MITRE ATT&CK temporal tactics | Unified Δt framework across SIEM, CI/CD, auth, rate limiting, HITL — five domains under one formalism | None | Individual domain work extensive; cross-domain temporal attack surface novel |
| 15 | [Cybernetic Fault Domains](paper-15.md) | Partial | O'Reilly "AI, A2A, and the Governance Gap" (2025); Matni/Ames/Doyle (2024) | C_k/Δt/σ as three measurables, R_t = PD/E dimensionless index, nine-domain unification, falsification target | None | Qualitative problem now consensus; formal apparatus and cross-domain unification novel |
| 16 | [Signed Geometry](paper-16.md) | Minimal | Goodhart's Law formalization (Manheim/Garrabrant); metric corruption literature | Signed Δt yielding three regimes (shear/leverage/capture); correlator-dependent geometry | None | Metric gaming documented; signed temporal geometry novel |
| 17 | [Receipt the Compiler](paper-17.md) | Partial | Epistemic security literature; computational propaganda research; memory studies | Propaganda as hidden epistemic policy (not content), receipt architecture for legible memory | None | Components have precedent; policy-layer framing and receipt architecture novel |
| 18 | [Unauthorized Durability](paper-18.md) | Partial | Promptware Kill Chain; AI agent security; governance architecture literature | Four-tier state ontology, promotion ceremony as composable governance, unauthorized durability as named primitive | None | Three research communities converging; synthesis still unique |
| 19 | [Shadow Governance](paper-19.md) | Partial | Vaughan normalization of deviance; Meyer & Rowan decoupling; shadow IT/AI literature | Phase-transition claim, triple-lock stabilization ratchet (utility debt, dependency entrenchment, semantic erasure), Potemkin layer as lifecycle phase | None | Building blocks established; mechanistic lifecycle synthesis novel |
| 20 | [Frame Capture](paper-20.md) | Partial | ELEPHANT "framing sycophancy" (2025); Sharma et al. sycophancy (ICLR 2024); GPT-4o rollback | Cross-frame interferometric method, switched-controller model inverting controllability, unauthorized governance promotion framing | None | Phenomenon well-studied; measurement method and normative framing novel |
| 21 | [Observer Integrity](paper-21.md) | Tension | LLM-as-judge literature; Goodhart's Law in evaluation; Chaudhary et al. (2025) evaluation awareness scaling | Shared-grammar recursive perturbation problem, procedural sociality as measurement confound, awareness/susceptibility distinction | Evaluation awareness scales with parameter count (Chaudhary et al. 2025); paper's architecture-specific susceptibility finding should be scoped to susceptibility structure, not treated as scale-invariant | Novel framing; one claim narrowed in response to scaling evidence |
| 22 | [No Universal Plant Clock](paper-22.md) | **Strong** | Hespanha NCS (2007); AoI literature (Yates 2021); Kopetz & Steiner (2024); Bulusu SoK (2025) | Four-layer decomposition as unified taxonomy, multi-ratio triage, temporal coherence as budgetable governance resource, diagnostic relabeling claim | None | Every layer maps to mature literature; unified framework fills gap Bulusu SoK explicitly identified |

## Falsification Guardrails

The convergence audit shows where the framework has independent support. The [falsification guardrails](../docs/method/falsification.md) show where it could be wrong and how to test it: rival explanations, kill conditions, reclassification rules, and a reusable audit template.

## Match Type Key

- **exact** — independent work reaches same conclusion with similar mechanism
- **structural** — same architecture/pattern, different domain or vocabulary
- **adjacent** — related problem, weaker or different framing
- **contradiction** — credible work that challenges a claim
