# Observer Foundation — Promotion Preflight (NOT promoted)

**Status:** CANDIDATE / non-binding. Filed 2026-06-14, **updated 2026-06-14 after a
seven-system excavation pass.** This is a *handle for review*, not authorization to
build. Consolidation/promotion is ratification-tier and deferred.

**What changed in the update:** the original blocker ("no present consumer → withhold")
is **discharged** — it was the wrong gate. The observer theorem did not need a *future
forcing case*; it needed an *excavation pass* across already-shipping systems. Seven of
them fell out of the closet wearing fake mustaches. They are the forcing cases. The
nucleus codomain also moved: it is **not** `Prop` (my guess) and **not** `Strength`
(the other guess) — it is an abstract `Verdict`.

Do **not** rewrite the four existing Lean slices on the strength of this. They are
correct *specimens* at a fixed codomain (Prop); they are fossils, not errors. The
correction is **additive** (a new generic slice), recorded here as a receipt *before*
any Lean move — so the correction is custody-tracked, not "Claude got excited and fixed
the math."

---

## The excavation pass (2026-06-14) — the "no consumer" blocker is discharged

Seven shipping systems were read read-only for their force/admissibility model. Every
one assigns force/admissibility **relative to consumer-supplied inputs** — none has a
bare `Force(artifact)`. The blocker is discharged by shipping evidence:
**NQ, nightshift, wicket, continuity, standing, verifier, WLP.**

| System | Force codomain | Freshness | Artifact | Root | Refusal |
|---|---|---|---|---|---|
| NQ (producer) | binary witness verdict | consumer-judged (emits age only) | flat; *rejects a witness that names its own claims* | none | typed |
| nightshift | product: binary gate × 5-level `RelianceClass` × scope bitmask | consumer-judged (own 90s; ignores NQ `fresh`) | flat | none (declared ceiling) | typed |
| wicket | product: 5-verdict × 3 dims (basis/precedence/standing), soft/hard | consumer-judged (`call_timestamp`; "time is evidence, not ambient reality") | flat | none ("bouncer, not legislature") | typed |
| continuity | binary (`rely_ok: bool`) | consumer-judged (`evaluation_time` param; kernel never calls clock) | flat | none ("Governor carries consequence") | typed |
| standing | binary (Allowed/Denied/Unknown) | consumer-judged (`VerifyOptions{skew, max_clock_divergence, now}`) | flat | **operator-fiat genesis** (the one root) | typed |
| verifier | **validity-only, NOT force**; frame-*independent* | **producer-baked** (`claim_state`) — lone exception | flat | none ("`authorized` reserved upstream") | typed |
| WLP | typed enum (9 verdicts) | consumer-judged (`reference_time`); explicit Expired + not-yet-valid | flat; *same artifact `Accepted` by one consumer, `Unsupported` by another* | none ("TLS secures the pipe, not the artifact") | typed |

## The five extracted invariants (unanimous; the actual nucleus)

1. **Force/verdict is consumer-relative.** No bare `Force(artifact)` anywhere (7/7).
   WLP is the cleanest exhibit: the *same* artifact is `Accepted` by one consumer and
   `Unsupported` by another, on the consumer's own `supported_policy_schemes`.
2. **The artifact is a flat fact.** No consumer/authority/root field on the evidence
   object (7/7). Force lives on the consumer side, never stamped on the envelope. NQ
   *rejects at the validator* any witness that names its own claims. (This is the
   absolute-force-stamp refusal and "Stamp must be unrepresentable" — already true
   architecturally.)
3. **Freshness is consumer-judged in force-assigning systems** (6/7). Consumer supplies
   the reference time/threshold and recomputes; no producer `fresh` flag is trusted
   (nightshift explicitly ignores NQ's). `standing`'s `VerifyOptions{skew,
   max_clock_divergence, now}` is literally `Freshness.DivergenceAcceptable` shipping.
4. **Rootless, except one single-genesis.** 6/7 have no trust root (authority is a
   declared ceiling); `standing` has operator-fiat genesis — the single-root case. This
   is `NoUniversalRoot` (rootless ⇒ consumer-relative) **plus**
   `universal_root_licenses_stamp` (the lone genesis licenses its own local stamp). Root
   is the exception, not the nucleus.
5. **Refusal/verdict is typed** — named variants / reason codes, never a bare bool or
   raw error (7/7).

## Verifier as the negative control

`verifier` is the only system that is **validity-only, not force-assigning** — and it is
*also* the only one that is **frame-independent** and uses **producer-baked freshness**
(`claim_state`, not a consumer threshold). The system that does not assign force also
does not judge freshness and is not consumer-relative. Force-assignment, consumer-
relativity, and consumer-judged freshness travel together; lose one, lose all three.
That is the confirming negative — it tells us the three invariants are one capability.

## The corrected nucleus

```lean
Force : Consumer → Artifact → Verdict      -- Verdict parameterized
```

- **NOT** `Force : Consumer → Artifact → Prop` (my earlier guess) — that is the
  degenerate 2-variant case, shipped by only 2/7 (continuity, standing).
- **NOT** `Force : Consumer → Artifact → Strength` (the other guess) — no system ships a
  scalar/lattice strength. The graded ones (nightshift, wicket) ship *products of small
  ordered enums + a binary gate*, not a scalar.

The codomain **varies by system** (binary / product / 9-variant enum). What is invariant
is **consumer-relative verdict production**, not the verdict's shape. So the foundation
must leave `Verdict` a type parameter; fixing it either way contradicts 5 of 7.

## Don't pave the fossils

The four existing slices (`ConsumerRelativeFreshness`, `ConsumerRelativeForce`,
`AbsoluteForceStampBridgePrice`, `NoUniversalRoot`) are correct **at codomain `Prop`** —
a real special case, useful specimens. Do **not** rewrite them. The correction is a new
generic slice that *subsumes* them, with the Prop versions surviving as the
`Verdict := Prop` instance.

## Subgate worksheet (vocabulary-foundation gate) — now answerable

The `wiring-is-not-folder-placement.md` vocabulary-foundation subgate's eight questions,
answered from the excavation:

1. **Downstream consumer now?** Seven shipping ones (table above). Discharged.
2. **Recurrence vs decoration?** The five invariants recur across 7 independent systems
   in 3 languages. Recurrence, not decoration.
3. **Excluded meanings?** `Consumer` = the verdict-producing frame that holds the
   reference time/threshold (= clock-frame; *not* end-user, *not* verifier-validity).
   `Force` = consumer-assigned verdict (*not* validity — verifier shows validity is the
   frame-independent sibling; *not* a scalar strength). `Verdict` = system-supplied
   closed type. `Root` = single-genesis exception, *not* a nucleus primitive.
4. **Minimal nucleus?** The five invariants + `Force : Consumer → Artifact → Verdict`
   with `Verdict` abstract. (Center theorem: `HasGlobalSection ↔ ConsumersAgree`,
   restated over `Verdict` equality.)
5. **Application lemmas that stay OUT?** All current observer theorems; the bridge-price
   (`AbsoluteForceStampBridgePrice`); the universal-root exception; cross-axis
   (observer × temporal) lemmas; the freshness adapter.
6. **Claim-register linkage?** None yet. Promotion to `CLAIM-REGISTER.md` is a separate
   later act.
7. **Import target?** A generic module (candidate name `ConsumerRelativeVerdict`),
   imported by the Prop specimens as the `Verdict := Prop` instance — *on promotion only*.
8. **Deprecation path?** If the nucleus is later split (e.g. force vs validity as
   verifier suggests), the `Verdict`-parameterized form already isolates the variation;
   the Prop specimens remain valid instances.

## Generic slice — BUILT (additive, 2026-06-14)

**Cut as `~/git/lean/LeanProofs/Scratch/ConsumerRelativeVerdict.lean`** (operator-authorized,
additive — the four Prop slices left intact as the `Verdict := Prop` instance).
`lake env lean` green, `sorry`-free, headline theorems (`has_global_section_iff_consumers_agree`,
`no_global_section_when_consumers_disagree`, the V3 specimen) depend on **no axioms**. Codex
adversarial pre-check: **clean** — independently flagged the backward direction's reliance on
`Consumer` inhabited and confirmed it is disclosed and discharged by `deriving Inhabited`; no
overclaim, no vacuity, no axiom leak. NOT wired, NO shared module, NO claim-register promotion.

The slice as built (matches the description below):

```text
Scratch/ConsumerRelativeVerdict.lean   (generic nucleus, Verdict parameterized)
```

```lean
structure Consumer where
  id : Nat
structure Artifact where
  id : Nat
variable {Verdict : Type}

def ConsumersAgree (force : Consumer → Artifact → Verdict) : Prop :=
  ∀ c d a, force c a = force d a

def HasGlobalSection (force : Consumer → Artifact → Verdict) : Prop :=
  ∃ global : Artifact → Verdict, ∀ c a, global a = force c a

theorem has_global_section_iff_consumers_agree
    (force : Consumer → Artifact → Verdict) :
    HasGlobalSection force ↔ ConsumersAgree force
```

This preserves the existing Prop theorem as the `Verdict := Prop` instance while
dropping the pretense that `Prop` is the real codomain. (`ConsumersAgree`/`HasGlobalSection`
use `Verdict` *equality*; no `DecidableEq` needed for the abstract theorem — it is
pure-logic and should stay axiom-free like the Prop version.)

## RATIFICATION QUESTION — RESOLVED 2026-06-14

> ~~Add a new generic scratch slice `ConsumerRelativeVerdict.lean` (Verdict-parameterized,
> additive, leaving the four Prop specimens intact)?~~ **YES — built additively 2026-06-14,
> codex-clean, zero-axiom; Prop slices untouched.** This was a scratch additive act, NOT
> promotion. What remains ratification-tier and still deferred: shared-vocabulary
> consolidation, a foundation module, the public-noun decision, and `CLAIM-REGISTER.md`
> promotion of the center theorem.

## The compromise: more scratch/integration, NOT a foundation module (2026-06-14)

ChatGPT pushed back on jumping to a shared foundation module, and the pushback holds.

- **More scratch / integration / audit — DONE.** A scratch *aggregator*
  `~/git/lean/LeanProofs/Scratch/ObserverPacket.lean` imports the five observer slices;
  `lake build LeanProofs.Scratch.ObserverPacket` is green (integration check — the slices
  build in the real lake graph, not just `lake env lean`); abstract center theorems
  zero-axiom; **NOT imported by `LeanProofs.lean`** (build-coverage, not custody). Plus two
  notes: [`excavation-vs-yagni.md`](excavation-vs-yagni.md) (doctrine) and
  [`observer-consumer-independent-verdict-claim.md`](observer-consumer-independent-verdict-claim.md)
  (paper-facing claim sketch, non-register).
- **Shared foundation module — STILL HELD.** A public module turns *names into substrate*:
  the moment other files `import` it, you have declared "these are the nouns future work
  must speak." That freezes choices that are *probably* right but not
  *make-downstream-depend-on-them-today* right.

**The live gate is now the noun, not the theorem.** `has_global_section_iff_consumers_agree`
is clean. The risk is `Force`: the excavation found *consumer-relative verdict production*,
and `Force` is one loaded reading of the verdict (enforceability), not the neutral
foundation word. The public noun (`Force` / `Adjudicates` / `Evaluates` / `AssignsVerdict`
/ `Admits` / `Relies` / `Consequence`) determines what future lemmas accidentally claim,
and is decided **at module-mint, not now**. The scratch `Force` label is a fossil, not a
ratified noun.

## OPERATOR DECISION — 2026-06-14 (deadlock break)

To stop the loop re-litigating "noun undecided" as "observer work frozen," the operator
ruled. **"Noun undecided" does not freeze fenced progress.**

1. **Global doctrine — HOLD.** Do **not** promote `excavation-vs-yagni.md` to global
   `CLAUDE.md`. Correct, but only one firing; candidate until a second independent
   recurrence. Keep the local breadcrumb (the `Scope vs coverage` slot pointer).
2. **Shared observer vocabulary — DO NOT MINT YET.** No public module, no claim-register
   promotion.
3. **Provisional Lean-facing neutral noun — RECORDED (not minted):**
   `VerdictFor : Consumer → Artifact → Verdict`. Names the *output*, not the metaphysics;
   codomain-aware (works for `Allowed`/`Denied`/`Unknown`); avoids the
   `Force`/`Admits`/`Adjudicates` overloading.
   - **`AssignsVerdict`** — acceptable fallback (precise, clunkier identifier).
   - **`Relies`** — **rejected as nucleus language**, reserved for paper prose /
     reliance-specific application lemmas only. Reason: the codomain includes negative /
     unknown verdicts, so `Relies consumer artifact = Denied` / `= Unknown` reads as "the
     consumer relies on a denial" — a semantic oil slick. `Relies` is good paper-language,
     bad foundation-language.
4. **Continue fenced progress only:** scratch aggregation, compile/audit, codex precheck,
   non-register prose. No shared module, no `LeanProofs.lean` wiring, no `CLAIM-REGISTER`
   promotion.

This is a *recorded provisional*, not a mint: when a public module is eventually minted,
`VerdictFor` is the default unless a better reason surfaces. The scratch `Force` label
stays as-is (fossil); not renamed.

## Graduation steps (unchanged, gated on the question above)

1. (done) Excavate the constellation; record invariants + corrected codomain here.
2. (done) Generic-slice question resolved: yes, additive.
3. (done) Added `ConsumerRelativeVerdict.lean` (green, codex-clean, zero-axiom); Prop
   slices remain as the `Verdict := Prop` instance, not rewritten.
4. (deferred, ratification-tier) Shared-vocabulary consolidation / foundation module /
   public-noun **mint** (provisional preference recorded: `VerdictFor`, fallback
   `AssignsVerdict`; see Operator Decision above) / `CLAIM-REGISTER.md` promotion of the
   center theorem — all still gated, still the operator's call.

## Pointers

- Lean scratch (Prop specimens): `~/git/lean/LeanProofs/Scratch/{ConsumerRelativeFreshness,
  ConsumerRelativeForce, AbsoluteForceStampBridgePrice, NoUniversalRoot}.lean`
- Excavated systems: `~/git/{nq-root,nightshift,wicket,continuity,standing,verifier,wlp}`
- Subgate: `working/wiring-is-not-folder-placement.md` (vocabulary-foundation subgate)
- Index pin: `docs/formalization-index.md` (observer, warrant-tier, not promoted)
