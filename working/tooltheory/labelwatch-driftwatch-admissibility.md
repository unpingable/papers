# Labelwatch / driftwatch — admissibility doctrine

**Tool-specific application of the tooltheory canon to the observatory pair.** Filed 2026-05-12.

## Why these tools

Labelwatch and driftwatch operate across the whole admissibility ladder:

```
raw observations → features → findings → claims → public rhetoric
```

They sit close enough to messy social telemetry that the abstract admissibility moves get *field-tested* against real data, not polite control diagrams. That makes them the **anti-laundering testbeds** for the program. The discipline has to survive contact with Bluesky-shaped reality, or it's only good for diagrams.

## How the doctrine lands

### Labelwatch — pressure points

- **Feature → finding promotions.** Labeler co-occurrence is a feature. "Cartel" is a claim. Don't auto-promote.
- **Burst handling.** A spike of labels / reports / conflicts triggers regime-change witness; don't launder into *"we have detected coordinated abuse"* without a target witness.
- **Aggregation of labelers.** Multiple labelers ≠ multiple witnesses unless they have observability diversity (different source lists, different graphs, different taxonomies, different upstream automation). Per [heterogeneous-witness-cohorts](heterogeneous-witness-cohorts.md).
- **Public rhetoric closure.** Labelwatch findings should authorize investigation, further inquiry, or advisory caution; they should not authorize ontological closure (*"this is abuse"*) absent target-witness testimony.

### Driftwatch — vintage-control as canonical case

Driftwatch already encodes the discipline operationally. The vintage-control lesson is the worked anti-laundering case:

- The measured surface (label registry, PDS distribution snapshot, archival artifact) is real.
- The natural-sounding claim (*"this is the current locus"*) is not licensed by the surface — because the surface may be vintage / replica / archived.
- Discipline: *the measured surface was real; the claim attached to it was not licensed.*

Tooltheory gold: the discipline is operational, not abstract. It prevented a bad claim.

## Tool-side imports

What labelwatch and driftwatch can adopt from the kitchen as concrete rules:

- **Scope tags on findings.** Each finding carries an explicit scope statement — what witness population it testifies to, what claim domain it does and doesn't license.
- **Advisory verdicts as first-class output types.** *"This pattern warrants investigation"* is a different output than *"this is abuse."* Don't collapse them at the type level.
- **Burst classifier vs intent classifier.** Burst-detection outputs *regime-change witness*. Intent attribution requires a different witness with different scope.
- **Vintage-vs-live as a witness property.** Driftwatch already encodes this; the generalization is that any archival / replicated / snapshot evidence carries a vintage tag that limits the claim scope.
- **Heterogeneity-preserving aggregation.** Avoid mean-collapse over labelers that share substrate; preserve per-witness structure when scope matters.

## The thermal-paste rule

> You spread this stuff around like thermal paste — too little and the heat doesn't move; too much and now everything is disgusting and conductive in the wrong places.

Tooltheory holds the reusable boundary rule. Individual tools only import the rule when it blocks a real bad transition. Otherwise every project wakes up with a tiny Department of Admissibility stapled to its forehead. Very prestigious. Completely cursed.

## Promotion gate

When labelwatch / driftwatch implementation hits a specific case where one of these doctrines forms a load-bearing distinction the current code can't express — file the gap as a project-side spec in the relevant downstream repo, then decide whether to import the doctrine in or refine the doctrine to fit. Don't pre-emptively import.

Companions: [social-telemetry-claim-boundaries](social-telemetry-claim-boundaries.md) (general five-claim doctrine), [consequence-scoping](consequence-scoping.md) (rhetoric form), [proxy-shock-mismatch](proxy-shock-mismatch.md) (burst-handling sibling).
