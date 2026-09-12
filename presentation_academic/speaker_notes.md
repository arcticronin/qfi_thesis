12-minute defence — academic version, English

Twelve main slides, followed by four backups for questions. The text leaves room for pauses, pointing to equations and reading plot axes. Rehearse aloud; timings are targets, not a guarantee of delivery speed.

| Slide | Duration | End |
|---|---:|---:|
| 1. Thesis title and collaboration | 0:35 | 0:35 |
| 2. Fisher information and parameter estimation | 0:55 | 1:30 |
| 3. VQSE and principal-component extraction | 1:30 | 3:00 |
| 4. Local metrology in the transverse-field Ising model | 0:55 | 3:55 |
| 5. Thermal preparation and the operating field range | 1:20 | 5:15 |
| 6. Spatial-mode measurements for exoplanet imaging | 0:50 | 6:05 |
| 7. Experimental observations and identifiability | 0:55 | 7:00 |
| 8. Classical probabilities and quantum states | 1:05 | 8:05 |
| 9. A sequential quantum-to-classical model | 1:05 | 9:10 |
| 10. Predictive validation of the calibration model | 1:05 | 10:15 |
| 11. Information retention under restricted readout | 1:10 | 11:25 |
| 12. Conclusions and experimental outlook | 0:35 | 12:00 |

1 — Title and context

“My thesis studies how much information a quantum sensor can provide about an unknown physical parameter, and how much remains available in the measurements we actually record.

This work was developed in collaboration with the Italian Space Agency, within the project Quantum Computers for Space Exploration.

I will connect a computational method for mixed quantum states to two applications: magnetic-field sensing and an optical experiment motivated by exoplanet imaging.”

Delivery: credit the collaboration briefly; let the formal title remain visible without reading every word.

2 — Fisher information

“Each pair of curves represents measurement statistics at two nearby parameter values. On the left, the distributions overlap strongly. On the right, the same small parameter change produces a larger statistical response.

Fisher information quantifies this local sensitivity: how effectively the statistics distinguish nearby values.

Quantum Fisher information, or QFI, is the largest Fisher information available when we optimize over the measurement. It is a benchmark for the state, which a practical detector may or may not attain.

For mixed quantum states, calculating this benchmark becomes expensive as the system grows. This motivates the variational approach.”

Delivery: point to the plots. They are conceptual illustrations, not experimental data.

3 — VQSE and PCA

“The Variational Quantum State Eigensolver, or VQSE, extracts the dominant components of a mixed quantum state. The connection to PCA is useful here.

PCA diagonalizes a covariance matrix. Its eigenvectors give principal directions, and its eigenvalues tell us how much variance each direction carries.

VQSE works with a density matrix, which represents a quantum state. Its eigenvectors describe orthogonal state components, and its eigenvalues are probability weights. The shared idea is spectral compression, although these are different kinds of matrix.

We apply a trainable quantum circuit to repeated copies of the state. The circuit learns a basis rotation that approximately maps the dominant eigenvectors onto known measurement outputs. Their frequencies estimate the eigenvalues. Applying the inverse rotation to an output basis state recovers its corresponding eigenvector.

These retained components enter fidelity-based QFI bounds, reducing the need for full classical diagonalization. A dominant component does not necessarily contain all the sensitivity, so truncation must be assessed.

My contribution is implementing and benchmarking these established algorithms and applying them to sensing problems.”

Delivery: compare the decompositions, then point to the rotation equation. V is a physical circuit. Omit cost functions, gates and optimizer details. Do not claim a demonstrated speedup.

4 — Spin sensor

“The first application is a transverse-field Ising chain. Six interacting spins respond to the magnetic field, but only a four-spin subsystem is accessible to measurement.

Even when the full system is pure, this accessible subsystem can be mixed.

I compare three preparations: the ground state, a depolarized ground state, and a thermal equilibrium state.

Discarding part of the system or applying fixed noise cannot increase QFI. A thermal preparation, however, is a different field-dependent family: both its state components and their populations change with the field.

The relevant comparison is therefore how each accessible preparation responds across the operating range.”

Delivery: point to the retained and discarded spins. Here “local” means access to a subsystem, not independent single-spin measurements.

5 — Thermal preparation

“The horizontal axis is the magnetic field in units of the coupling. The vertical axis is the exact QFI of the accessible subsystem. White is the reduced ground state; teal is the reduced Gibbs state at beta J equal to two.

The thermal state has a lower peak: about 2.61 compared with 3.93. But beyond the ground-state optimum, the teal curve remains higher over the shaded region.

This matters when the environment is not known precisely enough to keep the sensor near its most sensitive field. If plausible fields extend into this region, selecting a preparation solely by its maximum QFI can overlook useful sensitivity elsewhere.

The result does not make the thermal state universally preferable: the choice depends on the expected field range. It shows a trade-off between peak and off-peak performance.

Physically, changes in thermal populations provide an additional source of information. This is an exact finite-system numerical comparison of preparation families.”

Delivery: point first to the lower thermal peak, then to the shaded region. The plot ends at h/J = 2. Do not claim a proven optimum under an unspecified prior, a uniformly better sensor, or that fixed noise increases QFI.

6 — Optical measurement

“The optical application concerns a faint companion beside a bright star. Direct imaging records photon positions, where the two overlapping profiles can be difficult to distinguish.

SPADE, or spatial-mode demultiplexing, instead sorts light into spatial patterns before counting it. With ideal alignment, the bright source mainly occupies the reference mode, while displacement creates a response in other modes.

This connects naturally to representation learning: the choice of basis affects how accessible a weak signal becomes. Here the transformation happens physically, before the data are recorded.”

Delivery: define a mode as a spatial pattern. The sorter does not identify the source of each photon.

7 — Observations and identifiability

“The completed ASI Matera experiment supplied 52,500 count observations across 525 settings, with 100 repetitions per setting.

The initial aim was a truncated-QFI analysis. But the record contained aggregate first-order counts, without separate modal outputs or measurements in additional bases.

Repeating one measurement improves the precision of that statistic. It does not reveal a coherence or eigenvector that the measurement cannot observe.

The data can support prediction of the recorded response and its variability, but not reconstruction of the full quantum state. This motivated a framework that makes the relationship between the physical model and the measured statistics explicit.”

Delivery: frame this as an identifiability result and a reasoned change in research direction.

8 — Classical and quantum descriptions

“To introduce that framework, start with a classical probability vector. Putting its entries on the diagonal gives a valid quantum density matrix with exactly the same outcome probabilities in that basis.

A general quantum state can also contain off-diagonal entries, called coherences. They allow interference when modes are combined. The probability vector alone does not determine these entries.

We must also distinguish states from transformations. A classical channel is a stochastic matrix acting on probabilities. A quantum channel acts on the whole density operator, including populations and coherences.

So this embedding connects the two descriptions. It allows us to extend a classical response model to include coherent physics, while keeping clear which parts are supported by measurements and which require physical assumptions or additional data.”

Delivery: point from the vector to the diagonal, then to c. A probability vector is not itself a quantum channel.

9 — Why the channel model is useful

“The experiment is organized into source preparation, optical propagation and restricted access, measurement, and classical readout.

Before measurement, the quantum description can represent interference, mode mixing and loss while preserving valid probabilities. Measurement then produces a classical probability vector, to which readout and count statistics apply.

There are two practical benefits. First, the stages are modular: independent calibration can constrain or replace individual assumptions. Second, we can compare information before and after each stage and locate where sensitivity is lost.

Loss and failure outcomes remain explicit, so they are not silently absorbed into a normalized signal. The archived counts constrain the final observed response; they do not identify every hidden optical mechanism.”

Delivery: follow the arrows once. This explains the modelling contribution and leads to both prediction and information accounting.

10 — Validation

“The statistical model combines a physical mean response with a positive calibration correction. A Gaussian process captures smooth variation across nearby settings, alongside setting-specific scatter.

I assessed prediction with grouped five-fold validation: interleaved cells, complete distance rows, and complete source-ratio columns were held out. All model parameters were refitted within each training fold.

The nominal 95 percent intervals covered approximately 94 percent of held-out means across the three splits. Standardized residuals also had a spread close to one.

This provides evidence for prediction and uncertainty estimates for the mean of 100 repeated counts. That is the validated target; it does not establish a complete quantum-channel reconstruction.”

Delivery: explain grouped splits; let the cards carry the percentages. Avoid calling coverage “accuracy.”

11 — Information retention

“The quantum model also supports a conditional comparison of receivers. These results use the same nine settings and are normalized per photon surviving the common loss stage.

An ideal receiver resolving the reference mode, the first-order mode and the complement retains between 99.68 and 100 percent of the source-state QFI as classical Fisher information.

With binary reporting and assumed symmetric port confusion of 0.35 percent, retention ranges from 0.13 to 57 percent.

Small leakage can matter because the reference port is bright and the displacement-sensitive signal is extremely weak near alignment. Both aggregation and confusion contribute to the difference.

These are conditional model results, not QFI reconstructed from the archived counts. They show how the channel description turns an abstract information limit into concrete requirements for modal resolution and readout.”

Delivery: emphasize the common normalization. Ranges describe settings, not confidence intervals.

12 — Conclusions

“The thesis connects three contributions: implementation of variational tools for mixed-state QFI bounds; a preparation comparison showing higher thermal sensitivity away from the ground-state optimum; and a sequential experimental model with validated count prediction and explicit inference limits.

The next step is a new acquisition with resolved outputs, independent calibration and a programmable optical basis, enabling a test of the proposed VQ-SPADE protocol.

Thank you.”

Delivery: finish by 12:00 and leave this slide visible during questions.

Questions to prepare:

- **Is VQSE quantum PCA?** It shares spectral extraction with PCA. It learns a physical basis rotation for a density matrix, whose eigenvalues are mixture weights rather than variances. It is not PCA on the count table.
- **Why does spectral truncation help?** It reduces the state information needed for fidelity bounds. The validity and tightness of those bounds still matter; low-weight components can have high parameter sensitivity. Backup A distinguishes finite-displacement bounds from exact local QFI.
- **Why beta J = 2?** It illustrates a trade-off that a peak-only comparison misses: a lower maximum but higher off-peak QFI over part of the displayed range. It is not an optimized temperature for every possible field distribution.
- **Have you proved better performance in an unknown environment?** The curves show higher local QFI in a specified region. Choosing a preparation for an uncertain field requires an operating range or prior and an appropriate decision criterion; no universal Bayesian or minimax optimum is claimed.
- **Why can temperature help despite data processing?** The preparations are different parameterized families. Partial trace still decreases or preserves QFI within each family. See backup B.
- **Can a classical channel be embedded in a quantum channel?** Yes. For a column-stochastic matrix R, one valid embedding is E_R(rho) = sum over i,j of R_ji times rho_ii times |j><j|. It measures the input basis and prepares an output basis state. It reproduces R on diagonal states but erases coherences; other physical models can have different coherence dynamics. The classical response does not identify a unique quantum channel.
- **Why use a quantum model if the data are classical?** Physical propagation may involve coherences and interference. A quantum forward model provides physically constrained information checkpoints; the classical likelihood describes what the detector records. Assumed coherences are not treated as reconstructed quantities.
- **Why a GP?** Smooth calibration over a small structured setting grid, with predictive uncertainty. The evidence is held-out mean performance, not a claim that GPs are uniquely optimal. Backup C has full metrics.
- **Was a quantum advantage demonstrated?** No general computational speedup is established. The variational methods were implemented and benchmarked; the thermal curves use exact small-system calculations.
- **Was VQ-SPADE implemented?** It is a proposal. Resolved outputs, programmable coherent transformations, overlap measurements and independent calibration would be required. See backup D.

If rehearsal runs long, shorten the spin preparation descriptions, the missing-observables list and the GP explanation. Preserve the PCA distinction, thermal trade-off, channel motivation, validation target and conclusion.
