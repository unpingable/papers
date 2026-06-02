# ContractionHinge slice — codex adversarial review

**Status:** Agent-filed 2026-06-02. Single-pass codex review of
`LeanProofs/Admissibility/ContractionHinge.lean` (at `~/git/lean/`),
Slice 0 of the substructural-sequent program (axis 2 of the
[maximal-calculus axis map](maximal-calculus-map.md)).

Distinct from the amendment-fragment log
([`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md))
to keep the per-fragment review traces separated.

## Build status

- `lake env lean LeanProofs/Admissibility/ContractionHinge.lean`: exit 0, no warnings after `@[inherit_doc]` cleanup.
- `lake build`: exit 0, 8305 jobs (identical to baseline — annex is not imported).
- `#print axioms` output:

```
'Admissibility.ContractionHinge.T1'  does not depend on any axioms
'Admissibility.ContractionHinge.T2'  depends on axioms: [propext, Quot.sound]
'Admissibility.ContractionHinge.T3'  depends on axioms: [propext, Quot.sound]
'Admissibility.ContractionHinge.T3'' does not depend on any axioms
```

## Codex invocation

`codex exec -c approval_policy="never" --sandbox read-only --skip-git-repo-check --cd /home/jbeck/git/lean` (model gpt-5.5). Prompt scope: the charter's nine review items, with explicit "do not redesign the calculus" guardrails.

## Findings (verbatim)

1. **Axioms:** Strictly unclean for T2/T3: `propext` and `Quot.sound` appear. T1 is clean; T3' is clean. If Lean-default foundations are allowed, this is acceptable, but not axiom-free.
2. **Placeholders:** Pass. No `sorry`, `admit`, or `True`-shaped theorem/proof placeholder.
3. **Context Type:** Pass. Contexts are `List Formula`; no `Multiset`, `Finset`, or deduplication.
4. **T3 Base System:** Pass. `T3` is stated over `Derivable`, not `DerivableC`, and does not route through contraction.
5. **tensorR:** Pass. Signature is split-context multiplicative: `Derivable Γ A → Derivable Δ B → Derivable (Γ ++ Δ) (A ⊗ B)`.
6. **tensorL Trailing Δ:** Pass. Signature includes trailing `Δ`: `Derivable (Γ ++ A :: B :: Δ) C → Derivable (Γ ++ (A ⊗ B) :: Δ) C`.
7. **Rule Glosses:** Pass. The five base rules match the listed charter glosses.
8. **Cut / Hidden Contraction:** Pass. No cut rule; no contraction rule in `Derivable`; base proofs do not simulate contraction.
9. **No Silent Weakening:** Pass. `T3` is arbitrary `A : Formula`; `v` is leaf-counting with atoms weight `1`; refusal is not made vacuous by redefining `weight`.

## Agent verdicts

- **Finding 1:** **INFORMATIONAL.** `propext` and `Quot.sound` are Lean 4 *core* foundations, used internally by `simp` and other standard tactics. They are not user-introduced and are present in virtually every non-trivial Lean 4 proof. Codex's own framing conceded "if Lean-default foundations are allowed, this is acceptable." The charter's "no sorry/admit/True placeholders" review constraint is satisfied; "axiom-free" was not a stated criterion. No correction.
- **Findings 2–9:** **AFFIRMS (no action).** Each charter review point passes per codex's read of the source.

## Integration

**None.** No bounded corrections apply. The slice ships as written.

## Cross-references

- Slice source: `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`.
- Axis map: [`maximal-calculus-map.md`](maximal-calculus-map.md) (axis 2 = ContractionHinge).
- Sibling slice's review trace: [`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md) (axis 1 = AmendmentFragment).
- Codex calling discipline: `~/.claude/skills/codex-exec/SKILL.md`.
