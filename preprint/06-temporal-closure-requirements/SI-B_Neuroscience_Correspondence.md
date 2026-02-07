<!-- Converted from DOCX via pandoc on 2026-02-02 -->
Supplementary Information B:

Extended Neuroscience Correspondence

Overview

This supplement provides detailed correspondence between the Δt framework\'s three operators and known neural mechanisms. We demonstrate that biological systems implement these operators through specific anatomical structures and physiological processes, validating the framework\'s substrate-independence claim.

1\. Operator 1: Timescale Hierarchy in Neural Systems

1.1 Empirical Evidence for Cortical Timescale Stratification

Murray et al. (2014) measured intrinsic timescales across macaque cortex using autocorrelation of spiking activity. Key findings:

• Early sensory areas (V1, A1): τ ≈ 50-100ms

• Intermediate areas (MT, parietal): τ ≈ 200-500ms

• Prefrontal cortex: τ ≈ 1000-3000ms

• Anterior prefrontal: τ up to 10 seconds

**Framework correspondence:** Ratios between adjacent layers range from 2× to 50×, with most transitions in the O(10²) regime required by Operator 1.

1.2 Cross-Frequency Coupling as Temporal Integration

Canolty & Knight (2010) demonstrated that slower oscillations modulate the amplitude of faster oscillations---exactly the coupling pattern predicted by the framework.

**Theta-Gamma Coupling (4-8 Hz modulating 30-100 Hz):** Observed in hippocampus and cortex during memory encoding. Ratio ≈ 10×, matching framework predictions.

**Alpha-Beta Dynamics (8-12 Hz, 13-30 Hz):** Alpha gates information flow; beta coordinates motor/cognitive control. Intermediate timescale layer.

**Circadian-Neural Coupling (24h modulating hours-minutes):** Circadian rhythms modulate neuromodulator release, which adjusts neural timescales. Ratio ≈ 10³-10⁴.

2\. Operator 2: Endogenous State Maintenance

2.1 Persistent Neural Activity

Neurons in prefrontal cortex maintain elevated firing rates during working memory delays (Fuster & Alexander 1971, Goldman-Rakic 1995). This persistent activity continues without external input for seconds to minutes---clear example of endogenous state evolution.

**Mechanism:** Recurrent excitatory connections create attractor states. NMDA receptor kinetics provide slow time constants enabling persistence.

2.2 Synaptic Bistability

Calcium-calmodulin-dependent protein kinase II (CaMKII) exhibits bistable states that persist for hours to days (Lisman et al. 2002). Phosphorylation state acts as molecular memory, maintaining synaptic strength changes.

**Framework correspondence:** Multiple timescales of state maintenance---milliseconds (membrane potential), seconds (persistent firing), hours-days (synaptic modifications). All continuously evolving via autonomous dynamics.

2.3 Default Mode Network as Resting Dynamics

When external inputs cease, the brain does not become inactive---it enters a characteristic resting state with organized activity patterns (Raichle et al. 2001). The Default Mode Network (DMN) shows correlated fluctuations even during rest.

**Critical implication:** The brain maintains temporal identity even without external stimulation. This is endogenous state evolution---exactly what transformers cannot implement.

3\. Operator 3: Homeostatic Coherence Regulation

3.1 Anterior Cingulate Cortex as Error Monitor

ACC detects conflicts, errors, and unexpected outcomes (Botvinick et al. 2001). When conflict exceeds threshold, ACC signals need for increased control to PFC.

**Framework correspondence:** ACC implements coherence metric χ monitoring. High conflict = approaching basin boundary. ACC → PFC signaling triggers intervention.

3.2 Thalamic Gating and Gain Control

Thalamus regulates information flow between cortical layers via dynamic gating (Sherman & Guillery 2002). During high arousal or conflict, thalamus modulates cortical gain---equivalent to adjusting coupling strength.

**Mechanism:** Reticular nucleus provides inhibitory control. Adjusts effective coupling matrix M in real-time based on cortical state.

3.3 Neuromodulatory Systems

Dopamine, norepinephrine, serotonin, and acetylcholine modulate neural excitability and coupling strength on timescales of seconds to minutes.

**Dopamine:** Modulates PFC working memory stability. High DA → stronger attractor basins. Low DA → more flexible switching.

**Norepinephrine:** Adjusts signal-to-noise ratio. LC-NE system responds to arousal/uncertainty, modulating cortical gain.

**Acetylcholine:** Regulates attention and plasticity. High ACh → increased encoding. Low ACh → consolidation mode.

**Framework correspondence:** These systems implement adaptive coupling control and homeostatic parameter restoration---the two key controller functions.

4\. Clinical Phenomenology as Invariant Violations

If the framework is correct, psychiatric and neurological disorders should map onto specific invariant violations. This section proposes testable correspondences.

4.1 Dissociative Episodes (Flicker)

**Phenomenology:** Transient loss of perceptual integration. Derealization/depersonalization. System returns to baseline quickly.

**Neural signature:** Temporary theta-gamma decoupling observed during dissociative states (Bob 2003).

**Framework prediction:** Shallow excursion from metastable basin. Coupling temporarily weakens but basin structure remains. System naturally returns.

4.2 Psychotic Breaks (Snap)

**Phenomenology:** Catastrophic loss of reality testing. Sudden transition to alternative cognitive regime. Difficult to reverse spontaneously.

**Neural signature:** Abnormal cross-frequency coupling patterns in schizophrenia (Uhlhaas & Singer 2010). Disrupted theta-gamma coordination.

**Framework prediction:** Noise-driven escape from basin when barrier αΦ(Δt) ≈ O(1). System crosses into alternative attractor with high hysteresis.

4.3 Treatment-Resistant Depression (Hysteresis)

**Phenomenology:** Locked in negative cognitive basin. Intervention temporarily lifts mood but system returns to depressed state. High relapse rate.

**Neural signature:** Reduced PFC-limbic coupling. Abnormal default mode activity (Sheline et al. 2009).

**Framework prediction:** Deep basin with high exit barrier. Standard treatments provide insufficient energy to escape. Requires sustained intervention or barrier-lowering (e.g., ketamine\'s rapid plasticity effects).

5\. Detailed Anatomical Layer Mapping

Layer L₀ (Fast, τ ≈ 10-100ms): Sensorimotor Integration

**Neural structures:** Primary sensory cortices (V1, A1, S1), motor cortex (M1), cerebellum

**Oscillations:** Gamma (30-100 Hz), fast beta (20-30 Hz)

**Function:** Feature binding, sensory integration, motor control

Layer L₁ (Intermediate, τ ≈ 100ms-1s): Cross-Modal Integration

**Neural structures:** Associative cortices (parietal, temporal), basal ganglia loops

**Oscillations:** Alpha (8-12 Hz), beta (13-20 Hz)

**Function:** Attention, action selection, perceptual categorization

Layer L₂ (Slow, τ ≈ 1s-1min): Working Memory & Narrative

**Neural structures:** Prefrontal cortex (DLPFC, VLPFC), hippocampus, anterior cingulate

**Oscillations:** Theta (4-8 Hz), slow oscillations during sleep (\<1 Hz)

**Function:** Working memory maintenance, episodic sequence tracking, goal-directed planning

Layer L₃ (Very Slow, τ ≈ hours-days): Identity & Goals

**Neural structures:** Medial prefrontal cortex, ventromedial PFC, default mode network, neuromodulator systems

**Oscillations:** Circadian rhythms (24h), ultradian cycles (90min), slow cortical potentials

**Function:** Value systems, long-term goals, self-concept, memory consolidation

6\. Testable Neurophysiological Predictions

Prediction 1: Cross-Frequency Coupling Breakdown Predicts Coherence Loss

Test: Measure theta-gamma phase-amplitude coupling during task performance. Framework predicts that coupling strength correlates with behavioral coherence (maintained goal pursuit across trials).

**Method:** Local field potential recordings during working memory tasks. Compare high vs low coupling trials.

**Expected result:** Low coupling predicts increased error rates, premature task abandonment, or goal confusion.

Prediction 2: Pharmacological Coupling Modulation Affects Metastability

Test: Manipulate dopamine or acetylcholine levels while recording neural activity. Framework predicts changes in basin depth and transition rates.

**Method:** Systemic drug administration (dopamine agonist/antagonist) with simultaneous LFP or fMRI recording.

**Expected result:** DA agonists → deeper basins (more rigid). DA antagonists → shallower basins (more flexible, but less stable).

Prediction 3: Lesioning Controller Structures Causes Specific Instabilities

Test: Reversible inactivation of ACC or thalamic nuclei should increase metastable regime failures.

**Method:** Optogenetic silencing or muscimol injection in ACC during cognitive tasks requiring coherence maintenance.

**Expected result:** Increased Flicker (transient performance drops) and Snap (catastrophic goal abandonment). Hysteresis effects where system gets stuck in low-performance states.

7\. Conclusion

The extensive correspondence between the Δt framework\'s three operators and known neural mechanisms provides strong validation. The brain implements:

• Temporal separation through cortical hierarchy and oscillatory stratification

• Endogenous state via persistent activity, synaptic bistability, and resting-state dynamics

• Adaptive control through ACC monitoring, thalamic gating, and neuromodulatory systems

Clinical disorders map onto predicted invariant violations, suggesting the framework captures fundamental organizational principles rather than superficial analogies. The testable predictions provide paths for empirical validation or falsification.

Most critically: these neural mechanisms evolved to solve the same temporal coherence problem the framework addresses. This convergence across billions of years of evolution suggests the constraints are fundamental, not arbitrary.

References

Botvinick, M.M., et al. (2001). Conflict monitoring and cognitive control. Psychological Review, 108(3), 624-652.

Buzsáki, G. (2006). Rhythms of the Brain. Oxford University Press.

Canolty, R.T. and Knight, R.T. (2010). The functional role of cross-frequency coupling. Trends in Cognitive Sciences, 14(11), 506-515.

Fuster, J.M. and Alexander, G.E. (1971). Neuron activity related to short-term memory. Science, 173(3997), 652-654.

Goldman-Rakic, P.S. (1995). Cellular basis of working memory. Neuron, 14(3), 477-485.

Lisman, J., et al. (2002). The molecular basis of CaMKII function in synaptic and behavioural memory. Nature Reviews Neuroscience, 3(3), 175-190.

Murray, J.D., et al. (2014). A hierarchy of intrinsic timescales across primate cortex. Nature Neuroscience, 17(12), 1661-1663.

Raichle, M.E., et al. (2001). A default mode of brain function. Proceedings of the National Academy of Sciences, 98(2), 676-682.

Sherman, S.M. and Guillery, R.W. (2002). The role of the thalamus in the flow of information to the cortex. Philosophical Transactions of the Royal Society B, 357(1428), 1695-1708.

Sheline, Y.I., et al. (2009). The default mode network and self-referential processes in depression. Proceedings of the National Academy of Sciences, 106(6), 1942-1947.

Uhlhaas, P.J. and Singer, W. (2010). Abnormal neural oscillations and synchrony in schizophrenia. Nature Reviews Neuroscience, 11(2), 100-113.
