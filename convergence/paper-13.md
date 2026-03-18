# Paper 13 — Temporal Asymmetry in Censorship — Convergence Spike

**Full title:** Temporal Asymmetry in Censorship Systems
**Date:** 2026-01-13
**DOI:** 10.5281/zenodo.18235696

## Status: complete

## Claim Cluster
- DPI circumvention mechanisms are formalizable as exploitation of temporal asymmetry between evidence accumulation and enforcement
- A Universal Bypass Inequality (UBI) governs the conditions under which censorship/inspection systems can be systematically evaded
- Timing, computational cost, and evidence denial are the three structural axes of circumvention
- Censorship systems have an inherent control-theoretic vulnerability: they must accumulate evidence before acting, while the circumvented party can act before evidence accumulates

## Search Terms
- deep packet inspection circumvention timing attack
- censorship evasion temporal asymmetry
- evidence accumulation enforcement race condition
- network censorship control theory formal model
- bypass inequality inspection systems
- timing-based censorship circumvention
- asynchronous enforcement evidence denial
- DPI evasion formal analysis defender perspective

## Expected Convergence Level
partial convergence likely
Censorship circumvention is well-studied in networking and security communities, but usually from an engineering rather than control-theoretic perspective. The formal temporal asymmetry framing may be novel, but the underlying observations about timing advantages are likely recognized by practitioners.

## Hits

### Strong Partial Convergence (same observations, different framing)

1. **Geneva: Evolving Censorship Evasion Strategies**
   - Authors: Kevin Bock, George Hughey, Xiang Qin, Dave Levin
   - Year: 2019
   - Venue: ACM CCS 2019
   - URL: https://dl.acm.org/doi/10.1145/3319535.3363189
   - Match type: **strong partial** — same attack surface, automated rather than formal
   - Claims touched: Packet manipulation as DPI bypass; fragmentation, timing, header tricks as bypass primitives
   - How close: Geneva discovers bypass strategies empirically via genetic algorithm using the same four primitives (drop, tamper, duplicate, fragment) that Paper 13 would classify under Families A and B. Geneva treats these as an engineering search problem; Paper 13 treats them as instances of a unified control-theoretic inequality. Geneva does NOT formalize *why* these work in terms of temporal asymmetry or resource bounds — it finds *that* they work. Complementary, not contradictory.

2. **SymTCP: Eluding Stateful Deep Packet Inspection with Automated Discrepancy Discovery**
   - Authors: Zhongjie Wang, Shitong Zhu, Yue Cao, Zhiyun Qian, Chengyu Song, Srikanth V. Krishnamurthy, Kevin S. Chan, Tracy D. Braun
   - Year: 2020
   - Venue: NDSS 2020
   - URL: https://www.ndss-symposium.org/ndss-paper/symtcp-eluding-stateful-deep-packet-inspection-with-automated-discrepancy-discovery/
   - Match type: **strong partial** — identifies the same structural vulnerability (DPI state machine differs from endpoint state machine), but frames as implementation discrepancy not temporal asymmetry
   - Claims touched: DPI middleboxes implement simplified state machines that diverge from endpoints; this discrepancy is exploitable
   - How close: SymTCP's core insight — that DPI implements a *simplified* state machine that differs from the endpoint — is exactly what Paper 13 formalizes as bounded W_j and D_j. SymTCP uses symbolic execution to find the discrepancies; Paper 13 derives *why* they must exist from resource bounds. Different method, converging diagnosis.

3. **Come as You Are: Helping Unmodified Clients Bypass Censorship with Server-side Evasion**
   - Authors: Bock, Hughey, Merino, Arya, Liscinsky, Pogosian, Levin
   - Year: 2020
   - Venue: ACM SIGCOMM 2020
   - URL: https://dl.acm.org/doi/10.1145/3387514.3405889
   - Match type: **partial** — discovers that China's GFW uses distinct censorship boxes per protocol, each with own bugs; supports multi-stage model
   - Claims touched: DPI enforcement stages have independent parameters; bypass can exploit per-stage weaknesses
   - How close: Empirically confirms what Paper 13 models as independent enforcement stages (W_j, D_j, B_j, C_j per stage). Does not formalize the relationship.

4. **Even Censors Have a Backup: Examining China's Double HTTPS Censorship Middleboxes**
   - Authors: Bock, Naval, Reese, Levin
   - Year: 2021
   - Venue: ACM SIGCOMM FOCI 2021
   - URL: https://dl.acm.org/doi/10.1145/3473604.3474559
   - Match type: **partial** — empirically documents "censorship in depth" (layered enforcement) that Paper 13 models as multi-stage cascades
   - Claims touched: Censors deploy redundant enforcement stages; primary can be defeated independently from secondary
   - How close: Provides empirical evidence for multi-stage enforcement architecture. Paper 13's contribution is the formal model showing why each stage faces the same UBI constraints independently.

5. **Detecting and Evading Censorship-in-Depth: A Case Study of Iran's Protocol Whitelister**
   - Authors: Bock, Fax, Reese, Singh, Levin
   - Year: 2020
   - Venue: USENIX FOCI 2020
   - URL: https://www.usenix.org/conference/foci20/presentation/bock
   - Match type: **partial** — documents fail-open/fail-closed behavior and protocol whitelisting as enforcement regime
   - Claims touched: Iran's protocol filter examines first two data packets then commits (W_j = 2 packets); exploitable via bad-checksum trick (evidence manipulation); fail-closed enforcement with 60-second penalty
   - How close: Provides a concrete instance of Paper 13's enforcement stage formalization. The filter's "look at first two packets then commit" is exactly a tight inspection window W_j. The bad-checksum trick is a Family B desynchronization (feeding evidence the DPI accepts but the endpoint rejects). Does not generalize to formal framework.

6. **Exposing and Circumventing SNI-based QUIC Censorship of the Great Firewall of China**
   - Authors: Zohaib et al.
   - Year: 2025
   - Venue: USENIX Security 2025
   - URL: https://www.usenix.org/conference/usenixsecurity25/presentation/zohaib
   - Match type: **strong partial** — documents that GFW decrypts QUIC Initial packets but cannot reassemble fragmented ClientHello across multiple QUIC CRYPTO frames
   - Claims touched: T_E > W_j (evidence fragmentation defeats inspection); computational overhead of decryption reduces effectiveness under load; Family A (Δt inflation) via SNI splitting
   - How close: Directly confirms Paper 13's prediction that QUIC SNI fragmentation exploits reassembly limitations (D_j). The finding that "computational overhead of decryption reduces effectiveness under moderate traffic loads" is exactly Cost(f(E)) > B_j(λ). Strong empirical validation of UBI terms, without the formal framework.

7. **Encrypted Client Hello (ECH) in Censorship Circumvention**
   - Authors: Niklas Niere et al.
   - Year: 2025
   - Venue: FOCI 2025 (PETS)
   - URL: https://petsymposium.org/foci/2025/foci-2025-0016.php
   - Match type: **strong partial** — documents ECH censorship shifting to DNS/IP blocking (regime change), confirming Paper 13's "ECH as phase transition" thesis
   - Claims touched: ECH forces censors from precision targeting to crude infrastructure bans (DNS blocking, IP blocking); Russia censors ECH connections to Cloudflare IPs; China/Iran prevent ECH via encrypted DNS censorship
   - How close: Empirically confirms Paper 13's central ECH claim: "ECH doesn't make censorship slower — it makes it cruder." The finding that censorship shifts to DNS and IP blocking is precisely the predicted regime transition from Regime 1 (content-based DPI) to Regime 4 (infrastructure bans). Does not use "phase transition" language or formal model.

8. **QUICstep: Circumventing QUIC-based Censorship**
   - Authors: Watson Jia, Yixin Wang et al.
   - Year: 2023
   - Venue: arXiv / MadS&P
   - URL: https://arxiv.org/abs/2304.01073
   - Match type: **partial** — uses QUIC connection migration to hide handshake, then resume in plaintext
   - Claims touched: Family C (Δt escalation control) — starts with encrypted channel for handshake only, migrates to direct connection, minimizing commitment
   - How close: QUICstep's strategy (encrypt handshake via proxy, then migrate to direct path) is an instance of commitment minimization — use high-cost channel only for evidence-sensitive phase, then drop to low-cost. Operationalizes what Paper 13 models as Comm(L_i) optimization.

### Taxonomies and Surveys (overlap in classification, not in formal framework)

9. **RFC 9505: A Survey of Worldwide Censorship Techniques**
   - Authors: Hall, Aaron, Andersdotter, Jones, Feamster, Knodel
   - Year: 2023
   - Venue: IRTF RFC
   - URL: https://datatracker.ietf.org/doc/rfc9505/
   - Match type: **weak partial** — comprehensive taxonomy of censorship techniques but purely descriptive, no formal model
   - Claims touched: Catalogs the same techniques Paper 13 formalizes (DPI, DNS, IP blocking, protocol blocking)
   - How close: Enumerates what Paper 13 organizes into a formal hierarchy. RFC 9505 classifies by mechanism; Paper 13 classifies by which UBI term is exploited.

10. **A Taxonomy of Internet Censorship and Anti-Censorship**
    - Authors: Christopher Leberknight, Mung Chiang, Felix Ming Fai Wong
    - Year: 2010 (draft), 2012 (published)
    - Venue: Princeton / International Journal of E-Politics
    - URL: https://www.princeton.edu/~chiangm/anticensorship.pdf
    - Match type: **weak partial** — early taxonomy, no temporal/control-theoretic framing
    - Claims touched: General classification of censorship and anti-censorship techniques
    - How close: Foundational taxonomy work, but purely descriptive. Does not formalize why bypass works.

11. **A Survey of Internet Censorship and its Measurement: Methodology, Trends, and Challenges**
    - Authors: Wendzel et al.
    - Year: 2025
    - Venue: arXiv (2502.14945) / Computers & Security
    - URL: https://arxiv.org/abs/2502.14945
    - Match type: **weak partial** — comprehensive survey bridging censorship with traffic obfuscation and information hiding
    - Claims touched: Surveys censorship techniques, measurement methods, circumvention tool detection
    - How close: Descriptive survey, no formal framework. Useful as evidence that the field lacks the kind of unifying model Paper 13 proposes.

12. **SoK: The Spectre of Surveillance and Censorship in Future Internet Architectures**
    - Authors: Michael Wrana, Diogo Barradas, N. Asokan
    - Year: 2025
    - Venue: PETS 2025 (Best Paper Award)
    - URL: https://petsymposium.org/popets/2025/popets-2025-0073.php
    - Match type: **weak partial** — analyzes censorship capabilities of future internet architectures
    - Claims touched: Routing/addressing design choices affect censorship feasibility
    - How close: Different scope (future architectures vs. current DPI), but reinforces that censorship capability is structurally determined by protocol design — consistent with Paper 13's claim that protocol evolution forces regime transitions.

### Tangentially Related (same domain, different focus)

13. **The Discriminative Power of Cross-layer RTTs in Fingerprinting Proxy Traffic**
    - Authors: Diwen Xue, Robert Stanley, Piyush Kumar, Roya Ensafi
    - Year: 2025
    - Venue: NDSS 2025
    - URL: https://www.ndss-symposium.org/ndss-paper/the-discriminative-power-of-cross-layer-rtts-in-fingerprinting-proxy-traffic/
    - Match type: **tangential but interesting** — uses cross-layer timing discrepancies to *detect* circumvention (censor's perspective)
    - Claims touched: Transport vs. application layer timing misalignment as fingerprint; exploits the same two-clock structure Paper 13 describes, but from the defender side
    - How close: Implicitly validates Paper 13's two-clock model by showing that the temporal misalignment between transport and application layers is real and measurable. The censor uses it for detection; Paper 13 argues the circumventor exploits the same structural feature for evasion. Two sides of the same coin.

14. **Advancing Obfuscation Strategies to Counter China's Great Firewall: A Technical and Policy Perspective**
    - Authors: (unnamed in results)
    - Year: 2025
    - Venue: arXiv (2503.02018)
    - URL: https://arxiv.org/abs/2503.02018
    - Match type: **partial** — discusses GFW's precision-cost tradeoff
    - Claims touched: "aggressive filtering that mistakenly classifies legitimate encrypted communications as VPN traffic leads to false positives" — confirms Paper 13's precision-robustness curve and political budget κ_j
    - How close: Observes the same tradeoff Paper 13 formalizes but does not provide formal framework.

15. **Enemy at the Gateways: Censorship-Resilient Proxy Distribution Using Game Theory**
    - Authors: Milad Nasr et al.
    - Year: 2019 (published), 2023 (NDSS)
    - Venue: NDSS
    - URL: https://www.ndss-symposium.org/ndss-paper/enemy-at-the-gateways-censorship-resilient-proxy-distribution-using-game-theory/
    - Match type: **tangential** — game-theoretic model of proxy distribution, not DPI bypass
    - Claims touched: Formal/game-theoretic treatment of censorship, but addresses proxy discovery not inspection evasion
    - How close: Shows game theory applied to censorship domain but on a different problem (resource allocation for proxy distribution, not timing of inspection bypass).

16. **GoodbyeDPI / NoDPI / Zapret (tools)**
    - Authors: ValdikSS (GoodbyeDPI), GVCoder09 (NoDPI), bol-van (Zapret)
    - Year: 2024-2025 (active development)
    - Venue: GitHub
    - URLs: https://github.com/ValdikSS/GoodbyeDPI, https://github.com/GVCoder09/nodpi
    - Match type: **partial** — implement exactly the Family A and B tactics Paper 13 describes
    - Claims touched: ClientHello fragmentation, SNI splitting, packet jitter, desynchronization as practical DPI bypass
    - How close: These tools *operationalize* what Paper 13 *formalizes*. NoDPI splits ClientHello into four parts around SNI. GoodbyeDPI fragments packets so DPI cannot reassemble. Zapret uses "desynchronization and forgery techniques." None provide formal analysis of *why* these work — they are empirical engineering.

### Collateral Damage / Political Cost (supports κ_j formalization)

17. **"Collateral Freedom" framework (various authors, CFR, Berkman Klein)**
    - Year: 2011-2018
    - Venue: Council on Foreign Relations, Berkman Klein Center
    - URLs: https://www.cfr.org/articles/bold-proposal-fighting-censorship-increase-collateral-damage, https://cyber.harvard.edu/publication/2018/censorship-and-collateral-damage
    - Match type: **partial** — formalizes collateral damage as strategic lever against censors
    - Claims touched: Censors are less willing to block when economic damage is high; fail-closed censorship forces choice between allowing bypass or suffering maximum collateral damage
    - How close: The "Collateral Freedom" concept is the strategic implication of Paper 13's political budget κ_j. Paper 13 formalizes this as a constraint in the UBI; prior work treats it as a strategic observation.

## Notes

**What the literature confirms:**
- The *observations* underlying Paper 13 are well-established: DPI has timing constraints, fragmentation defeats shallow inspection, ECH shifts censorship to cruder methods, censors face precision-cost tradeoffs.
- The Bock et al. research program (Geneva, SymTCP, Come as You Are, Even Censors Have a Backup) provides extensive empirical evidence for nearly every individual claim in Paper 13.
- The USENIX Security 2025 paper on QUIC censorship provides almost exactly the empirical validation Paper 13 would predict: fragmentation bypasses reassembly limits, computational cost reduces effectiveness under load.

**What remains novel in Paper 13:**
1. **The two-clock model** (T_transport vs. T_inspect): No published work frames DPI bypass as a clock desynchronization problem. The NDSS 2025 cross-layer RTT paper uses timing discrepancies for *detection* but does not formalize the two-clock structure for *evasion theory*.
2. **The Universal Bypass Inequality**: No formal necessary-and-sufficient condition for bypass exists in the literature. Geneva finds strategies empirically; SymTCP finds them via symbolic execution; Paper 13 derives *when they must exist* from first principles.
3. **Three Δt attack families as unified taxonomy**: Existing taxonomies (RFC 9505, Leberknight-Chiang) classify by mechanism (DNS, IP, DPI). Paper 13 classifies by which *temporal parameter* is exploited (inflation, desynchronization, escalation control). This is a genuinely different organizing principle.
4. **Enforcement stage formalization (W_j, D_j, B_j, C_j, κ_j)**: Individual parameters are observed informally (Iran's protocol filter looks at first two packets = tight W_j; GFW's false positive sensitivity = κ_j constraint). No work formally bundles these into a tuple.
5. **"Offense in depth" as commitment minimization**: The layered escalation strategy is practiced (tools exist at every layer) but not formalized as commitment signal minimization under adversarial observation.
6. **ECH as "phase transition" (formal)**: Niere et al. (FOCI 2025) observe the same regime shift empirically but do not characterize it as a phase transition or connect it to evidence denial (E(t) = emptyset) in a formal model.
7. **Cross-domain generalization** (institutional governance, LLM control, BFT): Not attempted elsewhere in censorship literature.

**What is well-covered (not novel):**
- DPI bypass via fragmentation/manipulation (Geneva, GoodbyeDPI, etc.)
- ECH shifting censorship to DNS/IP blocking (Niere et al.)
- Collateral damage as strategic constraint
- Censorship-in-depth as layered enforcement

**No contradictions found.** All empirical work is consistent with Paper 13's predictions.

## Verdict

**Partial convergence confirmed, as predicted.** The empirical observations and engineering practices are thoroughly validated by the published literature (2019-2025). What Paper 13 adds is genuinely novel: a unified control-theoretic framework (two-clock model, UBI, three attack families, enforcement stage tuple) that explains *why* all known bypass tactics work and *when* they must succeed. The formal temporal asymmetry framing, the Universal Bypass Inequality as a necessary-and-sufficient condition, and the three-family classification by temporal parameter are not present in any published work found. The cross-domain generalization to institutional governance and LLM control is entirely novel.

The paper should cite Geneva (CCS 2019), SymTCP (NDSS 2020), the Bock group's empirical work, the USENIX Security 2025 QUIC paper, and Niere et al. (FOCI 2025) as empirical validation. The NDSS 2025 cross-layer RTT paper is worth citing as evidence that the two-clock structure is real and measurable from the censor's side.

**Risk level: Low.** The formal framework appears genuinely novel. The main risk is that someone publishes a similar control-theoretic formalization before this paper gains traction, but no evidence of such work was found.
