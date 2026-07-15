# Admissible Incompleteness for the Lean Stack

*Status:* CANDIDATE / working note. Operator-supplied doctrine, filed 2026-07-06.
Externally cross-checked (ChatGPT + DeepSeek) before integration.
*Lean custody:* extracted-to: `~/git/lean/LeanProofs/Scratch/AdmissibleIncompleteness.lean` (scratch-checked; extraction is not public promotion)
(Custody-Class: SCRATCH, unwired, sorry-free, **zero-axiom** — every invariant below
that has a Lean shape is a proved theorem, not an `axiom`).
*Not* a resurrection of "admissibility calculus": local enums, no typeclass, nothing
exported for cross-calculus reuse.

**Operator fence (binding):** do NOT encode admissible incompleteness as "eventual
completeness." It is not a TODO state. It is a governed state. Some open findings are
meant to remain open while still allowing scoped continuation.

---

## Thesis

Admissible incompleteness in the Lean stack is **bounded formal partiality with custody**.

A Lean artifact may be incomplete and still useful when its incompleteness is explicit,
scoped, carried forward, and unable to launder itself into proof, authority, runtime
correspondence, or closure.

Lean proves **profile laws / derivation properties / bridge obligations** inside a
declared formal frame.

Lean does **not** by itself prove:

- that the frame is adequate to the real system,
- that AG/Rust implements the frame correctly,
- that runtime schemas match the formal model,
- that an admissible claim is authorized for action,
- that a candidate/scratch artifact is ratified,
- that local profile validity implies global authority.

The core rule:

> Incomplete Lean evidence may discharge a narrower obligation.
> It may not silently discharge the wider obligation the user/operator wished were true.

## Admissible vs Inadmissible Incompleteness

### Admissible incompleteness

Incomplete Lean work is admissible when it states:

- the exact theorem/model/profile/frame being claimed,
- the import surface or artifact tier,
- the assumptions/axioms/model boundary,
- the obligation it can discharge,
- the obligation it cannot discharge,
- whether it is `SCRATCH`, `CANDIDATE`, `IMPORT_SURFACE`, or `RATIFIED`,
- what external ratification would be required for runtime/governance use.

This is the Lean version of:

> permit scoped continuation, deny closure, leave the finding open.

### Inadmissible incompleteness

Incomplete Lean work is inadmissible when it lets any of these happen:

- scratch/candidate proof cited as ratified doctrine,
- import reachability treated as custody,
- green build treated as semantic admission,
- local theorem treated as global authority,
- admissibility proof treated as operational authorization,
- profile theorem used across a boundary without an explicit bridge,
- proof receipt treated as model adequacy,
- generated theorem treated as its own justification,
- runtime correspondence assumed without AG/Rust/specimen ratification.

## Lean-Specific Rule

A Lean theorem can say:

> "Under formal frame F, derivation D satisfies property P."

It cannot silently say:

> "Therefore production system S may act."

That requires a bridge:

```text
Γ ⊢ p admissible@σ
r : AuthorizesUse(p, α, σ)
--------------------------------
Σ ⊢ α authorized@κ
```

Without `r`, evidence stays evidence. (The bridge receipt `r` is the anti-pope
scoped conversion receipt already resident at
`LeanProofs/Admissibility/AuthorityScope.lean` — cite, do not re-derive.)

## Artifact Tiers

### SCRATCH

A scratch artifact may explore a law, counterexample, encoding, bridge shape, or model
repair. It may be useful evidence. It may not be cited as discharging an obligation.

Allowed claim: "This scratch artifact suggests law L is encodable."
Forbidden claim: "Law L is now part of the admitted Lean surface."

### CANDIDATE

A candidate artifact may be compiled, reviewed, and proposed as a future obligation
discharge. It remains non-authoritative until ratified.

Allowed claim: "Candidate theorem T appears to prove profile property P under model M."
Forbidden claim: "AG may rely on T as a runtime gate."

### IMPORT_SURFACE

An imported, checked theorem may discharge the exact formal obligation it states.
It still does not certify model adequacy or runtime correspondence.

Allowed claim: "The formal obligation P is discharged inside Lean."
Forbidden claim: "The production system satisfies P."

### RATIFIED

A ratified Lean claim is one the operator/project has accepted as a governed claim,
usually after linkage to Rust/AG behavior, hostile specimens, docs, and observed
correspondence.

Allowed claim: "This theorem discharges named obligation O for profile/version V."
Still forbidden: "This proves all adjacent authority claims."

Ratification is scoped, not contagious.

## Core Invariants

1. **No master profile.** Each profile is local; cross-profile use requires a named
   bridge. (Resident: ArtifactProfiles, v7 slice 1.)
2. **Pairwise bridges only.** A bridge must name source profile, target profile,
   carried evidence, lost evidence, required payment/obligation, refusal mode.
3. **Proof does not imply authorization.** Lean can prove admissibility; AG/Rust
   governs action. The epistemic→operational bridge is explicit and paid.
4. **Model adequacy is not proved by the model.** A proof may discharge an internal
   obligation; it may not certify the obligation was the right one, the threat model
   adequate, the real system correspondent, or the frame fit to govern production.
5. **Green is not minted.** A green build means the checked surface typechecks. It
   does not promote scratch, ratify candidates, or authorize AG behavior.
6. **Typed refusal is positive evidence, not total knowledge.** A finite custody
   checker's refusal proves that refusal under that finite support/profile, not
   completeness over all future artifacts/schemas/hostile encodings.
7. **Staleness is admissible only if named.** A theorem may remain mathematically
   valid while operationally stale. The artifact is not "wrong"; its authority
   bridge is stale.

## Verdict Vocabulary

```text
DISCHARGED          proved in the admitted/imported surface
DISCHARGED_PARTIAL  proved only for a narrowed profile/frame/scope
CANDIDATE           plausible, may inform ratification, discharges nothing   [tier fact]
SCRATCH             exploratory, evidence only, no discharge                 [tier fact]
OPEN_FINDING        known gap, explicitly bounded; continuation only inside
                    the receipt horizon
HELD                missing evidence inside the obligation horizon; no closure
BLOCKED             missing/invalid evidence would allow authority laundering
OPERATOR_REQUIRED   action may proceed only by explicit operator responsibility
```

Encoding note: CANDIDATE and SCRATCH are **tier** facts, not verdicts — the Lean
encoding keeps them on the tier axis so one axis cannot impersonate the other.

## Minimal Lean Receipt

```text
LeanReceipt {
  artifact: file/module/theorem
  tier: SCRATCH | CANDIDATE | IMPORT_SURFACE | RATIFIED
  profile: local authority/profile/frame
  obligation: what this artifact can discharge
  assumptions: axioms/model boundaries
  imports: actual import/custody surface
  proves: exact theorem/property
  cannot_testify: claims this artifact cannot support
  bridge_required: yes/no + named bridge if yes
  runtime_claim: none | candidate | ratified by AG/Rust
  staleness_conditions: schema/profile/runtime changes that demote relevance
  operator_status: unreviewed | accepted | rejected | superseded
}
```

Only the fields that do proof work are modeled in Lean (tier, verdict, claim =
profile×obligation×scope, bridge_required, cannot_testify); the rest stay prose here.

## The Key Maxim

> Lean may close formal obligations.
> It may not close custody, authority, runtime correspondence, or operator
> responsibility unless those are explicitly part of the ratified bridge.

Shorter:

> **Incomplete Lean is admissible when it narrows authority.
> Incomplete Lean is inadmissible when it borrows authority.**

---

## Encoding delta (what the shipped Lean does relative to the seed sketch)

The seed sketch (this note's provenance chat) proposed `axiom` declarations. The
shipped file proves everything; **zero axiom declarations, zero-axiom footprint**
(`#print axioms` = "does not depend on any axioms" for all load-bearing theorems —
below even the resident propext/Quot.sound footprint).

Deliberate corrections and extensions:

1. **No self-declared surface.** The sketch carried `surface : AuthoritySurface` as a
   receipt *field*. A receipt that self-declares `execute` is the tiny pope the
   AuthorityScope annex demotes. Shipped: the surface is **computed** —
   `cap r = min(tierCap, verdictCap, bridgeCap)` — so a receipt cannot self-assert
   authority. `runtime_anatomy` then *derives* the sketch's
   `AuthorizesRuntimeUse := execute ∧ ratified ∧ ¬bridgeRequired` as a theorem.
2. **Ceiling matrix** (evidenceOnly < propose < admit < promote < execute):
   tier scratch→evidenceOnly, candidate→propose, importSurface→admit,
   ratified→execute; verdict discharged→execute, dischargedPartial→admit,
   openFinding→propose, held/blocked/operatorRequired→evidenceOnly;
   bridge unpaid→admit, paid→execute. Design call: an unpaid bridge caps at `admit`
   (not just blocking execute) so staleness composes — a stale artifact drops below
   promotion without its theorem becoming wrong.
3. **Staleness = bridge demotion.** `stale r` flips only `bridgeRequired`;
   `stale_never_raises` (monotone down), `stale_blocks_runtime`, and
   `stale_validity_orthogonal` (**`Iff.rfl`** — staleness cannot touch discharge)
   encode invariant 7 exactly.
4. **No promotion function** exists in the file, per the operator fence. The only
   endogenous transform is `stale`, and it is provably downward. Tier ascent is the
   paid external rung (ProfileStages `ascend`).
5. **Operator layer.** `OperatorWarrant` + `operator_required_is_not_proof` +
   `operator_leaves_cap_at_evidence`: responsibility moves; authority does not.
6. **Exactness instead of a scope order.** `discharge_is_exact` (a receipt discharges
   exactly its stated claim) does all anti-widening work; `ratified_scope_does_not_
   expand` and `no_cross_profile_discharge` are corollaries. The honest move licensed
   by DISCHARGED_PARTIAL is *restating the narrow claim on a fresh receipt*, never
   widening this one.

All eight theorems from the seed sketch's candidate list are present under their
proposed names: `partial_not_full`, `candidate_never_authorizes_runtime`,
`scratch_never_authorizes_runtime`, `cannot_testify_blocks_discharge`,
`bridge_required_blocks_runtime_authority`, `ratified_scope_does_not_expand`,
`held_is_not_discharge`, `operator_required_is_not_proof`. Plus:
`import_surface_never_authorizes_runtime` (the sharpest new face: even the import
surface never authorizes runtime), `green_is_not_minted`,
`discharge_is_not_authorization` (NoFreeStandingReadout's sibling),
`incomplete_never_promotes`, `cap_never_exceeds_tier`, `blocked_denies_continuation`,
`continuation_is_not_closure`, and positive witnesses (`full_green_path_executes`,
`partial_at_admitted_tier_admits`, `open_finding_permits_continuation`) so the kernel
is not universal refusal.

## Overlap ledger (cites, does not re-derive)

- **ProfileStages** — tier *dynamics* (paid rungs). This work freezes tier, studies
  the ceiling it buys.
- **Admissibility/AuthorityScope (annex)** — what a paid bridge *is*;
  `bridgeRequired` here is demand-side only.
- **ArtifactProfiles** — no master profile / paid pairwise bridges.
- **NoFreeStandingReadout** — CanRead⊬MayReadout; sibling structural absence here is
  CanDischarge⊬AuthorizesRuntimeUse.
- **BestEffortCompleteness** — closes ≠ discharges; held/blocked/operatorRequired are
  its verdict-side siblings.
- **CaveatSequent** — burdens grow under derivation; `cannotTestify` is the static
  face of the burden surface.
- **OverlapAudits Run 1** — `cannot_testify` vocabulary already resident for derived
  relations; here it becomes a receipt field with teeth.

## Downstream (candidate, operator's lane)

The verdict vocabulary (DISCHARGED / DISCHARGED_PARTIAL / OPEN_FINDING / HELD /
BLOCKED / OPERATOR_REQUIRED) and the LeanReceipt schema are the pieces most likely to
fall out as changes in AG and other tooling (gate outcomes, receipt formats).
That adoption is a consumer move with its own ratification; nothing in the Lean
scratch file or this note authorizes it.
