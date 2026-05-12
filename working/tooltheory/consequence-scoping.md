# Consequence scoping

**Slogan:** Evidence may authorize inquiry, caution, or advisory posture without authorizing closure.

**Operational phrasing:** *"This evidence supports caution, triage, or further inquiry; it does not support closure on the underlying claim."*

**Source:** P25 §3.1 / §6.1 admissibility frame; grok reviewer Q3 + chatty lane-mapping 2026-05-12.

## What it is

P25 names responsibility as living at the consequence boundary — not for failing to observe the unobservable, but for *treating proxy evidence as target authority*. Consequence scoping is the operational form of that discipline: evidence has scope; scope limits consequence. The same observation can authorize advisory caution while failing to authorize binding action.

The radioactive version of the claim — *"I am regulating contamination risk, not truth"* — is socially difficult to adopt. The consequence-scoped version — *"this supports caution, not closure"* — is the rhetoric coalitions can actually accept without confessing they're vibe-policing.

## Tool mapping

- **Agent Governor (AG):** advisory verdicts vs authorized verdicts. Proxy evidence → advisory basis; proxy evidence -/-> target-binding authorization. Basis / standing / effect split applies directly.
- **Wicket:** in CI, diff touches authority-bearing surface → evidence supports "review required" but not "safe to merge." License / NOTICE / identity attribution / package-permission / GitHub-Actions-permission changes are the worked surfaces. Distinguish:
    - "this looks suspicious, ask a qualified owner";
    - "this violates a known rule, block";
    - "this has standing, permit";
    - "unknown authority surface, deny or require review."
- **NQ:** scope-tagged testimony. Witness can say what it testifies *to* and what it does *not*.

## Lean candidates

- `proxy_evidence_does_not_authorize_target_closure`
- `advisory_basis_does_not_authorize_mutation`

## Promotion gate

Promote to project spec (downstream repo) when an NQ/AG/Wicket implementation hits a case where the advisory-vs-authorizing distinction makes a load-bearing difference and the current code can't express it cleanly.
