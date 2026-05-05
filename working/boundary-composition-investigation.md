# Boundary Composition Investigation

**Logged:** 2026-05-05 (late session, multi-model: claude-code + chatty + deepseek)
**Status:** Pin / handle for tomorrow. Methodological pivot named, no Lean work started yet.
**Lives near:** P28 candidate territory (synthesis question for the P22→P27 spine).

---

## What this is

A handle for the move from **formalization-as-validation** to **formalization-as-investigation** on the admissibility kernel. Triggered by the P25 citation-debt audit (2026-05-05), which surfaced the admissibility-binding seam between P25's substitution-forcing theorem and `AuthorizedStep` ("stale basis cannot bind at mutation layer"). That seam plus the P22→P27 spine raised the synthesis question: do the admissibility boundaries actually *compose*, or are they only a family resemblance?

This note exists to keep the question crisp for tomorrow without re-deriving it from the conversation.

---

## The methodological pivot

**Before:** prose discovers claim → Lean validates / audits. Bottom-up. The Lean kernel records what's already known; sorries get classified per the existing discipline (proof / vocabulary-deficient / placeholder).

**Now (proposed):** named target proposes structure → Lean investigates whether the structure exists. Top-down. Success = a composition theorem with sharp content. Failure = a null result with *also* sharp content (here are the obstructions; the boundaries do not compose in this way).

The discipline the new mode requires that the old one didn't:

1. **State the target before searching.** Theorem statements written explicitly enough to fail honestly.
2. **Accept null results as content.** "Family, not Calculus" is publishable.
3. **Don't redefine terms mid-search.** Primitive-ratification gate applies harder in investigative mode than in validation mode.

---

## The named object

**Working title (provisional):** Boundary Calculus / `BoundaryCompositionExperiments`

**Slogan (load-bearing):**

> A system's ability to execute is not evidence of its authority to act.

**The research question, in its sharpest form:**

> Can two action-indexed boundary theorems be composed to produce a third action-indexed boundary theorem about a composite action, without redefining either input?
>
> If yes, repeatedly: that's a calculus.
> If only sometimes and conditionally: that's a Family with composition lemmas.
> If never cleanly: that's "related refusals, not an algebra."

**Three-fork outcome map:**

- **Composition laws emerge cleanly:** P28 honestly = "Boundary Calculus." Title earns itself.
- **Composition partially works with obstructions:** P28 = "Admissibility Boundary Family," with a strong null-result section.
- **No meaningful composition:** finding is "these are related refusals, not an algebra." Still publishable; prevents synthesis fraud.

---

## The discipline package (DeepSeek + chatty + claude lint)

### Action-indexing

**Every theorem must be indexed by the action under scrutiny.** No free-floating invalidity. No system-wide taint. No "one rotten receipt poisons the universe." DeepSeek caught two specific failures:

- The boundary theorem was globally poisonous (existence of *some* inadmissible boundary anywhere couldn't deny authorization for *any* composite action — the bad boundary has to be one *the action actually crosses*).
- The receipt theorem forgot to connect the derivation to the action (`¬ Authorized a` for arbitrary `a` from a bad receipt-derived derivation `d` is absurd; the derivation has to target the specific action, or one wants `¬ authorized_by d a`, not `¬ authorized a`).

**Structural consequence:** composition is stated at the **action level**, not on free-floating boundary objects. Boundary Calculus is a calculus of *action composition under boundary constraints*, not a calculus of boundary objects in the abstract. Latter is universal-solvent territory; former has teeth.

### Locked-ish definitions before the search

Required commitments (chatty's six + one):

1. What counts as a boundary?
2. What counts as crossing?
3. What counts as binding?
4. What counts as authorization?
5. What counts as composition?
6. What failure is allowed to block the whole composite?
7. **What counts as the same boundary twice vs two different boundaries?** (individuation principle — without this, "do they compose?" can be silently answered by changing what counts as separate)

If "boundary" gets quietly broadened mid-search to make a theorem go through, the result is post-hoc rather than discovery — fake calculus / formal puppet show. The locked definitions are the protection.

---

## First deliverable: audit, not theorem

**The investigative branch's first commit is the audit, not a theorem.** Before stating new targets, inspect what the existing kernel already commits to about composition.

Live-audit-over-cached-roadmap discipline: verify against actual repo state, not against memory of what the roadmap said weeks ago.

**Existing kernel objects to audit** (under `~/git/lean/LeanProofs/Admissibility/`):

- `Authority` module
- `StateTransition` module (mutation algebra, `StepAllowed`)
- `Derivation` module
- `Execution` module
- `Corrective` module (corrective monotonicity; corrective steps as down-edges; re-entry as replacement)
- `AuthorizedStep` (stale basis cannot bind at mutation layer)
- `classify : Step → StepClassification` (the enforcement surface)

**Audit columns (per object):**

| Column | Question |
|---|---|
| Object | Name of theorem / definition / module |
| Boundary kind involved | Authority / StateTransition / Derivation / Execution / Corrective / other |
| What composes? | What does this theorem combine? |
| What blocks composition? | Under what conditions does it fail? |
| Action-indexed? | Is the theorem indexed by the action under scrutiny, or free-floating? |
| Derivation-indexed? | Is the conclusion `¬ authorized a` or `¬ authorized_by d a`? |
| Global-state-indexed? | Does it reach into ambient state? |
| Already a composition theorem? | Or just a single-step property? |
| **Individuation load-bearing?** | If you collapsed the involved boundaries into a single predicate, would the theorem still go through? (Yes = decoration; No = kernel committed to that split) |
| Could this generalize? | Without broadening definitions? |

The "individuation load-bearing" column is the operational form of question 7 above.

---

## Candidate theorem shapes (for after the audit)

These are sketches, not commitments. Stated to mark the territory; the audit may show some are already proved, others are vocabulary-deficient.

**1. Denial composition (boundary violation blocks authorization, action-indexed):**

```lean
theorem boundary_violation_blocks_authorization
  (a : Action) (b : Boundary) :
  crosses_boundary a b →
  required_for_action a b →
  ¬ admissible_crossing a b →
  ¬ authorized a
```

**2. Receipt non-laundering (action-indexed, derivation-indexed):**

```lean
theorem receipt_does_not_authorize_without_basis
  (a : Action) (r : Receipt) (d : Derivation) :
  valid_receipt r →
  uses_receipt d r →
  derives_authorization_for d a →
  ¬ authorization_basis d →
  ¬ authorized_by d a
```

Note: conclusion is `¬ authorized_by d a`, not `¬ authorized a` — another derivation could still authorize `a`. (DeepSeek catch.)

**3. TTL / revocation breaks composition:** likely already substantially in `AuthorizedStep`.

**4. Kind separation:** policy / evidence / gap / receipt / corrective stores do not collapse into each other under transition. Likely partially in the five-sibling-module decomposition.

**5. Possible null result:** boundaries may not form a lattice or clean algebra because authority, evidence, time, scope, execution are different *kinds*, not elements of one neat order. → Family, not Calculus.

---

## Three promotion errors (the compression target if synthesis lands)

If the synthesis paper happens, the operator vocabulary should compress to one slogan and a small number of promotion errors. Chatty's compressed list (after self-correcting from a 14-operator overshoot):

1. **Evidence promoted to authority.** "We observed something, therefore we may act."
2. **Proxy promoted to target.** "We can measure V′, therefore we are governing V." (P25 case.)
3. **Mechanism promoted to legitimacy.** "The system can execute the transition, therefore the transition is authorized." (`AuthorizedStep` case.)

Everything else — testify, interpret, recommend, authorize, act, bind, revalidate, revoke — stays *background grammar*, not minted primitives. Adding more requires the ratification gate.

---

## What this is NOT

- **NOT** an authorization to draft P28. The audit comes first; the title comes last; the theorem statements come in between.
- **NOT** a license to mint operators. Every primitive that gets added must replace more than it adds.
- **NOT** a framework-launch. Books + Zenodo is the venue; "named admissibility discipline" is a temptation, not a goal.
- **NOT** event-triggered control adjacent. That neighborhood belongs to P22 actuation / Δt timing, not P25 or the synthesis question. Recorded here to prevent re-confusion.

---

## The case atlas (separate, parallel object)

Mentioned for completeness; not part of the Lean investigation. Could be book / Substack / appendix-shaped, not necessarily a preprint. Format:

> Many cases, one grammar (the three promotion errors), no new theorem unless cases break the grammar. **Includes contrast cases** — failures that look adjacent but aren't promotion errors — to demonstrate the framework's edges. Without contrast cases the atlas is a confirmation parade.

Each case answers: What was promoted? Into what authority? What boundary failed? What consequence followed? What refusal rule would have blocked it?

The atlas is the anti-universal-solvent companion to the synthesis paper. It can exist whether or not the calculus exists.

---

## Tomorrow's first move

1. Open `~/git/lean/`.
2. Walk the five admissibility modules + `AuthorizedStep` + `classify`.
3. Fill the audit table (above) per existing object.
4. Mark which objects are already composition theorems vs single-step properties.
5. Mark which boundary individuations are load-bearing vs cosmetic.
6. From the audit, decide which candidate theorems are already (partially) proved, which are vocabulary-deficient, and which are next-target-shaped.
7. *Then* state targets in `BoundaryCompositionExperiments`.

The audit is not a theorem. The audit is the precondition for honest theorem-stating.

---

## Pointers

- P25 paper: `preprint/25-epistemic-border-control/epistemic_border_control.md`
- P25 citation-debt note: `preprint/25-epistemic-border-control/NOTES.md` (last section)
- Lean repo: `~/git/lean/LeanProofs/Admissibility/`
- Project memory pointers: `project-authority-kernel.md`, `project-admissibility-family-structure.md`, `project-paper25-candidate.md`
