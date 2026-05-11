# Commitment Standing Decay
## Notes toward Cybernetic Realpolitik

**Status:** Candidate / exploration phase. Not ratified. Forcing case: US–France alliance 1778–1800 (Treaty of Alliance → 1793 Neutrality Proclamation → Quasi-War → 1800 Convention of Mortefontaine). Sibling axis to FiatAdmissibility, Signal Authority, and testimony-vs-self-theory under the proposed superclass *Admissibility decay under representational persistence* (see [admissibility-decay-family-note.md](admissibility-decay-family-note.md)). Filed per name-early discipline; explicitly not promoted, Lean not built.

## The primitive

A declared commitment remains rhetorically present while the admissible-action selector no longer permits actions that would satisfy it.

Formal skeleton:

- **Declared commitment:** `C ⊆ U` (a constraint on the action space)
- **Admissible action set under current viability conditions:** `A(t) ⊆ U`
- **Operational standing:** `standing(C, t) := C ∩ A(t) ≠ ∅`
- **Operational revocation:** `C ∩ A(t) = ∅` while public language still asserts `C`
- **Rhetorical continuity:** the speech-act module continues to emit `we honor C`
- **Betrayal condition:** `C` persists as speech while losing standing as action

Keeper line:

> **The state does not need to break its word; it only needs to move the word outside the control loop.**

The system does not have to "decide" the obligation is dead. The action selector simply no longer admits actions that would satisfy the commitment, while the rhetoric module continues operating undisturbed. *Feedback reclassification* — not conscious cynicism, and not unconscious drift either, but the structural consequence of viability-driven action selection meeting a fixed commitment set.

## Control-theoretic skeleton

Following the classical robust-control framing:

- **State** `x_t ∈ X` — high-dimensional summary (fiscal position, legitimacy, military capacity, recognition status, elite coalition structure, debt-rollover risk, etc.)
- **Control inputs** `u_t ∈ U` — policy actions (treaties, tariffs, deployments, diplomatic language, budget allocations)
- **Dynamics** `x_{t+1} = f(x_t, u_t, w_t)` with `w_t` exogenous disturbance
- **Viability set** `V_t ⊆ X` — region of state-space where the political order survives (regime doesn't collapse, debt doesn't default, coalition doesn't fracture)
- **Admissible action set** `A_t(x_t) = { u ∈ U : f(x_t, u, w_t) ∈ V_{t+1} with acceptable probability }`
- **Commitment as constraint** `C ⊆ U` — the publicly declared restriction

The control loop selects `u_t` from `A_t(x_t)` because exiting viability is existential. The commitment `C` is *enforced* only while it intersects the admissible set comfortably. Once `C ∩ A_t(x_t) = ∅`, the loop has no choice: violate the commitment or collapse. The system does not register itself as breaking its word; it merely optimizes over `A_t(x_t)` while the speech-act module continues to emit the string `we honor C`.

The cybernetic piece: the viability filter is the implicit PID; the commitment is a constraint that once passed through the filter and now does not. The filter doesn't decide to discard the commitment. It just stops finding actions that satisfy both.

## Four-branch typology

Different mechanisms, different repair operators:

**1. Emergent standing decay.**
Nobody formally kills the obligation. It stops being selected because the viability set changed. *Repair:* recognize the structural revocation; either re-bind under new conditions or acknowledge the loss.

**2. Managed rhetorical camouflage.**
Officials know the obligation is dead but preserve the language to avoid legitimacy costs. *Repair:* expose the gap between internal acknowledgment and public language. This is deliberate concealment, not feedback reclassification — distinct from branch 1 even though they look identical from outside.

**3. Successor continuity theater.**
New actors inherit old rhetoric without inheriting basis. Personnel changes; language doesn't. *Repair:* audit succession against the standing relation — *does succession preserve basis, or only vocabulary?* This branch generalizes outside states (companies after leadership change, open-source maintainership, institutions after founder death, standards bodies, churches, universities — anywhere rhetoric outlives the actors who originally bound themselves).

**4. Transparent revocation.**
Formal exit, treaty withdrawal, open repudiation. Same family, different mechanism — the standing change is announced rather than hidden. *Not a failure mode;* this is the case where the system does the honest thing.

The diagnostic test:

> Did the language of commitment remain stable while the admissible action space stopped containing actions that would satisfy it?

If yes → branches 1, 2, or 3 (further audit needed to distinguish).
If the language explicitly changed → branch 4.
If neither the language nor the admissible action space changed → not the primitive; you have ordinary policy reversal, hypocrisy, or imperial garbage in a nicer hat.

## Forcing case: US–France 1778–1800

The historical specimen that exercises every joint of the framework:

- **1778:** Treaty of Alliance with France. Mutual defense obligation, alliance language, anti-British orientation.
- **1789–1793:** French Revolution, Reign of Terror, declaration of war on Britain. Viability conditions for the US shift radically: independence is now consolidated, recognition matters, trade with Britain has become economically critical, ideological alignment with revolutionary France carries domestic costs.
- **1793:** Washington's Neutrality Proclamation. The Treaty of Alliance remains technically in force. The language: "duty and interest" require friendly and impartial conduct toward all belligerents. The substance: the mutual defense obligation is no longer in the admissible action set.
- **1798–1800:** Quasi-War. US and France engage in undeclared naval conflict. The 1778 alliance is still nominally alive.
- **1800:** Convention of Mortefontaine formally terminates the alliance.

The seven-year gap between 1793 (operational revocation) and 1800 (transparent revocation) is the specimen. During those years, the constitutional apparatus is continuous, the alliance language is preserved at low cost, and the admissible action set excludes the mutual defense obligation. Branch 1 (emergent standing decay) with some branch 2 contamination (Hamilton/Adams faction knew exactly what they were doing).

## Prior art mapping

Eight veins of close-but-not-quite work:

1. **Realism / raison d'état** — too blunt; states pursue interest, fine, but no mechanism for *language persisting after operational standing decay*.
2. **Vienna Convention Art. 62 / *rebus sic stantibus*** — legal cousin; covers formal exit under fundamental change of circumstances. Doesn't cover the informal / undeclared variant where rhetoric persists.
3. **Krasner, *Sovereignty: Organized Hypocrisy*** — closest in spirit; sovereignty as enduring norm repeatedly violated. Doesn't have the control-loop / admissibility framing.
4. **Brunsson, *organizational hypocrisy*** — structurally closest. Talk/decisions/actions split. Closer to the primitive than realism is, but organization-theory frame; doesn't generalize cleanly to state-system viability.
5. **Meyer & Rowan, institutional decoupling** — formal structures persist as legitimacy theater while actual work decouples. Captures the *ceremonial interface* piece but not the *viability-set movement* driver.
6. **Credible commitment / time inconsistency / Putnam two-level games** — the political-economy machinery. Models commitments becoming non-credible/non-ratifiable under shifting domestic-international constraint. Doesn't articulate it as a standing-collapse primitive.
7. **Stafford Beer / Viable Systems Model** — the cybernetic skeleton for systems maintaining viability under environmental change. Provides the framework without the commitment-as-constraint application.
8. **The 1778 US–France alliance specimen** — referenced in (2) and Krasner; not usually positioned as a control-theoretic example.

The distinctive cut is *admissibility theory applied to state commitments under shifting viability constraints*. None of the prior art combines:
- The control-loop / admissibility framing
- The rhetorical-vs-operational split as structural rather than behavioral
- The four-branch typology
- The diagnostic test (language stable, admissible action space shifted)

## Relation to the admissibility-family superclass

Per [admissibility-decay-family-note.md](admissibility-decay-family-note.md), this primitive is one of five sibling instances of *Admissibility decay under representational persistence*. The shared pattern:

> X licenses use U under conditions Γ. Conditions change such that X no longer licenses U. The system continues acting as if it still does.

For Commitment Standing Decay specifically:

- **X** = declared commitment (speech-act)
- **U** = operational obligation
- **Γ** = viability conditions making the commitment-set intersect the admissible-action set
- **Persistence** = rhetoric module continues asserting the commitment

The Lean module under consideration — `Admissibility/CommitmentStanding.lean`, *not* `CyberneticRealpolitik.lean` — would express this in the same admissibility vocabulary as the existing kernels. *Cybernetic Realpolitik* is the essay handle; *CommitmentStanding* is the honest module name (same precedent as FiatCalculus / FiatAdmissibility).

## Lean module candidate (deferred)

Module path reserved, not built:

```
~/git/lean/LeanProofs/Admissibility/CommitmentStanding.lean
```

Minimal sketch (not a serious draft):

```lean
structure CommitmentSystem where
  State    : Type
  Action   : Type
  admissible : State → Set Action
  commitment : Set Action

def standing (s : CommitmentSystem) (x : s.State) : Prop :=
  ∃ u : s.Action, u ∈ s.admissible x ∧ u ∈ s.commitment

-- Under shrinking admissibility with fixed commitment,
-- standing eventually vanishes without any change in declaration.
theorem revocation_under_shrinking_viability
    (sys : CommitmentSystem)
    (x₀ : sys.State)
    (step : sys.State → sys.State)
    (shrink : ∀ n, sys.admissible (step^[n+1] x₀) ⊆ sys.admissible (step^[n] x₀))
    (initial_standing : standing sys x₀)
    -- C is fixed; rhetoric module emits unchanged declarations
    : ∃ n, ¬ standing sys (step^[n] x₀) := sorry
```

The theorem says: under shrinking admissibility, a fixed commitment loses standing with no change in declaration. Same structural shape as `proxy_cannot_self_certify_magnitude` in FiatAdmissibility — the licensing relation is missing, not the artifact.

**Don't build yet, per the same rule that applied to Signal Authority:** four-branch typology still doing prose work; structural vs temporal sub-distinction (see family note) not yet resolved; second forcing case beyond US–France not surfaced. The Boolean form of "commitment in admissible set vs. not" is probably too coarse for the four-branch typology, the same way `silenceMeansNothing | silenceMeansRejection` was too coarse for Signal Authority.

## What's deferred

- Lean module not built. Same posture as Signal Authority: distinctions still doing prose work.
- Primitive not promoted. Second forcing case needed (candidates: corporate governance after leadership change; church doctrine after schism; standards-body commitments after vendor capture; treaty obligations of successor states).
- The structural vs temporal sub-axis (see family note) not resolved for this primitive's place in the taxonomy.
- Branch 2 (managed camouflage) vs. branch 1 (emergent decay) — diagnostic to distinguish them in practice not specified beyond "did internal memos acknowledge the obligation was dead?"
- Successor continuity theater (branch 3) generalization beyond states not pursued. Real candidates exist (companies, open-source, churches, universities); not yet surfaced as their own forcing cases.

## Ratification gate

Conditions for promoting candidate → doctrine:

- Second forcing case beyond US–France that exercises all four branches
- Resolution of structural-vs-temporal sub-axis classification
- Generator test: does the four-branch typology cut sharply enough to distinguish cases that are *not* the primitive?
- Kind test: tentatively an *axis* (commitment-standing as the dimension) with the four branches as values along it. May resolve as a boundary.
- Composition audit with FiatAdmissibility, Signal Authority, testimony-vs-self-theory: same kernel architecture or sibling axes?
- Anti-collapse check: confirm the primitive is *not* a costume of Signal Authority's "authorized-but-illegitimate clause" pathway

Not promoted. Filed.

---

**Cross-references:**

- [admissibility-decay-family-note.md](admissibility-decay-family-note.md) — superclass and five-axis family
- [signal-authority-candidate.md](signal-authority-candidate.md) — sibling primitive (signal-shape axis)
- [testimony-vs-self-theory.md](testimony-vs-self-theory.md) — sibling primitive (witness-standing axis)
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — sibling kernel (artifact-kind axis, built)
- `project-admissibility-doctrine-stubs.md` (memory) — declared-substitution stubs (the broader laundering family)
