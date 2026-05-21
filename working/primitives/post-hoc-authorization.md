# Post-Hoc Authorization Laundering

**Status:** candidate
**Kind:** Boundary condition
**Originated:** 2026-05-20 (eight-slice brainstorm + audit; named pattern, not new kernel)
**Primary home:** no paper yet — operational pattern with downstream Wicket / Agent Governor fixture potential

## Keeper

> **Lucky is not authorized.**

Adjacent lines:

> Success after the fact cannot mint prior authority.

> **No transition may smuggle its warrant backward from the state it creates.** *(Formal/transition-system register, added 2026-05-21 from a Federalist-Papers riff with ChatGPT + DeepSeek. The anti-time-travel rule for authority: the witness authorizing S → S′ must already be valid in S, not created by S′.)*

## Failure shape

```
action executes successfully
  ↓  (success observation)
success treated as evidence of safety
  ↓  (safety inference)
safety treated as evidence of authorization
  ↓  (authorization inference)
missing prior standing is erased
```

The inference chain is operationally ubiquitous — it produces most incidents that nobody gets blamed for, because the chained success bound the inference together. The chain is its own immunity from review.

## Failure predicate

Post-hoc authorization laundering occurs when:

- An action $a$ executed at time $t$ produced an observable success outcome at $t' > t$, **and**
- At $t$, no admissible basis existed for $a$ under the relevant authority kernel, **and**
- After $t'$, the success outcome is invoked as evidence that authorization was present at $t$.

The error is *temporal direction*: post-$t'$ outcome evidence is being used to claim pre-$t$ authority. Outcome surfaces do not testify backward across causality.

## Decision branches (transition-system shape)

For a candidate transition $S \to S'$ whose authorization is being evaluated:

| Branch | Verdict | Reading |
|---|---|---|
| Witness already valid in $S$ | **Allowed** | *"This rule existed before the change and permits this change."* The standard case. |
| Witness created by $S'$ | **Denied** (backward smuggling) | *"After the change, there will be a rule saying the change was permitted."* The post-hoc authorization core case. |
| Witness *is* the transition artifact | **Denied** (self-validating transition) | *"The artifact produced by the transition is also the proof that the transition had authority."* A specific sub-case of backward smuggling where the change and its warrant are the same object. |
| Witness valid in $S$ but only because it is entrenched against renewal | **Suspicious / deferred** | *"The old rule permits this, but only because it has outlived the substrate that justified it."* Handoff to [[stale-binding]] / [[project-commitment-standing-decay]] — the witness *is* in $S$ (so this is not post-hoc smuggling), but its presence in $S$ is itself a separate admissibility question. |

The fourth branch is the load-bearing one for cases where Post-Hoc Authorization isn't quite the right diagnosis but the transition still smells wrong. The first three are temporal-direction failures (warrant flow from future-state back to past-state); the fourth is a temporal-persistence failure (warrant flow from past-state into present-state without renewal) — Post-Hoc's sibling on the temporal-authority axis, not Post-Hoc itself.

## Do not collapse: self-certification vs. self-entrenchment

The second and fourth branches above describe different errors and should not be conflated, even though both can produce *"this transition smells unauthorized"* reactions.

**Self-certification** is when the proposed authority validates itself:

> *This transition is authorized because the state produced by the transition says it was authorized.*

This is the canonical Post-Hoc Authorization case (branch 2). The witness for $S \to S'$ exists in $S'$ but not in $S$. The transition is its own warrant.

**Self-entrenchment** is when existing authority protects itself from revision:

> *This rule was already valid in $S$, and it constrains future changes to itself.*

This is branch 4. The witness genuinely is in $S$ — self-entrenchment is *not* post-hoc authorization. The error (when there is one) is in a different layer: stale-basis authority, foreclosed renewal, [[project-commitment-standing-decay]]. Self-entrenchment may be **formally valid** while still raising serious admissibility concerns about whether the entrenched basis still tracks present substrate.

The distinction matters because the *countermeasure* is different. Self-certification refuses at the transition gate (Post-Hoc verdict; CollapsedSurface + SurfaceAuthorization machinery already handles it). Self-entrenchment refuses upstream of the transition, by asking whether the entrenched rule still has authority over present conditions — a renewal question, not a witness-time-direction question.

Worked example of self-entrenchment that is *not* Post-Hoc: U.S. Constitution Article V's equal-Senate-suffrage clause — the rule blocks its own modification absent state consent. The witness predates any candidate transition; the question is whether the entrenched witness still has standing, not whether it's been backward-smuggled. Wrong tool: Post-Hoc verdict. Right tool: stale-basis / renewal-failure audit.

## Verdict naming

Operator-language: **lucky is not authorized**.

Kernel-shaped verdict name: **`POST_HOC_AUTHORIZATION_DENIED`** — the receipt that *should* be emitted for this pattern.

Less precise but human-friendlier: `UNAUTHORIZED_SUCCESS`. Both valid in different registers; the verdict name is the kernel-shaped one because it names the *refusal*, not the *outcome*.

## Kernel backing — NOT a new module

This pattern is **already covered structurally** by the existing kernel. It does not earn a new Lean module:

- **`LeanProofs/CollapsedSurface.lean`** — proves *"a collapsed surface identifies no cause."* The observed surface *action succeeded* collapses across distinct causes (authorized + competent / unauthorized + lucky). The cause is not identified from the success surface alone.
- **`LeanProofs/Admissibility/SurfaceAuthorization.lean`** — keeper: *"A collapsed surface may authorize inquiry. It may not authorize attribution."* Post-hoc authorization laundering is precisely the failure mode where the collapsed success surface is used to retroactively attribute the *authorization* cause.

The pattern is the *temporal-direction* specimen of the surface-vs-attribution kernel result. The kernel already proves the refusal; what was missing was the *named pattern* in the field notebook.

> **DO NOT BUILD `Admissibility/PostHocAuthorization.lean`.** Per the gate stack: the kernel theorem exists, the failure predicate is named here, the fixture work belongs in Wicket/AG. No new module is earned.

## Do not confuse with

- **Stale Binding** — substrate-rich primitive for *lagging memory*. Stale Binding: truth moved, decision didn't notice. Post-hoc Authorization: outcome appeared, prior standing was retroactively invented. Different temporal directions — Stale Binding looks backward at truth that has already moved; Post-hoc Authorization looks backward at *its own action's outcome* to mint pre-action standing. Sibling on the temporal-authority axis.
- **Memory Skew** — directional comparison between prior and observed claim. Post-hoc Authorization is one possible *trigger* of skew (success outcome creates a leading-direction claim about prior standing), but the named pattern is the inference chain, not the comparison.
- **Receipt Theater** (AWP §3.D) — receipts accumulate without constraining future decisions. Adjacent: receipt theater is *receipts not binding*, post-hoc authorization is *outcomes minting backward bindings that never existed*. Different failure modes; receipt theater can co-occur with post-hoc authorization but the kernel surfaces are different.
- **Survivorship bias** — folk-statistical sibling. Post-hoc Authorization is the *operational* version where the survivorship is converted into *retroactive authority*, not just into *favorable evidence*.

## Typical symptoms

- Postmortems that conclude "no harm, no foul" and skip basis-at-execution-time review.
- Production deploys with no recorded admissible basis whose only review artifact is the green CI run after the fact.
- Capability claims sourced entirely from "we already did this" without prior-standing reconstruction.
- Cron jobs that ran cleanly for six months and acquired implicit authority to mutate state they were never granted authority over.
- Agent-loop steps that complete without incident and become precedent for adjacent steps under accumulated context (composes with Role Accretion).

## Architectural rule

> **A receipt must record the basis that existed at execution time, not the outcome that followed.** Outcome-only receipts permit post-hoc authorization laundering; basis-bearing receipts refuse it structurally by failing to find authority that wasn't there.

## Used by

Anticipated, not built:

- Wicket — preflight authority-bearing changes; fixture target. *Did the change have admissible basis at the moment of mutation, or only a successful test run after?*
- Agent Governor — admissibility verdicts on actor/operation pairs; the verdict `POST_HOC_AUTHORIZATION_DENIED` slots into AG's verdict space.

**Wicket/AG fixture probe** noted as future work, **not executed in this session**. Requires reading those repos; deferred.

## Cross-references

- `LeanProofs/CollapsedSurface.lean` — kernel theorem `collapsed_surface_not_identified` underlying the structural refusal.
- `LeanProofs/Admissibility/SurfaceAuthorization.lean` — Governor-facing refusal gate; keeper *"collapsed surface may authorize inquiry, not attribution."*
- `working/primitives/stale-binding.md` — temporal-authority sibling (lagging direction).
- `working/primitives/role-accretion.md` — composes with post-hoc authorization when accumulated successes mint expanded scope.
- `working/adversarial-witness-protocol.md` §3.D Receipt Theater — adjacent operational pattern (receipts without constraint, vs. receipts retroactively confabulated).

## Promotion gates

This stays as a candidate until at least one of:

- Wicket or AG produces a concrete fixture that benefits from named-receipt-verdict treatment (then: implementation invariant, possibly small lemma in `SurfaceAuthorization.lean`).
- A second non-ops domain exhibits the same temporal-inference-chain failure cleanly (then: working status).
- A live consumer requests the verdict in its receipt schema (then: spec stub).

Until then: named pattern, kernel-backed, no implementation.

## Provenance

Emerged from the 2026-05-20 eight-slice brainstorm following the morning's MemorySkew/AxisSkew work and the methodology discussion about *specification vs attack*. Identified as the strongest genuinely-new candidate from the brainstorm after audit ruled out seven other slices. The pattern was floating in the operational substrate of multiple repos without a named handle; this note supplies the handle and points to the existing kernel underneath. Per the gate stack: handle filed, predicate stated, fixture deferred to Wicket/AG, kernel work refused.

**2026-05-21 additions.** Federalist-Papers riff (operator + ChatGPT + DeepSeek) re-derived the same rule under transition-system framing — *"a transition S → S′ is authorized only if the witness authorizing S → S′ is already valid in S, not created by S′"*. Kernel-overlap audit fired clean (per [[feedback-kernel-overlap-audit]] keeper *"the system can do X ≠ X is justified"*) — same rule, different domain, no new note minted. Two pieces folded in: (1) the formal-register keeper *"No transition may smuggle its warrant backward from the state it creates"* added alongside the original operator-register keepers; (2) the four-branch decision table (Allowed / Denied / Denied / Suspicious-deferred) added as a new section, with the fourth branch explicitly handing off to stale-binding / commitment-standing-decay rather than collapsing into Post-Hoc. The Federalist-Papers domain (Senate representation, founding compromise, constitutional renewal) has now generated two closely-related re-derivations of the temporal-authority kernel this week — useful as worked-example terrain, not as a source of new theorems.
