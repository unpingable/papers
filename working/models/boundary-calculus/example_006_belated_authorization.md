# Example 6: Belated Authorization

Status: toy model / temporal non-overlap example
Authority: non-doctrinal
Purpose: demonstrates that valid authorization cannot bind a consequence whose viability window has closed
Adds beyond previous examples:
  - consequence viability interval, separate from basis validity
  - non-overlap between basis validity and action viability
  - post-deadline degradation of execution authority into historical evidence
  - distinction between procedural validity and operational binding
Known limitation:
  - authorization grant is external (not modeled inside the boundary-calculus rules)
  - only one deadline / one action is modeled
  - document persistence is separated from authority persistence only informally

The authorization is real, procedurally correct, and documented. It simply remains valid — or arrives — too late. This is not basis expiry (Example 5's TTL decay); it is **non-overlap** between the interval when authorization is procedurally valid and the interval when the action's consequence can still be realised. The result is a basis that authorizes only an archival record — evidence of an institutional timing failure — but never the action itself.

> **Containment note.** Like Example 5, this example uses time passage as a boundary transition. It does **not** define a separate temporal calculus. The mechanism under test is non-overlap between basis validity and consequence viability, instantiated within the existing boundary-calculus rule set (preservation + degradation). See `notes/temporal-boundary-patterns.md`.

---

## 1. States, actions, bases

States \(\Gamma(t)\) at time \(t \in \mathbb{R}_{\ge 0}\). Time is the only state component. The model fixes a deadline \(t_a\) — the **consequence-viability boundary**.

| State (informal label)  | Time range | Meaning                                                       |
|-------------------------|------------|---------------------------------------------------------------|
| \(\Gamma_{\text{before}}\) | \(t < t_a\) | action opportunity open                                       |
| \(\Gamma_{\text{action}}\) | \(t = t_a\) | last viable moment for the action's consequence               |
| \(\Gamma_{\text{after}}\)  | \(t > t_a\) | opportunity closed; only archival outcomes are possible       |

The **consequence viability interval** is \((-\infty, t_a]\) — the action must occur at or before \(t_a\) to have its intended effect.

**Actions**

| Action               | Meaning when admissible                                    |
|----------------------|------------------------------------------------------------|
| \(a_{\text{execute}}\) | perform the action while consequence is still viable       |
| \(a_{\text{record}}\)  | record approval as a historical fact / audit entry         |

**Bases**

| Basis                       | Kind                                                          |
|-----------------------------|---------------------------------------------------------------|
| \(\kappa_{\text{pending}}\) | request submitted, no decision yet                            |
| \(\kappa_{\text{auth}}\)    | full authorization to execute (granted at some time \(t_g\))  |
| \(\kappa_{\text{hist}}\)    | belated or spent authorization record (audit only)            |

---

## 2. Primitive admissibility (axioms)

\[
\begin{aligned}
\text{(Pending)}\quad
&\Gamma(t) \;\vdash_{\kappa_{\text{pending}}}\; \mathsf{Adm}(a_{\text{record}})
\quad\text{always; the request itself is a recordable fact, but it never authorizes execution.} \\[4pt]
\text{(Auth-Execute)}\quad
&\Gamma(t) \;\vdash_{\kappa_{\text{auth}}}\; \mathsf{Adm}(a_{\text{execute}})
\quad\text{only when } t \le t_a. \\[4pt]
\text{(Hist-Record)}\quad
&\Gamma(t) \;\vdash_{\kappa_{\text{hist}}}\; \mathsf{Adm}(a_{\text{record}})
\quad\text{always; historical evidence supports audit but never execution.}
\end{aligned}
\]

The Auth-Execute side-condition is load-bearing. After \(t_a\), the token \(\kappa_{\text{auth}}\) may persist but the axiom no longer applies, so \(\mathsf{Adm}(a_{\text{execute}})\) is not derivable from it. Without the side-condition, "I still hold the authorization" would silently re-license execution past the deadline.

---

## 3. Boundary transitions

For any \(\Delta t > 0\):
\[
B_{\Delta t} : \Gamma(t) \;\to\; \Gamma(t + \Delta t)
\]

Two named cases — both special instances of \(B_{\Delta t}\) — make the deadline-crossing structure visible:

\[
\begin{aligned}
B_{\text{deadline}} &: \Gamma(t) \to \Gamma(t_a) \quad\text{for } t < t_a \\
B_{\text{belated}}  &: \Gamma(t_a) \to \Gamma(t') \quad\text{for } t' > t_a
\end{aligned}
\]

---

## 4. Transport and degradation

Bare-basis-survives-therefore-action-survives is exactly the rake to be kept closed: the token may persist while its execution-authorizing meaning does not.

**Auth basis transport** — preserves execution authority only inside the consequence window:

\[
\mathsf{Transport}\bigl(B_{\Delta t}: \Gamma(t) \to \Gamma(t + \Delta t),\; \kappa_{\text{auth}}\bigr) =
\begin{cases}
\kappa_{\text{auth}} & \text{if } t + \Delta t \le t_a \\[4pt]
\bot                 & \text{otherwise}
\end{cases}
\]

Transport never carries \(\kappa_{\text{auth}}\) past the deadline as an authorization-bearing basis. The token's persistence as a document is a separate fact, captured here only by what `Degrade` produces (an explicit \(\kappa_{\text{hist}}\)).

**Pending and historical transport** — these bases persist trivially; they do not authorize execution under any rule:

\[
\mathsf{Transport}(B_{\Delta t},\; \kappa_{\text{pending}}) = \kappa_{\text{pending}}
\qquad
\mathsf{Transport}(B_{\Delta t},\; \kappa_{\text{hist}}) = \kappa_{\text{hist}}
\]

**Belated degradation** — when \(\kappa_{\text{auth}}\) crosses the deadline, both the basis kind and the action change:

\[
\mathsf{Degrade}\bigl(B_{\Delta t}: \Gamma(t) \to \Gamma(t'),\; \kappa_{\text{auth}},\; a_{\text{execute}}\bigr) =
\begin{cases}
(\kappa_{\text{hist}},\; a_{\text{record}}) & \text{if } t \le t_a < t' \\[4pt]
\bot                                          & \text{otherwise}
\end{cases}
\]

No other transport or degradation is defined.

---

## 5. Deduction rules

(Same shape as previous examples.)

**Preservation rule.** Same action, basis survives:

\[
\frac{
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\quad
B: \Gamma \to \Gamma'
\quad
\mathsf{Transport}(B, \kappa) = \kappa' \neq \bot
}{
\Gamma' \vdash_{\kappa'} \mathsf{Adm}(a)
}
\]

**Degradation rule.** Action changes with basis:

\[
\frac{
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\quad
B: \Gamma \to \Gamma'
\quad
\mathsf{Degrade}(B, \kappa, a) = (\kappa', a')
}{
\Gamma' \vdash_{\kappa'} \mathsf{Adm}(a')
}
\]

---

## 6. Two cases

### Case A — missed execution window

Authorization exists before the deadline, but the action is not taken in time. Crossing the deadline degrades execution authority into historical evidence.

Let \(t_a = 10\). Authorization granted at \(t_g = 5\).

1. **At \(t = 5\)** — granting produces \(\kappa_{\text{auth}}\). Auth-Execute holds (\(5 \le 10\)):
   \[
   \Gamma(5) \vdash_{\kappa_{\text{auth}}} \mathsf{Adm}(a_{\text{execute}}).
   \]

2. **Advance \(\Delta t = 3\) to \(t = 8\)** — inside the consequence window (\(8 \le 10\)):
   \(\mathsf{Transport}(B_3, \kappa_{\text{auth}}) = \kappa_{\text{auth}}\). Preservation:
   \[
   \Gamma(8) \vdash_{\kappa_{\text{auth}}} \mathsf{Adm}(a_{\text{execute}}).
   \]
   The action could be taken here. Suppose it is not.

3. **Advance \(\Delta t = 3\) from \(t = 8\) to \(t = 11\)** — across the deadline (\(11 > 10\)):
   \(\mathsf{Transport}(B_3, \kappa_{\text{auth}}) = \bot\); preservation does **not** fire on \(a_{\text{execute}}\).
   \(\mathsf{Degrade}(B_3, \kappa_{\text{auth}}, a_{\text{execute}}) = (\kappa_{\text{hist}}, a_{\text{record}})\) because \(8 \le 10 < 11\). Degradation:
   \[
   \Gamma(11) \vdash_{\kappa_{\text{hist}}} \mathsf{Adm}(a_{\text{record}}).
   \]

4. **Attempt \(a_{\text{execute}}\) at \(t = 11\):** Auth-Execute requires \(t \le t_a\); the side-condition fails. No rule produces an execute judgment from \(\kappa_{\text{hist}}\). Execution is not derivable.

### Case B — belated authorization

Authorization is granted after the deadline. The external granting process produces \(\kappa_{\text{hist}}\) directly (because the consequence window is already closed); \(\kappa_{\text{auth}}\) is never instantiated as an execute basis. (The granting mechanism is external to the boundary calculus; this is a constraint on what the granting process produces, not a calculus rule.)

Let \(t_a = 10\). Granting attempt at \(t_g = 13\).

1. **Before \(t_g\)**: only \(\kappa_{\text{pending}}\) exists. Pending axiom:
   \(\Gamma(t) \vdash_{\kappa_{\text{pending}}} \mathsf{Adm}(a_{\text{record}})\). \(a_{\text{execute}}\) is not derivable from any basis.

2. **At \(t_g = 13 > t_a\)**: the granting process produces \(\kappa_{\text{hist}}\) directly (not \(\kappa_{\text{auth}}\), because the consequence window is closed). Hist-Record:
   \[
   \Gamma(13) \vdash_{\kappa_{\text{hist}}} \mathsf{Adm}(a_{\text{record}}).
   \]

3. **Attempt \(a_{\text{execute}}\) at any \(t \ge 13\):** Auth-Execute would require \(t \le t_a = 10\); cannot hold. No \(\kappa_{\text{auth}}\) basis exists. Execution is not derivable from any basis.

In both cases the result is identical: \(a_{\text{record}}\) is admissible on \(\kappa_{\text{hist}}\); \(a_{\text{execute}}\) is admissible on no basis.

---

## 7. What this illustrates

- **Procedural validity ≠ operational binding.** Authorization can be procedurally correct, formally documented, and currently held — and still authorize nothing executable, because the consequence window has closed.
- **Non-overlap is the failure shape.** The pathology is not basis expiry (Example 5's TTL decay). \(\kappa_{\text{auth}}\) is not "stale." It is non-overlap between the basis-validity interval and the consequence-viability interval.
- **Late authority is evidence, not authority.** The same procedural artifact can authorize an audit record while authorizing no executable action. Cases A and B converge on the same outcome.
- **Anti-resurrection.** No rule in the system produces an execution judgment from \(\kappa_{\text{hist}}\). Historical evidence stays historical.

The core theorem-shape:

\[
\text{Valid}(\kappa_{\text{auth}}, t) \;\land\; \neg\,\text{Viable}(a_{\text{execute}}, t) \;\nRightarrow\; \mathsf{Adm}(a_{\text{execute}}, t)
\]

Slogan form: *authorization does not bind a consequence whose viability window has closed.*

---

**Keeper line:**
*Late authority is not authority over the missed consequence. It is evidence of institutional timing failure.*
