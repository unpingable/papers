# Borrowed spend: credit extends the spend horizon, never the standing horizon

*Status: UNRATIFIED-CANDIDATE, 2026-07-12. Specimen BUILT same day
(`~/git/lean/LeanProofs/Scratch/BorrowedSpend.lean`, green, all headline
theorems zero-axiom). Forcing consumer named at filing: NQ → Nightshift →
expensive-API preventive operations.*

## The split

Three quantities, never two:

    budget   — current spendable capacity
    credit   — authorized temporary negative capacity
    standing — what transitions may legally be attempted

    effective_capacity  = budget + available_credit      (lawful)
    effective_authority = standing + urgency             (REFUSED)

**Spend may cross below zero without authority crossing beyond its horizon.
You can borrow capacity. You cannot borrow standing.** The second equation is
how emergency powers become a lifestyle brand.

## The borrowed-spend contract (seven conditions, all encoded in the gate)

1. named threatened event (typed class, not "things may get bad");
2. bounded intervention (exposure ceiling, hard expiry, no automatic
   refinancing);
3. evidence floor (receipts distinguish intervention from speculation);
4. named repayment source (a loan without a repayment domain is budget
   laundering);
5. dominance under the active risk profile (abstract predicate,
   profile-indexed — expected-avoided-loss arithmetic stays at the consumer,
   or Lean proves finance cosplay);
6. non-borrowable authority (standing must pre-exist; urgency may unlock a
   credit facility, never expand action scope);
7. post-crossing custody (debt/evidence/action/outcome stay attached;
   **failure to prevent does not retroactively unauthorize** a crossing valid
   at decision time — otherwise outcome bias corrupts the ledger).

## What the specimen proves

- `borrow_extends_spend_horizon` — inhabited: admitted draw, cost 500 against
  budget 100 (lawfully 400 below zero, inside ceiling, repayment named); and
  `borrow_is_a_crossing` — generically, EVERY admitted borrow exceeds its
  budget (within-budget spend uses the ordinary spend instrument; the credit
  gate doesn't double as it — typed separation of instruments).
- `principal_positive` / `principal_within_ceiling` — the borrowed principal
  (cost − budget) is first-class: positive, inside the ceiling; the runtime
  receipt carries it rather than auditors reconstructing it.
- `borrow_never_extends_standing` — admission inverts to pre-existing
  standing; the gate cannot mint it.
- `urgency_is_not_standing` — the tempting `standing ∨ urgent` evaluator
  admits an action the gate refuses at EVERY budget/ceiling/window/profile.
- `refinancing_structurally_absent` — repay-a-debt purpose has no admission
  derivation (structural absence, not a checked flag).
- `debt_names_repayment_budget`, `exposure_bounded`, `window_required`.
- `outcome_bias_is_a_different_predicate` — decision-time validity: the
  admitted draw whose threatened event arrives anyway is refused by the
  outcome-scrubbing evaluator yet remains admitted.
- Headline package: `credit_extends_spend_not_standing`.

Typed refusal vocabulary (`BorrowRefusal`, 8 codes) declared for consumers;
per the control-flow-laundering meta-pattern, runtime checkers must collect
ALL violated conditions (List, not first-failure Except). The file ships the
judgment, not the checker.

## Bridge-lattice observation (candidate, not a promotion claim)

The borrow gate instantiates **all five obligation atoms** of
`working/bridge-obligation-lattice.md` simultaneously: non-amplification
(standing fixed under credit), temporal bounding (expiry), type fidelity
(typed purpose/threat), freshness (evidence floor), anti-precedent (no
refinancing). First candidate observed to pay the full atom set — the
opposite corner from "a fog machine is a bridge with the empty obligation
set." If the lattice doctrine ever needs a total specimen, this is it.
Precision (post blind-review): temporal-bounding is paid **at admission**
(decision-time window), not as a maturity lifecycle; and `repayment = some b`
names a destination without proving acceptance/futurity/distinctness — the
`RepaymentCommitment` receipt is the runtime bridge's obligation.

## Instrument register (FILE NOW; FORMALIZATION MAY LEAD)

Borrowing is the primitive stress test — it introduces **time without
introducing a casino**, and asks the sharpest question: *can the system
authorize expenditure it does not presently possess without pretending it
possesses authority it was never granted?* The stranger instruments are
named here so they stay named without becoming an automatic build queue:

- **reserve** — pre-funded budget, no debt;
- **insurance** — third party accepts bounded loss custody;
- **option** — spend now to preserve a later action right;
- **bond/escrow** — lock capacity against misconduct/nonperformance;
- **tranche** — release more spend as evidence accumulates;
- **hedge** — accept one bounded exposure to reduce another.

Each would be its own admissibility contract with its own laundering modes.
Any one may be formalized before runtime adoption when it yields a coherent,
non-redundant contract or countermodel with explicit scope, overlap, and
non-vacuity controls. The note itself does not establish those conditions.
Runtime instrument work remains parked until a concrete integration need;
formalization may lead that work rather than wait for an incident.

## Gates

- **Scope:** single draw, decision-time, possibilistic. No interest,
  amortization, probability, portfolios, or repayment enforcement (the
  receipt names the budget; collection is the consumer's ledger).
- **Promotion:** Scratch remains non-testimony until a separate proof-scope,
  custody, compatibility, and public-surface review. Nightshift's borrow gate
  or an NQ intervention-candidate emitter may provide priority and runtime
  correspondence evidence, but citation alone neither promotes the theorem nor
  proves conformance. The BorrowedIntervention runtime artifact is AG/NQ-lane
  work that should be written against this contract, not before it. The Lean object has exposed
  its required fields: standing basis, threat basis, profile judgment, cost,
  current capacity, **borrowed principal**, ceiling, maturity,
  **repayment commitment**, decision-time receipt.
