# Frontier proof obligations — ledger + cadence

> **Status:** internal proof-obligation ledger.
> Companion to [[kernel-to-body-map]] (dependency-ordered slice inventory) and [[calculus-2-exit-criteria]] (the six conditions for "body exists").

## Per-slice proof pattern

Every slice follows the same five-step shape. Slice work that skips a step does not count toward an exit criterion.

1. **Negative model** — exhibit what 1.0 does not imply.
2. **Minimal vocabulary** — add only the terms required to *state* the wound.
3. **Bridge theorem** — prove the positive property under **explicit extra hypotheses**.
4. **Consumer specimen** — `ExamplesTwo.lean` entry that exercises the theorem.
5. **Non-claim update** — `WHAT-THE-LEAN-STACK-PROVES.md` says what still is not proven.

The discipline keeps each addition paying rent. Less *and then we add modules*; more *each addition closes a specific wound and updates the public account of what is not proven*.

## Proof-obligations ledger

| Frontier | Wound                                          | Counterexample file                | Bridge hypothesis                  | Positive theorem (target)                    | Consumer    |
| -------- | ---------------------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------------------- | ----------- |
| Safety   | Authorized need not preserve value             | `AuthorizedNotSafe.lean`           | `SafetyEnv`                        | `authorized_safety_preserving_under_env`     | Example 8   |
| Locality | Merge may leak exposure                        | `BadMerge.lean`                    | `MergeAdmissible`                  | `merge_admissible_necessary` (+ corollaries) | Example 9   |
| Self-mod | Actor amends own binding rule                  | `SelfAmendmentTrap.lean`           | `Binds actor policy`               | `no_self_amendment_authorized_step`          | Example 10  |
| Belief   | Authorized update leaves dependents incoherent | `BeliefRevisionContradiction.lean` | `Dependency + Revise` obligation   | `coherent_revision_under_dependency`         | Example 11  |
| Axes     | Composed axes license stronger claim           | `AxisCompositionFailure.lean`      | cross-axis env                     | (named only when a consumer demands)         | Example 12  |

This table is how the body avoids becoming a mist machine. Each row is harder to fake than a paragraph. A frontier with no row is not closed.

## How rows are added

- A row appears when its counterexample file lands. Not before.
- "Positive theorem (target)" is a target name, not a promise. Renaming on landing is fine; deleting the row when the slice is closed is not — the cell freezes as the historical receipt.
- "Bridge hypothesis" is the name of the extra structure the theorem requires. If a slice closes without one, the row says so explicitly; that is part of the negative testimony.
- The Locality row's positive-theorem cell ("`merge_admissible_necessary` (+ corollaries)") covers necessity *for the named exposure-safety property under the current `LocalBoundary` model* — not global necessity. See Slice B in [[kernel-to-body-map]].

## What this ledger is not

- Not a TODO list. A row is filed only when its counterexample exists.
- Not a slice plan. Slice ordering lives in [[kernel-to-body-map]].
- Not an exit-criterion substitute. Ledger rows are necessary, not sufficient — see [[calculus-2-exit-criteria]].
