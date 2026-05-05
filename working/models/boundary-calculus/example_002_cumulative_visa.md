# Example 2: Cumulative Visa Budget

Status: toy model / mutable-basis example
Authority: non-doctrinal
Purpose: demonstrates basis mutation across repeated boundary transitions
Adds beyond previous examples:
  - numeric basis value
  - resource consumption
  - repeated composition
  - exhaustion / underivability
Known limitation:
  - cost is attached only to destination states
  - no identity transitions
  - no distinction between calendar time and transition cost
  - no recovery/fresh-basis rule

This example treats Transport not as mere recognition but as a value-transforming operation on the basis.

### Cumulative visa / time budget — basis mutates across repeated transitions  

Here, the basis is a **mutable numeric resource** (remaining days on a visa). Every boundary transition into a new country deducts the cost of that country from the budget. The basis evolves across repeated transitions, always authorising the same action (`present`), but with a shrinking balance. If the budget becomes insufficient for a transition, the basis cannot be transported and presence in the new country is underivable from that basis.

---

### 1. States, action, basis

- **States** \(\Gamma\):  
  \(\Gamma_{\text{out}}\) (outside the travel area),  
  \(\Gamma_X\) (country X),  
  \(\Gamma_Y\) (country Y),  
  \(\Gamma_Z\) (country Z).

- **Action** \(a\):  
  `present` – the traveller is legally present in the current state.

- **Basis** \(\kappa\):  
  \(\mathsf{visa}(n)\) where \(n \in \mathbb{N}\) is the **remaining days**.

- **Costs** assigned to countries:  
  \[
  \begin{aligned}
  \text{cost}(X) &= 10 \\
  \text{cost}(Y) &= 5 \\
  \text{cost}(Z) &= 3
  \end{aligned}
  \]

  There is no cost for being outside.

---

### 2. Primitive admissibility (axiom)

The only initial fact is the starting basis outside:

\[
\text{(A0)}\quad
\Gamma_{\text{out}} \;\vdash_{\mathsf{visa}(90)}\; \mathsf{Adm}(\mathsf{present})
\]

No other direct admissibility judgments exist for the countries. The only way to obtain them is through the boundary transition rules.

---

### 3. Boundary transitions

We allow transitions from any state to any other distinct state (outside ↔ countries, and between countries). The set:

\[
\mathcal{B} = \{\, B_{\Gamma \to \Gamma'} \mid \Gamma, \Gamma' \in \{\Gamma_{\text{out}}, \Gamma_X, \Gamma_Y, \Gamma_Z\},\;\Gamma \neq \Gamma' \,\}
\]

(For simplicity, we ignore identity transitions.)

---

### 4. Transport (basis mutation)

The transport function for a transition into a country \(\Gamma'\) deducts the country’s cost from the visa balance. For a transition out of a country into \(\Gamma_{\text{out}}\), the basis is preserved unchanged (no cost). Formally:

\[
\mathsf{Transport}(B_{\Gamma \to \Gamma'},\; \mathsf{visa}(n)) =
\begin{cases}
\mathsf{visa}(n - \text{cost}(\Gamma')) & \text{if } \Gamma' \neq \Gamma_{\text{out}} \text{ and } n \geq \text{cost}(\Gamma') \\
\mathsf{visa}(n)                       & \text{if } \Gamma' = \Gamma_{\text{out}} \\
\bot                                    & \text{otherwise}
\end{cases}
\]

That is:
- Entering a country with cost \(c\) consumes \(c\) days (if enough remain).
- Returning to outside costs nothing, and the balance is unchanged.
- Insufficient days cause transport failure.

---

### 5. Deduction rule (preservation with mutation)

There is a single rule that lifts admissibility across a boundary, mutating the basis:

\[
\frac{
\Gamma \;\vdash_{\kappa}\; \mathsf{Adm}(a)
\qquad
B : \Gamma \to \Gamma'
\qquad
\mathsf{Transport}(B,\;\kappa) = \kappa' \neq \bot
}{
\Gamma' \;\vdash_{\kappa'}\; \mathsf{Adm}(a)
}
\]

No other rule invents new bases or resurrects failed transports. The action \(a\) is always `present`.

---

### 6. Example trace

Start with the axiom:
\[
\Gamma_{\text{out}} \;\vdash_{\mathsf{visa}(90)}\; \mathsf{Adm}(\mathsf{present}) \tag{1}
\]

**Move into country X**

Take \(B_{\text{out} \to X}\).  
\(\text{cost}(X)=10\).  
\(\mathsf{Transport}(B_{\text{out} \to X},\; \mathsf{visa}(90)) = \mathsf{visa}(80)\).  
By the preservation rule:
\[
\Gamma_X \;\vdash_{\mathsf{visa}(80)}\; \mathsf{Adm}(\mathsf{present}) \tag{2}
\]

**Move to country Y**

Take \(B_{X \to Y}\).  
\(\text{cost}(Y)=5\).  
\(\mathsf{Transport}(B_{X \to Y},\; \mathsf{visa}(80)) = \mathsf{visa}(75)\).  
We obtain:
\[
\Gamma_Y \;\vdash_{\mathsf{visa}(75)}\; \mathsf{Adm}(\mathsf{present}) \tag{3}
\]

**Move to country Z**

Take \(B_{Y \to Z}\).  
\(\text{cost}(Z)=3\).  
\(\mathsf{Transport}(B_{Y \to Z},\; \mathsf{visa}(75)) = \mathsf{visa}(72)\).  
We obtain:
\[
\Gamma_Z \;\vdash_{\mathsf{visa}(72)}\; \mathsf{Adm}(\mathsf{present}) \tag{4}
\]

**Return to outside**

Take \(B_{Z \to \text{out}}\) from (4).  
\(\mathsf{Transport}(B_{Z \to \text{out}},\; \mathsf{visa}(72)) = \mathsf{visa}(72)\).  
We obtain:
\[
\Gamma_{\text{out}} \;\vdash_{\mathsf{visa}(72)}\; \mathsf{Adm}(\mathsf{present}) \tag{5}
\]
The balance is preserved.

After repeated transitions, suppose the current judgment is:

\[
\Gamma_Y \vdash_{\mathsf{visa}(2)} \mathsf{Adm}(\mathsf{present})
\]

Attempt to enter country X:

\[
\mathsf{Transport}(B_{Y \to X}, \mathsf{visa}(2)) = \bot
\]

because \(2 < \text{cost}(X)=10\). Therefore no judgment

\[
\Gamma_X \vdash_{\mathsf{visa}(2)} \mathsf{Adm}(\mathsf{present})
\]

is derivable from this basis.

---

### 7. Observations

- **Basis mutation**: The same kind of basis (`visa(n)`) authorises the same action (`present`) in every state, but its *value* changes stepwise with each border crossing — a cumulative time budget.
- **Repeated transitions**: Each move into a country that consumes days further mutates the basis. This models a real‑world scenario where a single multiple‑entry visa has a total allowed stay, used up progressively across different countries.
- **Transport failure = underivability**: When the balance drops below a country’s requirement, the basis cannot be transported, and presence there cannot be justified from that old basis. A fresh basis (e.g., a new visa) would be needed, but that is outside this model.
- **No ad hoc resurrection**: There is no rule that lets you `Adm(present)` in a country without either starting there axiomatically (there are no such axioms) or arriving via a successful transport. The system is closed under the transport rule.

This instance shows that the boundary calculus easily captures **mutable numeric credentials** and **resource‑consuming transitions**, with admissibility tied to the ever‑shrinking resource.

---

**Keeper line:**
*The basis survives, but not unchanged.*
