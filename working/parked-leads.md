# Parked Leads

**Filed:** 2026-05-20 from the eight-slice brainstorm + audit, after the build-list collapsed to MemorySkew (shipped) + Post-Hoc Authorization (filed as working primitive).

**Purpose:** record candidate leads that did not earn new construction *now*, but should not be silently dropped. A backlog ticket quietly becomes obligation. A parked lead with a reopening predicate just says "this shape was seen; reopen only if the world coughs up another specimen."

## The framing

> **"Not earned" is a custody state, not a truth value.**

The dangerous collapse is *not buildable now → not important → discard*. The equally dangerous collapse is *not buildable now → preserve as obligation → haunted backlog*. The middle state is:

> **Preserved, non-binding, reopenable.**

A parked lead lives at *handle* stage in the [[feedback-gate-stack]]. Reopening promotes it to *predicate* stage. Build authorization waits for *fixture* stage.

**Discarding** says: this was noise.
**Deferring** says: this is not allowed to spend authority yet.

The name survives. The authority does not.

## The parking rule

> Deferred leads are not rejected.
> They are preserved as advisory residue with reopening predicates.
> They may not authorize build work until new evidence appears.
>
> A parked lead may be reopened only when it gains one of:
>
> 1. a new negative fixture,
> 2. a live repo consumer,
> 3. a cross-tool recurrence,
> 4. a contradiction not already covered by an existing kernel.
>
> Absent one of those, the lead remains advisory residue.

Per-lead schema (four fields, no more):

- **Handle** — the name.
- **Why it seemed real** — the observation or shape that surfaced it.
- **Why it did not earn promotion** — the audit's specific refusal.
- **Reopen trigger** — the concrete condition that would lift the lead from handle to predicate.

The load-bearing line:

> **"Not earned yet" is not "false." It is "don't let the name spend authority."**

That is the whole anti-goblin-door policy.

---

## Warm leads

Likely real, plausible consumers, repo/audit pressure away from earning construction. Watched, not built.

### Coverage Cannot Mint Absence

- **Handle:** Coverage Cannot Mint Absence.
- **Why it seemed real:** Non-observation is admissible only relative to declared coverage. *Scanner saw no failure* commonly converts to *no failure exists* in operational language; the missing coverage variable creates a sharp inference jump.
- **Why it did not earn promotion:** NQ's `cannot_testify` discipline + `LeanProofs/Admissibility/RecoveryMargin.lean` (*"visible green does not entail recovery margin"*) + `CollapsedSurface` as structural dual already cover the shape. Compression candidate, not new doctrine; would deliver as a keeper sentence + possible small lemma extension to `RecoveryMargin.lean`, not a new module.
- **Reopen trigger:** NQ audit finds a green / non-observation result that downstream consumers convert into *healthy / recovered / absent / safe* without declared coverage being recorded in the receipt.

### Receipt Envelope / WLP Minimum Viable Shape

- **Handle:** Receipt Envelope / WLP MVS.
- **Why it seemed real:** NQ / Wicket / AG / Nightshift each invent receipt-shaped soup independently; tools don't share grammar; consolidation could prevent future drift before the divergence calcifies.
- **Why it did not earn promotion:** Consolidation shape, not new-primitive shape. Cannot be audited from the papers/lean seat (requires reading those tool repos). Designing the envelope from projected usage rather than forced usage is the enterprise-architecture failure mode the brainstorm explicitly flagged.
- **Reopen trigger:** Cross-tool audit of *existing* receipts across NQ / Wicket / AG / Nightshift surfaces a forced shared spine — fields that the tools have already confessed under pressure, not fields a design exercise projects forward.

### Serialized Authority Becomes Claim

- **Handle:** Serialized Authority Becomes Claim.
- **Why it seemed real:** A serialized token / capability / signed attestation crosses a boundary and is treated as still-operational authority by shape alone (JWT replay across `kid` rotation, capability handoff between processes, signed attestation in stale signing context). Operationally common.
- **Why it did not earn promotion:** Already covered by `working/authority-observable-not-constructible.md` from the seven-probe gnat lab (Ada / Lisp / Rust / TypeScript / Erlang / macaroons / Prolog). Existing kernel modules (`Authority.lean`, `SurfaceAuthorization.lean`) structurally imply it. Compression *"once authority crosses serialization, it is no longer authority; it is a claim requiring verification/reminting"* would land as a keeper sentence in the existing working note, not as a new module.
- **Reopen trigger:** Standing / WLP / API boundary surfaces a fresh specimen where a serialized token was treated as live authority without verifier/remint, in a way the gnat-lab probes did not already enumerate.

### Spend Discipline

- **Handle:** Spend Discipline (second of three authority axes; sibling to *Serialized Authority Becomes Claim* above).
- **Why it seemed real:** Memory [[project-authority-kernel]] names three orthogonal authority disciplines from the gnat-lab probe series, each answering a different operational question:
  - *construction:* can this authority be minted? *(covered by current kernel)*
  - *serialization:* can this authority survive crossing a boundary? *(deferred — parked separately above)*
  - *spend:* can this authority be consumed to cause an effect? *(this entry)*
  These are not the same axis. Treating them as one blob is how capability systems go from *beautifully principled* to *why did this token just become a skeleton key.*
- **Why it did not earn promotion:** No live consumer needing spend semantics inside the kernel; current kernel covers construction-discipline only by design. `Corrective.lean`'s attenuation is adjacent but not identical to spend (attenuation is about basis-permissiveness over time, not exercise-mode at the moment of use).
- **Reopen trigger:** A WLP / Standing / AG fixture needs one-shot-vs-replayable authority semantics, attenuation-under-transfer rules, or single-use receipt enforcement *at the kernel level* — not at the consumer side.

### Metric / Clock-Bound Admissibility

- **Handle:** Metric / Clock-Bound Admissibility.
- **Why it seemed real:** Kerberos-audit lesson — initially classified as working-note-no-Lean because fanout was one shape and no consumer was visible; topology later found Standing/Freshness pressure. *Aperture can lie about leads that look bounded.* The clock-comparison shape (observed_at vs evaluated_at, with bounded divergence) is operationally common.
- **Why it did not earn promotion:** `Freshness.lean` (added earlier in May; metric-time admissibility kernel with `WithinValidity` / `DivergenceAcceptable`) likely already carries this predicate. If a consumer surfaces, the audit is *compression vs Freshness* first — possibly small Freshness extension, not new module.
- **Reopen trigger:** A new Standing / WLP / NQ edge needs *observed_at* vs *evaluated_at* bounded comparison **after verifying `Freshness.lean` does not already encode the predicate**.

Aperture caveat: audited from ChatGPT summary of the Kerberos chat; original chat not directly accessed from this seat.

### CorrectiveMonotone / RevocationStore Wiring

- **Handle:** CorrectiveMonotone / RevocationStore Wiring.
- **Why it seemed real:** Prior audit called this the *"single-most-load-bearing future Lean obligation."* `Corrective.lean` + `CorrectiveBoundary.lean` exist with monotonicity claims; the held obligation is making those claims *bite operationally* rather than holding vacuously over an unread revocation store.
- **Why it did not earn promotion:** Held pending a concrete derivation that needs to read revocation state rather than treating monotonicity as a vacuous wrapper. Without a downstream theorem that consumes revocation, the wiring is over-specification.
- **Reopen trigger:** A concrete derivation in `Authority.lean` / `Execution.lean` or a sibling module requires reading revocation state rather than treating monotonicity vacuously — i.e., a fixture where the corrective monotonicity claim becomes load-bearing.

### Cross-Axis Composition Lemmas

- **Handle:** Cross-axis composition lemmas (Fiat × Numerical × Surface × Freshness × AxisSkew composition).
- **Why it seemed real:** Sibling kernel count is now 15. Each kernel proves one-axis admissibility. The deferred question — *how do refusal verdicts from different axes compose into a single fixture verdict?* — is operational pressure that grows with the kernel count.
- **Why it did not earn promotion:** Deliberately deferred in each module's "Not included in v0" section; memory [[project-authority-kernel]] calls out the deferral pattern explicitly. Without a fixture that forces two-axis composition, the lemmas would be aesthetic, not operational.
- **Reopen trigger:** One fixture requires two or more refusal axes to combine into a single verdict — e.g., a finding refused by both `FiatAdmissibility.classify` and `SurfaceAuthorization` that needs a single composed receipt verdict rather than two parallel verdicts.

### WLP `acted` / Validation Coupling

- **Handle:** WLP `acted` / validation coupling (HandlingReceipt v0.2 pressure).
- **Why it seemed real:** Validation success and action attestation are currently too close in WLP's HandlingReceipt shape. Empty `policy_refs` is the cheap fixture; the deeper coupling is `acted` reading validation success as evidence of mutation. This is the post-hoc-authorization-laundering shape applied to WLP specifically.
- **Why it did not earn promotion:** v0.2 pressure rather than v0.1; the coupling is a known design weakness but no fixture has forced separation yet. Composes naturally with `working/primitives/post-hoc-authorization.md` when a concrete fixture surfaces.
- **Reopen trigger:** HandlingReceipt gets used as evidence that action happened or was authorized, in a way that bypasses the prior-standing check — concrete WLP consumer required.

Aperture caveat: audited from ChatGPT summary of the WLP-next-steps chat; original chat not directly accessed from this seat.

### NQ Witness-Profile Extraction

- **Handle:** NQ witness-profile extraction (shared scaffolding vs bespoke collectors).
- **Why it seemed real:** Previously held pending second profile. With DNS now real-ish in NQ (per recent work), a second non-ZFS profile may force shared scaffolding instead of independent bespoke collectors per witness substrate.
- **Why it did not earn promotion:** Held at single-profile stage previously; insufficient witness-substrate variation to force the extraction pattern.
- **Reopen trigger:** Second non-ZFS witness profile in NQ forces shared scaffolding instead of bespoke collectors — **likely already met if DNS-witness work has landed**.

Aperture caveat: audited from ChatGPT summary; status of NQ DNS work not verified from this seat. May already be at reopen condition — consumer-side check recommended.

### P27 Deferred Predicates (`substrateAccusation`, `receiptOutlives`)

- **Handle:** P27 deferred predicates — `substrateAccusation`, `receiptOutlives`.
- **Why it seemed real:** Both predicates cleared a two-case forcing gate during P27 v1.0 prep but were not promoted because no downstream composing theorem needed them at the time. Classic *not false, not yet spendable* territory.
- **Why it did not earn promotion:** Promotion would have been *constitution-by-typechecker without a downstream composing theorem.* `True` placeholders kept in `Admissibility.lean` skeleton with deferred-real-statement docstrings; rule preserved as *"kill the sorrys, don't let the sorrys design the constitution."*
- **Reopen trigger:** A sibling theorem (P28 candidate, AG fixture, distributed-admissibility extension) needs substrate accusation or receipt-horizon as an actual predicate, not as `True` placeholder.

Cross-reference: also recorded in `docs/formalization-backfill-notes.md` P27 entry. The register entry adds the explicit reopen trigger.

### Post-Hoc Authorization Laundering — *already filed*

This lead earned a candidate primitive note this session: `working/primitives/post-hoc-authorization.md`. Listed here for completeness; the Wicket/AG fixture probe is the next reopening trigger but the named-pattern artifact already exists.

---

## Cold leads

Real-looking, but too pretty or too meta. Reopening predicate set deliberately high.

### Cartographer Aperture / UNVERIFIED_RESIDUE

- **Handle:** Cartographer Aperture / UNVERIFIED_RESIDUE.
- **Why it seemed real:** Limited observation context should cap claim strength. A chat-context agent observing a pattern shouldn't promote it as corpus/kernel doctrine without repo access. The discipline is in active use across the session — every parked lead in this register is the rule being applied.
- **Why it did not earn promotion:** Too clean. *ContextAperture → MaxClaimStanding* is suspiciously symmetric and resembles the four-axis-trap shape from an earlier session. All current specimens are chat-context conversations *about* audits; the rule cannot be tested by its own application without circularity. Memory [[feedback-kernel-overlap-audit]] is doing this work as audit-procedure rule already; minting a primitive from it would be naming the audit gate as a primitive — possible, but premature without independent specimens.
- **Reopen trigger:** Two non-chat specimens where limited aperture produces over-strong doctrine or promotion claims in observed third-party work, not in our own audit chatter.

Warning preserved from the brainstorm: do not formalize until both specimens exist. Otherwise it becomes a mirror staring into another mirror and charging rent.

### BridgeStatus Evidence Ladder

- **Handle:** BridgeStatus evidence ladder (graded causal-evidence enum: `absent → observed_sequence → model_assumed → experimentally_supported → mechanistically_witnessed → counterfactual`).
- **Why it seemed real:** 2026-06-10 multi-model session proposed a graded ordinal for how strongly a causal claim is backed, as the gating vocabulary for a "causal overclaim" linter. The verb-class observation underneath it is genuine — *"prevented / reduced / avoided"* are mostly counterfactual claims wearing witnessed hats.
- **Why it did not earn promotion:** The kernel side is deliberately **binary** — `LogOnlyProvesEmission.causalityOf` is audit-unit form (*does not discharge causality*, full stop), not a 6-point strength scale. A graded `inductive Foo | a | b | c | d` ordinal is exactly the autocomplete-shaped [[feedback-enum-regression-tell]] move; it belongs (if anywhere) at the **linter-UX / presentation** layer, not as admissibility substrate. Causal overclaim itself is already register alias entry 16 + `dashboard-quiet-is-not-recovery` + `causality-control-plane`.
- **Reopen trigger:** A concrete linter (NQ / Nightshift postmortem checker) needs a *display-layer* vocabulary to label causal-claim strength on artifacts — and even then it stays UX vocabulary, not a kernel enum. **Rename caveat:** `mechanistically_witnessed` overclaims and should not survive into any shipped surface as written — a witnessed *intervention* is not a witnessed *mechanism*.

---

## Doctrine / methodology keepers

Not build leads. Sentence-level survival, not module-level. Reopening trigger is recurrence in the writing, not in the kernel.

### Narrative Cannot Mint Authority

- **Handle:** Narrative Cannot Mint Authority. *Gap-side framing:* "narrative → standing" / "a story becomes a warrant" has no formal home — same underlying concern, different angle.
- **Why it seemed real:** A story emotionally mobilizes attention, then silently becomes operational authorization. The mythos/mechanism interface needing teeth. The refusal direction is covered by the kernel; the *gap* — the bridge by which narrative is converted into operational warrant — is named but not formalized anywhere.
- **Why it did not earn promotion:** `FiatAdmissibility.classify` already encodes the kernel-side refusal: `metaphor.derive = denied`, `metaphor.authorize = denied`, `prestigeToken.citeSupport = denied`, `prestigeToken.authorize = denied`. `compression-becomes-authority-vocabulary.md` carries the prose. Essay/Chronopolitics layer, not kernel layer.
- **Reopen trigger:** A narrative/testimony layer starts routing action without receipt-backed authorization in a way the existing FiatAdmissibility classifications + compression-becomes-authority prose fail to catch — i.e., a concrete fixture where the *gap* (narrative-to-warrant conversion) is the operative failure, not the *refusal* (FiatAdmissibility-denied claim).

Keeper line worth preserving even if the lead never reopens: *"Narrative may route attention to receipts, but may not authorize mutation."*

### Specification Does Not Mint Object

- **Handle:** Specification Does Not Mint Object.
- **Why it seemed real:** Naming a thing makes it feel formalized. *MemorySkew*, *Receipt Theater*, *Admissibility Drift* — the name reads like the predicate. The shape is operationally important.
- **Why it did not earn promotion:** This *is* the audit procedure ([[feedback-gate-stack]]), not a primitive candidate. Already encoded across `feedback-gate-stack`, `feedback-kernel-overlap-audit`, `feedback-primitive-ratification-gate`. The rule that decides what gets to be a candidate; not itself a candidate.
- **Reopen trigger:** Repeated naming-before-predicate failures appear in audits in a way the existing gate-stack memory does not catch — i.e., the audit procedure itself misses cases the explicit rule would catch.

Keeper line: *"A named pattern does not become an admissible formal object until it has a failure predicate, at least one negative fixture, and a bounded transition surface."*

---

## Already-resolved (recorded for completeness)

| Slice | Status | Where it landed |
| --- | --- | --- |
| **MemorySkew V0** | shipped 2026-05-20 morning | `LeanProofs/Admissibility/AxisSkew.lean` + `working/primitives/memory-skew.md` |
| **Post-Hoc Authorization Laundering** | filed 2026-05-20 evening | `working/primitives/post-hoc-authorization.md` as candidate; Wicket/AG fixture probe deferred as future work |

---

## Why this file exists

The eight-slice brainstorm produced one shipped module, one new working primitive, and six leads that the audit refused to authorize as new construction. Without a parked-leads register, those six either (a) silently die and get re-derived next session, or (b) become a haunted backlog that converts to obligation.

This register is the third option: a deliberate watch handle per lead with an explicit reopening predicate. The leads remain advisory residue until the world produces a specimen sharp enough to spend the audit gate's authority.

> The actual unit of progress is finding the smallest transition where a weak artifact becomes operational authority without earning the crossing.

This file refuses that transition for six leads at once. Names earned: zero. Authority spent: zero. Specimens awaited: enumerated, bounded, conditional.

## Cross-references

- [[feedback-gate-stack]] — handle → predicate → fixture → kernel discipline (this file lives at handle stage for all six entries)
- [[feedback-kernel-overlap-audit]] — the morning's audit rule
- [[feedback-primitive-ratification-gate]] — ten-criterion canonization gate
- `working/primitives/AUDIT.md` — per-primitive overclaim/non-case audit for currently-active primitives
- `working/primitives/post-hoc-authorization.md` — sibling artifact from the same brainstorm; chose the candidate-primitive path because kernel backing existed and the named pattern was operationally ubiquitous
