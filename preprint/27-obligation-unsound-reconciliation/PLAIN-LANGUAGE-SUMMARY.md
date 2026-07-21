# Plain-language summary

**Companion to:** *Ephemerality Is a Transition Property: Obligation-Unsound Reconciliation in Kubernetes and Other Control Loops* (Δt Paper 27)

**Version/status:** v1.0, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A reconciliation controller can restore the desired visible state while destroying what an operator will later need to understand the failure. A pod is replaced and service becomes healthy, but its logs, substrate accusation, causal history, or chain of custody disappear during recovery. The controller converged correctly; the transition left the operator unable to testify about what happened.

The paper models the controller as acting on a lossy view of a richer substrate. If two substrate states look identical to the control plane but leave different investigative or custody duties, the controller has collapsed distinctions that operators still need. The paper calls this an **obligation-unsound quotient** and proposes **transition admissibility** as a safety property separate from convergence.

Under that property, every affected obligation receives a recorded outcome: preserved, transferred, discharged, degraded with a receipt, or retained as an open finding. Silence is the failure. Receipts must outlive the obligations they cover and sit outside the audited action's authority. This lets a controller recover service without falsely implying that evidence is intact, the substrate is clean, or the investigation is closed. Convergence describes the destination; transition admissibility preserves the trail.

## Claim boundary

An archived scratch Lean companion contains three local accounting proofs, but its horizon result is vacuous while `H ≡ 0`, and two case-level theorems remain `True` placeholders. The file is not imported by the current stable Lean surface. The distributed receipt-substrate condition, three separate durability horizons, recursive audit governance, and runtime conformance remain paper-level or future work.

**Post-publication relationship note:** later Governed Admissibility Calculus and BreakGlass work supplies nearby vocabulary for origin-bound history and audit refusal, but there is no reviewed adapter from P27’s accounting and audit-state model, no P27 instance, and no discharge of its placeholder or horizon theorems. Proximity is not closure.

## Read the paper

- [Manuscript source](obligation_unsound_reconciliation.md)
- [PDF](obligation_unsound_reconciliation.pdf)
- [Directory guide](README.md)
- [DOI and Zenodo record](https://doi.org/10.5281/zenodo.20275071)
