# Blind-Auditor Bundle — Cross-Altitude Novelty Audit (self-contained)

**Packet prepared:** 2026-06-07. **Self-contained.** **Does not require file or URL access** to perform the audit; all materials needed are inlined below. URLs are provided for verification only.

## What you are being asked to do

You are auditing five proposed claims against a frozen corpus of eight documents (excerpts inlined below). For each claim, decide whether the corpus supports it, refutes it, contains the proposal under different vocabulary, exhibits a hidden lexical fracture, or fits another category from the verdict palette.

Cite specific excerpts by their bracketed IDs (e.g. `[PEP635-MOTIVATION-01]`). Be explicit about uncertainty.

The corpus has no typechecker, no theorem prover, no executable test suite invoked. You may use a Python interpreter or static analyzer to sharpen verdicts; if you do, mark explicitly where mechanical aid was used.

You may revise verdicts on re-read. Mark any verdict that changed during your audit and explain why.

## Audit method (terse)

The Cross-Altitude Novelty Audit tests whether a proposed claim about a feature, design, or specification:

1. Already exists in the corpus at some altitude (DUPLICATE)
2. Collides with the corpus's own internal disambiguation of similar concepts (ALIAS-RISK)
3. Is explicitly refused by some altitude of the corpus itself (INTERNAL-REFUTATION GAP)
4. Imports framing one altitude of the corpus rejects, smoothing it over from another altitude (LAUNDERING)
5. Silently assumes a precondition another corpus artifact formalizes (MISSING-PRECONDITION)
6. Sits in a real gap the corpus knows about but does not authorize the claim's filling (GAP CONFIRMED + RELAY-FRAMING REFUSED)
7. Would compose two valid artifacts into a third the corpus does not endorse (COMPOSITION-GAP)
8. Is a candidate cross-altitude bridge (BRIDGE-CANDIDATE)
9. May contradict an existing claim (COUNTEREXAMPLE-CANDIDATE)
10. Has no real connection (DEAD-END)

The audit's discriminator is *cross-altitude*: a claim that looks novel at one altitude may be old or refused at another. Read across the corpus's altitudes before settling on a verdict.

## Verdict palette (definitions; use these exact labels)

| Label | Definition |
|---|---|
| **DUPLICATE** | The proposed claim already exists in the corpus under different vocabulary or at a different altitude. Cite the corpus location that contains the claim. |
| **ALIAS-RISK** | A single word, phrase, or concept in the claim carries multiple distinct relations across the corpus; the claim collapses them. Cite each sense the corpus uses and the location for each. |
| **LAUNDERING** | The claim imports a framing or mental-model the corpus's decision-record altitude (rationale / proposal / design-doc) explicitly rejects; another altitude (changelog / release-notes / tutorial) carries the rejected framing as if it were endorsed. Cite the rejection and the import. |
| **INTERNAL-REFUTATION GAP** | A real gap or open question exists; the corpus itself contains the refusal of the tempting framing the claim proposes. The audit records that the refusal exists at a specific altitude. Cite the refusal. |
| **MISSING-PRECONDITION** | One corpus artifact silently assumes a condition another corpus artifact formalizes, but the dependency is not surfaced. The claim names the condition without naming the corpus dependency. Cite both artifacts. |
| **GAP CONFIRMED + RELAY-FRAMING REFUSED** | A real corpus gap exists; the claim proposes a framing the corpus is structurally not authorized to accept. Cite the gap and the structural refusal. |
| **BRIDGE-CANDIDATE** | The claim names a possible cross-altitude bridge that does not yet exist in the corpus. Cite the prospective endpoints. |
| **COMPOSITION-GAP** | Two corpus artifacts are individually valid but their composition produces a result the corpus does not endorse. Cite the components and the failed composition. |
| **COUNTEREXAMPLE-CANDIDATE** | The claim contradicts an existing corpus claim under specific conditions. Cite the contradiction. |
| **DEAD-END** | No real connection; the claim is a false positive. Brief justification only. |

Multi-class verdicts (e.g., `ALIAS-RISK + INTERNAL-REFUTATION GAP`) are permitted when the claim genuinely exhibits more than one class. State each class and its citation separately.

If none of the existing labels fits, record the claim as **LABEL-FAILURE** with a brief explanation. Do not invent new labels.

## Frozen corpus manifest

Eight documents, six altitude classes, no formal proof layer.

| # | Document | URL (for verification only) | Altitude |
|---|---|---|---|
| 1 | PEP 634 — Structural Pattern Matching: Specification | https://peps.python.org/pep-0634/ | normative spec / proposal |
| 2 | PEP 635 — Structural Pattern Matching: Motivation and Rationale | https://peps.python.org/pep-0635/ | argument / rationale |
| 3 | PEP 636 — Structural Pattern Matching: Tutorial | https://peps.python.org/pep-0636/ | tutorial / user-facing docs |
| 4 | Python 3.10 What's New — Structural Pattern Matching section | https://docs.python.org/3/whatsnew/3.10.html | changelog / release residue |
| 5 | Python Language Reference — The `match` statement | https://docs.python.org/3/reference/compound_stmts.html#the-match-statement | normative reference |
| 6 | CPython implementation tracking | https://github.com/python/cpython/issues/86294 | implementation tracking |
| 7 | CPython implementation PR | https://github.com/python/cpython/pull/22917 | implementation decision |
| 8 | PEP 653 — Precise Semantics for Pattern Matching | https://peps.python.org/pep-0653/ | follow-up PEP / re-specification |

## Claims to audit

Five claims. Audit each independently.

**Claim A.** *"Structural pattern matching in Python 3.10 unifies sequence unpacking, `isinstance()` checking, and dict-key extraction under a single declarative form, replacing the historical fragmentation of these idioms."*

**Claim B.** *"The match statement exhibits a binding-vs-comparison semantic fracture: capture patterns bind, value patterns compare, and the syntactic disambiguator (dotted vs bare names) is load-bearing for type safety."*

**Claim C.** *"PEP 634's first-to-match semantics silently assume guards are side-effect-free; without this assumption, the first-to-match guarantee provides no meaningful determinism over the program state observed in case bodies."*

**Claim D.** *"Pattern matching extends the switch statement found in C/Java/JavaScript to support structural decomposition of subject values; the case-clause discipline is the same in spirit, with the addition of binding semantics."*

**Claim E.** *"PEP 634's class pattern semantics are sufficient for production use because `isinstance()` plus `__match_args__` covers all observed class-matching needs, with `collections.abc` providing the sequence/mapping classification."*

---

# Inline corpus excerpts

Each excerpt has: bracketed ID, source title, URL, altitude, and the excerpt text. Excerpts are drawn from frozen documents stored at the listed URLs; full sanitized source files are available in the companion zip if you need surrounding context.

The excerpts below are selected to support audit of the five claims. They are *not* a complete reproduction of the corpus; if you want to verify outside this excerpt set, the URLs are provided.

## From Document 1: PEP 634 (spec)

### [PEP634-PATTERNS-01] Pattern types enumerated
- **Source:** PEP 634, Pattern Types section
- **URL:** https://peps.python.org/pep-0634/
- **Altitude:** normative spec
- **Excerpt:**

> Pattern Types Defined:
> - **Literal Patterns**: Match specific values (numbers, strings, None, True, False)
> - **Capture Patterns**: Bind the subject to a name
> - **Wildcard Pattern**: Matches anything without binding (`_`)
> - **Value Patterns**: Match dotted names against subject values
> - **Group Patterns**: Parenthesized patterns for emphasis
> - **Sequence Patterns**: Match sequences like lists/tuples with fixed or variable lengths
> - **Mapping Patterns**: Match dictionaries with specific keys
> - **Class Patterns**: Match class instances and extract attributes
> - **OR Patterns**: Match alternatives separated by `|`
> - **AS Patterns**: Bind matched results to names
>
> Key normative claims:
> - "match" and "case" are soft keywords, not reserved words, allowing their use as variable names in other contexts.
> - Name bindings from successful pattern matches outlive the executed block.
> - Guards evaluate in order and stop once a case block is selected.
> - An irrefutable pattern (guaranteed to succeed) can only appear as the final case block.
> - Sequence patterns exclude strings, bytes, and bytearray despite their sequence nature.
> - Standard library classes like namedtuples and dataclasses receive auto-generated `__match_args__` attributes to support positional pattern matching.

---

## From Document 2: PEP 635 (rationale)

### [PEP635-MOTIVATION-01] Idioms enhanced by pattern matching
- **Source:** PEP 635, Motivation section
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** argument / rationale
- **Excerpt:**

> **Type and Shape Checking:**
>
> ```python
> # Before
> if isinstance(x, tuple) and len(x) == 2:
>     host, port = x
>     mode = "http"
> elif isinstance(x, tuple) and len(x) == 3:
>     host, port, mode = x
>
> # After
> match x:
>     case host, port:
>         mode = "http"
>     case host, port, mode:
>         pass
> ```
>
> **AST Traversal:**
>
> ```python
> # Before
> if (isinstance(node, BinOp) and node.op == "+"
>         and isinstance(node.right, BinOp) and node.right.op == "*"):
>     a, b, c = node.left, node.right.left, node.right.right
>
> # After
> match node:
>     case BinOp("+", a, BinOp("*", b, c)):
>         # Handle a + b*c
> ```

### [PEP635-PATTERNS-CONSTRAINTS-01] Patterns are not expressions; bind not assign
- **Source:** PEP 635, Rationale / Patterns
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "Patterns fulfill two purposes: they impose (structural) constraints on the subject and they specify which data values should be extracted from the subject and bound to variables."
>
> "Although patterns might superficially look like expressions, it is important to keep in mind that there is a clear distinction. In fact, no pattern is or contains an expression."
>
> "Patterns bind names to values rather than performing an assignment. This reflects the fact that patterns aim to not have side effects." The term "bind" emphasizes this distinction from traditional variable assignment.

### [PEP635-GUARDS-01] Patterns ideally pure; guards permit dynamic eval
- **Source:** PEP 635, Rationale / Guards
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "From a conceptual point of view, patterns describe structural constraints on the subject in a declarative style, ideally without any side-effects. Guards bridge this by allowing dynamic evaluation where pure patterns are insufficient."
>
> Guards are attached only to case clauses, not individual patterns, maintaining clear separation between structural and dynamic logic.

### [PEP635-CAPTURE-01] Rationale against explicit capture markers
- **Source:** PEP 635, Rationale / Capture Patterns
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "Capture patterns take on the form of a name that accepts any value and binds it to a (local) variable (unless the name is declared as `nonlocal` or `global`)."
>
> "A name used for a capture pattern must not coincide with another capture pattern in the same pattern." This mirrors function parameters, which must be unique.
>
> **Rationale Against Explicit Markers:**
>
> Proposals to mark capture patterns (e.g., `?x`, `$x`, `=x`) were rejected:
> - Based on **misconception that pattern matching extends switch statements**.
> - Would undermine pattern matching's core purpose: binding extracted values.
> - Explicit markers introduce unnecessary syntactic clutter.

### [PEP635-WILDCARD-01] Wildcard rationale and else-block rejection
- **Source:** PEP 635, Rationale / Wildcard Pattern
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "The wildcard pattern is a special case of a 'capture' pattern: it accepts any value, but does not bind it to a variable."
>
> Universal in every language with pattern matching: "C#, Elixir, Erlang, F#, Grace, Haskell, Mathematica, OCaml, Ruby, Rust, Scala, Swift, and Thorn"
>
> **Else Block Rejection:**
> `case _:` is not equivalent to an `else:` block syntactically because either could follow `case` without ambiguity, making indentation placement contentious.

### [PEP635-VALUE-01] Value patterns vs capture patterns: dotted-name rule
- **Source:** PEP 635, Rationale / Value Patterns
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "Strictly speaking, value patterns are not really necessary, but could be implemented using guards, i.e. `case (status, body) if status == HttpStatus.OK:`. Nonetheless, the convenience of value patterns is unquestioned and obvious."
>
> **Rule for Distinguishing from Capture Patterns:**
> "Any dotted name (i.e., attribute access) is to be interpreted as a value pattern." This precludes local/global variables from acting as constants.
>
> **Rejected Alternatives:**
> - Case sensitivity convention: No precedent in core Python
> - Leading dot notation (`.CONSTANT`): Insufficient visual marking
> - Global variable treatment: Would create unintended side effects when module variables change
>
> "The current proposal therefore leaves the discussion and possible introduction of such a 'constant' marker for a future PEP."

### [PEP635-CLASS-01] Class patterns: __match_args__ and isinstance
- **Source:** PEP 635, Rationale / Class Patterns
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "Anecdotal evidence revealed that `isinstance()` is one of the most often used functions in Python in terms of static occurrences in programs."
>
> "In a way, `__match_args__` is similar to the declaration of formal parameters, which allows calling functions with positional arguments rather than naming all the parameters."
>
> **Mirroring Construction Syntax:**
> "The syntax of class patterns is based on the idea that de-construction mirrors the syntax of construction."

### [PEP635-MAPPING-01] Mapping patterns: structural subtyping behavior
- **Source:** PEP 635, Rationale / Mapping Patterns
- **URL:** https://peps.python.org/pep-0635/
- **Altitude:** rationale
- **Excerpt:**

> "Dictionaries...have natural structural sub-typing behavior, i.e., passing a dictionary with extra keys somewhere will likely just work. Should it be necessary to impose an upper bound on the mapping and ensure that no additional keys are present, then the usual double-star-pattern `**rest` can be used."

---

## From Document 3: PEP 636 (tutorial)

### [PEP636-TUT-01] Tutorial examples across pattern kinds
- **Source:** PEP 636, Tutorial
- **URL:** https://peps.python.org/pep-0636/
- **Altitude:** tutorial / user-facing docs
- **Excerpt:**

> Tutorial Examples include sequence patterns, multiple patterns, specific values, unpacking, or-patterns, as-patterns, guards, object matching, positional attributes, constants/enums, and mapping patterns.
>
> "The match statement will check patterns from top to bottom. If the pattern doesn't match the subject, the next pattern will be tried. However, once the _first_ matching pattern is found, the body of that case is executed, and all further cases are ignored."
>
> Or-pattern warning: "An important restriction when writing or patterns is that all alternatives should bind the same variables."
>
> As-pattern: "The as-pattern matches whatever pattern is on its left-hand side, but also binds the value to a name."
>
> Guards: "The guard is not part of the pattern, it's part of the case. **It's only checked if the pattern matches, and after all the pattern variables have been bound.**"
>
> Object matching: "A pattern like `Click(position=(x, y))` only matches if the type of the event is a subclass of the `Click` class... A pattern like `KeyPress()`, with no arguments will match any object which is an instance of the `KeyPress` class."

### [PEP636-CONSTANTS-01] Dotted-name warning at user-facing altitude
- **Source:** PEP 636, Tutorial / Matching Against Constants and Enums
- **URL:** https://peps.python.org/pep-0636/
- **Altitude:** tutorial
- **Excerpt:**

> "This will work with any dotted name (like `math.pi`). However an unqualified name (i.e. a bare name with no dots) will be always interpreted as a capture pattern, **so avoid that ambiguity by always using qualified constants in patterns**."

### [PEP636-MAPPING-01] Mapping pattern extra keys ignored
- **Source:** PEP 636, Tutorial / Mapping Patterns
- **URL:** https://peps.python.org/pep-0636/
- **Altitude:** tutorial
- **Excerpt:**

> "The keys in your mapping pattern need to be literals, but the values can be any pattern... You can use `**rest` within a mapping pattern to capture additional keys in the subject... if you omit this, extra keys in the subject will be ignored while matching."

### [PEP636-SUMMARY-01] Tutorial key-features summary
- **Source:** PEP 636, Key Features Summary
- **URL:** https://peps.python.org/pep-0636/
- **Altitude:** tutorial
- **Excerpt:**

> - "Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. An important exception is that they don't match iterators or strings."
> - "Most literals are compared by equality, however the singletons `True`, `False` and `None` are compared by identity."
> - Named constants "must be dotted names to prevent them from being interpreted as capture variable."

---

## From Document 4: Python 3.10 What's New

### [WHATSNEW-OPENING-01] Pattern matching introduced via switch comparison
- **Source:** Python 3.10 What's New, Structural Pattern Matching section
- **URL:** https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
- **Altitude:** changelog / release residue
- **Excerpt:**

> Structural pattern matching has been added in the form of a *match statement* and *case statements* of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data.
>
> **## Declarative approach**
>
> Readers may be aware of pattern matching through the simple example of matching a subject (data object) to a literal (pattern) with the **switch statement found in C, Java or JavaScript** (and many other languages). Often the switch statement is used for comparison of an object/expression with case statements containing literals.
>
> More powerful examples of pattern matching can be found in languages such as Scala and Elixir. With structural pattern matching, the approach is "declarative" and explicitly states the conditions (the patterns) for data to match.

### [WHATSNEW-GUARD-01] Guards: value capture happens before guard
- **Source:** Python 3.10 What's New, Guards subsection
- **URL:** https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
- **Altitude:** changelog
- **Excerpt:**

> We can add an `if` clause to a pattern, known as a "guard". If the guard is false, `match` goes on to try the next case block. **Note that value capture happens before the guard is evaluated:**
>
> ```python
> match point:
>     case Point(x, y) if x == y:
>         print(f"The point is located on the diagonal Y=X at {x}.")
>     case Point(x, y):
>         print(f"Point is not on the diagonal.")
> ```

### [WHATSNEW-OTHER-01] Other key features (sequence/mapping/literal/named-constants)
- **Source:** Python 3.10 What's New, Other Key Features
- **URL:** https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
- **Altitude:** changelog
- **Excerpt:**

> - Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. Technically, the subject must be a sequence. Therefore, an important exception is that patterns don't match iterators. Also, to prevent a common mistake, sequence patterns don't match strings.
> - Mapping patterns: `{"bandwidth": b, "latency": l}` captures the `"bandwidth"` and `"latency"` values from a dict. **Unlike sequence patterns, extra keys are ignored.**
> - Most literals are compared by equality. However, the singletons `True`, `False` and `None` are compared by identity.
> - Named constants may be used in patterns. **These named constants must be dotted names to prevent the constant from being interpreted as a capture variable.**

---

## From Document 5: Python Language Reference (match statement)

### [LANGREF-OVERVIEW-01] Match overview and execution model
- **Source:** Python Language Reference § 8.6.1 Overview
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> 1. The subject expression `subject_expr` is evaluated and a resulting subject value obtained.
> 2. Each pattern in a `case_block` is attempted to match with the subject value. **Name bindings made during a successful pattern match outlive the executed block and can be used after the match statement**.
>
>    Note: During failed pattern matches, **some subpatterns may succeed**. Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match. **The exact behavior is dependent on implementation and may vary. This is an intentional decision made to allow different implementations to add optimizations.**
>
> 3. If the pattern succeeds, the corresponding guard (if present) is evaluated.
>
> Note: Users should generally **never rely on a pattern being evaluated**. Depending on implementation, the interpreter may cache values or use other optimizations which skip repeated evaluations.

### [LANGREF-GUARDS-01] Guards may have side effects
- **Source:** Python Language Reference § 8.6.2 Guards
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> A `guard` (which is part of the `case`) must succeed for code inside the `case` block to execute. It takes the form: `if` followed by an expression.
>
> The logical flow of a `case` block with a `guard` follows:
>
> 1. Check that the pattern in the `case` block succeeded. If the pattern failed, the `guard` is not evaluated and the next `case` block is checked.
> 2. If the pattern succeeded, evaluate the `guard`.
>    - If the `guard` condition evaluates as true, the case block is selected.
>    - If the `guard` condition evaluates as false, the case block is not selected.
>    - If the `guard` raises an exception during evaluation, the exception bubbles up.
>
> **Guards are allowed to have side effects as they are expressions. Guard evaluation must proceed from the first to the last case block, one at a time, skipping case blocks whose pattern(s) don't all succeed. (I.e., guard evaluation must happen in order.) Guard evaluation must stop once a case block is selected.**

### [LANGREF-CAPTURE-01] Capture pattern grammar
- **Source:** Python Language Reference § 8.6.4.4 Capture Patterns
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> ```
> capture_pattern: !'_' NAME
> ```
>
> A single underscore `_` is not a capture pattern (this is what `!'_'` expresses). It is instead treated as a `wildcard_pattern`.
>
> In a given pattern, a given name can only be bound once.
>
> Capture patterns always succeed. The binding follows scoping rules established by the assignment expression operator in PEP 572.

### [LANGREF-VALUE-01] Value pattern grammar
- **Source:** Python Language Reference § 8.6.4.6 Value Patterns
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> ```
> value_pattern: attr
> attr:          name_or_attr "." NAME
> name_or_attr:  attr | NAME
> ```
>
> The dotted name in the pattern is looked up using standard Python name resolution rules. The pattern succeeds if the value found compares equal to the subject value (using the `==` equality operator).
>
> In simple terms `NAME1.NAME2` will succeed only if `<subject> == NAME1.NAME2`.
>
> Note: If the same value occurs multiple times in the same match statement, **the interpreter may cache the first value found and reuse it** rather than repeat the same lookup. This cache is strictly tied to a given execution of a given match statement.

### [LANGREF-SEQUENCE-01] Sequence pattern: not strings/bytes/bytearray
- **Source:** Python Language Reference § 8.6.4.8 Sequence Patterns
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> The following is the logical flow for matching a sequence pattern against a subject value:
>
> 1. If the subject value is not a sequence, the sequence pattern fails.
> 2. **If the subject value is an instance of `str`, `bytes` or `bytearray` the sequence pattern fails.**

### [LANGREF-CLASS-01] Class pattern: built-in carve-out
- **Source:** Python Language Reference § 8.6.4.10 Class Patterns
- **URL:** https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- **Altitude:** normative reference
- **Excerpt:**

> Logical flow:
> 1. If `name_or_attr` is not an instance of the builtin `type`, raise `TypeError`.
> 2. If the subject value is not an instance of `name_or_attr` (tested via `isinstance()`), the class pattern fails.
> 3. (positional + keyword arg processing)
>
> **For the following built-in types the handling of positional subpatterns is different:**
>
> - `bool`, `bytearray`, `bytes`, `dict`, `float`, `frozenset`, `int`, `list`, `set`, `str`, `tuple`
>
> **These classes accept a single positional argument, and the pattern there is matched against the whole object rather than an attribute.** For example `int(0|1)` matches the value `0`, but not the value `0.0`.

---

## From Document 6: CPython tracking issue #86294 (selected comments)

### [CPYTHON-TRACK-01] Implementation scope statement
- **Source:** GitHub issue python/cpython#86294 (Brandt Bucher, contributor)
- **URL:** https://github.com/python/cpython/issues/86294
- **Altitude:** implementation tracking
- **Excerpt:**

> PEP-634 has not yet been accepted, but we'd like to hit the ground running and get this into alphas as soon as it (hopefully) is.
>
> Several people have volunteered to review the implementation, since it's so huge. Other reviews are very welcome, if anybody has a bit of time to pitch in. This touches tons of stuff: the parser, the compiler, the VM, the builtins, the stdlib, the tests... I'd like as many eyeballs as possible!

### [CPYTHON-TRACK-02] Docs derivation note
- **Source:** GitHub issue python/cpython#86294 (Brandt Bucher, contributor)
- **URL:** https://github.com/python/cpython/issues/86294
- **Altitude:** implementation tracking
- **Excerpt:**

> A lot of work has gone into writing these PEPs...  we should see how much we can easily convert into actual docs. It seems to me:
>
> - Parts of PEP-634 and PEP-635 can be worked into the language reference.
> - Guido's overview (the appendix of PEP-636) can probably just be dropped verbatim into the What's New for 3.10.

---

## From Document 7: CPython implementation PR #22917 (selected comments)

### [CPYTHON-PR-01] Buildbot failures dismissed as cross-branch flakiness
- **Source:** GitHub PR python/cpython#22917 (Brandt Bucher, contributor)
- **URL:** https://github.com/python/cpython/pull/22917
- **Altitude:** implementation decision
- **Excerpt:**

> So I see three categories of buildbot failures:
>
> - Memory leaks in `test_io` (all Refleak jobs).
> - Undefined references to `_Py_Mangle` and `PyAST_CompileObject` during LTO (all Fedora Stable LTO jobs).
> - Segfaults in `testlib2to3` (PPC64LE RHEL7 LTO, s390x Fedora LTO PR, s390x RHEL8 LTO + PGO).
>
> I've verified that all of these same failures occur on the 3.x buildbots, so I think they can be safely ignored here.

---

## From Document 8: PEP 653 (post-acceptance precise-semantics PEP)

### [PEP653-MOTIVATION-01] Direct critique of PEP 634's undefined behavior
- **Source:** PEP 653, Motivation
- **URL:** https://peps.python.org/pep-0653/
- **Altitude:** follow-up PEP / re-specification
- **Excerpt:**

> "**PEP 634 explicitly includes a section on undefined behavior. Large amounts of undefined behavior may be acceptable in a language like C, but in Python it should be kept to a minimum. Pattern matching in Python can be defined more precisely without losing expressiveness or performance.**"

### [PEP653-CONTROL-01] Critique of PEP 634's class/container handling
- **Source:** PEP 653, Motivation / Improved Control
- **URL:** https://peps.python.org/pep-0653/
- **Altitude:** follow-up PEP / re-specification
- **Excerpt:**

> PEP 634 "privileges some builtin classes with a special form of matching, the 'self' match" and "delegates the decision over whether a class is a sequence or mapping to `collections.abc`."

### [PEP653-ROBUSTNESS-01] Critique of PEP 634's attribute-access semantics
- **Source:** PEP 653, Motivation / Robustness
- **URL:** https://peps.python.org/pep-0653/
- **Altitude:** follow-up PEP / re-specification
- **Excerpt:**

> "with this PEP, access to attributes during pattern matching becomes well defined and deterministic" — addressing concerns about "object-relational mappers" and "unintended consequences should attribute access have side-effects."

### [PEP653-DIFF-01] Key differences from PEP 634
- **Source:** PEP 653, Key Differences from PEP 634
- **URL:** https://peps.python.org/pep-0653/
- **Altitude:** follow-up PEP / re-specification
- **Excerpt:**

> - Uses `cls.__match_container__` instead of `issubclass()` checks against abstract base classes
> - Requires `__match_args__` to be a **tuple** rather than any sequence
> - Allows `__match_class__ = 0` to opt out of deconstruction
> - Provides explicit, deterministic semantics for all matching scenarios

---

# Required receipt format

Return a single markdown document with the following structure. Do not depart from this structure.

```markdown
# Blind-Auditor Receipt — [your auditor identifier]

**Audited:** [date]
**Time spent:** [approximate]
**Mechanical aids used:** [list any: Python interpreter, mypy, etc., or "none"]

## Per-claim verdicts

### Claim A
- **Verdict:** [single label or multi-class]
- **Citations:** [list excerpt IDs, e.g. [PEP635-MOTIVATION-01], [WHATSNEW-OPENING-01]]
- **Reasoning:** [2–6 sentences explaining why this verdict, not another]
- **Uncertainty:** [low / medium / high; note what would change the verdict]
- **Revised during audit?:** [yes/no; if yes, briefly: from what to what, why]

### Claim B
[same structure]

### Claim C
[same structure]

### Claim D
[same structure]

### Claim E
[same structure]

## Cross-cutting observations

- **Where operator judgment is doing hidden work:** [enumerate]
- **Where mechanical aid would have helped:** [enumerate]
- **Was the verdict palette sufficient?:** [yes / no / explain]
- **Any label-failures:** [explain if any]

## Overall

- **Method discrimination assessment:** [retains discrimination / degrades gracefully / collapses into vibes — pick one and briefly justify]
- **Caveats and limitations:** [list]
- **Notes the packet preparer should know:** [optional]
```

Return only this receipt.

## Audit instructions (one paragraph)

Read the corpus excerpts fully before forming any verdict. For each claim, scan all excerpts for relevant material; identify which altitude each piece of relevant material occupies; check whether the claim's framing is consistent with all altitudes or whether it collides with one altitude while matching another. Cite by excerpt ID. If a claim seems to fit two labels, state both with separate citations. If a claim seems to fit no label, mark it LABEL-FAILURE rather than inventing a new label. Verdict stability is itself an audit signal: if your verdict on a claim changes between first pass and second pass, record the change and the reason.

## Notes (for the auditor's information)

- Documents 1, 2, 3, and 8 are PEP texts authored by named individuals.
- Document 4 (What's New) is authored by the Python documentation team.
- Document 5 (Language Reference) is the post-implementation normative anchor; it may diverge from the original PEP.
- Documents 6 and 7 (CPython issue and PR) are implementation-altitude artifacts.
- Document 8 (PEP 653) is a follow-up PEP that exists, regardless of its formal acceptance status.

The excerpts inlined above are a subset selected to support audit of the five claims. If you find an excerpt insufficient or want to verify a citation, the URLs are listed in each excerpt header and the frozen sources are bundled in the companion zip. Do not pull material outside what is bundled here; if you do, mark it as out-of-bundle and treat that citation as secondary.

---

**End of bundle. Audit and return receipt. Do not request expected verdicts.**
