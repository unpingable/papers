# Coalition-Bound Hardball
## Admissibility under coalition viability constraints

**Status:** Applied instance / working note. **Not a primitive candidate.** Not a Lean module. Not a doctrine promotion. No memory pointer yet — the note carries the weight first. Filed 2026-05-11 because it usefully demonstrates the admissibility machinery transferring into coalition politics without requiring new theoretical apparatus.

## Specimen

Online thread about Democratic Party hardball strategy: should Democrats match Republican procedural escalation (court packing, filibuster elimination, aggressive redistricting, election-certification brinkmanship)? Multiple voices argued versions of the same constraint:

- The median voter / coalition / legal environment doesn't permit "just become ruthless powermaxxers"
- Even if escalation is technically possible, it may exit the party's viable coalition space
- Voters who punish failure-to-escalate may also punish escalation itself

The thread crystallized a recurring failure mode in online political reasoning: treating tactic availability as substrate-independent when it is in fact coalition-bound.

## Formal mapping

The predicate: `H ∈ A_P(t)` — tactic H is in the survivable action set for party-system P at time t.

The empirical observation:

```
Republican hardball ∈ A_R(t)
Democratic hardball ∉ A_D(t), or only barely
```

`A_P(t)` is not "what P thinks is okay." It is the set of actions P can execute without destroying its coalition viability, legal pathway, donor/media tolerance, candidate discipline, or persuadable-voter margin. The substrate condition is *coalition metabolic capacity*, not normative permission.

The "Republican switch fantasy" — *they did it, so we can too* — silently assumes `A_R(t) = A_D(t)`. The fantasy fails because coalition substrates differ:

- Republican coalition has metabolized procedural vandalism as strength, necessity, or vengeance
- Democratic coalition contains substantial voters, donors, lawyers, judges, institutionalists, and norm-adherents who experience the same act as disqualifying

Same tactic, different admissibility, because different substrate. The structural refusal is *kind-blindness laundered into a universal claim*.

## Forecasting analogy: sabermetrics and fixed move-sets

Conventional forecasting estimates outcome likelihood conditional on a presumed action menu. Coalition-bound hardball asks whether the tactic is available at all. The sabermetric analogy is useful up to the point where rules, roles, and event categories remain stable.

Sabermetrics works best when:

- rules are stable
- roles are legible
- events are enumerable
- performance is repeated
- the action-space is mostly fixed

Coalition politics breaks that because:

- the rules are contested
- the audience is part of the plant
- legitimacy changes the payoff matrix
- the tactic can alter the coalition that must execute it

The forecasting error is analogous to applying a performance model while treating the playbook as fixed. Coalition politics requires modeling not just expected electoral payoff, but whether the tactic remains inside the coalition's viable action set. *The move is not merely chosen; it must be metabolized.*

## Inconsistent licensing pressure (sub-observation, flagged)

A sub-observation worth flagging separately from the main mapping: voters apply *inconsistent* admissibility pressure to the same action.

```
Voters demand outcome O.
O requires tactic H.
H exits A_D(t) for enough voters that O becomes less reachable.
The same voters then punish failure to obtain O.
```

This is not hypocrisy exactly. It is coalition members applying contradictory licensing constraints — punishing both `Y` and `¬Y` — without internal coordination among the licensors.

This shape may exist in other domains: Putnam's two-level games (domestic vs. international pressure with no joint admissibility), corporate governance with conflicting stakeholder constraints, regulatory capture vs. populist accountability dynamics. If it surfaces in two or three more domains with clean forcing cases, it may earn a separable primitive slot — *inconsistent licensing pressure* or *multi-licensor incoherence*.

For now: flagged, not promoted. This candidate does not yet have its second forcing case.

## Relation to the admissibility family

This rhymes with FiatAdmissibility but does not reduce to it. The substrate condition is different:

- **FiatAdmissibility:** artifact-kind licenses use (structural, time-independent)
- **Coalition-Bound Hardball:** coalition substrate licenses tactic-use (substrate-dependent and time-indexed)

Both belong to the broader superclass *admissibility under viability constraints* (see [admissibility-decay-family-note.md](admissibility-decay-family-note.md)). Same family resemblance; different axis. The kernel theorems from FiatAdmissibility (e.g., `prestige_cannot_support`) don't directly apply, but the *structural refusal* they encode is the same shape as the rejection of the "Republican switch fantasy."

Cleaner bridge phrasing:

> Normative entitlement does not license operational tactic-use unless the coalition substrate can survive the tactic.

This sits adjacent to but outside the five-axis family of stale-license primitives. It exercises the same admissibility apparatus, with a substrate condition the existing family members don't directly cover (live coalition metabolism rather than artifact-kind, signal-shape, witness-standing, commitment-scale, or composition-scope).

## Keeper line

> **Power is not what your side is morally entitled to do. Power is what your coalition can survive doing.**

Maxim form. Separates normative entitlement from operational admissibility. Same generic shape as "testimony does not admit its preferred theory of itself" and "the dashboard had no standing." The substrate condition here: *survivability under coalition metabolic constraints*.

## Anti-collapse note

Do **not** mint *CoalitionAdmissibility* as a primitive unless multiple cases require it. This is a worked example demonstrating that existing machinery transfers cleanly, not a new department.

The discipline:

- Useful as an application instance
- Provides a smoke test for the admissibility-family superclass
- Demonstrates the kernel has transfer beyond its originating domain (philosophy of mind / methodology)
- Does NOT extend the kernel, propose a Lean module, or add to MEMORY.md

If a second domain produces the same coalition-substrate-metabolizes-tactic shape with a different specimen, this note can be promoted to candidate primitive territory. Until then, it remains an instance.

---

**Cross-references:**

- [admissibility-decay-family-note.md](admissibility-decay-family-note.md) — family superclass; this instance is adjacent (different substrate condition), not a member
- [commitment-standing-decay-candidate.md](commitment-standing-decay-candidate.md) — sibling under the broader viability-constraint framing; uses the same `A(t)` apparatus
- [signal-authority-candidate.md](signal-authority-candidate.md) — adjacent primitive (silence-shape admissibility); the cross-substrate extrapolation here parallels the "unauthorized protocol extension" failure mode there
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — kernel whose structural refusal rhymes with the rejection of the "Republican switch fantasy"
- `project-control-set-laundering.md` (memory) — cross-substrate extrapolation failure; the "they did it, we can too" reasoning is a control-set-laundering specimen at coalition scale
