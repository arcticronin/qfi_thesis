# Thesis defence — 15-minute speaking script

**Luca Manzi · English · presentation_4 · 19 main slides**

Read only the **Spoken script** sections aloud. Bracketed directions are silent cues. **Details to keep in mind** are preparation for questions, not additional material for the timed talk. The spoken text is approximately 1,730 words. Timings include pointing, slide changes and short pauses; rehearse aloud to calibrate them to your pace. Do not read the equations in the technical notes symbol by symbol.

This script follows the current main deck and the agreed story for slide 14. **Slide 14 still contains the HG-mode image in `main.tex`; the script assumes the planned copy of slide 6, used as a pipeline callback.** No slide source has been changed for this script.

The central thread is: **a sensor must retain useful sensitivity through preparation, restricted access and measurement, over the range where it will operate.**

## Timing map

| Slide | Topic | Duration | Clock |
|---|---|---:|---|
| 1 | Opening | 0:30 | 0:00–0:30 |
| 2 | Classical Fisher information | 0:50 | 0:30–1:20 |
| 3 | Measurement animation and QFI | 1:00 | 1:20–2:20 |
| 4 | Mixed states and spectral estimation | 1:05 | 2:20–3:25 |
| 5 | Two applications | 0:30 | 3:25–3:55 |
| 6 | Numerical and circuit pipeline | 1:05 | 3:55–5:00 |
| 7 | Magnetometry divider | 0:05 | 5:00–5:05 |
| 8 | Magnetometer model | 0:55 | 5:05–6:00 |
| 9 | Broader thermal sensitivity | 1:00 | 6:00–7:00 |
| 10 | Stronger thermal peak | 0:55 | 7:00–7:55 |
| 11 | Exoplanet divider | 0:05 | 7:55–8:00 |
| 12 | Imaging problem and SPADE | 0:55 | 8:00–8:55 |
| 13 | Mode probabilities and cross-talk | 0:55 | 8:55–9:50 |
| 14 | Initial analogy and VQ-SPADE proposal | 0:40 | 9:50–10:30 |
| 15 | Why quantum and classical channels | 1:05 | 10:30–11:35 |
| 16 | Available data | 0:40 | 11:35–12:15 |
| 17 | Constructed channel model | 0:55 | 12:15–13:10 |
| 18 | Mean-response result and implications | 1:00 | 13:10–14:10 |
| 19 | Conclusions | 0:50 | 14:10–15:00 |

## Slide 1 — Opening

### Spoken script

Good morning. My thesis studies how to assess the sensitivity of quantum sensors when we include the conditions under which they actually operate.

The work was developed in collaboration with the Italian Space Agency. I will connect two applications: a quantum magnetometer and an optical experiment motivated by exoplanet detection.

The common question is: how much information about an unknown parameter can we actually access?

### Details to keep in mind

- The magnetometer is a numerical model and a circuit-method benchmark. The optical application uses a completed laboratory experiment motivated by exoplanet imaging; it is not an astronomical detection of a real exoplanet.
- Your contribution combines implementations, numerical studies, data interpretation and a future proposal. These have different evidential status throughout the talk.

## Slide 2 — Classical Fisher information

### Spoken script

Before discussing quantum sensors, consider an ordinary measurement.

[Point to the probability distributions.]

An unknown parameter, such as a magnetic field, determines the distribution of possible outcomes. If changing the parameter barely changes that distribution, the measurement tells us very little. If a small change produces a distinguishable response, estimation becomes easier.

Fisher information quantifies this local sensitivity. It compares the change in the outcome probabilities with their statistical fluctuations.

So it is not simply a measure of how large the signal is. A bright but almost constant signal can be less informative than a weaker signal that responds strongly to the parameter.

### Details to keep in mind

For a fixed measurement with probabilities (p(x\mid\theta)),

\[
F_C(\theta)=\sum_x\frac{[\partial_\theta p(x\mid\theta)]^2}{p(x\mid\theta)}.
\]

The classical Cramér–Rao bound is (\operatorname{Var}(\hat\theta)\geq 1/[N F_C(\theta)]) for (N) independent repetitions and an appropriate locally unbiased estimator, under regularity assumptions. Large Fisher information is a precision benchmark, not a guarantee that an arbitrary finite-sample estimator attains the bound. “Local” means around a parameter value; it does not establish global identifiability.

Source: [MathBackground.tex](../TeXtured/chapters/MathBackground.tex).

## Slide 3 — Fisher information and measurements

### Spoken script

A quantum state can contain information that a particular measurement fails to reveal.

[Start at zero degrees. Point to the two coloured vectors.]

These vectors illustrate states at two parameter values. Keep the states fixed, and rotate only the measurement basis.

[Advance through thirty and forty-five degrees.]

The classical Fisher information changes because the measurement probes the state differently.

[Advance through sixty and seventy-five degrees.]

Some bases are more responsive to the parameter variation than others.

[Advance to ninety degrees. Pause at the meeting of the curves.]

Here, the measurement reaches the quantum Fisher information, or QFI: the best local sensitivity available from the state over all measurements.

The state has not become more informative. We have become better at reading the information it already contains. That distinction will matter again in the optical experiment.

### Details to keep in mind

The current animation uses **mixed states**, with Bloch radius (r=0.8), and evaluates Fisher information locally at (\theta=0). For the illustrated equatorial family,

\[
\rho_\theta=\tfrac12[I+r(\cos\theta\,\sigma_x+\sin\theta\,\sigma_y)],
\qquad
F_Q=r^2=0.64,
\]

\[
F_C(\varphi)=\frac{r^2\sin^2\varphi}{1-r^2\cos^2\varphi}.
\]

- The two vectors have a visible finite separation for illustration. The plotted information is **not** computed as their finite difference.
- At the initial basis, probabilities have zero first derivative at the reference point. They can still change at second order over a finite displacement.
- For this pure-state limit, generic equatorial projective bases attain the same QFI; the mixed-state choice makes the measurement dependence visible. Singular zero-probability settings require care with limits.
- The optimal basis can depend on the unknown parameter. Local attainability does not imply one globally optimal, immediately known measurement.

Reference: Appendix J of the deck and [measurement_overlay.tex](assets/measurement_overlay.tex).

## Slide 4 — How we deal with mixed states

### Spoken script

What are mixed states? They describe statistical mixtures of quantum states, using a density matrix.

Why study them? Real sensors interact with their environment, and we may observe only part of the probe. Mixed-state sensitivity is therefore important, but computing it exactly becomes expensive as the system grows.

[Point to the truncated density matrix.]

Our approach keeps the dominant eigencomponents instead of treating the entire spectrum in equal detail.

VQSE, the Variational Quantum State Eigensolver, learns a change of basis that exposes the leading eigenvalues and allows their eigenvectors to be prepared.

These components then enter TQFI, Truncated Quantum Fisher Information, through fidelity-based bounds. Intuitively, we compare nearby states using a compact spectral description to estimate how distinguishable they are.

### Details to keep in mind

\[
\rho_m=\sum_{i=1}^{m}\lambda_i|v_i\rangle\langle v_i|,
\qquad \lambda_1\geq\cdots\geq\lambda_d.
\]

- A mixed state need not represent ignorance about a unique underlying ensemble: ensemble decompositions are nonunique. Entanglement with an unobserved system also produces a mixed reduced state.
- **Truncation is a chosen computational strategy, not a requirement for describing mixed states.** The matrix above is generally subnormalized: ($\operatorname{Tr}\rho_m\leq1$). Renormalizing it would change the quantities entering the stated bounds.
- Large eigenvalue weight does not automatically mean that all parameter sensitivity is retained. Dependence of both eigenvalues and eigenvectors matters.
- The thesis treats truncated-fidelity and generalized-fidelity bounds at finite displacement; their local-QFI interpretation requires the appropriate small-displacement limit. TQFI is not simply “calculate ordinary QFI after deleting small eigenvalues.” Use Appendix A if challenged.
- VQSE changes the measurement basis, not the input state's eigenvalues. Its numerical outputs are approximate and depend on ansatz expressivity, optimization and sampling. The established method is from the literature; your contribution is its implementation, benchmarking and integration.
- The introduction calls mixed-state QFI less explored. Do not turn that into “nobody has studied mixed states.”

Sources: [Methods.tex](../TeXtured/chapters/Methods.tex), [VQSE.tex](../TeXtured/chapters/VQSE.tex).

## Slide 5 — Applications

### Spoken script

I used these ideas in two complementary settings.

The magnetometer provides a controlled model: I can vary preparation, noise and access, and compare the resulting sensitivities.

The optical experiment asks a different question: given a real measurement record, which parts of the sensing process can we reconstruct or meaningfully model?

Both start from the same distinction between information in a state and information in recorded outcomes.

### Details to keep in mind

The two applications do not both demonstrate experimental TQFI. The numerical study benchmarks metrological quantities; the archived optical counts do not reconstruct an optical state or its TQFI. Presenting this asymmetry explicitly strengthens the scientific story.

## Slide 6 — Parallel numerical and quantum-circuit workflow

### Spoken script

This is the computational structure I developed.

[Follow the upper row from left to right.]

Numerically, I prepare the parameter-dependent state, restrict access to the sensor, and calculate its spectrum. This gives an exact reference within the chosen finite model.

[Follow the lower row.]

The circuit formulation represents preparation and evolution through gates. Leaving the environment unobserved reproduces the accessible subsystem statistics. VQSE then provides a variational route to the dominant spectral components.

The two routes meet at the information calculation, where I can compare exact QFI with the truncated bounds.

The practical advantage is modularity: I can replace an implementation of one stage while keeping its physical meaning and interfaces fixed. This lets me check whether a discrepancy comes from the model, restricted access, or a numerical or variational approximation.

### Details to keep in mind

- Partial trace obeys ($\rho_S=\operatorname{Tr}_E\rho_{SE}$). Marginal measurement statistics on (S) agree whether (E) is traced out mathematically or simply unobserved. Conditioning on an outcome in (E) is a different operation.
- Interchangeable implementations do **not** imply interchangeable stage order; channels generally do not commute.
- Exact matrix calculations, Trotterized dynamics and variational spectral estimation have different approximation errors. “Validated against numerical references” is more defensible than an unconditional “perfectly matching.”
- Unitary evolution of a pure state does not prepare a global Gibbs state. The dynamical circuit example and the ground/Gibbs preparation branches are distinct.
- Do not claim a demonstrated hardware quantum advantage. This establishes and benchmarks a route to variational estimation.

Source: [Methods.tex](../TeXtured/chapters/Methods.tex).

## Slide 7 — Quantum Magnetometry

### Spoken script

Let me first show what this framework tells us about a quantum magnetometer.

### Details to keep in mind

This is a transition slide. Advance immediately after the sentence.

## Slide 8 — A noisy quantum magnetometer

### Spoken script

The probe is an interacting spin chain described by the transverse-field Ising model. The magnetic field we want to estimate changes its quantum state.

[Point to the six sites, then the two dashed sites.]

In this example there are six spins, but only four are accessible. The other two are traced out, so even a pure global preparation can give a mixed accessible state.

I compare ground-state preparation, thermal preparation and a depolarizing-noise baseline. I also study how access and boundary conditions affect the response.

The question is not just which preparation gives the highest peak. It is which gives useful sensitivity in the field range where the sensor must operate.

### Details to keep in mind

The plotted examples use (N=6), (n=4), periodic boundaries and (J=1). The general methods chapter also discusses open chains; do not mix their Hamiltonian summation limits with this ring.

For a fixed, parameter-independent partial trace or noise channel, QFI cannot increase. More accessible qubits can recover information hidden in the larger probe. However, changing the **preparation family** is not an application of that same data-processing comparison.

This is a finite model: say “sensitivity peak” or “near the critical region,” not a true finite-system thermodynamic singularity. Here “local QFI” may also refer to the accessible subsystem; distinguish that from locality in the estimated parameter when answering questions.

Source: [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex).

## Slide 9 — Temperature broadens the useful range

### Spoken script

Here, white is the reduced ground-state reference and green is the reduced thermal preparation at inverse temperature beta equal to two.

[Point first to the white maximum, then to the shaded region on the right.]

The thermal state does not win at the highest ground-state peak. Its advantage appears away from that optimum, where the green curve remains above the white curve.

Imagine that the field is not known well enough to place the sensor exactly at its best operating point. A narrow, high peak may be less useful than a response that remains informative across the relevant interval.

Temperature therefore becomes a preparation control: it changes where useful sensitivity is available, rather than simply increasing or decreasing one maximum.

### Details to keep in mind

- ($\beta=1/(k_B T)$): larger beta means lower temperature. Plot labels use ($\beta J$); the numerical convention is ($J=1$).
- The global Gibbs state ($e^{-\beta H(h_x)}/Z(h_x)$) is prepared **before** tracing out two spins. It is not generally the Gibbs state of the isolated four-spin Hamiltonian.
- The shaded region marks pointwise higher QFI in this example. You did not establish a globally optimal Bayesian or minimax preparation for an arbitrary prior over fields. “Useful when the field is uncertain” is a design interpretation of the curves, not a completed prior-weighted optimization.
- Thermal populations depend on the field; this can supply information in addition to changes of eigenvectors. This is not evidence that arbitrary heating or parameter-independent noise improves QFI.

Sources: [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex), [NoiseAnalysisAppendix.tex](../TeXtured/chapters/NoiseAnalysisAppendix.tex).

## Slide 10 — Cooling strengthens the peak

### Spoken script

Now I lower the temperature, increasing beta to five.

[Point to the green peak.]

For this preparation and accessible subsystem, the thermal peak is also higher than the reduced ground-state peak.

The intuition is that low-energy excited states are not necessarily useless background. Their populations change with the magnetic field, and that change can carry information.

Together, these plots show two possible benefits: broader sensitivity away from the ground-state optimum, or stronger sensitivity around a favourable operating region.

This is not a universal claim that mixed states are better. It shows why preparation must be evaluated against the intended sensing task, rather than judged only by purity or by proximity to the ground state.

### Details to keep in mind

For the reported (N=6,n=4,\beta=5) periodic example, the thesis gives a 23.5% higher peak. Keep this as a question-answer detail; the main slide deliberately avoids large numerical callouts.

The comparison is between the **reduced ground-state family** and the **reduced globally thermal family**. Both accessible states can be mixed. The field derivative acts on the field-dependent Gibbs preparation, including its populations. No fixed noisy processing of the same ground-state family is claimed to increase QFI. The preparation resources and equilibration time are not optimized by these plots.

## Slide 11 — Exoplanet Detection

### Spoken script

The second application moves from a controlled sensor model to an optical experiment.

### Details to keep in mind

Change pace slightly; this is the start of the second application, not a new mathematical introduction.

## Slide 12 — The exoplanet problem

### Spoken script

A faint companion close to a bright star is difficult to resolve because their images overlap.

[Point from the resolved image to the unresolved image.]

Direct imaging records photon positions. But position is only one possible measurement of the optical field.

SPADE, spatial-mode demultiplexing, instead sorts light into spatial modes. With the sorter aligned to the star, the bright reference mainly occupies the fundamental mode, while the displaced companion contributes to higher modes.

This makes the separation-sensitive component easier to access, even when two intensity peaks are not visibly resolved.

It is the same principle as the earlier measurement animation: changing the measurement can reveal information that another basis reads poorly.

### Details to keep in mind

SPADE does not defeat all diffraction limits or identify the source of each photon. Its advantage is parameter- and model-dependent measurement sensitivity. Alignment, brightness ratio, throughput, background and readout matter.

Mutual incoherence of star and companion does not mean that their spatial density matrix is diagonal in an arbitrary HG basis. An individual displaced source occupies a coherent superposition of HG modes; an incoherent source mixture can retain off-diagonal entries in that basis.

Sources: [Astrophysical.tex](../TeXtured/chapters/Astrophysical.tex), [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex).

## Slide 13 — SPADE modes and readout cross-talk

### Spoken script

[Point to the fundamental mode, then the two first-order modes.]

I call the probability of the fundamental outcome p-zero. It is dominated by the aligned star. P-one is the combined probability of the two first-order outcomes, which carry the separation-sensitive signal.

These are mode labels, not labels telling us which source emitted a photon.

Now introduce chi: the probability of confusing the two reported ports in a symmetric readout model.

The observed first-order probability contains both correctly reported first-order events and leaked fundamental-port events.

Because the star is much brighter, even a small confusion probability can contaminate the weak signal. This is why a realistic analysis must include the detector, not just the ideal optical measurement.

### Details to keep in mind

For ideal mode outcomes,

\[
p_0=\operatorname{Tr}(M_0\rho),\qquad
p_1=\operatorname{Tr}(M_1\rho),
\]

\[
M_0=|HG_{00}\rangle\langle HG_{00}|,\qquad
M_1=|HG_{01}\rangle\langle HG_{01}|+|HG_{10}\rangle\langle HG_{10}|.
\]

The symmetric readout assumption gives

\[
p_1^{\rm rep}=\chi p_0+(1-\chi)p_1.
\]

- The companion also contributes to (HG_{00}). Neither port exclusively identifies photon origin.
- Higher modes and loss require an additional outcome; generally (p_0+p_1\neq1) unless a binary normalization/conditioning convention has explicitly been imposed.
- Chi here is **classical reported-port confusion**, not coherent amplitude mixing. The latter requires a pre-measurement optical model.
- The thesis takes 0.0035 from an external reported cross-talk calibration. Equal reverse leakage and an unaffected failure outcome are assumptions, not a fully measured transfer matrix.
- A fixed classical post-processing channel can reduce CFI but does not change the pre-measurement state's QFI.

## Slide 14 — Returning to the pipeline: a limitation and a proposal

### Spoken script

[On the planned copy of slide six, point to access, then spectrum.]

Initially, we considered SPADE as a way to access selected components of the optical state within this pipeline.

But there is a crucial distinction: mode populations are not generally eigenvalues. The state need not be diagonal in the Hermite–Gaussian basis.

This motivated VQ-SPADE: a proposed trainable mode rotation before detection, aiming to learn an eigenbasis and make the populations usable for spectral estimation.

That is a future proposal. For the existing experiment, I instead model the optical transformations and the recorded outcomes explicitly.

### Details to keep in mind

**The crucial correction is that SPADE gives access to mode populations, not necessarily eigenvalues:**

\[
p_j=\langle HG_j|\rho|HG_j\rangle.
\]

When the measurement basis diagonalizes the state, individually resolved populations coincide with eigenvalues. Aggregating two modes, as in (p_1), gives a **sum** even in that case.

Also, observing selected modes is a projection/coarse-graining operation; it is not generally the partial trace used in the magnetometer. Tensor-factor access and restriction to a modal subspace are different mathematical constructions.

In the proposed extension,

\[
p_j(\boldsymbol\alpha)
=\langle HG_j|U(\boldsymbol\alpha)\rho U^\dagger(\boldsymbol\alpha)|HG_j\rangle.
\]

The trainable optical transformation would learn the basis; **SPADE performs the readout**. This would need sufficient mode resolution, controllable transformations, repeated state preparations and calibration of mode-dependent losses. A simple rotation plus the current aggregate record is not already an eigensolver. VQ-SPADE was not implemented or tested.

Source: [Conclusions.tex](../TeXtured/chapters/Conclusions.tex), deck Appendix I.

## Slide 15 — Why quantum and classical channels?

### Spoken script

A classical channel transforms a probability distribution. Readout confusion is an example: it changes how outcomes are reported.

[Point to the diagonal matrix.]

We can represent a probability vector as a diagonal density matrix. That lets classical statistics sit within the same mathematical language.

[Point to the off-diagonal entries.]

But optical transformations can also act on coherence: the phase relationships between modes. A probability vector alone cannot describe those effects.

The quantum-channel model therefore follows the state before measurement, while classical channels describe the later readout.

The benefit is a physically organized model. We can separate loss, coherent mixing and reporting errors, and ask at which stage information becomes inaccessible. We do not infer quantum coherence merely by writing probabilities in a matrix.

### Details to keep in mind

- The diagonal embedding is a valid construction, not quantum-state reconstruction. A stochastic map does not uniquely fix how a quantum extension acts on off-diagonal elements.
- The two-by-two slide is a **conceptual illustration**. Actual ($HG_{01}/HG_{10}$) aggregation, higher modes and loss require additional structure. Do not silently identify a two-dimensional pure optical basis with one fundamental mode plus an unresolved two-mode sector.
- Coherent mixing before measurement and classical label confusion after measurement can produce similar changes in populations, but differ on coherent inputs and in their physical position in the sequence.
- For a parameter-independent channel, QFI is nonincreasing. A parameter-encoding channel can introduce sensitivity; the data-processing statement does not prohibit that.

Sources: [MathBackground.tex](../TeXtured/chapters/MathBackground.tex), [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex).

## Slide 16 — What the experiment recorded

### Spoken script

The completed ASI Matera experiment provides repeated photon counts over a grid of separations and relative source intensities.

[Point to the individual acquisition, then the averaged map.]

Averaging reveals a clear response, but the archive contains only the aggregate first-order stream.

We do not have separate modal outputs, measurements in other bases, or all the flux and failure information needed to reconstruct the optical state.

So the question becomes more specific: can a physically structured model explain the observed mean response, and tell us what a future experiment should measure?

### Details to keep in mind

The record has 525 settings, 100 repetitions per setting and 10 ms per exposure: 52,500 observations, not necessarily 52,500 photons. Separate ($HG_{00}$), ($HG_{01}$), ($HG_{10}$), higher-mode and loss records are absent.

Without an independent incident-flux calibration, count scale does not separate flux from efficiency. Without basis rotations or phase-sensitive observables, the record does not identify HG coherences. Repetition improves knowledge of the measured mean but does not add a new kind of observable.

## Slide 17 — From physical assumptions to predicted counts

### Spoken script

[Trace the pipeline once.]

I start with a source state, apply optical channels, model the SPADE measurement, and then include readout and classical calibration to predict counts.

For the optical stages, I chose physically motivated models for effects such as loss, dephasing and mode mixing, represented through valid Kraus operators.

These choices are assumptions that we can replace and test. They are not optical parameters reconstructed from this dataset.

The recorded counts instead constrain the classical response: throughput, background, displacement offset and coupling corrections.

This separation makes the model useful. A future calibration can replace one assumed channel without rebuilding the entire sensing and inference pipeline.

### Details to keep in mind

A completely positive map can be written

\[
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger,
\qquad \sum_a K_a^\dagger K_a=I
\]

for a trace-preserving channel on its stated input/output spaces. For loss, an explicit failure flag can retain trace preservation; the surviving subblock alone is generally trace decreasing.

**Two kinds of freedom must be distinguished:**

1. Different Kraus representations can describe the **same channel**: ($K'_a=\sum_b u_{ab}K_b$) for a suitable unitary/isometry. This is representational freedom.
2. Choosing a loss, mixing or dephasing model chooses a **physical map**. It is a modelling assumption, not merely a different Kraus representation of an already identified channel.

Physical interpretation is attached to the full map and, when justified, an environment model or instrument. It cannot generally be uniquely assigned to each Kraus operator from output counts alone.

The provisional workbench fixes example optical parameters and fits throughput, background, offset and a coupling field. It also includes random displacement and readout assumptions. Its construction and provenance are documented in [ExoplanetExperimentAppendix.tex](../TeXtured/chapters/ExoplanetExperimentAppendix.tex), “Provisional Channel Workbench.”

## Slide 18 — Reproducing the observed mean response

### Spoken script

[Point to the observed map and then the modelled map. Pause.]

The model reproduces the main structure of the averaged observations: the central minimum and the increase with separation and relative source intensity.

This supports the usefulness of the complete forward model for describing the mean response. It does not prove that the individual assumed optical mechanisms are the ones present in the apparatus.

Different combinations can produce similar counts, especially when classical calibration can absorb part of their effects.

The model is therefore also a tool for designing the next experiment. Separate modal counts, independent throughput measurements and measurements in additional bases would help distinguish competing explanations.

The contribution is both a reconstruction of the observed mean pattern and a clear account of what evidence is still missing.

### Details to keep in mind

- The displayed panels are the **provisional workbench's observed and modelled setting means**, compared on the data used for fitting. Do not call this plot alone a held-out validation.
- The thesis separately reports grouped held-out prediction of setting means. That is evidence for the predictive classical calibration layer, not identification of all quantum channels. Use Appendix H if asked.
- Reproducing means is not reproducing the distribution of individual counts. The thesis finds overdispersion and rejects the tested simple deterministic count models as complete descriptions of individual exposures.
- Avoid “the channels were fitted” and “I reconstructed the experimental QFI.” Instead: **“The optical channels were specified; the observable count response was calibrated.”** A model-based QFI remains conditional on the specified state and channels.
- More measurements help only if they resolve relevant ambiguities: separate ports address modal aggregation; known flux and loss outcomes address efficiency; phase-sensitive or rotated-basis measurements address coherence; controlled mode injection constrains transfer properties. Complete channel identification can require several calibrated inputs as well as outputs.

## Slide 19 — Conclusions

### Spoken script

To conclude, I developed a numerical and quantum-circuit workflow for studying mixed-state sensor sensitivity, using exact references and variational spectral estimation.

I used it to compare preparation, noise and restricted access in a magnetometer. The thermal results show that the most useful preparation depends on the operating range, not only on the ground-state peak.

For SPADE, I constructed a quantum-to-classical channel description that reproduces the observed mean response while making the limits of the available data explicit. I also proposed VQ-SPADE as a future route to optical spectral estimation.

The common lesson is that useful sensitivity belongs to the whole sensing procedure: what we prepare, what we can access, and what we actually measure.

Thank you.

### Details to keep in mind

- The current conclusion slide says “Perfectly matching.” In speech, use the validated-workflow wording above: finite numerical precision, Trotter error and variational convergence still matter.
- VQ-SPADE is a proposal; the current archived experiment is not a demonstration of variational diagonalization.
- The main talk ends here. The following optional responses are outside the 15-minute budget.

## Optional responses for questions

### “Is the quantum natural gradient just Newton's method?” — Appendix B

“They share the idea of transforming the gradient using a matrix. But Newton's method uses curvature of the objective, while the quantum natural gradient uses the geometry of the state family. It scales a parameter step by how much that step changes the quantum state.”

\[
\Delta\boldsymbol\alpha
=-\eta\,(F^{\mathrm{ans}}+\lambda I)^{-1}\nabla C.
\]

Here (F^{\mathrm{ans}}) is a metric with respect to **trainable circuit parameters**, not the scalar QFI with respect to the sensed field. For pure states, the QFI matrix is four times the Fubini–Study metric, depending on convention. A mixed-state VQSE input needs an appropriate mixed-state metric; a pure-state metric is otherwise a surrogate. Regularization stabilizes poorly conditioned directions. Do not claim a measured general speedup or equivalence to the Hessian.

### “Why can temperature help if noise cannot increase QFI?” — Appendix D

“The comparison changes the preparation family. At each field, the Gibbs populations depend on that field, so they can carry sensitivity. This is different from applying the same parameter-independent noisy channel to an already prepared ground-state family.”

### “Does retaining most probability retain most information?” — Appendix A

“Not automatically. A small component can vary strongly with the parameter. The retained spectral weight gives a compact representation, but metrological accuracy has to be assessed using the bounds and the numerical benchmark.”

### “Did you identify the detector's quantum channel?” — Appendices F, H, K–M

“No. The counts constrain an observable classical response. I constructed compatible, physically motivated optical stages and calibrated the count model, while keeping their assumptions explicit. Identifying the optical channel would require additional controlled measurements and calibrations.”

### “Why not just use a classical regression?”

“A classical model is appropriate for predicting the measured counts, and the thesis includes that layer. The channel framework adds a description of the optical stages before measurement. It lets us ask how a different measurement, loss mechanism or calibrated optical transformation would change the accessible information. The current data do not uniquely determine that optical description.”

### “What does VQ-SPADE add to ordinary SPADE?” — Appendix I

“Ordinary SPADE measures in a specified modal basis. VQ-SPADE would add a trainable optical transformation so that the measurement basis could be adapted towards an eigenbasis of the state. That would need resolved outputs and calibration, and remains a proposed extension.”

## Rehearsal notes

- First rehearse **only** the spoken sections, including the five overlay advances on slide 3. The technical notes are not a second spoken paragraph.
- Clock checkpoints: start magnetometry near **5:05**, exoplanets near **7:55**, and conclusions near **14:10**.
- If running late, shorten the modularity explanation on slide 6 and the future-measurement examples on slide 18. Preserve the distinctions between populations/eigenvalues, assumptions/fits, and demonstrated/proposed work.
- On plots, name the axes or curves, point to the relevant feature, then state its implication. Give the audience a moment to look before continuing.
- Do not rush the final sentence. Finish with the conclusion slide visible.
