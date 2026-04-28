# Stale Binding

**Status:** candidate
**Originated:** 2026-04-28 (DeepSeek "cache invalidation as a Δt primitive" sketch + chatty correction; this session's exchange in `papers/` repo)
**Primary home:** P26 (premature/belated duality) — headline exhibit / worked primitive

## Formal object

A **cache** is a triple $(S, \delta, \iota)$:

- $S_t \in \mathcal{X}$ — cached source-of-truth value at time $t$.
- $\delta \ge 0$ — invalidation lag (constant, bounded, or stochastic).
- $\iota$ — invalidation policy (write-through, write-back, TTL, poll, control-plane-triggered).

A **truth process** $T_t \in \mathcal{X}$ evolves under external dynamics. The cache satisfies $S_t = T_{t - \delta_t}$, where $\delta_t$ is effective staleness at $t$. Optionally, $S_t$ stores a lossy projection of $T_t$ (analogous to P25's $\alpha$).

A **decision** $d$ at time $t_d$ is **bound** to $S_{t_d}$ if it is authorized against the cached value; the binding has a **consequence window** $[t_d, t_c]$ during which the decision's effect is committed to.

## Failure predicate

Stale binding occurs when:

$$d \text{ is bound to } S_{t_d}, \quad T_{t_d} \neq S_{t_d}, \quad \text{and no revalidation occurs before } t_c.$$

Equivalently: the invalidation horizon exceeds the consequence window. The decision lands in the **empty window** between truth-already-moved and cache-not-yet-refreshed.

## Stale Binding Theorem (corrected)

Given a truth process $T_t$ with characteristic update timescale $\tau$ and a cached process $S_t = T_{t-\delta}$:

If $\delta$ exceeds the coherence horizon of $T$ relative to a decision function $u$, there exists $\varepsilon > 0$ such that

$$P(C(u(S_t), T_t) = \text{false}) \ge \varepsilon$$

where $C$ is a correctness predicate. Furthermore, if observation $h$ is computed only from $S_t$, the divergence is **not observable through $h$**.

**The system can be wrong in a way its own measurement plane cannot see.**

For a binary-flip source $T_t \in \{0,1\}$ with flip probability $p$ per step:

$$P(S_t \neq T_t) = \frac{1 - (1 - 2p)^\delta}{2} \xrightarrow{\delta \to \infty} \frac{1}{2}.$$

The cache loses testimonial advantage over guessing.

**Note:** DeepSeek's original sketch claimed $\Delta_t$ becomes "unbounded with high probability." This overclaims for finite state spaces (enums, auth states, K8s objects, bounded metrics): $\Delta_t$ becomes *maximally untrustworthy*, not unbounded. The base-rate-decay form is the correct claim.

## Typical symptoms

- Caches that look fresh because they are self-consistent: the controller acts on $S_t$, observes $h(S_t)$, and the model and the observation agree by construction.
- Aggregate priors computed over stale witness reads (P24): the freeze is maintained by stale arithmetic; the aggregator cannot distinguish stale-but-balanced from fresh-but-converged.
- Operator handoffs that reinitialize internal state $\hat{x}$ from briefings/shift notes (P23): the new operator acts on stale state until reorientation; identity continuity fails.
- Proxy regulators (P25): the proxy *is* the cache; staleness of $V'$ relative to $V$ drives substitution.
- Reconciliation controllers that evict cache entries (logs, indices, pod state) without writing through to a durable receipt (P27): the testimony of the prior state is masked.

## Used by

- **P26** (empty-window): primary home. Stale binding is the operational form of the temporal-seam failure. The architectural rule (below) is P26's empty-window theorem applied with the cache as one party.
- **P25** (substitution): the cache as proxy; staleness is the mechanism by which $V'$ drifts from $V$.
- **P27** (transition admissibility): stale evidence/causality across reconciliation; receipt horizons must outlive the things they explain or stale binding follows.
- **P24** (aggregation-layer masking): stale witness reads pass through first-moment aggregators undetected; the freeze is maintained by stale arithmetic.
- **P23** (non-self-identical controller): handoff state reinitialization from a stale cache (briefing, hat-x estimate) is the controller's identity-continuity instance of stale binding.

## Do not confuse with

- **Cache invalidation** — that is the *mechanism*; stale binding is the *failure mode*. Cache invalidation can be perfectly correct and stale binding still occurs (if invalidation lag exceeds consequence window).
- **Goodhart-style proxy gaming** — stale binding does not require any agent to be gaming the proxy. The failure is structural, not adversarial. (Though stale binding is a substrate gaming exploits.)
- **Race conditions** — locality phenomenon (concurrent access to mutable state). Stale binding is a horizon phenomenon (decision committed before revalidation). They can co-occur but are different objects.
- **Stale controller identity (P23)** — symptom-shaped sibling. P23's failure is the *controller* being non-self-identical. Stale binding is a more general statement about decisions bound to cached state, of which P23's hat-x reinitialization is one instance.
- **Versioned semantics** (candidate primitive) — *truth didn't move; the interpreter moved.* Stale binding is "truth moved, decision didn't notice"; versioned semantics is "decision didn't change, but its meaning did." Different animal.
- **External irreversibility** (candidate primitive) — different axis. External irreversibility is about consequence escaping the rollback boundary; stale binding is about commitment to a value that has already moved.

## Architectural rules

> **Never authorize irreversible consequence from a cache whose invalidation horizon exceeds the consequence window.**

Sharper than DeepSeek's "never govern from a cache you cannot invalidate," because the right discipline is not about invalidatability — it is about the *relative horizons*. A cache you can invalidate in 5 minutes is fine for a 10-minute consequence window and lethal for a 30-second one.

Operational design implications (each is a small theorem-shaped claim, not formalized here):

- **Write-through with receipt lineage** — pair every cache update with a durable receipt that outlives the cache entry. Ties to P27.
- **Active probing** — periodic forced revalidation against $T_t$, with the probe rate bounded below by the consequence-window structure.
- **Dual-cache with source-of-truth comparison** — when feasible, hold two caches with independent invalidation paths; divergence is observable.
- **Refuse to bind across the horizon** — if consequence-window length is unknown or exceeds invalidation horizon, refuse the decision rather than bind to stale state. The Governor primitive: permit action, deny closure, leave finding open.

## Keeper aphorisms

> *A cache is borrowed authority with a clock problem.*

> *A cache is not dangerous because it is stale. It is dangerous when authority remains bound to it after truth has moved.*

> *The system can be wrong in a way its own measurement plane cannot see.*

## Open questions

- **Adversarial staleness injection.** Can an adversary widen $\delta$ deliberately (network partition attack, slow-write attack, garbage-collection pressure) to force stale-binding regimes? Power-move analysis ties to P26's "power buys time twice."
- **Partial invalidation in distributed caches.** Where invalidation is per-key or per-region rather than global, what is the failure topology? Probably a graph-shaped extension of the basic theorem.
- **Composability with versioned semantics.** When the interpreter changes during the invalidation lag, is the resulting failure mode stale binding, versioned semantics, or a new composite?

## Cross-references

- DeepSeek seed: original "Cache Invalidation as a Δt Primitive" sketch (2026-04-28 thread).
- chattY correction: bounded base-rate decay (not unbounded $\Delta_t$); rename from "cache invalidation" (mechanism) to "Stale Binding" (failure mode); placement as P26 headline exhibit, not P28.
- Folk antecedent: "There are only two hard things in computer science: cache invalidation and naming things." This note formalizes the first while incidentally honoring the second.
