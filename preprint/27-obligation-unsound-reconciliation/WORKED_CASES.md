# Paper 27 — Worked Cases

**Purpose.** Force the transition-admissibility vocabulary from concrete reconciliation cases before promoting any missing Lean predicates. The cases drive the predicates; Lean follows the cases. Filing predicates in `~/git/lean/LeanProofs/Admissibility.lean` ahead of forcing cases would be constitution-by-typechecker — exactly the failure mode `memory/feedback-lean-debt-discipline.md` warns against.

**Discipline rule.** No new Lean predicate (e.g. `substrateAccusation`, `causalBinding`, `maskedByRecovery`, `orphanedCausality`, `receiptOutlives`) gets promoted to the formal layer until *at least two cases independently force it.* One case can be colorful; two cases start to define structure; three cases give the admissibility vocabulary without hallucinating a tiny courthouse inside Lean.

**Status.** Scaffold (2026-05-01). Scenario seeds transcribed from NOTES.md; all other fields are placeholders for population by the author. The three cases are the Masked / Orphaned / DegradedWithReceipt split named in P27's audit-state vocabulary.

---

## Case 1 — Masked Recovery

### Scenario
Pod fails on a suspect-disk node. Reconciliation drains and reschedules; the drain destroys useful logs (kernel messages, dmesg, container stdout); the replacement pod is scheduled onto a node in the same node class — same substrate risk, no record that the controller noticed.

### Binding / transition event
The reconciliation transition that drains the failing pod from its current node and schedules a replacement pod, ending when the new pod reports Ready.

### Substrate state $B$
Node has hardware-level disk degradation accumulating: rising I/O error rate, occasional latency spikes, kernel disk-error log entries that have not yet been promoted to a node-level condition. The substrate has standing — there is a real, named problem with this node — but it is not yet a first-class control-plane object.

### Control-plane projection $K$
Pod status, schedulable-nodes set, replica counts, readiness probes, scheduler-visible node labels, node conditions surfaced by kubelet or NPD.

### Projection gap $\alpha: B \to K$
The accumulating substrate-disk evidence does not project into $K$. The kubelet's view of "container exited" reaches $K$; the kernel's view of "disk is degrading" does not, because no condition has been promoted. From $K$'s perspective, the pod simply failed.

### Reconciliation action
Drain the pod (which destroys the container's stdout/stderr and any kernel messages tied to that pod's lifecycle); reschedule onto another node selected by the existing scheduling policy, which in the absence of a node-condition signal may select another node in the same node class with the same substrate risk profile.

### Convergence result
Pod healthy, replicas at desired count, service Ready — by the convergence specification, the loop has succeeded.

### Destroyed / degraded obligations
- Evidence: kernel disk-error logs, dmesg, container stdout/stderr destroyed at drain; no durable artifact ties the pod failure to the substrate-disk evidence.
- Causality: the link between the observed pod failure and the substrate-disk state is never bound; the causal chain ends at "container exited."
- Custody: no controller takes custody of the substrate-disk evidence across the transition; the evidence exists at $t-\epsilon$ and is gone at $t+\epsilon$.
- Authority: K8s reconciliation had authority to drain and reschedule, but no authority requirement to preserve the substrate evidence accompanying the action.
- Continuity: the replacement pod re-enters a substrate equivalent (same node class) to the failed one; the failure mode is preserved across the transition.
- Substrate accountability: the failing-disk node remains in the schedulable pool with no recorded accusation; the next pod scheduled there inherits the same risk silently.

### Audit state
Masked.

### Why convergence-only correctness misses it
The $K$-level convergence test (replicas = desired ∧ all pods Ready) is satisfied at $t+\epsilon$. Nothing in the convergence specification asks whether the underlying substrate problem was diagnosed, recorded, or could resurface. The reconciliation appears successful on its own terms; the cost is paid in $B$, which $K$ does not project.

### Predicate forced
`substrateAccusation` (the substrate carries a standing finding that should outlive the transition); `maskedByRecovery` ($K$ reports recovery while the substrate accusation remains open and undeclared).

### Receipt requirement
A receipt for this transition must reference the suspect-node identity, the destroyed-evidence class, and the substrate accusation as an open finding. It must persist outside the pod lifecycle (which has been recycled) and outside the node lifecycle (the failing node may be cordoned, drained, replaced, or relabeled before the finding is investigated). Receipt durability ≥ substrate-accusation investigation horizon.

---

## Case 2 — Orphaned Causality

### Scenario
Volume corruption is detected. A replica is restored from backup. By the time the corruption is investigated, the substrate event that caused it (scheduling history, hardware fault, neighbor-pod interference) has aged out of the retention window. The data is back; the causal chain to a specific substrate event is not.

### Binding / transition event
The replica restore from backup following corruption detection, ending when the volume integrity check passes on the restored replica.

### Substrate state $B$
Volume corruption traceable, in principle, to a specific substrate event at time $t_\text{event}$: a hardware fault, neighbor-pod resource interference, a scheduling-induced disk contention episode, or a related substrate-layer disturbance. The substrate-layer evidence (scheduling history, hardware logs, neighbor-pod activity, node-level metrics around $t_\text{event}$) exists at the time of corruption detection but is subject to retention horizons typically shorter than the corruption-detection-to-investigation horizon.

### Control-plane projection $K$
Replica state, backup state, volume integrity-check result, the controller's view of "corrupted → restoring → restored."

### Projection gap $\alpha: B \to K$
$K$ sees the artifact-level transition: corruption observed → restore initiated → integrity check passes. It does not project the substrate-event causal chain into the artifact's record. The substrate event was not bound to the artifact at the time it occurred.

### Reconciliation action
Restore the affected replica from backup, potentially onto a different node selected by the scheduling policy. Integrity checks confirm the restored data; the controller advances to the next obligation.

### Convergence result
Replica healthy, integrity check passes, data accessible to consumers — converged.

### Destroyed / degraded obligations
- Evidence: substrate-event evidence (scheduling history, hardware logs, neighbor activity, node metrics) has aged out of retention by the time causal investigation begins; the evidence existed but was not preserved against this retention horizon.
- Causality: causal binding between corruption and substrate event is no longer attributable — not because the link was wrong, but because the link was never durably bound at the moment when evidence on both sides was live.
- Custody: the original corrupted volume may have been deleted as part of restore; the artifact-side evidence is gone, and the substrate-side evidence is aged out; no controller holds custody across the gap.
- Authority: the restore was authorized; no authority requirement attached preservation-of-causal-chain to the restore obligation.
- Continuity: the same substrate conditions could produce the same corruption on a different volume, but the pattern is not recognized because no specific substrate event was bound.
- Substrate accountability: no specific substrate event is accountable; the root cause is structurally unattributable.

### Audit state
Orphaned.

### Why convergence-only correctness misses it
Data is back; integrity checks pass; convergence is satisfied. There is no specification requirement that the causal chain be preserved. The transition that restored availability also dissolved the conditions under which substrate accountability could be established.

### Predicate forced
`causalBinding` (binding between artifact state and substrate accusation must be established while both are live); `receiptOutlives` (receipt durability must exceed the substrate-event retention horizon, not merely the artifact-recovery horizon).

### Receipt requirement
A receipt for the corruption-detection event (not the restore event) must be bound at the time of detection to the substrate evidence then available. Its durability must exceed the substrate-event retention horizon. The restore receipt alone is insufficient; what is needed is a binding receipt that captures the causal-chain endpoints while both still exist.

---

## Case 3 — DegradedWithReceipt

### Scenario
A node is drained for a thermal event. The Node Problem Detector marks the substrate accusation as open. Pods relocate successfully under the controller's reconciliation policy. The downstream service continues to operate, with the open accusation surfacing through a durable receipt that outlives the immediate transition. The system is *admissible* — the obligations are accounted for under `degradedWithReceipt` — but the finding is not closed.

### Binding / transition event
The NPD-driven cordon + drain of a node carrying an open thermal-event accusation, combined with the pod-relocation transitions that follow, ending when the downstream service operates without the drained node's pods.

### Substrate state $B$
Node experiencing a thermal event: a specific, named substrate condition with durable evidence (thermal sensor data, NPD-recorded condition, possibly hardware-vendor diagnostics). Cause may be cooling failure, sustained thermal load, environmental anomaly, or related; the accusation is open and accountable to a specific node and time window.

### Control-plane projection $K$
Node condition (set by NPD), node schedulability state (cordoned), pod-relocation status, replica counts, downstream service health.

### Projection gap $\alpha: B \to K$
The thermal condition projects into $K$ via NPD's node-condition record. The exact physical scope of the thermal event (single node? rack? cooling domain? regional?) may not fully project, but the per-node accusation does; the open finding has a custodian and a record. This is a smaller projection gap than Cases 1 and 2 — by design.

### Reconciliation action
NPD writes the node condition; the controller cordons the node, drains pods to other nodes selected under the scheduling policy, and marks the substrate accusation as an open finding bound to the node identifier.

### Convergence result
Pods relocated, replicas at desired count, downstream service available — converged.

### Preserved / transferred / open obligations
- Evidence: thermal sensor data preserved by NPD; durable; references node identifier and time window of the accusation.
- Causality: substrate accusation bound to a specific node at a specific time window; causal chain preserved as long as the receipt outlives the investigation horizon.
- Custody: NPD acts as custodian for the open finding for the substrate event; receipt is shape-preserving and durable.
- Authority: drain and reschedule actions were authorized; the *receipt* of the open finding is authorized to persist regardless of remediation outcome, and persists outside the pod and node lifecycles affected by the drain.
- Continuity: downstream service operates in `degradedWithReceipt` mode — admissible because the open finding is not laundered into closure; not closed because the substrate accusation remains active.
- Substrate accountability: the substrate accusation is named, durably recorded, and bound to a specific accountable substrate locus; remediation responsibility is attributable to the substrate custodian.

### Audit state
DegradedWithReceipt.

### Why this is admissible but not closed
The reconciliation produced service availability *and* preserved the obligation to track the substrate accusation. The system reports its state honestly: service available, finding still open. Convergence is satisfied; transition admissibility is also satisfied, because no affected obligation is `unaccounted` and the receipt horizon outlives the affected obligations. Admissibility is achieved through receipt durability rather than through quotienting the finding away. The Governor primitive applies: permit action, deny closure, leave finding open.

### Predicate forced
`receiptOutlives` (receipt horizon ≥ obligation horizon); `substrateAccusation` (named and durably recorded); `openFinding` (admissible Outcome class already defined in the Lean kernel).

### Receipt requirement
Receipt persists across the drain/reschedule transition and outlives the longest-affected obligation. Bound to the substrate-locus identifier (the node, or larger cooling-domain identifier if the accusation has scope beyond the node). Durable through subsequent node lifecycle events (replacement, relabeling, removal) until the substrate accusation is independently resolved or invalidated by the custodian.

---

## Predicate ledger (populated as cases force)

When a predicate appears in two or more cases under "Predicate forced," promote it here with a one-line gloss before filing in Lean.

| Predicate | Cases that force it | Gloss |
|---|---|---|
| `substrateAccusation` | 1, 3 | A standing finding bound to a substrate locus, accountable independent of $K$-side artifact lifecycles |
| `receiptOutlives` | 2, 3 | Receipt durability horizon meets or exceeds the longest-lived affected obligation; failure to outlive collapses causal binding |
| `maskedByRecovery` | 1 | $K$ reports recovery while substrate accusation remains open and undeclared — candidate, not yet promoted |
| `causalBinding` | 2 | Binding between artifact state and substrate accusation must be established while both are live — candidate, not yet promoted |
| `openFinding` | 3 | Already defined in `~/git/lean/LeanProofs/Admissibility.lean` as an admissible `Outcome` class |

When a predicate has cleared the two-case gate, file it in `~/git/lean/LeanProofs/Admissibility.lean` and update the corresponding `True`-placeholder theorem(s):

- `masked_recovery_not_resolved` (currently `True`, pending substrate-accusation + K-transition outcome predicates)
- `orphaned_causality_inadmissible` (currently `True`, pending causal-binding + attributability predicates)

**Disposition for P27 v0.1.** `substrateAccusation` (Cases 1, 3) and `receiptOutlives` (Cases 2, 3) have cleared the two-case gate. Per the closure-audit scope discipline — *treat `True`-placeholder Lean theorems as limitations, not implementation pressure* — these predicates are **not** promoted into the Lean kernel in this draft. The paper's §6 records both as deferred-but-cleared limitations; the kernel stays as-is. Future work may promote them if a downstream theorem forces composition with the existing `AuthorizedStep` / `Corrective` layer.

---

## Notes

- Cases 1 and 2 share the *destroyed-obligations* shape; Case 3 is the *admissible-degraded* shape that distinguishes the audit vocabulary from a flat fail/pass binary. The asymmetry is deliberate.
- Receipt requirement field captures the durability invariant the case demands: $H(\text{receipt}) \ge \max H(\omega)$ over affected obligations $\omega$. Cases that demand long-horizon receipts (e.g., spanning hardware-replacement cycles) drive the durability claim that lives in §7 of the paper.
- "Why convergence-only correctness misses it" is the load-bearing field for the convergence/testimony gap thesis. If a case cannot articulate a concrete operator-side loss that convergence-only correctness ignores, it is not worth its slot.
- These three are the seed set. Additional cases can be added if the predicate ledger does not stabilize after the first three; do not add cases just because they are colorful.
