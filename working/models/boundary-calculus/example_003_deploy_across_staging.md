# Example 3: Staging → Production Promotion

Status: toy model / scope-boundary example
Authority: non-doctrinal
Purpose: demonstrates that authorization does not inherit across scope boundaries
Adds beyond previous examples:
  - scope-local credentials
  - artifact/authority separation
  - fresh target-scope basis
Known limitation:
  - action should probably be parameterized by target environment
  - artifact transport is implicit, not modeled
  - production basis is axiomatically available rather than provisioned by a separate rule

### Deploy across staging → production — scope boundary blocks inherited authorization

In this model, a deployment action is authorized in a staging environment under a staging‑specific credential. Promoting that deployment to production crosses a **scope boundary** that explicitly prevents the staging credential from being carried forward. Production requires its own, independently provisioned authorization.

---

### 1. States, action, bases

- **States** \(\Gamma\):  
  \(\Gamma_{\text{staging}}\) – the staging environment,  
  \(\Gamma_{\text{prod}}\) – the production environment.

- **Action** \(a\):  
  `deploy` – push the application artifact to the environment and make it live.

- **Bases** \(\kappa\):  
  \(\mathsf{stag\_key}\) – a credential valid only for staging,  
  \(\mathsf{prod\_key}\) – a credential valid only for production.

---

### 2. Primitive admissibility (axioms)

Exactly two base facts are given:

\[
\begin{aligned}
&\text{(A1)}\quad \Gamma_{\text{staging}} \;\vdash_{\mathsf{stag\_key}}\; \mathsf{Adm}(\mathsf{deploy}) \\[4pt]
&\text{(A2)}\quad \Gamma_{\text{prod}}   \;\vdash_{\mathsf{prod\_key}}\; \mathsf{Adm}(\mathsf{deploy})
\end{aligned}
\]

Neither credential is recognised in the other environment. In particular, \(\Gamma_{\text{prod}} \vdash_{\mathsf{stag\_key}} \mathsf{Adm}(\mathsf{deploy})\) is **not** an axiom and cannot be derived from the rules that follow.

---

### 3. Boundary transition

A single promotion transition moves the context from staging to production:

\[
B_{\text{promote}} : \Gamma_{\text{staging}} \to \Gamma_{\text{prod}}
\]

This transition represents the act of promoting the deployment artifact across the environment boundary.

---

### 4. Transport function (scope boundary)

The transport function encodes the scoping rule: the staging key is **scoped** to staging only, and therefore cannot survive the transition. We narrow the formal statement to the case the model actually uses:

\[
\mathsf{Transport}(B_{\text{promote}},\; \mathsf{stag\_key}) = \bot
\]

For other bases the transport function is left unspecified in this model. The central claim is narrow and load-bearing: the staging credential cannot be transported across the promotion boundary. Whether other bases survive promotion is a separate design question that does not affect this example. The earlier "absolute block for all κ" framing was an over-statement — production credentials, for instance, are not "blocked by promotion"; they are simply not obtained through that transition.

---

### 5. Deduction rule

Only the preservation rule is needed:

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

There is no degradation rule, and no rule that invents new bases. If the transport fails, the rule simply does not fire.

---

### 6. Non‑inheritance in action

Starting from the axiom (A1):

\[
\Gamma_{\text{staging}} \;\vdash_{\mathsf{stag\_key}}\; \mathsf{Adm}(\mathsf{deploy}) \tag{1}
\]

We apply the transition \(B_{\text{promote}}\). Because \(\mathsf{Transport}(B_{\text{promote}}, \mathsf{stag\_key}) = \bot\), the preservation rule does **not** apply. We therefore obtain **no** judgement of the form

\[
\Gamma_{\text{prod}} \;\vdash_{\mathsf{stag\_key}}\; \mathsf{Adm}(\mathsf{deploy})
\]

Thus, the staging authorization is **blocked** at the scope boundary – it cannot be inherited in production.

---

### 7. Fresh basis restores authorization

Despite the transport failure, the production environment is not left without any authorization. The axiom (A2) provides a **fresh basis** that is completely independent of the staging one:

\[
\Gamma_{\text{prod}} \;\vdash_{\mathsf{prod\_key}}\; \mathsf{Adm}(\mathsf{deploy}) \tag{2}
\]

This fresh basis is not the result of a transport or transformation; it is a separate primitive that must be provisioned in the production scope. The boundary calculus accurately captures the real‑world practice where production deployments require their own credentials, distinct from those used in staging.

---

### 8. Summary

- The **scope boundary** is expressed as a transport failure for the staging credential.
- Admissibility of `deploy` in staging does **not** entail admissibility of `deploy` in production under the same basis.
- The system nevertheless remains consistent because production can have its own axiomatically given basis, entirely disconnected from the staging authorisation.
- This is a clean instance of the core negation: \(\mathsf{Adm}(a,\Gamma) \land \neg\mathsf{Survives}(B,a) \nRightarrow \mathsf{Adm}(a,\Gamma')\). The failure of transport leaves the truth of admissibility in the target state completely open; it may be established by other means (or not).

---

**Keeper line:**
*Promotion may transport the artifact; it does not transport staging authority.*
