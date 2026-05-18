# Cargo-Culted Engineering: SRE as Shock Absorption Layer

*Draft — 2026-04-20*

## The inheritance problem

Feynman's cargo cult science wasn't fraudulent. It was something more specific: the *form* of a practice preserved after the *function* had been stripped out. Runway lights and coconut headphones organized behavior, focused attention, and produced the appearance of competent infrastructure. What they couldn't do was make planes land. The planes landing had never been about the runway lights.

The claim of this essay is that a similar substitution happened inside reliability engineering over the last fifteen years, and that naming it accurately matters — both because the substitution is costing real operational capacity, and because the people paying the cost are largely invisible to the measurement apparatus that replaced the engineering they used to do.

Specifically: Site Reliability Engineering, as exported from Google into the broader industry, cargo-culted the methods of engineering into a shock absorption layer. The metrics survived. The dashboards survived. The incident-response choreography survived. What did not survive the export was the specific engineering culture that had made those methods mean something in their original context. In the absence of that substrate, the methods kept doing *something* — organizing behavior, focusing attention, legitimizing infrastructure — but what they stopped doing was actually stabilizing the systems they were nominally designed to stabilize.

## Form preserved, function replaced

The SRE book reads very differently if you come to it expecting a control-theoretic treatment of operational stability. Classical control would ask: what is the plant, what is the controller, what is the loop bandwidth, what is the phase margin, what happens under disturbance, what are the conditions for closed-loop stability. The SRE book mostly does not ask these questions. It asks: what is the error budget, what is the SLI, what is the SLO, what is the toil ratio, how is on-call structured, how is the postmortem conducted.

Those are not the same questions. An error budget is a target, not a stability analysis. You can hit your error budget in a system that is one perturbation away from catastrophic failure, and you can miss your error budget in a system that is fundamentally stable but experiencing benign noise. The quantity being measured is not the quantity that determines whether the system is actually safe.

This matters because the measurement regime generates its own legitimacy. Once an organization commits to error budgets as the central metric, the question "is this system stable?" gets answered indirectly, by asking whether the budget is being hit. The indirect answer is not wrong, exactly. It is just about a different object — a statistical summary of past outputs — than the object the original engineering vocabulary was designed to analyze.

## The shock absorption function

Systems have to be stabilized by *something*. If the methodology cannot improve underlying stability — because it is not actually doing control-theoretic analysis, only measuring outputs — then stabilization has to happen somewhere else. The somewhere else is almost always people.

This is not a metaphor. It is a control-theoretic claim with specific structure. In the closed-loop system *plant + nominal controller*, the nominal controller is whatever the documented methodology says it is: the automation, the runbooks, the scheduled procedures. But the realized closed loop is *plant + nominal controller + H*, where H is a latent human compensator acting on side information that does not appear in the official model.

H is why the system appears stable. Remove H — through retirement, layoff, reorganization, or burnout — and the true poles reveal themselves. Everyone is surprised. The surprise is structural: H was never in the model, so there was never a way for the apparatus to predict what its absence would mean.

Two masking conditions keep H invisible. First, if both the nominal and the compensated actions are clipped by the same authority or rate-limit envelope, the human contribution disappears at the boundary — the person is pushing on a locked door, and the measured output does not distinguish that effort from no effort at all. Second, if H acts on unmeasured or indirectly measured plant state, then it can change future recoverability without moving any current SLI. Quiet heroics are structurally invisible under the measurement map.

The SRE measurement regime is almost perfectly engineered to miss H. SLIs are chosen to be observable and to correlate with user-facing behavior. They are not chosen to reveal the counterfactual — what the system would look like in the absence of its human compensators. So H stays off the dashboard, which means H stays off the roadmap, which means the investment decisions that would relieve the pressure on H do not get made.

## Error budgets as policy

The error budget framing is particularly vulnerable to this critique because it is the clearest example of SRE smuggling governance decisions in under engineering vocabulary. "How much unreliability is acceptable" is a political question. Who bears the cost of outages, whose workload absorbs the recovery, what gets prioritized when reliability and feature velocity trade off, who decides when the budget is exhausted — these are allocation decisions about labor, risk, and attention. They are not technical parameters.

Error budgets dress that allocation up as math. The math is real; the arithmetic is correct; the resulting number has decimal places. But the arithmetic is downstream of a set of choices about what to measure, what to exclude, whose time counts as toil, whose time counts as engineering, and whose judgment is authoritative over the trade-off. Those choices are policy. The math is the form; the policy is the function.

This is what "governance wearing engineering clothes" means. It is not an accusation of bad faith. It is an observation that the practice works by converting allocation questions into measurement questions, and then treating the answers to the measurement questions as if they settled the allocation. They don't. They just move the allocation into a vocabulary where challenging it requires first challenging the measurement — a much higher bar.

## Handoff and the serialization myth

SRE's handoff practices — runbooks, postmortems, onboarding documentation, incident timelines — are the serialization layer for operational knowledge. The discipline's self-image depends on a claim that these artifacts capture enough of the controller state to allow smooth transitions between operators, between teams, across time.

They don't, and every team knows this experientially. Every team has the senior person whose mental model is not documented anywhere, whose retirement would be a months-long stability event. Every team has the runbook that works only for the person who wrote it. Every team has the postmortem whose real lesson never made it into the document because the real lesson was about a subtle pattern of system behavior that the author could not figure out how to communicate in prose.

Handoff under bandwidth constraint is a lossy operation. The outgoing operator serializes what they think is load-bearing. The incoming operator reconstructs from that serialization plus whatever residual context survives. In between, information is lost, and the loss is not uniform: the information most likely to be lost is the information that the outgoing operator did not know was load-bearing, because the perturbations it absorbed never became legible enough to document.

This means that every operational transition is a live experiment in whether the written system and the actual system are the same thing, conducted without consent from the people who are about to find out. The methodology officially denies this, because the official story is that the runbooks work. The methodology unofficially depends on it, because the alternative would require admitting that stability is produced by something the documentation cannot capture.

## On-call as designed shock absorber

The on-call model is where the pattern bites hardest. The entire rotation structure is premised on the idea that a rested operator can absorb perturbations that the system itself cannot. This is empirically true. Operators do absorb those perturbations. The absorption is what keeps the system running across the gap between advertised reliability and real reliability.

But systems get designed *around* that absorption, which means the operator is not a safety net. The operator is a load-bearing component whose failure mode is burnout. The burnout is not a bug in the methodology. It is the methodology working as designed, just not as advertised. The shock absorption has to happen somewhere; the rotation is where it was placed.

Naming this changes what the on-call burnout literature is about. It is not a story about insufficient support or poor rotation hygiene or inadequate mental health resources, though all of those matter at the margin. It is a story about a structural mismatch between what the methodology can actually do (measure, legitimize) and what the systems require (stabilization), where the mismatch is closed by consuming human cognitive capacity at a rate the rotation structure cannot sustain.

## Legitimacy export

The SRE methodology did not arise in a vacuum. It arose at Google, in a specific engineering culture, operated by a specific population of engineers, on a specific class of systems. In that context, the methodology was not cargo-culted; it was genuinely doing engineering, because the people operating it understood the substrate well enough to know what the measurements meant.

The export stripped the context. What traveled was the vocabulary, the practices, and — crucially — Google's legitimacy. "This is how Google does it" is not just a practice recommendation. It is a legitimacy claim, and organizations adopting the methodology borrowed that legitimacy in exchange for taking on the absorption role.

This is why the critique has to be of the exported methodology, not of the people practicing it or of Google's original work. The people practicing it are doing their best with the tools available. Google's original practice made sense in its original context. What happened in the export is a pattern that shows up elsewhere in the legitimacy economy: a practice developed under specific conditions gets abstracted into "best practice," the specific conditions get stripped out, and the resulting methodology functions primarily as legitimacy infrastructure rather than as the thing it was originally.

## What the critique is for

The point of naming this is not to drive a stake through anyone's career. Reliability engineering as a field will outlast this methodology the same way it predated it. The people doing the work are not the target; the work is real, the exhaustion is real, the expertise is real, and none of that is in question.

The point is to make the seam visible. Operational stability has a control-theoretic structure. That structure has specific failure modes — handoff as lossy observer transfer, authority latency versus viability, hidden compensation under projection and observability masking, fatigue as both parameter drift and mode fracture. The methodology that currently dominates the field does not name these failure modes because its vocabulary cannot see them. The absorption role it assigns to humans is precisely the shape of what its vocabulary excludes.

A different vocabulary is available. It is older than the methodology it would replace. It asks what the plant is, what the controller is, what the loop bandwidth is, what the phase margin is, what happens under disturbance. It treats operators as part of the closed loop rather than as consumers of the metrics the loop produces. It treats handoff as an observer-transfer problem rather than as a documentation problem. It treats error budgets as policy rather than as math.

That vocabulary is not new. It was just annexed. Getting it back is the work.
