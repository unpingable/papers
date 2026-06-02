# Maximal-calculus — codex adversarial review log

**Status:** Agent-maintained log, seeded 2026-06-02. Per
[`/home/jbeck/.claude/plans/cheeky-plotting-reef.md`](../../.claude/plans/cheeky-plotting-reef.md):
each Lean milestone of `LeanProofs/Admissibility/MaximalCalculus.lean`
(scratch annex in `~/git/lean`) gets a `codex exec` adversarial review
pass before the next milestone begins. Findings are tagged ACCEPT /
REJECT / DEFER (operator) with a one-line reason and (where applicable)
the integration that followed.

## Conventions

- **ACCEPT** — agent constructed the laundering example or confirmed
  the missing hypothesis is silent; fix applied this iteration.
- **REJECT (reason)** — agent disagrees, with reason. Often "lifted to
  type" (the constraint is intentionally environmental in the same way
  the fragment uses) or "misreads the boundary."
- **DEFER (operator: <decision>)** — finding implicates a refused
  decision, the keystone choice, or absorption of another register
  case. Surfaces to operator-decision queue at end of file.

Lean module SHA recorded after each milestone for reproducibility.

**Closeout note (2026-06-02).** The Lean file referenced throughout
this log was originally drafted at
`LeanProofs/Admissibility/MaximalCalculus.lean` with namespace
`Admissibility.MaximalCalculus` and env type `MaxCalcEnv`. After the
D.4 outside-aperture audit concluded the artifact is an "amendment
fragment of [a maximal calculus], not a maximal calculus," the
operator directed a rename. The file now lives at
`LeanProofs/Admissibility/AmendmentFragment.lean` with namespace
`Admissibility.AmendmentFragment` and env type `AmendmentEnv`.
Verbatim codex outputs in entries below preserve the original
names as historical record; the artifact at the cited locations
should be read against the renamed file.

---

## 2026-06-02 Milestone A.1: Types only (State, MaxCalcEnv, AuthEvidence)

**Lean module SHA before review:** `0e7ca7e5d13dfd928d8d505c22fde022716ea77c0261e2273265425f19eaa69a`
**Build status:** `lake build` green; standalone `lake env lean` exit 0.
**Codex invocation:** `codex exec -c approval_policy="never" --sandbox read-only --skip-git-repo-check --cd /home/jbeck/git/lean` (model: gpt-5.5, session 019e88e1-66c1-7802-9198-4390d6762512).

### Codex output (verbatim)

1. **Policy is not actually in state alone.** `State` stores only a `Policy` value. The authorization relation still lives in `MaxCalcEnv.Validates`. So the header's "policy lives in State, not env" is only true for the policy token, not for the policy semantics.

2. **`AuthEvidence` is just an abbrev to `Prop`.** There is no opaque evidence type indexed by policy. After unfolding, evidence is exactly `E.Validates p o`. Any available implication, equivalence, or equality transport can manufacture `AuthEvidence E p o` from `AuthEvidence E p' o`.

3. **The no-coercion claim is overstated.** Lean will not implicitly coerce `AuthEvidence E p' o` to `AuthEvidence E p o`, but explicit transport along `h : p' = p` works. Also if `Validates` ignores `p`, evidence at different policies may reduce to the same proposition.

4. **A1 is not yet carried by the types.** There is no transition type, no pre-state argument, and no slot requiring `AuthEvidence E s.policy o`. The current layer only makes such a future slot possible; it does not encode "valid in `S`, not introduced by `S'`."

5. **Fixed-value collapse is allowed.** Nothing prevents `applyOp` from preserving policy or `Validates` from ignoring policy. The specimen therefore admits the fixed-value/environmental regime as an instance; the "maximal calculus" distinction is not enforced at this milestone.

### Agent verdict per finding

- **Finding 1: ACCEPT (header precision).** True. State carries the policy *value*; env carries the `Validates` *grammar*. Fix header: don't claim "policy lives in state, not env" — say "current policy value in state; judgment grammar (`Validates`) in env, indexed by policy." Structural parallel to the fragment: there `Allowed` is environmental too; what makes A1 hold is the *type-level binding of the policy argument to the source state*, which lands in A.2.
- **Finding 2: ACCEPT-with-narrowing.** True at the abstract spec layer: `MaxCalcEnv` does not force `Validates` to depend on its `Policy` argument. A degenerate env (`fun _ o => …`) makes the policy index vacuous. Per `feedback-narrow-construction-on-failure`, do NOT add a policy-sensitivity axiom to the env — narrow the statement instead: the (A1) discipline is conditional on the env actually using its policy argument; degenerate envs make A1 vacuous but not violated. Document this in a §"What this milestone does not yet enforce" block.
- **Finding 3: ACCEPT (docstring precision).** True. Equality transport is universal across indexed propositions. Tighten `AuthEvidence` doc: "no *implicit* coercion across policy indices" instead of "is not a value of."
- **Finding 4: ACCEPT (intent — this is what A.1 is scoped to).** Correct observation; intentional scope. A.1 = scaffolding; A.2 = (A1) at transition signature. Add an explicit "what A.2 will add" forward reference to the header so a reader doesn't mistake this milestone for the keystone.
- **Finding 5: ACCEPT (subsumption, not collision).** True and intended. The fragment is the *special case* where `applyOp` preserves `s.policy`. Maximal calculus *generalizes* fragment; it should subsume it, not refuse it. Codex's framing implies bug; I disagree on framing but accept the observation. Add note in the doesn't-yet-enforce block: fragment regime is a permitted instance, not a leak.

### Integration

Apply five header/docstring edits (see next file revision); add a §"What this milestone does not yet enforce" block listing (A1 at transition signature — A.2), (policy-sensitivity is env-author's contract, not enforced by spec), (fragment-as-special-case). Re-run `lake build`.

## 2026-06-02 Milestone A.2: Transition with evidence at S.policy

**Lean module SHA after milestone:** `9e8c19026c62716950fa35b16c8bf458160a2ea081f4eda265eb067b012dbe8c`
**Build status:** standalone compile exit 0; `lake build` not yet re-run (no annex import).

### Codex output (verbatim)

1. **No direct type-level laundering path found.** `Transition E S` has only `op` and `evidence : E.Validates S.policy op`; `destination` and `postPolicy` are projections computed after construction. Anonymous constructors, dot notation, and projections do not add another construction route.

2. **`applyOp` cannot forge evidence by itself.** It can compute a post-state whose policy authorizes `op`, but that value is not accepted in the `evidence` field unless it also proves `E.Validates S.policy op`.

3. **Equality transport is not a structural leak.** If `S.policy = (E.applyOp S op).policy`, then evidence can be transported between source and post policy. That is a fixed-point/propositional-equality case, not laundering across distinct policies. If the policies are genuinely unequal, Lean will not coerce post-policy evidence into source-policy evidence.

4. **No implicit-instance forge path appears.** There are no typeclass arguments, coercions, or instance-resolved fields in `AuthEvidence`, `Transition`, `destination`, or `postPolicy`. The only hidden arguments are ordinary universe/type/state parameters inferred from `E` and `S`.

5. **Header-vs-type drift: universe generality.** The specimen says policies and operations are arbitrary types, but the declarations use `(Policy Op : Type)` rather than universe-polymorphic `(Policy : Type u) (Op : Type v)`. That is not an A1 laundering hole, but it is a formal generality gap.

Codex's bottom line: *"for distinct S.policy and t.postPolicy, a Transition E S cannot be built from post-state-only authority unless the environment itself supplies a way to derive source-policy validity."*

### Agent verdict per finding

- **Finding 1: AFFIRMS (no action).** Codex actively confirmed (A1) holds at the type level. Log for record.
- **Finding 2: AFFIRMS (no action).** Codex confirms `applyOp` is not an evidence-forging path. Log.
- **Finding 3: AFFIRMS (no action).** Codex confirms equality transport at `S.policy = postPolicy` is the vacuous/fixed-point case, not laundering. Log.
- **Finding 4: AFFIRMS (no action).** Codex confirms no implicit-instance forge path. Log.
- **Finding 5: REJECT (style consistency).** Universe polymorphism not a (A1) issue; `SafetyBridge.SafetyEnv` and all sibling modules in `LeanProofs/Admissibility/` use monomorphic `Type`. Changing here alone creates inconsistency. Per YAGNI: no universe machinery without forcing case. If a polymorphic instance ever shows up downstream, both this specimen and the fragment will lift together.

### Integration

None — codex's review is structurally clean. Caveat-finding 5 rejected with reasoning above. Module unchanged after the codex pass.

## 2026-06-02 Milestone A.3: WellFoundedAmendment predicate + necessity lemma

**Build status:** standalone compile exit 0.

### Codex output (verbatim)

1. `WellFoundedAmendment t := E.Validates S.policy t.op` is the right phrasing for pre-state evidence. It does not conflate with post-state policy. `E.Validates t.postPolicy t.op` cannot prove it by unfolding alone; it needs an equality/path showing `t.postPolicy = S.policy`, or a degenerate `Validates` insensitive to policy. That is not a laundering bug in this definition.

2. The predicate is ceremony logically, but useful interface ceremony. Deleting it loses a named theorem target matching the prose/spec altitude. Without it, later statements must expose raw `E.Validates S.policy t.op`, making the A1 concept less stable under refactors and harder to cite.

3. `transition_is_well_founded` does not overclaim. There is no `t : Transition E S` for which `WellFoundedAmendment t` can fail, because the structure field is exactly `t.evidence : AuthEvidence E S.policy t.op`, definitionally `E.Validates S.policy t.op`.

4. **Header/type drift:** the block says "well-foundedness is necessary and constructively sufficient." This theorem only proves necessity for an existing `Transition`. Constructive sufficiency requires a constructor lemma from `E.Validates S.policy o` to `Transition E S`, which is available by structure construction but not stated here. The prose slightly outruns the block's actual exported theorem.

5. **Load-bearing caveat:** because `AuthEvidence` is an `abbrev` to `Prop`, proof irrelevance and definitional transparency are fine here, but the model has no way to distinguish "witness produced before transition" from "same proposition proved after looking at the post-state." A1 is enforced only as policy-indexed validity at `S.policy`, not temporal provenance of the proof term.

### Agent verdict per finding

- **Finding 1: AFFIRMS (no action).** Phrasing correct.
- **Finding 2: AFFIRMS (defended ceremony).** Codex confirms predicate is useful interface anchor for later theorems.
- **Finding 3: AFFIRMS (no action).** No overclaim.
- **Finding 4: ACCEPT.** Genuine prose-outruns-export gap. Added `authorized_yields_transition` theorem proving constructive sufficiency from `E.Validates S.policy op` to `∃ t : Transition E S, t.op = op`.
- **Finding 5: ACCEPT (honest disclosure).** Deep correct point. Added §"Policy-index discipline, not temporal provenance" block explicitly noting: A1 is policy-index, not temporal-provenance; temporal-provenance lives at the protocol layer (receipt-gated `(O₁ → wait → O₂)` patterns from amendment-cut.md §"Case B"), outside the kernel's scope. Matches fragment's `AuthStep E s` semantics.

### Integration

Two adds: `authorized_yields_transition` theorem, §"Policy-index discipline, not temporal provenance" documentation block. Module recompiles standalone exit 0.

## 2026-06-02 Milestone A.4: Case #3 negative theorem

**Build status:** standalone compile exit 0.

### Codex output (verbatim)

1. **Broader than case #3 — acceptable.** Theorem subsumes the self-certifying shape. To pin case #3 explicitly, add a corollary with the unused-premise pattern:
   ```lean
   E.Validates (E.applyOp S op).policy op →
   ¬ E.Validates S.policy op →
   ¬ ∃ t : Transition E S, t.op = op
   ```
2. **No laundering through `t' : Transition E S'`.** Existential is fixed at `Transition E S`; a transition from a different source is the wrong type.
3. **Proof is clean.** Ordinary equality transport via `hop ▸ t.evidence`. No `applyOp`/`destination`/`postPolicy` consulted; no post-state authorization smuggled.
4. **Header drift.** §"What this milestone does not yet enforce" is stale — A.2 and A.4 now enforce the laundering refusal it disclaimed. Tighten or retitle.
5. **Persistent caveat (policy-index, not temporal-provenance, not non-vacuity).** Already disclosed in current header; theorem relies on that boundary.

### Agent verdict per finding

- **Finding 1: ACCEPT.** Added `case3_self_certifying_inadmissible` corollary with the unused-premise pattern (underscore-prefixed `_hpost` to mark intentional disuse). Case #3 is now visible at the API.
- **Finding 2: AFFIRMS (no action).**
- **Finding 3: AFFIRMS (no action).**
- **Finding 4: ACCEPT.** Retitled to "Persistent kernel-level caveats (post-A.4)"; dropped item 1 (A1-at-signature, now enforced); kept items 2–3 (policy-sensitivity contract, fragment-as-special-case); added new item 3 (policy-index vs temporal provenance, cross-referencing the dedicated block).
- **Finding 5: AFFIRMS (already disclosed).**

### Integration

Two edits: case-#3 corollary added; "Persistent kernel-level caveats" block retitled and items refreshed. Module recompiles standalone exit 0.

## 2026-06-02 Milestone A.5: Standing specimen + case-#4 positive + case-#3 instantiated

**Build status:** standalone compile exit 0. First-pass build error caught: `theorem` for a `Type`-valued result; corrected to `def`.

### Codex output (verbatim)

1. **Genuinely maximal, not fixed-value.** `standingApplyOp` changes `State.policy` by extending `hasStanding`. Unless `B` already had standing, post-policy differs. Exercises policy mutation; not the fixed-value fragment.
2. **Case #4 positive is intentionally constructor-shaped.** Not a deep theorem but not a tautology — the real obligation is exactly the `evidence` field, reducing to `S.policy.hasStanding A`. Proof term `hA` is pre-state standing. Intended kernel shape.
3. **Case #3 negative is properly kernel-level.** `case3_self_grant_inadmissible` is an instantiation of `no_transition_without_pre_authorization`, but that lemma *is* the case-#3 work. The specimen test is whether concrete self-grant reduces to missing pre-standing for `B`; it does.
4. **Honesty gap: strict growth is only prose.** Doc says post-state policy is "strictly larger," but the def/theorem doesn't require `¬ S.policy.hasStanding B`. If `B` already has standing, policy may be extensionally unchanged. Doesn't break A1 or case #4 admissibility, but the claim is not proven.
5. **Post-authorization case #3 not exhibited in concrete theorem.** Generic `case3_self_certifying_inadmissible` includes `_hpost`. Concrete `case3_self_grant_inadmissible` omits the fact that after `grant B B`, `B` would have standing. That fact is definitionally provable and would make the specimen visibly match the full case-#3 shape.

### Agent verdict per finding

- **Finding 1: AFFIRMS (no action).** Codex confirms specimen exercises maximal regime.
- **Finding 2: AFFIRMS (no action).** Codex confirms case-#4 is real kernel obligation.
- **Finding 3: AFFIRMS (no action).** Codex confirms case-#3 kernel-level mapping.
- **Finding 4: ACCEPT (narrow the prose).** Softened "strictly larger" to "may differ from S.policy" with conditional "(strict growth holds when ¬ S.policy.hasStanding B)." Honest disclosure that the load-bearing fact is *witness in pre-state*, not strict growth.
- **Finding 5: ACCEPT (full case-#3 shape).** Added two theorems: `case3_post_state_would_validate` exhibiting the post-state witness via `Or.inr rfl`, and `case3_self_grant_full_shape_inadmissible` instantiating the generic `case3_self_certifying_inadmissible` with both hypotheses present. Specimen now visibly matches the full case-#3 shape.

### Integration

Three additions to `StandingSpecimen`: prose tightening, `case3_post_state_would_validate`, `case3_self_grant_full_shape_inadmissible`. Module recompiles standalone exit 0.

## 2026-06-02 Milestone A.6: Founding transitions (describable, non-blessable)

**Build status:** standalone compile exit 0; `lake build` green (8305 jobs).

### Codex output (verbatim)

1. **`founding_does_not_bless` is weaker than its prose.** `_f : FoundingTransition Policy Op S` is independent of `{op}`. The theorem states some separately chosen `op` is non-blessable while an arbitrary founding record is present. Prefer making `op := f.op`.
2. **`FoundingTransition` is disjoint from `Transition` only as a different structure type, not semantically.** Lean gives no default coercion path here; the type-level boundary is real in the narrow sense. But the same `op` can inhabit both records if external pre-state evidence exists. Prose should avoid "disjoint" unless qualified as "no constructor/projection/coercion from founding data alone."
3. **`founding_is_describable` is intentionally trivial, and that's enough.** It only describes `(op, newPolicy)` syntactically. It does not say `newPolicy = (E.applyOp S op).policy`, because `FoundingTransition` has no `E`. If "follows" means operational arrival under an environment, the type is under-specified.
4. **Unused founding parameter is honest documentation, but the current shape makes it look more load-bearing than it is.** With the fix in finding 1, the unusedness becomes defensible: the founding record selects the operation, but contributes no evidence. As written, `_f` does not even select the operation.
5. **Header drift: update the caveat marker.** "Persistent kernel-level caveats (post-A.4)" is stale for an A.6 specimen. Also add the founding caveat: founding events are representable outside `Transition`, but the kernel proves only non-blessability under failed pre-authorization, not historical occurrence or semantic arrival.

### Agent verdict per finding

- **Finding 1: ACCEPT.** Tightened signature: `f : FoundingTransition Policy Op S` named (not `_f`), `op` removed from explicit args, theorem now binds the op via `f.op`. The founding now genuinely selects the op.
- **Finding 2: ACCEPT (prose qualification).** Replaced "Disjoint from `Transition`" with explicit "Boundary qualification" block noting same `op` can cohabit both records given external evidence; what is structurally disjoint is the *constructor route*.
- **Finding 3: ACCEPT (under-specification disclosure).** Added "Operational under-specification" block to `FoundingTransition` docstring: `newPolicy` not constrained to equal `(E.applyOp S op).policy`; `FoundingTransition` has no env by design; foundings are meta-environment events.
- **Finding 4: ACCEPT (subsumed by Finding 1 fix).** After Finding 1, the unused-`f` pattern becomes defensible — the founding contributes its op, not evidence.
- **Finding 5: ACCEPT.** Retitled to "Persistent kernel-level caveats (post-A.6)"; added item 4 on founding events.

### Integration

Four substantive edits: tightened `founding_does_not_bless` signature; added "Boundary qualification" + "Operational under-specification" blocks to `FoundingTransition` doc; retitled and extended the caveats block; updated the prose around `founding_does_not_bless`. Full `lake build` green (8305 jobs, identical to baseline — no annex bleed).

## 2026-06-02 Phase D.4: Final outside-aperture audit

**Bundle sent to codex:** kernel module + `maximal-calculus-discharge-connection.md` + `maximal-calculus-founding-events.md` + `maximal-calculus-case4-instantiation.md`. Question asked without leading: *"Is this a maximal calculus, or only the amendment fragment of one? Name what it does not cover."*

### Codex verdict (verbatim)

> **It is not a maximal calculus. It is the amendment fragment of one.**
>
> 1. It covers one structural axiom: an operation that changes authority must be authorized by the source policy, not by the authority it installs.
> 2. It does not cover value mutation as such: changes to what counts, what is owed, what is discharged, what is ranked, or what value-function governs later judgment.
> 3. It does not cover retroactive legitimation generally: later admissibility, acceptance, receipt, discharge, or adoption rewriting the status of an earlier act.
> 4. It does not cover multi-step protocol structure: pending states, valid waits, receipts, issuer authority, observation, acceptance windows, or future-witness discipline.
> 5. It does not cover exceptional substitution or origin problems: crisis authority replacing ordinary authority, reflective adoption being mistaken for origin legitimation, or foundings as historical occurrences rather than merely describable non-blessable records.
>
> So the kernel is a clean source-authorization gate for amendments. It is not yet the maximal calculus, because maximal altitude needs the surrounding shapes where authority, value, time, receipt, exception, and origin can all be mutated or laundered.

### Agent posture

**No action.** Per `feedback-outside-aperture-audit` and the plan's D.4 stop condition, this audit is operator territory. The agent's job here is to surface — not to ratify, reject, or integrate. Filed for operator decision.

Cross-mapping to the register (for operator's convenience, NOT a verdict):

- Codex's item 2 (value mutation) ≈ register case #1 (value-function amendment).
- Codex's item 3 (retroactive legitimation) ≈ register case #2 (retroactive legitimation) + case #6 (reflective adoption).
- Codex's item 4 (multi-step protocol) ≈ the open question filed in `maximal-calculus-discharge-connection.md` §"Open question: what is a valid wait?".
- Codex's item 5 ≈ register case #5 (crisis substitution) + the founding-events question filed in `maximal-calculus-founding-events.md` §"Adjacent shape" (whether founding is reflective adoption at the constitutional layer).
- Codex's "foundings as historical occurrences rather than merely describable non-blessable records" is a *doctrinal* claim that differs from amendment-cut.md §"The distinguished failure," which holds describable-not-blessable is the correct boundary. Operator owns this disagreement.

The agent's autonomous run completes here. All four next moves from amendment-cut.md §"Next moves" have been carried as far as the plan's stop conditions allow:

- **A. Kernel specimen of well-foundedness** — DONE (Phase A.1–A.6, six milestones, six codex passes integrated).
- **B. Discharge-connection note** — DONE (Phase C.1).
- **C. Founding-event handling note** — DONE (Phase C.2).
- **D. Case #4 instantiation test** — DONE (Phase D, PASS with explicit narrowness disclaimers).

The outside-aperture audit above is the agent's last act; it surfaces what the operator decides next.

## Operator-decision queue

Surfaced for operator review at end-of-run:

1. **Ratify or revise the well-foundedness condition as keystone.** The Phase-A kernel and Phase-D case-#4 PASS are evidence; the question of whether the condition is *the* keystone vs. *a* candidate among several is operator-only per amendment-cut.md §"What this note does NOT do."
2. **Doctrinal disagreement with codex on foundings.** Codex's outside-aperture item 5 treats describable-not-blessable as under-coverage; amendment-cut.md treats it as the correct boundary. Operator decides.
3. **Whether the maximal calculus is one paper or several.** Codex's verdict (kernel is "the amendment fragment of one") gives independent surface evidence that the calculus is plural; the register's refusal still stands.
4. **Discharge essay promotion path.** `maximal-calculus-discharge-connection.md` cross-references the discharge essay candidate; whether the formal cousin should be folded in or kept sibling is operator-only.
5. **Title and naming.** Per `project-paper-naming-stack`, the *An Admissibility Calculus* slot remains reserved; no naming was attempted.
6. **The "valid wait" question** (filed open in C.1). What counts as the receipt-gated middle term `(O₁ → wait → O₂)`? Codex's outside-aperture finding 4 confirms this is genuinely outside the kernel; whether it earns a Lean shape, a paper shape, or a doctrine note is operator-only.

