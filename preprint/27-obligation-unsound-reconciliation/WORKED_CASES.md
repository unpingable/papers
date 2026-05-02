# Paper 27 — Worked Cases

**Purpose.** Force the transition-admissibility vocabulary from concrete reconciliation cases before promoting any missing Lean predicates. The cases drive the predicates; Lean follows the cases. Filing predicates in `~/git/lean/LeanProofs/Admissibility.lean` ahead of forcing cases would be constitution-by-typechecker — exactly the failure mode `memory/feedback-lean-debt-discipline.md` warns against.

**Discipline rule.** No new Lean predicate (e.g. `substrateAccusation`, `causalBinding`, `maskedByRecovery`, `orphanedCausality`, `receiptOutlives`) gets promoted to the formal layer until *at least two cases independently force it.* One case can be colorful; two cases start to define structure; three cases give the admissibility vocabulary without hallucinating a tiny courthouse inside Lean.

**Status.** Scaffold (2026-05-01). Scenario seeds transcribed from NOTES.md; all other fields are placeholders for population by the author. The three cases are the Masked / Orphaned / DegradedWithReceipt split named in P27's audit-state vocabulary.

---

## Case 1 — Masked Recovery

### Scenario
Pod fails on a suspect-disk node. Reconciliation drains and reschedules; the drain destroys useful logs (kernel messages, dmesg, container stdout); the replacement pod is scheduled onto a node in the same node class — same substrate risk, no record that the controller noticed.

### Binding / transition event

### Substrate state $B$

### Control-plane projection $K$

### Projection gap $\alpha: B \to K$

### Reconciliation action

### Convergence result

### Destroyed / degraded obligations
- Evidence:
- Causality:
- Custody:
- Authority:
- Continuity:
- Substrate accountability:

### Audit state
Masked.

### Why convergence-only correctness misses it

### Predicate forced

### Receipt requirement

---

## Case 2 — Orphaned Causality

### Scenario
Volume corruption is detected. A replica is restored from backup. By the time the corruption is investigated, the substrate event that caused it (scheduling history, hardware fault, neighbor-pod interference) has aged out of the retention window. The data is back; the causal chain to a specific substrate event is not.

### Binding / transition event

### Substrate state $B$

### Control-plane projection $K$

### Projection gap $\alpha: B \to K$

### Reconciliation action

### Convergence result

### Destroyed / degraded obligations
- Evidence:
- Causality:
- Custody:
- Authority:
- Continuity:
- Substrate accountability:

### Audit state
Orphaned.

### Why convergence-only correctness misses it

### Predicate forced

### Receipt requirement

---

## Case 3 — DegradedWithReceipt

### Scenario
A node is drained for a thermal event. The Node Problem Detector marks the substrate accusation as open. Pods relocate successfully under the controller's reconciliation policy. The downstream service continues to operate, with the open accusation surfacing through a durable receipt that outlives the immediate transition. The system is *admissible* — the obligations are accounted for under `degradedWithReceipt` — but the finding is not closed.

### Binding / transition event

### Substrate state $B$

### Control-plane projection $K$

### Projection gap $\alpha: B \to K$

### Reconciliation action

### Convergence result

### Preserved / transferred / open obligations
- Evidence:
- Causality:
- Custody:
- Authority:
- Continuity:
- Substrate accountability:

### Audit state
DegradedWithReceipt.

### Why this is admissible but not closed

### Predicate forced

### Receipt requirement

---

## Predicate ledger (populated as cases force)

When a predicate appears in two or more cases under "Predicate forced," promote it here with a one-line gloss before filing in Lean.

| Predicate | Cases that force it | Gloss |
|---|---|---|
| | | |

When a predicate has cleared the two-case gate, file it in `~/git/lean/LeanProofs/Admissibility.lean` and update the corresponding `True`-placeholder theorem(s):

- `masked_recovery_not_resolved` (currently `True`, pending substrate-accusation + K-transition outcome predicates)
- `orphaned_causality_inadmissible` (currently `True`, pending causal-binding + attributability predicates)

---

## Notes

- Cases 1 and 2 share the *destroyed-obligations* shape; Case 3 is the *admissible-degraded* shape that distinguishes the audit vocabulary from a flat fail/pass binary. The asymmetry is deliberate.
- Receipt requirement field captures the durability invariant the case demands: $H(\text{receipt}) \ge \max H(\omega)$ over affected obligations $\omega$. Cases that demand long-horizon receipts (e.g., spanning hardware-replacement cycles) drive the durability claim that lives in §7 of the paper.
- "Why convergence-only correctness misses it" is the load-bearing field for the convergence/testimony gap thesis. If a case cannot articulate a concrete operator-side loss that convergence-only correctness ignores, it is not worth its slot.
- These three are the seed set. Additional cases can be added if the predicate ledger does not stabilize after the first three; do not add cases just because they are colorful.
