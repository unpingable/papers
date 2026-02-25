# Who Governs the Compiler?

*Receipts, Authority, and the Agentic Software Supply Chain*

**James Beck** — draft — 2026

---

## Abstract

Software can now write software. This is not a capability gap; it is a governance gap. The build pipeline has always been a policy-bearing system — encoding assumptions about authority, scope, provenance, and accountability into every artifact it produces. When the pipeline's participants were human, informal trust and social norms filled the governance layer. When the participants are agents, that layer collapses. The response will either be receipted governance — typed, versioned, auditable decision trails — or it will be extractive governance-as-a-service, where the policy layer gets enclosed by whoever arrives first with a working product. This paper argues for the first option and describes what it requires.

---

## 1. The Informal Trust Model Is Breaking

Open source software has always run on informal trust. Not because the community was naive, but because the attack surface was constrained by human labor. A malicious or incompetent contributor could submit a bad pull request, but submitting pull requests took time, required some engagement with the project, and produced a trail that other humans could inspect. The cost of attack was bounded by human bandwidth.

Agent systems break this constraint. The cost of generating a plausible pull request is now approximately zero. The cost of generating a thousand plausible pull requests is approximately the same. An agent can read a codebase, identify contribution opportunities, generate syntactically correct and superficially reasonable changes, write a compelling commit message, and submit — at scale, continuously, without sleeping.

The changes do not have to be malicious to be damaging. Most of them will just be wrong in subtle ways, or right in ways that create technical debt, or correct but unnecessary, or correct but inconsistent with project direction. The problem is not the adversarial case. The problem is the ambient noise floor rising until human maintainers cannot distinguish signal from plausible-sounding garbage.

This is already happening. The response so far has been ad hoc: maintainers adding bot-detection heuristics, projects going invite-only, foundations exploring contribution gates. These are reasonable immediate responses to an immediate problem. They are not governance. They are duct tape on a structural gap.

---

## 2. The Question Nobody Is Asking

The conversation about agentic software development is almost entirely focused on outputs. Can the agent write correct code? Can it pass the tests? Can it follow the style guide? Does it hallucinate imports?

These are real questions. They are also the wrong level of analysis.

The question is not whether the output is correct. The question is:

- Who proposed this change?
- Under what authority?
- With what scope?
- Using which tools?
- Against what policy?
- With what review path?
- What happens when it breaks?

These are governance questions. They are the questions a build system implicitly answers when its participants are humans operating under shared social norms. When the participants are agents, the implicit answers disappear and the questions become urgent.

A signed artifact tells you the binary was produced by a specific key. It does not tell you whether the decision to produce that binary was within scope, authorized by the right policy, reviewed by a human with appropriate standing, or recoverable if it turns out to be wrong.

You can sign a binary and still have no idea how the decision happened.

---

## 3. The Build Pipeline Has Always Been a Policy System

This is not a new problem introduced by agents. Agents make it visible.

Every build pipeline encodes policy:

- Which branches can trigger production deploys?
- Who can approve a merge to main?
- What test coverage is required before artifact promotion?
- Which dependency versions are permitted?
- What happens when a security scan fails?
- Who can override a failed gate?

These are not technical decisions. They are governance decisions expressed in technical form. The pipeline is a policy engine. It has always been a policy engine. The humans operating it just provided enough ambient context that the policy layer felt natural and self-evident rather than explicit and contestable.

Agents remove that ambient context. When an agent triggers a pipeline action, the question "is this within policy?" does not have an obvious answer derivable from social norms. It requires an explicit policy, an explicit scope, and an explicit authorization chain.

The engineering community has solved adjacent versions of this problem before. Supply chain security gave us signed artifacts and provenance attestations. Infrastructure-as-code gave us version-controlled, reviewable policy. GitOps gave us auditable deployment history. The missing piece is the decision layer — not what was built, but who decided to build it, under what authority, and with what accountability.

---

## 4. What Receipted Governance Looks Like

The governor pattern applied to software development is not a new category of tooling. It is the application of a principle that engineers already accept in adjacent domains: **consequential decisions should leave typed, versioned, auditable trails.**

A governed agentic build pipeline would capture, at minimum:

**Proposal receipt.** What change was proposed, by whom or what, at what time, against what version of the codebase, using which tools, with what stated rationale. Not just the diff — the decision context that produced the diff.

**Authority receipt.** What policy authorized this agent to propose this class of change in this repository at this time. Scope matters: an agent authorized to fix typos in documentation is not authorized to refactor the authentication module, even if it believes the refactor would be an improvement.

**Review receipt.** Who reviewed this proposal, with what standing, under which review policy, at what confidence. If the review was automated, which checks passed and which were waived, under what exception policy.

**Merge receipt.** Who merged this change, with what authority, under which policy version, at what time. If merged automatically, which conditions were satisfied and which policy authorized automatic merge.

**Policy receipt.** When the policies governing any of the above change — who can propose what, what requires human review, what triggers automatic rejection — that change is itself a receipted event. Policy version is explicit. Policy drift is visible.

**Rollback receipt.** When a change is reverted, the reversion carries provenance: what triggered it, who authorized it, what the reversion restores.

This is not a radical architecture. It is a modest extension of practices the industry already endorses for security and compliance: signed commits, artifact attestations, policy-as-code, audit logs. The extension is to treat the *decision layer* — the authority and scope under which agents act — as a first-class object in the governance model rather than an implicit assumption.

---

## 5. The Extractive Path

If receipted governance is straightforward in principle, why does it not already exist?

Because building it is slower than building the alternative, and the alternative solves an immediate, painful, expensive problem.

The immediate problem is this: maintainers are being flooded. Agent-generated PRs, AI-assisted issue spam, plausible garbage at scale. The pain is real, the burnout is real, and whoever ships relief first will capture the market.

The relief that will ship first is a trust scoring and filtering layer: an opaque model that evaluates contribution quality, assigns reputation scores, gates access, and filters noise. It will work. It will reduce the maintainer burden. It will be adopted broadly because maintainers are drowning and this is the life preserver.

Then the constitutional layer will appear.

Six months or a year after adoption, the policy surface that was implicit in the filtering model will start to matter. Who defines what counts as "likely AI spam"? Who sets the trust score thresholds? Who decides which contributor classes get auto-throttled? Who handles appeals when the filter produces false positives? What is the recourse path when a legitimate contributor's reputation is incorrectly scored?

The answers to these questions will live inside the vendor's model. They will not be inspectable. They will not be contestable in any meaningful sense. They will change when the vendor updates the model, without notice, without versioning, without the projects that depend on them having any input into the change.

This is not a hypothetical. It is the standard enclosure pattern, applied to a new surface: solve real pain, build real dependency, monetize the policy layer once switching costs are high enough. The Hashicorp license change and the Red Hat source code restrictions are recent examples of the same pattern in adjacent domains — not malicious at the point of adoption, consequential once dependency was entrenched.

The submarine governance model: the extraction is not the pitch. It is the upgrade path.

---

## 6. The Non-Extractive Path

The non-extractive path exists. It is slower. It does not offer immediate relief to drowning maintainers. It requires building governance before the crisis rather than enclosing it after.

It looks like this:

**Signed provenance for agent actions.** Every agent action in a build pipeline carries a cryptographic attestation of its origin: which agent, which model version, which tool configuration, at what time. This is the receipt plumbing layer. It is necessary but not sufficient.

**Explicit scope declarations.** Agents operate under declared scope: which repositories, which file classes, which action types, within which time windows. Scope is explicit, versioned, and attached to every action the agent takes. Actions outside declared scope are rejected, not filtered by opaque heuristics.

**Project-local trust tiers.** Contributor trust is maintained by the project, not by a third-party reputation graph. Trust tiers are explicit policy, not scores. Tier changes are versioned events with human authorization. This keeps the authority over contributor standing inside the project's governance rather than outsourced to a platform.

**Public policy documents for triage and merge criteria.** The rules governing what gets reviewed, what gets auto-rejected, and what triggers human escalation are written down, versioned, and publicly visible. Policy changes are pull requests. Policy drift is trackable.

**Appeal paths with human override.** Every automated rejection has an appeal path that routes to a human with actual authority to reverse the decision. The appeal path is not a support ticket queue. It is a governance surface with documented response commitments.

**Reproducible CI snapshots.** The build environment that evaluated a change is reproducible and documented. "It passed CI" means something specific and verifiable, not "it passed whatever CI was running at that moment."

None of these are exotic. Several are already standard practice in security-conscious organizations. The gap is in treating them as a unified governance layer rather than a collection of independent tooling choices.

---

## 7. The Schema Fight

The political economy of this space will be determined by whoever defines the schema.

What counts as "AI-generated"? What counts as "authorized agent action"? What fields are required in a contribution provenance record? What constitutes a valid appeal? What is the canonical format for a scope declaration?

These questions sound like technical standards questions. They are constitutional questions. The answers determine what can be represented in the governance system, which determines what can be contested, which determines where power actually sits.

If a dominant vendor defines these schemas inside a proprietary system, the open source community will spend the next decade "standardizing" a proprietary ontology. The code will remain open. The governance will be enclosed.

If the schemas are developed in the open — by foundations, by working groups, by the same community processes that produced existing supply chain security standards — the governance layer remains contestable. Not perfect. Not captured by any single actor. Contestable.

The schema fight has not started yet in earnest. The agent spam problem is new enough that most projects are still in the duct-tape phase. The window for getting the governance layer right is open. It will not stay open indefinitely.

---

## 8. Procedural Truth vs. Procedural Plausibility

There is a useful distinction between two things agent systems can produce.

**Procedural plausibility** is output that looks correct: passes tests, matches style, references the right abstractions, produces no obvious errors. It is the output of a system optimized for surface correctness without accountability for the decision process that produced it.

**Procedural truth** is output that is correct and whose correctness is traceable: the decision to produce it was authorized, the scope was appropriate, the review was genuine, the policy was current, and the trail from decision to artifact is intact and auditable.

Most of what agent systems produce right now is procedural plausibility. This is not entirely the agents' fault. The infrastructure for procedural truth does not widely exist. There is no standard way to attach a typed scope declaration to an agent action, no standard format for a proposal receipt, no common expectation that merge decisions carry policy provenance.

Building that infrastructure is the work. It is less exciting than building agents that can write increasingly impressive code. It is more important.

Software that can write software is a capability. Software that can govern that process is infrastructure. The industry is very good at building capabilities before building the infrastructure they require. The technical debt from that pattern is usually manageable. The governance debt may not be.

---

## 9. Conclusion

The build pipeline is now an epistemic system. It takes inputs from agents whose authority, scope, and accountability are often unspecified. It produces artifacts whose decision provenance is often untraceable. It operates under policies that are often implicit, unversioned, and invisible to the projects that depend on them.

This is not a problem that better agents will solve. Better agents will produce more plausible output faster. The governance gap will widen.

The solution is not to make agents less capable. It is to make the systems that govern their actions more legible: typed scope declarations, proposal receipts, policy versioning, explicit authority chains, contestable appeal paths, and the schema standards that make all of the above interoperable.

The extractive path is faster. It solves the immediate pain. It will capture the market if the open path does not move.

The question is not whether governance comes to the agentic software supply chain. It is coming regardless. The question is who writes the constitution.

That fight has not started yet. It should.

---

## Notes

This paper is part of a series on receipted epistemic governance. The underlying architecture — the receipted factor graph, typed policy nodes, and governor constraints — is developed in *Receipt the Compiler* (Beck, 2026). The phenomenology of living under governed vs. ungoverned information systems is explored in *The Ground Stops Moving* (Beck, 2026).

The political economy of governance enclosure — who builds this, who pays for it, who captures it — is the next layer of analysis and is outside the scope of this paper. It is, however, the layer that determines whether the non-extractive path described in Section 6 ever ships at scale.

The Hashicorp and Red Hat examples referenced in Section 5 are illustrative of a general pattern, not accusations. Both companies made defensible business decisions under competitive pressure. The pattern is structural, not moral.
