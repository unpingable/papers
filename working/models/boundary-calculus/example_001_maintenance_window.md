# Example 1: Maintenance Window Degradation

Status: toy model / first degradation example
Authority: non-doctrinal
Purpose: demonstrates non-inheritance plus controlled basis degradation
Adds beyond Example 0:
  - basis mutation
  - role degradation
  - post-boundary admissibility for a different effect
Known limitation:
  - models degradation as action-change; later kernel should distinguish basis-role degradation from action derivation (i.e., the cleaner formulation is `B ⊢ κ : authorization(a_maint) ↦ κ' : evidence(a_maint)` plus a separate rule `evidence(a_maint) supports Adm(a_audit)`)

> **“Maintenance‑window authorization degrades into historical evidence.”**

The idea: during a planned maintenance window, a special live token authorises disruptive actions (e.g., reboot, patch). After the window closes, that token becomes *historical evidence* – it no longer permits the original actions, but it does authorise auditing, reporting, or proving that maintenance took place.

---

## 1. States, actions, bases

**States** (Γ) – three temporal phases for a server:

| State      | Meaning                       |
|------------|-------------------------------|
| Γ_pre      | before the maintenance window |
| Γ_open     | window is open (active)       |
| Γ_post     | window has closed             |

**Actions** (a):

| Action       | Description                                |
|--------------|--------------------------------------------|
| a_maint      | perform disruptive maintenance (reboot…)   |
| a_audit      | run an audit, prove maintenance occurred   |

**Bases** (κ) – kinds of justification:

| Basis      | Nature                                      |
|------------|---------------------------------------------|
| κ_live     | a live maintenance token (valid only during window) |
| κ_hist     | historical record derived from κ_live after the window |

---

## 2. Primitive admissibility (axioms)

Admissibility `Γ ⊢_κ Adm(a)` is initially given by exactly two facts:

\[
\begin{aligned}
&\text{(A1)}\quad \Gamma_{\text{open}} \;\vdash_{\kappa_{\text{live}}}\; \mathsf{Adm}(a_{\text{maint}}) \\[4pt]
&\text{(A2)}\quad \Gamma_{\text{post}} \;\vdash_{\kappa_{\text{hist}}}\; \mathsf{Adm}(a_{\text{audit}})
\end{aligned}
\]

No other `(Γ, κ, a)` combination is an axiom. In particular, neither `Γ_pre` nor `Γ_post` recognise `κ_live` as authorising `a_maint`.

A2 records the intended post-state recognition of `κ_hist`; the trace below shows how that basis may also be produced by degradation from `κ_live`. The two routes coincide here by design — A2 fixes what `κ_hist` should authorise in `Γ_post`, and degradation supplies the route by which the post-state basis is actually obtained from the live token.

---

## 3. Boundary transitions

Two transitions move the system through the maintenance lifecycle:

\[
\begin{aligned}
B_{\text{open}} &: \Gamma_{\text{pre}} \to \Gamma_{\text{open}} \quad\text{(window opens)} \\
B_{\text{close}} &: \Gamma_{\text{open}} \to \Gamma_{\text{post}} \quad\text{(window closes)}
\end{aligned}
\]

---

## 4. Transport and degradation

We need two different mechanisms for what happens to a basis when the state changes:

- **Transport** (same‑action persistence): `Transport(B, κ)` returns a new basis `κ'` that can still authorise the **same** action, or `⊥` if the basis does not survive for that action.
- **Degradation** (action change): `Degrade(B, κ, a)` returns a pair `(κ', a')` of a new basis and a **new** action, or `⊥` if no such transformation exists.

For our model they are defined as follows:

**Transport** (never maps `κ_live` to a live basis after the window):

\[
\mathsf{Transport}(B_{\text{close}},\; \kappa_{\text{live}}) = \bot
\qquad
\text{all other Transport}(B,\kappa) = \bot
\]

**Degradation** (maps live maintenance token into historical evidence):

\[
\mathsf{Degrade}(B_{\text{close}},\; \kappa_{\text{live}},\; a_{\text{maint}}) = (\kappa_{\text{hist}},\; a_{\text{audit}})
\qquad
\text{all other cases } \bot
\]

So `Degrade` only fires when we have a live maintenance action at window‑close; it turns the basis into a historical record that now authorises auditing.

---

## 5. Deduction rules

**Preservation rule** (same action, if basis survives):

\[
\frac{
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\qquad
\mathsf{Transport}(B:\Gamma\to\Gamma',\; \kappa) = \kappa' \neq \bot
}{
\Gamma' \vdash_{\kappa'} \mathsf{Adm}(a)
}
\]

**Degradation rule** (basis transforms and authorises a different action):

\[
\frac{
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\qquad
B:\Gamma\to\Gamma'
\qquad
\mathsf{Degrade}(B,\; \kappa,\; a) = (\kappa', a')
}{
\Gamma' \vdash_{\kappa'} \mathsf{Adm}(a')
}
\]

These are the only rules for moving admissibility across boundaries. There is no rule that resurrects a dead basis or changes the action arbitrarily.

---

## 6. A trace through the system

1. **Window opens** – we assume `Γ_pre` provides no admissibility for `a_maint`.  
   The system enters `Γ_open`. Axiom (A1) gives us (perhaps because an admin injects the token):

   \[
   \Gamma_{\text{open}} \;\vdash_{\kappa_{\text{live}}}\; \mathsf{Adm}(a_{\text{maint}})
   \]

   Maintenance can now be performed.

2. **Window closes** – apply transition \(B_{\text{close}} : \Gamma_{\text{open}} \to \Gamma_{\text{post}}\).

   - **Transport check**:  
     `Transport(B_close, κ_live) = ⊥` → preservation rule does **not** fire.  
     We obtain **no** judgement of the form `Γ_post ⊢_κ_live Adm(a_maint)`.

   - **Degradation check**:  
     `Degrade(B_close, κ_live, a_maint) = (κ_hist, a_audit)` is defined.  
     Degradation rule fires, giving:

     \[
     \Gamma_{\text{post}} \;\vdash_{\kappa_{\text{hist}}}\; \mathsf{Adm}(a_{\text{audit}})
     \]

     This matches axiom (A2) – the historical evidence now authorises auditing.

3. **After the window** – we cannot perform `a_maint` under any basis (no rule introduces it).  
   But we can legitimately run `a_audit` using `κ_hist`.  
   The live token has *degraded* into historical evidence.

---

## 7. What this illustrates

- **Non‑inheritance of the original action**: `a_maint` does **not** remain admissible after the window – the old basis simply does not transport.
- **Controlled basis mutation**: a boundary transition can change what a piece of evidence authorises, not merely preserve it. This is captured cleanly by the `Degrade` function.
- **Fresh actions from the past**: the historical record `κ_hist` is a genuine basis for a new action, not a failed leftover.
- The calculus distinguishes **preservation** (same action) from **transformation** (new action), giving a fine‑grained account of how authorisation can evolve across state boundaries.

This model can be extended (e.g., adding multiple windows, chained degradations, or bases that degrade multiple times) but already captures the core idea: a maintenance token lives, dies, and leaves behind an audit trail – all within a uniform judgement form `Γ ⊢_κ Adm(a)`.

---

**Keeper line:**
*The live token dies as authority but survives as evidence.*
