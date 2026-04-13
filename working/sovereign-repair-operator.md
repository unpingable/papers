---
title: Self-Similar Sovereign Repair Operator
author: James Beck
date: 2026-04-13
status: design note (math sketch)
extends: Paper 18 (unauthorized durability), promotion ceremony
---

# Self-Similar Sovereign Repair Operator

Paper 18 defines the promotion ceremony as a composable governance primitive — the typed, attested, auditable transition from lower-tier state to higher-tier authority. This note sketches the inverse operation: controlled repair of state that was promoted without ceremony.

Not a magic legitimacy exorcist. A recursive operator that can act on any governed scope, detect shadow dominance, choose enforcement vs migration, and reconstitute authorized state without pretending the shadow state never existed.

---

## The governed cell

Define a governed cell:

$$
G = (R, S_f, S_s, B, W, C)
$$

Where:

- $R$ = current regime / invariant set
- $S_f$ = formal state
- $S_s$ = shadow state
- $B$ = write barriers / promotion controls
- $W$ = witness / receipt / observability surface
- $C$ = child cells

## Shadow state decomposition

Shadow state decomposes into two disjoint classes:

$$
S_s = S_a \cup S_p
$$

- $S_a$ = **active shadow state** — unauthorized state still exerting live governing force
- $S_p$ = **parked shadow state** — unresolved but contained items (quarantine and defer outcomes)

A deferred item that still quietly governs is not deferred. It is shadow state in a fake mustache. The partition requires a containment predicate:

$$
S_p = \{x \in \hat{S}_s \mid \text{class}(x) \in \{\text{quarantine}, \text{defer}\} \land \text{Contained}(x, W)\}
$$

$$
S_a = \hat{S}_s \setminus S_p
$$

Where $\text{Contained}(x, W)$ requires at minimum:

- Item is no longer exerting live governing force
- Expansion is blocked
- Observability $W$ is sufficient to detect continued force
- Explicit owner assigned
- Review trigger or expiry defined

If the shadow state has captured the measurement apparatus, the operator will misclassify active force as parked. The partition is normative, not merely descriptive — it requires an accurate $W$.

### Aging and escalation

Deferred and quarantined items age:

$$
A(x,t) = t - t_{\text{deferred}}
$$

Items that exceed their review window are automatically escalated:

$$
\mathcal{E}_{\tau}(x) =
\begin{cases}
\text{reclassify}(x) & \text{if } A(x,t) > \tau_{\max} \\
x & \text{otherwise}
\end{cases}
$$

Reclassification rules (policy-defined, not pure math):

- Expired `defer` + suspected live force → `quarantine`
- Expired `defer` + no detected force → forced reconsideration for `repeal` or `ratify`
- Expired `quarantine` + no expansion + no live force → candidate `repeal`
- Expired `quarantine` + continued force → back to $S_a$ (failed containment)

Without escalation, `defer` becomes a constitutional landfill — the backlog becomes the regime.

## Divergence measures

### Active divergence (primary)

$$
D_a(G,t) = \frac{|S_a(t)|}{|S_f(t)| + |S_a(t)|}
$$

This is the thing the repair operator is supposed to drive down. It measures unauthorized state still actively governing.

### Pending inventory burden

$$
P(G,t) = \frac{|S_p(t)|}{|S_f(t)| + |S_a(t)| + |S_p(t)|}
$$

This is not governing shadow force. It is unresolved repair burden — boxed up but not settled.

Where magnitude in both measures is **effective influence on behavior**, not count. One regime-wide policy reversal and one tiny moderation fix do not both count as "1."

### Additional control variables

$$
H(G,t) = \text{hysteresis / reversibility cost}
$$

$$
O(G,t) = \text{observability quality}
$$

- High $H$ means the system has reorganized around shadow state
- Low $O$ means you can see consequences but not the promotion path

Once unauthorized promotions accumulate, the system can settle into a hysteretic basin where "just enforce the rules" breaks the plant.

---

## The repair operator

$$
\mathcal{R}_{\sigma}(G)
$$

Where $\sigma$ is the sovereign repair mandate: authority to suspend, ratify, quarantine, supersede, and rebuild barriers inside scope $G$.

### Phase 1: Freeze new unauthorized promotion

Before repair, stop digging.

$$
B' = \text{tighten}(B)
$$

- Freeze silent promotions
- Require explicit receipts for new L1→L2 / L2→L3 transitions
- Allow only emergency exceptions with scar tissue

Close the write barrier leak before auditing the flood.

### Phase 2: Surface shadow state

Build a candidate set:

$$
\hat{S}_s = \text{infer\_shadow}(G, W)
$$

Sources: unreceipted durable consequences, gap-flagged objects, policy deltas with no attestation path, observed actions with no proposal/evaluation/audit trail.

### Phase 3: Classify shadow state

For each $x \in \hat{S}_s$, classify:

$$
\text{class}(x) \in \{\text{ratify},\ \text{reissue},\ \text{quarantine},\ \text{repeal},\ \text{defer}\}
$$

- **ratify**: shadow state was de facto right; promote it formally. Moves item from $S_a$ to $S_f$. Implies a legitimacy source not reducible to current formal state.
- **reissue**: same outcome, but replay through valid ceremony. Moves item from $S_a$ to $S_f$. Formal state was right in principle; path was broken.
- **quarantine**: keep effect visible but non-expanding. Moves item from $S_a$ to $S_p$ only if containment is real.
- **repeal**: remove force. Removes item from $S_a$ entirely.
- **defer**: insufficient standing/evidence; isolate and revisit. Moves item from $S_a$ to $S_p$ only if genuinely frozen pending judgment, not still shaping outcomes.

The ratify/reissue distinction is the sovereign hinge. If `ratify` collapses into `reissue`, the operator is just a cleanup crew for L3's blind spots, not a sovereign repair mechanism. Ratify means the operator can look at the shadow and say "this is now law; it was always right."

### Phase 4: Choose regime

$$
M(G) =
\begin{cases}
\text{enforcement} & \text{if } D_a \le \epsilon \text{ and } H \le \eta \\
\text{migration} & \text{if } D_a > \epsilon \text{ or } H > \eta
\end{cases}
$$

- **enforcement** = remove violating state directly
- **migration** = construct formal successor alongside shadow, then cut over gradually

Isolated violations get enforcement. Stabilized shadow basins need migration.

### Phase 5: Reconstitute formal state

$$
S_f^{*} = \text{rebuild}(S_f, \hat{S}_s, M, R, \sigma)
$$

Rules:

- Shadow state is not silently erased
- Every promotion, quarantine, repeal, or supersession emits a repair receipt
- Historical shadow artifacts remain legible as historical facts
- New state gains force only through explicit repair acts

Once shadow governance is load-bearing, you cannot pretend it didn't happen. Formalize from here forward rather than rewrite history.

### Phase 6: Recurse into child cells

For each child $c \in C$:

$$
\mathcal{R}_{\sigma_c}(c)
$$

Same operator. Same diagnostic. Same mode choice. Then aggregate upward:

$$
D_{\text{parent}} = \Phi(D(c_1), D(c_2), \dots, D(c_n), D(G))
$$

Weighted by scope criticality / influence / blast radius, not democratic vibes.

### Compact form

$$
\mathcal{R}_{\sigma}(G) =
\text{freeze} \rightarrow
\text{surface} \rightarrow
\text{classify} \rightarrow
\text{choose mode} \rightarrow
\text{reconstitute} \rightarrow
\text{recurse} \rightarrow
\text{recompute } D
$$

Closure predicates are two-tier (not "terminal conditions" — closure is a maintenance condition, not an achievement):

**Pass completion**: $D_a(G,t) < \epsilon$ and all unresolved items are in controlled state (quarantine or defer) with explicit owner, review condition, expiry trigger, and non-expansion guarantee.

**Regime closure**: additionally $P(G,t) < \kappa$, with no expired deferred items and no quarantined items still exerting live force. Without this second condition, `defer` becomes a constitutional landfill.

**Critical property (machine-checked):** Closure is not monotone under escalation. A governed cell can satisfy pass completion at time $t$ and lose it when expired parked items are reclassified into active shadow state. This means the repair operator is not a one-shot closure function — it is a maintained control regime. "We fixed it" is a claim about a moment, not a state. The operator needs a heartbeat, not just a trigger.

---

## Repair telemetry (sibling metrics, not L4)

The repair operator's behavior should be legible without pretending that legibility solves the legitimacy problem.

### Repair outcome vector

For a governed cell $G$ over window $[t_0, t_1]$:

$$
W_k(G,[t_0,t_1]) = \sum_{x \in X_k} I(x)
$$

Where $k \in \{\text{ratify}, \text{reissue}, \text{quarantine}, \text{repeal}, \text{defer}\}$ and $I(x)$ is the effective influence weight of item $x$. Same influence notion as $D(t)$.

Normalized:

$$
\rho_k(G,[t_0,t_1]) = \frac{W_k}{\sum_j W_j}
$$

Repair profile vector:

$$
P_{\mathcal{R}}(G,[t_0,t_1]) = (\rho_{\text{ratify}}, \rho_{\text{reissue}}, \rho_{\text{quarantine}}, \rho_{\text{repeal}}, \rho_{\text{defer}})
$$

### Interpretation

- **High reissue**: process debt, legitimacy mostly intact, bureaucracy failed but constitution maybe didn't
- **High ratify**: formal regime lagging reality, constitutional blind spots, operator drawing on extra-formal legitimacy
- **High quarantine + defer**: epistemic or standing deficit, operator buying time or unable to classify
- **High repeal**: restoration pressure, active conflict with entrenched shadow state, breakage risk rises with hysteresis

### Derived indices

- **Formal Lag Index**: $L = \rho_{\text{ratify}}$ — how far behind reality is formal governance
- **Process Debt Index**: $E = \rho_{\text{reissue}}$ — how often content is fine but path is broken
- **Restoration Pressure Index**: $C = \rho_{\text{repeal}}$ — how much time spent fighting durable shadow state
- **Epistemic Deficit Index**: $Q = \rho_{\text{quarantine}} + \rho_{\text{defer}}$ — how often the operator can't cleanly classify

### Repair effectiveness (separate from style)

Performance asks whether repair is actually reducing shadow governance without wrecking the plant.

Pass effectiveness:

$$
\Gamma_{\text{pass}}(G,[t_0,t_1]) = \alpha \Delta D_a + \beta \Delta H + \gamma \Delta O
$$

Where $\Delta D_a = D_a(t_0) - D_a(t_1)$, $\Delta H = H(t_0) - H(t_1)$, $\Delta O = O(t_1) - O(t_0)$.

Backlog penalty:

$$
\Lambda(G,t) = \mu P(G,t) + \nu A(G,t)
$$

Where $P$ is pending inventory burden and $A$ is an aging factor on deferred items (unresolved items that exceed their review trigger accumulate penalty).

Net repair health:

$$
\Gamma_{\text{net}} = \Gamma_{\text{pass}} - \Lambda
$$

This ensures wise deferral does not tank pass effectiveness, but permanent limbo still shows up as pathology. Defer is acceptable as a temporary containment outcome, not as a terminal ontology.

### Recursive telemetry

Each child cell gets its own $D$, $P_{\mathcal{R}}$, $\Gamma$. Parent aggregates by influence weight. Same measurement logic at every scope.

---

## What this does not solve

- Who grants $\sigma$
- How competing sovereign repair claims are arbitrated
- What happens when L3 itself is captured
- Whether frequent `ratify` indicates wisdom or a polite coup
- The influence weight $I(x)$ — "effective influence on behavior" is easy to write and hard to operationalize

The repair receipt chain gives second-order observability of repair behavior. That is not L4. It is the beginning of one, with fewer lies in it.

---

## Formal verification results (2026-04-13)

Hostile kernel check via Lean 4 (`~/git/lean/LeanProofs/RepairOperator.lean`). Goal: force separation of structural invariants from political placeholders and measurement handwaving. Not a full formalization — $I(x)$, $\sigma$, $O(G,t)$, and $\Phi$ are deliberately left abstract.

### Partition soundness (4 theorems)

- `active_parked_disjoint`: $S_a \cap S_p = \emptyset$ — an item cannot be simultaneously active and parked
- `parked_resolved_disjoint`: parked and resolved are disjoint
- `active_resolved_disjoint`: active and resolved are disjoint
- `trichotomy`: every shadow item is in exactly one of {active, parked, resolved}

### Classification effects (4 theorems)

- `classify_resolves`: ratify/reissue/repeal produces a resolved item
- `classify_resolves_not_active`: resolving classification removes item from $S_a$
- `classify_parks_contained`: park outcome + real containment → item enters $S_p$
- `classify_parks_uncontained`: park outcome + fake containment → item stays in $S_a$. **Fake containment does not magically park anything.**

### Escalation (2 theorems)

- `escalate_no_outcome_becomes_active`: expired parked item with no reclassification returns to $S_a$
- `escalate_to_resolve`: escalation to a resolving outcome resolves the item

### Terminal conditions (2 theorems)

- `regime_implies_pass`: regime closure implies pass completion
- `empty_is_closed`: empty shadow inventory trivially satisfies regime closure

### The structural finding (1 theorem)

- `escalation_can_break_pass_completion`: **pass completion is not monotone under escalation.** A cell that achieved $D_a < \epsilon$ can lose it when expired deferred items are reclassified back to active shadow. Constructed witness: a cell with one parked `defer` item (age 5, $\tau_{\max}$ = 3) satisfies pass completion; after escalation with no new outcome, containment is revoked and the item returns to $S_a$.

This is the theorem that earns its keep. It proves that repair is a maintained regime, not an achieved state. The escalation clock is always running.

### What the kernel did NOT check

- Influence weight $I(x)$ — left as abstract `Nat` field, not grounded
- Sovereign mandate $\sigma$ — not represented at all
- Observability $O(G,t)$ — not represented
- Parent aggregation $\Phi$ — not represented
- Real-world convergence — the operator converges in the toy transition system; whether it converges in practice is not a Lean question

---

## Connections

- **Paper 18**: promotion ceremony is the forward primitive; this is the inverse operation (controlled demotion/reclassification of state promoted without ceremony)
- **Governor**: operating envelopes and regime detection map to the enforcement/migration mode choice
- **Admissibility family**: the seven invariants are what $R$ contains; each system detects specific shadow-state patterns the repair operator would classify
- **Lean persistence model**: three-way recovery distinction (internally recoverable / externally repairable / locked in) maps to enforcement / migration / the hysteresis threshold

---

## Minimal repair receipt schema

```json
{
  "repair_id": "...",
  "cell_id": "...",
  "shadow_item_id": "...",
  "outcome": "ratify|reissue|quarantine|repeal|defer",
  "influence_weight": 0.73,
  "reason_basis": ["process_break", "standing_gap", "constitutional_blind_spot"],
  "mode": "enforcement|migration",
  "pre_state": { "D": 0.61, "H": 0.74, "O": 0.32 },
  "post_state": { "D": 0.52, "H": 0.71, "O": 0.48 },
  "issued_at": "2026-04-13T21:30:00Z",
  "issuer": "...",
  "signature": "..."
}
```

Load-bearing fields: `outcome`, `influence_weight`, `mode`, enough state deltas to compute profile/effectiveness later. Concrete identity and signing schemes are implementation decisions for whatever system instantiates this.
