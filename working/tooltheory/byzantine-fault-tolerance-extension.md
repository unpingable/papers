# Byzantine fault tolerance extension to the N-time decomposition

**Status:** Forward-looking plan. Sibling to `three-time-decomposition.md`. Filed 2026-05-26 after operator unparked the three-time decomposition and named the aspiration: *"I'm aiming for true fault tolerance with this stuff."*

**Posture:** Plan, not formal substrate. Not a Lean module. Not a public surface. Names what going Byzantine adds to the N-time framework, and what each layer would need to support BFT-grade receipt-gated coordination.

**Foundation:** the native three-time decomposition (operator-time / metric-time / phase-time) plus any extension regimes (legal, billing, version, sensor, durability, retention — see `three-time-decomposition.md` §"Generalization to N regimes"). Byzantine does not add axes; it adds an adversarial-model dimension *per axis*.

---

## Core observation

> **Going Byzantine does not restructure the N-time decomposition. It adds an adversarial-model dimension to each axis, with cryptographic and protocol-level mitigations.**

The three failure modes that single-time loses — stale-phase replay, causality violation, liveness failure — all have **Byzantine analogues** where the failures are adversarial rather than accidental. Same failure classes; defense surface shifts from operational to cryptographic.

## Per-axis adversarial models and defenses

### Operator-time, Byzantine

**Adversarial models:**
- Malicious operator signs conflicting commands under same correlation ID (equivocation).
- Replay attacks: old operator commands replayed by adversary to trigger duplicate actions.
- Authority forgery: adversary impersonates an authorized operator.
- Out-of-order injection: adversary injects commands that claim earlier operator-time positions than they actually have.

**Defenses:**
- Signed correlation IDs with non-equivocation proofs (each correlation ID has at most one signed command).
- Operator authority chains (signed delegation; revocation receipts).
- Replay-protection nonces tied to operator + epoch.
- Authenticated operator-time ordering: each command signs the prior command's receipt hash (Merkle / linked-receipt chain).

### Metric-time, Byzantine

**Adversarial models:**
- Adversarial nodes lie about wall-clock (claim a later time to bypass deadlines).
- Clock-skew attacks: adversary uses skew to invalidate honest receipts as "stale" or accept stale receipts as fresh.
- Future-dating: adversary issues receipts with future timestamps to grant artificial freshness.
- Adversarial freshness claims: "this receipt is fresh — trust me" without external attestation.

**Defenses:**
- Distributed timestamp protocols (e.g., Roughtime; threshold-signed timestamps from trusted clock cluster).
- Signed timestamps from threshold-trusted clock sources with quorum verification.
- Bounded-skew assumptions with explicit drift bounds; receipts outside the bound are rejected.
- Multi-source timestamp attestation (a receipt is fresh only if N-of-M independent clock sources agree).

### Phase-time, Byzantine

**Adversarial models:**
- View equivocation: a node claims to be in phase 4 to some peers and phase 5 to others.
- Double-voting: a node votes in multiple phases for conflicting values.
- Phase-identity forgery: adversary issues a receipt claiming a phase it was never authorized for.
- Phase-rollback: adversary tries to convince a peer the system is in an earlier phase than it actually is.

**Defenses:**
- Quorum certificates pinning phase identity (PBFT-style: a phase advance requires N - f signatures).
- Cryptographic phase attestation: each phase identity is a hash chain over prior quorum certificates.
- Non-equivocation proofs (e.g., HotStuff's three-chain rule; Tendermint's lock/unlock discipline).
- Monotonic phase counters that cannot decrease (signed by quorum at each advance).

### N-regime extension under Byzantine

Each *additional* regime named in the N-time generalization gets its own adversarial model:

- **Legal / effective time, Byzantine:** adversarial backdating of value dates; jurisdiction-shopping attacks. Defense: cryptographically-signed timestamps from regulator-trusted sources.
- **Billing-epoch time, Byzantine:** adversarial epoch-boundary manipulation; double-billing or no-billing attacks. Defense: signed epoch boundaries from billing authority with quorum-verified rollover.
- **Version / deployment time, Byzantine:** adversarial version impersonation; rollback-attack to vulnerable version. Defense: signed deployment manifests with monotonic version counters; quorum-verified version advancement.
- **Sensor / event time, Byzantine:** adversarial sensor data injection; Sybil attacks on sensor identity. Defense: hardware-attested sensor signatures; multi-sensor cross-validation.
- **Retention / expiry time, Byzantine:** adversarial retention extension (refusing to delete); pre-deletion data exfiltration. Defense: deletion-attestation receipts; multi-party retention enforcement.

The pattern generalizes: **for any time regime added to support a new stakeholder/lifecycle/compliance boundary, the Byzantine extension adds the cryptographic / quorum-based mechanism that prevents adversarial manipulation of that regime.**

## Target fault-tolerance properties

The plan aims at three FT capability levels, increasing in strength:

1. **Crash-fault tolerance (CFT):** the system continues to make correct receipt-gated decisions when up to *f* nodes crash or fail to respond. Native three-time decomposition with timeout-based liveness already provides this if receipts are signed and durable.
2. **Byzantine fault tolerance (BFT):** the system continues to make correct receipt-gated decisions when up to *f* nodes behave arbitrarily — including signing conflicting messages, lying about state, manipulating timestamps. Requires the per-axis defenses above.
3. **Liveness under partial synchrony:** under an eventually-synchronous network model (asynchronous initially, eventually bounded delay), the system eventually makes progress. Requires view-change discipline (phase-time advances under quorum even when previous phase stalls).

Stretch goal: **non-equivocation in cross-kernel contexts** — when a single physical actor (e.g., an NQ instance) emits both an NQ-side claim and a Wicket-side authorization based on it, Byzantine extension ensures the actor cannot equivocate (issue one claim to NQ consumers and a contradictory claim to Wicket consumers).

## Migration path

Plan in four phases. Each phase has its own gate; do not skip ahead.

### Phase 1 — Doctrine substrate (this note)

Document the Byzantine extension as forward-looking plan. Does not modify any runtime, receipt format, or Lean module. Names what each axis would need.

**Status:** complete with the filing of this note.

### Phase 2 — Receipt-format extensions (consumer-side, no Lean)

Add attestation fields to receipt formats in NQ / Wicket / NS — but only when a real consumer needs them. Per-axis attestation lives in receipt format, not in the formal kernel.

Specific extensions, gated by forcing case:

- **Operator-time:** add `signed_correlation_chain` field to receipts (the Merkle chain of prior operator commands).
- **Metric-time:** add `attested_timestamp` field with threshold signature from clock source.
- **Phase-time:** add `quorum_certificate` field with N-of-M signatures binding the phase identity.
- **Per-extension regime:** add corresponding attestation field (legal, billing, version, sensor, retention).

**Status:** not yet authorized. Forcing case: an active soundness incident where current receipt format leaks an adversarial attack surface.

### Phase 3 — Consumer-policy extensions (consumer-side, no Lean)

Each consumer (NQ, Wicket, NS, agent_gov) extends its receipt-verification policy to check the attestation fields from Phase 2. Verification is consumer-side; the kernel layer doesn't model verification.

**Status:** depends on Phase 2.

### Phase 4 — Optional Lean formalization (forcing-case-gated)

If a specific soundness theorem requires reasoning about adversarial state production (not just static state assignment), the formal Lean layer extends to model Byzantine adversarial state. This would force the **Path C disposition revisit** per the pre-commitment in `cross-kernel-disposition.md`:

> *If the cross-kernel adapter requires expressing affirmative cross-kernel semantics during Lean construction, Path C is incorrect and the disposition must be revisited rather than the brake being relaxed.*

Byzantine adversarial state is exactly the case where the formal layer needs to reason about *who signed what* (cryptographic provenance), not just *what state holds* (refusal propagation). The current Path C disposition explicitly brackets this; opening it would be a substantive expansion of the Lean kernel's scope.

**Status:** not authorized. Forcing case: a specific Byzantine-soundness theorem that the operational layer (Phases 2-3) cannot prove without formal substrate. Likely candidates:
- A regulatory requirement for formal verification of receipt-attestation chains.
- A specific cross-kernel theorem where adversarial equivocation across kernels can't be ruled out by receipt-format alone.
- A safety property where the current `CascadeSound` obligation must extend to include adversarial state production.

## Brakes

The Byzantine extension must respect existing brakes plus new ones specific to BFT:

- **Do not** collapse the three native time axes (or any extension regimes) into a single "Byzantine clock." Each axis retains its independence; Byzantine adds adversarial defense to each.
- **Do not** introduce Byzantine adversarial models into the formal Lean layer without a Phase 4 forcing case.
- **Do not** assume an honest majority beyond the protocol's explicit quorum size. BFT means quorums must include enough non-Byzantine nodes to outvote adversaries; the framework does not assume the population is mostly honest.
- **Do not** collapse crash + Byzantine into one fault class. CFT and BFT are different disciplines with different quorum requirements (typically `f+1` for CFT, `2f+1` or `3f+1` for BFT depending on the model).
- **Do not** treat cryptographic primitives as a substitute for the framework. Signatures and quorum certificates are *mechanisms*; the framework is *what to attest*. Confusing the two grows the "cryptographic cathedral" anti-pattern.
- **Do not** promote the Byzantine extension to a public Lean surface until Phase 4 fires.

## Failure modes to refuse during plan execution

- The Byzantine extension starts wanting a "Byzantine time algebra" that fuses all axes → kill.
- The plan starts wanting blockchain / consensus primitives baked into the formal layer → kill.
- The receipt format starts carrying full transaction histories rather than attestation summaries → kill.
- The consumer policy starts requiring globally-consistent state across all kernels → kill (that's the "Unified Theory of Nope" again, just with crypto).
- The plan starts wanting threshold-trust assumptions that exceed the protocol's explicit quorum size → kill.

## Keepers

> **Byzantine does not restructure the N-time decomposition. It adds an adversarial-model dimension per axis, with cryptographic mitigations.**

> **Same three failure classes; defense surface shifts from operational to cryptographic.**

> **For each time regime added to support a stakeholder/lifecycle/compliance boundary, the Byzantine extension adds the cryptographic mechanism that prevents adversarial manipulation of that regime.**

> **CFT and BFT are different disciplines; do not collapse them.**

> **Signatures are mechanisms; the framework is what to attest. Confusing the two grows the cryptographic cathedral.**

## Relationship to existing Lean substrate

The current Lean layer (`RefusalPropagation` + its three sub-layers Law / Examples / Annex) operates on *static state assignments* with no temporal or adversarial dimension. Byzantine extension does NOT change this *yet*. Specifically:

- `CascadeSound`'s directionality (refusal propagates, admission doesn't) is the structural brake against jurisdiction merge. It remains the kernel-level discipline regardless of whether the surrounding system is CFT or BFT.
- `Composition.refusal_composes_two_hop` and `refusal_propagates_transitively` operate over a generic `requiredFor` relation that doesn't model who signed what. These remain valid under BFT — they reason about *if the dependency chain holds*, not *whether the chain can be forged*.
- Forgery prevention lives in receipt format (Phase 2) and consumer policy (Phase 3), not in the kernel theorems.

The kernel theorems are *signature-agnostic*: they hold for any pair `(Entity, DependsOn)` regardless of how the `DependsOn` relation was established. Whether that relation came from honest cooperation or from cryptographically-verified Byzantine quorum, the cascade still propagates refusal. The formal layer doesn't need to know the provenance.

This is the *clean separation* the framework offers: the law is signature-agnostic; the substrate provenance is consumer-side.

## Cross-references

- [[three-time-decomposition]] — native three-time decomposition + N-regime generalization. This Byzantine note is its forward-looking adversarial-model sibling.
- [[cross-kernel-disposition]] — Path C; brackets temporal cross-kernel composition out of the formal Lean layer. Phase 4 of this plan is the trigger that would force a Path C revisit.
- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — current static-state formal kernel; signature-agnostic per the discussion above.
- `~/git/lean/LeanProofs/Admissibility/Freshness.lean` — metric-time axis in the kernel; Byzantine extension would add timestamp-attestation defenses at the consumer layer, not in this module.
- `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` — phase-time axis in the kernel; Byzantine extension would add quorum-certificate defenses at the consumer layer.
- `~/git/nq/`, `~/git/agent_gov/`, `~/git/nightshift/` — consumer-side codebases where Phase 2/3 receipt-format and consumer-policy extensions would land.

## Provenance

- **2026-05-26.** Operator stated true-fault-tolerance ambition while unparking the three-time decomposition. Also surfaced the N-regime extension ("consider more than 3 time regimes"), validated by DeepSeek's analysis of legal-effective time, billing epochs, version/deployment time, sensor event time, durability time, retention expiry.
- Filed as sibling note (option B per the operator's chosen filing scope) to keep the BFT adversarial-model layer separate from the structural N-time decomposition. Three is native; N is structural extension; Byzantine is adversarial extension. Three distinct concerns; three distinct notes.

## Disposition

Forward-looking plan. No immediate action authorized. Specifically:

- Phase 1: complete (this note).
- Phase 2: deferred. Forcing case = real soundness incident exposing adversarial attack surface in current receipt format.
- Phase 3: deferred (depends on Phase 2).
- Phase 4: deferred. Forcing case = Byzantine-soundness theorem unprovable at consumer layer.

Closing the plan: when all four phases land, the framework would support **true fault tolerance** in receipt-gated cross-kernel coordination — receipt provenance is cryptographically attested per time regime, consumer policy verifies attestations, and the formal Lean layer optionally proves soundness against adversarial state production. Until then, the plan is the substrate.

> **The plan is the substrate. The signature is the mechanism. The kernel is signature-agnostic. The discipline is the keeper.**
