# Refusals need receipts too — the liveness dual / mandamus

**Filed:** 2026-06-06 (Fri PM). **Status:** doctrine note + sprint manifest. **NOT** a candidate Lean kernel. **Curdling discipline:** same as [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) and [`heterogeneous-turtles-not-witnesses.md`](heterogeneous-turtles-not-witnesses.md) — *do not formalize before 2026-06-07, and the four corrections below must settle before any `Mandamus.lean` spike. Cursed little theorem gremlins are a separate file from this one.*

**Custody:** doctrine note + manifest; pre-ratified per name-early. Companion file: [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md) — the calculus's first typed-deferral receipt, governing its own constitutional layer per the discipline it's about to ship. Memory pointer: `project-refusals-need-receipts`.

## The pivot

The admissibility stack to date is a **soundness theory**: refuse to discharge a predicate on insufficient evidence. The degenerate solution to that spec is the boundary that discharges nothing — sound against wrongful acceptance, perfect denial infrastructure, *Kafka with type signatures*.

The missing half is the **liveness dual**: refuse to stall, fog, or withhold when the evidence is sufficient. The kernels-to-date defend against wrongful acceptance; this layer defends against **wrongful refusal**.

Together:

| Error | Refusal kernel domain |
|---|---|
| **Wrongful acceptance** — insufficient artifact caused an effect | Soundness side (existing) |
| **Wrongful refusal** — sufficient artifact failed to discharge, advance, decide, or receive timely explanation | Liveness side (this layer) |

The core rule:

> **Refusal is an accountable act.**

A boundary that can refuse but cannot be checked for wrongful refusal is not running admissibility. It is running *discretion in a lab coat*.

## Effect-indexed permission (Entitles)

Acceptance is not binary. A receipt may discharge a predicate without entitling every consequence that predicate could license. The acceptance ladder:

```text
log only
flag for review
quarantine
delay
notify
require second witness
reversible mutation
irreversible mutation
punitive action
strategic escalation
```

⚠ **Not a total order.** Reversibility, blast radius, scope, and *who bears the harm* are partial-order axes. Reversible-but-global-prod is not "below" irreversible-but-one-log-line. `Entitles` ranges over a **lattice**, not a chain. The classification function — *who decides which effects sit in which class* — is itself a capture surface (route 2 next moves here: not redefining the predicate, but reclassifying the effect; calling losing-your-house *appealable* therefore *recoverable*). The lattice ordering needs its own witness discipline.

Core primitive:

```text
Entitles(predicate, effect_class, surface, scope, horizon)
```

NOT generic `MayAct`. The 1979 NORAD case had this shape already: the artifact was good enough to discharge precautionary predicates (scrambles, NEACP launch), but not the nuclear-release predicate. *Admissibility is effect-indexed.*

## Effect-indexed obligation (Owes) — the dual

Permission alone makes the liveness gap worse. Every rung is a new place to park a claimant. *"Your receipt was sufficient to flag-for-review"* is the most beautiful denial machinery ever specified — formally sound, effect-indexed, and the review never comes.

The fix: index obligation too.

```text
Owes(predicate, effect_class, deadline)
```

If the receipt is sufficient for effect class E, then withholding E past the horizon **becomes the violation**. Intermediate states accrue duties on a clock — *Freshness.lean pointed at the institution instead of the artifact.* Quarantine emits obligation receipts on a timer.

Duality:

| Permission | Obligation |
|---|---|
| `Entitles(predicate, effect_class)` | `Owes(predicate, effect_class, deadline)` |
| What an accepted artifact *may* cause | What a sufficient artifact *compels* |

The calculus had a rich theory of the first column and nothing of the second. This is the bigger half.

## The RefusalReceipt

Every refusal must mint a structured artifact:

```text
RefusalReceipt(
  actor,
  surface,
  time,
  submitted_artifact,
  predicate_sought,
  failed_condition,
  rule_version,
  required_receipt_type,
  cure_path,
  appeal_path,
  decision_horizon
)
```

The fog tokens this refuses: *"denied"*, *"insufficient documentation"*, *"unable to verify"*, *"still processing"*. Those are not refusals. They are weather.

## ReachableCure — with the progress-measure correction (correction #1)

A refusal-receipt naming a cure-path is honest *only if* the cure path is reachable. *Castle bureaucracy with receipts* names every office; the graph never terminates.

**Initial draft was wrong:** acyclic. Legitimate cure paths cycle (revise-and-resubmit passes through the same node twice; that's healthy). The correct constraint is **progress over a well-founded measure**: the set of unmet conditions monotonically shrinks, a cured condition stays cured absent a versioned rule change.

```text
ReachableCure(
  progressing,            -- well-founded measure strictly decreasing
  satisfiable,            -- some compliant artifact discharges the residue
  cost_bounded,           -- proportionate to the entitlement
  time_bounded,           -- horizon must exist
  rule_version_fixed,     -- for in-flight matters
  known_before_submission,
  reachable_by_claimant_class -- see correction #2
)
```

The blame inversion:

> **An unreachable discharge condition is not claimant insufficiency. It is a refusal authored by the rulemaker.**

In Lean terms (deferred per curdling timer): this is a termination measure on the rule graph, not a DAG constraint. Termination measures are what the proof assistant was born to eat — the *most novel formal object in the set* and the meatier second target after `Owes`.

## Claimant-capability indexing (correction #2)

A cure path can be formally reachable and *practically enclosed* — reachable only by claimants with counsel, six weeks of daytime availability, and a notary. That's the literacy-test structure: published, knowable, finite, and discriminating.

```text
ReachableCure must be indexed to a declared claimant-capability class.
```

The corpus's [[project-negative-inclusivity]] work names the *durability* of this distortion as the failure mode; this is where that work lands inside the calculus. A reachability claim that doesn't declare the claimant class it's reachable for is making a literacy-test argument under a different name.

Composes directly with the WitnessInvariance regime axis: capability-class is a regime, and discharge conditions must hold under the regime they're advertised for.

## Blocking-predicate discipline (correction #3)

The minimal viable kernel says discharge owes when no *"valid blocking predicate"* exists. **That clause is where displaced discretion will rehome.** Pending-security-review, quality-hold, integrity-check — institutions discover an inexhaustible supply of blockers the moment `Owes` binds.

Blocking predicates must inherit the full discipline:

- **typed** (which predicate is blocking, named)
- **versioned** (which rule version introduced this blocker)
- **knowable before submission** (per NoMovingGoalposts; otherwise the blocker is a new requirement)
- **witnessed** (the block itself needs a witness of independent type — *blocker assertions can't witness themselves either*; the same-custody and receipt-type axes apply)
- **clock-charged to the institution** (the matter clock keeps running while the blocker is active; an idle blocker spends institutional budget)

Otherwise a blocker is just the supplemental-request scam wearing a different badge.

## Matter-clock monotonicity

Per-round deadlines are a scam surface. Every *"please provide one more thing"* resets the clock and converts denial-as-weather into denial-as-seasonal-cycle (*bureaucratic TCP keepalive for denial*).

```text
The matter clock is monotonic per matter, not per round.
Supplemental requests spend institutional budget, not claimant time.
Non-decision past matter horizon is deemed refusal.
```

Some jurisdictions already run this in administrative law as **deemed-approval statutes**: construction permits granted by operation of law if the agency sits past the deadline. *RefusalTimeout with the polarity flipped to maximum institutional discomfort.* The calculus is typing what the writ has always demanded.

## ExceptionBudget

Provisional action is sometimes owed (hospital, incident response, lethal-refusal domains — *false negative is not always cheaper than false positive*). But emergency channels become the load-bearing path if they're cheaper than the normal one and audited by their owner.

```text
ProvisionalAct(reason, missing_witness, harm_of_waiting,
               scope_limit, rollback_plan, posthoc_review_deadline)
```

Rules:

- ProvisionalAct **burns exception budget** per surface per horizon.
- Posthoc review **must sit on a different custody chain** than the actor invoking the exception.
- Budget exhaustion **closes the emergency path** and forces traffic back to the normal one.
- Repeated emergency use is **evidence that the normal path is broken or being bypassed** — not a license, a signal.

*SRE doctrine annexing Carl Schmitt.* Keep that in a jar. Error budgets for states of exception.

## Appellate independence (NORAD-shape recursion)

Appeals that terminate inside the refusing institution rebuild the [barbershop quartet](heterogeneous-turtles-not-witnesses.md) at the adjudication layer. The same-custody refusal recurses upward:

```text
AppealReview does not discharge IndependentReview
if reviewer shares custody chain with refusing boundary.
```

Heterogeneity is not just for evidence; it's for review. *The appellate boundary must sit outside the refusing boundary's failure cone*, same principle as 1979's independent sensor families applied to judgment instead of observation.

## Ministerial vs discretionary — must survive in types (correction #5)

The MVK below flattens `MustDischarge` into "owes discharge/advance/decision." The ministerial/discretionary split has to survive into the types:

- **Ministerial surfaces** owe *discharge* when the receipt is sufficient. (Construction permit, license renewal where statutory criteria are met, etc.)
- **Discretionary surfaces** never owe discharge. They owe **decision plus reasoned, receipted refusal within horizon**.

```text
type Surface = Ministerial | Discretionary
Owes(Ministerial, predicate, effect_class, deadline) → discharge
Owes(Discretionary, predicate, _, deadline) → decision + RefusalReceipt
```

Collapse those and the first administrative lawyer to read it finds the error in four minutes.

## The enforcement boundary (correction #4) — courts as record-consumer

*Emits violation* needs a consumer. A violation receipt with no enforcement surface is a strongly worded letter with a type signature. **The kernel cannot compel.** That's outside the system; pretending otherwise would be the framework committing its own sin.

But this is a feature, not a bug. Mandamus has always foundered on the claimant's inability to **prove** the elements — sufficiency, ministerial duty, elapsed time, exhausted process. The kernel's actual product is **the record**, manufactured continuously, in admissible form.

> **The loop closes through the courts — the oldest effect boundary, the one that already has a bailiff.**

Positioning sharpens:

- *Not:* "adopt our governance framework."
- *Instead:* "everything your system does is now somebody's exhibit."

The kernel doesn't compel; it produces discharge-grade evidence that compels through the boundary that already retains compulsion power. This is the calculus's external-pitch unlock and the answer to the *who consumes the violation receipt* question.

## Administrative-law mapping — the positioning unlock

The liveness half doesn't need to be invented. Administrative law has been running it in prose for centuries, badly instrumented:

| Calculus primitive | Administrative-law analogue |
|---|---|
| Wrongful refusal | **Mandamus** (sufficient artifact, withheld effect, ministerial duty) |
| RefusalReceipt | Reasoned-decision requirement |
| NoMovingGoalposts | Fair notice |
| RefusalTimeout / deemed refusal | Deemed-approval statutes |
| Ministerial vs discretionary | The discretionary/ministerial distinction (load-bearing in admin doctrine forever) |
| ExceptionBudget | Exigent-circumstances ratchet under judicial review |
| Appellate independence | Separation of agency adjudication from initial action |

This matters for positioning. The soundness half formalizes **evidence law**; the liveness half formalizes **mandamus and due process**. The corpus is not proposing exotic machinery — it is typing the oldest writs in the common law:

> **We typed the old writs because the machines learned bureaucracy.**

## The eight core refusals — dual lists

Soundness side (existing):

1. Insufficient artifact does not discharge required predicate.
2. Same-custody artifacts cannot witness each other ([[project-admissibility-vs-arms-control]]).
3. Heterogeneity reduces correlation but does not change receipt type ([[project-heterogeneous-turtles-not-witnesses]]).
4. *(other refusal-kernel-specific rules: log ≠ truth, bundle ≠ join, etc.)*

Liveness side (this layer):

5. Sufficient artifact does not permit continued refusal.
6. Refusal without reachable cure is discretion.
7. Non-decision past horizon is refusal.
8. Clock reset by supplement request is laundering.
9. Same-custody appeal is not independent review.
10. Emergency action without exception budget is exception laundering.
11. Blocker without typed/versioned/witnessed discipline is supplemental-request scam.
12. Rule amendment is an effect, not metadata ([deferred to Frontier 3](frontier3-rule-change-deferral.md)).

Dual-list structure: the soundness side says *"this artifact does not discharge that predicate"*; the liveness side says *"this maneuver does not excuse that duty."* Same audit-unit shape, opposite polarity.

## The minimal viable kernel (sprint target, NOT tonight)

```text
Given:
  submitted artifact A
  predicate P sought
  rule version R
  discharge condition C
  actor/boundary B (Ministerial | Discretionary)
  horizon H
  claimant capability class K

If:
  A satisfies C under R before H
  and ReachableCure(C, R, K) holds with progress measure
  and no valid blocking predicate exists (under blocking-predicate discipline)
  and B = Ministerial, then P entails ministerial effect E

Then:
  Owes(B, P, E, H).
  Continued refusal past H emits violation receipt
  consumable by the enforcement boundary.

If B = Discretionary:
  B owes decision + RefusalReceipt within H, not discharge.
```

## Sprint manifest (post-curdling, post-audit)

Per the fourth Claude's structural read, in order:

1. **Doctrine note** — *this file.* Filed 2026-06-06.
2. **Deferral receipt for Frontier 3** — [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md). Filed 2026-06-06. The calculus practicing what it preaches.
3. **Lean spike #1 — small kernels (deferred to 2026-06-07+):**
   - `SufficientBeforeHorizon`
   - `MinisterialEffect`
   - `Owes` / `MustDischarge`
   - `ContinuedRefusal`
   - `DeemedRefusal`
   - First theorem (boring on purpose): `sufficient_receipt_before_horizon_implies_owes`
   - Second: `refusal_after_owes_is_violation`
   - Third: `nondecision_past_horizon_is_deemed_refusal`
4. **Lean spike #2 — the meat (deferred):**
   - `DischargeReachable` with the **progress measure** (NOT acyclic).
   - Termination measure over rule graphs.
   - *The most novel formal object in the set.*
5. **Essay** — `Mandamus.lean` is the working title, but the public-facing essay uses the pitch line directly: *the kernel that proves the institution owed you an answer.*

The public-facing essay is the artifact this calculus has never had: admissibility has no natural constituency (nobody wakes up angry about discharge predicates), but *everyone has been ground by an institution that said "still processing" for eleven months*. The mandamus framing is the door into the stack for readers who will never open a `.lean` file.

## What this is NOT (curdling guard)

- **Not a refusal of refusal.** Refusal is the architecture; the corpus stands on that. This layer adds that refusal must be *accountable* — typed, witnessed, clocked, appealable.
- **Not a new bridge family.** It's a dual to the existing one. Permission and obligation are co-indexed over the effect lattice.
- **Not a claim that institutions will adopt this voluntarily.** The pitch is exhibit-shaped, not adoption-shaped. Records, not adoption ceremonies.
- **Not the constitutional layer.** Rule amendment, self-amendment, and the governance of governance itself live at Frontier 3. See [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md) for the typed deferral. *Touch it now and the sprint becomes a constitutional convention held inside a haunted vending machine.*
- **Not formalizable tonight.** Curdling timer matches the parent doctrines (do not formalize before 2026-06-07); four corrections from the fourth Claude must settle in the prose first; Lean spike comes after.

## Relationship to existing corpus artifacts

This doctrine **adds the other half** to existing artifacts:

- [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) — same-custody axis. This layer adds: same-custody review of refusals also fails the witness test (§ Appellate independence).
- [`heterogeneous-turtles-not-witnesses.md`](heterogeneous-turtles-not-witnesses.md) — receipt-type axis. This layer adds: heterogeneity at the adjudication layer recurses the same problem.
- [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) — obligation atoms over witness. This layer adds: the corpus had a rich theory of permission and nothing of obligation; the obligation atoms are now the spine of the liveness half.
- [`tooltheory/witness-carrier-model-candidate-2026-06-06.md`](tooltheory/witness-carrier-model-candidate-2026-06-06.md) — carrier model. The RefusalReceipt is a carrier; its discipline composes.
- **Paper 27** (obligation-unsound reconciliation) — the obligation-unsoundness result. This layer is the operational machine that paper proposed in principle.
- **Freshness.lean** — clock machinery. This layer points it at the institution instead of the artifact.
- **Three-tier refusal taxonomy** — the test harness.
- [[project-negative-inclusivity]] — *the harm theory of wrongful refusal.* This layer's claimant-capability indexing is where negative-inclusivity lands inside the calculus.
- **Managed insufficiency** — the field guide. This layer is the structural response.

The liveness half wasn't missing; *it was unconsolidated.* Tonight's manifest is the consolidation schema.

## Cross-references

- [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md) — companion deferral receipt; the calculus's first typed deferral of its own constitutional layer.
- [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) — parent doctrine; same-custody refusal extends to appellate review here.
- [`heterogeneous-turtles-not-witnesses.md`](heterogeneous-turtles-not-witnesses.md) — sibling doctrine; receipt-type refusal extends to adjudication layer here.
- [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) — obligation atoms; this layer's `Owes` dual sits over the same atoms.
- [`tooltheory/documentation-keepers.md`](tooltheory/documentation-keepers.md) — keepers from this round.

## Provenance

Filed 2026-06-06 (Fri PM) from a multi-model exchange following the heterogeneous-turtles doctrine:

1. **ChatGPT** proposed effect-indexed admissibility (the acceptance ladder, parameterized `MayAct(surface, effect_class, scope, horizon)`).
2. **Claude (web)** named the missing layer as obligation, not permission refinement — the *liveness gap*: every effect-class rung is a new place to park a claimant; the kernel had a rich theory of one half and nothing of the other.
3. **ChatGPT** consolidated into the liveness dual with `MustDischarge`, `RefusalReceipt`, `ReachableCure`, matter-clock monotonicity, ExceptionBudget, and the administrative-law mapping (mandamus / due process / fair notice / deemed approval / discretionary-ministerial split).
4. **Claude (the fourth pass)** stress-tested with four corrections: acyclic → progress measure; satisfiable-by-whom (claimant-capability indexing); blocking-predicate discipline (the back door); enforcement-boundary framing (record-as-evidence through courts); ministerial/discretionary survives in types. Also named the public handle and the sprint manifest. *Stop generating and start building.*
5. **Operator** carried the threading throughout and produced the original *"safety has no liveness"* observation that opened the layer — the calculus is a soundness theory whose dual is mandamus, not a new theory of agentic permissions.
6. **Claude Code** (this session) filed the consolidated doctrine note 2026-06-06 with the four corrections folded into structure (not buried as caveats) and the curdling timer matching the same-custody parent.

## Jar inventory — keepers from this round

Top tier (operator-flagged or title-shape):

- *"The kernel that proves the institution owed you an answer."* — title-shape; public-pitch line.
- *"We typed the old writs because the machines learned bureaucracy."* — positioning unlock.
- *"Kafka with type signatures."* — the negative version of the same line.

Strong:

- *"Refusal is an accountable act."*
- *"A boundary that cannot state what would discharge the predicate is not performing admissibility. It is exercising discretion."*
- *"An unreachable discharge condition is not claimant insufficiency. It is a refusal authored by the rulemaker."*
- *"The cure path is the new fog."*
- *"Same-custody appeal is not independent review."*
- *"Non-decision past horizon is refusal."*

Jar (kept for the prose voice, not always quotable in pitch):

- *"Bureaucratic TCP keepalive for denial."*
- *"SRE doctrine annexing Carl Schmitt."* (Error budgets for states of exception.)
- *"Strongly worded letter with a type signature."* (What violation receipts without an enforcement boundary become.)
- *"Constitutional convention held inside a haunted vending machine."* (What touching Frontier 3 tonight would have looked like.)
- *"Discretion in a lab coat."* (What unaccountable refusal actually is.)

## Definition of done

> *A reader can use this doctrine to argue, in administrative law or institutional review, that the institution owed them an answer — and the kernel's machinery produces the record that proves it.*

Test: given a real refusal in the wild (benefits, immigration, hospital, moderation, procurement), can a claimant point at the receipt artifacts that prove their case? If the kernel produces the record in admissible form and the courts are the consumer, the loop closes.

> *Soundness was the safety theory — refusal as architecture. Liveness is the legitimacy theory — refusal as accountable act. The first one protects institutions from artifacts. The second protects people from institutions.*

That sentence is the project's second wing.
