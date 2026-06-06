# Heterogeneous turtles are not witnesses

**Filed:** 2026-06-06 (Fri PM). **Status:** doctrine note + agentic-system specimen bridge. **NOT** a candidate Lean kernel. **Curdling guard:** same discipline as the parent doctrine in [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) — *do not formalize before 2026-06-07; cursed little theorem gremlins are a separate file from this one.*

**Custody:** doctrine note; pre-ratified per name-early. Companion to [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) § The core rule — *same-custody artifacts cannot witness each other* is one axis of witness-source quality; this note names the orthogonal axis: *multi-source same-type artifacts cannot witness each other either.* Memory pointer: `project-heterogeneous-turtles-not-witnesses`.

## The headline theorem

> **Heterogeneity reduces correlation. It does not change receipt type.**

Decorrelation is not discharge. A heterogeneous verifier stack produces multiple assessments with lower shared failure probability. It does not transform assessment into observation. N uncorrelated model verdicts remain in the *claim* column unless one verifier is coupled to an external witness.

## The three-way split

```text
Homogeneous verifier stack:
  one claim echoed through shared failure modes.
  Common hallucination cone.

Heterogeneous verifier stack:
  multiple claims with lower shared failure probability.
  Respectable jury, but a jury that observed nothing.

Witness:
  an observation coupled to the world or authority surface.
  Receipt of a different type than the artifact being verified.
```

Heterogeneity gets you from row 1 to row 2. It does not get you from row 2 to row 3.

## Core refusals

> **Consensus does not discharge `Witnessed`.**

> **Uncorrelated assessment does not discharge `Observed`.**

> **`ModelVerifier(worker_output)` may discharge `Reviewed`, `Disputed`, `Undisputed`, or `NeedsWitness`. It does not discharge `True`, `Observed`, `Safe`, or `MayAct`.**

## What coupling-to-world actually looks like

A verifier earns admissibility at an effect boundary only when it can produce or bind a receipt of a different *type* than the artifact being verified. Examples of non-turtle witnesses:

- compiler / typechecker result
- unit / integration test
- signed external API response
- sensor reading
- ledger entry
- database state under custody
- human observation with accountable standing
- reproducible experiment
- policy engine with typed authority input

At that point the model may *interpret* the receipt, but it did not *mint* the receipt. The ground did. The receipt-type is different from any model output.

## The brutal image

> *A jury can weigh testimony. It cannot become the eyewitness by agreeing really hard.*

Heterogeneous model verifiers form a jury. The jury can deliberate, disagree, force questions back to the worker, surface inconsistencies. What the jury cannot do: become the eyewitness through process. There is no number of model verdicts that adds up to one observation.

## The operative gem

> **A verifier becomes useful at an effect boundary only when it can produce or bind a receipt of a different type than the artifact being verified. Otherwise the system has improved its covariance matrix, not its admissibility.**

The covariance-matrix line is the load-bearing one — it gives the difference between *useful epistemic hygiene* (real, valuable, not what this doctrine attacks) and *admissibility discharge* (the thing it refuses).

## Defense against agent-team diagrams

The question for any proposed multi-agent verification scheme is not *"how many checkers?"* It is:

> **Which checker can produce evidence of a different type than the worker's output?**

If none, the diagram is **barbershop epistemology**: a lot of confident assessment, no admissible observation. Adding more agents — even heterogeneous ones — improves the covariance matrix without changing the conclusion: nothing in the loop has touched the ground.

## The relationship to same-custody (parent doctrine)

[`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) § The core rule says *same-custody artifacts cannot witness each other.* That refuses a witness because of where it came from (same source). This doctrine refuses a witness because of what kind of thing it is (same type, even across multiple sources). The orthogonal axes:

| Witness-source axis | Refusal | Specimen |
|---|---|---|
| Same custody chain | NORAD 1979: training tape + display + alert all share custody | Independent sensor family required |
| Same evidence type | N model verifiers: all produce `assessment` regardless of how many | External coupling (test result / sensor / ledger / etc.) required |

A witness must clear **both** axes: independent custody **and** receipt of a different type than the artifact. Either failure refuses the discharge.

## Modern analogues

- **"We had three different LLMs review the output."** — heterogeneous turtles. The receipt type is still *model assessment*; the worker's output also produces *model assessment*-shaped artifacts. Same evidence type across the stack. Refusal: this discharges `Reviewed`, not `Observed`.
- **"The agent ran its own tests."** — depends entirely on whether the tests are agent-generated stubs (turtles) or compiler/runtime artifacts coupled to the actual code (witness). The distinction is *who minted the receipt*.
- **"Consensus across the panel."** — *consensus does not discharge `Witnessed`.* A panel that has not observed anything cannot become an observer through agreement.
- **"Multi-model self-review."** — see above. The Claude-common-mode discipline ([[feedback-claude-common-mode-synthesis]]) names the homogeneous version; this doctrine names the heterogeneous version. Both fail for the same root reason: no receipt of a different type.

## Override discipline (carries from parent)

When a heterogeneous-turtle review needs to be treated as if it discharged a stronger predicate (institutions sometimes need this release valve), the override is admissible only if it mints a custody-bearing artifact:

```text
Override(actor, time, predicate_bypassed, reason, evidence_considered)
```

with `evidence_considered` enumerating the model verdicts as *assessments*, not *witnesses*. The override is then admissible against the bypasser per the parent doctrine. The bypass is recorded; the doctrine is preserved.

## What this is NOT (curdling guard)

- **Not a refusal of heterogeneous verifier stacks generally.** They are useful for triage, disagreement surfacing, and common-mode reduction. The refusal is specific: they do not discharge witness-type predicates.
- **Not a claim that humans automatically witness.** Human observation with accountable standing is one entry in the coupling list; humans-as-rubber-stamp is another turtle on the stack.
- **Not a new bridge family.** This is a *transversal quality* on witness-source: the receipt-type axis, orthogonal to the same-custody axis from the parent doctrine.
- **Not formalizable yet.** The "different type" predicate is too rich to encode this week. The carrier model's `evidence_ref` field gestures at it but does not formalize the type-distinction across artifact-vs-witness. Curdle.

## Relationship to existing corpus artifacts

This doctrine **constrains** every refusal kernel without **replacing** any:

- [`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md) — parent doctrine; same-custody axis. This file adds the receipt-type axis.
- [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) — obligation atoms say what a witness must preserve. *Same-custody* says where it can't come from. *Receipt-type independence* says what kind of thing it must be. All three are transversal qualities, not new families.
- [`tooltheory/witness-carrier-model-candidate-2026-06-06.md`](tooltheory/witness-carrier-model-candidate-2026-06-06.md) — the carrier model's `evidence_ref` field carries the "link to underlying evidence" obligation; this doctrine sharpens it: the underlying evidence must be of a *different type* than any artifact in the verifier stack producing the carrier.
- [`tooltheory/documentation-keepers.md`](tooltheory/documentation-keepers.md) — keepers added today: covariance-matrix line; heterogeneity-receipt-type theorem; consensus-not-Witnessed; barbershop epistemology.
- [[feedback-claude-common-mode-synthesis]] — the homogeneous version of this doctrine, scoped to Claude-reviewing-Claude. This file is the more general statement.
- [`vocabulary/receipt-and-witness-senses.md`](vocabulary/receipt-and-witness-senses.md) — receipt/witness role-disambiguation glossary. This doctrine's *"type"* classification (production-mechanism: model vs compiler vs sensor vs ledger vs signed external vs human observation vs reproducible experiment vs policy engine) is the *transversal meta-axis* across the glossary's three role senses (submission record / verdict artifact / non-authorizing acknowledgment), NOT a fourth role sense. The orthogonality with the same-custody axis ([`admissibility-vs-arms-control.md`](admissibility-vs-arms-control.md)) is recorded there as well.

## Provenance

Filed 2026-06-06 (Fri PM) from a multi-model exchange following the supply-side / demand-side reconciliation:

1. ChatGPT named the missing anti-agentic-slop theorem and produced the three-way split (homogeneous / heterogeneous / witness).
2. The covariance-matrix sentence emerged from the operator: *"Otherwise the system has improved its covariance matrix, not its admissibility."* — the operator-flagged keeper.
3. The "barbershop epistemology" framing emerged from the operator's defense-against-agent-team-diagrams paragraph.
4. The "jury that observed nothing" image is the doctrinal compression — a jury can weigh testimony, not become the eyewitness.
5. Claude Code filed the consolidated doctrine note 2026-06-06 with cross-references to the same-custody parent and the bridge-obligation lattice. Same curdling timer.

## Definition of done

> *A reader can refuse a heterogeneous-verifier discharge in their own institution without having to argue the math of decorrelation. The argument is type-level, not statistical.*

Test: given a proposed agent-team verification scheme, can you state which receipt type its witnesses produce, and whether any verifier produces a *different* type than the worker's output? If no verifier in the loop produces a different type, the scheme is barbershop epistemology regardless of how decorrelated the model panels are.
