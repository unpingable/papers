# Promotion Claims Require Artifact-Level Custody Witnesses

**Filed:** 2026-06-05. **Status:** self-audit doctrine. Names a failure mode the corpus just demonstrated against itself. Dual to [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md) ([[project-wiring-vs-folder-placement]]); sibling to [`custody-classes.md`](custody-classes.md).

## The headline

> **A promotion claim recorded in memory, README, or doctrine — but not legible at the artifact layer — is itself an admissibility failure.**

The framework rejects silent promotions between institutional object-kinds. This rule applies the same gate to the corpus's own repo. A doctrine note saying "X is in the 1.0 surface" is a *claim*. A directory containing X, an import in the public aggregator, and a class label in X's docstring are the *witnesses* that make the claim mechanically checkable. Without those witnesses, the doctrine note is destination-only — a stamp of authority that does not bind the artifact, exactly the laundering pattern the framework refuses elsewhere.

## The triggering case

This rule was filed because the corpus caught itself.

On 2026-06-05, an audit surfaced three findings:

1. The `Custody-Class:` Option C policy was named in doctrine but covered ~12 of 47 `Admissibility/*.lean` files (and only as prose, not as a grep target).
2. The `LeanProofs/AdmissibilityKernels/` directory — named in memory as the canonical 1.0 surface after the 2026-06-03 calculus retirement — did not exist on disk. The eight files claimed for that surface were still mixed into `Admissibility/`.
3. The federation result that survived the calculus retirement ("no unifier without laundering," the witness-carrier invariant table, the bridge obligation lattice) was filed in working notes but had no Lean specimen.

(1) and (2) are the load-bearing self-audit cases. The doctrine layer made promotion claims; the artifact layer did not carry the receipts. The framework's own anti-laundering rule applies: a destination claim without a witness is not a witness.

(3) is a different shape — a candidate that is openly unbuilt under YAGNI/forcing-case discipline. That is not a self-audit failure; the doctrine note correctly says *named, not built*. It is included here only to keep the three findings legible together.

## The rule

A promotion claim has three layers and requires receipts at each:

| Layer | Claim form | Receipt |
|---|---|---|
| **Doctrine** | "X is in the canonical surface" | Working note or memory entry naming X |
| **Wiring** | "The build covers X as part of the public claim" | Import of X in the public aggregator |
| **Custody** | "Future edits to X are bound by the promotion" | `Custody-Class: PUBLIC-SHIPPED` in X's docstring, plus a custody prose paragraph stating the binding mechanism |

A claim at the doctrine layer that lacks the wiring and custody receipts is admissible only as a *candidate* — `UNRATIFIED-CANDIDATE` is the legible class for this state. A claim asserting full promotion without those receipts is the failure mode this note exists to name.

## What this is not

- Not a rule that doctrine cannot lead artifacts. Doctrine can and should name targets before they are built — the [[feedback-name-early]] discipline is unchanged. The rule is that a *promotion* claim (not a candidate claim) requires the receipts.
- Not a rule that requires receipts to land in a single commit. Phased work is fine; the rule is that the doctrine layer should not assert "X is promoted" while the wiring and custody layers are still empty. If a phase ships the doctrine first, the doctrine should describe the candidate state, not the promoted state, until the receipts arrive.
- Not a license to demand ratification for routine implementation. Per the register-discipline rule, this is custody-affecting work — directory placement, public aggregator imports, class labels — by construction. It does not extend to ordinary code edits or local docs.

## The composition

This rule and [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md) are duals:

- *Wiring is a promotion claim, folder placement is not.* — the **supply side**: what does or does not constitute a promotion.
- *Promotion claims require artifact-level custody witnesses.* — the **demand side**: a promotion claim asserted without the witnesses it requires is itself the failure mode.

A repo that follows wiring-is-not-folder-placement avoids accidentally promoting by moving files. A repo that follows this rule avoids accidentally promoting by writing doctrine. Both gates are needed; they catch different mistakes.

## The self-audit observation

The cleanest reading of the 2026-06-05 finding is that the framework's anti-laundering gate fired against the corpus itself: the audit produced a refusal kernel pointed at its own author. That is the falsifiability handle landing on the framework, not a procedural slip. It is also the only reading under which the finding is not embarrassing — the framework cannot claim to detect silent promotions in others' speech acts if it cannot detect them in its own filesystem.
