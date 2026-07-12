# Constitutional optionality spend and self-entrenchment (candidate note)

*Status: UNRATIFIED-CANDIDATE, 2026-07-12. Composite doctrine + one kernel
candidate. Reclassification ratified by operator + ChatGPT same day.*

## The reclassification

"Irreversible spend" is **not a new primitive**. It is a derived condition over
existing machinery:

1. restoration misses the binding horizon → **P26 window machinery** (c(t)
   consequence-viability applied to the restoration action; `IrrevSpend(x,h)` =
   the recovery's binding window is empty; "nothing is metaphysically
   irreversible" = irreversibility is horizon-indexed);
2. recovery margin insufficient or consumed → `RecoveryMargin.lean` + v9
   Spendability capacity-linearity (missing only transition-level accounting);
3. continuity/capability needed for restoration lost → continuity/reliance
   family;
4. rollback rung unreachable → fork-modes contraction asymmetry;
5. **recovery authority captured → the one new atom** (below).

The first four are composition. Effect-layer irreversibility is already proved
(v9: *revoke provably can't reach the effect log*). The `(O, C, T, L)` state
tuple stays prose; no optionality calculus. Political-economy register
(Bell / fabs / payment rails) routes to P26 / book / Substack lane.

## The new atom: reversal-authority capture (self-entrenchment)

> **Transition x changes the state, then makes admissibility of reversing x
> depend on authority whose standing is causally downstream of x.**

Refusal: `effect(x) ∉ ancestors(authorityFor(recover x))`.

Rulings (operator, 2026-07-12):

- **Provenance, not motive.** No "beneficiary" in the kernel — benefit is
  interpretive; the load-bearing relation is causal/provenance dependence.
- **No `AuthorityOrigin := preexisting | minted` enum** — counterfeit rigor;
  the fixture would tell the theorem what it is supposed to discover. The
  classification must fall out of the trace.

Doctrinal placement: temporal-forward twin of RetroactiveLegitimation
(post-state **authority** gating pre-state **restoration**); Deform-family
aggravation (SurfaceDeformationRequiresCoupling governs frame mutation; the new
content is the self-reference — the deformed frame adjudicates the deformer's
own undo); distinct from control-path-independence (static capture) because
here the capture is *manufactured by the transition under review*.

## The specimen (BUILT, green, zero-axiom)

`~/git/lean/LeanProofs/Scratch/SelfEntrenchment.lean` — scratch,
compile-is-contact, all headline theorems axiom-free. Trace vocabulary:
`Ledger` (mintedBy / delegatedFrom / basisOf — ledger facts, not a
classification), `DownstreamOf` closure (direct mint, act hops, delegation
hops), `CanForceRefusal` / `Captured` (a gate is captured when the
x-downstream coalition can force refusal of x's reversal).

The five shapes, all discharged:

1. pre-existing authority independent (`elder_independent`);
2. direct mint downstream (`mintX_downstream`);
3. laundering fails at both hop types: delegation (`mintXDeleg_downstream`)
   and act hops — x mints a, a licenses act z, z mints the gate
   (`deepLaundered_downstream`);
4. **negative control:** created after x, independently grounded → NOT
   downstream (`postIndep_independent`) — causal dependence, not chronology;
   the "must predate the transition" proxy is refuted in **both** directions
   (`chronology_is_not_independence`: accepts a captured gate whose body
   predates x, refuses an independent gate created after x);
5. **mixed chains resolve by blocking power, not membership**: one downstream
   veto edge captures (`veto_gate_captured`); the same downstream member below
   a 2-of-3 quorum's blocking threshold does not (`quorum_gate_not_captured`,
   `downstream_membership_without_blocking_power_does_not_capture`).

Headline package: `transition_cannot_mint_its_own_reversal_authority`.

Case-5 resolution, stated once: **poisoning tracks blocking edges, not roster
presence.** The general n-of-k threshold claim stays prose until a consumer
asks.

## Gates

- **Scope:** no (O,C,T,L) formalization, no optionality calculus, no general
  quorum theory, no benefit/motive vocabulary.
- **Promotion:** scratch until register adjudication + a forcing consumer
  (AG governor verdict, NQ finding, or a transition-kernel obligation) needs to
  refuse a self-entrenching transition. Composite doctrine ("constitutional
  optionality spend") stays a recognition handle unless an existing home
  provably can't stretch.

## Scope fence

Possibilistic (capture = CAN force refusal), concrete fixtures, declared trace
vocabulary. Nothing here claims restoration economics, political feasibility,
or that entrenchment always succeeds — only that the authority calculus can
refuse the manufactured-reversal-gate shape, and that neither chronology nor
membership rosters are valid proxies for it.
