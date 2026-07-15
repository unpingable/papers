# Frontier 3 — Rule-change-as-effect: typed deferral receipt

**Filed:** 2026-06-06 (Fri PM). **Status:** *deferral receipt*. The calculus governs its own constitutional layer using the discipline it ships. *The calculus is the first institution governed by it.*

## What is deferred

**Rule amendment as a governed effect.** The recognition that rule changes are not metadata but effects — possibly the highest-blast-radius effects in the entire system — and that they require:

- Their own authority predicate (`RuleChange requires authority`).
- A defined applicability horizon (which in-flight matters the change touches; which it does not).
- Treatment of in-flight matters (grandfathering by default, unless the amendment rule itself permits retroactive reach).
- Membership in the **effect lattice** with the strongest receipt class associated with their blast radius.
- Witnessed authority for the change itself (the `RuleAuthority` predicate must clear the same same-custody and receipt-type axes as any other discharge).
- Versioning, notice, and a typed transition rule for amendment of amendment-rules (the recursion).

This is the **constitutional layer**.

## Why deferred

Tonight's manifest (`refusals-need-receipts.md`) consolidated the **operational liveness layer** — refusal accountability, deemed refusal, cure-graph reachability, matter-clock monotonicity, exception budgets, appellate independence, ministerial/discretionary split. That layer is bounded and shippable.

The constitutional layer is bounded by:

1. The operational layer must stabilize first; the constitutional layer governs amendments to the operational layer, so the operational primitives must settle before their amendment rules can be typed.
2. Constitutional questions recursively raise *meta-constitutional* questions (who governs the amendment of the amendment rules) which require their own deferral discipline lest the calculus accidentally rebuild the entire administrative-law canon in one session.
3. The fourth Claude's review explicitly named this: *"touch it now and the sprint becomes a constitutional convention held inside a haunted vending machine."*

Per the calculus's own NoMovingGoalposts and ReachableCure discipline, *the deferral itself must be a typed receipt*, not fog. This file is that receipt.

## Dependency and priority conditions

Formal kernel work depends on condition 1: the operational primitives being amended
must be stable enough to model. Conditions 2 and 3 can raise priority or sharpen the
model, but are not permission to formalize:

1. **Operational liveness layer stabilizes.** `refusals-need-receipts.md` primitives have a Lean implementation, the four corrections have settled, and the sprint manifest's first four theorems build green. *(Concrete trigger: `Mandamus.lean` § Lean-spike #1 + § Lean-spike #2 both elaborate.)*
2. **Forcing case for amendment governance surfaces.** A real-world matter is identified where a rule change retroactively altered in-flight discharge conditions and the operational layer cannot refuse it without the constitutional layer's machinery.
3. **External pressure from the legal-academic neighborhood.** Administrative-law scholarship surfaces a sharper formulation of governed amendment that maps cleanly onto the calculus's existing primitives. (Suggested watch: rulemaking-procedure literature, fair-notice jurisprudence, and the deemed-approval / constructive-grant statutory tradition.)

Until the operational dependency stabilizes, the constitutional kernel remains
deferred on intrinsic model grounds. After that, a precise, non-vacuous amendment
model may be formalized before any real-world incident or academic prompt and may
lead the later implementation. The calculus does not pretend the layer doesn't
exist; it records what is deferred and why.

## What this deferral does NOT cover

- It does *not* defer the operational layer's typing of rule version into the matter (`rule_version_fixed for in-flight matters` per ReachableCure — that's already in the operational doctrine).
- It does *not* defer the recognition that rule changes are effects (the principle is recorded; what's deferred is the kernel that governs them).
- It does *not* defer treatment of in-flight matters under default grandfathering (operational machine assumes default grandfathering unless overridden; what's deferred is the override discipline).

## The metarule

This deferral receipt is itself an instance of the calculus's discipline:

```text
DeferralReceipt(
  what:        "Rule-change-as-effect / constitutional layer kernel",
  why:         "Operational liveness must stabilize first; meta-constitutional recursion risk",
  authored_by: "operator + multi-model exchange 2026-06-06",
  reopens_when: [ "operational layer ships green",
                  "forcing case surfaces",
                  "external pressure sharpens formulation" ],
  applicable_horizon: "indefinite until reopening condition triggers",
  contestability: "operator can override at any time; deferral is not refusal"
)
```

The calculus runs on records. This is the calculus's own record of what it has chosen not to build yet, and the conditions under which the choice reopens. *NoMovingGoalposts applies to the calculus itself.*

## Cross-references

- [`refusals-need-receipts.md`](refusals-need-receipts.md) § Rule amendment deferral pointer.
- [`mandamus-liveness-dual.md`](mandamus-liveness-dual.md) § The four corrections (Frontier 3 mention in correction context).
- [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) — obligation atoms; rule-change-as-effect would carry its own obligation set when reopened.

## Provenance

Surfaced as Frontier 3 in the 2026-06-06 multi-model exchange that produced the liveness-dual doctrine. Operator explicitly flagged constitutional-layer recursion risk; fourth-Claude named the haunted-vending-machine failure mode; deferral pattern follows the calculus's own NoMovingGoalposts and ReachableCure discipline. Filed 2026-06-06 as the calculus's first typed self-governance receipt.
