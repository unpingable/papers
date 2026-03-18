# Paper 14 — Temporal Attack Surface — Convergence Spike

**Full title:** The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems
**Date:** 2026-01-13
**DOI:** 10.5281/zenodo.18236164

## Status: complete

## Claim Cluster
- SIEM alerting, CI/CD security gates, authentication flows, rate limiting, and human-in-the-loop approvals share a common control-theoretic failure structure rooted in temporal decoupling
- Race windows between attacker commitment and defender response constitute a distinct vulnerability class (the temporal attack surface)
- Mitigation strategies based on temporal coupling are more effective than configuration hardening for this class of vulnerability
- Defender-side instrumentation can measure temporal vulnerability independent of specific attack vectors

## Search Terms
- TOCTOU race condition security temporal
- SIEM detection delay attacker advantage
- CI/CD pipeline security gate bypass timing
- authentication flow race condition temporal
- temporal decoupling security vulnerability class
- detection-response gap security architecture
- rate limiting bypass timing attack
- security temporal coupling mitigation

## Expected Convergence Level
partial convergence likely
TOCTOU vulnerabilities are well-known in security. The generalization to a unified temporal attack surface across SIEM, CI/CD, auth, and rate limiting is more novel but likely has parallels in security architecture literature that discusses detection-response gaps.

---

## Hits

### STRONG CONVERGENCE (same problem space, overlapping framing)

**1. Schneier & Raghavan, "Agentic AI's OODA Loop Problem" (2025)**
- Authors: Bruce Schneier, Barath Raghavan
- Year: 2025
- Venue: IEEE Security & Privacy
- URL: https://www.schneier.com/blog/archives/2025/10/agentic-ais-ooda-loop-problem.html
- Match type: Strong parallel
- Claims touched: Temporal decoupling as structural vulnerability; race between observation and action; speed as vulnerability; integrity across observe-orient-decide-act cycle
- How close: Schneier/Raghavan argue that AI agents' OODA loops are structurally vulnerable because "adversaries aren't just metaphorically inside the loop; they're literally providing the observations and manipulating the output." They identify the same temporal asymmetry: "the faster the loop, the less time for verification—millisecond decisions result in millisecond compromises." Their framing is OODA-based rather than control-theoretic, and focused on AI agents rather than security systems generally, but the core insight—that temporal gaps between observation and action create structural (not configurational) vulnerabilities—converges strongly with Paper 14's thesis. They do NOT generalize to SIEM/CI-CD/auth/rate-limiting. They do NOT formalize commitment points, commitment polarity, or political budget.

**2. Temporal Analysis Framework for Intrusion Detection Systems (2025)**
- Authors: (multiple, see arXiv)
- Year: 2025 (November)
- Venue: arXiv:2511.03799
- URL: https://arxiv.org/abs/2511.03799
- Match type: Strong parallel (detection side)
- Claims touched: Temporal taxonomy for security; time-aware detection; mapping temporal approaches to MITRE ATT&CK
- How close: Proposes a five-category temporal taxonomy (Static Per-Flow, Static Contextual Snapshot, Intra-Flow Sequential, Inter-Flow Sequential, Temporal Window-Based Sequential) for IDS methods. Systematic review of 40+ studies. Maps temporal detection approaches to ATT&CK tactics. Identifies dataset bias toward late-stage attacks limiting early detection research. This converges with Paper 14's detection clock (W_j) analysis and the claim that temporal structure matters for security. However, it is purely about detection classification—does NOT frame the detection-decision-response chain as a race condition, does NOT model commitment points, does NOT cover CI/CD/auth/rate-limiting, and does NOT provide the unified inequality framework.

**3. CrowdStrike Global Threat Reports (2024-2026): Breakout Time Analysis**
- Authors: CrowdStrike Intelligence
- Year: 2024-2026
- Venue: Industry reports
- URLs: https://www.crowdstrike.com/en-us/global-threat-report/ ; https://www.kiteworks.com/cybersecurity-risk-management/crowdstrike-2026-threat-report-breakout/
- Match type: Strong empirical convergence
- Claims touched: Attacker speed vs. defender detection/response; race window as operational reality; T_commit < T_respond
- How close: CrowdStrike's breakout time metric is the closest industry operationalization of Paper 14's T_commit < T_respond race condition. Average breakout time dropped from 48 minutes (2024) to 29 minutes (2025), fastest at 27 seconds. One case showed data exfiltration within 4 minutes. 82% of detections malware-free (credential-based). CrowdStrike explicitly frames this as a race: "If your incident response process is measured in hours, you are already too late." This is strong empirical validation of the temporal attack surface concept, but CrowdStrike does NOT provide a formal framework, does NOT generalize across security domains, does NOT model commitment polarity or political budget.

### MODERATE CONVERGENCE (overlapping domain, partial framing overlap)

**4. Alert Fatigue in Security Operations Centres: Research Challenges and Opportunities (2025)**
- Authors: (multiple, see ACM)
- Year: 2025 (April)
- Venue: ACM Computing Surveys
- URL: https://dl.acm.org/doi/10.1145/3723158
- Match type: Moderate convergence (SOC domain)
- Claims touched: Human-in-the-loop as slowest/most vulnerable layer; alert fatigue as operational reality; political budget (κ_j) concept
- How close: Systematic survey documenting that 51% of SOC teams are overwhelmed by alert volume, 62% of alerts are ignored, accuracy drops 40% after extended shifts. Uses A2C framework (automation, augmentation, collaboration). This strongly validates Paper 14's κ_j (political budget) concept and the claim that humans are the most vulnerable temporal layer, though the survey frames it as a human-factors problem rather than a control-theoretic race condition.

**5. Alert Prioritisation in Security Operations Centres: A Systematic Survey (2025)**
- Authors: (multiple, see ACM)
- Year: 2025
- Venue: ACM Computing Surveys
- URL: https://dl.acm.org/doi/full/10.1145/3695462
- Match type: Moderate convergence (SOC domain)
- Claims touched: Detection delay; analyst overwhelm; W_j distribution
- How close: Companion survey on alert prioritization methods. Validates that SIEM temporal dynamics (detection delay, queue depth, analyst capacity) are recognized research problems. Does NOT frame as race condition or provide unified temporal framework.

**6. Ruohonen, "SoK: The Design Paradigm of Safe and Secure Defaults" (2024)**
- Authors: Jukka Ruohonen
- Year: 2024 (December, arXiv) / 2025 (journal)
- Venue: arXiv:2412.17329 / Journal of Information Security and Applications
- URL: https://arxiv.org/abs/2412.17329
- Match type: Moderate convergence (defaults/polarity)
- Claims touched: Commitment polarity (C_j); fail-open vs. fail-closed as design paradigm; zero trust as evolution of defaults
- How close: Systematic mapping study of safe/secure defaults paradigm spanning decades. Identifies "off by default" principle, overriding/fallback principles, and zero trust as expansions. This validates Paper 14's C_j (commitment polarity) concept as a recognized design concern, but Ruohonen treats defaults as static design choices rather than temporal race condition parameters. Does NOT connect defaults to temporal attack surface or detection-response gaps.

**7. Game Theory in Distributed Systems Security (2025)**
- Authors: (Purdue, multiple)
- Year: 2025
- Venue: Purdue DCSL working paper
- URL: https://engineering.purdue.edu/dcsl/wp-content/uploads/2025/02/Game_Theory_in_Distributed_Systems_Security_Foundations_Challenges_and_Future_Directions.pdf
- Match type: Moderate convergence (formalization)
- Claims touched: Security as attacker-defender race; dynamic/sequential game models; temporal evolution
- How close: Reviews game-theoretic models for distributed systems security. 68.5% of models use sequential-move games. Models temporal evolution of attacker-defender interactions. This converges with Paper 14's framing of security as a race, but uses game-theoretic rather than control-theoretic formalization. Does NOT model detection-decision-response as three clocks, does NOT formalize commitment polarity or political budget.

**8. Attacker-Defender Games Review (2024-2025)**
- Authors: (multiple, see PMC)
- Year: 2024-2025
- Venue: PMC / MDPI Games
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12366505/
- Match type: Moderate convergence
- Claims touched: Dynamic attacker-defender interactions; temporal dynamics in security
- How close: Comprehensive review of attacker-defender game models. Frames security as competitive resource allocation over time. Converges on the race framing but uses different formalism. Does NOT address the specific temporal decomposition (detection-decision-response clocks) or the five-domain generalization.

**9. MFA Fatigue / Prompt Bombing Literature (2024-2025)**
- Authors: Various (industry/practitioner)
- Year: 2024-2025
- Venue: Industry blogs, vendor documentation
- URLs: https://www.prophetsecurity.ai/blog/what-is-mfa-fatigue-attack-mfa-bombing-best-practices ; https://www.pingidentity.com/en/resources/blog/post/mfa-bombing-dismantled.html
- Match type: Moderate convergence (authentication domain)
- Claims touched: Human-in-the-loop as vulnerable temporal layer; timing exploitation of human approval; authentication race windows
- How close: MFA fatigue attacks are well-documented as exploiting human temporal vulnerability—"particularly effective when launched during off-hours, like overnight or on a weekend." This validates Paper 14's authentication case study and the claim that human approval is the slowest/most exploitable layer. However, literature treats this as a specific attack technique rather than an instance of a general temporal vulnerability class.

**10. "Rubber Stamp Risk: Why Human Oversight Can Become False Confidence" (2025)**
- Authors: CyberManiacs
- Year: 2025
- Venue: CyberManiacs blog
- URL: https://cybermaniacs.com/cm-blog/rubber-stamp-risk-why-human-oversight-can-become-false-confidence
- Match type: Moderate convergence (human-in-the-loop)
- Claims touched: Approval fatigue; κ_j exhaustion; human oversight as false safety
- How close: Argues that "oversight without role clarity, training, decision criteria or feedback becomes a rubber stamp—not a risk control." Cognitive fatigue and cultural pressure turn oversight into theater. Validates Paper 14's human-in-the-loop case study. Does NOT connect to temporal framework or formalize the failure mode.

### WEAK CONVERGENCE (related domain, different framing)

**11. OODA Loop in Cybersecurity (various, 2016-2025)**
- Authors: Various
- Venue: NIST, SecurityWeek, industry blogs
- URL: https://csrc.nist.gov/CSRC/media/Presentations/The-Cyber-OODA-Loop-How-Your-Attacker-Should-Help/images-media/day3_security-automation_930-1020.pdf
- Match type: Weak convergence (framework level)
- Claims touched: Observe-orient-decide-act as security cycle; speed advantage
- How close: OODA loop application to cybersecurity is established. Frames attacker-defender as competing loops. But OODA is a decision-making model, not a vulnerability model—it describes the cycle but does NOT formalize when the cycle fails, does NOT model commitment points, and does NOT provide measurement framework for temporal gaps.

**12. TOCTOU Race Conditions: Systematic Review (2022)**
- Authors: Various (see ResearchGate)
- Year: 2022
- Venue: ResearchGate
- URL: https://www.researchgate.net/publication/358760100_Defense_and_Attack_Techniques_against_File-based_TOCTOU_Vulnerabilities_a_Systematic_Review
- Match type: Weak convergence (foundational)
- Claims touched: Race conditions as vulnerability class
- How close: TOCTOU is the narrowest version of what Paper 14 generalizes. This review covers file-based TOCTOU over 35 years. Paper 14 explicitly positions itself as generalizing TOCTOU to system-level temporal attack surfaces. The TOCTOU literature treats these as implementation bugs, not structural control-theoretic properties.

**13. Temporal Adversarial Attacks Survey (2026)**
- Authors: (multiple)
- Year: 2026 (January)
- Venue: Preprints.org
- URL: https://www.preprints.org/manuscript/202601.0598
- Match type: Weak convergence (different meaning of "temporal")
- Claims touched: Adversarial attacks on time-series data
- How close: Covers adversarial attacks on time-series and RL systems—temporal in the data sense, not in the security-architecture sense. 127-paper survey. Different problem entirely despite shared terminology.

**14. Security Debt as Governance Issue (2025-2026)**
- Authors: Various (Veracode, ISACA)
- Year: 2025-2026
- Venue: Industry reports
- URLs: https://www.veracode.com/blog/security-debt-crisis/ ; https://www.isaca.org/resources/white-papers/2026/security-debt-the-unseen-risk-undermining-cyber-resilience
- Match type: Weak convergence (temporal dimension of unpatched vulnerabilities)
- Claims touched: Temporal gap in vulnerability remediation; measurement of security debt
- How close: Security debt (flaws unresolved >1 year) has a temporal dimension. 82% of organizations affected. Median fix time 243 days. This validates the general insight that temporal gaps create security exposure, but addresses vulnerability management rather than detection-decision-response architecture.

**15. Zero Trust Architecture Literature (NIST 800-207, 2020+)**
- Authors: NIST, various
- Year: 2020+
- Venue: NIST SP 800-207, various
- URL: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
- Match type: Weak convergence (implicit temporal minimization)
- Claims touched: Continuous verification; minimize trust window; per-request authorization
- How close: Zero trust literature describes continuous verification and minimal trust windows. Paper 14's insight that "zero trust implicitly minimizes temporal attack surface" appears to be a novel reframing. The zero trust literature does NOT use temporal/control-theoretic language to explain WHY continuous verification works.

**16. Quantifying Temporal Dynamics in Global Cyber Threats (2025)**
- Authors: (multiple)
- Year: 2025
- Venue: MDPI Mathematics
- URL: https://www.mdpi.com/2227-7390/13/10/1670
- Match type: Weak convergence (temporal but different scope)
- Claims touched: Temporal dynamics in cybersecurity
- How close: GPT-driven framework for risk forecasting based on temporal patterns in 11,497 incidents. Temporal in the trend-analysis sense, not in the detection-response-gap sense.

---

## Notes

### What converges
- The detection-response gap as a security problem is widely recognized (CrowdStrike breakout time, MTTD/MTTR metrics, OODA loop literature)
- Alert fatigue / approval fatigue as human temporal vulnerability is well-documented (ACM surveys, MFA fatigue literature, rubber-stamp risk)
- Fail-open vs. fail-closed as a design concern is established (Ruohonen SoK on secure defaults)
- Attacker-defender race dynamics are modeled in game theory literature
- TOCTOU as a race condition vulnerability class is foundational (35+ years)
- Schneier/Raghavan's OODA loop paper is the closest in spirit: same structural insight about temporal gaps creating exploitable vulnerabilities

### What remains novel in Paper 14
1. **Unified framework across five domains**: No existing work unifies SIEM, CI/CD, auth, rate limiting, and human-in-the-loop under a single temporal vulnerability model. Each domain has its own literature that touches temporal aspects, but the cross-domain generalization is new.
2. **Universal Bypass Inequality (UBI)**: The formal inequality (T_E > W_j) ∨ (Cost(E) > B_j) ∨ (E(t) = ∅) as a universal condition for security bypass has no direct parallel. No search returned this term or equivalent formalization.
3. **Three-clock model (detection, decision, response)**: The decomposition into three explicitly named temporal clocks with measurable parameters is not found elsewhere.
4. **Commitment polarity (C_j) as temporal parameter**: While fail-open/fail-closed is well-known as a design principle (Ruohonen), framing it as a temporal race condition parameter that determines system behavior under evidence insufficiency is novel.
5. **Political budget (κ_j)**: While alert fatigue is extensively documented, naming it as a formal parameter (political budget) that constrains security controls and modeling its interaction with temporal dynamics is new.
6. **Precision-robustness tradeoff in security enforcement**: The claim that attackers force defenders from precise (temporally coupled) to crude (temporally decoupled) enforcement, with ECH/DPI as canonical example, appears novel. The accuracy-robustness tradeoff in adversarial ML is well-known but applied to model training, not security architecture.
7. **Defender instrumentation framework**: The specific audit checklist (measure W_j distributions, map T_commit boundaries, audit C_j defaults, estimate κ_j thresholds) as a temporal security audit methodology has no direct parallel.
8. **Zero trust as temporal minimization**: Reframing zero trust principles as temporal coupling optimization (making T_commit small and frequent rather than large and rare) appears to be a novel interpretation.

### Strongest threat to novelty
- Schneier/Raghavan (2025) makes the same structural argument about temporal gaps creating security vulnerabilities, but for AI agents specifically rather than security systems generally. If they generalize their argument, it would overlap significantly.
- The game theory literature on attacker-defender dynamics covers similar conceptual ground but uses different formalism.
- CrowdStrike's breakout time analysis is the closest empirical operationalization and could be cited as validating evidence.

---

## Verdict

**Partial convergence confirmed, with substantial remaining novelty.**

The temporal dimension of security (detection delays, response gaps, human latency) is widely recognized in industry and research, but Paper 14's specific contributions remain novel:

- **Well-established (cite, don't claim novelty):** Detection-response gap as security problem; TOCTOU as race condition class; alert fatigue; MFA fatigue; fail-open/fail-closed defaults; OODA loop applied to security; breakout time as metric; attacker-defender game dynamics.
- **Converging but distinct (cite and differentiate):** Schneier/Raghavan OODA loop paper (closest parallel, different scope); temporal IDS taxonomy (arXiv:2511.03799, detection-only); game-theoretic attacker-defender models (different formalism).
- **Still novel (core contributions):** Unified five-domain temporal framework; Universal Bypass Inequality; three-clock model; commitment polarity as temporal parameter; political budget formalization; precision-robustness tradeoff in security enforcement; defender instrumentation audit methodology; zero trust as temporal minimization.

The paper's main contribution—generalizing temporal vulnerability into a single cross-domain framework with measurable parameters—has no direct precedent in the literature found. The closest work (Schneier/Raghavan) shares the structural insight but does not generalize across security domains or provide a measurement framework.
