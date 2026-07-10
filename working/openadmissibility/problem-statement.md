# OpenAdmissibility: A Problem Statement for Profile-Scoped Reliance Decisions

**Status:** working draft v0.1 (2026-07-09). Rung 1 of the publication
ladder in [README.md](README.md). Written to be readable by someone with no
prior contact with this body of work. Compressed from
`working/where-admissibility-fits.md` and siblings; provenance at the end.

---

## The problem in one question

Every operational system — CI pipeline, deploy gate, agent runtime,
monitoring stack, compliance process, ML eval harness — at some point
converts a *claim* into *permission to act*:

> May this claim be used to authorize this consequence?

The tests passed, so merge. The attestation verified, so deploy. The
monitor saw nothing, so close the incident. The eval scored above
threshold, so ship the model. The timestamp is recent, so the data is
fresh. The operator clicked approve, so run it.

Almost no system asks this question explicitly. It is asked implicitly, in
glue code, at a hundred unmarked sites — and at unmarked sites, the answer
degrades in one characteristic direction: **evidence gets converted into
authority at exchange rates nobody set.** We call these conversions
*laundering*, and they have recognizable, recurring shapes:

- **Presence is not admissibility.** A receipt exists, therefore its claim
  is treated as usable.
- **Publication is not authorization.** The artifact was durably recorded
  (log appended, receipt published, ack returned), therefore the action is
  treated as permitted.
- **Agreement is not corroboration.** N monitors, replicas, or model
  samples agree — but share a deploy pipeline, a signature feed, or a base
  model, so the agreement was never independent testimony.
- **Provenance is not standing.** The artifact's supply chain is verified,
  therefore it is treated as qualified for *this* decision in *this*
  regime.
- **A fresh envelope is not fresh evidence.** The packet was minted
  recently; the observation inside it is old. Freshness gets read off the
  wrong timestamp.
- **Silence is not health.** No new alerts, therefore the incident is
  treated as resolved. Loss of observability *reduced* what could be known
  and got booked as good news.
- **An eval pass is not deployment competence.** A benchmark score is
  testimony from one harness under one regime; it gets spent as a general
  license.
- **Late success is not timely success.** The step completed after the
  deadline; the completion gets recorded and the miss disappears.

Each of these is an *admissibility* failure, not an authorization failure.
The authorization logic did what it was told. The failure happened one
layer earlier, at the unexamined step where something was allowed to
*count as a premise*.

## Why the existing categories don't cover it

The standard security stack has four well-named layers: **authentication**
(who is acting), **authorization** (whether they may act), **accounting /
audit** (what happened), and **attestation** (what evidence exists). The
question above belongs to none of them:

> Authorization reasons from premises. Admissibility governs whether those
> premises may count.

Policy engines (OPA, Cedar, XACML) evaluate rules over inputs; they do not
govern which inputs were eligible to arrive. Observability (OpenTelemetry
and its ecosystem) answers *what happened operationally* with great
precision, and nothing in it distinguishes "collected" from "may be relied
on." Supply-chain attestation (SLSA, in-toto, Sigstore) produces signed
provenance, but provenance is not standing — there is no structured place
to say "this attestation is qualified for this regime but not that one."
Timestamping (RFC 3161) proves existence at a time, which is routinely
spent as if it proved current validity.

The gap has a legal name older than software: *admissibility*, in the
Federal Rules of Evidence sense. Courts long ago separated "is this
testimony true?" from "may this testimony be used in this proceeding?" —
and built procedure for witnesses, standing, freshness, scope, and
challenge. Operational systems make the same class of decision constantly,
without the procedure and mostly without noticing the decision was made.

**The falsifier, stated up front.** This positioning is a choice about how
to slice the stack, not a natural kind. It would be deprecated by an
authorization system that handles the laundering moves above wholly inside
its authz layer without a separate admissibility step — genuinely, and not
by reifying all provenance into an enriched entity model, which makes the
admissibility layer instrumentally invisible rather than absent. The
closest existing neighbor (Cedar with its Lean/SMT analysis tooling) does
not currently do this; a system that did would falsify the need for a
distinct layer. A problem statement that cannot lose is a pitch.

## What OpenAdmissibility is

OpenAdmissibility (OA) is a proposed small, public ABI for making reliance
decisions explicit, portable, and refusable — in roughly the relationship
to reliance that OpenTelemetry has to telemetry:

> OpenTelemetry answers "what happened?" OpenAdmissibility answers "what
> may be relied on, by whom, under which profile, for which claim or
> effect — and what structured refusal follows if not?"

The pipeline it standardizes is deliberately short:

```text
observation → receipt → profile-local claim → decision → governed effect
                                                          or structured refusal
```

- **Observations are testimony, not facts.** A collector reports; a
  receipt records who reported what, when, about which subject.
- **Claims derive only through profile rules.** A *profile* is the local
  law: which witnesses may testify to which observation kinds, what
  freshness each claim requires, which claims each governed effect
  requires. There is no path from receipt to claim that skips a rule.
- **Decisions are a discriminated union, not a boolean.** A gate emits
  either a permit (carrying the derived claims it rests on) or a refusal
  carrying a typed *obstruction* — `MissingReceipt`, `CannotTestify`,
  `StaleWitness`, `ClaimNotEstablished`, `ProfileDigestMismatch`, and
  kin. Refusal is a first-class product, not an error state. Decision
  artifacts are forbidden to contain `ok`/`success` booleans.
- **The profile's digest is its authority identity.** A human-readable
  profile name is display metadata; a request that names its profile only
  by name is refused before evidence is considered.
- **Foreign decisions are testimony.** A permit from one profile's gate
  does not transfer to another's; it crosses only through an explicit
  bridge rule, under a cap that can narrow and never widen.

Two design commitments distinguish this from the ecosystems it resembles:

1. **The dock, not the law.** OA standardizes artifact shapes, digest
   identity, decision/refusal codes, trace attribution, and a conformance
   corpus format. It does *not* standardize a policy ontology, an identity
   system, effect execution, scheduling, or anyone's definition of
   authority. Profiles are local law; the ABI is the customs paperwork.
   Every prior system of this ambition died by swallowing its neighbors'
   ontologies; the non-goals list is load-bearing.
2. **Conformance is a corpus, not a certification.** The unit of agreement
   between implementations is a shared fixture set — concrete requests,
   evidence, profiles, and the exact decision artifact each must produce,
   including the refusals. An implementation conforms if it reproduces the
   corpus byte-for-byte at the decision surface. Doctrine that cannot be
   fixtured does not go in the spec.

## What it is not

Gravity wells, named so they can be refused:

- **Not a policy language.** Conditionals belong to profiles and
  elaborators; the kernel surface stays mean and underfed.
- **Not an observability replacement.** It sits beside monitoring and
  answers a strictly narrower question.
- **Not a compliance platform.** Adapters may emit compliance-shaped
  receipts; the ABI encodes no framework.
- **Not an agent runtime or orchestrator.** It rules on admissibility; it
  executes nothing. Adapters perform or refuse real effects after a
  permit.
- **Not a trust registry, PKI, or root oracle.** There is no global
  trusted party in the model — and deliberately no way to express one.
  Certifiers are admitted per claim class and scope; delegation does not
  compose without a rule; a watcher's act has no force outside the profile
  that admitted it.

## State of the evidence

This is a problem statement, not vaporware, and also not a product. What
currently exists, labeled honestly:

- **A specification skeleton** — thesis, scope, canonical JSON profile,
  core objects, artifact envelopes, obstruction codes, trace model,
  conformance format, and the OpenTelemetry relationship note, with draft
  JSON schemas and a first corpus (one permit specimen, ten refusal
  specimens).
- **A working reference gate** (prototype) — a Python reference checker
  and a Rust checker held in parity against a shared corpus (33 local +
  23 bridge-crossing cases), with typed obstruction ABIs for both local
  and bridge refusals, exercised behind local transport shims. Explicitly
  not production custody; its bridge signature verifier is a labeled
  placeholder.
- **Machine-checked specimen laws** — a set of small Lean 4 theorems
  pinning the semantics the checkers are supposed to have: claims derive
  only through admitting rules; missing / stale / cannot-testify / revoked
  evidence refuses; a profile name cannot substitute for its digest;
  transport acknowledgements support custody but never authority; bridge
  crossings narrow; eligibility never converts to spendable capacity;
  custody hops never refresh a producer clock; late success is not timely
  success. These are formalization-first candidates: they pin intended
  semantics and do not certify any implementation's compliance.

The honest gap list is short and known: the eligibility/capacity and
temporal-basis laws are newer than the corpus that should exercise them;
conformance by independent parties has not happened; and nothing here has
survived contact with a hostile implementer yet.

## What feedback is wanted

This document is rung 1 of a deliberate sequence — problem statement,
then artifact/refusal-ABI note, then corpus + reference checker, then a
multiple-implementation conformance story, and only then (if the evidence
supports it) any standards-body draft. Standardization is downstream
evidence of usefulness, not the birth canal.

The questions worth answering now:

1. Is the layer real *in your stack*? Name the site where a claim becomes
   permission implicitly — deploy gate, eval harness, incident closure,
   attestation consumer — and whether a typed refusal surface there would
   have caught a real incident.
2. Is the refusal vocabulary right-sized? The obstruction codes are meant
   to be the smallest set that covers the laundering shapes above; missing
   shapes and mergeable codes are both findings.
3. Does the dock/law split hold? If you cannot express your local rules as
   a profile without the core ABI growing, that is a design failure worth
   reporting early.

## Provenance

Compressed from `working/where-admissibility-fits.md` (2026-05-09
multi-model application map; "boundary object, not platform pitch"),
`working/admissibility-as-pre-authorization-layer.md` (the fifth-category
positioning and the Cedar falsifier), the OpenAdmissibility spec skeleton,
and the RRP admissibility-gate prototype. The formal substrate is the
admissibility-kernels line of the Lean repo (v9, "Dynamic Traces and
Profile Semantics") and the published Δt-framework preprint series (esp.
P22, P25, P27). The doctrine slogans scattered through this document —
*receipt presence is not admissibility*, *publication is not
authorization*, *agreement is not corroboration*, *freshness is admitted
elapsed time under a declared witness contract* — are each backed by a
named theorem or a named corpus fixture in those artifacts, which is the
point: the whitepaper makes no claim the machinery has not already been
made to refuse.
