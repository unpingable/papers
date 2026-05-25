# Signed Is Not Witnessed

**Subtitle:** Receipt kinds and admissible claim boundaries for witnessed systems
**Date:** 2026-05-25
**Status:** Specification note (not a roadmap, not a protocol proposal)
**Scope:** Cross-corpus receipt vocabulary
**Non-goals:** Protocol design, ATProto-specific proposal, archival system design, new admissibility kernel
**Related:** Agent Governor admissibility gates; NQ witness packets; Wicket receipts; Labelwatch custody/audit surfaces; [`civic_migration_appliance.md`](civic_migration_appliance.md); [`atproto_provenance_instrument.md`](atproto_provenance_instrument.md); Signal Authority candidate primitive (working notes)

## Position

This note does not introduce a new admissibility kernel.

It names receipt kinds and schema requirements that make existing admissibility distinctions operationally legible at the artifact boundary.

The recurring failure is that signed artifacts are treated as if they automatically prove observation, custody, availability, or downstream claim authority. They do not. A signature preserves integrity and authorship. Everything else — being seen, being preserved, being globally available, supporting a downstream claim — is a separate transition that requires a separate receipt.

## Related / Existing Substrate

This note applies existing admissibility doctrine to receipt-bearing systems. The substrate is already in place; what is missing is the receipt-level vocabulary that prevents cryptographic integrity from being laundered into observation, custody, or claim authority across systems that share no kernel.

Existing distinctions consolidated here:

- **Basis is not standing.** From the Admissibility kernel's `Authority.lean` discipline: basis (evidence kind) and standing (authorization to bind) are separately derived; both are required for an authorized verdict.
- **Preservation is not admissibility.** From `SurfaceAuthorization.lean` and the Calculus 1.0 slogan: refusal across the surface, freshness, witness, and authority axes is structural — preservation alone does not satisfy any of them.
- **Recovery is not live observation.** From `Freshness.lean`, `RecoveryMargin.lean`, and `PublicReceiptRefinement.lean`: recovery doctrine is bounded; recovered state cannot launder into freshness or witness claims.
- **Evidence crossing a boundary does not carry authority across that boundary.** From [`civic_migration_appliance.md`](civic_migration_appliance.md): the receivership pattern keeps evidence portable and authority local.
- **Silence is not negative evidence unless protocol coverage makes it admissible.** From the Signal Authority candidate primitive: missing ACK ≠ NACK; timeout ≠ verdict; silence ≠ revocation unless the protocol says so.
- **Witness invariance does not require witness completeness.** From `WitnessInvariance.lean`: stability under perturbation is proved; declared non-coverage is not. This note adds the latter as a receipt-schema obligation.

What is new here is not those distinctions in isolation. The contribution is their consolidation into:

- Four named receipt kinds.
- Required coverage and non-coverage declarations on observation receipts.
- A forbidden-transitions table for receipt-to-claim composition.

## Receipt Kinds

### 1. Source receipt

> Actor A authored, committed, emitted, or signed statement S.

Supports claims about authorship, integrity, origin, and commitment. Does *not* support claims about observation, preservation, availability, or downstream admissibility.

Minimum fields: `kind`, `subject`, `author`, `signed_at`, `signature`.

### 2. Observation receipt

> Witness W observed subject S at time T under declared coverage C.

The first receipt kind that can honestly support *"was seen."* The claim is local to that witness under that coverage. It does *not* support global availability, universal visibility, or absence of contrary observations.

Required fields: `kind`, `subject`, `witness`, `observed_at`, `source`, `coverage`, `gaps`, `cannot_testify`, `signature`. See *Required Observation Receipt Fields* below for the substantive obligation.

### 3. Custody receipt

> Custodian C preserved, reconstructed, or transferred artifact S through chain K.

Supports claims about preservation, reconstruction, and archival handling. Does *not* support live-observation claims. The forbidden collapse is *"we reconstructed it later"* becoming *"we saw it then."*

Minimum fields: `kind`, `subject`, `custodian`, `custody_event`, `generated_at`, `chain`, `cannot_testify`, `signature`.

### 4. Claim receipt

> Claim Q is admissible given evidence E, standing S, scope C, freshness F, and consequence boundary B.

Records that a downstream assertion has passed an admissibility check. Does not merely preserve an observation; it records the verdict at the admissibility boundary.

Minimum fields: `kind`, `claim`, `subject`, `basis` (one or more lower-kind receipt digests), `standing`, `scope`, `freshness`, `verdict`, `cannot_support`, `signature`.

## Required Observation Receipt Fields

An observation receipt **MUST** declare:

- `subject` — what was observed (content digest, event ID, state digest)
- `witness` — the observing identity
- `observed_at` — time of observation, with timezone
- `source` — vantage point (relay cursor, sensor ID, log offset)
- `coverage` — declared mode and scope of observation
- `gaps` — known interruptions or unobserved intervals within coverage
- `cannot_testify` — explicit non-coverage: classes of claims this observation cannot support

An observation receipt **SHOULD** declare:

- stream continuity state (live, replayed, reconstructed)
- replay or reconstruction status if not strictly live
- drop or backpressure state
- negative-evidence eligibility (does this coverage make absence claims admissible?)
- freshness or expiry semantics for the observation itself

The substantive requirement:

> A witness that cannot say what it cannot testify to **MUST NOT** be treated as an admissible witness for claims outside its declared coverage.

This is the receipt-schema discipline. A witness that emits only positive observations without gap semantics or non-coverage declarations invites laundering: consumers will treat *"no receipt"* as *"no event,"* even where the witness had no standing to make that negative claim.

`cannot_testify` is not decorative. It is part of the receipt's admissibility boundary.

## Forbidden Transitions

| From                  | To                            | Status                                                           | Reason                              |
| --------------------- | ----------------------------- | ---------------------------------------------------------------- | ----------------------------------- |
| Source receipt        | Observation claim             | DENY unless supported by an observation receipt                  | Authorship is not observation       |
| Observation receipt   | Global availability claim     | DENY unless coverage supports global scope                       | Local witness is not global witness |
| Custody receipt       | Live observation claim        | DENY unless live observation was separately receipted            | Reconstruction is not observation   |
| Receipt absence       | Negative claim                | DENY unless coverage makes silence admissible (Signal Authority) | Missing receipt is not absence      |
| Valid signature       | Standing                      | DENY unless signer has standing for the claim                    | Integrity is not authority          |
| Preserved artifact    | Claim authority               | DENY unless an admissibility layer grants it                     | Custody is not claim authority      |

The table is the spec's bite: future systems may implement these forbidden transitions, or violate them. Either case becomes legible at the receipt boundary.

## Examples

### Event stream

A signed event from a source actor is a source receipt. A relay or consumer that observed the event may emit an observation receipt. An archive that later reconstructs the event from stored state emits a custody receipt. A moderation, audit, or governance system that says *"this event was available to X at T"* requires a claim receipt or equivalent admissibility decision. Four distinct statements; four distinct artifacts.

### Sensor network / ADS-B

A decoded message is not enough. A receiver may emit an observation receipt declaring vantage R at time T with coverage details. A database export emits a custody receipt. A downstream claim *"aircraft A was present in region R at T"* must account for receiver coverage, timestamp quality, spoofing risk, sensor gaps, and claim consequence — a claim receipt with explicit basis and scope, not the raw sensor record.

### Agentic control surface

A model-generated command proposal is source-like evidence. A runtime witness may observe the command, environment, or result (observation receipt). Execution logs preserve custody. A Governor/Wicket-style admissibility decision determines whether the action or the downstream claim is authorized (claim receipt). Treating any signed blob in that chain as authorization is the canonical laundering failure.

## Keepers

Restatements of existing kernel discipline applied to receipt typology:

- Signed is not witnessed.
- Witnessed is not preserved.
- Preserved is not admissible.
- Admissible is not authorized beyond scope.
- Reconstruction is not observation.
- Availability is not receipt.
- Signature is not standing.
- Custody is not claim authority.

The receipt-typology-novel keeper:

> A witness that cannot say what it cannot testify to should not be trusted as a witness.

The cross-substrate keeper:

> Cryptography can make a statement durable. It cannot decide what the statement is allowed to mean.

## Closing

Cryptographic systems are good at preserving statement integrity. They are bad at preserving semantic restraint unless the restraint is explicitly modeled at the receipt schema.

A signature can tell us that a statement survived tampering. It cannot tell us what the statement is allowed to prove. The receipt-kind vocabulary, the required non-coverage declarations, and the forbidden-transitions table are the smallest adapter that lets existing admissibility doctrine constrain receipt-bearing systems without recapitulating the kernel.

The contribution is not new doctrine. It is the layer at which doctrine becomes operationally legible at the artifact boundary.
