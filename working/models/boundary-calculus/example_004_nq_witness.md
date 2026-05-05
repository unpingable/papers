# Example 4: NQ Witness Testimony

Status: toy model / local-derivation + anti-laundering example
Authority: non-doctrinal
Purpose: observation survives ingest as evidence, but testimony is locally constructed only when explicit coverage permits it
Adds beyond previous examples:
- local derivation rules (alongside boundary transport / degradation)
- basis pairing (observation + coverage → testimony)
- explicit coverage as a condition of testimony (via a separate Cov predicate)
- anti-laundering from observation to finding
- negative coverage / cannot_testify as a blocking verdict

Core lesson:
Observation may survive ingest as evidence, but testimony is locally constructed only when explicit coverage permits it.

### NQ Witness Testimony — Observation Survives, Testimony Does Not  

A raw backend observation is admissible as evidence, but testimony-grade claims require explicit witness coverage. Crossing from observation space into testimony space the raw basis cannot be silently upgraded; only a properly paired observation and coverage declaration can produce testimony. The testimony, once formed, can authorise a finding, but the raw observation alone can never travel directly to a finding.

---

### 1. States, action, bases  

**States** \(\Gamma\):  

| State          | Meaning                                         |
|----------------|-------------------------------------------------|
| \(\Gamma_{\text{backend}}\) | Backend / integration state – raw data lives here       |
| \(\Gamma_{\text{witness}}\) | Witness evaluation state – coverage is declared here   |
| \(\Gamma_{\text{finding}}\) | Finding / export state – final conclusions live here    |

**Actions** \(a\):  

| Action          | Description                                      |
|-----------------|--------------------------------------------------|
| \(a_{\text{observe}}\) | Record / hold a raw observation            |
| \(a_{\text{testify}}\) | Issue witness testimony (a graded statement) |
| \(a_{\text{find}}\)    | Emit a formal finding based on testimony     |

**Bases** \(\kappa\):  

| Basis       | Kind                          |
|-------------|-------------------------------|
| \(\kappa_{\text{obs}}\)  | Raw backend observation       |
| \(\kappa_{\text{cov}}\)  | Witness coverage declaration  |
| \(\kappa_{\text{test}}\) | Testimony basis               |
| \(\kappa_{\text{find}}\) | Finding basis                 |

A coverage basis \(\kappa_{\text{cov}}\) is not a basis for an action; it is a basis for a coverage *verdict* of the form \(\mathsf{Cov}(\text{scope},\; v)\) where \(v \in \{\mathbf{can\_testify},\; \mathbf{cannot\_testify}\}\). The \(\mathbf{cannot\_testify}\) verdict is an explicit "cannot testify" declaration, distinct from absence of any coverage at all. Treating coverage as a verdict (not as `Adm(a_declare)`) avoids the semantic awkwardness of having a `cannot_testify` token "authorize" a declaration.

---

### 2. Primitive admissibility (axioms)  

\[
\begin{aligned}
&\text{(A1)}\quad 
\Gamma_{\text{backend}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}}) \\[4pt]
&\text{(A2)}\quad 
\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{cov}}}\; \mathsf{Cov}(\text{scope},\; v)
\quad\text{(optional; only present if coverage is declared)}
\end{aligned}
\]

Axiom (A2) may be instantiated with \(v = \mathbf{can\_testify}\) or \(v = \mathbf{cannot\_testify}\), each for some scope (e.g., the scope of the observation). If coverage has never been declared, the axiom is simply absent.

---

### 3. Boundary transitions  

\[
\begin{aligned}
B_{\text{ingest}} &: \Gamma_{\text{backend}} \to \Gamma_{\text{witness}} \quad\text{(observation moves into witness context)} \\
B_{\text{emit}}   &: \Gamma_{\text{witness}} \to \Gamma_{\text{finding}} \quad\text{(testimony moves into finding context)}
\end{aligned}
\]

---

### 4. Transport, degradation, and a local derivation rule  

**Transport** (same‑action persistence):  

\[
\mathsf{Transport}(B_{\text{ingest}},\; \kappa_{\text{obs}}) = \kappa_{\text{obs}}
\qquad
\text{all other cases } \bot
\]

**Degradation** (action‑change across a boundary):  

\[
\mathsf{Degrade}(B_{\text{emit}},\; \kappa_{\text{test}},\; a_{\text{testify}})
\;=\; (\kappa_{\text{find}},\; a_{\text{find}})
\qquad
\text{all other cases } \bot
\]

No other transport or degradation is defined.

**Witness testimony rule (WTR)** – a **local derivation rule** inside \(\Gamma_{\text{witness}}\):

\[
\frac{
\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}})
\qquad
\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{cov}}}\; \mathsf{Cov}(\mathsf{scope}(\kappa_{\text{obs}}),\; \mathbf{can\_testify})
}{
\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{test}}}\; \mathsf{Adm}(a_{\text{testify}})
}
\]

This rule is the **only** way to obtain the testimony basis \(\kappa_{\text{test}}\). If coverage is absent, or if the only available coverage verdict is \(\mathbf{cannot\_testify}\), the second premise is unsatisfiable and the rule cannot fire.

---

### 5. Deduction rules for boundaries  

- **Preservation rule**:  
  \[
  \frac{
  \Gamma \vdash_{\kappa} \mathsf{Adm}(a)
  \qquad
  B : \Gamma \to \Gamma'
  \qquad
  \mathsf{Transport}(B,\kappa) = \kappa' \neq \bot
  }{
  \Gamma' \vdash_{\kappa'} \mathsf{Adm}(a)
  }
  \]

- **Degradation rule**:  
  \[
  \frac{
  \Gamma \vdash_{\kappa} \mathsf{Adm}(a)
  \qquad
  B : \Gamma \to \Gamma'
  \qquad
  \mathsf{Degrade}(B,\kappa,a) = (\kappa',a')
  }{
  \Gamma' \vdash_{\kappa'} \mathsf{Adm}(a')
  }
  \]

---

### 6. Successful trace (coverage present and permissive)  

1. **Backend observation** (A1)  
   \(\Gamma_{\text{backend}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}})\).

2. **Ingest into witness** via \(B_{\text{ingest}}\)  
   \(\mathsf{Transport}(B_{\text{ingest}},\kappa_{\text{obs}}) = \kappa_{\text{obs}}\).  
   Preservation yields:  
   \(\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}})\).

3. **Coverage declared** (A2, with \(v = \mathbf{can\_testify}\) for the relevant scope)  
   \(\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{cov}}}\; \mathsf{Cov}(\mathsf{scope}(\kappa_{\text{obs}}),\; \mathbf{can\_testify})\).

4. **WTR fires**: the two premises combined satisfy the rule, so we obtain  
   \(\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{test}}}\; \mathsf{Adm}(a_{\text{testify}})\).

5. **Emit finding** via \(B_{\text{emit}}\)  
   \(\mathsf{Degrade}(B_{\text{emit}}, \kappa_{\text{test}}, a_{\text{testify}}) = (\kappa_{\text{find}}, a_{\text{find}})\).  
   Degradation rule yields:  
   \(\Gamma_{\text{finding}} \;\vdash_{\kappa_{\text{find}}}\; \mathsf{Adm}(a_{\text{find}})\).

---

### 7. Failure trace (coverage missing)  

1. \(\Gamma_{\text{backend}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}})\) as before.  
2. Ingest → \(\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{obs}}}\; \mathsf{Adm}(a_{\text{observe}})\).  
3. **No coverage axiom** — no \(\mathsf{Cov}\) verdict is available for any scope.  
   The WTR premise \(\Gamma_{\text{witness}} \vdash_{\kappa_{\text{cov}}} \mathsf{Cov}(\mathsf{scope}(\kappa_{\text{obs}}),\; \mathbf{can\_testify})\) cannot be satisfied.  
4. Therefore \(\kappa_{\text{test}}\) is **underivable**.  
5. Since no judgment of the form \(\Gamma_{\text{witness}} \vdash_{\kappa_{\text{test}}} \mathsf{Adm}(a_{\text{testify}})\) exists,  
   the degradation rule for \(B_{\text{emit}}\) does not fire.  
6. \(\Gamma_{\text{finding}} \vdash_{\kappa_{\text{find}}} \mathsf{Adm}(a_{\text{find}})\) remains **underivable**.  
7. The raw observation \(\kappa_{\text{obs}}\) is still present in \(\Gamma_{\text{witness}}\), but it cannot generate testimony or a finding.

---

### 8. Failure trace (coverage says “cannot testify”)  

Same as above, except (A2) is present with \(v = \mathbf{cannot\_testify}\), giving:

\[
\Gamma_{\text{witness}} \;\vdash_{\kappa_{\text{cov}}}\; \mathsf{Cov}(\mathsf{scope}(\kappa_{\text{obs}}),\; \mathbf{cannot\_testify}).
\]

The WTR's second premise requires \(\mathsf{Cov}(\mathsf{scope}(\kappa_{\text{obs}}),\; \mathbf{can\_testify})\), which is not derivable from the available \(\mathbf{cannot\_testify}\) verdict (the two verdicts are distinct; one does not entail the other). Therefore the rule does not fire.  
Result: testimony and finding are again underivable, despite raw observation and a formal coverage declaration existing.

---

### 9. Summary  

- \(\kappa_{\text{obs}}\) **survives** the ingest boundary, preserving the ability to speak about the observation.  
- But the raw observation basis **never silently upgrades** to testimony; testimony requires explicit, permissive coverage (\(\mathbf{can\_testify}\)).  
- If coverage is absent or explicitly denies testimony (\(\mathbf{cannot\_testify}\)), the system refuses to derive \(\mathsf{Adm}(a_{\text{testify}})\).  
- From testimony, a finding can be produced via degradation, but raw observation cannot jump directly to a finding (no transport/degradation path exists).  
- The model obeys the core non‑inheritance principle: admissibility of an observation in \(\Gamma_{\text{backend}}\) does not entail admissibility of testimony or finding in later states under the same basis.

---

### 10. Known limitations  

- Coverage is treated as a single global declaration; a richer model would index coverage to particular observation sets or time‑windows.  
- The degradation from testimony to finding is one‑way; no provision is made for findings that later require re‑testimony.  
- The witness testimony rule is intentionally local. Boundary transport governs what survives crossing; local derivation governs what can be constructed inside a state from admissible bases (and verdicts) already present there. The two are complementary, not redundant; future work should not seek to eliminate local derivation by pushing all construction into transition combinators — doing so would let "boundary calculus" eat normal inference.

---

**Keeper line:**  
*Observation can cross the boundary as evidence. It cannot appoint itself witness.*
