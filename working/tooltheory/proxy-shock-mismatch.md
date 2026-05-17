# Proxy shock mismatch

**Slogan:** Sensor geometry selects the proxy; shock mismatch accelerates false target inference.

**Operational form:** *A shock on the proxy channel is evidence of changed conditions, not proof of target state.*

**Source:** P25 §4.5 second-channel observation; grok reviewer Q2 + ChatGPT lane-mapping 2026-05-12.

## What it is

P25 §4.5 names two sufficient channels for substitution: (1) observability-Gramian asymmetry (the geometric channel — main contribution) and (2) filter mis-specification with respect to real state statistics on a channel coupled to $y$ (the shock channel — second sufficient condition observed in simulation).

In discourse settings, shock mismatch is an amplifier, not the main channel. Sudden pile-ons, coalition jumps, bot floods, viral context collapse — these arrive in distributions the regulator's filter is not calibrated for. They get misread as target evidence even when the sensor angle is less bad.

## Doctrine

A shock on the proxy channel is evidence of *changed conditions*, not proof of *target state*. The temptation is to interpret a sudden proxy-channel spike as target evidence; the discipline is to treat it as regime-change evidence requiring uncertainty posture — entering watch / defer mode, preserving uncertainty, avoiding premature closure.

## Tool mapping

- **NQ:** shock-detection on proxy channels triggers regime-change witness, not target witness. Don't launder "proxy channel spiked" into "target degraded" without an actual target witness.
- **Nightshift:** workflow shape under proxy-shock — enter watch / defer mode, preserve uncertainty, avoid premature closure, coordinate *"we saw a shock"* without pretending *"we know what it means."*

Examples worth instrumenting:

- sudden alert flood;
- sudden label / post burst;
- sudden user-report spike;
- sudden CPU / memory / disk anomaly;
- sudden social contamination around a claim;
- sudden CI failure cluster after a dependency move.

In each case the proxy-channel shock is real and informative — it just doesn't authorize *target-binding* action.

## Lean candidates

- `proxy_shock_does_not_authorize_target_closure` — relative of consequence-scoping (see [consequence-scoping](consequence-scoping.md))

## Promotion gate

When NQ or Nightshift implementation actually hits this — a sudden-shock event needs to be classified as regime-change vs target-evidence and the current code can't distinguish — then the doctrine gets a concrete pin and may promote to project gap/spec.
