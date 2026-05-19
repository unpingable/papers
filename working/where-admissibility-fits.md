# Where Admissibility Fits

**Status:** working note / application map. Not a paper, not a roadmap, not a roadmap-in-disguise.
**Origin:** 2026-05-09 multi-model brainstorm (claude-code-papers / claude-agent-governor / claude-nq) synthesized through ChatGPT.
**Audience:** people approaching the admissibility work from outside the haunted machinery — platform engineers, ML/evals practitioners, security/compliance, formal-methods folks, observability people. Anyone who already builds systems that take claims and convert them into permission to act.

## What this note is and is not

This is **applicability mapping**, not a roadmap. The point is to make the admissibility constellation legible to people who already work on adjacent shapes: to say *here is where this lands inside vocabulary you already have*, not *here is what you should build next*.

The author will not pursue most of these mappings. They are documented so that other people can recognize the shape, borrow what is useful, and build adapters where the fit is good — without first having to swallow the entire ontology.

> *This is a boundary object, not a platform pitch.*

## The common question

Every shape below is, underneath, asking one question:

> **May this claim be used to authorize this consequence?**

Different communities have different vocabularies for the parts. The constellation supplies a compact decomposition.

> **Admissibility is the layer where Δt becomes enforceable or evasible.** Other layers can be timely or untimely without temporal coherence becoming jurisdictional. (Multi-model relay 2026-05-18; longer multi-axis form at `agi-requirements-framework.md:767`.)

## Core pattern

Every admissibility decision involves seven parts:

- **Claim** — what is being asserted
- **Evidence** — what the claim is backed by
- **Standing** — whether the claim has the position to bind
- **Scope** — what the claim is qualified to authorize
- **Precedence** — which claim wins under conflict
- **Consequence** — the action being authorized (or refused)
- **Receipt** — the immutable record of the verdict, including refusals and gaps

The kernel ruling is small and structured: *authorized*, *denied*, *gap*, *unaccounted*. The space is deliberately mean and underfed; expressiveness lives in the adapters and the elaborator, not the kernel.

## Existing software analogues

These are shapes the work already is, with vocabulary borrowed from elsewhere.

### Admission controllers
Kubernetes `AdmissionReview → AdmissionResponse`. CI release gates. GitHub merge gates. Deploy preflights. MCP tool-call authorization. Different vocabulary, same job: a structured ruling on whether a requested operation may proceed, separate from the operation itself.

### Policy decision points (PDP / PEP split)
OPA, Cedar, XACML. The admissibility kernel sits at the PDP role — but with a deliberate refusal to grow into a policy DSL. (See *Non-goals* below; this is the OPA/Rego gravity well that sinks projects of this shape.)

### Typecheckers and proof kernels
Small trusted kernel; large, dirty elaborator. Conformance fixtures as theorems. Lean's ~10k-line kernel + 200k-line elaborator is the architectural prior. The admissibility kernel is small enough to be Lean-checked outright; that is one of the candidate Lean shadow paths in `~/git/lean/LeanProofs/Admissibility/`.

### SMT / solver calls
SAT / UNSAT / UNKNOWN maps directly to authorized / denied / (gap + unaccounted). *UNKNOWN is admissible* is the same doctrinal move as the open-finding discipline: a structured non-answer is a real verdict, not a failure.

### Capability systems
Macaroons, attenuated authority, caveats, deferred discharge proofs. The `*_CALLER_ASSERTED_UNVERIFIED` discipline in agent-governor is what macaroons call third-party caveats. Provenance is a caveat, not a permission.

### Federal Rules of Evidence (legal analogue)
"Admissibility" is borrowed deliberately from FRE 401–403. The constellation asks the federal-rules-of-evidence question for agent operations: *may this claim be used to authorize this consequence?* The legal vocabulary is older and crisper than the software vocabulary; institutions building adapters should consider borrowing it directly.

## Adjacent domains (light adapter, same kernel)

### Observability and monitoring
Monitoring asks *what happened*. Admissibility asks *whether what happened may be used*. NQ-shaped systems sit here: not a monitoring replacement, but a witness-standing broker that runs alongside monitoring and answers a strictly narrower question. The natural consumer is a downstream that prefers *cannot-testify* over *no-problem-found* — adversarial domains, high-stakes ML/safety, legal/compliance.

### AI evals and LLM ensembles
*Eval pass is not automatically competent evidence for deployment authority.* Every "we ran the eval and the model passed" is a multi-witness aggregation: eval framework as exporter, harness as transport, score aggregation as $D_A$. Self-consistency / multi-agent debate / N-of-M sample voting all routinely launder same-model agreement as corroboration. See [witness-invariance-composition](primitives/witness-invariance-composition.md) for the formal vocabulary; the keeper *agreement is not corroboration unless the witnesses fail independently* lands here directly.

### Supply-chain attestation (SLSA / in-toto / Sigstore)
Provenance, signed receipts, transitive trust — already half-admissibility-shaped. The gap: *provenance is not standing.* SLSA today does not have a structured place for "this attestation is qualified for this regime but not that one." Aggregator-contamination ($D_A$) shows up as which attestations get surfaced and how transitive trust is computed.

### Coordinated vulnerability disclosure (CVE / CVD)
A reporter discovers V in product P; a CNA (one of ~400 — Mitre, GitHub, Red Hat, Apple, etc.) mints a CVE-ID; the vendor confirms / disputes / scopes; NVD scores CVSS separately; downstream scanners, compliance, and procurement bind remediation. Seven-part mapping:

- **Claim:** *V exists in P versions R, allowing impact I via prerequisite C.*
- **Evidence:** PoC, reproduction, static-analysis trace, sometimes a working exploit.
- **Standing:** *forked across at least five roles* — reporter (claim) / CNA (publication-mint) / vendor (confirm/dispute/scope) / NVD (independent scoring) / downstream (remediation-binding).
- **Scope:** affected product+version range; expands post-publication as variants surface.
- **Precedence:** RESERVED / PUBLIC / DISPUTED / REJECT state graph; non-monotone in publication time.
- **Consequence:** patch obligation, scanner alert, compliance flag, procurement block, regulatory action (DORA, NIS2).
- **Receipt:** CVE record + CVSS vector + advisory. The CVE-ID is the canonical bearer.

Two worked examples illustrate that the kernel handles the strain without new primitives:

**DISPUTED is not gap.** A DISPUTED CVE carries reporter's positive claim and vendor's denial as concurrent first-class entries; both retain Receipt-issuing standing; consumers adjudicate downstream. The multi-mint allowance from `authority-observable-not-constructible.md` (each trust boundary mints its own Authority; consumers compose) encodes persistent multi-party disagreement without a "parallax" or "posted-disagreement" primitive. Cross-CNA scoring divergence (NVD vs. vendor CVSS) is structural permission, not bureaucratic dysfunction.

**Embargo as temporal-scope specimen.** Between reporter→vendor contact and publication, the CVE has standing inside the embargo group and none outside; publication is a scope-of-standing expansion at time T. Second named instance of the temporal-scope gap tracked at `admissible-recovery-semantics.md` §11 Open Question 5 and the Δt crosswalk above (specimen 1: evaluator-mutation laundering). Tracking, not promoting.

### Compliance and audit
A logged control is not necessarily evidence with standing. SOC2 / HIPAA / FedRAMP tooling routinely treats *the control was logged* as *the evidence has standing.* That collapse is exactly the gap the constellation targets. Auditors actually want the temporal-admissibility split (state moved / authority fell off / verdict at decision time); current tooling does not articulate it.

### Distributed systems
Quorum reads, multi-AZ failover, "replicated to 3 regions" — all treated as N-witness corroboration when the contamination basis (shared deploy pipeline, shared library version, shared NTP source, shared kernel) is undeclared. Jepsen / Aphyr / Marc Brooker have been arguing this for a decade in different vocabulary; S3 us-east-1, CrowdStrike, log4j, Fastly are textbook aggregate-WIF. The composition lemmas in [witness-invariance-composition](primitives/witness-invariance-composition.md) supply the formal frame.

### Multi-factor auth / defense-in-depth
"SMS + password" where both flow through the same compromised email recovery. "WAF + IDS + EDR all saw nothing" where all share the same signature feed. Orthogonality of the factors is itself a claim, almost nobody audits it. Agreement-as-anti-evidence is the sharp diagnostic.

### Bridge oracles / multi-source price feeds
Nominally N-of-M decentralized; in practice N wrappers around the same upstream feed. Existing oracle-manipulation attacks are exactly aggregate-WIF.

## Stranger shapes (where the kernel could go)

These are speculative — named so the doors exist, not opened.

- **Conformance suite.** SPEC + fixtures + multiple implementations as a doctrine standard. Web-platform-tests for admissibility. Turns "ratification surface" from a memory note into something other people can do work against.
- **WASM component.** Pure-logic admissibility kernel as an in-process gate, no IPC, no daemon. Lets the kernel ride into agent runtimes that won't accept a Python sidecar.
- **LSP-shaped admissibility server.** Long-running daemon, JSON-RPC, single-call per editor action. Editors consume it the way they consume a type checker.
- **Build-system gate (Bazel/Nix-shaped).** "Are these inputs sufficient for a hermetic action?" Receipts already look like content-addressed action receipts.
- **Smart-contract precondition gate.** `require` clauses as unstructured admissibility calls. Doctrine probably doesn't survive contact with on-chain incentive design, but the shape fits.
- **Insurance underwriting / claims adjudication.** Closest non-software analog with established institutional vocabulary. Worth borrowing language from.

## Non-goals

The kernel **does not** become any of these. They are gravity wells the work explicitly resists.

- Not a **policy language**. OPA/Rego gravity is real; the kernel must stay mean and underfed. Conditionals belong in the elaborator.
- Not an **observability replacement**. NQ-shaped systems sit beside monitoring, not in front of it.
- Not a **compliance platform**. Adapters can produce compliance-shaped receipts; the kernel does not encode any specific framework.
- Not a **universal agent runtime**. The kernel rules on whether actions are admissible; it does not orchestrate them.
- Not a **new orchestration system**.
- Not an **MCP server** as a transport-coupled service. (An MCP shim may exist; the kernel turning into one should not.)

## Integration principle

```text
Adapters may sprawl.
The kernel must not.
Receipts must remain comparable.
Fixtures must remain sovereign.
```

Or sharper:

> *The constellation is not a monitoring stack. It is an admissibility stack.*
>
> *Monitoring asks what happened. Admissibility asks whether what happened may be used.*

## Audience-shaped framings

For each, the move is the same: name the gap admissibility fills *inside the audience's existing vocabulary*, without claiming ownership of their domain.

- **Platform engineers** — admission gates, deploy gates, mutation preflights. The kernel is small enough to sit in front of, behind, or beside what you already run.
- **AI / tooling people** — tool-call authorization, eval competence, agent action receipts. *Your benchmark pass is not automatically competent evidence.*
- **Observability people** — witness standing, cannot-testify verdicts, anti-false-corroboration. Not a replacement; a strictly narrower question.
- **Compliance / security** — audit evidence competence, supply-chain provenance limits, attestation scope. *Provenance is not standing.*
- **Formal / spec people** — small kernel, conformance fixtures, multiple implementations, Lean shadow.

The rhetorical move: *these are not proposed expansions of the kernel. They are integration shapes. The kernel remains narrow; the adapters explain how other systems can consume or produce admissibility claims.*

## Candidate public framing (for later compression)

Not for the unpingable front page yet — but the seed of what eventually goes there:

> **Admissibility tools and doctrine for agentic and operational systems.**
>
> Compact frameworks for deciding when a claim, witness, or evaluation has standing to authorize a consequence. Sits in front of, behind, or beside policy engines, monitoring systems, CI gates, eval harnesses, and supply-chain attestation. Asks the narrower question: *may this claim be used to authorize this consequence?*

## Pointers into the existing work

This note collapses across several artifacts. For readers who want to dig:

- **Series papers (papers/preprint/):** P22 (foundational failure geometry), P25 (epistemic border control), P27 (obligation-unsound reconciliation). The published preprints are the formal substrate; this note is the application surface.
- **Primitives field notebook (working/primitives/):** [witness-invariance-failure](primitives/witness-invariance-failure.md), [witness-invariance-composition](primitives/witness-invariance-composition.md), [stale-binding](primitives/stale-binding.md), [zombie-obligation](primitives/zombie-obligation.md), [epistemic-threat-contamination](primitives/epistemic-threat-contamination.md), [attractor-admissibility-gap](primitives/attractor-admissibility-gap.md). See [primitives/README.md](primitives/README.md) for the field-notebook discipline.
- **Working notes (working/):** [admissibility-control](admissibility-control.md), [admissible-recovery-semantics](admissible-recovery-semantics.md), [boundary-composition-investigation](boundary-composition-investigation.md), [epistemic-border-control](epistemic-border-control.md), [sre-as-shock-absorption](sre-as-shock-absorption.md).
- **Lean formalization (~/git/lean/LeanProofs/Admissibility/):** Authority / StateTransition / Derivation / Execution / Corrective siblings; WitnessInvariance module with relational, typed-perturbation-relation, and regime-bounded forms.
- **Sibling implementations:** agent-governor (deployment substrate), NQ (witness-standing broker), Wicket (admissibility kernel). These live outside the papers repo and are not all public; the application shapes above describe what they instantiate.

## Open mappings (future work, not promised)

Things this note names but does not pursue:

- **Conformance suite formalization** — SPEC + fixtures + multiple implementations as a published standard.
- **Eval admissibility layer** — explicit treatment of eval-as-witness with declared regime and contamination basis.
- **Distributed-systems vocabulary fold-in** — connecting WIF-composition to the existing Jepsen / correlated-failure literature.
- **Insurance/legal vocabulary borrow** — adopting institutional vocabulary that is older and crisper than the software equivalent.
- **WASM / LSP / Bazel adapter shapes** — deployment surfaces beyond sidecars.

Each is a candidate door, not a commitment.

## Provenance

- **2026-05-09.** Multi-model brainstorm: user asked all three working claudes (claude-code-papers, claude-agent-governor, claude-nq) the same question — *what other software shapes does this work fit?* — then synthesized through ChatGPT. Each floor saw the same object from a different elevation: AG floor surfaced deployment/integration shapes (admission controllers, PDP/PEP, capability systems, WASM, LSP, conformance suites); NQ floor surfaced consumer-discipline shapes (compliance, ML evals, supply-chain attestation, CI gating) and the *cannot-testify-over-no-problem-found* downstream pattern; papers/lean floor surfaced formal-vocabulary shapes (distributed-systems consensus, LLM ensembles, MFA orthogonality, CI signal aggregation, oracles, multi-reviewer review, sensor fusion as positive reference).
- **ChatGPT (synthesis).** Identified that the three responses were not disagreeing but triangulating: Wicket as admissibility kernel, NQ as testimony/standing substrate, Lean/paper work as warrant layer. Coined the *boundary object, not platform pitch* framing. Drafted the structural shape this file follows.
- **claude-code-papers (this file).** Folded the synthesis into the working/ directory as an applicability map. Added repo-aware cross-references so the document is navigable, not just legible. Resisted scope expansion: this is staging for a later compressed front-page version, not the front page itself.
- Filed as working note. Not a paper. Not promised. Marked explicitly as boundary object — read by whoever is approaching the constellation from an adjacent vocabulary, not by people already inside it.
