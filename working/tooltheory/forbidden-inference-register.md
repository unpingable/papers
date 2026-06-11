# Forbidden-inference register

**Status:** Durable matrix. First spike-session output under `prior-art-spike-plan.md`. Filed 2026-05-26. Keyed by **forbidden inference** (the reasoning error each substrate mechanism exists to prevent), not by protocol name.

**Doctrine header:**

> **Formalize only where a substrate blocks a distinct forbidden inference your current corpus does not already block.**

The register is the anti-slop engine. New rows must name a specific forbidden inference, cite a substrate specimen that blocks it, identify existing-primitive overlap, declare residue (or lack thereof), and pin a triage bucket per the spike plan's framework (A/B/C/D/E).

---

## The register

| # | Forbidden inference | Substrate specimen | Existing primitive overlap | Residue | Triage bucket | Lean status |
|---|---|---|---|---|---|---|
| 1 | *Past witness authorizes present mutation* — "I saw version v, so I may write now" | HTTP `If-Match`, etcd Txn (compare-version), ZooKeeper expected-version updates, object-store generation-match | witness + action + freshness + transition authority | Commit-point precondition: identity of prior state, not time-distance from it | **C** (new structural axis) | Annex refusal kernel sketch: `VersionBoundAction` |
| 2 | *Absence proves nonexistence* — "no answer means none exists" | DNSSEC authenticated denial (NSEC / NSEC3 with bounded denial TTL per RFC 9077) | silence + freshness + authority + witness | Proof-carrying denial: positive negative witness under scoped authority | **C** | Annex refusal kernel sketch: `AuthenticatedDenial` |
| 3 | *Origin authority implies forwarding authority* — "valid origin, therefore valid propagation" | BGP route-leak controls (RFC 9234 OTC), RPKI ROAs (RFC 6811) | authority + standing + transition authority | Propagation-scope as composition theorem; only first-class axis if it surfaces across multiple substrates | **C** (theorem-schema first) | Annex refusal kernel sketch: `FencedEpochAuthority` (subsumes propagation under scope-fenced authority) |
| 4 | *Held authority once means holds authority now* — "I had it, so I still have it" | Lease expiry, ZooKeeper ephemeral nodes, Raft / Paxos terms, Spanner leader-lease disjointness, fencing tokens | transition authority + freshness | Epoch-bounded transition authority: stale holders must be fenced even when they retain artifacts and messages are delayed | **C** | Annex refusal kernel sketch: `FencedEpochAuthority` |
| 5 | *Retry same payload means same operation* — "if it looks identical, it's the same action" / *Timeout means no effect* — "no acknowledgement, therefore safe to redo" | Idempotency keys (AWS / Stripe-style), QUIC 0-RTT retry, RFC 9110 idempotent methods | action + receipt + freshness + refusal composition | Operation identity as first-class, distinct from request text / delivery / receipt | **C** | Annex refusal kernel sketch: `ReplaySafeActionIdentity` (optional fourth) |
| 6 | *Inclusion in a log proves history integrity* — "logged, therefore custody" | Certificate Transparency (CT), Merkle tree consistency proofs, Sigstore, in-toto, Git | witness + provenance | Public auditable append-only shape, NOT custody, NOT authority | **B** (annex witness, not kernel) | `DivergenceProof` / `ConsistencyProof` as annex witness types only |
| 7 | *Reachability implies legitimacy* — "the route is up, so it's authorized" | BGP path validation, DNS glue / referral, anycast / CDN edge | authority + scope | Reachability-authority split: routes exist, glue resolves, but neither confers content authority | **B** (already covered by authority + scope, but worth glossary handle) | Glossary handle / working note |
| 8 | *Valid signature or chain means current authority* — "verified, therefore live" | X.509 path validation, OCSP, CRL, OCSP must-staple, ACME challenges | authority + freshness | Live-status as freshness-governed revocation; theorem over existing modules | **A** (covered by authority + freshness) | Theorem over existing modules; no new kernel |
| 9 | *Transport ACK means semantic receipt* — "TCP ACK'd, so the app received it" | TCP/HTTP/QUIC delivery acks vs application-level commit | receipt | Semantic receipt boundary: protocol layer ≠ application layer | **D** (anti-confusion glossary) | Permanent glossary entry; explicitly NOT a primitive |
| 10 | *Available read is current* — "the replica answered, so the answer is authoritative" | Linearizable vs serializable reads (etcd), follower reads under partition, CAP/PACELC | time decomposition + authority | Coordinated admissibility under partition: quorum intersection theorem over standing sets | **E** (possible Public Phase D criterion shift, but unlikely soon) | Working note; possible calculus 2.0 candidate only if global authority under partial visibility becomes load-bearing |
| 11 | *Timestamp order is exact order* — "T₁ < T₂, therefore E₁ before E₂* | Lamport / vector clocks; Spanner TrueTime intervals with commit-wait; NTS-secured time sync | time decomposition (three-time / N-time) | Interval time + causal partial order; already captured under existing time-decomposition extensions | **A** (covered by three-time + N-time) | No new primitive; possible refinement to `Freshness.lean` for interval semantics |
| 12 | *Cached negative or stale data is durable* — "TTL still valid, so still true" | DNS negative caching, HTTP `stale-while-revalidate`, `stale-if-error` | freshness + silence | Bounded reliance under policy; refinement of freshness with explicit window + allowed-stale policy | **B** (incremental Freshness extension) | Theorem-level support in `Freshness.lean`; not a new kernel |
| 13 | *Admit everything; retries are harmless* — "the system can absorb this" | TCP congestion control, HTTP 429 / Retry-After, circuit breakers, load shedding | refusal composition + time decomposition | Operational refusal for system preservation; failure-mode map material | **B** (failure-mode map entry) | Working note; possibly `Refusal.until t reason overload` schema |
| 14 | *First-observed binding is globally authoritative* — "TOFU = trust" | SSH first-key, SSHFP via DNSSEC | witness + standing + contestability | Provisional local standing, explicitly weaker than certified authority | **D** (glossary handle; explicit weakness) | Permanent glossary entry; NOT a primitive |
| 15 | *Convergence implies correctness* — "the replicas agreed, so they're right" | CRDTs, eventual consistency, Dynamo divergence + reconciliation | consolidation denial + refusal composition | Reconciliation under non-total order; project-specific unless concurrent-claim merging becomes a forcing case | **A** (covered) or **B** (annex extension) depending on consumer | Working note |
| 16 | *Intervention authorizes causal credit* — "I applied mitigation I, therefore I caused / prevented / fixed / own / deserve credit (or blame) for outcome O" | Incident postmortems, SRE mitigation narratives, policy announcements, dashboard SLIs | `LogOnlyProvesEmission.causalityOf`; [[dashboard-quiet-is-not-recovery]]; [[../causality-control-plane]] | None — actor-self-attribution alias of `causalityOf`; sequence/intervention is not causation | **A** (covered) — alias/tripwire, no new kernel | Covered by `LogOnlyProvesEmission.causalityOf`; no new module |

**Entry 16 is an alias, not a target** — and is *not* part of the internet-substrate spike below (different provenance, added later). Filed because *"I applied the mitigation, therefore I prevented the outage"* is common enough to deserve a named tripwire, but it points *backward* into the three existing kernels in its overlap column; it does not spawn a "Causal Claim Admissibility" package. Provenance: 2026-06-10 multi-model session (Daoist / Warring-States framing → *"receipt type gates claim grammar"* extraction). The kernel-overlap audit found the extraction was already `LogOnlyProvesEmission.causalityOf` + `dashboard-quiet-is-not-recovery` + `causality-control-plane` — fresh vocabulary made an existing kernel look like a new surface. Keeper from that detour, kept on the wall not in the register: *generative re-derivation is not discovery — if the new frame compiles to an existing forbidden inference, it is an index entry, not progress.* (The graded `BridgeStatus` evidence ladder from the same session is parked in `parked-leads.md` as linter-UX vocabulary only, not admissibility substrate.)

---

## Bucket distribution

Of the 15 spike entries (entry 16 is a later alias, excluded from this distribution):

- **Bucket A (already covered):** 4 entries (8, 11, 15 partially, plus implicit "already covered" entries not enumerated)
- **Bucket B (adjacent extension):** 4 entries (6, 7, 12, 13)
- **Bucket C (new structural axis):** 4 entries (1, 2, 3, 4, 5 — three or four kernel candidates)
- **Bucket D (out of scope / rejected):** 2 entries (9, 14)
- **Bucket E (forcing-case revisit):** 1 entry (10, conditional)

That's roughly 27% A / 27% B / 27% C / 13% D / 6% E. **The C count is high** because this is the first systematic prior-art pass — many genuinely-new structural axes surface at once. Subsequent spike sessions in other slices (consensus literature, regulatory frameworks, real-time systems) should produce a more A/B-heavy distribution as the framework matures.

If subsequent sessions keep producing high C counts: signal that the framework was substantially under-developed in the surveyed slices. If they keep producing high A/D counts: signal that the framework is mature and the spike is doing confirmation work.

## Triage actions

Per bucket:

- **C candidates → annex sketch pack** (filed separately as `annex-sketch-pack.md`).
- **B entries → adjacent extensions queued** (most route into Freshness / refusal-composition refinements; cumulatively bounded).
- **A entries → cross-ref in existing artifacts** (no new filing; docstring updates where load-bearing).
- **D entries → permanent glossary handles** (filed under explicit-rejection discipline; prevents re-derivation).
- **E entries → opened audit if forced** (only entry 10 currently qualifies; not opened today).

## Doctrine keepers

> **Internet protocols repeatedly rediscovered refusal kernels because distributed systems punish forbidden inferences.**

> **Formalize only where a substrate blocks a distinct forbidden inference your current corpus does not already block.**

> **The register catalogues forbidden inferences. The kernels block them. The glossary contains the dead ends.**

## Three load-bearing distinctions surfaced this session

These are not new primitives. They are *sharpenings* the register makes explicit:

1. **Freshness governs reuse. Version governs mutation.** Time-distance from observation is not state-identity at commit. Conflating them launders forbidden inference #1.
2. **Authority is not conserved across propagation.** Origin authorization is not export authorization. Forbidden inference #3.
3. **The mirror is admissible only as evidence; never as verdict.** (Re-stating the existing NQ-on-NQ keeper.) A log proves shape; it does not appoint a custodian. Forbidden inference #6.

## Cross-references

- [[prior-art-spike-plan]] — parent plan; this register is the first spike-session output.
- [[internet-substrate-failure-map]] — sibling artifact; failure-mode routing for the same substrate.
- [[annex-sketch-pack]] — sibling artifact; the three (or four) C-bucket refusal-kernel sketches.
- [[three-time-decomposition]] — captures forbidden inference #11 already (timestamp order ≠ causal order).
- [[byzantine-fault-tolerance-extension]] — adversarial extension of the three-time framework; intersects multiple register entries.
- [[cross-kernel-disposition]] — Path C bracketing; forbidden inference #10 is the closest possible Public Phase D revisit trigger.
- [[refusal-kernel-to-refusal-receipt-seam]] — register entries 6, 9, 14 are anti-laundering specimens of the same family the seam note governs.

## Provenance

- **2026-05-26.** Operator authorized prior-art spike with internet substrate as the first slice. ChatGPT performed survey + reduction passes; DeepSeek did sanity-check / external-reader reaction; operator routed all three back for triage. Three distilled artifacts (this register, failure map, sketch pack) capture the spike-session output.
- DeepSeek's three questions on the spike output specifically validated the triage choices:
  - *Version separate from freshness?* → Yes; freshness governs reuse, version governs mutation. Two axes, not one.
  - *Propagation scope as new axis or theorem?* → Composition theorem first; first-class axis only after multiple-substrate evidence.
  - *Merkle for NQ-side forcing case?* → Annex witness only; never a kernel primitive. The brake: *Merkle proves shape. It does not appoint a custodian.*

> **The register is the durable artifact. The kernels are the probes. The map is the routing layer.**
