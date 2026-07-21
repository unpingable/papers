# Plain-language summary

**Companion to:** *Ops Is Control with a Non-Self-Identical Controller* (Δt Paper 23)

**Version/status:** v1.0, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Many operational systems assume that the controller remains known and continuous. Real control rooms, on-call rotations, flight decks, and clinical teams violate that assumption. Control is handed off, authority arrives late, fatigue changes behavior, and experienced people quietly compensate using knowledge the official system does not record.

The plant may appear stable even though the controller that is actually stabilizing it differs from the controller described on paper.

The paper separates two kinds of continuity. **Continuity of action** asks whether an intervention can still reach the plant before rescue becomes impossible; authority routing, handoff loss, reorientation, and ambiguity all consume that time budget. **Continuity of identity** asks whether observers can recover the controller that actually produced the behavior when nominal procedure is supplemented by hidden human compensation.

The paper gives three ways that compensation can become invisible: the authority model can project it away, the measurement system can be insensitive to it over the relevant horizon, or it can resemble an ordinary change within the nominal controller family. Together, the two axes distinguish loss of timely control from loss of knowledge about who or what was controlling. That tells operators why better handoff documents may be insufficient: authority routing and observability can be the binding problems even when the procedure is clear.

## Claim boundary

The projection-masking result is exact. Null-space masking is first-order over a finite horizon under local assumptions, and controller-family aliasing is only bounded up to an output tolerance. The theorem gives sufficient, not necessary, conditions and does not establish how often they occur. The grid scenario is composed and illustrative rather than a diagnosis of a named incident. The framework targets human-operational control layers, not all automated control systems.

## Read the paper

- [Manuscript source](non_self_identical_controller.md)
- [PDF](non_self_identical_controller.pdf)
- [Directory guide](README.md)
- [Concept DOI](https://doi.org/10.5281/zenodo.19715301)
- [Zenodo record](https://zenodo.org/records/19715302)
