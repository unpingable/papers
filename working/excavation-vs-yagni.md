# Excavation is not invention — YAGNI does not gate formalization

**Filed:** 2026-06-14. **Status:** doctrine note. **Promotion candidate** (cross-project;
see "Promotion" below). **Policy correction:** 2026-07-14. The original note used
*forcing-case* vocabulary inherited from the former consumer-gating rule. Here that
phrase now means pressure or correspondence evidence only; it never grants permission
to formalize. Formalization may precede and lead implementation.

## The rule

> YAGNI constrains speculative implementation and public-surface commitment. It does
> not block a coherent formal investigation, and it does not block recording repeated
> structure already shipping across independent systems. Excavated invariants are not
> speculative abstractions.

When the same structural invariant is independently enforced by N of your own running
systems, "wait for a forcing case before abstracting it" is **the bug, not the
discipline.** The implementation evidence is already distributed across the
constellation, smoking quietly in the corner. More importantly, even a new formal
statement does not need a consumer's permission: theorem shape, overlap, semantics,
proof, and anti-vacuity determine whether the formal work is sound. Runtime recurrence
strengthens a correspondence or promotion case; it does not open the theorem gate.

## The worked example (the scar that produced this note)

The observer foundation (`Force : Consumer → Artifact → Verdict`) was gated for weeks
under "no present consumer → withhold." That was the former forcing-case reflex
misfiring; the consumer gate is now superseded. A
read-only excavation of seven shipping systems —
**NQ, nightshift, wicket, continuity, standing, verifier, WLP** — found the *same five
invariants* enforced independently, in three languages:

1. force/verdict is consumer-relative (no bare `Force(artifact)`),
2. the artifact is a flat fact (no consumer/authority/root stamped on it),
3. freshness is consumer-judged in force-assigning systems,
4. rootless except one single-genesis (standing's operator-fiat),
5. refusal is a typed outcome.

(Full table + the corrected abstract codomain in
[`observer-foundation-promotion-preflight.md`](observer-foundation-promotion-preflight.md).)

Seven independent implementations are not a hunch. They are strong recurrence and
correspondence evidence — stronger than literature prior-art, because they are *your
own load-bearing code*. They strengthened the case for promotion; they were never the
source of permission to state or prove the invariant.

## How this composes with existing doctrine (not a contradiction)

- **Scars as evidence** (global): prior art / named failure classes count as anticipatory
  evidence. This note is the *in-house, distributed* case: the invariant is already a
  scar in N of your systems. Even stronger than literature prior-art.
- **Former forcing-case calibration** ([[feedback-forcing-case]]): "not every next step
  needs to be blessed by disaster." The current correction is stronger: no consumer or
  incident is an admission authority for formal work. Runtime cases are pressure and
  correspondence evidence. The three-tier ladder (public surface / bounded annex /
  playground) still governs custody and compatibility, not permission to prove.
- **YAGNI scope** (global): "don't build the operational abstraction yet" still governs
  speculative implementation. The discriminator **did you invent this shape, or
  excavate it?** bears on implementation and promotion confidence. It does not bar a
  bounded formal model whose statement is coherent and whose scope is explicit.

## The discriminator (so this can't be abused as a license)

This is NOT "any abstraction I like is excavated." The bar:

- **≥ 2 independent shipping systems** enforce the structure (not one elegant use, not a
  plan, not "Claude/ChatGPT agree" — that's a dopamine receipt, cf. the Table-Flip
  Override's invalid bypasses).
- The structure is **read off the artifacts**, not designed and then matched.
- Recurrence is **structural**, not vocabulary coincidence.

Below the bar → do not claim the abstraction is excavated from shipping reality. A
bounded formal investigation is still allowed, but public promotion must stand on its
own theorem-shape, overlap, anti-vacuity, custody, and compatibility review. At/above →
excavation; abstracting is recording reality, not speculating.

**Crucially, formalization does not need excavation's permission, and excavation does
not imply public promotion.** That the shape recurs in implementations (earned) is a
separate question from whether to mint it as public substrate (ratified). The
vocabulary-foundation subgate (`wiring-is-not-folder-placement.md`) still governs
"make downstream depend on it." A downstream implementation may then cite the promoted
contract, but citation alone does not establish conformance; it also needs an explicit
mapping and runtime evidence or a refinement argument.

## Keepers

> A consumer can test a theorem's correspondence. It cannot grant permission to develop
> the theorem.

> Excavation is not invention. YAGNI governs implementation scope, not mathematics.

> Earned ≠ public. Excavation earns; ratification publishes.

## Promotion

Candidate for promotion to global guidance (`~/.claude/CLAUDE.md`). **Nearest sibling: the
`Scope vs coverage` section** (added to global CLAUDE.md 2026-06-14) — that section splits
*YAGNI-governs-scope* from *completeness-governs-coverage*; this note adds the third
discriminator in the same family (*YAGNI does not gate excavated, already-shipping
structure*), and its `earned ≠ public` fence is the same tier discipline. It would slot
directly after `Scope vs coverage`.

**Status: ONE firing (the observer excavation). Operator decision 2026-06-14: HOLD** — do
not promote to global CLAUDE.md until a second independent recurrence (candidate until
repeated; global CLAUDE.md is highest-blast-radius). Keep this local breadcrumb + the
`Scope vs coverage` slot pointer so the lift is cheap and not rediscovered cold when it
recurs. Provenance: observer-foundation excavation, 2026-06-14, operator + ChatGPT +
Claude; AG-Claude independently noted the `Scope vs coverage` adjacency.
