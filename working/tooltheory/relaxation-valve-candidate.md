# Relaxation valve — de-escalation receipts (candidate)

**Status:** candidate / non-binding handle. **Custody fence: this is governor/AG runtime
doctrine** — operator ratifies, AG-Claude builds; NOT paper/Lean's to mint. All instances
are of existing primitives; do not mint a new family.
*Migrated from Claude memory on 2026-06-22 (`project-relaxation-valve-candidate`).*

2026-06-15 (Chatty-seeded, refined cross-session). **Caution inflation** — custody climbs
even when evidence doesn't (Session A flags → B inherits + can't clear by absence + adds
→ C infers danger from A+B) — is the operational form of *stale entries vote*, and the
de-escalation **dual of No Negative Clearance**. The one-liner: **absence is never a
receipt, in either direction** (the down-direction face of null-laundering / *no silent
conversion of moss into evidence*, see `project-signal-authority`). Slogan: **No Negative
Clearance needs positive clearance.**

**Three receipt families** (caution is a state lifted/lowered only by paid receipts):
- **CautionReceipt** — raises/maintains concern from an *admissible* basis.
- **ClearanceReceipt** — discharges the concern (gone / inapplicable / narrowed /
  superseded / misclassified / expired-by-contract); inherits as **settled** in scope.
- **WaiverReceipt** — concern stays **LIVE**; operator accepts bounded use (authority /
  scope / expiry); inherits **only** as "accepted risk under these bounds," **never** as
  safe. *AcceptedRisk is authorized burden-carrying, NOT clearance.* Collapsing a waiver
  to "cleared" rebuilds the laundering one port over (Session D reads a live risk as
  safe). Inheritance state: `Cleared / Waived / Live`.

**The key fact — this is NOT a new kernel.** Each invariant is an instance of a primitive
already in the corpus; don't mint a ForkMode-style new family (classify against the
anti-laundering family table first):
- **Two-port split (Waiver ≠ Clearance)** = *operator basis licenses the authority gap
  only, not evidentiary/custodial* (the chmod-777 rule, BestEffortCompleteness *type the
  justification, don't rank it*). Waiver = operator-basis; Clearance =
  evidentiary/custodial basis.
- **"Caution lineage is not caution basis"** = `no_free_lift` for the caution direction:
  every caution must trace to a **non-caution** kernel basis. Caution citing caution = a
  lift that never bottoms out (what `naked_lift_unsound` refuses). Typed `basis_kind`:
  DirectEvidence / DerivedFromEvidence / FailedClearance / FailedWaiver / OperatorPolicy /
  PriorCautionContextOnly (last = NOT sufficient). Invariant: *no self-sustaining caution
  chains* — if all non-caution bases clear, derived caution must clear/narrow/rebase on
  new direct evidence. See `project-admissibility-lift-cluster` for the no-free-lift home.
- **Residual-risk budget (waiver port)** = the divergence/budget primitive
  (`budget_conserved`; readout-arc diachronic scalars). Waivers are cheaper to pull than
  clearances → path of least resistance becomes waiving not resolving → live waivers pile
  up, `residual_risk` tracked per-waiver but never summed. Fix: make residual risk a
  **conserved, aggregated budget across live waivers in scope**, so the Nth waiver costs
  more standing and crossing the budget **fails the next one closed.** Symmetric bound:
  caution can't reproduce upward, waivers can't accumulate downward.
- **Expiry caveat:** expiry discharges *only* if it was in the original caution's
  contract — else you rebuild negative clearance with a clock (freshness/standing split
  is prior art, attack-04).

**Why:** the apparatus had only ratchet teeth (observe→claim→sign→promote, custody up
only). The valve is the missing reverse bridge — a *paid* downward lift. First physical
instance already exists: `experiments/no_free_lift_wiring/RATIFICATION-PENDING.md`
discharges accumulated caution by typed positive acts (Name/Custody signatures), and its
`( ) Custody` box is exactly an operator WaiverReceipt.

**How to apply:** candidate / non-binding handle. This is **governor/AG runtime doctrine**
→ operator ratifies, AG-Claude builds; not paper/Lean's to mint. Forcing case to BUILD the
receipt types = an actual caution that needs discharging and can't be. Until then it's
three receipt families + three invariants, each already homed in an existing primitive.
Composes with name-early discipline.
