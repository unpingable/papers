# NQ-on-NQ — Candidate forcing case for refusal composition

**Status:** Candidate forcing-case note. Filed 2026-05-26 after the C.4/C.5 Lean work pulled `refusal_composes_two_hop` into existence and a parallel observation surfaced: NQ is not only a witness system; NQ is also witnessable substrate. Not a promoted forcing case yet — needs at least one concrete NQ-on-NQ fixture to convert from candidate to active.

**Posture:** Forcing-case scoping memo. No Lean module written. No `CalculusOne.lean` change. No promotion to 2.0. No `NQFleetDependency` adapter yet — the note is the gate that decides whether the adapter is worth building.

**Sibling forcing-case candidates:** `labelwatch-driftwatch-admissibility.md` (first candidate). NQ-on-NQ is the second. Two candidates is not a corpus; it is the minimum density at which a generic law starts to look load-bearing rather than decorative.

---

## Core sentence

> **NQ is itself witnessable substrate; NQ-on-NQ is the internal forcing case for refusal composition.**

The shape that flips: every external-consumer audit asks *who else needs the contract?* and the answer is always plausible-but-hypothetical. NQ-on-NQ is structurally different — NQ already has substrate properties (ingest freshness, WAL state, writer pressure, retention behavior, schema/state migration health, receipt production, preflight availability, testimony-dependency cascade health) that themselves admit refusal verdicts. The system that emits substrate-health claims itself has substrate-health claims.

That is recursion with consequences. The contract pressure is internal, not imported.

## Local case

One NQ instance observes / refuses its own substrate-health claims:

- `nq.self.ingest_state` — is this NQ instance currently ingesting from its declared sources?
- `nq.self.wal_health` — is the WAL writable, replayable, bounded?
- `nq.self.preflight_available` — can preflight queries land?
- `nq.self.receipt_production` — is `From<PreflightResult> for Receipt` operating?
- `nq.self.testimony_dependency_cascade` — is the suppression cascade firing as `TESTIMONY_DEPENDENCY V1.0+V1.1+V1.2` requires?

Local NQ-on-NQ is useful as honest internal observability. It is **not** sufficient for trust at the fleet layer — a single NQ instance certifying itself is exactly the self-reference loop the doctrine refuses.

Local NQ-on-NQ refusal must propagate. If `nq.self.ingest_state = cannot_testify`, every claim downstream that requires fresh ingest must inherit the refusal. The cascade is the same shape as `device_enumeration_witness → smart_witness → disk_state`, applied recursively within the system itself.

## Aggregate case

Multiple NQ instances cross-adjudicate each other's substrate health:

- `nq_b.about(nq_a).receipt_health` — instance B asserts something about instance A's receipt-producing capacity.
- `nq_c.about(nq_a).preflight_health` — instance C asserts something about A's preflight surface.
- Fleet-level rollups depend on cross-testimony (B about A, C about A, etc.), not on A about itself.

Aggregate NQ-on-NQ is what the cascade theorem can carry: if `nq_a.self.receipt_health = cannot_testify`, then any `nq_b.about(nq_a).fleet_claim` that depends on A's receipt must inherit the refusal, and any fleet-level claim depending on B's claim about A must inherit it again.

## Lean connection

This maps directly onto the existing `RefusalPropagation.Composition` machinery:

| Abstract | NQ-on-NQ |
|---|---|
| `witnesses A B` | A's substrate state supports B's downstream testimony |
| `requiredFor B C` | B's testimony is required as basis for C's claim |
| `BasisInheriting` | Cross-instance suppression cascade |
| `refusal_composes` | One-hop fleet refusal propagation |
| `refusal_composes_two_hop` | A → B's-claim-about-A → fleet-rollup-about-B's-claim |

The aggregate case is precisely the shape `refusal_composes_two_hop` was pulled into existence to express. The chain:

```
nq_a cannot testify to its own receipt-producing health
  ↓ (requiredFor)
nq_b's claim about nq_a depends on nq_a's testimony
  ↓ (requiredFor)
fleet-level claim depends on nq_b's claim about nq_a
  ↓
fleet-level claim cannot bind from that chain
```

is exactly the two-hop pattern. Two declared dependency edges, one cascade, one refusal-composition law.

## Anti-goal

> **No self-certifying closure.** NQ cannot certify its own standing merely by emitting a receipt about itself. Local self-observation is observable, not authoritative. The mirror is admissible only as evidence; never as verdict.

Keeper:

> **Recursive testimony is admissible only when recursion preserves refusal; otherwise it is self-certification with better logging.**

Concretely:
- `nq.self.X = observable` is NOT sufficient to authorize `nq.self.X` for binding use elsewhere.
- Trust must come from cross-testimony, independent vantage, or declared dependency that *can* refuse — not from "NQ said NQ is fine."
- The cascade is the discipline that prevents the loop: if any substrate-input to NQ-A's self-claim is `cannot_testify`, the self-claim must refuse, regardless of how cleanly the self-claim was emitted.
- A passing self-claim is admissible as observation, advisory, or input to cross-adjudication. It is not admissible as fleet authority for itself.

## Candidate first fixture

A boring, concrete shape that would convert this note from candidate to active forcing case:

```
instance A: nq_a.self.ingest_state = cannot_testify
            (e.g., declared source unreachable; WAL not advancing)
declared:   nq_b.about(nq_a).receipt_health requires nq_a.self.ingest_state
declared:   fleet.aggregate.health requires nq_b.about(nq_a).receipt_health
expected:   fleet.aggregate.health = cannot_testify (cascade-inherited)
forbidden:  fleet.aggregate.health = observable    (self-certification breach)
```

This is a single integration test or a single live scenario. If NQ ships this fixture and the cascade fires correctly, the forcing case is active. If NQ ships this fixture and the cascade does NOT fire (fleet aggregate reports `observable` despite the underlying refusal), there is a real soundness gap to fix.

Either outcome is load-bearing information. The fixture is the gate.

## Promotion posture

**Current:** candidate forcing case. Phase D criterion 3 stays at **B** (potential consumer identified, forcing case pending) per `nq-forcing-case-audit.md`.

**Conditional upgrade trigger:** ONE concrete NQ-on-NQ fixture (the candidate above or an equivalent) lands in NQ as an integration test or a real scenario. At that point, criterion 3 may upgrade to **"candidate active forcing case"** — still not Phase D promotion authorization, but a real consumer-side anchor.

**Not in scope for this note:**
- Writing `NQFleetDependency.lean` (a second concrete adapter mirroring `NQDependency`).
- Generalizing `RefusalPropagation` to a transitive closure or `Path` type.
- Three-hop or higher composition lemmas.
- A fleet-aggregation kernel separate from the existing refusal-composition machinery.
- Letting `refusal_composes_two_hop` accumulate a crown.

**In scope for follow-up (deferred until fixture exists):**
- If/when the candidate fixture lands, a second tiny adapter (`NQFleetDependency`, ≤30 lines, mirroring `NQDependency`'s pattern) becomes worth writing — to show that *two* concrete cases instantiate the same generic two-hop law.
- That second adapter, *if it also goes clean through `refusal_composes_two_hop`*, is the point at which "composition support is real" stops being one bespoke instance and becomes a repeated-load pattern.

## What this changes about Phase C/D

Before this note:
- C.3/C.4/C.5 demonstrated that `refusal_composes` and `refusal_composes_two_hop` reproduce NQDependency's cascade contract.
- That made the abstract law load-bearing for *one* concrete case.

After this note:
- A second concrete case is named and structurally distinct (aggregate cross-instance vs. single-instance dependency).
- The abstract law is now a candidate carrier for *two* concrete cases, one of which (NQ-on-NQ) is recursive — i.e., the carrier law must refuse self-certification while permitting cross-testimony.

The Phase D gate still has all five criteria. This note moves criterion 3 framing closer to active without crossing the line:

| Phase D criterion | After NQ-on-NQ note |
|---|---|
| 1. Composition between kernels | Unchanged. The composition is within the refusal-kernel family, not yet between distinct kernels. |
| 2. New abstraction count | Unchanged. `refusal_composes_two_hop` already exists; no new abstractions named. |
| 3. Second forcing case exists | Upgraded framing: **two candidate cases (labelwatch + NQ-on-NQ)**, neither active yet. Still B until one ships a fixture. |
| 4. Slogan-blast-radius | Unchanged. Keepers stay honest. |
| 5. PL/UC stay as working notes | Unchanged. |

## Brakes (explicit)

- **Do not** build `NQFleetDependency.lean` yet. No Lean writes in response to this note.
- **Do not** generalize `refusal_composes_two_hop` to three-hop, four-hop, or transitive closure. The two-hop law was earned by one concrete instance; multi-hop or transitive forms need their own forcing case.
- **Do not** introduce a `Path` type, claim graph, scope algebra, time index, or use-kind table. The user's standing brake list applies.
- **Do not** let local NQ-on-NQ become fleet-trust by sleight of hand. Local self-observation is observable; never authoritative for itself.
- **Do not** treat this note as an unblocking authorization for Phase D. It is a candidate, not a verdict.

## Keepers

> **NQ is not only a witness system. NQ is also witnessable substrate.**

> **Recursive testimony is admissible only when recursion preserves refusal; otherwise it is self-certification with better logging.**

> **The mirror is admissible only as evidence; never as verdict.**

> **A candidate forcing case is upgraded by a fixture, not by a memo.**

## Cross-references

- [[nq-testimony-dependency-contract.md]] — the contract receipt for the C.3/C.4/C.5 Lean spike that established `refusal_composes` + `refusal_composes_two_hop` as load-bearing for NQDependency.
- [[nq-forcing-case-audit.md]] — the predecessor classification (B: plausible consumer, missing instantiation). NQ-on-NQ is a sibling candidate, not a replacement.
- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — `Composition` namespace (refusal_composes, refusal_composes_two_hop) and `NQDependency` adapter (the first concrete case).
- [[labelwatch-driftwatch-admissibility.md]] — first candidate forcing case (external consumer). NQ-on-NQ is the second; the pair is the minimum density at which the abstract law starts looking carried rather than decorative.
- [[refusal-kernel-to-refusal-receipt-seam.md]] — runtime-vs-formal-layer split; NQ-on-NQ lives on the seam.
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Phase C/D versioning plan. This note moves criterion 3 framing without opening Phase D.
- `~/git/nq/docs/ROADMAP_EXPECTATIONS_FROM_LEAN_KERNEL.md` — NQ's roadmap memo. The NQ-on-NQ pattern is consistent with NQ's headline ("more exact, not more powerful") — making recursive testimony less self-certifying is precisely the precision-pressure direction.
- `~/git/nq/docs/WITNESS_PACKET.md` §60 — declared-dependency discipline applies recursively when NQ is itself the witnessed substrate.

## Provenance

- **2026-05-26** — relay observation following the C.5 result that two proofs of the disk-state refusal (bespoke + generic) coexist in `RefusalPropagation.Annex.NQDependency`. The follow-on insight: NQ is itself witnessable substrate, so the consumer for `refusal_composes`/`refusal_composes_two_hop` is not only external (labelwatch, Nightshift, future SRE goblin) but also internal (NQ-A's substrate-health admissible to NQ-B; fleet-aggregate admissible only when both cross-testimony links preserve refusal).
- The pair-with-labelwatch reframing is what makes this less hypothetical: two candidate forcing cases of distinct shape (external-consumer vs. recursive-self-observation) is materially harder to dismiss than one.
- Filed by claude-code, 2026-05-26, after operator brought the relay observation forward with the explicit instruction *"write the forcing-case note first, then stop."*

> **NQ-on-NQ is the forcing case only if it makes recursive testimony less self-certifying, not more.**
