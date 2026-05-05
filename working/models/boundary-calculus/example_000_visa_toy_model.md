# Example 0: Visa Toy Model

Status: toy model / notation test  
Authority: non-doctrinal  
Purpose: demonstrates indexed admissibility, basis transport and non-inheritance  
Limitation: binary transport only; no basis-kind degradation; local axioms do most of the work

This example is intentionally small. It exists to test whether the notation runs, not to establish the final shape of the calculus.

Here’s a tiny concrete instance: **visa-based tourist stays across borders**.

---

## States, action, bases

- **States** \(\Gamma\): where the traveller is physically located.  
  \(\Gamma \in \{\mathsf{US},\; \mathsf{FR},\; \mathsf{DE}\}\)

- **Action** \(a\):  
  \(\mathsf{stay}\) (remain as a tourist)

- **Bases** \(\kappa\) (visa types held by the traveller):  
  \(\kappa \in \{\mathsf{v\_US},\; \mathsf{v\_Schengen}\}\)

The traveller is assumed to hold **both** visas at all times (they are physical documents that don’t disappear when crossing a border).  
What changes is whether a visa is *valid* in the current country.

---

## Local admissibility (axioms)

Admissibility \(\Gamma \vdash_{\kappa} \mathsf{Adm}(\mathsf{stay})\) is given by exactly these three primitive facts – one for each valid visa–country pair:

\[
\begin{aligned}
&\mathsf{US} \vdash_{\mathsf{v\_US}} \mathsf{Adm}(\mathsf{stay}) \qquad\text{(A1)} \\[2pt]
&\mathsf{FR} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay}) \qquad\text{(A2)} \\[2pt]
&\mathsf{DE} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay}) \qquad\text{(A3)}
\end{aligned}
\]

No other combination is an axiom; e.g. \(\mathsf{FR} \vdash_{\mathsf{v\_US}} \mathsf{Adm}(\mathsf{stay})\) is **not** derivable from these alone.

---

## Boundary transitions

Each boundary crossing is a transition \(B : \Gamma \to \Gamma'\):

\[
\begin{aligned}
&B_{\mathsf{US}\to\mathsf{FR}} : \mathsf{US} \to \mathsf{FR} \\
&B_{\mathsf{FR}\to\mathsf{DE}} : \mathsf{FR} \to \mathsf{DE} \\
&B_{\mathsf{DE}\to\mathsf{US}} : \mathsf{DE} \to \mathsf{US}
\end{aligned}
\]

(Only the ones relevant for the example are listed.)

---

## Transport of bases

Whether a visa \(\kappa\) “survives” the transition is governed by a validity table in the target state:

\[
\mathsf{valid\_in}(\Gamma, \kappa)
\quad
\begin{array}{c|ccc}
& \mathsf{US} & \mathsf{FR} & \mathsf{DE} \\ \hline
\mathsf{v\_US}      & \text{true} & \text{false} & \text{false} \\
\mathsf{v\_Schengen}& \text{false}& \text{true}  & \text{true}
\end{array}
\]

The transport function is then:

\[
\mathsf{Transport}(B:\Gamma\to\Gamma',\ \kappa) \;=\;
\begin{cases}
\kappa & \text{if } \mathsf{valid\_in}(\Gamma', \kappa) \\
\bot   & \text{otherwise}
\end{cases}
\]

Explicitly:
- \(\mathsf{Transport}(\mathsf{US}\to\mathsf{FR},\ \mathsf{v\_US}) = \bot\)
- \(\mathsf{Transport}(\mathsf{US}\to\mathsf{FR},\ \mathsf{v\_Schengen}) = \mathsf{v\_Schengen}\)
- \(\mathsf{Transport}(\mathsf{FR}\to\mathsf{DE},\ \mathsf{v\_Schengen}) = \mathsf{v\_Schengen}\)
- \(\mathsf{Transport}(\mathsf{FR}\to\mathsf{DE},\ \mathsf{v\_US}) = \bot\)
- \(\mathsf{Transport}(\mathsf{DE}\to\mathsf{US},\ \mathsf{v\_Schengen}) = \bot\)
- \(\mathsf{Transport}(\mathsf{DE}\to\mathsf{US},\ \mathsf{v\_US}) = \mathsf{v\_US}\)

---

## The preservation rule (the only deduction rule for transitions)

\[
\frac{
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\quad
\mathsf{Transport}(B:\Gamma\to\Gamma',\ \kappa) \neq \bot
\quad
\kappa' = \mathsf{Transport}(B,\kappa)
}{
\Gamma' \vdash_{\kappa'} \mathsf{Adm}(a)
}
\]

---

## Non‑inheritance (meta‑level)

There is **no rule** that allows one to infer anything about
\(\Gamma' \vdash_{\kappa} \mathsf{Adm}(a)\) when the transport of \(\kappa\) fails.
The failure simply means the old basis cannot be carried forward.
Admissibility may still be established in \(\Gamma'\) using a **different** basis,
by applying the axioms of the new state directly.

---

## A trace through the system

1. **Start in the US**  
   By axiom (A1): \(\mathsf{US} \vdash_{\mathsf{v\_US}} \mathsf{Adm}(\mathsf{stay})\).

2. **Cross from US to FR** (\(B_{\mathsf{US}\to\mathsf{FR}}\))  
   Transport of \(\mathsf{v\_US}\) fails (\(\bot\)).  
   Preservation does **not** apply; we get **no** judgement of the form
   \(\mathsf{FR} \vdash_{\mathsf{v\_US}} \mathsf{Adm}(\mathsf{stay})\).

   However, axiom (A2) independently gives us a **fresh basis**:  
   \(\mathsf{FR} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay})\).

3. **Cross from FR to DE** (\(B_{\mathsf{FR}\to\mathsf{DE}}\))  
   We have \(\mathsf{FR} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay})\).  
   \(\mathsf{Transport}\) for \(\mathsf{v\_Schengen}\) is successful:
   \(\mathsf{Transport}(\mathsf{FR}\to\mathsf{DE},\ \mathsf{v\_Schengen}) = \mathsf{v\_Schengen}\).  
   Preservation yields: \(\mathsf{DE} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay})\), exactly matching axiom (A3).

4. **Cross back to the US** (\(B_{\mathsf{DE}\to\mathsf{US}}\))  
   Transport of \(\mathsf{v\_Schengen}\) fails (\(\bot\)), so the judgement from DE does **not** carry.  
   Once again we cannot conclude anything about \(\mathsf{US} \vdash_{\mathsf{v\_Schengen}} \mathsf{Adm}(\mathsf{stay})\).  
   But by axiom (A1) we **re‑establish** admissibility on the fresh basis \(\mathsf{v\_US}\).

---

This miniature calculus shows:

- **Preservation** when the basis is recognised in the destination (\(\mathsf{FR}\to\mathsf{DE}\)).
- **Loss of the basis** when it is not recognised (\(\mathsf{US}\to\mathsf{FR}\), \(\mathsf{DE}\to\mathsf{US}\)).
- **Non‑inheritance** in practice: the failure never forces inadmissibility; a new basis can always be invoked if one exists.

## Known limitations

- Transport is modeled as target validity, not authority-role preservation.
- Bases are binary: they either survive or fail.
- The model does not represent degradation, e.g. authorization becoming historical evidence.
- Target-state axioms can re-establish admissibility directly, so preservation is illustrative rather than necessary.

## Next example

Example 1 models maintenance-window authorization crossing a time boundary:
a live authorization token survives as historical evidence but no longer authorizes execution after the window closes.

## Cold-read notes

External cold reads identified this example as an instance of indexed admissibility / modal authorization-style logic.

Useful refinements:
- Treat Transport as a partial relation in later examples.
- Treat validity as recognition by the target state, not merely a global table.
- Add later examples with basis degradation, cumulative budget and time-window expiration.

This example intentionally remains binary.
