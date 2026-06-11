# Refusal-aware IDL — contained counter-spec (rejected interface)

> **RKL v0.0-negative: why the obvious DSL is almost right and
> therefore dangerous.**

**Status:** Contained counter-spec / anti-rederivation note.
**Not candidate doctrine. Not a new architecture. Not a replacement
for [[forbidden-inference-register]] or [[conversion-router-candidate]].**
**Date filed:** 2026-06-10.
**Custody:** working note in `working/tooltheory/`. No Lean module, no
parser, no crate, no schema commitment, no promotion path from this
file.
**Provenance:** DeepSeek "RKL v0.1" spec + ChatGPT correction pass,
2026-06-10 relay; audited in
[[guarded-lift-admission-overlap-audit-2026-06-10]]. This file is the
quarantined preservation of the interface shape plus the corrected
semantics, so neither has to be re-derived — and so the broken version
cannot be re-proposed as new.

---

## 1. Why this note exists

The 2026-06-10 relay produced a refusal-aware IDL sketch ("RKL") that
is attractive, register-consistent, and **semantically broken in a
specific, instructive way**. The overlap audit refused it as a
candidate (it is the unifier-shaped object
[[project-no-unifier-without-laundering]] refuses, and its live,
correctly-scoped sibling is [[conversion-router-candidate]]). But
refusing it without preserving it invites two failure modes:

1. **Re-derivation.** A future fresh-context session will reinvent the
   IDL shape — the vocabulary is too natural not to recur. Without
   this note, the next session re-derives both the shape *and* the
   bug.
2. **Rake repetition.** The fatal semantic error (treating kernel
   refusal as absolute refutation) has now appeared **twice** from the
   same external model in three weeks (see §3). It is a named failure
   mode. The corrected model deserves a citable location.

So: preserve the shape, pin the rake, show the correction, point at
the artifacts that already do the real work. This is a **counter-spec**
in the same genre as a rejected-design ADR — its value is what it
prevents, not what it builds.

The constructive reading, stated once so the containment doesn't read
as a ban: the corrected core (§4–5) is a legitimate **interchange
notation** — a common envelope for describing lift attempts,
objections, bridges, witnesses, and receipts that existing artifacts
already expose. RKL-as-envelope serializes downstream of the
constellation; it is never the source of truth. *It is the placard
next to the machine saying which parts sever fingers* — not the
machine, not the machine's replacement, and not a unifier wearing
notation clothes. What stays refused is RKL-as-engine, RKL-as-calculus,
and RKL-with-the-broken-semantics.

## 2. The tempting RKL shape

The shape that keeps getting proposed (quarantined exhibit — this is
the **rejected interface**, reproduced so it can be recognized, not
used):

```text
Kernel   ::= 'kernel' Id '{' refuses Lift+ '}'
Lift     ::= Id '->' Id
Bridge   ::= 'bridge' Id 'admits' Lift 'from' KernelId 'to' KernelId 'under' Guard
Witness  ::= 'witness' Id ':' Guard
Receipt  ::= 'receipt' Id '{' status ';' info* '}'
Status   ::= 'Admitted' | 'RefusedByPolicy' | 'RefutedByKernel' | 'Unknown'
Query    ::= 'explain' Lift 'with' Testimony 'for' Consumer 'in' KernelSet
```

With validity and evaluation rules (RKL v0.1, verbatim in substance):

> A bridge is **valid** iff there is no kernel in the current set such
> that `refuses_K(L)` is provable.
>
> Evaluation: for each kernel `K`, if `refuses_K(L)` holds, return
> `RefutedByKernel`. **Else**, for each bridge admitting `L`, if its
> guard holds, return `Admitted`. Else `RefusedByPolicy` or `Unknown`.

Why it tempts: the surface reads exactly like the corpus. Kernels
refuse lifts; bridges admit them under guards; receipts carry
provenance; `Unknown` is first-class. Four of the five nouns are
already corpus vocabulary. The grammar is small enough to look
harmless.

What the IDL framing gets *right* (worth preserving):

- **Receipt as output, not decision.** The artifact explains a refusal;
  it does not adjudicate access.
- **`Unknown` is first-class.** No false closure; "no modeled answer"
  is a legal verdict, not an error.
- **Bridges are first-class named objects**, not exceptions or
  overrides.
- **No global composition law is assumed.** Composition exists only as
  named, guarded, proof-bearing lift admission.
- **Notation-first, engine-never** as the stated ambition (the
  ambition was honest; the semantics betrayed it — see §3).

## 3. The fatal rake: absolute refusal collapses guarded bridge discharge

RKL v0.1's own worked example:

```text
kernel Medical {
  refuses PatientData -> Diagnosis
}

bridge ConsentBridge
  admits PatientData -> Diagnosis
  from Medical to Medical
  under exists c:Consent(c.patient == testimony.patient && c.signed)
```

Expected output: `Admitted` via `ConsentBridge`.

Actual output under its own semantics: `RefutedByKernel`, always. The
evaluation rule consults kernels **before** bridges and returns on the
first refusal; the validity rule makes any bridge over a refused lift
**invalid by definition**. The spec encodes:

> bridges may only admit lifts that no kernel refuses

— which makes every bridge either vacuous (nothing refused the lift,
so nothing needed admitting) or invalid (something refused it, so the
bridge cannot exist). **A drawbridge that only opens when there is no
moat.**

The root error: modeling `refuses : Lift → Prop` as an **absolute
property of the lift**, when the corpus's refusals are **objections
against a specific basis, raised in a specific context, dischargeable
by a specific named bridge**. A kernel refusal is not "this lift is
impossible." It is "this lift does not go through *on the basis
offered*, absent the named bridge."

This is the second instance of the same collapse from the same
external model:

- **2026-05-25** ([[refusal-kernel-to-refusal-receipt-seam]],
  provenance section): `if Fluent s then CANNOT_TESTIFY` — refusing
  *the system* instead of *the basis offered*. Corrected to: the
  runtime refuses the forbidden basis kind for the forbidden use,
  never a property of the system.
- **2026-06-10** (this note): bridge-valid-iff-no-kernel-refuses —
  refusing *the lift absolutely* instead of *raising a dischargeable
  objection*.

Same flattening both times: **objection-indexed refusal collapsed into
absolute refusal.** When an external model's spec makes its own worked
example unsatisfiable, check for this collapse first (sibling tell to
[[feedback-enum-regression-tell]]).

The corrective keeper:

> **A bridge does not require the absence of refusal; it is a named,
> guarded discharge of a specific refusal objection.**

This is not a new claim — it is a restatement of structure the corpus
already carries (the CONDITIONAL edge type in [[seam-graph-candidate]]:
*preservation gated by an obligation discharged at construction*; the
five-element bridge tax in [[project-no-unifier-without-laundering]]).
The counter-spec exists because external models keep losing exactly
this structure in translation.

## 4. Corrected core: Attempt → Objections → Discharges → Receipt

The minimal honest semantics, stated so the next relay can be checked
against it:

```text
LiftAttempt = (source, target, testimony, consumer, context)

objections : Kernel → LiftAttempt → Set Objection
discharges : Bridge → Objection → Witness → Prop
```

Evaluation of an attempt:

```text
1. Collect objections from every applicable kernel in context.
   An objection names: the forbidden basis promotion, the refusing
   kernel, its strength, and (if dischargeable) the bridge kind that
   would discharge it.

2. Classify each objection by strength:
   - refutable      — a no-lift theorem applies; NOT dischargeable
                      (Lean countermodel / non-inhabitation; the
                      formal layer's verdict)
   - dischargeable  — policy/boundary objection; a named bridge kind
                      could discharge it, given a witnessed guard
   - unmodeled      — the kernel cannot classify this attempt

3. Apply bridges. A bridge discharges ONLY the objections it
   explicitly names, and only with a witnessed guard. Discharge is
   per-objection, never per-lift.

4. Resolve status:
   - refuted_by_no_lift_theorem — an undischargeable (refutable)
                                  objection remains
   - admitted_by_bridge         — every blocking objection discharged
                                  by a witnessed bridge; receipt lists
                                  discharges
   - refused_missing_bridge     — dischargeable objection remains and
                                  no bridge of the named kind is on
                                  file
   - refused_missing_witness    — bridge on file, guard not witnessed
                                  for this attempt
   - unknown_unmodeled          — no kernel could classify the attempt
```

Five values, not four. The relay's square (`Admitted / RefusedByPolicy
/ RefutedByKernel / Unknown`) collapses missing-bridge into
missing-witness, which are different repair paths (author a bridge vs.
produce a witness). And five is still a **projection**: the router's
six cut kinds (COUNTERMODEL / NO-LIFT / BLOCKING / ISOLATION /
MODEL-DEPENDENCE / DECLARED-MISSING) remain finer and win on conflict.
Do not degrade the constellation into four labels because an LLM found
a nice square.

Receipt shapes (illustrative, not a schema commitment):

```json
{
  "status": "refused_missing_bridge",
  "lift": "PostValidatedLater -> AuthorizedAtDecision",
  "objection": "post_validation_not_authorization",
  "refusing_kernel": "RetroactiveFigLeaf",
  "missing_bridge": "decision_time_authorization",
  "consumer": "Nightshift"
}
```

```json
{
  "status": "admitted_by_bridge",
  "lift": "PatientData -> Diagnosis",
  "bridge": "ConsentBridge",
  "witness": "consent_form_456",
  "discharged": ["no_basis_for_diagnosis_lift"]
}
```

Three constraints the corrected core must keep (the constitution, from
the seam note and the audit):

```text
Lean refutation        ≠ runtime refusal
runtime missing-bridge ≠ logical impossibility
bridge admission       ≠ global kernel composition
```

And two arity warnings:

- **Bare `Lift = Id -> Id` is too thin.** Real refusals depend on
  consumer, time, witness freshness, use-kind, standing, scope. The
  attempt tuple above is a *projection* of the seam note's seven-tuple
  `(claim, basis, witness, scope, time, use_kind, consequence)`; any
  implementation defers to that, not to this.
- **Receipts are not retroactively falsified by kernel-set change.**
  Old receipts stay historically true relative to their kernel-set /
  contract version (`tree_or_build_id` discipline); they may become
  superseded/stale/out-of-scope, never silently rewritten.

## 5. Minimal vocabulary

Seven nouns, each with its existing home — none minted here:

| Noun | One line | Existing home |
|---|---|---|
| **Kernel** | names a refusal boundary; raises objections against attempts | Lean refusal kernels, `LeanProofs/Admissibility/` |
| **LiftAttempt** | proposed movement testimony→consequence, indexed by consumer/context | "forbidden inference" rows in [[forbidden-inference-register]]; seam-note seven-tuple |
| **Objection** | a kernel's named, strength-classified block against a specific attempt | cut kinds in [[seam-graph-candidate]] (COUNTERMODEL / NO-LIFT / BLOCKING / DECLARED-MISSING / …) |
| **Bridge** | named, guarded permission for one lift; discharges only the objections it names | bridge tax (five elements) in [[project-no-unifier-without-laundering]]; CONDITIONAL edges |
| **Guard** | decidable condition under which a bridge may discharge | obligation-discharged-at-construction pattern (`CorrectiveMonotone`, `SafetyEnv.preserves`) |
| **Witness** | the evidence instance satisfying a guard | witness/receipt discipline; `ns.wlp_refusal.v1` lineage |
| **Receipt** | the output: status + objections + discharges + missing bridges | [[conversion-router-candidate]] receipt artifact (`ns.claim_route.v1` candidate fields) |

## 6. Mapping to existing artifacts

This counter-spec adds **no machinery**. Everything load-bearing
already exists, in finer grain:

| Counter-spec element | Existing artifact | Note |
|---|---|---|
| Specimen inventory of forbidden lifts | [[forbidden-inference-register]] (2026-05-26) | the relay's "first durable artifact," built two weeks before the relay |
| `explain` query + verdicts | [[conversion-router-candidate]] (2026-06-09): `path / blocked / open` | the live, Nightshift-scoped engine shape; this note defers to it entirely |
| `refuted_by_no_lift_theorem` vs `refused_missing_*` | router cut kinds: COUNTERMODEL/NO-LIFT (theorem-backed) vs DECLARED-MISSING (receipted absence) | router's six cut kinds are **finer** than the five statuses here |
| `unknown_unmodeled` | router verdict `open` ("no theorem-backed edge or cut registered") | identical semantics |
| Objection-discharge model | CONDITIONAL edge type + bridge tax | §3's keeper is a restatement, not an addition |
| Lean/runtime split | [[refusal-kernel-to-refusal-receipt-seam]] (2026-05-25) | including the first instance of the same rake |
| Cedar/XACML/OPA positioning | [[cedar-shaped-certificate-checker-candidate]] (superseded archive) + router's "Explicitly NOT Cedar" | comparison already done and bounded |
| Audit provenance | [[guarded-lift-admission-overlap-audit-2026-06-10]] | the receipt that classified the relay this note quarantines |

If any element of this note appears to conflict with the router
candidate or the register, **those artifacts win** — this file is
downstream commentary, not source of truth.

## 7. Non-claims / refusal list

Explicitly NOT promoted by this note:

- **No general engine.** No runtime, no evaluator, no decision
  procedure. The only engine-shaped artifact remains
  Nightshift-local per [[conversion-router-candidate]].
- **No parser, no surface syntax.** The §2 grammar is a quarantined
  exhibit of the rejected interface. Building syntax before an IR
  before a consumer is the vocabulary-mill failure mode.
- **No calculus.** No composition laws are claimed. Per the seam
  note's ladder: specimens → annex; composition theorems → calculus.
  None landed here.
- **No category semantics.** No objects, morphisms, identities, or
  composition. "Category where morphisms are guarded bridges" remains
  a possible *later* semantics, unclaimed; the identity-bridge
  question alone is unresolved and stays that way.
- **No deontic umbrella.** I/O logic remains one prior-art row, not a
  framing.
- **No cross-repo shared notation.** A general refusal-aware IDL is
  the unifier-shaped object the no-unifier doctrine refuses; the only
  lawful path to shared notation is the router candidate's build
  trigger firing, and that path runs through *that* file, not this
  one.
- **No venue posture.** The relay's CSF/PLAS/POPL steering is refused
  per standing venue posture (books + Zenodo). Nothing here is a
  paper, a tool demo, or "PC-survivable" anything.

## 8. Promotion gate, deliberately unmet

For completeness, the conditions under which an objection-indexed
refusal notation could earn promotion — listed to record that **none
is met and this note is not waiting for them**:

1. [[conversion-router-candidate]]'s build trigger fires (second
   non-Freshness blocked conversion at Nightshift runtime, or a third
   refusal kind demanding the same artifact-emission pattern) — in
   which case the router note, not this one, is the live artifact.
2. A **second runtime consumer** beyond Nightshift needs to consume
   the same receipt vocabulary, forcing a genuine cross-repo
   serialization question.
3. An actual consumer needs the **objection-indexed** distinction
   mechanically (per-objection discharge, not per-lift verdict) and
   the router's cut-kind taxonomy cannot express it.
4. The whole stack survives a fresh kernel-overlap audit at that
   future date ([[feedback-kernel-overlap-audit]]).

If all four fire, the promotion artifact is an extension of the
conversion-router schema. This file's job at that point is to be the
ADR explaining why the bridge-validity semantics look the way they do
— and to stop the drawbridge bug from shipping.

Until then:

> **The counter-spec is the receipt that the interface was considered,
> the rake was named, and the correction was filed. Nothing else moved.**

## Cross-references

- [[guarded-lift-admission-overlap-audit-2026-06-10]] — parent audit
  receipt; classification of the full relay.
- [[forbidden-inference-register]] — the durable specimen inventory.
- [[conversion-router-candidate]] — the live, correctly-scoped engine
  candidate; owns the build trigger.
- [[refusal-kernel-to-refusal-receipt-seam]] — layer split, seven-tuple,
  first instance of the rake.
- [[seam-graph-candidate]] — edge/cut typing this note's objection
  strengths map onto.
- [[project-no-unifier-without-laundering]] — why no general IDL.
- [[feedback-kernel-overlap-audit]] — the gate any future promotion
  re-runs.
