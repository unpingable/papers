# Plain-language summary

**Companion to:** *Cybernetic Fault Domains: When Commitment Outruns Verification* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Ordinary backlog is inconvenient; unverified actions becoming irreversible are more dangerous. A system enters the paper’s target condition when it can commit a consequential state change before verification and response can finish, then repeats that crossing often enough for unverified state to accumulate.

The problem appears different in software agents, organizations, security systems, platforms, and model evaluation because each has a different point of no return. The paper asks for a common way to name that boundary without pretending the later failure symptoms are identical.

The paper defines a commitment boundary, a correction horizon, the lag between commitment and completed verification, and a boundary load that counts unresolved crossings. Its containment pattern is a governor: proposals remain proposals until a separate mechanism checks a typed precondition, decides whether the action may cross the boundary, and records the result. The `agent_gov` specimen implements that pattern for code and tool calls, with implementation claims mapped to tests for guarded transitions, evidence, receipts, scope, and retry limits.

The resulting engineering question is concrete: where does this action become hard to reverse, and what can still stop it before then? A governor has to interpose on that path; advice, warnings, or logs produced after commitment do not perform the same job. The paper supplies shared measurement language for comparing this failure shape across domains without claiming that their downstream failures are identical.

## Claim boundary

The current implemented scope is one domain: a code/tool-call governor for language-model agents. The other domain mappings are hypotheses, not conforming implementations. There is no controlled governed-versus-ungoverned deployment study, no independent replication, and the thresholds and risk components require domain-specific calibration. One of the 37 mapped enforcement claims lacks a direct test. Compromised hosts, lying tools, evidence laundering, rubber-stamping, and verification-queue capacity remain outside or incomplete.

Later formal admissibility work supplies useful comparison vocabulary, but it does not certify `agent_gov`, the 37 claims, cross-domain generality, evidence honesty, or runtime conformance. Those require explicit adapters and separate verification.

## Read the paper

- [Manuscript source](cybernetic-fault-domains-v1.0.md)
- [Rendered PDF](cybernetic-fault-domains-v1.0.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18686130)
- [Zenodo record](https://zenodo.org/records/18686130)
