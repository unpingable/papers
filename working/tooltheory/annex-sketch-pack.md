# Annex sketch pack — four refusal-kernel candidates

**Status:** Third of three spike outputs (sibling to `forbidden-inference-register.md` + `internet-substrate-failure-map.md`). Filed 2026-05-26 under `prior-art-spike-plan.md` as the C-bucket residue from the first internet-substrate spike session.

**Posture:** Sketches, not Lean modules. Each sketch carries: exact technical guarantee, precise forbidden inference, kill test against existing primitives, minimal Lean API, refusal-kernel statement, one pressure example, and brakes. **No Lean was built in this dated pass.** A sketch may become a bounded formal probe before any runtime consumer exists once its model, discriminating theorem, overlap, and proof controls are clear; public promotion remains separate.

**Doctrine header:**

> **Formalize only where a substrate blocks a distinct forbidden inference your current corpus does not already block.**

Each sketch survives reduction against existing primitives. Each names what makes it NOT collapse into freshness, authority, witness, or receipt. If the survival argument fails during future Lean construction, the disposition revisits — per the standing pre-commitment.

---

## Organizing insight — four flavors of identity

The spike did not just produce *more examples* of refusal kernels. It produced **identity refinements**: four distinct flavors of identity that internet protocols repeatedly carve out as separate from witness, freshness, authority, and receipt.

| Identity flavor | Question it answers | Substrate witnesses |
|---|---|---|
| **Version identity** | *Am I acting on the same state I observed?* | HTTP `If-Match`, etcd `Txn`, ZooKeeper expected-version, object-store generation-match |
| **Denial identity** | *Is this negative claim the same as authoritative absence?* | DNSSEC NSEC / NSEC3, RFC 9077, negative-cache TTL |
| **Scope identity** | *Is this authority still valid after crossing a boundary?* | BGP OTC (RFC 9234), RPKI origin vs path, DNS delegation, lease expiry |
| **Operation identity** | *Is this retry the same action or a new side effect?* | AWS / Stripe idempotency keys, QUIC 0-RTT replay protection, HTTP retry hazard |

The four flavors are not arbitrary; they correspond exactly to the four C-bucket sketches below. The organizing insight: **each is a way that two artifacts with similar surface shape must be refused as non-equivalent at admissibility time.**

**Anti-universal-solvent brake.** "Identity" is strong enough as an organizing concept that it can start eating adjacent concepts. The discipline:

> **Identity refinements are admitted only when two artifacts with similar surface shape must be refused as non-equivalent.**

Concretely, the four admitted refinements share that exact shape:

- *same witness surface, different version* → `VersionBoundAction`
- *same negative surface, different denial standing* → `AuthenticatedDenial`
- *same authority surface, different propagation scope* → `FencedEpochAuthority`
- *same payload surface, different operation identity* → `ReplaySafeActionIdentity`

Future "identity" candidates must pass the same test: name the two surface-similar artifacts and the non-equivalence the refusal kernel enforces. Without that, "identity" decays into universal solvent and the discipline collapses. The corpus-internal name for the failure mode: *ontology ranch dressing* — pours over anything, distinguishes nothing.

### Constructive contribution (structural note)

This spike is the first one in the corpus to name a **positive family** of refusal-shaped abstractions rather than refusal-shaped *failure modes*. The corpus has been good at naming what goes wrong — teleological laundering, managed insufficiency, observability inversion, curdling pipeline, prosecutorial decomposition. Those are pathologies.

The four-identity carve is structurally different: it names what *correctly-shaped distinctions look like* — patterns that have been doing the right work in production systems for decades, made legible as a family. The substrate already exists; the spike's contribution is **legibility**, not invention. Which means the failure mode "you made this up" doesn't apply — the patterns are CAS / If-Match / NSEC / OTC / idempotency keys, all of which predate the carve by years to decades.

That makes constructive contribution easier to defend than critique: pointing at *solved problems that hadn't been recognized as a family* is harder to dismiss than pointing at problems.

---

## 1. VersionBoundAction

**Forbidden inference:**

> **"I once observed version `v`, therefore I may write now."**

Past witness does not authorize present mutation. Time-distance from observation is not state-identity at commit.

**Substrate witnesses:**

- HTTP `If-Match` / `If-Unmodified-Since` with ETag validators (RFC 9110); server returns `412 Precondition Failed` on mismatch.
- etcd `Txn` with `Compare(modRevision)` — transaction aborts if observed revision is not current.
- ZooKeeper `setData` with expected-version — atomic mismatch refusal.
- Object-store generation-match (Cloud Storage, S3 conditional writes).

**Kill test:**

Looks initially like `witness + action + freshness + transition authority`. Residue survives because the refusal is keyed on **identity of prior state at commit**, not time-distance from observation. A stale witness can match by luck (no one else mutated); a fresh witness can be invalidated immediately by another actor. Time is not the discriminator; commit-point version is.

Per DeepSeek's Q&A and ratified: **freshness governs reuse; version governs mutation.** Two axes.

**Minimal Lean API (sketch — not built):**

```lean
namespace Admissibility.VersionBoundAction

-- Abstract version type; consumer instantiates (etcd ModRevision, ETag string, etc.)
variable (Version : Type) [DecidableEq Version]

-- A versioned state: current state has a version.
structure VersionedState (σ : Type) where
  state : σ
  version : Version

-- An action carries the version it was predicated on.
structure VersionBoundAction (σ : Type) where
  effect : σ → σ
  observedVersion : Version

-- Commit-point predicate: action's observed version matches current.
def PreconditionHolds {σ} (a : VersionBoundAction σ) (current : VersionedState σ) : Prop :=
  a.observedVersion = current.version

-- Refusal kernel: action is inadmissible if precondition fails.
theorem versionMismatch_blocks
    {σ} (a : VersionBoundAction σ) (current : VersionedState σ)
    (h : ¬ PreconditionHolds a current) :
    ¬ Admissible a current := sorry

end Admissibility.VersionBoundAction
```

**Refusal kernel (informal):** *If the observed version no longer matches the current version at commit, the action is inadmissible regardless of freshness, authority, or receipt status.*

**Forcing case (NQ-adjacent):**

An ops agent reads an incident finding as `unacknowledged` (version v₁), prepares an escalation, and submits. Between read and submit, another actor acknowledged the finding (version v₂). The agent's escalation must be **refused** at commit, not silently overwrite. The version-bound check is what makes the refusal admissible — freshness alone would not catch the race.

**Brakes:**

- Do NOT fold `Version` into `Freshness` or `TimeDecomposition`. Two distinct axes.
- Do NOT generalize to "any state-mismatch refusal." This kernel is about *commit-point exact-state precondition*, not state-similarity heuristics.
- Do NOT smuggle multi-party preconditions (CAS over multiple objects) into this
  single-object kernel. A separate transactional-CAS model may be formalized when it
  has a precise, non-redundant theorem and controls; it may lead its runtime case.

---

## 2. AuthenticatedDenial

**Forbidden inference:**

> **"No positive answer arrived, so nonexistence is established."**

Absence is not denial unless an authority can testify negatively.

**Substrate witnesses:**

- DNSSEC NSEC / NSEC3 records (RFC 4033, RFC 5155) — signed proof that a name or RRset is absent in a signed zone.
- RFC 9077 — denial TTL must not outlive its intended validity.
- Negative-cache TTL (RFC 2308) — bounded reliance on cached nonexistence.

**Kill test:**

Looks initially like `silence + freshness + authority + witness`. Residue survives because **silence is not denial** — silence is absence of information; signed denial is positive testimony under scoped authority. A timeout, SERVFAIL, or unsigned NXDOMAIN are not admissible as proof of nonexistence; an NSEC chain signed by the zone's authoritative key is.

Sharpens the existing `Silence` doctrine: silence is one thing; signed nonexistence is another.

**Minimal Lean API (sketch — not built):**

```lean
namespace Admissibility.AuthenticatedDenial

variable (Zone : Type) (Query : Type)

-- A denial witness: the zone's authority testifies that q is absent,
-- bounded by a freshness window.
structure DenialWitness where
  zone : Zone
  query : Query
  proof : ZoneAuthoritySignedAbsence zone query  -- consumer instantiates
  validUntil : Time

-- A finding is "absent (admissibly)" only with a denial witness.
def AdmissiblyAbsent (q : Query) (z : Zone) (now : Time) : Prop :=
  ∃ w : DenialWitness, w.zone = z ∧ w.query = q ∧ now ≤ w.validUntil

-- Refusal kernel: silence / timeout / unsigned-NXDOMAIN does NOT imply absence.
theorem silence_is_not_denial
    (q : Query) (z : Zone) (now : Time)
    (h_no_witness : ¬ ∃ w : DenialWitness, w.zone = z ∧ w.query = q ∧ now ≤ w.validUntil) :
    ¬ AdmissiblyAbsent q z now := sorry

end Admissibility.AuthenticatedDenial
```

**Refusal kernel (informal):** *A claim of nonexistence is admissible only when accompanied by an authority-signed denial witness within its validity window. Timeout, server error, or unsigned negative response do not constitute admissible absence.*

**Forcing case (NQ-adjacent):**

NQ-side claim: *"There is no `cannot_testify` record for ingest-stale at host H."* The agent must distinguish three cases:
- (a) Signed NSEC-equivalent denial from the NQ authority — admissibly absent.
- (b) Query timeout, query failure, or partial response — **not** admissibly absent; the calculus must treat this as `cannot_testify` about the absence-claim itself.
- (c) Cached negative response within negative-cache TTL — admissibly absent for the cached interval, but only for reuse, not for present-tense binding action.

**Brakes:**

- Do NOT collapse "silence" into "denial." That's the whole point.
- Do NOT silently generalize DNSSEC's *scoped namespace* authority model to social or
  institutional denials. A separate model may proceed when it states their different
  authority structure and a discriminating theorem or countermodel; it need not wait
  for a runtime forcing case.
- Do NOT extend the validity window past authority freshness. RFC 9077's discipline (denial TTL ≤ signed window) is load-bearing.

---

## 3. FencedEpochAuthority

**Forbidden inference:**

> **"I held authority once, therefore I still hold authority now."** (Epoch side.)
>
> **"Valid origin authorization implies valid propagation authorization."** (Scope side.)

The sketch initially treats the two as a *combined kernel* — the two surfaces share structural shape: **authority is not conserved across time or across boundaries.** Old leases must be fenced; export rights are not origin rights.

**Caveat (per ChatGPT spike review):** propagation scope and epoch fencing **overlap but are not identical**. Two distinct axes that share a refusal shape:

- **Propagation scope** — authority may not survive **boundary crossing**. (Example: BGP OTC; DNS delegation; cross-kernel receipt consumption.)
- **Epoch fencing** — authority may not survive **generation change / lease turnover**. (Example: Raft term advance; ZooKeeper session expiry; Spanner leader-lease rotation.)

Both block *"same-looking authority artifact still authorizes action"*, but the **axis** differs: one is a *spatial* boundary (crossing a kernel / namespace / network frontier), the other is a *temporal* one (the holding's generation has advanced). The combined-kernel framing survives only while a precise composition theorem needs both axes. If a theorem, countermodel, or instantiation needs one without the other, the sketch **splits** into separate kernels. Composition theorem first, axis-promotion lazy, separation-pressure honored when it appears.

**Substrate witnesses (lease side):**

- ZooKeeper ephemeral nodes + session leases.
- Raft / Paxos terms + view-changes; stale leaders must be fenced.
- Spanner leader-lease disjointness — exactly one leader holds the lease at any wall-clock moment.
- Fencing tokens (Lamport / Martin Kleppmann style) — monotonic IDs that invalidate stale holders.

**Substrate witnesses (scope side):**

- BGP route-leak controls (RFC 9234, "Only To Customer" / OTC).
- RPKI origin-vs-path distinction — origin authorized, path possibly leaked.
- DNS delegation: parent referral is not child-zone content authority.

**Kill test:**

Looks initially like `transition authority + freshness` (lease) and `authority + scope` (propagation). Residue survives because:

- Stale holders may retain artifacts and replay them long after their authority lapsed — freshness *of the artifact* is not what's needed; freshness *of the holder's epoch* is.
- Origin-validation does not imply path-validity; the export step is a separate authority check.

Per ChatGPT's spike + DeepSeek validation: **start as composition theorem, promote to axis only if multiple substrates force it.** The composition theorem form:

> Authority to originate or hold a claim does not entail authority to propagate it across a boundary or to assert it after the holding epoch ends.

**Minimal Lean API (sketch — not built):**

```lean
namespace Admissibility.FencedEpochAuthority

variable (Actor : Type) (Claim : Type) (Boundary : Type)

-- Epoch as monotonic counter (lease side).
structure Epoch where
  generation : Nat
  validUntil : Time

-- An authority binding: actor holds claim within epoch.
structure Holding where
  actor : Actor
  claim : Claim
  epoch : Epoch

-- Refusal kernel (lease side): a holding past its epoch cannot authorize action.
theorem stale_epoch_blocks
    (h : Holding) (now : Time)
    (h_stale : h.epoch.validUntil < now) :
    ¬ Admissible (h.actor, h.claim) now := sorry

-- Propagation scope (boundary side): origin authority does not imply export.
def OriginAuthorized (actor : Actor) (claim : Claim) : Prop := sorry
def PropagationAuthorized (actor : Actor) (claim : Claim) (b : Boundary) : Prop := sorry

-- Refusal kernel (scope side): origin authorization does not transitively license export.
theorem origin_does_not_imply_propagation
    (actor : Actor) (claim : Claim) :
    OriginAuthorized actor claim → ¬ (∀ b : Boundary, PropagationAuthorized actor claim b) := sorry

end Admissibility.FencedEpochAuthority
```

**Refusal kernel (informal):**

- *(Lease)* A holding's authority is inadmissible past its epoch's validity, regardless of whether revocation notice reached the holder.
- *(Scope)* An origination authorization does not imply a propagation authorization across any boundary. Each boundary-crossing requires its own admissibility check.

**Forcing case (NQ + Wicket + Nightshift):**

- *(Lease)* A previously-authorized agent resurfaces after partition healing and attempts a transition citing its old authorization. The receipt-system must refuse because the holding's epoch is stale, even if the agent's signed evidence is otherwise valid. Fencing token discipline.
- *(Scope)* Wicket consumes an NQ receipt and authorizes downstream action. Nightshift attempts to use Wicket's authorization to propagate the original NQ claim into a different boundary (e.g., across a fleet/cohort boundary). The propagation must be refused — Wicket authorized the action within Wicket's scope; that does not authorize re-propagation of the underlying NQ claim. This is the cross-kernel disposition's Path C in action.

**Brakes:**

- Do NOT collapse lease + propagation into a single "authority scope" axis. They share structure but live on different gates (time-bounded vs boundary-bounded).
- Do NOT promote to first-class axis until multiple substrates outside BGP/leases force it. Per DeepSeek's caution: *make it win a small county election first.*
- Do NOT model fencing tokens as cryptographic mechanisms in the kernel — that's a Byzantine-extension concern (see `byzantine-fault-tolerance-extension.md`).
- Do NOT confuse social revocation (e.g., institutional authority withdrawal) with lease expiry. Different failure modes, different mechanisms.

---

## 4. ReplaySafeActionIdentity (optional fourth)

**Forbidden inference:**

> **"Timeout means no effect occurred"** and
>
> **"Repeating the same request payload is always a new action (or always the same action)."**

Operation identity is first-class, distinct from request text, transport delivery, or receipt.

**Substrate witnesses:**

- AWS-style idempotency keys: caller-provided UUIDs with bounded dedup window; same key + bounded window → at-most-once effect.
- Stripe `Idempotency-Key` header — same key replays return same result, server-side dedup.
- TLS 1.3 / QUIC 0-RTT replay-safety — application must explicitly mark which early-data is safe to replay.
- HTTP `POST` retry hazard (RFC 9110) — automatic retry only safe under idempotency or out-of-band confirmation.

**Kill test:**

Looks initially like `action + receipt + freshness + refusal composition`. Residue survives because **operation identity is missing as a first-class thing**. Receipt confirms a specific action; freshness bounds the validity; but neither captures *the operation's identity across attempts*. A retried POST with same body and same correlation ID is one operation; a retried POST with same body and different idempotency keys is two.

**Minimal Lean API (sketch — not built):**

```lean
namespace Admissibility.ReplaySafeActionIdentity

variable (OpId : Type) [DecidableEq OpId] (Effect : Type)

-- An attempt: caller-provided operation ID + intended effect.
structure Attempt where
  opId : OpId
  intended : Effect
  attemptedAt : Time

-- Dedup window: bounded interval during which same OpId is deduplicated.
def WithinDedupWindow (a₁ a₂ : Attempt) (window : Duration) : Prop :=
  a₁.opId = a₂.opId ∧ |a₁.attemptedAt - a₂.attemptedAt| ≤ window

-- At-most-once: across dedup window, same OpId produces at most one effect.
def AtMostOnce (attempts : List Attempt) (window : Duration) (effects : OpId → List Effect) : Prop :=
  ∀ a ∈ attempts, (effects a.opId).length ≤ 1

-- Refusal kernel: an attempt without an OpId (or after the dedup window) cannot be assumed
-- to produce a fresh independent effect.
theorem unsafe_replay_blocks_assumed_independence
    (a : Attempt) (h_no_id : a.opId = default ∨ a.attemptedAt > a.attemptedAt + dedupWindow) :
    ¬ Admissible.assumeIndependentEffect a := sorry

end Admissibility.ReplaySafeActionIdentity
```

**Refusal kernel (informal):** *A retry is admissibly the-same-operation only when caller-provided operation identity is present within a bounded dedup window. Absent operation identity, the calculus cannot distinguish retried-same-action from second-independent-action; neither inference is admissible by default.*

**Forcing case (NQ-adjacent):**

An ops agent issues an HTTP `POST` to create a pager event in response to an NQ finding. The HTTP response is lost (timeout or transport failure). The agent retries.

- *If* the original POST included an idempotency key and the retry uses the same key within the dedup window: the server treats it as the same operation, returning the same result. Single pager event.
- *If* no idempotency key, or the dedup window has lapsed: the server treats the retry as a new operation. Two pager events. Probably wrong.

The refusal kernel's contract: the calculus refuses to assume "no effect occurred" from a timeout, and refuses to assume "same action" from same payload text. Operation identity must be carried explicitly.

**Brakes:**

- Do NOT generalize "operation identity" to include semantic equivalence (two attempts that "mean the same thing"). Identity is caller-provided, not server-inferred.
- Do NOT confuse application-level operation identity with transport-level delivery semantics. TCP ACK is not application receipt; idempotency key is not transport-layer.
- Do NOT extend to cross-operation transactional semantics (two operations atomically). That's a different family.

---

## Bucket summary

All four sketches are **Bucket C** (genuinely new structural axis) per the spike plan's triage framework. None collapses into existing primitives without residue.

### Phase D promotion potential (theoretical / formal cleanliness)

| Sketch | Promotion potential | Rationale |
|---|---|---|
| `VersionBoundAction` | High | Distinct axis (commit-point precondition); clean Lean shape; consumer-side substrate already on the NQ wire (revision counters in `warning_state`). |
| `AuthenticatedDenial` | Medium-high | Sharpens existing silence/denial work; high consumer relevance (NQ `cannot_testify` could carry signed-denial semantics). |
| `FencedEpochAuthority` | Medium | Composition theorem first; promotion to axis requires multi-substrate evidence. Cross-kernel disposition Path C already touches the scope side. |
| `ReplaySafeActionIdentity` | Medium | Real and operationally ubiquitous; primary consumer is action-taking tools (Wicket / Nightshift / agent_gov), not NQ proper. |

### Recommended build order (operational urgency — distinct question)

Promotion potential and build order are not the same question. Promotion potential answers *which sketch most cleanly earns the public surface.* Build order answers *which sketch most urgently needs to exist before agentic tooling breaks against the forbidden inference.*

Per ChatGPT's spike review (operational urgency axis):

| Order | Sketch | Why this order, not the formal-cleanliness order |
|---|---|---|
| 1 | `VersionBoundAction` | Highest promotion potential AND immediate ops-agent relevance. No reorder pressure. |
| 2 | `ReplaySafeActionIdentity` | Bumped up from 4th. Reasoning: anything agentic that touches side effects hits retry ambiguity *before* it hits signed-denial witnesses. *Same payload means same operation* is wrong every Tuesday; nature's tax on optimism. Wicket / Nightshift / agent_gov consume this directly. |
| 3 | `FencedEpochAuthority` | Composition theorem; composes with agent authorization work. Strongest forcing case: an actor with a token-shaped artifact whose epoch has advanced past the artifact's validity. |
| 4 | `AuthenticatedDenial` | Formally attractive but substrate-dependent. A probe must model the signed-denial/silence distinction and cryptographic boundary explicitly; an NQ or DNSSEC fixture can later instantiate and stress it but is not permission to formalize. |

The reorder reflects operational priority, not formal admission. `ReplaySafeActionIdentity`'s "timeout means no effect" mistake is what duplicates pager incidents, doubles rollbacks, doubles "our bad" entries. `AuthenticatedDenial`'s sharpening of silence-vs-denial needs a precise signed-denial model; formal work may establish that contract before a tool path exists.

## What this pack is NOT

- **Not a build order.** Each sketch's Lean API is illustrative, not automatically sound or testimony-bearing. A specific probe needs stable semantics, bounded cost, a distinct theorem residue, overlap review, and surviving brakes; no runtime forcing case is required.
- **Not promotion of any kernel to Public Phase D.** Public Phase D Criterion 3 (production fixture) still gates promotion; sketches don't satisfy that gate.
- **Not a commitment to all four candidates surviving.** The `ReplaySafeActionIdentity` optional-fourth may get demoted after further scrutiny; `FencedEpochAuthority`'s lease/scope combination may split into two kernels if forcing cases diverge.
- **Not a closed list.** Future spike sessions in other prior-art slices (consensus literature, real-time systems, regulatory frameworks) may surface additional C-bucket candidates. The pack grows; the discipline doesn't.

## Doctrine keepers

> **The sketches are the substrate. The Lean modules are the probes. Precise models, discriminating theorems, overlap review, and proof controls gate the probes; forcing cases inform priority and public promotion.**

> **Each sketch carries its own kill test. If the residue argument fails during construction, the sketch is retracted, not extended.**

> **Operation identity, version identity, scope identity, denial identity — these are the four flavors of identity that internet protocols repeatedly carve out as distinct from witness, freshness, authority, and receipt.**

> **Identity refinements are admitted only when two artifacts with similar surface shape must be refused as non-equivalent.** (Anti-universal-solvent brake.)

> **Operational misbehavior arrives before theoretical purity demands resolution.** (Build-order discipline; formal version.)

> **The incident clown car arrives before the theorem parade.** (Same discipline; field version. Use when audience is closer to ops than formal methods.)

> **Without the brake, "identity" decays into *ontology ranch dressing* — pours over anything, distinguishes nothing.** (Failure mode named.)

> **The cursed adult choice: four small refusal kernels and a matrix.** Not a new field; not deletion of interesting residue; the staging discipline between those two failure modes.

> **The substrate already exists. The spike's contribution is legibility, not invention.** (Constructive vs critique distinction; defensible against "you made this up" because CAS / NSEC / OTC / idempotency keys predate the carve by decades.)

## Cross-references

- [[prior-art-spike-plan]] — parent plan; this pack is the third of three spike-session outputs.
- [[forbidden-inference-register]] — sibling matrix; rows 1-5 of the register correspond to this pack's four sketches plus the closely-related operation-identity variant.
- [[internet-substrate-failure-map]] — sibling artifact; failure families C/D/H map onto these sketches.
- [[three-time-decomposition]] — `VersionBoundAction` is the missing axis sibling to operator-time / metric-time / phase-time. Version is a *non-time* identity axis.
- [[byzantine-fault-tolerance-extension]] — adversarial layer; each sketch has Byzantine-extension defenses (signed version chains, signed denial chains, signed epoch certificates, signed operation IDs).
- [[cross-kernel-disposition]] — Path C; `FencedEpochAuthority`'s scope side is the cross-kernel propagation refusal the disposition already covers.
- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — current annex substrate; sketches would land as new namespaces under `RefusalPropagation.Annex.*` *if* future construction-discipline gates fire.
- `~/git/lean/LeanProofs/Admissibility/Freshness.lean` — sketch 1 (VersionBoundAction) is the residue axis NOT covered by Freshness.
- `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` — sketch 2 (AuthenticatedDenial) sharpens the silence/denial distinction that ConsolidationDenial implicitly carries.

## Provenance

- **2026-05-26.** First internet-substrate spike session under `prior-art-spike-plan.md`. ChatGPT performed broad survey + reduction pass; DeepSeek sanity-checked the residue claims and asked three clarifying questions; operator routed all three model outputs back for triage. Four C-bucket candidates surfaced and survived reduction.
- DeepSeek's Q&A directly informed three sketches:
  - *Q1 (version separate from freshness?)* → Yes. Sketch 1 keeps it separate.
  - *Q2 (propagation scope as new axis?)* → Composition theorem first. Sketch 3 starts composition-shape, defers axis promotion.
  - *Q3 (Merkle as NQ forcing case?)* → Annex witness only, NOT in this pack. *Merkle proves shape. It does not appoint a custodian.*

## Disposition

Pack filed. No Lean built in this pass. Each sketch survives a preliminary kill-test against existing primitives. Phase D Public promotion is separately gated by:

- Construction-discipline trigger (substrate-exists + bounded-cost + brakes-survive) for any specific sketch.
- Production fixture (Public Phase D Criterion 3) for actual public promotion.

Priority and correspondence watchlist per sketch — these targets can prioritize or instantiate a probe, but do not grant permission to formalize:

- `VersionBoundAction`: NQ adds revision-bound preflight (likely near-term given existing `warning_state.last_basis_generation` substrate).
- `AuthenticatedDenial`: NQ ships signed `cannot_testify` witnesses (requires cryptographic substrate, deferred per BFT plan).
- `FencedEpochAuthority`: agent_gov / Wicket adds explicit epoch-bounded authority (likely near-term).
- `ReplaySafeActionIdentity`: any consumer that retries side-effecting actions (Nightshift proposal execution, agent_gov action issuance).

> **Sketches are pre-construction substrate. The discipline is in the kill-test. Precise formal questions decide what may be probed; runtime cases help decide priority, correspondence, and public promotion.**
