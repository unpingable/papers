# Accountable Mutation as an OS-Layer Primitive

**Status:** working note / recognition frame. 2026-05-06.
**Scope:** conceptual exploration, not implementation commitment.
**Stance:** prewarmed branch, not forcing case.

---

## Kernel thought

Unix made execution composable.
systemd made machine obligations explicit.
Kubernetes made desired state recurrent.

The topology age lacks a shared primitive for **accountable mutation**: who/what may change what, under what authority, with what scope, what consequence, what receipt, and what recovery path.

The OS asks: *can this process write?*

The missing layer asks: *what kind of state is this, who is changing it, under what role, with what consequence, what recovery path, and what receipt survives?*

## The dangerous-but-interesting version

This is potentially the **OS-substrate instantiation of the admissibility shape**, not merely adjacent to admissibility. The framing matters because "adjacent" is too weak: the mutation questions below map approximately onto the admissibility-family six boundaries plus the Corrective-monotonicity / non-laundering recovery vocabulary plus zombie-obligation-as-stale-basis.

Keeper lines:

> **If accountable mutation is the missing OS primitive, zombie obligation is one of its named failure modes.**
>
> **The operator is currently the missing primitive.**

A zombie obligation is what you see when a mutation's basis decayed but the mutation kept firing. The authority graph is dead. The system has no shared primitive to notice the contradiction. That is not merely an ops/book primitive — it is an accountable-mutation failure mode visible from a different angle.

The second keeper sharpens the first. A graybeard with `grep`, `journalctl`, `systemctl`, `strace`, `auditd`, shell scripts and resentment can reconstruct almost anything. That does not mean the OS has the primitive. It means the operator is acting *as* the missing primitive, holding the dependency graph in their head and adjudicating basis validity by hand.

## Non-claim

This is **not**:

- a claim that agent_gov / Governor doctrine owns this layer.
- a proposal to build a workbench, OS, supervisor, or kernel module.
- a replacement for Unix, Plan 9, systemd, Kubernetes, capability OSes, or security models.
- a P28 candidate.

It is a **recognition frame** for a missing layer between execution, service obligation, and consequence-bearing state mutation. The note exists so that the next time the constellation points at this floor from a new angle, the recognition does not have to be rediscovered cold.

## Mutation questions

For any meaningful state change:

- What state-kind is being touched?
- Who/what is acting?
- Who owns or custodies the state?
- What authority/basis permits the action?
- What scope boundary is crossed?
- What consequence is bound?
- Is the basis current or stale?
- Is the mutation reversible?
- What depends on the new state?
- What receipt survives?
- What recovery path exists?

## Existing partial ancestors

### What each ancestor asks

| Ancestor | The question it asks |
| --- | --- |
| Capability OSes (KeyKOS, EROS) | *Do you hold authority?* |
| Provenance systems (PASS, Hi-Fi, CamFlow) | *How did this state come to be?* |
| OS transactions (TxOS) | *Can this mutation commit atomically or roll back?* |
| Information-flow OSes (HiStar, Flume, DStar) | *What may influence what?* |
| Standing-obligation managers (systemd, runit) | *Is this obligation still declared?* |
| Reconciliation engines (Kubernetes, operators) | *Does the desired state still hold?* |
| History / reproducibility (Git, Nix) | *What was the prior state, and how was it derived?* |
| Audit / eBPF | *What just happened?* |

Accountable mutation asks the question none of them ask:

> **Is this mutation still justified?**

That is the floor. Not access. Not trace. Not rollback. Not declared-state convergence. **Basis validity.**

### Detailed inventory

These addressed pieces but did not synthesize the bundle:

- **Capability OSes** (KeyKOS, EROS): authority-as-unforgeable-token, persistence, checkpoint/restart. Mostly access, not full mutation accounting.
- **Multics**: protection-as-architecture, rings, controlled sharing. Protection without mutation receipt vocabulary.
- **Provenance-aware storage** (PASS, Hi-Fi, CamFlow): retrospective traceability of derivation. Not prospective admissibility.
- **OS transactions** (TxOS): mutation as commit/rollback. Consistency without governance.
- **Information-flow OSes** (HiStar, Flume, DStar): explicit information flow, taint, declassification. Information-security framing, not operational mutation.
- **Standing-obligation managers** (systemd, runit, launchd): named machine obligations. Service ontology, not mutation ontology.
- **Reconciliation engines** (Kubernetes, operators): recurrent desired-state. Obligation with teeth, no admissibility on transitions (P27 territory).
- **History / reproducibility** (Git, Nix): narrow artifact classes. Not workspace-wide mutation memory.
- **Audit / eBPF**: observation surfaces. Not policy on consequence.

The corpses are everywhere; the body is not assembled.

## Missing synthesis

Mutation as **typed, scoped, time-bounded, consequence-bearing**, with receipt and recovery as first-class outputs — and authority/basis treated as decaying, not timeless.

## Falsifier

This recognition is **empty** if its specific synthesis reduces cleanly to "capability + provenance + transactions + DIFC + receipts repackaged with new vocabulary."

Bite test: does it distinguish failure modes the partial ancestors miss — *natively*, not through operator archaeology?

Candidate distinguishing failure modes (held, not promoted):

- **Stale-basis zombie obligation.** Mutation continues firing after the authority graph that justified it has decayed.
- **Cross-tool mutation laundering.** One role's mutation is reattributed to another via shared substrate or ambient permission inheritance.
- **Receipt-unsoundness.** Recovery path exists in code but cannot be evidenced after the fact (controller-correct, operator-unsound — see P27).
- **Decay-blindness.** The OS has no native vocabulary for "this authorization was valid when issued but is not now."
- **Recurrent mutation after justification lapse.** Reconciliation engines keep trying to apply a spec whose authoring basis has expired; convergence does not check basis currency.

**Operator archaeology does not count as native support.** A competent operator with `journalctl`, `systemctl`, `auditd`, `strace`, eBPF probes, shell scripts and resentment can reconstruct most of these symptoms after the fact. That does not mean the OS has the primitive. It means the operator is *acting as* the missing primitive — holding the dependency graph in their head, manually adjudicating basis validity, paying the cost the OS refuses to pay. The bite test is whether the system itself can natively name, question, and revoke the basis of a mutation, not whether a sufficiently determined human can do it from logs.

If the candidate failure modes reduce cleanly to existing partial-ancestor vocabularies *under that constraint*, the recognition has not earned its keep and the note retires.

## Forcing case (not yet)

Per three-term vocabulary (forcing case / default future work / prewarmed branch): this is **prewarmed branch**. Zombie obligation is the closest visible instance; the recognition holds without a forcing case but should be revisited if one sharpens.

Do not open this drawer absent:

- a concrete laundering path that no existing OS primitive can name, or
- a desktop / cloud-agent / AI-assistant failure mode that the admissibility-family vocabulary handles cleanly while existing OS vocabularies miss it, or
- a second forcing-case-shaped instance from another constellation member.

## Prototype direction (if revisited — not now)

Do **not** start in kernel.
Do **not** start in FreeBSD.

Start workspace-scoped on Linux, where the failure evidence lives:

- Manifest declares state-kinds (durable artifact / cache / authority-bearing config / credential / replica / receipt / publication / disposable runtime).
- Launcher records tool/actor role.
- fanotify or eBPF watcher records before/after hashes.
- Receipts append-only.
- btrfs/ZFS snapshots for high-consequence mutation classes.
- Optional policy layer flags out-of-scope mutation.
- Cockpit answers: what changed, why, by whom, recoverable how.

FreeBSD is the cleaner *conceptual* lift (ZFS, jails, Capsicum, MAC framework, base-system coherence) but the *wrong substrate first*. The accountable-mutation thesis is about the topology age's actual mutation failures: browsers, systemd unit explosion, cgroup mismanagement, Wayland fragility, Electron forests, package managers, cloud agents, AI tools mutating files on inferred intent. Those bodies are buried in Linux. Substrate clarity follows from problem reality, not the other way around.

## User-facing vocabulary (if revisited — not now)

If accountable mutation ever surfaces to the operator, it should not be bureaucracy. It should be ordinary workbench questions answered in concrete, boring vocabulary:

| Term | What it names |
| --- | --- |
| **standing** | who/what may act |
| **basis** | why the action is currently allowed |
| **lease** | how long the basis remains valid |
| **scope** | what state boundary the action may cross |
| **receipt** | what durable record survives |
| **revoke** | stop future mutation under this basis |
| **recover** | undo or reconstruct previous state |
| **quarantine** | preserve evidence, block propagation |

The shape of the user-facing surface is more `workbench` than `mutationctl-as-lifestyle-brand`:

```sh
workbench status
workbench changes --since yesterday
workbench why path/to/file
workbench standing
workbench revoke <actor-or-lease>
workbench receipts --state config
workbench recover <receipt-id>
```

The cockpit is not a metric dashboard. It is a **standing-and-recovery surface** for the continuity layer. The earlier memory-pressure widget is a degenerate case: widget = witness, user = authorizer, restart = mutation, oomd = automated mutator, app.slice rule = standing policy, PSI threshold = evidence trigger. The gap is that the receipt and recovery side is currently scattered or absent — which is why the operator ends up improvising the missing primitive.

## Relation to existing constellation

This sits potentially **underneath** rather than adjacent to:

- Admissibility family (six non-collapsible boundaries between signal and action).
- Authority + StateTransition + Derivation + Execution + Corrective Lean kernel under `LeanProofs/Admissibility/`.
- Governor doctrine (agent_gov authority-boundary instantiation).
- Continuity doctrine (~/git/continuity reliance-boundary instantiation).
- Zombie obligation (named failure mode of stale-basis mutation; commit a68c545, 2026-05-06).
- P25 Epistemic Border Control (substitution under observability asymmetry).
- P27 Obligation-Unsound Reconciliation (transition admissibility, controller-correct/operator-unsound).
- `working/admissible-recovery-semantics.md` (corrective monotonicity / non-laundering recovery).

The OS-substrate framing would mean: these doctrines are not parallel domain-specific instantiations of unrelated primitives. They are surface manifestations of an accountable-mutation primitive that has not yet been canonized at the OS layer.

This claim is **not made**. It is recorded as the dangerous-but-interesting version of the recognition, so that if the constellation keeps pointing at it, the connection is already named rather than rediscovered as if novel.

## Provenance

- Multi-model conversation 2026-05-06: chatty riff on "Unix stopped one abstraction level too early" plus Plan 9 / capability-OS / provenance / TxOS / DIFC research-island survey.
- claude-code corrections folded in: Linux-first (not FreeBSD-first), constellation-pointer sharpening (substrate, not adjacent), falsifier requirement, prewarmed-branch framing.
- Filed as working note, recognize-don't-build, per name-early-ratify-lazily discipline. Not a paper, not a project, not a P28.
