# Post-Hoc Authorization Laundering

**Status:** candidate
**Kind:** Boundary condition
**Originated:** 2026-05-20 (eight-slice brainstorm + audit; named pattern, not new kernel)
**Primary home:** no paper yet — operational pattern with downstream Wicket / Agent Governor fixture potential

## Keeper

> **Lucky is not authorized.**

Adjacent line:

> Success after the fact cannot mint prior authority.

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
