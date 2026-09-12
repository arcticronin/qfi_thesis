12-minute defence — English speaking script

This script follows the 14 main slides of `presentation_3/main.pdf`. Quoted paragraphs are spoken text; delivery notes and answers below are for preparation. The timings include short pauses and pointing to figures. Rehearse aloud before treating them as a reliable duration. The ten appendix slides are for questions only.

| Slide | Topic | Time | Cumulative end |
|---|---|---:|---:|
| 1 | Thesis title and ASI collaboration | 0:25 | 0:25 |
| 2 | Local distinguishability and QFI | 0:40 | 1:05 |
| 3 | Measurement direction: geometric example | 1:00 | 2:05 |
| 4 | VQSE and the PCA analogy | 1:05 | 3:10 |
| 5 | QFI geometry and optimization | 0:55 | 4:05 |
| 6 | The finite Ising magnetometer | 0:40 | 4:45 |
| 7 | Thermal sensitivity outside the optimum | 1:15 | 6:00 |
| 8 | SPADE detector image | 0:10 | 6:10 |
| 9 | Spatial modes and the recorded data | 0:45 | 6:55 |
| 10 | Quantum-to-classical channel model | 0:55 | 7:50 |
| 11 | Non-unique Kraus representations | 1:05 | 8:55 |
| 12 | Physical loss model and completeness | 1:05 | 10:00 |
| 13 | Information retained by the receiver | 1:15 | 11:15 |
| 14 | Conclusions and outlook | 0:45 | 12:00 |

1 — Thesis title and collaboration

“My thesis asks how much information a quantum sensor contains about an unknown physical parameter, and how much of it remains accessible in an experiment.

Developed in collaboration with the Italian Space Agency, it connects variational quantum methods with magnetic-field sensing and an optical experiment motivated by exoplanet imaging.”

Delivery: credit ASI without reading the full title or supervisors aloud.

2 — Local distinguishability

“These curves represent measurement statistics at two nearby parameter values. If a small parameter change produces a large statistical response, those values become easier to distinguish.

Classical Fisher information quantifies that local sensitivity for a chosen measurement.

Quantum Fisher information asks for the largest value attainable by choosing the measurement optimally. It is a property of the parameterized state family, and an upper limit for any particular detector.

The next example makes this distinction concrete.”

Delivery: point to the curves, then to the supremum. Do not read the CFI formula term by term.

3 — Measurement direction

“On the left is a two-dimensional section of the Bloch ball. The black point represents a mixed qubit, and the arrow shows how it moves when the unknown rotation angle changes slightly.

The blue and green lines are two possible measurement axes through the origin. We keep the state family fixed and change only the measurement.

The plot on the right gives the resulting classical Fisher information. The diagonal measurement extracts about 0.47. At this operating point, the vertical measurement is optimal and reaches 0.64, the quantum Fisher information.

The horizontal green line is that quantum limit. A different measurement changes how much information we extract; it does not change the limit itself.”

Delivery: use the pointer in this order: state point, short state-change arrow, blue diameter, blue point on the CFI curve, green diameter, green maximum. The small unknown angle is theta; phi is the measurement setting. The plotted Fisher information concerns theta, not phi. Appendix J contains the exact calculation.

4 — Variational spectral estimation

“For a large mixed state, evaluating quantum information can require expensive spectral information. The Variational Quantum State Eigensolver, or VQSE, learns a useful basis instead.

The analogy with PCA is spectral extraction. PCA ranks covariance directions by variance; VQSE ranks components of a density matrix by probability weight.

A trainable circuit rotates copies of the state. At the ideal optimum, output frequencies reveal eigenvalues, and the inverse rotation recovers the corresponding eigenvectors.

Retaining dominant components supplies information for fidelity-based QFI bounds, without requiring full classical diagonalization. Their weight alone does not guarantee that they contain all the sensitivity.

My contribution was implementing and benchmarking these established methods and examining their use in sensing.”

Delivery: compare the two matrices, then point to the rotation. Attribute the algorithms to the cited literature. The exact SLD results shown later are numerical references, not hardware estimates.

5 — Geometry and optimization

“QFI has another role when the parameters are adjustable circuit controls. It describes how strongly different control changes move the prepared quantum state.

This gives a useful connection to Newton's method. Newton preconditions the gradient using the Hessian, which describes curvature of the objective. Quantum natural gradient instead uses the ansatz QFI matrix, which describes state distinguishability.

The update structures are similar, but these matrices are not generally equal. Regularization stabilizes directions with little or redundant state change.

So the same information geometry can help train a variational circuit, as well as assess the sensitivity of a sensor.”

Delivery: say “Hessian of the objective” and “geometry of the state” distinctly. Do not imply this proves faster VQSE training. The separate RBM stochastic-reconfiguration example is in Appendix C.

6 — Ising magnetometer

“The first physical application is a transverse-field Ising chain. Six interacting spins encode the field, while measurements access only four.

I compare two preparations of the full chain: its ground state and a thermal Gibbs state. Both are then reduced to the same accessible subsystem.

The comparison keeps the sensor and the observation restriction fixed, while changing the preparation. Even a pure global ground state can appear mixed when part of the system is inaccessible.”

Delivery: point to the four coloured spins and two outlined spins. The discarded spins are not the thermal bath. Avoid deriving the Hamiltonian.

7 — Thermal sensitivity

“The horizontal axis is the transverse field; the vertical axis is the exact QFI of the four-spin subsystem. Blue is the reduced ground state, and green is the reduced thermal state at beta J equal to two.

The thermal preparation has a lower peak: about 2.61 compared with 3.93. But beyond the ground-state optimum, its QFI is higher over the shaded interval.

That matters when the field is not already known to lie near the best sensing point. A preparation selected only for its maximum QFI may perform less well elsewhere in the plausible operating range.

This is a comparison of different field-dependent preparation families. Thermal populations themselves change with the field and contribute information. It does not mean that applying fixed noise increases QFI, or that a thermal state is always the best choice.”

Delivery: read the axes first, point to the lower green peak, then follow the shaded region. Pause before the operating-range interpretation. This is a finite-system numerical result; an unknown-field decision still requires a plausible range or prior.

8 — SPADE detector

“The second application is an optical receiver: SPADE, which separates incoming light into spatial modes before photon counting.”

Delivery: show the detector image for approximately ten seconds. This slide remains reserved for your image; do not describe apparatus details that are not visible or verified.

9 — Measurement and archived record

“The reference mode responds mainly to the aligned bright source, while displacement creates a response in first-order modes.

The completed experiment supplied 52,500 counts, from 525 settings repeated 100 times. However, it recorded only the sum of two first-order outputs, without resolved ports, failure events or measurements in additional bases.

Repeating that observation improves its precision, but does not reveal unmeasured coherences. The record supports modelling the observed response; it cannot identify the complete optical state. That motivated the channel framework.”

Delivery: point to the summed-count equation. Modes are spatial patterns; the sorter does not label each photon as coming from one source or the other.

10 — Quantum-to-classical model

“The framework separates source preparation, optical propagation, measurement, classical readout and repeated counts.

Before measurement, quantum channels describe effects such as loss, dephasing and coherent mode mixing. The measurement converts the output state into probabilities. Readout and calibration then describe how these probabilities become recorded counts.

This distinction matters physically: mixing optical amplitudes is different from confusing detector labels after measurement.

The model also creates information checkpoints. We can ask what the source contains, what survives the optical channel, and what the receiver extracts. Independent calibration can constrain individual stages instead of absorbing every discrepancy into one effective fit.”

Delivery: follow the diagram once. Emphasize the boundary at measurement and the role of independent calibration. The GP validation results are available in Appendix H.

11 — Kraus representations

“A quantum channel can be written as a sum over Kraus operators, but that representation is not unique.

For example, consider complete dephasing in a two-mode basis. One representation uses the two basis projectors. Another describes an equal mixture of applying the identity or a phase flip.

Both give exactly the same output density matrix for every input: they preserve populations and erase the off-diagonal coherences.

Choosing a different Kraus basis therefore does not, by itself, define a different channel. Nor can measurements on the output system distinguish these equivalent descriptions.

For the experiment, the task is to justify a physical channel model and its parameters. An interpretable Kraus representation then makes its assumptions and probability accounting explicit.”

Delivery: point to the two operator sets and their shared output. Do not read the full algebra. Appendix E proves representation freedom; Appendix F distinguishes it from different channels agreeing only on measured populations.

12 — Physical loss model

“Here is a concrete construction. Each optical mode has a transmission probability tau j.

The transmission operator multiplies its amplitude by the square root of that probability. The remaining operators send lost events into an orthogonal failure state.

Adding all the operator products gives the identity: transmission plus failure accounts for every input. This proves trace preservation. The Kraus form also ensures complete positivity, including when the input is correlated with another system.

But that mathematical proof does not establish the transmissions of the actual apparatus. They require independent calibration, for example by injecting known modes.

Keeping the failure branch also prevents us from silently discarding lost events and reporting only postselected performance.”

Delivery: identify the transmission and failure terms, then point to tau plus one minus tau. The input here is the one-photon space conditional on the earlier common-survival stage.

13 — Information retention

“With parameter-independent downstream channels, information can only decrease along this sequence. This lets us compare receiver designs using a common source-state QFI.

The two rows use the same nine settings, normalized per photon surviving the common loss stage. Resolving the reference, first-order and failure outcomes retains between 99.68 and 100 percent of the source QFI as classical Fisher information.

With binary reporting and assumed port confusion of 0.35 percent, retention ranges from 0.13 to 57 percent. Both aggregation and confusion contribute to that reduction. Small leakage matters because it transfers light from a bright reference into a very weak signal.

These are conditional model results, not experimental QFI reconstructed from the counts. They translate the information limit into requirements for mode resolution and readout.”

Delivery: identify what the percentages are fractions of. The ranges describe different settings, not uncertainty intervals. Avoid attributing the whole difference to cross-talk alone.

14 — Conclusions

“The thesis connects three aspects of quantum sensing.

Variational methods provide access to spectral information for mixed-state QFI bounds. Thermal preparation can improve sensitivity away from the ground-state optimum in the studied regime. And physically constrained channels connect those information limits to what an experiment can observe.

For SPADE, the next step is resolved outputs and independent calibration, followed by a programmable modal transformation to test the proposed variational protocol.

Thank you.”

Delivery: leave the conclusion visible during questions. Advance to appendix slides only when relevant.

Questions worth preparing:

- **Why not an ellipse?** An ellipse can illustrate a two-parameter information metric, but those directions are parameter changes, not measurement axes. For a contour delta-theta transpose F delta-theta = 1, the longest axis actually corresponds to the smallest eigenvalue of F. Its foci do not identify an optimal measurement. The Bloch example directly varies a measurement for one fixed state family.
- **Why use a mixed qubit?** A full-rank example with Bloch radius 0.8 gives a regular and visible dependence on measurement angle. At the chosen operating point its SLD is 0.8 Z, so the vertical measurement is optimal. The numbers come from exact probabilities, not an illustrative fit.
- **Does the optimal direction depend on the unknown parameter?** Generally yes. This example is local at theta = 0. In practice the measurement may be chosen near a calibrated point or adapted using preliminary estimates.
- **Is QNG the same as Newton's method?** No. Both precondition a gradient, but the QFIM is a state metric and the Hessian is objective curvature. They can be related in special statistical settings, but are not generally interchangeable.
- **Can experiments choose the physically correct Kraus set?** System-only observations determine a channel only with sufficient inputs and measurements, and still do not pick a unique Kraus representation. A particular realization or outcome-resolved instrument requires additional physical information, including environmental or detection records.
- **What has actually been validated with the optical data?** Prediction of held-out 100-repeat setting means under grouped cross-validation. That is separate from identifying the quantum channel. Appendix H contains the metrics.
- **Why does the thermal result respect data processing?** It compares different parameterized preparation families. Partial trace still cannot increase QFI within either family. Appendix D gives the precise statement.

If rehearsal runs long, shorten the PCA comparison, the list of missing observables and the channel-stage descriptions. Preserve the interpretation of the geometric plot, the thermal operating-range result, the distinction between channel validity and physical calibration, and the scope of the final percentages.
