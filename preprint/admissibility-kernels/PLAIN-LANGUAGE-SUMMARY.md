# Plain-language summary

**Companion to:** *Safety-Bridge Kernel: Authorization and Value Preservation*

**Version/status:** v0.2 draft; unpublished and awaiting a program-level framing repair

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A system can prove that an actor is permitted to take a step without proving that the step preserves anything the system is meant to defend. If those two kinds of evidence share one “approved” label, operational permission can be mistaken for safety.

The problem persists over sequences: a series of individually authorized steps can form an authorized history whose endpoint has lost defended value.

This focused Lean 4 note separates authorized steps from **bridged** steps. A bridged step carries both permission and an independent witness that the transition preserves a defended-value floor. Authorization may depend on who acts; preservation depends on what the transition does. One proof object is not allowed to stand in for the other.

The theorem family makes that separation operational. An authorized step can lose defended value, while preservation by bridged steps composes across a finite trajectory. A value-losing authorized endpoint cannot later be presented as though it came from such a bridged history. Evidence can be forgotten to recover an ordinary authorized path, but it cannot be manufactured in the other direction. Two small specimens show that the distinction is constructive and works across multi-actor paths.

## Claim boundary

The kernel proves a conditional separation result over small models. It is not a complete safety policy, real-world certification, institutional legitimacy proof, refinement theorem, or process calculus. The later Governed Admissibility Calculus v14 provides a larger formal context, but the exact relationship of this earlier theorem family to v14—incorporated instance, sibling family, or independent specialization—has not yet been established. This companion therefore does not claim that Safety-Bridge is a GT instance. The draft’s obsolete program-level denial of a unified calculus requires repair before publication; that historical framing is not part of this summary.

## Read the paper

- [Manuscript source](paper.md)
- [Directory guide](README.md)
- [Canonical Lean repository](https://github.com/unpingable/lean)
