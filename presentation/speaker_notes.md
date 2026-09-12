12-minute defence — English speaking script

The 11 main slides are timed to 12 minutes including short pauses. The script is deliberately shorter than a continuous 12-minute monologue: use the remaining time to point to diagrams, read axes, and let each result land. Rehearse aloud at a comfortable pace; do not fill the pauses by adding more technical detail. The four backup slides are for questions only.

| Slide | Time | Cumulative end | Purpose |
|---|---:|---:|---|
| 1. Learning what a quantum sensor can reveal | 0:35 | 0:35 | Establish the question |
| 2. Can we distinguish two nearby worlds? | 1:05 | 1:40 | Explain information intuitively |
| 3. Learn the dominant components | 1:20 | 3:00 | Connect variational quantum estimation to ML |
| 4. A sensor is more than its purest state | 1:05 | 4:05 | Set up the controlled comparison |
| 5. Thermal preparation can be more informative | 1:25 | 5:30 | Deliver the first result |
| 6. The measurement decides what becomes visible | 0:55 | 6:25 | Introduce the optical application |
| 7. Many observations. An incomplete view. | 1:05 | 7:30 | Explain the experimental turning point |
| 8. Connect the physics to the recorded data | 1:05 | 8:35 | Present the modelling contribution |
| 9. Physics + calibration predicts unseen settings | 1:10 | 9:45 | Deliver the second result |
| 10. Readout can erase the theoretical advantage | 1:15 | 11:00 | Translate theory into receiver design |
| 11. Useful sensing is an end-to-end problem | 1:00 | 12:00 | Connect the contributions and close |

1 — Opening

“Imagine that a magnetic field changes very slightly, or that a faint planet moves slightly relative to its star. Can our measurements tell the difference?

My thesis studies this question at two levels: how to calculate the information available in a quantum sensor, and how much of that information remains accessible in a practical experiment.

I implemented variational tools for the first problem, then applied this perspective to a spin sensor and an optical experiment with data supplied by ASI Matera.”

Delivery: leave the title visible while you establish the question. Do not read out the formal thesis title, supervisors, or institutional details.

2 — Information as distinguishability

“For this talk, we can understand information through these two pictures. Each curve represents the outcome statistics for one of two nearby parameter values.

On the left, changing the parameter barely changes the distribution. The two situations are difficult to distinguish. On the right, the same small parameter change produces a larger statistical response.

Fisher information quantifies this local sensitivity. Quantum Fisher information asks a further question: what is the largest information we could extract if we were free to choose the measurement?

It gives us a benchmark for the state. But a practical detector does not automatically reach that benchmark. And for mixed states, even calculating it can be expensive.”

Delivery: gesture left, then right. These curves are an illustration, not a fitted dataset. Pause after the plain-language QFI definition.

3 — The learning loop

“The computational problem grows quickly. An n-qubit density matrix has two-to-the-n rows and columns, and dense diagonalization scales exponentially.

The approach I implemented uses the Variational Quantum State Eigensolver, or VQSE. Think of it as learning a useful basis. We prepare copies of a mixed state, apply a trainable quantum circuit, and measure the outcome frequencies. A classical optimizer adjusts the circuit to minimize a weighted cost.

At the ideal optimum, this rotation brings the dominant eigenvectors onto known measurement outputs. Their frequencies reveal the corresponding eigenvalues.

This is related to principal-component extraction, although the rotation is a physical operation on the quantum state. The extracted components enter a variational pipeline for fidelity-based QFI bounds.

My contribution here is implementing and benchmarking these established methods, then examining what they tell us about a sensor.”

Delivery: follow the loop with your pointer. Explain the role of the method rather than enumerating circuit gates. Do not imply that you invented VQSE or proved a computational speedup.

4 — Controlled spin sensor

“To study the physical consequences, I used a finite spin chain as a controlled magnetometer. The spins interact with their neighbours, and their state depends on the magnetic field we want to estimate.

In this comparison there are six spins, but the observer can measure only four. So even a pure state of the full system can look mixed to the observer.

I compared three preparation families: the ground state, a ground state affected by depolarizing noise, and a thermal equilibrium state.

For a fixed noise channel, information cannot increase. But a thermal preparation is a different field-dependent state family. That distinction makes the comparison interesting: the purest global preparation does not have to give the most informative accessible state.”

Delivery: point to the four filled nodes and two outlined nodes. “Local” means access to the four-spin subsystem, not a restriction to independent single-spin measurements.

5 — Thermal result

“Here is the central numerical result. The horizontal axis is the magnetic field and the vertical axis is the exact local QFI. White is the reduced ground-state family. Teal is a fixed-temperature thermal preparation.

In this six-spin periodic system, the thermal preparation has a peak local QFI 23.5 percent higher. It also exceeds the ground-state preparation at 40 of the 60 sampled fields. The shaded region marks where it is more informative.

Why can this happen? Changing the field changes the energy levels and therefore their thermal populations. Those population changes carry information as well as the changes in the eigenvectors.

This is not a statement that noise generally helps. We are comparing different preparations in a finite system. The design lesson is that preparation should be chosen for the operating regime, rather than judged only by purity or by a single ideal peak.”

Delivery: read the axes before quoting either number. Let the result sit for a moment. The curves use exact SLD calculations, not experimental estimates from variational hardware.

6 — From magnetic sensing to optical sensing

“The second application asks how to extract a faint planet's spatial signal beside a bright star.

Direct imaging records where photons arrive. When the images strongly overlap, the planet causes only a small deformation of the bright profile.

SPADE, or spatial-mode demultiplexing, changes the measurement. It sorts the field into spatial patterns before counting photons. With ideal alignment, the star mainly occupies the reference mode, while displacement contributes to other modes.

The key idea is familiar from representation learning: choose a representation in which the weak signal is easier to access. Here that choice happens physically, before the recorded data exist.”

Delivery: define a mode as a spatial pattern. The two output labels indicate dominant response roles; SPADE does not identify the source of every individual photon.

7 — The experimental turning point

“The collaboration supplied 52,500 counts: 525 experimental settings, each repeated 100 times. Initially, I wanted to use the available low-order modes for truncated-QFI analysis.

But the experiment had already ended. The archived record contained only aggregate first-order counts. It did not include the separate modal outputs or the additional measurement bases needed to recover the state's spectral structure.

This exposed an important distinction. More repetitions make an observed statistic more precise, but they do not create an observable that was never measured.

The dataset could support prediction of the recorded response. It could not support reconstruction of the full quantum state. That changed the question: what can we infer reliably, and what should a future experiment record?”

Delivery: present this as a reasoned research decision. Avoid spending the minute apologizing for the data. The inference limit motivates the next contribution.

8 — Model the observation process

“I organized the experiment into a sequence. Source preparation is followed by optical channels, restricted access, a measurement, and finally classical readout and count statistics.

Before measurement, the model describes a quantum state, including its populations and coherences. After measurement, it describes probabilities and recorded counts.

This structure matters because different mechanisms can produce similar observed effects. For example, a baseline can combine optical leakage and background. A successful fit does not uniquely identify their physical origins.

The framework keeps physical constraints explicit, including probability lost into failure outcomes, while allowing a learned correction for calibration. As new calibration becomes available, individual stages can be replaced without rebuilding the entire analysis.”

Delivery: the four displayed boxes group the longer thesis sequence. Keep the explanation at the level of what each group does; do not introduce Kraus or Choi representations.

9 — Predictive validation

“For the setting means, the statistical model combines the expected physical response with a positive calibration correction. A Gaussian process captures smooth variation across nearby settings, with an additional term for setting-specific scatter.

I tested prediction using grouped five-fold cross-validation. The held-out groups were interleaved cells, complete distance rows, and complete source-ratio columns. Model parameters were refitted on the training portion of each fold.

The nominal 95 percent prediction intervals covered approximately 94 percent of the held-out means across these splits. The standardized residual spread was also close to one.

This supports prediction and uncertainty estimates for the mean of 100 repetitions. It does not validate a complete distribution for every individual count, and it does not identify the hidden quantum channel.”

Delivery: say “approximately 94 percent,” then let the three cards show the detail. Do not read all nine numbers from the backup table. Grouped validation is the part most likely to resonate with this commission.

10 — The receiver changes the answer

“The quantum model also lets us compare information at different checkpoints. Here both comparisons use the same nine test settings, normalized per photon surviving the common loss stage.

An ideal low-mode receiver that records the reference mode, the first-order mode and the complement keeps between 99.68 and 100 percent of the source-state QFI as classical information.

With binary reporting and an assumed symmetric cross-talk model, the retained information ranges from only 0.13 to 57 percent. These are ranges across settings, not confidence intervals.

Why such a large effect from a small confusion probability? The useful first-order signal is extremely weak near alignment. Leakage from the bright reference port can compete with it.

These are conditional theoretical results, not QFI reconstructed from the counts. They show why receiver design and readout must be included when assessing a sensor.”

Delivery: emphasize the common grid and the theoretical status briefly, then explain the mechanism. Both coarse reporting and confusion contribute to the difference; do not claim the whole drop is isolated cross-talk loss.

11 — Closing

“The thesis connects three decisions that are often considered separately.

First, learn a compact state representation so that mixed-state information can be bounded through a variational procedure.

Second, choose preparation for the actual sensing task. In the finite spin system, thermal populations can improve accessible sensitivity.

Third, model and validate the observation process. The optical data support predictive calibration, while also showing exactly which state information is missing.

The next step is a new acquisition with resolved optical outputs, independent calibration, and a programmable mode transformation to test the proposed optical variational protocol.

The useful sensor is the complete path from the physical parameter to the evidence we can actually collect. Thank you.”

Delivery: leave this slide on screen for questions. Do not advance into the backup material automatically.

Likely commission questions and concise answers:

- **What is specifically your contribution?** Implementation and benchmarking of established variational spectral/QFI tools; finite-system analysis of accessible sensitivity under different preparations; analysis of the available optical counts; and the sequential framework connecting physical assumptions to observable statistics. VQ-SPADE is a proposal, not a completed experiment.
- **Is VQSE just PCA?** It shares the goal of extracting dominant spectral components, but operates on copies of a quantum state through a trainable physical basis rotation. A dominant component does not automatically carry all the parameter sensitivity; the approximation must be assessed.
- **Did you demonstrate quantum advantage?** No general computational advantage or hardware speedup is established here. The work implements and evaluates a route to variational bounds, with exact small-system references.
- **Was the thermal result obtained on a quantum computer?** It is an exact finite-system numerical result. Distinguish the circuit implementations from the ground-state and Gibbs benchmarks used for this physical claim.
- **Why not let a neural network infer the entire state?** Any estimator needs an identifiable forward model and sufficient observations. More expressive modelling cannot supply missing measured information without introducing assumptions or prior information. A predictive model may work while several latent physical mechanisms remain compatible with the data.
- **Why a GP?** It supplies a smooth, uncertainty-aware correction across a small structured setting grid while retaining the known physical response. The evidence presented is grouped held-out performance, not a claim that GPs are uniquely optimal.
- **Does roughly 94% coverage prove the model correct?** It is evidence for predictive calibration of the specified setting means under these splits. It is not proof of the complete count distribution or of the underlying optical mechanism.
- **Can the experiment identify absolute efficiency?** Not from the existing stream. Incident flux and coupling are not independently recorded. The reported throughput is conditional on the model and normalization conventions.
- **Why can temperature help if information decreases under noise?** The compared Gibbs states are a different parameterized preparation family. Within each family, tracing out spins still cannot increase QFI.
- **What would you measure next?** Resolved modal outputs, flux, background, failure outcomes and measurements in additional coherent bases; then a programmable modal rotation and overlap measurements for VQ-SPADE.

If rehearsal runs long, save approximately 45 seconds by shortening the PCA analogy on slide 3, the list of missing observables on slide 7, and the explanation of GP scatter on slide 9. Preserve the axes and scope of the thermal result, the held-out validation target, and the final conclusion.
