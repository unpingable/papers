# Maximal-calculus tech tree — sequencing doctrine (CANDIDATE)

**Status:** CANDIDATE / non-binding. A handle for review, NOT authorization to
build. Captured 2026-06-30 while the operator was noodling on sequent calculus
with codex / ChatGPT / web-Claude — **work is incoming, not yet inspected.** This
note records the *sequencing* idea only; it does not look at or bless any
in-progress `Sequent.lean`.

Provenance: ChatGPT framing ("RTS tech tree — don't tech-rush Wonder before you
have farms"), operator-driven.

## The core move: three trees, do NOT unlock in parallel

### 1. Proof-theoretic admissibility logic — the *barracks*
First object: `ResourceSequent`. Answers: *what may be inferred, what must be
spent, what residue must remain?* Candidate receipts:
- `erases_to_sequent`
- `residue_preserved`
- `no_free_contraction`
- `bridge_token_required`
- later: `cut_admissible`

This is what makes an ordinary `Sequent` useful: ordinary sequent becomes the
**forgetful projection** of the resource layer. The doctrine-bearing arrow:

```
ResourceSequent  --erase-->  Sequent  --empty ctx-->  WDC Lift
```

Everything else is vibes until this arrow is proven.

### 2. Process calculus — the *stables / siege workshop*
Do NOT build as more formula grammar. Build as **operational traces**:
`state --action/spend--> state'`, labels = consume claim token / consume bridge
warrant / carry residue / emit refusal residue / revoke warrant / observe
freshness / execute bounded effect. Then prove **correspondence (adequacy)**:
```
process trace exists  ⇒  resource derivation exists
resource derivation   ⇒  some abstract process trace exists
```
Proof theory says *what is admissible*; process calculus says *how custody
moves*. Same machine, different camera angle.

### 3. Unified maximal calculus — the *late-game forbidden temple*
**The prize is a CONSERVATION THEOREM, not a monster datatype.** Shape:

> Adding process / custody / refusal / freshness layers is conservative over WDC
> erasure UNLESS an explicit witness / token / residue rule accounts for the
> extra authority. No extension may manufacture authority when projected back to
> WDC / ordinary sequent / resource erasure.

## The tech-tree ordering (dependency chain)

```
WDC Lift → ordinary Sequent → ResourceSequent → Trace/Process Semantics
        → Adequacy + Conservation → Doctrine-specific modalities
        → Maximal calculus as indexed family / projection theorem
```

## NAME FENCE — this is not the retired calculus in a fake mustache

"Maximal calculus" here is the **conservation/projection theorem**, NOT a positive
unifying datatype. The anti-pattern (ChatGPT's own joke, recorded as the thing to
refuse) is "ontology fondue":
```
inductive Formula | atom | bridge | freshness | custody | revocation
                  | refusal | execution | pain | capitalism | my inbox
```
That monster inductive is exactly the laundering [[project-calculus-vocabulary-retired]]
forbids and the [[feedback-enum-regression-tell]] autocomplete tell. If the
sequent work starts growing one giant constructor family, the fence has failed.

## Why this is doctrine-bearing (the connections that make it more than vibes)

- **The conservation theorem IS [[project-no-unifier-without-laundering]] applied
  to the calculus question.** The "unified maximal calculus" was never a positive
  unifier — *the positive calculus would be the FreeStandingBridge that opens
  every gate*. The honest form is the negative/conservation statement. This is the
  same no-go, now stated proof-theoretically.
- **Same shape as the no-free-X family.** "No projection manufactures authority"
  generalizes `no_free_lift` (NoFreeLift.lean), the seam money theorem
  (`global_not_implied_by_local`: local bridges ⊬ trajectory authority,
  `working/tooltheory/witnessed-seams-edge-ledger-candidate.md`), and
  no-free-standing-bridge. The maximal-calculus conservation theorem may be the
  umbrella those instances were circling.
- **Sequencing matches [[feedback-kernel-vs-process-calculus]]** — *build specimens,
  defer calculus namespace; court first, map later.* ResourceSequent specimen
  first; process traces second; conservation last.
- **This is INSIDE an opened surface**, so per [[feedback-forcing-case]] the gate
  is completeness-of-the-prior-layer, NOT a forcing case. "Don't tech-rush" =
  don't open tree N+1 before tree N's farms (receipts) are proven.
- Composes with the dormant maximal-calculus registers:
  `working/maximal-calculus-forcing-cases.md`,
  `working/maximal-calculus-decomposition-trigger.md`,
  `working/maximal-calculus-amendment-cut.md` (all "file-now-work-never").

## Immediate next unlock (the first non-toy footing)

Boring and brutal, and the only thing that earns the rest:

> Prove the **resource layer is strictly stricter** than the ordinary sequent
> layer, and that **residue cannot silently disappear** (`no_free_contraction` +
> `residue_preserved`, with `erase` to ordinary sequent as the forgetful map).

Until that lands, trees 2 and 3 stay locked.

## Refinement — cross-vendor pass (2026-06-30)

Gemini independently produced the same three-formalism carving (process calculus /
admissibility logic / unified maximal calculus) with a "swamp" warning label —
**cross-vendor convergence** (Gemini + ChatGPT + Claude). Caveat: this tree may
just be the *textbook* decomposition any competent model emits, so the convergence
is reassuring, not strongly evidential. **The corpus's value-add is not the tree —
it's the anti-laundering fences on it** (conservation-not-datatype, certificate
schema non-collapse, declared-order relativity). Those keep it out of the swamp.

Two position corrections that survive the pass:

- **Process calculus (tree 2) is NOT next — it's a choreography layer, deferred.**
  It proves the runner didn't deadlock; it CANNOT, by itself, tell you whether the
  runner laundered admissibility into authority (the payload problem). So it
  becomes useful *after* the certificate/checker exists, as choreography around it.
  *Process calculus waits until there is a thing worth choreographing.*
- **Admissibility logic (tree 1) is the next lane — with a precision fence.**
  "Valid proof ⇒ action is safe" OVERSTATES. Precise: *a valid proof relative to
  the declared calculus and evidence model satisfies the boundary rule encoded by
  that calculus.* It kills a class of laundering bugs; it does not make
  infrastructure spiritually clean — the machines remain haunted, as tradition
  requires. (= the declared-order relativity the corpus already carries:
  validity-under-declared-order, not absolute.)

**Sharpened conservation statement.** The maximal calculus is not "One Inductive To
Rule Them All" — it's the family law:

> Every layer forgets safely, and no forgotten layer can recover authority.

```
process trace      --projects to-->  resource certificate
resource certificate  --erases to-->  ordinary sequent / WDC reachability
ordinary reachability  --/->  resource executability   (without explicit token/witness)
```

**Keeper:** *build the boundary-enforcement layer before the choreography layer;
treat the maximal calculus as a conservation theorem, not a datatype.*

## Sibling: the runtime payoff

The *practical product* of tree 1 — a denial/authorization certificate whose proof
object cannot smuggle authority, plus a dumb checker + English explainer + fuzz
corpus — is captured separately at
`working/admissibility-runtime-certificate-candidate.md`. That path
**short-circuits** this tech-tree: it branches off tree 1's strictness slice and
ships without waiting for cut-elim / process calculus / maximal calculus.
*Verification engine first; the forbidden temple is not a prerequisite for the
customs officer.*

## What this note is NOT

- Not a look at the in-progress sequent work (operator said don't yet).
- Not authorization to build `ResourceSequent` or any of it.
- Not a revival of the retired "Admissibility Calculus" as a unifying object.
