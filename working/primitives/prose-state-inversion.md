# Prose-State Inversion

**Status:** candidate
**Originated:** 2026-04-30 (DeepSeek "LLM-native antipatterns" sketch + chatty refinement; this session's P23 README/metadata Zenodo mismatch as worked minimal example)
**Primary home:** no current paper home — cross-cuts P23 (handoff briefings), P25 (proxy substitution), P27 (operator-unsound reconciliation), and the LLM-substrate / governor doctrine work. Sibling to Stale Binding; specialization to the prose substrate.

## Core definition

Prose-State Inversion occurs when a human-readable artifact becomes operationally authoritative over the structured state it merely describes.

## Formal object

Let $S$ be operational or structured state — typed, schema-bound, validator-reachable (e.g., `metadata.yaml`, an OpenAPI spec, a database row, a deploy manifest, a Lean theorem).

Let $P$ be a prose artifact describing $S$ at some past moment — a README line, a comment, a TODO, a markdown status block, a status field in a docstring, an endpoint description in a Confluence page.

Let $\rho: P \to \mathcal{X}$ be a lossy interpretation function recovering claimed state from prose (regex, human reading, LLM extraction).

$S$ has a validator $V$ that fails loudly on schema violation, type mismatch, missing field, or stale hash. $P$ has no analogous mechanism: prose has no schema, no expiry, no derived-from pointer, no last-checked-against timestamp, no regeneration path. Prose fails *socially* — someone reads it later and believes it.

## Failure predicate

Prose-State Inversion holds at time $t$ when:

1. $P$ describes operational state $S$.
2. $S$ can change independently of $P$ — no write-coupling, no regeneration trigger, no validator coverage tying $P$'s contents to $S$'s schema.
3. $P$ lacks a validator, expiry, regeneration path, or authority pointer back to $S$.
4. A reader, tool, or agent treats $P$ as authoritative for action, publication, deployment, configuration, or downstream conclusion.
5. The resulting action or conclusion is *document-correct relative to $P$* but *system-wrong relative to $S$*.

(5) is what distinguishes the failure from mere "documentation drift": the drift becomes operational.

## Minimal example

This session, 2026-04-30:

- `preprint/23-non-self-identical-controller/metadata.yaml` (typed, validator-reachable substrate) carried `version: "1.0"`, `doi: "10.5281/zenodo.19055415"`, `zenodo_url: "https://zenodo.org/records/19715302"`. Truth.
- `preprint/23-non-self-identical-controller/README.md` (prose) carried `**Status:** Preprint v0.1 (initial draft, 2026-04-21). Not yet pushed to Zenodo.` Stale.
- An LLM agent (Claude) doing repository-state reasoning read the README first because it was the legible front door. Concluded "P23 not yet on Zenodo." Propagated that conclusion into `docs/formalization-index.md` and into a survey table.
- The agent was document-correct (the README really does say v0.1) and system-wrong (Zenodo really does have v1.0 since 2026-04-24).
- The user caught the divergence externally; the LLM had no internal mechanism to detect it because the prose read path never crossed the validator path.

The schema substrate (`metadata.yaml`) had a validator chain (`tools/zenodo_validate.py`, `tools/doi_validate.py`). The prose substrate (`README.md`) had no analogous validator. Inversion: the unvalidated artifact won the authority contest because it was read first.

## Typical symptoms

- README status / DOI lines drifting behind `metadata.yaml` after release ceremonies.
- Zombie comments: `// TODO: if retry > 3, escalate to DLQ` while the actual retry policy lives three files away and has changed.
- Markdown frontmatter pressed into service as a config layer with no schema, no versioning, no ownership.
- Architecture docs cited as endpoint registries — "the user service calls `/billing-webhook/v1`" while runtime calls `/v2`.
- Test suites that hand-encode invariants described in prose without any production validator enforcing them — green CI for invariants that exist only in the test author's head.
- Prose IPC: services coordinating by writing to a shared README's "Current Status" section and parsing it with regex.
- LLM-generated infrastructure where a prose convention is treated as a contract: the LLM saw a pattern, inferred a contract, generated against the contract, left no receipt that the contract exists anywhere enforceable.

## Used by (related concepts)

- **Stale Binding** (sibling primitive). Stale Binding is substrate-general — truth moved, decision didn't notice — and applies to caches, aggregator priors, hat-x estimates, proxies. Prose-State Inversion is the *prose-substrate specialization*: the cache happens to be prose, which lacks expiry semantics by default. PSI inherits stale-binding pathology and adds the legibility-without-enforceability hazard.
- **Design-Basis Erasure** (sibling primitive). DBE is "controller transferred without its hazard model"; PSI is "claim transferred without its validator." DBE is the broader import-without-load-bearing-context pattern; PSI is the prose-specific case where presentation imports the claim and silently drops the schema's hazard handling.
- **P25** (substitution): when the proxy $V'$ on which the system regulates is *prose* and the source-of-truth $V$ is the typed substrate, PSI is one mechanism by which $V' \neq V$ silently.
- **P27** (operator-unsound reconciliation): an agent acting on $P$ can satisfy controller-side correctness against the document while violating operator-side soundness against the system. Document-correct, system-wrong is exactly the P27 wound; PSI is one route to it.
- **LLM-as-substrate concerns** (governor, agent_gov, continuity). LLMs treat prose as `documentation + intent + configuration + precedent + permission` simultaneously — a blob collapse. This makes them PSI-accelerators by default.

## Do not confuse with

- **Documentation drift** — folk-level symptom. Drift is necessary but not sufficient: documentation can drift without anyone acting on it. PSI requires (4) and (5) — the drift must become operationally load-bearing.
- **Stale Binding** — see above. PSI is a substrate-typed specialization, not a synonym. A typed cache with a stale TTL exhibits Stale Binding without exhibiting PSI; the cache fails loudly when the validator catches it.
- **Versioned Semantics** — different animal. Versioned Semantics: same bytes, interpreter changed. PSI: prose unchanged, structured state changed under it. The two can compose (an LLM reads stale prose under a new schema interpreter), but they are distinct failure modes.
- **Goodhart-style proxy gaming** — PSI requires no adversary. The prose is not gamed; it just decays. Goodhart is a substrate that PSI can host, not a synonym.
- **"Bad documentation"** — moralized framing that suggests the answer is "write better prose." It is not. The answer is to bind prose to substrate so prose cannot be the authority. Better prose still has no validator.

## Architectural rules

> **Authority must live somewhere typed enough to fail.**

The discipline is not "write better docs" — it is to bind every prose artifact to a substrate that fails loudly:

- `metadata.yaml` owns publication state; README renders/summarizes it (and ideally is generated, not hand-edited).
- OpenAPI / GraphQL schemas own endpoint shape; docs explain it.
- Tests / runtime validators own invariant checks; comments explain intent.
- Receipts own transitions; summaries explain consequence.
- Schema migrations own data shape; CHANGELOG explains the move.

The pattern is the same every time. **Treat any natural-language artifact that could have been schema'd as a vulnerability.** This is harsh and probably correct.

For LLM-mediated workflows specifically: when an agent's read path crosses prose before substrate, assume PSI risk and require validator-crossing before any conclusion is propagated. The drift trap added to MEMORY.md after the P23 incident is one local instance.

## Keeper aphorisms

> *The artifact is legible enough to be trusted but not structured enough to fail.* (chatty, 2026-04-30)

> *Natural language is allowed to explain state, but not to own state.*

> *If prose is the only place a fact exists, the fact is not operationally real.*

> *Markdown is where state goes to become plausible.* (chatty)

> *The system is fully documented. None of the documentation is accountable.* (chatty, on the LLM-amplified version)

## Open questions

- **LLM-amplification dynamics.** Is PSI rate super-linear in LLM-generated code volume? The "soft dependency" framing — a contract preserved only by shared human interpretation, with no compiler / schema / validator knowing it exists — predicts yes, because LLMs see conventions and infer contracts without leaving receipts that the contract exists. This is a falsifiable empirical claim about codebase aging.
- **Composition with Versioned Semantics.** When the schema interpreter changes during the prose-currency lag, what is the resulting failure mode? Plausible composite primitive; hold as candidate.
- **Adversarial PSI injection.** Can prose claims be deliberately seeded into a substrate (training data, copy-paste, "AI summary" caches) such that they get propagated as authority by downstream LLMs? Likely yes; this is roughly the substrate version of prompt injection, but persistent.
- **Self-application.** This primitive note is itself prose. Its own anti-pattern check is whether anyone treats *this file* as authoritative for action without verifying the underlying claims (schema definitions, validator coverage, P-S-I taxonomy of a real codebase). Acceptance test: catching that.

## Cross-references

- DeepSeek seed: 2026-04-30 thread on LLM-native antipatterns (README-as-database, zombie comments, frontmatter-as-config, prose IPC, soft dependencies).
- chatty refinement: 2026-04-30. Promoted "soft dependency" to its own framing; reshaped the failure predicate from `authority(P) > freshness(P)` motto into the five-condition chain (motto preserved as keeper aphorism, not predicate); bounded the scope (no MEMORY.md write, no directory restructuring, no broad paper-claim mapping); flagged the role-accretion gravity that wanted to memorialize this into a ministry.
- Worked minimal example: this session's P23 README/metadata Zenodo divergence and propagation chain.
