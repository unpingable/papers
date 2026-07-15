# Standing as authorized readout; NoFreeStandingReadout (candidate)

**Filed:** 2026-06-15. **Status:** doctrine note — **DELTA only.** The freshness/standing split
is NOT re-derived here; it is already held by [`vector-mining/2026-06-05-attack-04-freshness-vs-standing.md`](vector-mining/2026-06-05-attack-04-freshness-vs-standing.md)
and [[project-admissibility-decay-family]]. This note records what that prior work does NOT
contain. The candidate theorem (`NoFreeStandingReadout`) and the regress are **name-early,
UNRATIFIED**. Formal work may proceed once the kernel-overlap audit below resolves its
identity and the theorem has a precise, non-vacuous model with proof controls; no runtime
forcing case is required. Public promotion remains a separate custody decision.

## What is already held (do not re-derive)

- "standing" is a **lexical fracture** — three relations (state-fact / operational /
  provable-now); expired freshness destroys evidence-side discharge, NOT standing-fact
  (attack-04, Freshness.lean header keeper).
- The federation gate **fires preventively** against any unifying primitive on the standing
  axis (`FreshStanding`/`StandingFreshness`). [[project-no-unifier-without-laundering]].
- `dS/dt = -λS` for standing is refused: it is freshness in a standing costume. Standing is
  have-it-or-don't; where time touches it, it touches as a **cliff** (statute of limitations
  = deadline, not exponential), never a slope.

This note does NOT mint a standing-axis primitive. It splits standing FROM a separate
substrate (maintenance) and keeps standing categorical — the opposite of the laundering the
gate guards. It passes the gate for that reason; if a future edit starts unifying the three
standing senses, the gate refires.

## DELTA 1 — synchronic standing vs diachronic maintenance

The Δt split, applied to this axis:

> **Standing is synchronic** (Boolean at the decision instant). **Maintenance is diachronic**
> (it evolves continuously/discretely between decisions). **Standing is the lossy, authorized
> readout — the collapse — of the maintenance trajectory plus categorical events, taken at
> the decision instant.** The verdict does not carry a scalar across the surface; it measures
> the scalar there and emits a category.

```text
MaintenanceTrajectory(subject, scope, t₀..t)   -- diachronic, may have rates
DirectCategoricalEvents(subject, scope, ≤t)     -- instant, no accumulator
GrantState / DeclaredOrder(root)
        ↓ governed readout (a GOVERNED act — see DELTA 3)
StandingVerdict(subject, scope, t) ∈
    { Full | Advisory | ObservationOnly | Quarantined | Revoked | NoStanding }
```

**No fractional standing at the effect surface.** Not because convention forbids 0.7, but
because *measurement* does — you cannot run an amplitude through a detector. Calculus may
govern the arcs **between** standing decisions; it may not be the public authority predicate.
The analogy is **credit, not citizenship**: you are not 37% a citizen, but accumulating
exposure can flip your categorical status.

## DELTA 2 — the maintenance scalars are typed, with two hard rules

Not a garbage-bag "trust score" (vibes with decimals; enterprise-SaaS smell). The dynamical
things are distinct kinds (same anti-garbage-bag discipline as the `Emission` split in
[[governance-kernel-scope-correction]]):

| Dynamic thing | Accrues by | Directly revoke? | Role |
|---|---|---|---|
| **Budget** | use/spend | no | limits reliance/effect volume |
| **Maintenance debt** | missed upkeep/audits | only via readout | downgrade/refusal at measurement |
| **Contradiction pressure** | external conflict | usually no | forces revalidation/escalation |
| **Disqualifying fact** | witnessed categorical event | **YES** | immediate revoke/quarantine |
| **Hazard** | forecast/inference | **NO** | scheduling, warning, preflight only |

Two load-bearing rules:

1. **Direct categorical paths must bypass the accumulator.** `RootRevocation`,
   `OfficeDissolved`, `ScopeTerminated`, `KnownLie`, `KeyCompromise`, `CustodyBreak` set
   `standing := revoked/quarantined` *immediately* — not `debt += 1`. Otherwise a witness
   caught lying once keeps standing until pressure crosses θ: **a known liar rendering as
   ok**, the NQ sin, in a risk-dashboard costume (tiny bar graph over a corpse). One proven
   lie is revocation now, not contradiction-pressure.
2. **Hazard must never push the transition.** Hazard estimates distance to the cliff; it is a
   forecast, not a state that crosses it. Let it push and a *guess* triggers a revocation —
   pre-crime, unwitnessed inference driving an effect (actuarial governance with a badge).
   Hazard rings a bell; it does not swing the axe.

## DELTA 3 — readout is a governed act → NoFreeStandingReadout (candidate)

The measurement metaphor's landmine: the detector is NOT "whoever looks." An unauthorized
observer minting public reality is **observer laundering**. The reader needs authority to
read:

```text
CanRead(reader, subject, state)      -- capability
MayReadout(reader, subject, scope)   -- authority
        CanRead ⊬ MayReadout         -- the refusal
```

**Candidate theorem `NoFreeStandingReadout`:** latent/process state does not become public
standing merely because someone can observe it. Sibling (NOT replacement) to
NoFreeStandingBridge:

- Bridge: *local validity does not lift across a boundary without an authorized crossing.*
- Readout: *latent state does not become public standing without an authorized reader.*

Different seam, same family — see [[no-free-standing-bridge-schema]] (and the meta-bridge
guard: family resemblance, NOT a reduction). The four laundering moves the readout family
names: **capability laundering** (CanRead⇒MayReadout), **observer laundering** (looked ⇒
public reality changed), **void ratification** (verdict valid because it exists), **root
smuggling** ("proven" when actually stipulated).

### The regress (the theorem-shaped part — belongs in Lean)

```text
MayReadout(reader, ...)  requires  Standing(reader, ...)
Standing(reader, ...)    requires  an authorized readout
```

So a standing verdict requires an authorized reader whose authority is itself a standing
verdict → **no non-root readout is free-standing**; it bottoms out in regress, circularity,
or a stipulated root (Münchhausen, governance helmet). The regress is **not a defect — it is
the kernel's own commitment biting**: it holds *because* we refuse to let capability ground
authority. "Fix" it by letting `CanRead` ground `MayReadout` and you have reintroduced
capability-laundering. Keep the regress.

Root clause, brutally explicit (= [[governance-kernel-scope-correction]]'s validity-under-
declared-order, now with its formal backing):

```text
RootReadout is stipulated by DeclaredOrder.
RootReadout is NOT internally legitimated by DeclaredOrder.
```

The root can rule; it just signs the receipt instead of wearing evidence as a costume.

## KERNEL-OVERLAP AUDIT (must clear BEFORE any build)

`NoFreeStandingReadout` is **not clean-slate.** Classify against
[`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md) and resolve overlap, or
we mint a duplicate (orphan-doctrine acne):

- **[[project-custodian-binding-accountability-candidate]]** (`custodian-binding-accountability-candidate.md`):
  `ObservationEdgeExists ⊬ AccountableCoverage` is structurally near-identical to
  `CanRead ⊬ MayReadout`. **Open question:** is custodian-binding the *synchronic atom* and
  NoFreeStandingReadout the *version-with-regress*? Do NOT build both as separate kernels
  until this is decided. Likely outcome: one kernel, two faces — the `CanRead⊬MayReadout`
  countermodel is the custodian-binding theorem; the regress is the genuinely new addition.
- **NoFreeStandingBridge** — sibling seam, confirmed distinct (lift vs readout).
- **SurfaceAuthorization** (force-on-envelope vs derived-by-reader) — adjacent; the reader-
  derives-the-verdict shape overlaps.
- **[[project-signal-authority]]** (silence ≠ revocation) — adjacent on the readout-absence side.

## FENCE — physics is heuristic, not proof (do not remove)

The Heisenberg-cut ↔ rule-of-recognition correspondence is **abductive**: it found the
basement door; it does not prove the door is there. **Admissible as heuristic, inadmissible
as proof** — signed is not witnessed, turned on our own method. So:

- **Book** gets the analogy ("the measurement problem said look here") — armored as
  *structural identity / same regress shape*, NEVER "same problem" (that drags you into
  Many-Worlds/QBism/objective-collapse mud; nobody leaves clean).
- **Lean** gets the regress that survives **with the physics deleted**. That deletion is the
  test of whether the artifact is real. No physics in the formal layer, not even as flavor.
- Tape this where the crystals would go: *the proof is the regress that remains after the
  physics is deleted.*

## Provenance / common-mode caution

Multi-model arc, 2026-06-15 (the user's own "trying to smuggle calculus back in" → DeepSeek's
`dS/dt` smuggle caught → ChatGPT's maintenance-vs-standing salvage → Claude's
synchronic-collapse + regress → the physics-identity overclaim caught and armored twice).
**Heavy Claude-web synthesis** — the physics-identity line is the highest common-mode risk
and is fenced above; do not let a Claude-Code pass inflate it past the heuristic armor. The
buildable residue (maintenance/readout architecture + the regress) is what survives the
deletion test; the rest is book.
