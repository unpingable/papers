# Residue custody — scratch (ToolTheory object, Lean contact)

**Custody-class: SCRATCH.** Compile-is-contact only. Not doctrine. Not discharge.
Not build authorization. This directory may *discover* predicates; it may not
*promote* them.

## What this is

The c(t) (consequence-viability) side of the m(t)/c(t) dual, filed as a
**ToolTheory object** — *not* "governance," "exit membrane," or "rollback"
(all blur it). The object keeps the tool in frame:

> Admissible **use** at t₀ ↛ admissible **consequence** at t₁.
> You are judging tool *residue*, not tool *use*.

Working names floated: "residue custody," "diachronic tool authority." The name
is paint; the **layer placement (ToolTheory)** is the contribution. "Residue
custody" is the 4th name for c(t) — do not let a nice phrase re-mint an existing,
already-parked object.

## What the Lean contact file does (and does not)

`scratch_residue_custody_noncollapse.lean` answers exactly one pre-code question
(ChatGPT, 2026-06-28):

> Can the residue-custody edges be represented **without collapsing into one
> generic `authorized : Bool`**?

It is a *representability smoke test*, not a theorem about residue. It sets two
representations side by side:

- `Collapsed` — one authorization bit. Every conversion holds for free
  (`collapsed_launders`): the seams are gone. This is the failure mode Rust will
  drift into if nobody names the non-conversions first.
- `Residue` — each predicate its own field. Every conversion is **refutable** by
  a countermodel: the seam stays open. A green edge theorem is a certificate that
  *that* seam did not collapse.

It compiles (self-contained, no imports) under the lean toolchain via:

```
cd ~/git/lean && lake env lean <abs path to the .lean>
```

It is **not** imported by `LeanProofs.lean`. It is not in the build graph or CI.

## The five edges (predicate inventory before implementation)

```
AdmittedUse        ↛ PersistentConsequence
WitnessFresh       ↛ WitnessStanding        (= "witness rot": fresh evidence, captured oracle)
Revoked            ↛ Unwound
Unwound            ↛ Repaired
ProducedBy         ↛ StillAuthorizedBy
```

These are anti-laundering / no-silent-conversion edges. Two are recombinations of
existing kernels, not new families: witness-rot = `Freshness` × standing-decay
pointed at the oracle; the quorum edge (`MultipleStanding ↛ QuorumAuthority`,
deliberately out of this file) = `quorum-cybernetics.md`, authority-*composition*.

## Provenance / gates

- Math home: `working/premature-belated-duality.md` (2026-04-23) — two-curve
  formalization, empty-binding-window, its own anti-inflation fuse; §5.1 parks the
  c(t) side "until Paper 26."
- Paper sibling: Paper 26 candidate (owns the *formal duality / paper*; this owns
  the *governance / ToolTheory object*).
- Memory: `project-residue-custody-candidate.md`.

**Promotion gate.** Any of the following is a phase change and requires reopening
the c(t) gate in `premature-belated-duality.md`:

- cited by P26 / ToolTheory as support,
- imported by real code as authority,
- treated as a governed artifact by tests/CI,
- names stabilized into doctrine,
- repo gravity (other files conform to it).

`recovery-topology-lock` is a floated name with **zero repo hits** — do not cite
it as existing.
