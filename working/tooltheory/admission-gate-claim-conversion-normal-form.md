# The admission gate (claim-conversion normal form) — name, boundary, fences

**Filed:** 2026-06-15 in `tooltheory/`. **Status:** deliberate *theory freeze* (name + boundary
+ fences), so neither proof nor implementation starts from vibes. The original filing assigned
the P0 normal-form gate to AG-Claude and put Lean behind the running gate. **That sequencing was
superseded 2026-07-14:** formalization leads code. A coherent formal boundary may be stated and
proved before any runtime consumer exists; the runtime gate then implements that boundary and
supplies separate conformance evidence.

## NAME FENCE — "Admission Calculus" collides with the retired-vocab decision

**What this is and isn't (do not skip).** Flagging the name is a *consistency check against the
project's own declared order*, **not** a judgment that the name is wrong. "Calculus" was retired
from live authority surfaces 2026-06-03 ([[project-calculus-vocabulary-retired]]): "Admissibility
Calculus" is the rejected paper name ([[project-paper-naming-stack]]), "Boundary Calculus" →
"Boundary Kernels". The retirement is **anti-laundering, not lexical purity** — "calculus" may
still appear as archaeology, fenced lineage, or exact old artifact names; what's marked
overclaim-prone is adopting it as a *new live noun*. "Admission Calculus" is that adoption, a
hair from the rejected name; the user flagged it ("calculus is the tell").

**Honest epistemic status.** This flag *echoes a past decision back with a fresh timestamp* — it
shows the apparatus is consistent with the declared order; it does **not** witness that the
decision (then or now) was *right*. By this note's own spine, no "is this right" verdict is
available from inside the order. So the compliant name below is **recommended as
consistent-with-declared-order, not validated.** (First-pass framing waved five-model agreement
around as a "common-mode catch" — retracted: agreement is not evidence, and a tripwire matching a
string against your own list is an echo, not an independent witness.)

Compliant names (paper/Lean-facing surface): **admission gate**, **claim-conversion normal
form**, **admission normalizer**. Avoid on this surface: *calculus, logic, foundation, kernel*.
Operative line for AG: *this is not a new epistemic calculus; it is a runtime gate that refuses
unlicensed conversion between epistemic species.*

**Status: `quarantined_alias`, not `refused`** (the precise state — itself a lesson from
over-refusing in the first pass):

```text
status       = quarantined_alias
reason       = collides with retired live-surface vocabulary (learned: attracts unification stink)
allowed_use  = scratch / historical / explanatory
blocked_use  = canonical module name or paper title
override     = operator judgment (the declared order is yours to amend)
```

Not "the word is cursed." Quarantine happens at *naming* time; the actual fail-closed lives
downstream at *reliance* (see Hand-off).

## The thing (one paragraph)

The layer **after receipt/witness capture** and **before epistemic logic proper**: it decides
whether a claim may be *admitted for reliance by a consumer* under scope / freshness / authority
/ provenance / kind-constitutivity. **It does not decide truth.** The receipt kernel says *this
happened*; the admission gate says *don't pretend that means more than it does.*
Epistemic/doxastic/justification/dynamic logics model an agent's *attitude* toward φ (knows /
believes / revises / justifies) — all on the believer's side of the door. The gate is the
**door**. The verbs it owns: admit / refuse / downgrade / scope / expire / supersede /
quarantine / promote.

## The seed (why typing the claim is right)

> **Math is not foundationless — it is worldless until applied.** Formal knowledge is invariant
> under representation; empirical knowledge is hostage to representation; **admissibility lives
> at the hostage exchange.**

`3 = 3` asks the world no permission (invariance under renaming = the signature of necessity).
"There are three roses" is math *bound to a world-model* (rose / discrete / countable /
same-kind / present-at-t / distinguishable). The cost enters at "rose," not at "3." **Arithmetic
is cheap; individuation is expensive.** (The formal floor still doesn't self-certify — that's
**Agrippa**, per the related-work foundations bucket; **NOT Gödel**.)

Claim species — candidate vocabulary, *earned by the refusal rules, not by listing*:
`Formal | ModelBound | Observed | Testimonial | Normative | Stipulated`. The conversion the gate
exists to refuse: **Formal ⊬ world-claim without a model-binding receipt.**

## The genuinely-new axis: constitutivity (the thermometer joins the weather)

A `ModelFidelityReceipt` assumes a target *independent* of the model. **Constructed kinds
violate that:** the model *participates in producing* the kind (creditworthiness, engagement,
GDP, a score). Fidelity then goes trivially perfect and meaningless — you can't be unfaithful to
a thing your instrument creates. So beside fidelity, a **constitutivity disclosure**, whose
load-bearing field is **`instrument_role` = Measures | Classifies | Allocates | Enforces |
Creates**. The political knife:

> If `instrument_role ∈ {Allocates, Enforces, Creates}`, the claim may not be presented as
> neutral measurement. *You don't get to call it measurement after the instrument starts
> issuing orders.* Formal machinery over a constructed kind is governance whether you admit it
> or not.

Two refinements:
- **The hybrid presented as stable is the dangerous case** (enough real substrate to make
  StableKind plausible while the constituted overlay does the political work). So `kind_claim`
  is the battleground; the gate **records the assertion, doesn't adjudicate it** — it relocates
  the fight to one field, doesn't end it.
- **Teeth in time:** a constructed kind deforms the world it measures (Goodhart) → the gate
  wants a **performativity clock** (ticks on reliance-volume / decision-surface /
  population-adaptation / gaming-signal / policy-induced distribution shift), **not** just data
  age. Freshness catches stale data; it doesn't catch the spec reshaping its target.

**Overlap audit — name-early axis, NOT a new kernel:** this is **Labelwatch's `authority_effect`**
(constitutivity taxonomy in a Bluesky hat — Measures vs Enforces), plus
[[project-negative-inclusivity]] (Goodhart / *durability* of distortion), plus the diachronic
performativity layer ([[governance-kernel-scope-correction]] § surfaces 6–7). File the
*constitutivity axis* against the family map; do not mint a fresh kernel.

## Related-work shelf (registered, fenced)

Registered in the demand-side related-work map (`admissibility-related-work-map.md`): **epistemic
logic** (Hintikka `K_a`; factivity = the **T axiom** `K φ→φ`, *not* the field; S5; doxastic =
fallible belief), **justification logic** (Artemov `t:φ` — the signature made explicit),
**dynamic epistemic logic** (updates), **AGM** belief revision, **BAN authentication logics**
(belief / freshness / jurisdiction / provenance — tightest rhyme), **Halpern–Moses** common
knowledge. Plus the **warrant lattice** the nap surfaced (analytic/synthetic + Quine's gradient;
necessary/contingent; a priori/a posteriori; **Kripke's** necessary-a-posteriori `water=H₂O` —
necessary ≠ derivable ≠ certain, a lattice not a line).

Fences (all heuristic, vocabulary-not-artifact):
- *The field is the country; the gate is the border.* Epistemic logic operates **after**
  admission; the gate **is** admission. None of it has a **Refusal** operator — it assumes the
  problem away.
- *Found the shelf ≠ handed the artifact.* "A research field exists" is a **signature, not a
  witness** that the gate runs. Reading makes the build better; it doesn't make it built.
  ("Maybe I don't have to build it" is forum-shopping the witness into a literature review.)
- **Halpern–Moses is a ceiling, not a tool:** common knowledge is unattainable over a lossy
  channel → states the governor can never certify. The Agrippa/Münchhausen floor, with a
  citation.
- **No Gödel inflation** (the foundations bucket already carries the NON-CLAUDE flag); **no
  "foundation."**

## Formalization posture (supersedes the original runtime-first stop sign)

The no-lift specimen *does* fall out — **Formal ⊬ world-claim without a model-binding receipt**
is `NoFreeStandingBridge` in the formal→empirical direction; family-consistent, name-early.
The theorem does **not** wait for executable admission behavior in the governor. It may be
formalized as soon as its claim species, model-binding relation, and refusal conclusion are
stated precisely enough to support a non-vacuous proof. The "receipt-shaped incense / loop
constituting its object" framing remains a useful heuristic against speculative machinery, but
it is not an admission gate for formal work. Runtime implementation is downstream: the P0 gate
must identify the theorem or formal contract it implements, and runtime evidence must establish
conformance. Neither a running gate nor a consumer is permission to begin the proof.

## Hand-off

- **Paper/Lean:** name + boundary + fences, then state the minimal conversion/refusal contract
  and its non-vacuous laws. Formalization may proceed before P0 exists; public promotion remains
  a separate custody and review decision.
- **AG-Claude:** build **P0** against that contract — a minimal normal-form admission gate (a
  *conversion checker*:
  not a theorem prover, not a policy language; no plugins / reflection / self-amendment). Sits
  after receipt/witness capture, before `derive_in_bounds` / promotion eligibility — the
  membrane between *recorded* and *usable* material. Five specimens to refuse cleanly:
  `3*3=9`→Formal-admitted; "9 servers"→refused w/o observation binding; "credit score measures
  creditworthiness"→refused/downgraded (Hybrid + Allocates/Enforces); "Reddit consensus says
  X"→testimony-yes / fact-no; "Coq proved system safe"→refused unless scoped `O over A` with
  `does_not_claim`. AG territory; not authored here. (Name the module *not*-calculus; treat
  "Admission Calculus" as a `quarantined_alias`, not canonical.)

**Design lesson carried from this exchange (the compiler-shaped takeaway).** Separate
*quarantine* (exploration/naming time) from *fail-closed* (reliance/promotion time). P0's
classification should be four-state, not binary:

```text
ClassificationResult = Candidate | Quarantined(reason) | Admitted(scope) | Refused(reason)
```

Only `Admitted` feeds governor reliance; `Quarantined` stays inspectable / discussable / testable
but **cannot promote**. The rule:

> Don't fail open. Don't fail closed at discovery. **Fail quarantined until reliance is
> attempted.**

This is the generalization of paper/Lean-Claude's own first mistake in this very arc — refusing a
name at *discovery* on a string-match, when the correct move was quarantine-pending-operator.
Recorded as a **recommendation** for AG (and validated by the exchange, not by an oracle), not an
imposed implementation. The formal contract leads this implementation; passing runtime examples
does not by itself prove conformance.

## Provenance

Multi-model 2026-06-15: the nap-delivered formal/empirical-typing seed → ChatGPT species +
constitutivity + `instrument_role` → Claude-web constitutivity/performativity refinement + the
stop-sign → DeepSeek's epistemic-logic shelf pointer (the one good pointer; raid the vocabulary,
not the claim). Keepers: *worldless until applied*; *arithmetic cheap, individuation expensive*;
*the thermometer joined the weather*; *you don't get to call it measurement after the instrument
starts issuing orders.* The original filing froze elaboration and made the build the next move.
The 2026-07-14 correction preserves that provenance while superseding its runtime-before-Lean
sequence: formalization now leads code.
