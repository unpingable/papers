# Dashboard quiet is not recovered reliability

**Slogan:** Dashboard quiet is not recovered reliability unless the dashboard has standing for the harmed surface.

**Source:** P25 §7 SRE / operations sibling paragraph; ChatGPT lane-mapping 2026-05-12.

## What it is

SRE / Ops bridge of the P25 substitution mechanism. The nominal target is customer-visible reliability or substrate health; the observable surface is SLIs, alert volume, ticket rate, saturation graphs, incident counts. SLIs are indispensable but they are not the target itself. A team can suppress alerts, improve dashboard shape, or reduce ticket inflow while leaving the underlying customer harm or substrate fragility unchanged.

The pathology is not that SLIs are bad. It is that, under partial observability, the controller can begin regulating the dashboard-visible surface while continuing to describe the action as reliability work.

## Doctrine

Closure on an incident requires consequence-channel confirmation, not just proxy quiet. *"Watch until customer-impact witness recovers"* is structurally different from *"alerts cleared."* The admissibility discipline: proxy evidence may authorize investigation or advisory caution, but it should not be allowed to spend authority as proof of recovered reliability.

## Tool mapping

- **NQ:** SLIs testify to *their coverage*, not to "reliability" as a whole. Dashboards are witnesses with explicit coverage boundaries.
    - Alert volume is not substrate health.
    - Ticket count is not customer harm.
    - Absence of alert is not absence of damage.
- **Nightshift:** incident closure should not be authorized solely by dashboard normalization if the original customer-impact channel remains unverified. *"Until customer-impact witness recovers"* is a real workflow state, separate from *"alerts cleared."*

## Lean candidates

- `dashboard_quiet_not_recovered_reliability` — domain-flavored; may refactor into a more abstract `proxy_quiet_does_not_authorize_target_closure` (the math should sniff the decorative version and prefer the abstract one)

## Promotion gate

When Nightshift implements incident-closure logic and needs to distinguish proxy-quiet from substrate-recovered. The distinction currently lives as runbook discipline; the question is whether it becomes a closure-authorization predicate.

Related siblings in this directory: [consequence-scoping](consequence-scoping.md) (general form), [proxy-shock-mismatch](proxy-shock-mismatch.md) (shock-side companion).
