# Prior-art spike plan — pattern discovery + triage

**Status:** Plan-shape note. Pinned 2026-05-26 by operator after the day's work surfaced the conservatism pattern: *"we've been WAY too conservative."* Not authorized for execution; the pin records the intent so when execution fires, the scope and triage discipline already exist.

**Posture:** Pin, not execute. The plan is the substrate.

---

## The aspiration

> **There's a metric shit ton of prior art we can use to (a) determine what we're missing AND (b) judge how it should be triaged.**

The day's work landed substantial framework (refusal-propagation + three-time/N-time decomposition + Byzantine extension + cross-kernel disposition + chain-adapter extraction). Each landing was paced by *forcing-case-gated* shipping discipline that other-claude correctly identified earlier as **the wrong gate for annex work**.

The corrected discipline (substrate-exists + bounded-cost + brakes-survive) authorized aggressive annex exploration. But the work has stayed *operator-driven* — patterns get filed when they surface in conversation, not when they exist in the broader prior-art literature. That's still conservative: we're sampling from "what the operator + ChatGPT + claude-web + DeepSeek surfaced this session" rather than "what the field has documented across decades."

The hypothesis: **prior art has answers we haven't asked**. Specifically, the existing framework intersects with many bodies of literature; each intersection is a potential gap or strengthening. A bounded scan would surface what's been considered before, what's been solved before, and what we're at risk of re-deriving badly.

## What this plan is NOT

- **Not boiling the ocean.** Bounded spike. Pick a slice, scan, triage, report.
- **Not authorization to file everything.** The triage framework IS the brake.
- **Not a replacement for formal discipline.** When prior art points at a Lean-relevant theorem, coherent statement, semantics, overlap, proof, and non-vacuity checks govern development; Phase D remains a separate public-promotion review.
- **Not an open scope for "find all the things."** Each scan slice has explicit start and stop conditions.
- **Not academic literature review.** Triage results are operational — bucket each find by what it does for the framework, not by citation completeness.

## The triage framework (five buckets)

When the spike fires and surfaces a prior-art pattern, sort it into exactly one bucket:

| Bucket | Meaning | Action |
|---|---|---|
| **A. Already covered** | Existing kernel, working note, or memory entry handles this pattern. | One-line cross-ref noting the prior-art match. No new filing. |
| **B. Adjacent to existing** | Incremental extension of existing substrate; bounded cost; brakes survive. | Annex working note or docstring update; possibly a small Lean fixture after intrinsic theorem/scope review. |
| **C. Genuinely new structural axis** | Doesn't fit any existing slot; would need its own working note or memory entry. | New working note with explicit non-claims and model/theorem, overlap, and non-vacuity gates. Possibly a new primitive candidate. |
| **D. Out of scope / reject** | Doesn't fit the discipline; explicit non-claim; the framework should NOT absorb this. | Brief rejection note (one sentence) recording WHY this is rejected — so future audits don't re-derive it. |
| **E. Forcing case for revisit** | Would force a Path C disposition revisit, a Public Phase D criterion change, or other doctrinal shift. | Open a separate audit; this is NOT just an annex-side filing. |

The triage discipline is the brake. Most finds should land in buckets A or B (covered or incrementally adjacent). Bucket C should be rare; bucket E should be very rare. Bucket D is healthy — explicit rejection is part of triage.

## Candidate prior-art bodies (seed list, not exhaustive)

Partial enumeration of bodies that intersect the framework. Each is a *candidate scan slice*; the spike picks one or a few per session.

### Distributed systems / coordination

- **Consensus protocols:** Paxos, Raft, PBFT, HotStuff, Tendermint. Already touched in DeepSeek's three-time analysis; deeper scan could surface specific quorum / view-change patterns relevant to phase-time Byzantine extension.
- **CAP / PACELC / fault-tolerance taxonomies:** Schneider's fault-tolerance taxonomy; CAP theorem and successors. Likely intersects with the cross-kernel disposition's "no jurisdiction merge" rule.
- **Failure detectors / eventual perfect:** Chandra-Toueg, Ω-failure-detector hierarchy. Relevant to liveness-under-partial-synchrony.
- **Causal consistency / vector clocks / version vectors:** Lamport timestamps, vector clocks, CRDTs. Intersects operator-time and the causality-preservation requirement.
- **Byzantine generals / oral messages / signed messages:** Lamport's original 1982 paper. Foundational for the Byzantine extension's adversarial models.

### Database / storage

- **ACID / isolation levels:** serializability, snapshot isolation, read committed. Likely intersects with metric-time and ingestion/durability time.
- **MVCC / versioning:** multiversion concurrency control. Intersects with version-time regime and the receipt-format attestation work.
- **Two-phase commit / three-phase commit:** classic distributed transactions. Intersects with phase-time and the BFT extension's commit protocols.
- **Saga pattern / compensating transactions:** long-running distributed workflows. Intersects with operator-time and the cross-kernel proposal/reconciliation cascade.

### Receipt-bearing protocols (already-deployed substrate)

- **TLS certificates + chain of trust:** X.509 PKI; certificate transparency (CT) logs; OCSP. Direct intersection with receipt-format BFT extensions.
- **Signed Certificate Timestamps (SCTs):** the CT log mechanism for proving "this certificate was logged at time T." Specific real-world analogue for metric-time Byzantine extension.
- **JWT / signed bearer tokens:** authority transfer via signed claims. Intersects with operator-time attestation.
- **DNSSEC / RPKI:** signed authority chains. Intersects with cross-kernel disposition's "no jurisdiction merge" — the chain of trust is exactly the structure that PROPAGATES authority while preserving role separation.
- **Macaroons:** capability tokens with attenuated authority. Possible model for Path C-aligned receipts.

### Real-time systems

- **Rate-monotonic / deadline-monotonic scheduling:** real-time-systems literature. Direct intersection with metric-time deadline enforcement.
- **Time-triggered architectures:** TTA, FlexRay. Phase-time + metric-time hybrid.
- **Lamport's "Time, Clocks, and the Ordering of Events":** the foundational paper. Already implicitly assumed; explicit scan might surface what the framework owes.

### Regulatory / compliance

- **GDPR / data sovereignty:** retention windows, right-to-be-forgotten, data residency. Direct intersection with retention-expiry regime.
- **Financial settlement (SWIFT, T+2, ISO 20022):** value-date enforcement, regulatory deadlines, audit trails. Direct intersection with legal-effective-time regime.
- **Healthcare data lifecycle (HIPAA, HL7):** patient-consent receipts, audit obligations, retention. Possible new substrate-domain consumer for the cascade pattern.
- **SOC 2 / NIST 800-53:** audit-evidence requirements. Intersects with the framework's "receipt as evidence" framing.

### Provenance / audit

- **W3C PROV:** standardized provenance ontology. Direct intersection with receipt-chain provenance.
- **SLSA (Supply-chain Levels for Software Artifacts):** signed build provenance. Possible model for the version-time Byzantine extension.
- **Notary / Sigstore / in-toto:** software supply-chain attestation. Direct real-world receipt-format substrate.

### Cryptographic substrate (for BFT plan)

- **Threshold signatures:** for distributed timestamping and quorum certificates.
- **Verifiable random functions (VRFs):** for unbiased leader selection in BFT contexts.
- **Verifiable delay functions (VDFs):** for time-bounded computation proofs.
- **Zero-knowledge proofs:** for receipts that attest properties without revealing underlying state.

### Logic / type theory (formal substrate)

- **Linear types / affine types:** resource discipline that maps onto receipt-consumption semantics.
- **Session types:** protocol-state verification. Direct intersection with phase-time and the cascade structure.
- **Modal logics of authorization:** Abadi et al., "A Calculus for Access Control in Distributed Systems." Direct intersection with the "no jurisdiction merge" rule.
- **Temporal logics (LTL, CTL):** for properties that involve time. Possible substrate for the formal layer if temporal cross-kernel composition is ever unbracketed.

### Cybernetic / control theory (corpus-native substrate)

- **Ashby, Wiener, Beer, Conant:** the corpus's existing substrate. Bounded scan to find anything the existing primitives don't capture.
- **Variety, requisite variety, model regulation:** Ashby's law applications to the receipt-gating discipline.
- **Hierarchical control / supervisory control:** ties to the cross-kernel disposition's "no jurisdiction merge."

## Output shape

When the spike fires, each session produces:

1. **A scope statement** — which slice of prior art was scanned this session (e.g., "consensus literature, sub-slice: HotStuff view-change discipline").
2. **A findings list** — patterns surfaced, each tagged with a triage bucket (A/B/C/D/E).
3. **A triage report** — one-line entry per finding, sorted by bucket:
   - Bucket A: "X pattern is already covered by Y existing artifact."
   - Bucket B: "X pattern incrementally extends Y; bounded annex update queued at Z."
   - Bucket C: "X pattern is structurally new; would need its own working note."
   - Bucket D: "X pattern explicitly rejected because Z."
   - Bucket E: "X pattern forces revisit of Y disposition; separate audit needed."
4. **Action items** — concrete next steps per finding (file note, update docstring, open audit, etc.).

Length per session: 1-3 pages of triage report. Bounded.

## Brakes

- **Do not** boil the ocean. Each session scans ONE slice, not all of them.
- **Do not** file everything. The triage framework is the brake — most finds should land in A (covered) or D (rejected). B (incremental) is fine; C (new structural axis) should be rare; E (forcing case for revisit) should be very rare.
- **Do not** treat prior-art as authority. The discipline is *what does this teach us about the framework*, not *what does the literature mandate*.
- **Do not** import vocabulary wholesale. The framework's vocabulary (refusal-propagation, three-time, Path C, etc.) has been earned by construction-discipline. Prior-art terms get translated, not adopted.
- **Do not** let the spike become an academic literature review. Each finding has an operational consequence (one of five buckets); if a finding doesn't fit a bucket, it's noise and gets discarded.
- **Do not** manufacture runtime demand. The spike is *discovery*; formal work may lead from a coherent result, while genuine consumer cases remain correspondence and priority evidence.
- **Do not** spawn new gates without naming them as gates. If a finding wants a new working-note category, name it explicitly as a category-creation move, not as a silent expansion.

## Forcing case for execution

The plan exists as a pin. Execution authorization conditions:

- **Operator says go.** Highest-bandwidth trigger.
- **A specific question surfaces** that prior art could answer (e.g., "is there a known protocol for cross-kernel non-equivocation with X property?").
- **A specific anomaly surfaces** in existing work that prior art might explain (e.g., a corner case in the cascade discipline that doesn't fit the current framework cleanly).
- **A specific consumer is about to ship** something that touches an under-considered area (e.g., NS about to implement BFT-grade attestation, and we want to scan BFT literature first).

No execution authorization without one of those triggers. The pin is the substrate; the trigger is the gate.

## Scope discipline per session

When a session fires:

- **Start condition:** one specific scan slice named (e.g., "GDPR + retention-expiry regime").
- **Duration cap:** one session, one report. No multi-session sprawl.
- **Stop conditions:** (a) the slice is scanned and triaged; (b) the slice opens into 3+ sub-slices, in which case stop and re-scope; (c) the scan starts wanting to spawn new working-note categories before any findings have landed, which is a sign of premature framework expansion.

After each session: stop, evaluate the triage report, decide whether to run another slice or hold.

## What gets earned by running this

The spike pays in three kinds of capital:

1. **Coverage.** What does the framework already handle? (Bucket A findings.) Confirms what's earned.
2. **Strengthening.** Incremental extensions that bounded annex work can absorb. (Bucket B.)
3. **Surprise.** Genuinely new structural axes the framework doesn't yet name. (Bucket C, rare.) Plus explicit rejections (D) that pre-empt re-derivation. Plus forcing-case openings (E, very rare) that would unblock Public Phase D or similar gates.

The healthy distribution: maybe 50% A, 30% B, 10% D, 8% C, 2% E. If the distribution skews heavily toward C or E, that's a signal the framework is under-developed in the scanned slice and the slice deserves a deeper pass. If the distribution skews heavily toward B with many small extensions, the framework is in healthy maintenance mode. If the distribution skews toward A and D, the framework is mature in the scanned slice and the spike is doing confirmation work.

## Relationship to existing work

This plan composes with the existing Phase C/D framework:

- **Construction-discipline gate** (substrate-exists + bounded-cost + brakes-survive) still applies. Prior-art findings don't bypass the gate; they inform what substrate exists and what counts as bounded.
- **Path C disposition** stays in force. Findings that would force its revisit go to bucket E and open their own audit.
- **Annex / Examples / Annex three-layer structure** in `RefusalPropagation.lean` is the substrate findings would extend if they land in bucket B.
- **The seven existing working notes** in `tooltheory/` (refusal-rebar-status, adapter-extraction-audit, cross-kernel-disposition, three-time-decomposition, byzantine-fault-tolerance-extension, nq-testimony-dependency-contract, nq-on-nq-forcing-case, nq-forcing-case-audit) plus this plan = the current annex substrate. Findings extend or contradict existing entries.

## Keepers

> **Prior art has answers we haven't asked.**

> **Triage discipline is the brake. Most finds should be covered or rejected.**

> **Bucket C (new structural axis) should be rare. Bucket E (forcing case for revisit) should be very rare.**

> **Each session: one slice, one report. Then stop.**

> **The plan is the pin. The trigger is the gate. Discovery is the spike. Triage is the discipline.**

## Cross-references

- All existing tooltheory working notes — findings extend or contradict.
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — the staged Phase A-D plan. Findings that touch Lean substrate route through Phase C/D gates.
- [[cross-kernel-disposition]] — Path C; bucket E findings might force a revisit.
- [[byzantine-fault-tolerance-extension]] — explicit forward-looking plan; prior-art on consensus/crypto/threshold-signatures intersects Phase 2-4 of the BFT plan.
- [[three-time-decomposition]] — explicit N-regime extension; prior-art on temporal logics, regulatory deadlines, real-time scheduling intersects.

## Provenance

- **2026-05-26 end of day.** Operator named the conservatism pattern: *"we've been WAY too conservative."* Surfaced the aspiration to use prior art as both discovery and triage substrate. Bounded scope explicit: *"I'm not trying to boil the ocean."*
- Filed by claude-code as a pin, not for immediate execution. The pin captures intent; execution gates remain.

## Disposition

Plan filed. No scan execution was authorized at filing. First execution is an operator-scoped research action with a specific slice named; that action-authorization rule is separate from permission to formalize any coherent result the scan later exposes. Triage framework ready. Brakes in place. The framework can absorb findings without overrunning intrinsic formal checks or public Phase D review.

> **Pinned. Not executed. The plan is the substrate.**
