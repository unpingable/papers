# Paper 27 — Working Notes

## Status

**v0.0-scaffold — 2026-04-28.** Directory + outline + abstract stub + Lean skeleton. **No full prose draft yet.** No K8s implementation. Companion Lean skeleton at `~/git/lean/LeanProofs/Admissibility.lean`.

**Update 2026-05-01.** Lean skeleton sorry-eliminated. Three theorems carry real proofs against the local `admissible` definition (`unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`); two remain `True`-placeholder discharges with deferred-real-statement docstrings (`masked_recovery_not_resolved`, `orphaned_causality_inadmissible`) — those need substrate-accusation and causal-binding predicates that P27 has not declared. House rule: kill the sorrys, do not let the sorrys design the constitution. File remains unwired by deliberate slot decision.

**Update 2026-05-01.** Working note `working/admissible-recovery-semantics.md` exists. Corrective monotonicity / non-laundering recovery semantics with companion Lean module at `~/git/lean/LeanProofs/Admissibility/Corrective.lean`. Candidate fold-in target for P27 pending the seven-path audit (working note §8). Slot decision deferred until audit produces concrete laundering paths or rules them out cleanly.

## Scope discipline (queue-jumping guardrail)

Queue-jumped per dependency-discovery argument: P27 supplies the constructive endpoint the P22–P26 negative spine demands. *Jumping the queue does not mean opening every drawer.*

**Done in scaffold pass:**

- Directory placeholder
- Abstract stub (in `metadata.yaml`)
- Section outline + contribution bullets (in `CANDIDATES.md`)
- Lean skeleton with corrected algebra (Accounting wraps Outcome; `unaccounted` is the inadmissible case; `openFinding` is admissible when durably recorded)
- Candidate theorem statements
- P25 and P26 import notes

**Not yet:**

- Full proof development
- Full related-work dive
- Full prose draft
- Kubernetes implementation rabbit hole

## Lean algebra correction (chattY pass, 2026-04-28)

Initial sketch had `openFinding ⇒ inadmissible`. That was wrong — it formalized the wrong doctrine. Corrected:

- `Outcome := preserved | transferred | discharged | degradedWithReceipt | openFinding`
- `Accounting := unaccounted | accounted Outcome`
- Admissibility: every affected obligation must be `accounted _`, not `unaccounted`.
- `openFinding` is admissible if the receipt horizon satisfies the relevant obligation horizon.
- Theorem name: `unaccounted_implies_inadmissible`, not `openFinding_implies_inadmissible`.

The model preserves the Governor primitive: *permit action, deny closure, leave finding open.* Open findings are honesty with a pager — refusal to launder uncertainty into closure — not failures of admissibility.

## Lit-differential sketch

Six neighborhoods. Gap at boundary.

| Neighborhood | Closest claim | What's missing |
|---|---|---|
| Anvil-style controller verification (Sun et al.) | `eventually current = desired` | dual safety property over transitions |
| Refinement / abstraction soundness (Lamport, Abadi; CEGAR) | refinement preserves spec | obligation-soundness as application-layer constraint |
| Failure masking (Schlichting & Schneider) | masking redundancy hides faults from clients | masked-by-recovery as transition audit state |
| Causal tracing / provenance (Dapper, Magpie, PROV-DM, Trio) | reconstruct evidence chains | retention horizons tied to obligation classes |
| Forensic readiness (Rowlingson, Tan) | preserve evidence pre-incident | integrate with control-loop transition admissibility |
| K8s NPD + chaos engineering (Litmus, Chaos Mesh) | surface substrate problems / inject faults | no admissibility framework over reconciliation transitions |

Gap claim: *these neighborhoods describe components of the same failure mode under different vocabularies. We identify the unifying structure — obligation-unsound quotienting — and define transition admissibility as the safety property complementary to convergence.*

## Cross-reference language

For §1 of the paper, when ready:

> P25 establishes that substitution is structurally forced under observability asymmetry. P27 addresses a distinct but related question: given that the controller cannot see what would constitute correct convergence, we can at least require that the transitions it executes do not destroy the conditions under which a different observer could later testify.

For §5/§7, when discussing horizons:

> Retention horizons follow the two-curve framing introduced in (Beck, Paper 26): admissibility maturity m(t) and consequence viability c(t) define an admissibility window over time. P27 specializes the c(t) curve per obligation class — evidence, causality, substrate-accusation — and requires the receipt horizon to outlive the longest-lived affected obligation.

## Drafting plan (when scope opens)

1. Cold reread of this scaffold + multi-model conversation that produced it.
2. §3 model formalization — substrate / control plane / projection / bridge.
3. §4 obligation-unsound quotients — formal definition + K8s instances.
4. §5 transition admissibility — obligations × outcomes × horizons.
5. §6 audit states — full vocabulary + state-transition rules.
6. §7 receipt durability — scope-limited; defer full self-governance.
7. §8 auditor sketch.
8. §9 worked examples — three concrete K8s scenarios.
9. Lean proofs — fill in `unaccounted_implies_inadmissible` and durability lemmas. Optional: prototype `admissible` decidability.
10. §11 generalization — beyond K8s.
11. Compression pass.
12. Lit-differential pass (close the six neighborhoods).

## Loose fragments

- "The controller converged. The testimony decayed." (Aphorism candidate.)
- "Kubernetes optimizes for convergence, not testimony." Sharper version: K8s' correctness specification is *silent* about testimony. Convergence and testimony are orthogonal objectives; the spec mentions only one. Frames the contribution as *extending the correctness vocabulary*, not rebalancing priorities.
- "The system turned red into green by eating the witness." (Aphorism, kept in reserve.)
- "It performed disappearance." (Closing-line candidate for §13.)
- Worked-example seeds: (i) pod failing on suspect-disk node, drain + reschedule destroys logs, replacement pod scheduled onto same node — Masked. (ii) volume corruption detected, replica restored from backup, root cause never bound to specific substrate event because scheduling history aged out — Orphaned causality. (iii) node drained for thermal event, accusation marked open in NPD, pods relocated successfully, downstream service operates DegradedWithReceipt for duration of substrate accusation.
