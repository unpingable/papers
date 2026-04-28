# Paper 26 — Candidate Claims

## Primary candidate

**Candidate claim:** Premature commitment and belated consequence are dual orientations of Δt detachment, formalized as two curves on the temporal axis. m(t) is admissibility maturity (readiness to bind); c(t) is consequence viability (whether action still has consequence). The valid binding window is W = { t | m(t) ≥ θ_m ∧ c(t) ≥ θ_c }. Failure modes:

1. *Premature* — binding at t with m(t) < θ_m.
2. *Belated* — binding at t with c(t) < θ_c.
3. *Empty window* — W = ∅; no admissible binding ever exists for this binding event.

**Status:** scaffolded — paper-shaped after formalization pass (chatty math 2026-04-23). Decision still deferred: this could become Paper 26 proper, a Substack piece, or a book chapter. The §6 empty-window test is the promotion gate.

**Imports:**
- Paper 15 — premature commitment instances (commitment can become irreversible before verification could possibly complete).
- Paper 2 — belated consequence at the 10-20y scale (compliance-vs-reputation lag).
- Paper 18 — hysteretic lock-in (T7).
- Paper 13 — premature consensus / commit before quorum.
- Paper 19 — premature remediation; ratchet deepening.
- Paper 22 — four-layer decomposition is *orthogonal* to this pair (asks which layer fails, not which direction the gap opens).
- Paper 16 — signed geometry (orientation but not yet used to place premature/belated as opposite orientations).

**Depends on:**
- §6 empty-window case testing producing concrete instances.
- Curve-shape / operating-point distinction not collapsing under scrutiny.
- `working/six-meets-six.md` partial-overlap analysis between binding-event six-tuple and admissibility-family six (currently not assumed identical).

**Risk:**
- Curve-shape distinction collapsing → folds back to §-insert in Paper 15 or Paper 22.
- Asymmetric-power moves ("power buys time twice") becoming the emotional center and dragging the paper into chronopolitics rather than formalism.
- "Much math, such control theory" prestige fog. The math has to distinguish cases prose would blur. If it doesn't, keep as architecture prose.

**Do not accidentally merge with:**
- Paper 25 (spatial substitution under observability asymmetry). P26 is the *temporal* sibling — both negative results in same family, distinct mechanisms. Do not let P26 absorb the substitution argument.
- Paper 22 (four-layer decomposition). Orthogonal axis; P22 asks *which layer* fails, P26 asks *which direction* the temporal gap opens.
- The book volume *Chronopolitics*. Adjacent thematically; the paper is the formal claim, the book chapter is the worked-out narrative. Don't conflate.

## Four asymmetric power moves

When the curves are not party-symmetric, power buys time twice:

1. Compress own admissibility (mature faster than legitimacy can certify).
2. Preserve own consequence (extend the window during which action still bites).
3. Slow others' admissibility (deny others maturity needed to act).
4. Accelerate others' consequence decay (let others' window close before they reach maturity).

## Descendant relation

P27 retention horizons (H : Obligation → Horizon) may cite m(t)/c(t) framing for evidence/causality/substrate-accusation horizons. P27 should *not* absorb the full premature/belated duality; it imports horizons, not the temporal-seam argument.
