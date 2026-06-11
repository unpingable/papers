# Paper 6 — working notes / changelog

## v1.1 candidate (local source edits — NOT yet pushed to Zenodo)

- **2026-06-11** — Added a **Formalization Status** section to
  `Paper6_Temporal_Closure_v1.0.md` (between the Conclusion and References).
  Points at the Lean kernel `LeanProofs/Scratch/Paper6TemporalClosureKernel.lean`
  (scratch-checked, sorry-free, axioms = `propext` only) and folds in
  ChatGPT's pre-drafted v0.1 register paragraph verbatim, bracketed with a
  scope fence: the kernel formalizes the **necessity-side type boundary**
  (finite context cannot manufacture unbounded history; inert wrappers cannot
  manufacture autonomous ticks), with constructive accumulator / clock /
  product witnesses. **Sufficiency remains OPEN** and the kernel is **not** a
  load-bearing dependency of the paper's claims.
- **2026-06-11** — **Overclaim retired in source** (v1.1-candidate; Zenodo
  v1.0 left as historical artifact). Three claim-surface patches so v1.1 does
  not carry a known-false register state:
  1. **Abstract** (main paper + README): "minimal architectural requirements"
     / "necessary and sufficient" → "necessary architectural roles" + a
     necessity-side type-boundary statement + the blast-door sentence
     *"General sufficiency for identity-preserving coherence under perturbation
     remains an open formalization target."*
  2. **Conclusion:** "We have derived the minimal architectural requirements"
     → "We have identified the necessary architectural roles".
  3. **SI-A §8.2:** "Sufficiency" → "Constructive Feasibility"; the demo is
     constructive feasibility of the operator roles, not a theorem of temporal
     identity under perturbation.
  The Lean kernel is necessity-side only; the abstract no longer implies
  sufficiency, so "now formalized in Lean" cannot leak into an inflated claim.

- **2026-06-11** — **SI-A ε goblin fixed** (§Operator 1 + §4.2): `ε = 0.05`
  (≈ 20×) no longer billed as "satisfying the O(10²) requirement" / "O(10²)
  regime required by framework"; relabeled as qualitative timescale separation
  in the reference implementation, explicitly *not* the stronger `10²–10³`
  adjacent-layer scale cited elsewhere. Lean temporal-separation operator stays
  propositional until a numeric-invariant module exists.

## Before a Zenodo push (ratification-tier — operator's call)

- [ ] Bump `metadata.yaml` `version` and rebuild the PDF/DOCX.
- [ ] Bump README Status/DOI lines to match `metadata.yaml`.
- [ ] Decide whether SI-A erratum and/or the abstract overclaim are in scope
      for the same push.
- [ ] Mirror the v1.1 status in `docs/formalization-index.md` change log.
