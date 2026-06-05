# The Institution Owed You an Answer — mandamus / liveness dual

**Filed:** 2026-06-06 (Fri PM). **Status:** positioning + public-pitch companion to [`refusals-need-receipts.md`](refusals-need-receipts.md). **Memory pointer:** `project-refusals-need-receipts` (shared with companion).

This file is the public-facing angle. The architectural and structural content — primitives, sprint manifest, four corrections, eight refusals — lives in `refusals-need-receipts.md`. This file exists because the project's load-bearing public-pitch line is its own retrievable artifact.

## The pitch

> **The kernel that proves the institution owed you an answer.**

Admissibility has no natural constituency. Nobody wakes up angry about discharge predicates. But everyone has been ground by an institution that said *"still processing"* for eleven months. The mandamus framing is the door into the stack for readers who will never open a `.lean` file.

## The structural shape

Soundness side:
> *This artifact does not discharge that predicate.*

Liveness side:
> *This maneuver does not excuse that duty.*

The first is evidence law. The second is mandamus. The corpus is not proposing exotic machinery — it is typing the oldest writs in the common law:

> **We typed the old writs because the machines learned bureaucracy.**

## The administrative-law mapping (the positioning unlock)

| Calculus primitive | Administrative-law analogue |
|---|---|
| Wrongful refusal | **Mandamus** — sufficient artifact, withheld effect, ministerial duty |
| RefusalReceipt | Reasoned-decision requirement |
| NoMovingGoalposts | Fair notice |
| RefusalTimeout / deemed refusal | **Deemed-approval statutes** (in some jurisdictions, the construction permit is *granted by operation of law* if the agency sits past the deadline) |
| Ministerial vs discretionary | The discretionary/ministerial distinction (load-bearing in admin doctrine forever) |
| ExceptionBudget | Exigent-circumstances ratchet under judicial review |
| Appellate independence | Separation of agency adjudication from initial action |

This makes the project *less* exotic, not more. Less *"new AI governance taxonomy,"* more *"the old writs, typed."*

## The enforcement boundary — the kernel is not the sheriff

The kernel cannot compel. That's outside the system. *Pretending otherwise would be the framework committing its own sin.*

But this is a feature, not a bug. Mandamus has always foundered on the claimant's inability to **prove** the elements: sufficiency, ministerial duty, elapsed time, exhausted process. The kernel's actual product is **the record**, manufactured continuously, in admissible form.

> *The system cannot force the institution to act. It can prove what the institution did, what it owed, when it owed it, and how it failed.*

Pitch:

- **Not:** "adopt our governance framework."
- **Instead:** "everything your system does is now somebody's exhibit."

The loop closes through the courts — the oldest effect boundary, the one that already has a bailiff. The kernel is **the exhibit factory.**

## The duality (architectural framing)

The admissibility stack to date is a soundness theory: refuse to discharge a predicate on insufficient evidence. The degenerate solution to that spec is the boundary that discharges nothing — sound against wrongful acceptance, perfect denial infrastructure, *Kafka with type signatures*.

The missing half — **wrongful refusal** — is the liveness dual:

| Error | Refusal kernel domain |
|---|---|
| Insufficient artifact caused an effect | Soundness side (existing) |
| Sufficient artifact failed to discharge, advance, decide, or receive timely explanation | Liveness side (this layer) |

> *Soundness was the safety theory — refusal as architecture. Liveness is the legitimacy theory — refusal as accountable act. The first one protects institutions from artifacts. The second protects people from institutions.*

That's the project's second wing. It's what makes the whole thing defensible in public, including to the welfare-rights lawyer who would otherwise correctly read the fire doors as locked exits.

## The four corrections that survived stress-testing

(Folded into the architecture in `refusals-need-receipts.md`; named here for orientation):

1. **Progress, not acyclicity.** Legitimate cure paths cycle (revise-and-resubmit). The bad thing is not revisiting a node — it's revisiting with no accountable decrease. Termination measure, not DAG.
2. **Claimant-capability indexing.** A cure path can be formally reachable and *practically enclosed* (literacy-test structure). Reachability is indexed to declared capability class.
3. **Blocking-predicate discipline.** The "no valid blocking predicate" clause is where displaced discretion will rehome. Blockers need: typed, versioned, witnessed, knowable-before-submission, *clock-charged to the institution*.
4. **Enforcement-boundary framing.** Violation receipts don't compel — they manufacture admissible record. Courts are the consumer.

Plus a fifth: **ministerial / discretionary must survive in types.** Discretionary surfaces never owe discharge; they owe reasoned, receipted decision within horizon.

## Cross-references

- [`refusals-need-receipts.md`](refusals-need-receipts.md) — companion: architectural doctrine + primitives + sprint manifest.
- [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md) — typed deferral of the constitutional layer.
- `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` — the build proof.
- [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) — same-custody axis (appellate independence here recurses that rule upward).
- [`heterogeneous-turtles-not-witnesses.md`](heterogeneous-turtles-not-witnesses.md) — receipt-type axis.
- [[documentation-keepers]] — full keeper register.

## Provenance

Same multi-model exchange as the companion file. See `refusals-need-receipts.md` § Provenance for the full walk. This file is the focused-positioning artifact derived from that exchange — the pitch line, the admin-law mapping, the exhibit-factory framing.
