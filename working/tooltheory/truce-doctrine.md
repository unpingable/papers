# Truce Doctrine: Contradiction, Remediation, and Binding State

Process is the truce over which declarations may bind future action.

This note records a terminology clarification, not a new kernel module. The existing Lean/kernel surface already implements the relevant distinction.

## Existing kernel support

- `Authority.lean` already treats conflicting precedence as authorization-blocking:
  - constructor: `PrecedenceVerdict.conflicting`
  - theorem: `conflicting_precedence_never_authorized`
- `RepairOperator.lean` already supplies the richer remediation layer:
  - `ratify`
  - `reissue`
  - `quarantine`
  - `repeal`
  - `defer`

## Doctrine

Official contradiction blocks authorization.

Remediation accounts for force outside authorization.

A contradiction among admissibility/precedence claims is not a two-party dispute to be adjudicated by picking a winner. The kernel's stronger posture is refusal-and-escalation: contradiction defeats authorization rather than becoming an opportunity for an adjudicator to launder one side into validity.

Shadow constraints are not competing lawful claims. They are incidents: causal force operating outside the declared admissibility model.

## Rejected sketch

Do not introduce an `adjudicator-picks-a-winner` model for conflicting admissible declarations. That model is weaker than the existing kernel stance.

Adjudication-style framing risks importing a courtroom metaphor where the kernel already has a stricter rule: contradiction blocks authorization; repair/remediation handles damaged, stale, shadowed, or externally forced authority.

## Summary

- Causal force is not admissibility.
- Binding requires admissibility.
- Official contradiction blocks authorization.
- Remediation accounts for force outside authorization.
- Process is the truce over which declarations may bind future action.
