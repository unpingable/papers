# Δb — Boundary Error

**Status:** Validated spike
**Domain:** Regulating the wrong system boundary
**Compression:** Named the wrong system

---

## Definition

A controller draws its regulatory perimeter such that the mechanism determining outcomes falls outside the boundary. Interventions succeed *inside the perimeter* and fail *at the system level* — not because the interventions are weak (Δa) or the coupling is wrong (Δk), but because the boundary excludes the causal substrate.

## Δb vs Δk

These look similar and aren't.

- **Δk (coupling mismatch):** Given a boundary, the things on either side of it are coupled too tightly (cascade) or too loosely (no coherent response). The boundary is in the right place; the coupling across it is wrong.
- **Δb (boundary error):** The boundary itself is in the wrong place. You can have perfectly calibrated coupling analysis inside a perimeter that excludes the part that matters.

Δk is an engineering problem. Δb is a framing problem. You can't fix Δb by tuning the coupling — you have to redraw the perimeter.

## Failure Criterion

**A boundary is a Δb error when the excluded region contains the mechanism that determines outcomes inside the boundary.**

The perimeter encloses the effects and excludes the cause. Everything inside the boundary looks fine by the boundary's own metrics.

## Examples

**1. Presentation layer vs. absorption layer.** An analyst reads a geopolitical actor's public composure — diplomatic language, measured rhetoric, institutional calm — and concludes the situation is stable. The analytical boundary is drawn around the presentation layer. The absorption layer — downstream cost-routing, strategic load distribution, structural stress — falls outside the perimeter. The presentation layer *is* stable. The system isn't. The boundary excluded the substrate where instability accumulates.

**2. Encampment sweeps.** A city targets visible homelessness: clear the camp, disperse the population, restore the streetscape. The regulatory boundary is drawn around the visible symptom. The reproduction mechanism — housing costs, psychiatric system gaps, discharge-to-street pipelines — falls outside the perimeter. The sweep succeeds inside the boundary (camp is gone) and fails at the system level (population redistributes, camps reform). The intervention is regulating the presentation layer of a problem whose causal mechanism is elsewhere.

**3. Transit as psychiatric/housing overflow.** A transit agency draws its operational boundary around transportation: routes, schedules, ridership, fare recovery. The system it actually operates includes de facto shelter, psychiatric crisis absorption, and last-resort public space. The operational boundary excludes the functions the system is *actually performing*, so interventions optimized for transit metrics degrade the system's real load-bearing role — which then shows up as "transit problems" inside the boundary. The boundary creates the problem it then measures.

## Anti-Example

**A hospital ED that triages and refers out.** An emergency department draws a boundary: stabilize and refer. Chronic disease management, housing, addiction treatment fall outside its perimeter. This looks like Δb but isn't — the ED's boundary is *correctly scoped* because those functions genuinely belong to other systems that (in principle) exist. The ED is not excluding the mechanism that determines its own outcomes; it's handing off to the appropriate system. Δb applies when the "appropriate system" doesn't exist or doesn't function — when the referral target is fictional, the boundary becomes a Δb error because "refer out" is actually "exclude from perimeter and pretend someone else handles it."

The anti-example shows the criterion's edge: the same boundary can be correct or erroneous depending on whether the excluded region actually has a functioning controller. Δb is not "your scope is narrow." Δb is "your scope excludes the thing that determines your outcomes."

## Why This Matters

Δb errors are invisible from inside the boundary. Every metric scoped to the perimeter confirms that the intervention is working. The sweep cleared the camp. The rhetoric analysis shows composure. The transit KPIs are on target. The failure only appears when you measure at the system level — and the boundary was drawn precisely to avoid doing that.

This is what makes Δb different from operational failures: you can't fix it by doing the same thing better. Tuning gain (Δg), strengthening actuation (Δa), tightening coupling (Δk) — all of these optimize inside a perimeter that's in the wrong place. The only repair is redrawing the boundary to include the causal mechanism. Which is hard, because the boundary was usually drawn where it is for political, institutional, or cognitive reasons that resist revision.
