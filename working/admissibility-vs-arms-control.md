# Admissibility vs arms control — nuclear command as specimen bridge

**Filed:** 2026-06-06 (Fri PM). **Status:** doctrine note + specimen bridge. **NOT** a candidate kernel. **NOT** Lean. **NOT** to be promoted into the `LeanProofs/Admissibility/` family yet — *curdle for a day before it becomes another cursed little theorem gremlin* (operator directive).

**Custody:** doctrine note; pre-ratified per name-early. Companion to [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) (the witness-obligation constraint this elaborates lives most naturally as a *cross-cutting refinement* of the obligation atoms — same-custody is not a new obligation, it's a *quality* the witness-source must have for any obligation to be honestly discharged). Memory pointer: `project-admissibility-vs-arms-control`.

## The reconciliation

The arms-control framing applies to **supply-side capability mobilization**: compute, labs, sovereign actors, concealment, defection incentives, verification regimes. This layer is geopolitical and coordination-heavy. *Bring snacks and a legal department.*

Admissibility applies on the **demand-side of authority conversion**. An institution does not need to prevent dangerous artifacts from existing; it can refuse to treat them as sufficient for an effect.

The clean formulation:

> **You do not have to prevent the artifact from existing.**
> **You only have to prevent it from being sufficient.**

So the corpus's refusal kernels are not miniature arms-control treaties. They are **acceptance rules**:

- This model output does not discharge `MayAct`.
- This receipt does not discharge `Fresh`.
- This citation does not discharge `Exists`.
- This label does not discharge `MayEnforce`.
- This confidence score does not discharge `Observed`.
- This dashboard does not discharge `Authority`.
- This after-the-fact validation does not discharge `AuthorizedAtTransition`.

The adversary can generate infinite key-shaped objects. Fine. **The lock only turns for a witness-shaped object.**

## The core rule

> **Same-custody artifacts cannot witness each other.**

A trusted display, signed message, dashboard, model output, alert, or workflow artifact may still be inside the same failure cone as the system that produced it. To discharge an operational predicate, the witness must come from a custody chain with independent failure modes.

This is the load-bearing constraint on every other refusal kernel. The obligation-set framing in [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) says what a witness must *preserve*; this rule says what a witness must not be — *the same source as the artifact under verification*.

## The two specimens

### NORAD 1979 — trusted-channel artifact fails because independent witness absent

A training tape entered the live warning/display path at NORAD. Screens at three command centers showed a full Soviet first strike. The artifact was *perfectly key-shaped*: it came from inside the trusted system, through trusted channels, rendering on trusted screens. Air-defense aircraft scrambled; NEACP launched; threat-assessment machinery spun up.

What did NOT happen: nuclear-armed aircraft were not activated; no increased alert measures were ordered for U.S. nuclear forces. **Some predicates discharged, the nuclear predicate did not.** The official SecDef memo records that the *absence of corroboration from DSP satellites and radar* is what avoided precipitous nuclear reaction. Source: U.S. Office of the Historian, FRUS 1977-80 v04 d167.

The kernel:

> **`LiveSystemDisplay` does not discharge `ObservedAttack` unless corroborated by an independent sensor family with separate custody and failure modes.**

Same-custody refusal in operation. The training tape and the display were in the same custody chain; the corroboration check demanded a second chain.

### Petrov 1983 — instrument verdict fails because verdict is not attack-shaped enough to discharge escalation

Oko satellite system reported five U.S. missile launches. The formal acceptance rule the system encoded *would have passed*: the satellite verdict discharged the system's predicate as written. Stanislav Petrov refused escalation on three grounds: (1) a real first strike would not be five missiles — wrong attack-shape; (2) the new system had no track record — *system maturity* counts against a single-instrument verdict; (3) the verdict was artifact-shaped rather than observation-shaped — later determined to be sunlight reflecting off high-altitude clouds. Source: Arms Control Association obituary.

The kernel:

> **`SensorReport` does not discharge `StrategicAttack` when attack-shape, system maturity, and independent confirmation fail.**

Petrov's refusal was an admissibility check the system did not encode. *He was the kernel the institution lacked.*

### The doctrine pair

| Specimen | Failure mode | Refusal kernel |
|---|---|---|
| **NORAD 1979** | Trusted internal artifact passes a too-loose acceptance rule | Display ≠ Observed without independent custody chain |
| **Petrov 1983** | System verdict passes its own predicate; the predicate that mattered was unencoded | Sensor report ≠ Strategic attack without attack-shape + maturity + corroboration |

Both arc back to the same root: *the institution's acceptance rule was narrower than reality required.*

## The keeper

> **Encode what Petrov did, so survival does not require Petrov.**

This is the entire program in one sentence. Refusal kernels are the institutional version of Petrov's judgment, formalized so the institution does not have to be lucky enough to have one Petrov at the right console.

## The modern analogue

> **`ModelOutput` does not discharge `MayAct` merely because it arrived through an official workflow.**

> **`ManagerApproved` does not discharge `Witnessed` unless the manager's approval is itself bound to a typed observation.**

Workflow trust is the modern NORAD training tape: the artifact comes through trusted infrastructure, rendering on trusted dashboards, signed by trusted-enough principals. None of that is independent witness. The acceptance rule must demand a custody chain that does not share failure modes with the rendering system.

## Override discipline

Overrides should be possible (institutions need release valves) — but every bypass should mint a custody-bearing artifact:

```text
Override(actor, time, predicate_bypassed, reason, evidence_considered)
```

The bypass is then **admissible against the bypasser**. The door's failure mode feeds the next adjudication. *Manager approved, full stop* is laundering; *manager-approved-with-typed-override-receipt-bound-to-this-specific-bypass-context* is custody-honest.

This is the *logged and embarrassing* clause from the operator's evasion list (route 4: human override laundering). The defense against forged witnesses (route 3) is the same shape: forged witnesses also leave receipts in a system where receipts are the whole game.

## Evasion landscape (operator's 6-route list)

This doctrine does not pretend to be unevadable. The local lock can be routed around by attacking the environment:

1. **Forum shopping** — find an institution without the refusal. *(Defense: the refusal is locally ratifiable; the corpus doesn't claim universality.)*
2. **Policy capture** — redefine the predicate until garbage passes. *(Defense: Lean kernels — prose refusals drift; type signatures don't.)*
3. **Witness forgery** — create fake provenance/custody. *(Defense: same-custody rule — forged witnesses fail the independent-chain check.)*
4. **Human override laundering** — *"manager approved,"* no real observation. *(Defense: override-as-typed-receipt; bypass becomes future exhibit.)*
5. **Pressure substitution** — *"accept this artifact or fall behind."* *(Defense: name the pressure as a predicate that does not discharge witnessing; record route 5 explicitly.)*
6. **Semantic drift** — refusal survives in wording but loses operational bite. *(Defense: the curdling pipeline; Lean kernels are the corpus's hedge against this exact attack.)*

The doctrine is not *"install one magic door."* It is:

> **Make the accepting surface narrow, typed, witnessed, logged, and embarrassing to bypass.**

## Relationship to existing corpus artifacts

This doctrine **constrains** every refusal kernel without **replacing** any:

- [`bridge-obligation-lattice.md`](bridge-obligation-lattice.md) — obligation atoms (non-amplification / temporal-bounding / type-fidelity / freshness / anti-precedent) say what a witness must preserve. *Same-custody* is the quality the witness-source must have for any of those preservations to be honestly discharged.
- [`tooltheory/witness-carrier-model-candidate-2026-06-06.md`](tooltheory/witness-carrier-model-candidate-2026-06-06.md) — the witness-carrier model's `MayMint` predicate already has the *"subject cannot be sole standing source"* consequence; this doctrine generalizes it to *"any same-custody source cannot be sole witness."*
- [`tooltheory/documentation-keepers.md`](tooltheory/documentation-keepers.md) § Multi-clause doctrine blocks — *"Lean kernels may identify/refuse a formal conversion; NQ gaps are discharged only by receipt, verdict, export, or runtime behavior."* This doctrine adds: *and the witness-source for any of those discharges must come from a custody chain independent of the system being witnessed.*
- [`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md) § The audit unit — *"this evidence does not discharge that predicate"* is the meta-rule; same-custody-refusal is one specific reason a piece of evidence fails to discharge its predicate even when it looks the part.

## What this is NOT (curdling guard)

- **Not a candidate Lean kernel yet.** The doctrine is too rich; formalizing it now would prematurely pin which obligation lattice axis carries the same-custody constraint. Let it sit.
- **Not a new bridge family.** The bridge-obligation lattice already covers the families; same-custody is a *transversal quality* across them, not a new family.
- **Not a claim about geopolitical arms control.** The reconciliation positions admissibility as the *demand-side counterpart* to supply-side arms control; it does not claim arms control is unnecessary or that admissibility scales globally. Local leverage, not universal coverage.
- **Not a Petrov-veneration note.** The doctrine sentence is *encode what Petrov did, so survival does not require Petrov.* If anything, the institutional discipline is the corpus's hedge against having to find Petrovs.

## Provenance

Filed 2026-06-06 (Fri PM) from a multi-model exchange:

1. ChatGPT surfaced the supply-side / demand-side reconciliation, the 6-route evasion list, and the *"narrow, typed, witnessed, logged, and embarrassing to bypass"* formulation.
2. Claude (web?) elaborated NORAD 1979 and Petrov 1983 as worked specimens, surfaced the *"same-custody artifacts cannot witness each other"* compression, the *"encode what Petrov did"* keeper, and the override-as-typed-receipt defense.
3. Operator pulled in the historical correction (1979 nuclear bombers did not launch; some predicates discharged, the nuclear one didn't), the *"trusted channel ≠ independent witness"* sharpening, and the curdling-before-Lean discipline.
4. Claude Code (this session) filed the consolidated doctrine note with cross-references to the existing corpus artifacts and the audit-loop discipline preserved.

The historical sources are cited inline:
- U.S. Office of the Historian, FRUS 1977-80 v04 d167 (NORAD 1979)
- Arms Control Association, *"The Man Who 'Saved the World' Dies at 77"* (Petrov 1983)

## Definition of done

> *A reader can use this note to refuse a same-custody artifact in their own institution without having to be Petrov.*

Test: read the doctrine pair + the modern analogue + the override discipline. Can you write the refusal rule for your own workflow without re-deriving the framing? If yes, done.

## Curdling timer

> Operator-imposed: do not formalize into Lean before 2026-06-07. *Cursed little theorem gremlins are a separate file from this one.*
