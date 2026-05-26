---
title: "Cross-kernel disposition for Public Phase D"
status: working disposition (Path C)
filed: 2026-05-26
supersedes: ambiguous Criterion 1 in i-want-a-plan-groovy-stardust.md
---

# Cross-kernel disposition for Public Phase D

**Status:** Working disposition. Captures the doctrine for Criterion 1 of Public Phase D in `~/.claude/plans/i-want-a-plan-groovy-stardust.md`. Filed 2026-05-26 after the Annex Phase D extraction landed cleanly and the cross-kernel scope question became answerable.

**Posture:** Doctrine first, formalization second, plan ratification third. This note exists *before* the Lean adapter that instantiates it, so the disposition shapes the Lean rather than the Lean reverse-engineering the disposition.

---

## The load-bearing sentence

> **Each kernel may consume another kernel's receipt, but may not inherit its authority.**

This is the whole claim. Everything else in this note serves it.

## The structural encoding

The "no jurisdiction merge" rule is **not aspiration. It is math.**

`Composition.CascadeSound` (as parameterized in `ChainAdapter` and instantiated across the four chain consumers) has direction:

```
∀ dep anc, DependsOn dep anc → Refused state anc → Refused state dep
```

The cascade goes **one way only**: refusal propagates from ancestor to dependent. There is no symmetric clause `Observable state anc → Observable state dep`. Affirmative authority **cannot** flow through `requiredFor` edges, because the cascade rule simply does not carry it. Only refusal does.

This means cross-kernel composition through receipts is already structurally bounded by the existing `RefusalPropagation` machinery. The brake is in the math, not in the prose. We do not need a new theorem family to prevent kernels from inheriting each other's authority — `CascadeSound`'s directionality already forbids it.

## The three paths considered

Three dispositions for Public Phase D Criterion 1 ("composition between refusal kernels"):

- **Path A — earn cross-kernel theorem family.** Build theorems that fuse kernel semantics (e.g., a theorem whose hypothesis cites both `SurfaceAuthorization`'s verdict and `FiatAdmissibility`'s classification, concluding a stronger refusal). Opens the sewer grate; risks growing a shared verdict algebra, cross-kernel authority synthesis, unified semantics ontology. The "Unified Theory of Nope" failure mode.
- **Path B — bracket cross-kernel as a non-goal.** Document explicitly that Public 2.0 does NOT claim composition between distinct refusal-kernel families. Austere; misses the receipt-propagation use cases that NQ + Wicket + Nightshift actually need.
- **Path C — cross-kernel refusal propagation through receipts; no jurisdiction merge.** Bounded between A and B. Refusal carries across kernel boundaries via receipt-dependency. Authority does not.

**Working disposition: Path C.**

## The outward-facing slogan candidate

> **Refusal provenance across kernel boundaries.**

The slogan is specific (refusal, not authority), bounded (provenance, not synthesis), honest (across boundaries, not merging them). It says what Public Phase D 2.0 would claim and — implicitly — what it would not claim.

The contrast with the non-goal is sharp: **not** a unified theory of refusal across kernels, **not** a shared verdict algebra, **not** cross-kernel authority synthesis. The receipt is the *interface*, never the *authority transfer*.

## Substantive surface area

Three use cases that ratify Path C as a real disposition (not a one-off accommodation):

1. **Claim → action (flagship: NQ → Wicket → Nightshift).** NQ produces a claim about substrate; Wicket consumes the claim as an authorization basis and produces a receipt; Nightshift consumes the receipt and decides whether to execute. If NQ emits `cannot_testify`, Wicket's receipt cannot bind authorization, and Nightshift's reconciler treats the absent authorization as denial-equivalent. The cascade carries refusal end-to-end; no kernel inherits another's affirmative authority.
2. **Deferred agent reconciliation.** Nightshift reconciles state across time. If Wicket previously refused, the deferred reconciliation must not proceed as if the refusal didn't happen. Refusal provenance persists across reconciliation cycles; the cascade discipline is the same single-snapshot one, applied at each reconciliation tick.
3. **Audit replay.** Replaying a sequence of (NQ claim, Wicket receipt, Nightshift proposal) for audit. Refusal must propagate the same way in replay as in original execution. The audit replay is structurally equivalent to a fresh cascade evaluation; the disposition holds across time.

Each use case shares the same *shape* (refusal-through-receipt, no authority transfer) while spanning different *substrate domains* (synchronous claim→action, asynchronous reconciliation, retrospective replay). That breadth is what makes Path C a disposition rather than a one-off NQ→Wicket→Nightshift fixture.

## Pre-commitment

> **If the cross-kernel adapter requires expressing affirmative cross-kernel semantics, the disposition is incorrect and should be revisited rather than the brake being relaxed.**

This is the survival condition for Path C. Pre-commitment is cheap; brake-relaxation in the middle of a proof is expensive.

Concrete failure modes that would invalidate Path C:

- The cross-kernel adapter wants a shared `AuthorityVerdict` type across kernels → stop.
- The adapter wants to express "if A authorizes and B authorizes, then C authorizes" (affirmative composition) → stop.
- The adapter wants kernel-A's `observable` state to license kernel-B's binding-admissibility → stop.
- The adapter wants a cross-kernel "merge" verdict beyond what each kernel produces independently → stop.

If any of these surface during the Lean adapter work, the right move is to revisit this disposition, not to relax the brake. The disposition note exists precisely so the Lean has a doctrine to fail against.

## What this disposition does NOT claim

- Does NOT claim cross-kernel theorem composition at the public surface (that's Path A, refused).
- Does NOT claim that all cross-kernel concerns are out of scope (that's Path B, austere).
- Does NOT claim a unified verdict algebra or shared semantics across kernel families.
- Does NOT claim affirmative authority transfer between kernels.
- Does NOT close Public Phase D by itself — Criterion 3 (production fixture) is independent.

### Scope clamp — live refusal propagation only

Path C is scoped to **live refusal propagation under static state**. The Lean adapter operates on a state assignment `Entity → State` evaluated at a single snapshot; there is no temporal dimension in the formal model.

The following are **explicit non-claims** of Path C — pinned here to pre-empt scope creep and to surface the forcing-case candidates that would legitimately require something beyond Path C if they materialized:

1. **No cross-kernel conflict resolution.** If NQ admits and Wicket refuses for independent reasons (not downstream of NQ's verdict), Path C does not adjudicate the composition. Nightshift consumes both receipts and applies *its own* composition policy; the formal kernel layer says nothing about the policy.
2. **No system-level invariant proofs.** Properties like "no chain of authorizations can grant standing exceeding the weakest link" are system properties that cross all kernels. Path C structurally encodes one such property ("no jurisdiction merge") via cascade directionality; it does NOT provide a framework for proving arbitrary system-level invariants.
3. **No receipt-chain validity reasoning under state change.** If state shifts between issuance and consumption, Path C cannot adjudicate whether a previously-valid receipt is still valid.
4. **No cross-kernel version migration semantics.** Version skew between kernel implementations (NQ v2 vs Wicket v1 cascade semantics) is operational discipline, not Path C work.
5. **No *temporal* cross-kernel composition.** Receipt expiry, basis invalidation, replay validity under shifted state — these are **receipt-format** and **consumer-policy** concerns, not formal kernel concerns. The Lean adapter's static `Entity → State` model is deliberately atemporal.
6. **No adjudication between "expired but historically valid" and "expired and basis-invalidated."** Same expired receipt, different correct downstream responses; that semantic decision is a **consumer-side** policy choice, not a kernel theorem.

### Where the temporal load lives (and why Wicket is the seam)

Path C bracketing temporal validity is not a gap — it's a routing decision. The Δt-aware load lives in:

- **Receipt format** (Wicket's job): freshness horizons, expiry semantics, basis-validity windows, standing-attestation metadata. The format carries time-aware fields that the formal kernel deliberately doesn't model.
- **Consumer policy** (Nightshift's job, at the receipt-consumption site): "this Wicket receipt carries a 24h freshness horizon; we're at T+48h; treat as expired" is a Nightshift-side decision, not a Lean theorem.

This is what makes **Wicket the load-bearing seam** between NQ and Nightshift. NQ doesn't know about Wicket's freshness horizons; Nightshift doesn't know about NQ's witness-staleness semantics; Wicket is the receipts layer that *does* know about both — not because it inherits jurisdiction (it doesn't), but because receipts are the format where Δt-aware metadata lives.

Wicket as the seam absorbs the temporal load the formal kernels can't carry. The format absorbs what the kernels can't; the consumer policy absorbs what the format can't; the formal layer stays small, static, and provable.

### Forcing-case candidates (if any materialize, Path C is insufficient)

These are the cases that would legitimately require something beyond Path C. Naming them makes future scope decisions legible rather than ambient:

- A use case requiring formal proof that two upstream receipts are mutually consistent under cross-kernel reasoning → currently consumer-side, but could force meta-view if it grows.
- A use case requiring formal proof that a receipt chain is still valid given changed underlying state → currently consumer-side + receipt-format.
- A use case requiring deadlock-freedom or circular-dependency-absence proofs at the kernel-system level → currently structural (directional `DependsOn`), but proving it across the system would be a meta-claim.
- A use case requiring formal cross-kernel version migration semantics → currently operational.

None of these forcing cases is currently active. The non-claims section exists so that if one materializes, the response is to revisit the disposition rather than relax the scope.

## What this disposition DOES claim

- Refusal propagates through cross-kernel receipt-dependency edges via the existing `CascadeSound` machinery.
- The "no jurisdiction merge" rule is structurally enforced by cascade directionality, not by prose alone.
- The outward-facing slogan is "refusal provenance across kernel boundaries."
- Three substrate use cases (claim→action, deferred reconciliation, audit replay) ratify the disposition's surface area.
- A single bounded Lean adapter (`NQ → Wicket → Nightshift`) suffices to demonstrate the disposition formally.

## Cross-references

- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Public Phase D Criterion 1 (to be updated to reference this disposition).
- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — `Composition` namespace + `ChainAdapter`; site of the cross-kernel adapter.
- [[adapter-extraction-audit-2026-05-26]] — preceded this; established the ChainAdapter foundation that Path C builds on.
- [[refusal-rebar-status-2026-05-26]] — state receipt that flagged cross-kernel disposition as a Public-D blocker.
- [[nq-testimony-dependency-contract.md]], [[nq-on-nq-forcing-case.md]] — substrate-side contract memos for NQ; Wicket and Nightshift sides have their own substrate documentation in `~/git/agent_gov/` and `~/git/nightshift/`.

## Provenance

- 2026-05-26. After Annex Phase D extraction landed (`ChainAdapter` namespace + four refactored chain consumers), the cross-kernel disposition became the next concrete blocker for Public Phase D. Path C surfaced through multi-model relay (operator + ChatGPT + claude-web) as the bounded middle path between the unconstrained Path A and the austere Path B. Web-claude validated the doctrine-first / plan-second / Lean-third ordering. Wicket — overlooked in the prior audit — restored as the receipts/authorization layer connecting NQ and Nightshift.

> **Refusal propagates. Authority does not. The receipt is the interface; the brake is in the cascade's direction.**
