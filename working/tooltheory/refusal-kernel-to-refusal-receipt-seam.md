# Refusal kernel → refusal algebra seam

**Status:** Seam note only. Not a ratified primitive. Filed 2026-05-25; multiple passes same day after multi-model relay surfaced an operator-family pattern, the *refusal algebra / calculus* category, and a critical logical correction. Possible P28 forcing-case candidate — *not yet, not now.* Needs composition theorems before any "calculus" claim earns its shoes.

**Posture:** Names a three-layer split (admissibility calculus / refusal kernel / refusal algebra) so the layers do not collapse under shared labels. The "algebra" framing is current; "calculus" is the post-composition aspiration. Not new doctrine; not new code. A bridge stub plus an operator-family observation.

**Vocabulary discipline:**
- *Refusal kernel* — individual machine-checked proof blocking one surface→substance witness move.
- *Refusal algebra* — the negative-space structure underneath admissibility: how surface predicates fail to license substantive predicates, how those failures compose, propagate, narrow, degrade, and admit repair.
- *Refusal calculus* — what *refusal algebra* gets to be called once composition rules are theorems, not just observations. Until then: algebra, not calculus.
- *Refusal receipt* — one candidate runtime shape an algebra outcome might take. The file path retains this earlier framing for stability of cross-refs.

---

## The distinction

> **Formal refusal blocks an inference. Runtime refusal blocks use of a basis.**

These are different objects at different layers. They should not share a category name.

| Layer | Object | What it does |
|---|---|---|
| Lean annex | **Refusal kernel** | Proves one witness move is structurally invalid (e.g. *fluency → settlement*) |
| Witness / libwitness | **Refusal testimony** (`cannot_testify` shape) | "This source cannot carry claim K over scope/time S" |
| NQ / preflight | **Admissibility consequence** | DENY / AMBIGUOUS / REQUIRES_REVALIDATION / CANNOT_BIND |
| Governor / Wicket | **Binding lock / denial receipt** | Prevents authority minting or action execution from inadmissible basis |

`RecoveryMargin`, `ClosureEligibility`, and `ConsolidationDenial` are layer-1 refusal kernels. The runtime analogue (whatever it eventually gets named) is a downstream consequence of refusal testimony plus admissibility computation plus enforcement — it lives *across* libwitness / NQ / Governor, not as a single primitive.

## Why this seam note exists

Fresh-context audit (Claude-web, 2026-05-25) read "refusal kernel" and reached one layer down — interpreted it as a runtime primitive that "locks another witness's claim." That is a real-ish operational shape, but inheriting the name "refusal kernel" would produce category collapse:

- **Formal refusal kernel:** invalidates *X therefore Y* as an inference rule. No data flows. Lives in `LeanProofs/Admissibility/`.
- **Runtime refusal (something):** scoped denial of standing for a specific witness / claim / use. Data flows. Lives across libwitness / NQ / Governor.

Same word, two different jobs. The seam note exists so future fresh-context audits don't get to make this layer-jump unobserved.

## The operator family — `surface predicate ⇏ substantive predicate`

The repeated shape across the refusal-kernel family is not coincidence. Each kernel breaks one instance of a single relation:

```
surface predicate  ⇏  substantive predicate
```

**Verified instances on the books (2026-05-25):**

| Surface | ⇏ | Substantive | Artifact |
|---|---|---|---|
| Fluent | ⇏ | SettlementAdequate | `LeanProofs/Admissibility/ConsolidationDenial.lean` (filed today) |
| Signed | ⇏ | Witnessed | `specifications/signed_is_not_witnessed.md` (filed today) |
| VisibleGreen | ⇏ | RecoveryMargin | `LeanProofs/Admissibility/RecoveryMargin.lean` |
| Survival | ⇏ | ClosureEligibility | `LeanProofs/Admissibility/ClosureEligibility.lean` |

**Candidate / predicted instances** (not yet filed as kernels; named here as recognition vocabulary, not as TODO):

- Valid ⇏ Licit (paper-side admissibility — claimed by Claude-web 2026-05-25, no kernel located yet)
- ReportedUncertain ⇏ UncertaintyGoverned (filed as working note [`uncertainty-custody.md`](uncertainty-custody.md) 2026-05-26; three candidate phrasings of one diagnostic family — `ReportedUncertain⇏UncertaintyGoverned`, `LoggedCovariance⇏CautionAtActuator`, `ConfidenceStatement⇏OperationalUncertainty` — plus a paired *uncertainty custody ≠ risk custody* non-equivalence clamp; Lean recognition handles sketched-not-built, absence is the intended state)
- Compressed ⇏ Authoritative (filed as working note [`projection-laundering.md`](projection-laundering.md) 2026-05-26; kernel-slot of the "compression-authority laundering" essay vocabulary in `working/compression-becomes-authority-vocabulary.md`; paired negative/positive theorem structure — `projection_launders_deferral` + `loss_aware_projection_blocks_deferral_laundering`; upstream composition partner to [[uncertainty-custody]]; Lean recognition handles sketched-not-built, absence is the intended state)
- (additional surface→substance pairs will likely surface; the table is open-ended)

**Same-day convergence note (2026-05-25):** the cluster produced two instances on the same day in two different layers (Lean kernel + spec note) within hours of each other, on top of the two pre-existing kernels. Claude-web flagged the convergence: *"that's not coincidence; that's the underlying object becoming visible because you finally have enough surface area to triangulate it."* ChatGPT applied the brake: *"refusal algebra is the negative-space structure underneath admissibility — not yet refusal calculus as a finished object."* Both correct. The operator family is real; the calculus claim is not yet earned.

### What "algebra" requires before it becomes "calculus"

A refusal *algebra* is operator-family recognition: enumerate the surface predicates that recur (fluency, signature, visibility, validity, survival, coherence, freshness, receipt shape), the substantive predicates they keep laundering into (settlement, witness standing, legitimacy, recovery, closure, authority, learning), and the structural relation that blocks each promotion.

A refusal *calculus* requires **composition** + **propagation** as theorems:

1. **Refusal composition.** If `A ⇏ B` and `B` is required as basis for `C`, then `A ⇏ C` for binding use. Currently a recognition observation; not a theorem.
2. **Refusal propagation.** A refusal over scope `S` propagates only to downstream claims whose basis depends on `S`. Currently a recognition observation; not a theorem.
3. **Refusal narrowing.** A refusal on use-kind `U₁` may license narrowed admission on use-kind `U₀` (advisory rather than binding, observe rather than authorize). Currently informal.
4. **Refusal repair.** A refusal may be revalidatable, scope-restrictable, time-restrictable, or contestable. Currently informal.

Until at least one of these is a theorem, this is algebra, not calculus. Same word, two different stages of work.

### Paper 28 — forcing-case candidate, NOT a draft authorization

Convergence-on-the-same-day made paper-Claude's smell change: P28 was previously round-number gravity; now there is a *possible forcing case*. The form a real P28 would need:

> Unify the annex refusal kernels as a typed family of blocked witness promotions, then show how refusal composes across basis, scope, standing, time, and use-kind.

The next evidence required is **composition**, not more examples. More examples are cheap; composition is the test of whether the algebra is a real algebra.

> *Do not write the paper yet. Capture the operator family, collect specimens, and watch for the first composition theorem to surface. Specimens are the appetizer; the composition theorem is the dish.*

## Versioning ladder on the shipped Admissibility Calculus

The shipped artifact (`~/git/lean/LeanProofs/Admissibility/CalculusOne.lean`, 1.0 as of 2026-05-24, patch 1.0.1 same day) is the positive admissibility path. The algebra/calculus distinction above maps onto its version semantics:

| Version | Shape | Earns its keep when |
|---|---|---|
| **1.0** *(shipped)* | Positive path: `basis → standing → authority → authorized transition → receipt / constraint`. Eight-module public surface; refusal-kernel annex compiled-not-promised. | (already shipped) |
| **1.x** | Documentation / coordination releases. Annex stays compiled-not-promised; README lifts refusal-kernel category into the headline (already done 2026-05-25). New refusal kernels land in the annex; no public-theorem promise change. | A reader needs to find the refusal kernels without spelunking; new specimens accumulate. |
| *(optional)* `RefusalKernels.lean` aggregator | Grouped annex import surface for refusal kernels, explicitly **non-CalculusOne**. Imports `RecoveryMargin` / `ClosureEligibility` / `ConsolidationDenial` / `SurfaceAuthorization` / `FiatAdmissibility` / etc. Annex semantics; non-public-promise. | Downstream code wants to cite "the refusal-kernel annex" without importing the constellation. |
| **2.0** | Public refusal-*calculus* surface. Composition / propagation / narrowing theorems on the `surface ⇏ substance` relation. NOT just more specimens; requires at least one theorem of the shape *if A cannot witness B and B is required as basis for C, then A cannot witness C for binding use.* | The composition theorem earns its shoes — see "What 'algebra' requires before it becomes 'calculus'" above. |

The discipline:

> **More specimens → annex / 1.x. Composition rules → calculus / 2.0.**

The cleaner one-liner (added to the keepers below):

> **A refusal kernel blocks one laundering move. A refusal calculus explains how blocked moves compose.**

Until at least one composition theorem lands, 2.0 is unauthorized; 1.x is welcome; the aggregator is optional and remains non-public-promise either way. Refusal kernels accumulate in the annex without needing a version bump.

Filed 2026-05-26 (tonight's pass).

## The keeper

> **A refusal does not negate reality. It negates standing.**

A witness saying *"I cannot testify to claim K over interval T"* does not assert that K is false. It asserts that this witness pool cannot carry K. The world-state remains whatever it is; what changes is whether this evidence base can be used to bind authority or action.

This is the NQ-shaped form. The Lean refusal kernel is the structurally-similar but layer-distinct form: a concrete countermodel where X holds and Y fails, breaking the inference *X therefore Y*.

## What can flow through the seam

Candidate bridge — not yet built or scheduled. The formal contract may be developed before a runtime target exists; the runtime receipt and enforcement pieces require their own concrete schemas and correspondence work:

1. **Lean refusal kernel** (e.g. `ConsolidationDenial`) — formalizes that *fluency does not witness settlement*.
2. **Witness refusal testimony** — a runtime witness emits `cannot_testify` for claim K over scope/time S because conditions invoked in the formal kernel obtain (system fluent but no settlement passes).
3. **NQ / preflight** — derives DENY (or REQUIRES_REVALIDATION / AMBIGUOUS / CANNOT_BIND) for any downstream claim that cited the now-inadmissible basis.
4. **Governor / Wicket** — refuses to mint authority or execute action requiring the denied basis. Receipt-bearing.

None of this composite bridge is built. The seam note exists to keep the layers distinct so the formal object, runtime receipt, and enforcement rule land at the right layers in whichever order the investigation establishes them.

### Logical correction — how the kernel plugs into runtime (DeepSeek's mis-rule, ChatGPT's repair)

DeepSeek proposed plugging the kernel into runtime as:

```lean
-- INCORRECT
if Fluent s then return RefusalStatus.CANNOT_TESTIFY
```

This is wrong. The theorem `fluency_does_not_witness_settlement` proves:

> *Fluency alone cannot witness settlement.*

It does NOT prove:

> *Any fluent system is unsettled.*

So the runtime rule must address the *basis offered*, not the surface predicate of the system:

```text
-- Correct shape:
if the basis offered for ClaimKind.audited_settlement
  is only of BasisKind.fluency_observation,
  for UseKind.binding_or_closure,
then RefusalStatus.CANNOT_TESTIFY
```

The runtime returns CANNOT_TESTIFY against *the basis*, not against *the system*. The system may be settled — it just can't *prove* settlement *from fluency*. Another witness pool (settlement-pass receipts, audit logs, etc.) could carry the claim; fluency alone cannot.

This correction generalizes:

> **Refusal kernels block specific surface→substance basis promotions. The runtime rule names the forbidden basis kind for the forbidden use, NOT a property of the system.**

A future fresh-context model will be very tempted to write the simpler "if fluent then refuse" rule. The simpler rule is wrong in the same way that mistaking the unconditional probability of an event for the conditional probability is wrong: it confuses *the observation* with *the basis being claimed from the observation*.

## Refusal is not binary — runtime algebra (parked, not built)

The Lean refusal kernel is the cleanest possible cut: *invalid witness move = blocked.* Pass / fail. That binary survives because the kernel is a formal countermodel — its only job is to break one inference.

The runtime side cannot afford that simplicity. *"Pass / fail"* collapses too many distinct non-pass states. Parking the multi-axis observation here so that a later formal model or concrete runtime integration does not have to re-derive the axes.

**The keeper that survives the multi-axis observation:**

> **Refusal is not a verdict on reality. It is a verdict on what a basis may authorize.**

That subsumes the layer-split keeper at the runtime layer. The Lean kernel breaks an inference; the runtime layer narrows what a basis may bind.

**The dimensional tuple** (NOT an authorization to type-encode):

```
(claim, basis, witness, scope, time, use_kind, consequence)
```

Refusal at runtime is then: *this basis cannot support this claim, for this use, over this scope/time, with this consequence.* All seven coordinates matter; reducing to fewer collapses real distinctions.

**Ten axes worth keeping warm** (one line each, recognition vocabulary only — most have existing partial coverage in NQ / Governor / Freshness / Standing / agent_gov / FiatAdmissibility / NumericalAdmissibility):

1. **Deny vs cannot-testify** — *cannot testify is not denial; it is basis absence.* DENY says the claim is inadmissible for this use; CANNOT_TESTIFY says this witness pool lacks standing/coverage/scope and another witness might carry it.
2. **False vs unsupported vs unearned** — three different monsters. *False* = contradicted by admissible evidence. *Unsupported* = no adequate basis. *Unearned* = basis exists but insufficient for this use-kind. A claim can be supported for display, unearned for closure, and false only if contradicted.
3. **Hard refusal vs degradation** — some refusals block the claim; others narrow what the claim may authorize. Binding → advisory, global → local, current → stale, causal → correlational, settled → provisional, authorized → requires-confirmation. Pass/fail is too stupid to live at this layer.
4. **Scope narrowing** — instead of rejection, narrowed admissibility. *"Resolver returned NXDOMAIN"* is admissible for resolver testimony at time T; not admissible as *"domain does not exist."* NQ already lives here.
5. **Temporal status** — fresh / stale / expired / not-yet-settled / pending-consolidation / decayed-beyond-recovery / requires-revalidation. Consolidation-denial plugs in here. *The claim may be syntactically intact but temporally unearned.*
6. **Conflict / ambiguity** — *conflict blocks binding before it proves falsehood.* Default is AMBIGUOUS / NON_BINDING / REQUIRES_RECONCILIATION / DEGRADE_TO_ADVISORY, not automatic DENY. Otherwise the first conflict becomes a veto machine.
7. **Contestability state** — contestable / revalidatable / permanently-barred / barred-for-this-interval / barred-until-new-witness / barred-until-authority-changes. A refusal without a repair path becomes bureaucracy cosplay.
8. **Consequence tier (use-kind axis)** — same claim, different required standard. Observe / summarize / recommend / authorize / mutate-or-execute / close-or-settle. *A claim can be admissible to observe and inadmissible to bind.* This is the SurfaceAuthorization / FiatAdmissibility pattern lifted to runtime; the kernel already has the formal version.
9. **Provenance contamination** — self-certified / derived-from-refused-basis / depends-on-stale-parent / compressed-from-unreviewed-residue / generated-during-consolidation-denial. The claim-graph seam; not yet operationalized.
10. **Receipt vs lock** — *A refusal receipt is evidence. A lockout is a consequence.* The refusal receipt records that basis failed; the lockout prevents downstream use; the propagation rule decides whether dependents are denied / degraded / stalled / requires-revalidation. Do NOT merge these three. This is the runtime equivalent of the Lean/runtime layer split itself.

**Candidate verdict enum** (parked, NOT a type spec):

```
ALLOW
ALLOW_NARROWED
ADVISORY_ONLY
CANNOT_TESTIFY
INSUFFICIENT_BASIS
CONFLICTING_TESTIMONY
STALE
REQUIRES_REVALIDATION
DENY_FOR_BINDING_USE
HARD_DENY
```

The enum is illustrative. The real algebra is the *tuple*, not the verdict; the verdict is a projection of the tuple under policy. Do not commit a runtime API to the enum until a concrete policy projection determines its shape. A bounded formal model may explore the tuple first.

**Cross-axis observations to preserve:**
- Axes 1, 5, 6, 10 are operational; axes 2, 8, 9 are graph/lineage; axis 7 is governance. Mixing them in one verdict type collapses dimensions.
- Most coverage already exists somewhere in the kernel stack (Freshness for axis 5, FiatAdmissibility / NumericalAdmissibility for axis 8, agent_gov for axis 7). The runtime side will mostly assemble existing primitives, not mint new ones.
- The new thing is the *tuple addressing*, not the verdicts.

## Conflict ≠ lockout (sub-distinction)

Two witnesses disagreeing usually produces:

- `BASIS_AMBIGUOUS`
- `CONFLICTING_TESTIMONY`
- `REQUIRES_RECONCILIATION`
- `CANNOT_BIND` (for the current step)

— not necessarily "both witnesses locked out." A hard lock is a *policy consequence* when conflict over claim kind K is configured to prevent binding; it is not the default outcome of disagreement. Don't model conflict-as-default-lock; that would smuggle a policy choice into the seam.

## Non-promotion guard

- Do NOT call the runtime object a "refusal kernel." That name belongs to the Lean annex pattern.
- Do NOT ship `RefusalReceipt` (or analogous) as a standalone runtime type yet: no concrete policy projection or integration target fixes its semantics. That is an implementation/promotion constraint, not a ban on formalizing the contract first.
- Do NOT add a Lean kernel for the runtime side. The Lean side blocks formal inferences; the runtime side blocks operational basis-use and properly lives across multiple tools.
- Do NOT treat the witness emitting refusal as making a claim about *reality*. The witness makes a claim about *its own standing to testify*.

## Runtime filing and promotion gate

A runtime "refusal receipt" / "admissibility lockout" / similar earns a name and a filing when:

1. A real NQ / libwitness / Governor integration produces refusal testimony that downstream code must consume.
2. The consumer cannot use existing primitives (Governor denial verdicts, NQ preflight outcomes, agent_gov authority gates, etc.) to express the shape — i.e. the shape is genuinely missing.
3. The shape is sharp enough to encode at the type level (libwitness shape addition, NQ verdict refinement, Governor receipt-schema extension).

Until then: this is a seam note, not a runtime build target. Formal theorem work remains independently admissible on its model, theorem-shape, overlap, and proof merits.

## Cross-references

- [`consolidation-denial.md`](consolidation-denial.md) — the refusal kernel whose landing prompted the layer-clarification.
- `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` (sibling `RecoveryMargin.lean`, `ClosureEligibility.lean`) — formal refusal kernel instances.
- `~/git/lean/LeanProofs/Admissibility/README.md` — the architectural-summary callout naming the refusal-kernel category at the formal-annex layer.
- `~/git/agent_gov/` — Governor / Wicket; runtime enforcement layer (where binding locks / denial receipts would land if/when they earn a name).
- `~/git/nq/` — claim preflight; admissibility-consequence layer.
- (libwitness — refusal testimony shape would live here if/when it earns a name; pointer pending a stable libwitness location.)
- `[[project-laundering-move-watchlist]]` — sibling attack-surface inventory; refusal kernels are the layer-1 locks against named laundering moves.
- `[[feedback-kernel-overlap-audit]]` — the audit pattern this seam note exists to support; *fresh-context audits surface category-membership gaps that kernel-aware audits self-censor*, and this seam note is what those audits will read first.

## Provenance

- **Layer-jump caught:** Claude-web, 2026-05-25 — read "refusal kernel" as "first formal refusal primitive / runtime counter-witness lock" / "kernel that gives admissibility check something to do."
- **Correction:** ChatGPT, same day — refusal kernel is the Lean annex category (formal countermodel); runtime analogue is a refusal receipt / admissibility lockout / similar, not the same object. Two layers, two names.
- **Filing recommendation:** ChatGPT — capture as seam note, do not promote, name the bridge so future fresh-context audits don't have to re-derive it.
- **Filed:** claude-code, 2026-05-25, after operator brought the multi-model relay forward with the framing *"name the seam, don't build the plant."*

The capture is worthwhile because the distinction prevents future category collapse, and the future fresh-context audit is the most likely place where the collapse would happen.

## Provenance — additional passes (2026-05-25)

- **DeepSeek (LLM-agent application + Lean signature sketch):** unpacked the kernel into LLM-agent design implications ("fluency trap," "fluency theater," `Nightshift` as structural requirement); proposed a `Runtime.Refusal` Lean module with `AdmissibilityQuery → RefusalStatus`. Useful prose; the proposed runtime module is NOT authorized — see ChatGPT's brake.
- **ChatGPT (logical correction + category brake):** caught DeepSeek's mis-rule (`if fluent → CANNOT_TESTIFY` is wrong — runtime refuses *the basis*, not the system). Named *refusal calculus* as the better category. Counseled: do NOT write the Lean module; do NOT commit to the enum; *enum-first design is how you summon a taxonomy demon.*
- **Claude-web (operator-family triangulation):** noticed that two same-day filings (Fluent⇏Settled in Lean kernel, Signed⇏Witnessed in spec) plus two pre-existing kernels (VisibleGreen⇏RecoveryMargin, Survival⇏ClosureEligibility) constitute four instances of one operator family; flagged the convergence as the underlying object becoming visible. Named *paper 28 was waiting.*
- **ChatGPT (brake on the P28 move):** *"Refusal algebra is the negative-space structure underneath admissibility — not yet refusal calculus as a finished object."* P28 needs composition + propagation theorems, not more examples. Smell changed from "round-number gravity" to "possible forcing case"; not yet a draft authorization.

## Companion reference

Prior-art citation stack (eight neighboring fields) + application zones (seven domains where the operator family already lives) + connection to the laundering-move watchlist as anti-laundering grammar live in [`refusal-algebra-prior-art-and-applications.md`](refusal-algebra-prior-art-and-applications.md). Filed 2026-05-25 ahead of the operator's planning pass; reference material, not promoted.

## Keepers (compact stack)

> **Formal refusal blocks an inference. Runtime refusal blocks use of a basis.**

> **The kernel blocks the move; the runtime negotiates the landing.**

> **A refusal does not negate reality. It negates standing.**

> **Refusal is not a verdict on reality. It is a verdict on what a basis may authorize.**

> **Admissibility tells you what can bind. Refusal tells you why something that looks bindable cannot.**

> **Refusal is the algebra of failed witness promotion.**

> **Refusal calculus is how a system preserves weaker truth without letting it impersonate stronger authority.**

> **A refusal kernel blocks one laundering move. A refusal calculus explains how blocked moves compose.**

The first three are layer-split keepers. The next two are structural keepers. The sixth is the operator-family handle. The seventh subsumes the layer split, the operator family, and the application story in one sentence; if only one survives long-term, it is probably that one. The eighth (added 2026-05-26) is the version-ladder discipline keeper — the sentence that decides what does and does not earn the word *calculus* on the shipped artifact.
