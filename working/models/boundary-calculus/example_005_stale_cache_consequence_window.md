# Example 5: Stale Cache and Consequence Window

Status: toy model / temporal-decay example
Authority: non-doctrinal
Purpose: demonstrates time passage as a boundary transition where a basis preserves, degrades or expires
Adds beyond previous examples:
  - viability interval / TTL
  - consequence window / grace horizon
  - basis decay over time
  - empty-binding window before basis creation
Known limitation:
  - single cache entry only
  - `fetch` introduction is abstract (no rule produces a fresh basis from a successful fetch)
  - no concurrent cache entries
  - grace policy is fixed rather than consequence-sensitive

A cached authorisation decision has a **viability interval** (its TTL). Within that interval the cached basis authorises immediate use. After the TTL, the basis **degrades** into a stale form that still permits a (consequential) action — a stale use with a logged warning — but only within a **grace horizon**. Beyond the horizon the basis dies completely. Before the cache is populated there is an **empty-binding window** where no basis for `use` exists, and only a `fetch` can create one.

> **Containment note.** This example uses time passage as a boundary transition. It does **not** define a separate temporal calculus. The mechanism under test is basis decay under boundary transition, instantiated within the existing boundary-calculus rule set (preservation + degradation). Any "temporal calculus" framing stays in the forbidden cabinet.

---

## 1. States, actions, bases

**States** \(\Gamma(t)\) — the system at time \(t \in \mathbb{R}_{\ge 0}\). Time is the only state component.

**Actions**

| Action      | Meaning when admissible                                                |
|-------------|------------------------------------------------------------------------|
| `use`       | use cached decision directly (within TTL; optimal-consequence path)    |
| `use_warn`  | use cached decision after TTL with a logged stale-use warning           |
| `fetch`     | fetch a fresh decision from upstream and populate the cache             |
| `evict`     | manually remove a cache entry                                           |

**Bases**

| Basis                              | Kind                                                          |
|------------------------------------|---------------------------------------------------------------|
| \(\kappa_{\text{fresh}}(d, t_0, \tau)\) | fresh cache entry for decision `d`, cached at `t₀`, TTL `τ`  |
| \(\kappa_{\text{stale}}(d, t_0)\)       | stale (degraded) entry for `d`, originally cached at `t₀`     |
| \(\kappa_{\text{req}}\)                  | a token permitting a `fetch` request                          |

---

## 2. Primitive admissibility (axioms)

These axioms hold at \(\Gamma(t)\) only when their time guards are satisfied.

\[
\begin{aligned}
\text{(Fresh-Use)}&\quad
\Gamma(t) \;\vdash_{\kappa_{\text{fresh}}(d, t_0, \tau)}\; \mathsf{Adm}(\text{use})
\quad\text{only when } t_0 \le t \le t_0 + \tau \\[4pt]
\text{(Stale-Warn)}&\quad
\Gamma(t) \;\vdash_{\kappa_{\text{stale}}(d, t_0)}\; \mathsf{Adm}(\text{use\_warn})
\quad\text{only when } t_0 + \tau < t \le t_0 + \tau + G \\[4pt]
\text{(Fetch)}&\quad
\Gamma(t) \;\vdash_{\kappa_{\text{req}}}\; \mathsf{Adm}(\text{fetch})
\quad\text{when no }\kappa_{\text{fresh}}(d, \ldots)\text{ or }\kappa_{\text{stale}}(d, \ldots)\text{ holds in }\Gamma(t)
\end{aligned}
\]

The Fetch axiom is **conditional**: it is present only when no fresh or stale basis for the same decision `d` currently holds. This models the **empty-binding window**.

The time guards on Fresh-Use and Stale-Warn prevent local axioms from resurrecting expired authority — without them, treating the basis as "present" outside its window would silently re-license the action.

---

## 3. Boundary transitions (time passage)

For any \(\Delta t > 0\):

\[
B_{\Delta t} : \Gamma(t) \;\to\; \Gamma(t + \Delta t)
\]

This transition advances the system in time. It does **not** remove any basis directly; transport and degradation handle that.

---

## 4. Transport and degradation across time

Let the **grace period** be a fixed constant \(G \ge 0\) (the horizon beyond TTL). Define the **total horizon** \(H = \tau + G\) from the caching moment.

**Fresh basis transport** — preserves only same-action authority:

\[
\mathsf{Transport}\bigl(B_{\Delta t},\; \kappa_{\text{fresh}}(d, t_0, \tau)\bigr) =
\begin{cases}
\kappa_{\text{fresh}}(d, t_0, \tau) & \text{if } t + \Delta t \le t_0 + \tau \\[4pt]
\bot                                  & \text{otherwise}
\end{cases}
\]

Transport never returns a stale basis — fresh-to-stale is an action change, not preservation, and so belongs to `Degrade` (below). This prevents the rake where `Γ(t) ⊢_κ_fresh Adm(use)` plus a transport that returns `κ_stale` would let the preservation rule derive `Γ(t+Δt) ⊢_κ_stale Adm(use)` — exactly the haunted "stale evidence authorizes fresh use" the model is meant to forbid.

**Stale basis transport**:

\[
\mathsf{Transport}\bigl(B_{\Delta t},\; \kappa_{\text{stale}}(d, t_0)\bigr) =
\begin{cases}
\kappa_{\text{stale}}(d, t_0) & \text{if } t + \Delta t \le t_0 + \tau + G \\
\bot                            & \text{otherwise}
\end{cases}
\]

**Fresh-to-stale degradation** — basis kind and action both change:

\[
\mathsf{Degrade}\bigl(B_{\Delta t},\; \kappa_{\text{fresh}}(d, t_0, \tau),\; \text{use}\bigr) =
\begin{cases}
\bigl(\kappa_{\text{stale}}(d, t_0),\; \text{use\_warn}\bigr) & \text{if } t_0 + \tau < t + \Delta t \le t_0 + \tau + G \\
\bot                                                            & \text{otherwise}
\end{cases}
\]

No other transport or degradation is defined. The `κ_req` basis for `fetch` does not transport — it is regenerated in each state whenever the empty-binding window is active.

---

## 5. Deduction rules

**Preservation rule** (same action, basis survives):

\[
\frac{
\Gamma(t) \vdash_{\kappa} \mathsf{Adm}(a)
\qquad
B_{\Delta t}: \Gamma(t) \to \Gamma(t + \Delta t)
\qquad
\mathsf{Transport}(B_{\Delta t}, \kappa) = \kappa' \neq \bot
}{
\Gamma(t + \Delta t) \vdash_{\kappa'} \mathsf{Adm}(a)
}
\]

**Degradation rule** (action changes with basis):

\[
\frac{
\Gamma(t) \vdash_{\kappa} \mathsf{Adm}(a)
\qquad
B_{\Delta t}: \Gamma(t) \to \Gamma(t + \Delta t)
\qquad
\mathsf{Degrade}(B_{\Delta t}, \kappa, a) = (\kappa', a')
}{
\Gamma(t + \Delta t) \vdash_{\kappa'} \mathsf{Adm}(a')
}
\]

Preservation handles fresh→fresh (within TTL) and stale→stale (within horizon). Degradation handles the fresh→stale action change at TTL expiry. Beyond the horizon, both rules fail to fire because transport and degradation both return ⊥.

---

## 6. Trace example

Let \(\tau = 10\) (TTL), \(G = 5\) (grace), so \(H = 15\). Cache populated at \(t_0 = 2\) with decision `d`. Initial state \(\Gamma(2)\).

**At \(t = 2\)** — cache just created. Fresh-Use axiom holds (\(2 \le 2 \le 12\)):
\[
\Gamma(2) \vdash_{\kappa_{\text{fresh}}(d,2,10)} \mathsf{Adm}(\text{use}).
\]

**Advance \(\Delta t = 5\) to \(t = 7\)** — inside TTL (\(7 \le 12\)):
\(\mathsf{Transport}(B_5, \kappa_{\text{fresh}}) = \kappa_{\text{fresh}}\). Preservation gives:
\[
\Gamma(7) \vdash_{\kappa_{\text{fresh}}(d,2,10)} \mathsf{Adm}(\text{use}).
\]

**Advance \(\Delta t = 6\) from \(t = 7\) to \(t = 13\)** — past TTL (\(13 > 12\)) but inside horizon (\(13 \le 17\)):
\(\mathsf{Transport}(B_6, \kappa_{\text{fresh}}) = \bot\) because \(13 > 12\), so preservation does **not** fire on `use`.
\(\mathsf{Degrade}(B_6, \kappa_{\text{fresh}}, \text{use}) = (\kappa_{\text{stale}}(d,2),\; \text{use\_warn})\). Degradation gives:
\[
\Gamma(13) \vdash_{\kappa_{\text{stale}}(d,2)} \mathsf{Adm}(\text{use\_warn}).
\]

**Advance \(\Delta t = 2\) from \(t = 13\) to \(t = 15\)** — still inside horizon (\(15 \le 17\)):
\(\mathsf{Transport}(B_2, \kappa_{\text{stale}}) = \kappa_{\text{stale}}\). Preservation gives:
\[
\Gamma(15) \vdash_{\kappa_{\text{stale}}(d,2)} \mathsf{Adm}(\text{use\_warn}).
\]

**Advance \(\Delta t = 3\) from \(t = 15\) to \(t = 18\)** — beyond horizon (\(18 > 17\)):
\(\mathsf{Transport}(B_3, \kappa_{\text{stale}}) = \bot\), and no degradation rule applies to a stale basis. The basis is lost. Neither `use` nor `use_warn` is derivable at \(t = 18\) from this basis.

**Empty-binding window** — before \(t = 2\), no fresh or stale basis for `d` exists. Therefore \(\kappa_{\text{req}}\) is available, and via the Fetch axiom:
\[
\Gamma(t) \vdash_{\kappa_{\text{req}}} \mathsf{Adm}(\text{fetch})
\quad \text{for } t < 2.
\]
The `use` action is not derivable in this window.

---

## 7. What this illustrates

- **Viability interval** \([t_0,\; t_0 + \tau]\): `use` is fully authorised on the fresh basis.
- **Consequence window** \((t_0 + \tau,\; t_0 + \tau + G]\): the basis degrades to stale; only `use_warn` is authorised — a "use with consequences", not the original action.
- **Beyond horizon** \((t_0 + \tau + G,\; \infty)\): no basis survives; authorisation is lost from this lineage.
- **Empty-binding window** \((-\infty,\; t_0)\): the cache is missing; only `fetch` is available to populate it.
- **Time passage as boundary transition**: a basis can preserve, degrade, or die under \(B_{\Delta t}\), with corresponding changes in admissible actions. Transport carries same-action authority; degradation carries action change. The two are kept structurally distinct so that "stale basis authorizes fresh use" is underivable by construction.

---

**Keeper line:**
*A cache's authority is a lease that turns into a warning before it vanishes.*
