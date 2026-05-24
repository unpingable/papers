# Judgmental / Sequent-Style Fragment: Starting Constraint

Status: working note; non-canonical; not public surface.

This note records the starting constraint for any future sequent-style or judgmental formal layer over the Admissibility Calculus kernel. The kernel itself is unaffected. The companion note [[judgmental-presentation]] introduces sequent-flavored notation for *reading* the existing kernel; this note is the rule for *building* a real derivation system later, if and when one is forced.

## Non-claim

Not a sequent calculus, proof-theoretic admissibility logic, process calculus, or public-surface extension. Canonical semantics remain in `~/git/lean/LeanProofs/Admissibility/`.

## The starting hazard

Do not model the judgmental context as containing `Authorized(c)` atoms and then derive authorization from membership:

```
Authorized(c) ∈ Γ
─────────────────
Γ ⊢ Surface(c)
```

This turns the judgmental layer into a self-authorizing registry. Authority enters the context before being earned. A compact, beautiful laundering machine — the exact shape the kernel exists to prevent.

The Lean kernel already refuses this discipline operationally: there is no `Authorized` state in `GovState`. The four stores (`PolicyStore`, `EvidenceStore`, `GapStore`, `RevocationStore`) hold the *substrate* over which authorization is computed; the verdict is derived per-claim, not stored. `Execution.AuthorizedStep` (`LeanProofs/Admissibility/Execution.lean:82`) cannot be constructed without both `StepAllowed` and `authorityAuthorized` proofs *by structure literal*. A future judgmental layer that admits `Authorized(c)` as an atom in `Γ` would undo this discipline at the surface where it most matters.

## Better starting shape

Contexts should contain evidence, verdict inputs, basis/precedence/standing states, scope and effect constraints. Authorization should be derived only as a conclusion:

```
Γ ⊢ BasisOK(c)
Γ ⊢ PrecedenceOK(c)
Γ ⊢ StandingOK(c)
──────────────────
Γ ⊢ Authorized(a)
```

or, in the smallest operationally-faithful fragment:

```
Γ.basis      = admissible
Γ.precedence = active / nonconflicting
Γ.standing   = present / valid
────────────────────────────────
Γ ⊢ Authorized(a)
```

## Second hazard: free contexts

Even with the correct shape (B/P/S → Authorized), a second laundering vector hides one level deeper: the context itself is forgeable.

If `JudgContext` is a plain record, anyone can construct:

```
{ basisStatus := .ok,
  precedenceStatus := .active,
  standingStatus   := .fresh,
  action           := ... }
```

…and derive `Authorized(a)`. The shape is right; the source is not. The laundering moved from `Authorized(c) ∈ Γ` (an admitted authority atom) to `basisStatus = .ok` (an admitted verdict-input atom). Smaller hat, same goblin.

**The rule:** the judgmental context is admissible only when projected from canonical kernel state, or paired with a provenance witness that it was produced by the kernel evaluator.

```
No free Γ.
Γ must be either:
1. a projection from kernel state, or
2. paired with a proof/provenance witness that it was produced
   by the kernel evaluator.
```

This shapes the soundness theorem. The right form is:

```
projected_sound :
  Derives (mkContext s a) (Authorized a) →
  kernel_decide s a = .authorized
```

**Not** the more general:

```
Derives Γ (Authorized a) → ...
```

…unless `Γ` carries the provenance proof.

And the doctrine in miniature is its own theorem:

```
arbitrary_context_not_authority :
  Derives Γ (Authorized a) does not itself authorize a kernel transition
```

> **The judgmental layer can explain; it cannot mint.**

The experimental module can still use a `JudgContext` record for ergonomics. The substantive theorems must be over projected contexts only.

## First target

Define a tiny inductive derivation relation inside Lean (probably at `LeanProofs/Admissibility/Experimental/Judgmental.lean`) and prove soundness against the existing kernel:

```
judgmental_authorized_sound :
  Derives Γ (Authorized a) →
  kernel_decision Γ a = authorized
```

Soundness first. Completeness later, if ever. Soundness is the anti-laundering constraint; completeness drags the project toward maintaining a second exact model of the kernel — useful but a different commitment.

The first blocking theorem should test the discipline:

```
basis_fail_never_authorizes :
  Γ ⊢ BasisFail →
  ¬ Derives Γ (Authorized a)
```

## Avoid at first

- A full proposition language (∧, ∨, →, ∀, ∃).
- Modal operators (`◊Authorized`, `□Fresh`, etc.).
- `¬ Γ ⊢ Refused(c)` as a positive authorization side condition — non-monotonic side conditions on the absence of proof are a swamp.
- Unrestricted weakening.
- Unrestricted cut.
- The name "admissibility logic." It collides with the proof-theoretic sense; see [[judgmental-presentation]] § *Vocabulary correction* for the false-friend hazard.

## Structural-rule warning

Weakening is not automatically valid. From

```
Γ ⊢ Authorized(a)
```

it does **not** follow that

```
Γ, revoked_basis(a) ⊢ Authorized(a)
```

Adding context can introduce contradiction, revocation, stale evidence, or stronger refusal. Ordinary structural weakening is not free in this setting.

Contraction is probably harmless under set/record contexts but becomes interesting if evidence multiplicity ever matters. Exchange is fine if Γ is unordered.

The first metatheoretic question is therefore not "prove the standard structural rules are admissible." It is: **which structural rules are admissible under which context discipline?** That's where the project starts being its own thing rather than a Gentzen rerun.

## Likely research seam: cut

Unrestricted cut is the natural home of authority laundering. Sketch of the laundering shape:

```
Γ ⊢ advisory(X)
Γ, X ⊢ Authorized(mutate)
─────────────────────────
Γ ⊢ Authorized(mutate)
```

That is the cursed move — an intermediate advisory artifact gets used as authority by being cut through. A real sequent-style project should distinguish:

- **Safe cut**: intermediate `X` carries same-or-stronger basis, standing for the effect, freshness at evaluation time, scope.
- **Blocked cut**: intermediate `X` lacks any of the above; cut through `X` cannot produce authorization.

That distinction is where the project stops being notation and starts being a calculus candidate. It is also where the proof-theoretic "admissibility" vocabulary becomes genuinely useful (in its own sense) — proving that the laundering-shaped cut rules are **inadmissible**, while the safety-preserving cut rules are admissible. Two different uses of "admissible," neither of which is the kernel's governance sense.

## Cross-references

- [[judgmental-presentation]] — companion working note: the reading-aid form, with severity-fenced status block and the "what would be required for a real sequent calculus" debt list.
- [[truce-doctrine]] — sibling note: contradiction blocks authorization, remediation handles force outside authorization. The judgmental layer's discipline is downstream of the truce: nothing in `Γ` can pre-declare itself part of the truce.
- Kernel reference: `Execution.AuthorizedStep` (`~/git/lean/LeanProofs/Admissibility/Execution.lean:82`) — the canonical instance of "authority is conclusion, not atom" implemented by Lean structure literals.
- Memory: [[feedback-green-vs-promised]] — same discipline applied at a different boundary; compiled (or judgmentally-derivable) does not mean promised (or authorized).
