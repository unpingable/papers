# Calculus 2.0 — tier map (2026-05-28)

**Status (split, per ChatGPT 2026-05-28 correction):**

- **Calculus 2.0 *core* (wound + bridge + trajectory + forgetful map + no-lift):** ratifiable now, gated only on the kernel-overlap audit and an exit-criteria update in `working/calculus-2-exit-criteria.md`. The skeleton has earned itself; tier-2 specimens are not needed to prove the second axis exists.
- **This tier map:** candidate until a tier-2 specimen (2A or 2B) lands and the orthogonality claim survives contact. The map's *topology* (4 tiers, 2A/2B orthogonal) is the part requiring future-evidence; the *core* it describes does not.

Filed at journal density per `working/tooltheory/` convention. Not ratification; the live source of truth is the Lean stack at `~/git/lean/LeanProofs/Admissibility/`.

**Provenance:** Multi-model conversation 2026-05-28 (Claude Code main thread, Claude opus 4.8 on web, ChatGPT-conservative). The tier framing emerged after the attestation-ledger second witness landed and the question "what's next?" forked into two genuinely different generalizations.

---

## The map

```
Tier 0 — minimal separation
    Receipt/poison model (Bool, Unit actor).
    Files: LeanProofs/Admissibility/AuthorizedNotSafe(Witness).lean
           LeanProofs/Admissibility/SafetyBridge.lean
           LeanProofs/Admissibility/SafetyBridgeWitness.lean
           LeanProofs/Admissibility/AuthorizedStepNotSafe(Witness).lean
           LeanProofs/Admissibility/SafetyTrajectory.lean
    Shows: authorized step can lose value; bridge can exclude wound;
           verdict-layer wound transfers from StepAllowed-layer wound;
           trajectory triple (positive / negative / no-lift).

Tier 1 — second concrete witness
    Attestation-ledger (Nat-valued, two asymmetric actors).
    File:  LeanProofs/Admissibility/AttestationLedger.lean
    Shows: generic SafetyEnv instantiates over a second textured model;
           role-based actor authorization coexists with actor-inert
           bridge (ρ-drop confirmed on non-degenerate evidence);
           per-hop actor in trajectory type expresses multi-actor paths
           as single trajectories (the brick-2 trajectory-global actor
           is a limitation now visible at tier 1).

Tier 2A — value-axis generalization (NOT BUILT)
    Budget-margin model.
    Forces: non-decrease invariant → floor / preorder.
            Theorem-shape rewrite: bridgedTraj_preserves becomes
            "trajectory stays above floor" rather than "value
            non-decreasing." Value codomain may generalize Nat → Preorder.
    Scope:  value semantics, not authorization geometry.
    Trigger condition: a concrete model needs to express legitimate
                       value-decreasing actions (budget spend, retry-
                       token consumption, etc.) without classifying
                       them as wounds.

Tier 2B — authorization-axis generalization (NOT BUILT)
    Quorum model.
    Forces: role authorization → certificate authorization;
            local bridge + global state invariant + intersection lemma
            inside preserves; bridge stops being constructor-inspection.
    Scope:  certificate geometry, not value texture.
    Trigger condition: a concrete model needs collective authorization
                       (cert/quorum/vote), with safety depending on
                       relational/historical facts across certificates
                       (e.g. quorum intersection ⇒ no conflicting
                       commits) that no local action-shape check can
                       capture alone.
```

**Orthogonality.** 2A and 2B are sibling stressors. Neither gates the other. Budget tests value texture on simple auth; quorum tests cert geometry on simple value (binary no-conflict). Pick by which generalization the next forcing case demands.

## Tier 2B design pins (pre-committed, to prevent re-litigation)

Filed now because the certificate-in-α move is the same logic as the ρ-drop's own escape hatch, and committing to it pre-empts the most likely wrong turn:

1. **Certificate as action payload.** `commit (x : Value) (cert : Cert)` puts the cert inside `α`. Both `Allowed` and `bridge : σ → α → Prop` read it from `α`. No κ parameter, no ghost actor index.
2. **Bridge stays local cert-validity.** Not "this cert vs all prior commits" (that would be relational and re-open `bridge_preserves` shape).
3. **Quorum intersection lives inside `preserves`, not the bridge.** `preserves` carries an inductive state invariant ("all committed values agree") whose maintenance uses the intersection lemma. The bridge stays the local sufficient-condition check.

If these pins survive the actual tier-2B brick, the ρ-drop is confirmed across both generalization axes.

## What this map does NOT claim

- It does not promise tier 2A and 2B can be composed (a unified "Calculus 3.0" with both generalizations layered) — that's a question for after both land.
- It does not claim the tier ordering is conceptual; tier numbers are taxonomic, not sequential. The actual build order will be set by which forcing case arrives.
- It does not justify minting "Calculus 2.0" publicly — that still gates on the kernel-overlap audit and the `working/calculus-2-exit-criteria.md` update.

## Known debt (track before public minting)

- **Trajectory-design divergence between brick 2 and tier-1 ledger.** `LeanProofs/Admissibility/SafetyTrajectory.lean` carries `AuthorizedTraj (a : Actor)` / `BridgedTraj (a : Actor)` — trajectory-global actor parameter, the inferior shape. `LeanProofs/Admissibility/AttestationLedger.lean` carries `LedgerAuthTraj : Ledger → Ledger → Type` with actor as a *field* in `LedgerAuthStep` (per-hop), expressing multi-actor paths as single trajectories. The divergence is invisible in brick 2 because that model has `Actor := Unit`, so it is not a bug — but it is a legibility liability for a candidate/paper (reviewers will ask why there are two trajectory designs) and the reconciliation (backport per-hop actor into `AuthorizedStepC` / `SafeAuthorizedStepC` and drop the `a` parameter from `AuthorizedTraj` / `BridgedTraj`) touches brick 1's downstream so is not free. **One canonical trajectory design before any public minting.** Web-Claude 2026-05-28 flagged this as the explicit debt item that should not stay as a docstring aside.

## Companion record

ρ-drop decision with ledger evidence: `safety-bridge-rho-drop-decision-2026-05-28.md` (filed same day).
