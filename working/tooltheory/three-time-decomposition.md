# Three-time decomposition — operator-time / metric-time / phase-time

**Status:** Working note. Filed 2026-05-26 via operator unpark after NS Claude surfaced the decomposition while surveying the Lean repo and DeepSeek produced three independent production-grade examples that validate the framework. Originally parked as "annex thinking, file as memory candidate only if sticky after sleep" — the operator overrode that and unparked it for filing now.

**Posture:** Doctrine note. Not a primitive (no containment audit yet); not a kernel module. Names a recurring structural decomposition that resolves what *kind* of time a system is reasoning about at any given site.

---

## Core observation

Receipt-gated coordination systems need to track three distinct time dimensions, not one. Collapsing them into a single notion of time loses real safety properties.

The three:

| Dimension | What it tracks | Where it lives |
|---|---|---|
| **Operator-time** | The sequence of events as intended/observed by an external orchestrator or human operator. *"Who asked for what, and in what order."* | NS disposition enum; ack obligation; correlation IDs; client-side causal ordering |
| **Metric-time** | Physical, real-world wall-clock time. Used for timeouts, deadlines, SLAs, leader leases, latencies. | NQ freshness gates; Lean `Freshness.lean` (metric-time admissibility axis); deadline-driven aborts |
| **Phase-time** | A logical clock that progresses through discrete, named stages or protocol phases. State-machine step, generation number, ballot number, view ID. | Lean `ConsolidationDenial.lean` (settlement intervals); Paxos terms; consensus view changes; protocol stage gates |

## Why a single time dimension fails

DeepSeek's analysis (2026-05-26) names three concrete failure modes:

1. **Stale-phase receipts.** A receipt from an earlier protocol phase arrives late after the system has advanced. Without phase-time, the late receipt is misinterpreted as a current-phase signal — a replay hazard that violates safety.
2. **Causality violation.** A client submits commands A, then B (where B depends on A's outcome). Physical arrival order may scramble these. Without operator-time, B can be executed before A's receipt is generated.
3. **Liveness failure.** Without metric-time, no real-world deadline drives abort/retry. Indefinite blocking on receipts that will never arrive.

Each dimension prevents a different failure class. Collapsing them removes the structural distinction.

## Concrete examples (production-grade)

DeepSeek surfaced three independent examples where all three dimensions are tracked simultaneously:

### 1. Multi-phase infrastructure rollout with hard deadline

Three-phase rolling update (drain / deploy / re-enable) gated by receipts at each phase, with a maintenance window deadline.

- **Phase-time** distinguishes which stage receipts belong to. A "drain complete" receipt is only a valid gate-release if `receipt.phase == current_phase`. Otherwise it's a stale straggler from an aborted previous attempt.
- **Metric-time** enforces the wall-clock deadline. Each phase has a real-time timeout; the maintenance window has an absolute end.
- **Operator-time** tracks the orchestrator's command ordering. Update-A receipts must not unlock gates intended for Update-B.

Real-world analogues: Kubernetes operators (Flagger + time-bound change tickets); AWS Step Functions with idempotency tokens (operator-time lineage) + timeout-catches (metric-time) + state-machine phases (phase-time).

### 2. Paxos/Raft consensus

Replicated log with external command ordering and leader leases.

- **Phase-time** (ballot/term/view ID): a leader's messages are only valid in a specific term. If a partition heals and old "command committed" receipts from term 4 arrive after the cluster has moved to term 5, phase-time discards them.
- **Metric-time**: leader leases give the leader certainty for a wall-clock interval to serve reads without a round trip. Client-side timeouts drive retry-or-failover.
- **Operator-time**: client correlation IDs ensure that a chain of commands (A → B where B depends on A's outcome) executes in the client's intended order, even when consensus reordering would otherwise permit different physical interleaving.

### 3. BFT cross-organizational asset transfer (inter-bank settlement)

Three-phase BFT protocol (propose / pre-commit / commit) for inter-bank transfers.

- **Phase-time** (view + sub-phase): a "pre-commit" receipt is only valid within its view and sequence number. View changes invalidate all previous phase-time receipts.
- **Metric-time**: phase deadlines trigger view-change timeouts; without them, the protocol stalls.
- **Operator-time**: business-transaction IDs preserve operator-intended ordering. Transfer B (conditional on A's settlement) cannot lift its commit gate until A's committed receipt is linked, regardless of consensus phase overlap.

## Mapping to existing local sites

The three-time decomposition is not just a DeepSeek-named framework — it's already implicitly running across the corpus's existing tools:

| Dimension | Existing site |
|---|---|
| **Operator-time** | `~/git/nightshift/` NS disposition enum, ack-obligation discipline ("who asked for what, in what order"); correlation across operator command sequences |
| **Metric-time** | `~/git/lean/LeanProofs/Admissibility/Freshness.lean` — metric-time admissibility axis explicitly named ("did this happen before that" vs "is this timestamp within an acceptable window"); NQ freshness gates; Slice B `imported_producer_basis_stale` |
| **Phase-time** | `~/git/lean/LeanProofs/Admissibility/Annex/ConsolidationDenial.lean` — separates phase-time ("has any settlement interval occurred at all?") from metric-time ("is this timestamp in the window?"); NS settlement-interval discipline; protocol-stage gates |

The decomposition gives each existing site a coordinate in a three-axis space rather than being separate concerns that happen to look similar.

## Generalization to N regimes

Three is the **native** decomposition. Production systems often require more. Per DeepSeek's 2026-05-26 follow-on analysis, real-world receipt-gated workflows can need four, five, or six independent time axes — one per distinct stakeholder, lifecycle, or compliance boundary.

### Additional regimes that surface in real systems

| Regime | What it tracks | Example |
|---|---|---|
| **Legal / effective time** | The date a transfer or contract is deemed to occur, independent of message exchange | Securities value date (T+2): settlement may message-complete today but legally effect Thursday |
| **Billing-epoch time** | Accounting periods that don't align with wall-clock; monthly/quarterly cycles | Cloud serverless function spanning month boundary — receipts must be split across two billing events, not gated as one |
| **Version / deployment time** | Which code version was active when the receipt was generated | Canary rollout: receipt from version V₁ must not be confused with receipt from V₂ even if metric-time and phase-time match |
| **Sensor / event time** | The physical moment a sensor detected something; may differ from metric-time due to skew/delay | IoT telemetry: event_time vs ingestion_time vs decision_time are three distinct clocks |
| **Ingestion / durability time** | When data becomes durably stored and visible to other components | Decision based on durable state must use durability-time, not metric-time |
| **Retention / expiry time** | Future deadline by which data must be irrevocably deleted | GDPR / data sovereignty: a decision-action receipt cannot be released using data past retention expiry |

### Concrete examples (DeepSeek-validated)

- **Financial clearing (4 regimes):** operator + metric + phase + **value date**. A settlement receipt cannot unlock the funds gate solely on metric/phase — value date is independent and binding.
- **Multi-tenant SaaS (5 regimes):** operator-per-tenant + metric + phase + **billing epoch** + **version**. Billing requires epoch boundaries; canary rollouts require version boundaries. Conflating either causes incorrect attribution.
- **Edge IoT with data sovereignty (6 regimes):** operator + metric + phase + **sensor event time** + **ingestion/durability time** + **retention expiry**. Each axis prevents a distinct failure: stale-data decisions, undurable-state decisions, retention violations.

### The general pattern

> **A receipt-gated workflow needs as many independent time axes as there are distinct stakeholders, lifecycles, and compliance boundaries.**

Each axis can advance independently; each must be validated at gating points. Production systems typically attach multiple timestamps (or logical counters) per receipt and check all relevant ones before unlocking action.

The native three are foundational because they map onto the *structural roles* in any coordination protocol: *who asked* (operator), *the physical clock* (metric), *which logical step* (phase). Additional regimes surface when external constraints (legal, fiscal, regulatory, physical) impose their own independent clocks that no internal coordinate can collapse into.

### Native three vs N-regime extension

| Question | Native three | N-regime extension |
|---|---|---|
| Why does this exist | Structural roles in any coordination | External constraints from stakeholders / compliance / physics |
| Always required? | Yes, in any non-trivial receipt-gated system | Conditional: only when the external constraint applies |
| Where it lives | Operator-time → consumer policy; metric → receipt freshness; phase → cascade structure | Per axis: legal time in regulatory metadata; billing in accounting layer; version in deploy manifest; sensor/ingestion/retention in data lifecycle |
| Discipline | The three are non-collapsible by construction | Each additional regime must justify its own non-collapsibility |

**Keeper:** *Three is native. N is extension.* Both follow the same discipline: separate axes because collapsing them loses safety properties.

## Byzantine extension

See sibling note: [`byzantine-fault-tolerance-extension.md`](byzantine-fault-tolerance-extension.md). The Byzantine extension does not add axes — it adds an *adversarial-model dimension* per axis, with cryptographic mitigations. Filed as a forward-looking plan toward true fault tolerance.

## Relationship to Path C (cross-kernel disposition)

`working/tooltheory/cross-kernel-disposition.md` filed 2026-05-26 brackets **temporal cross-kernel composition** out of Path C explicitly:

> *Path C scoped to live refusal propagation under static state. The Lean adapter operates on a state assignment `Entity → State` evaluated at a single snapshot; there is no temporal dimension in the formal model.*

And:

> *Where the temporal load lives:* receipt format absorbs Δt-aware metadata (freshness horizons, expiry semantics, basis-validity windows); consumer policy absorbs semantic decisions ("expired but historically valid" vs "expired and basis-invalidated"); the formal layer stays small, static, provable.

The three-time decomposition **operationalizes** that bracketing. Specifically:

- **Operator-time** lives in *consumer policy* (Path C's "consumer-policy absorbs semantic decisions").
- **Metric-time** lives in *receipt format* (Path C's "freshness horizons, expiry semantics, basis-validity windows").
- **Phase-time** lives partly in *receipt format* (which phase produced this receipt?) and partly in the *formal kernel layer* (Lean's `ConsolidationDenial` already encodes phase-time refusal as cascade structure).

So three-time is not a contradiction of Path C — it's a sharpening of Path C's "where the temporal load lives." Path C says *the temporal load doesn't live in the formal cross-kernel layer*; three-time says *it splits across operator/metric/phase, with each dimension having a distinct home in the larger system*.

## What this means for the Lean side

The three-time decomposition does NOT force a Lean change. Specifically:

- The formal kernel stays at phase-time (`ConsolidationDenial`) and metric-time (`Freshness`), each in its own module. The decomposition explains *why* these are separate axes rather than redundant time concerns.
- Operator-time stays in consumer-side tooling (NS / NQ / Wicket). It does NOT migrate into the formal layer.
- If the decomposition becomes load-bearing for a future Lean theorem (e.g., a cross-time cascade that needs to distinguish phase-from-metric for a soundness proof), that would force the Path C disposition revisit per the pre-commitment. Until then: useful framing, not formal substrate.

## Brakes

- **Do not** collapse three-time into a single time dimension in any formal model. The separation is what gives the structure its safety properties.
- **Do not** promote three-time to a Lean kernel axis without a forcing case. The three axes already exist implicitly in `Freshness` (metric) and `ConsolidationDenial` (phase); operator-time stays consumer-side.
- **Do not** treat three-time as a *unified theory of time* — it's a decomposition that explains why three distinct concerns recur, not a meta-framework that supersedes them.
- **Do not** add metadata to refusal cascades for time-tagging. That would be the temporal cross-kernel composition Path C explicitly refuses.

## Keepers

> **Operator-time is who asked. Metric-time is the clock. Phase-time is which step we're on.**

> **Collapsing the three loses real safety properties: stale-phase replay, causality violation, liveness failure.**

> **Each dimension has a distinct home: operator-time in consumer policy; metric-time in receipt format; phase-time in cascade structure.**

> **Three-time sharpens Path C's "where the temporal load lives." It does not contradict it.**

## Cross-references

- `~/git/papers/working/tooltheory/cross-kernel-disposition.md` — Path C; three-time operationalizes "where the temporal load lives" section.
- `~/git/lean/LeanProofs/Admissibility/Freshness.lean` — metric-time admissibility axis (canonical Lean site for metric-time).
- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — `Annex.ConsolidationDenial`-adjacent work via Nightshift fixture; the original `ConsolidationDenial.lean` (canonical Lean site for phase-time) lives in the kernel proper.
- `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` — phase-time refusal kernel: *fluency does not witness settlement*; *has any settlement interval occurred at all*.
- `~/git/nightshift/docs/DESIGN.md` and `~/git/nightshift/docs/GAP-nq-nightshift-contract.md` — NS disposition enum and ack-obligation work (canonical operator-time site).
- `[[consolidation-denial]]` (working note) — the original consolidation-denial tool doctrine; phase-time framing implicit there.
- `[[refusal-kernel-to-refusal-receipt-seam]]` — the layer split memo; three-time refines the temporal axis of that seam.

## Provenance

- **2026-05-26 morning** — NS Claude survey of the Lean repo flagged ConsolidationDenial as the phase-time site adjacent to NS's silence-aware-posture work, surfaced the three-time decomposition (operator-time / metric-time / phase-time) as worth-considering, and parked it as "annex thinking, not surface; file as memory candidate only if sticky after sleep."
- **2026-05-26 same day** — operator overrode the park: *"three-time unparked by operator, kicking the door down. fucking do it."*
- **2026-05-26 same day** — DeepSeek produced three production-grade examples (Kubernetes rolling update with maintenance window; Paxos/Raft consensus with leases; BFT inter-bank settlement) demonstrating that all three dimensions must be tracked together in real systems. Each example named distinct failure modes that single-time approaches incur.
- Filed by claude-code, 2026-05-26.

## Disposition

Working note, not promoted to primitive. Promotion gate: at least one forcing case where a Lean theorem or NS/NQ runtime would be measurably wrong without the three-axis decomposition explicit. Until then: doctrine substrate for understanding why `Freshness` and `ConsolidationDenial` are distinct kernels rather than redundant time concerns, and why operator-time lives consumer-side rather than kernel-side.

> **The decomposition explains the corpus's existing temporal structure. It does not propose new structure.**
