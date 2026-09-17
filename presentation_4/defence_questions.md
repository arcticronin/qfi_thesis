# Defence questions — statistics, machine learning and remote sensing

These are plausible questions inferred from the thesis and the committee's backgrounds, not predictions of what particular professors will ask. Start with the **short answer**, then use the **follow-up** only if needed. Each **Intuition** is a plain-language memory aid; use it when a technical answer needs unpacking. The proposed extensions below are suggestions, not completed thesis results.

For thermal preparation, start with the guided section at question 33. It builds from the Gibbs state to the exact meaning of your plotted comparison.

## First eight to rehearse

1. How does SPADE physically sort light into modes?
2. What did you contribute personally, and what comes from existing methods?
3. Does agreement with the observed means identify your optical channels?
4. How did you validate the model without data leakage?
5. Why use quantum channels instead of classical regression?
6. Is natural gradient the same as Newton's method?
7. Why can thermal preparation improve sensitivity if noise reduces QFI?
8. What would be needed to transfer this to an actual remote-sensing instrument?

## Optical intuition and remote sensing

### 1. “How does SPADE sort light into modes?”

**Intuition:** A sorter changes which question the detector asks. A camera asks “where did the photon arrive?”; a mode sorter asks “which spatial pattern did the field overlap with?”

**Short answer:**

“SPADE performs a change of optical basis before photon detection. A mode sorter transforms different spatial input profiles into different output ports; detectors then count those outputs. A useful analogy is a prism separating wavelengths, except here the components are transverse spatial modes.”

**How the hardware does it:**

Multi-plane light conversion uses designed phase patterns separated by propagation. Phase modulation and diffraction jointly map input modes to distinct output locations. See the primary experimental account of [multi-plane light converters](https://www.mdpi.com/2304-6732/11/3/241). The Santamaria experiment underlying the thesis uses this technology for HG demultiplexing: [experimental paper](https://arxiv.org/pdf/2309.02295).

**Mathematical follow-up:**

For an ideal sorter on the supported modes,

$$
U_{\rm sort}|HG_j\rangle=|\mathrm{port}_j\rangle,
\qquad
|\psi\rangle=\sum_j a_j|HG_j\rangle
\longmapsto\sum_j a_j|\mathrm{port}_j\rangle.
$$

A detection at port $j$ samples $|a_j|^2$. For a mixed state the probability is $p_j=\operatorname{Tr}(\rho M_j)$, with $M_j=|HG_j\rangle\langle HG_j|$ for an individually resolved ideal mode. The archived first-order stream combines two modes.

**Avoid:** “It looks at each photon and classifies its shape.” The optical transformation happens before destructive detection. A photon in a superposition is not split into fractional detector clicks. Real loss and cross-talk make the ideal mapping approximate.

### 2. “What exactly is a spatial mode? What do the two colours mean?”

**Intuition:** The positive and negative lobes are like opposite displacements of a vibrating string. They can cancel in an amplitude overlap, even though the measured energy or intensity is never negative.

**Short answer:**

“A spatial mode is a field-amplitude profile across the beam. The HG modes form an orthogonal family of such profiles. The two colours in the illustration represent opposite signs, or a relative phase of pi, not positive and negative intensity.”

**Follow-up:** The first-order mode has a sign change across one axis. Its overlap with a perfectly centred symmetric Gaussian vanishes by symmetry. A displacement breaks that symmetry and produces first-order amplitude. Measured intensity remains non-negative: $I\propto|E|^2$.

### 3. “Why can't you just project a camera image onto HG modes in software?”

**Intuition:** Taking the squared magnitude discards distinctions: amplitudes of opposite sign have the same intensity. Calculating afterwards cannot generally restore the amplitude relationships needed for another optical measurement.

**Short answer:**

“A camera records intensity in the position basis. SPADE combines optical amplitudes before detection. Processing an intensity image cannot generally reproduce that measurement, because the image has already discarded the relevant phase relationships.”

**Follow-up:** A classical estimator can improve use of the camera data and exploit prior assumptions; it cannot generally turn those data into the outcomes of an unperformed optical measurement. A field-sensitive measurement, such as an appropriate coherent receiver, would be a different acquisition system.

### 4. “Does this violate diffraction, or really detect an exoplanet?”

**Intuition:** Estimating where two overlapping sources are is different from seeing two separate bright spots. A model can support precise parameter estimation without producing a sharply resolved image.

**Short answer:**

“No. It changes the measurement used to estimate parameters of a diffraction-limited field. The thesis analyses a controlled laboratory experiment motivated by a bright star and a faint companion; it does not report detection of an astronomical exoplanet.”

**Follow-up:** Estimating separation, reconstructing an arbitrary image and detecting whether a companion exists are different tasks. QFI is a local estimation benchmark. A detection claim additionally needs hypotheses, false-alarm control and detection power. Do not promise the same improvement for all scenes or all source contrasts.

### 5. “Would this work on a telescope or an Earth-observation instrument?”

**Intuition:** A measurement optimized for one kind of scene is like a tool made for one job. The same principle may transfer, but its performance must be checked for the new scene and instrument.

**Short answer:**

“The transferable idea is to choose an optical measurement that is sensitive to the parameter of interest. But the present model assumes a much simpler scene and optical response than a deployed instrument. I would first test robustness to the actual point-spread function, alignment, aberrations, bandwidth, background and throughput.”

**Follow-up — proposed validation path:** First characterize the instrument; then test controlled scenes under realistic disturbances; finally compare against an appropriate imaging baseline using matched photon and acquisition budgets. HG modes are convenient for a Gaussian PSF, not automatically optimal for every pupil, wavelength or extended scene. Ground-based turbulence and platform jitter require different physical models and calibrations. Do not describe a deployment study as already completed.

### 6. “If you must align with the star, aren't you assuming the unknown position?”

**Intuition:** If the strong reference is slightly off-centre, its leakage can look like part of the weak companion signal. Alignment is therefore part of the inference problem, not just a cosmetic adjustment.

**Short answer:**

“We align to the bright reference, while the parameter of interest is the companion's displacement relative to it. In practice the reference position must itself be estimated. Residual misalignment leaks bright-source light into the weak-signal modes, so it must be calibrated or treated as a nuisance parameter.”

**Follow-up:** A possible implementation uses a preliminary alignment measurement and then the mode-sorting measurement. That consumes photons and time. A fair system comparison must include these costs. The thesis's ideal-alignment calculations are conditional on that assumption.

## Statistics and inference

### 7. “You reproduce the averages. Does that validate the physical channels?”

**Intuition:** A dim count stream can mean fewer incoming photons or more loss. The same observed total can have different physical explanations.

**Short answer:**

“It shows that the complete calibrated forward model can describe the mean response. It does not uniquely identify its optical stages. Different channel choices can give similar measured counts, and some effects can be absorbed into throughput or background.”

**Follow-up:** The workbench fixes example optical parameters and fits the classical response. The comparison on slide 18 is an in-sample comparison of means. The thesis separately evaluates held-out prediction of setting means. Neither establishes full quantum process tomography. This distinction is central to the contribution, not a minor disclaimer.

### 8. “How did you validate the model? Why not randomly split all 52,500 observations?”

**Intuition:** Testing on another repetition at a familiar setting asks “can I repeat this prediction?” Holding out a whole setting asks “can I predict where I have not calibrated?” Both are legitimate, different tests.

**Short answer:**

“A random split of individual repetitions would put the same experimental settings in training and test, which mainly tests prediction of another repetition at a known setting. The thesis also holds out groups of settings: checkerboard cells, entire distance rows and entire source-ratio columns.”

**Follow-up:** The model and its hyperparameters are refitted without those held-out setting means. These splits probe prediction across the observed setting domain. They do not prove unrestricted extrapolation or independence from all shared calibration errors. Distinguish that validation from the slide-18 fitted workbench image. See deck Appendix H.

### 9. “Why not assume Poisson photon counts?”

**Intuition:** A Poisson model assumes a fixed rate for a fixed condition. If that rate wanders between acquisitions, the combined counts fluctuate more than the fixed-rate prediction.

**Short answer:**

“The repeated counts are more variable than a fixed-rate Poisson model predicts. The median variance-to-mean ratio is about 2.5, rather than one. The thesis tests discrete overdispersed alternatives, but these still fail to describe all aspects of the individual counts.”

**Follow-up:** NB1 and Poisson–lognormal alternatives were considered. Better agreement with means does not guarantee correct variance, zeros or tails. Overdispersion alone does not establish photon bunching: changing background, coupling or intensity can also produce it. Use [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex) for the actual diagnostics rather than claiming that one count family solved the problem.

### 10. “Are your bootstrap uncertainties reliable?”

**Intuition:** Resampling repeats gives many plausible repeat datasets. It cannot reveal a calibration error shared by every acquisition, because that error is present in every resampled dataset too.

**Short answer:**

“For uncertainty at recorded settings, the thesis resamples the observed repetitions within each setting. This preserves discrete counts without assuming an exact parametric count family. It still relies on the repetitions being representative and approximately independent within each setting.”

**Follow-up:** Ordinary within-setting resampling does not preserve temporal dependence or shared systematic calibration error. Exchangeability alone is not enough to justify treating correlated repetitions as independent. If relevant dependence is present, a block or hierarchical resampling design may be needed. Intervals conditional on fixed calibration and variation across modelling assumptions answer different questions. Do not call either an unconditional bound on the true apparatus parameters.

### 11. “Can you estimate separation and brightness simultaneously?”

**Intuition:** A faint source farther away and a brighter source closer in can produce the same first-order count. One number cannot generally tell you which combination caused it.

**Short answer:**

“Not necessarily from the available aggregate probability. Near small separation, the first-order response depends approximately on a product of relative brightness and squared separation. Different parameter combinations can therefore produce similar counts. Joint inference needs additional information or constraints.”

**Follow-up:** In the thesis's ideal normalized convention,

$$
p_1=\epsilon q e^{-q},\qquad q=d_a^2/4,
$$

so $p_1\simeq\epsilon d_a^2/4$ at small displacement. The experimental calibration grid varies known settings; that is not equivalent to identifying all unknown parameters from a new single setting. For joint estimation, inspect the Fisher matrix and parameter degeneracies, not just scalar QFI with other variables held fixed.

### 12. “Why use Fisher information rather than estimator error?”

**Intuition:** Fisher information says how much nearby parameter values change the probability model. It is a local precision benchmark; estimator error is what a particular inference procedure actually achieves.

**Short answer:**

“Fisher information supplies a local precision benchmark for a specified statistical model and measurement. It lets me compare sensing designs without committing to one estimator. But it is not a substitute for finite-sample estimation error or robustness to model mismatch.”

**Follow-up:** Cramér–Rao bounds require suitable regularity and unbiasedness assumptions, and need not be attained at finite sample size. An empirical estimation study would also examine bias, RMSE, interval coverage and nuisance parameters. The stated QFI is not automatically the precision of the whole deployed instrument.

## Machine learning and computation

### 13. “What does VQSE learn, and where does the training signal come from?”

**Intuition:** The input spectrum stays fixed while the circuit turns the measurement basis to expose it. Training tries to make the dominant components visible in selected detector outcomes.

**Short answer:**

“It learns a circuit that rotates the state's dominant eigenvectors towards selected computational-basis states. Measurements after the circuit give probabilities used to evaluate a cost with an auxiliary Hamiltonian. A classical optimizer adjusts the gates using that measured objective.”

**Follow-up:** It is not supervised training against a table of true eigenvectors on hardware. Exact eigenpairs are available in the small numerical benchmarks for validation. The auxiliary Hamiltonian used to organize the eigensolver cost is not the magnetometer Hamiltonian. Eigenvalues are invariant under the unitary; the circuit changes which basis exposes them.

### 14. “Is natural gradient just Newton's method? Did it speed up your algorithm?”

**Intuition:** Two equal-sized knob adjustments can change the state by very different amounts. Natural gradient accounts for that unequal sensitivity; Newton instead uses how the objective itself bends.

**Short answer:**

“They both transform the gradient using a matrix, but the matrices describe different things. Newton uses objective curvature; natural gradient uses the geometry of the state family. I tested stochastic-reconfiguration training on selected small VQSE benchmarks, rather than establishing a general speedup.”

**Follow-up:** The metric concerns trainable circuit parameters, not the sensed field. A pure-state SR metric is generally a surrogate for a mixed-state problem. An exact intrinsic metric needs a mixed-state estimator or a correctly treated purification construction; choosing an arbitrary purification does not automatically give that metric. The metric also has an estimation and linear-solve cost. Compare accuracy against shots, circuit evaluations and wall time, not only optimization iterations. The plotted RBM training example is a separate pure-state demonstration. See Appendix B and [VQSE.tex](../TeXtured/chapters/VQSE.tex).

### 15. “Why truncate? How do you choose the rank?”

**Intuition:** A rarely occupied component may change very rapidly with the field. Throwing it away because it is rare can remove more sensitivity than its small probability suggests.

**Short answer:**

“Truncation makes spectral estimation more manageable when relatively few components are important. But retaining most probability is not a proof that most sensitivity is retained. In a benchmark I would assess rank through the information bounds and their agreement with the exact reference.”

**Follow-up:** The retained matrix is subnormalized. A small component can have a large parameter derivative. Increasing rank trades resources for a more complete description; do not assert a universal sufficient retained-weight threshold. Explain the rank and checks actually used if asked for a numerical result. See Appendix A.

### 16. “Why not use a neural network or Gaussian process directly on the counts?”

**Intuition:** Regression predicts the output. The physical stages express hypotheses about how it was produced, allowing questions about changing the apparatus—conditional on those hypotheses.

**Short answer:**

“A classical predictive model is appropriate for the recorded counts, and the thesis includes a calibration layer. The channel model adds a description of optical stages before measurement, so we can examine changes to the receiver and the information it preserves.”

**Follow-up:** Predictive accuracy alone does not identify internal physics. Conversely, writing a physical model does not prove its assumed mechanisms. The thesis uses their complementary roles: classical calibration for the observable response and replaceable channel assumptions for conditional physical analysis.

### 17. “Where is the quantum advantage?”

**Intuition:** A better optical measurement and a faster computer are two different advantages. Demonstrating one would not establish the other.

**Short answer:**

“This work does not demonstrate a computational quantum advantage. It implements and benchmarks a variational route to mixed-state information estimates. In the optical part, the advantage being investigated is a measurement advantage over direct imaging under stated conditions, which is a different claim.”

**Follow-up:** A computational advantage would require resource accounting, an appropriate classical baseline, larger instances and robustness tests. The optical measurement does not require you to claim entangled illumination or a universal quantum-computing speedup.

## Physics, novelty and next steps

### 18. “Why can temperature help if noise cannot increase QFI?”

**Intuition:** Excited-state populations can act as additional field indicators: their relative weights shift with the field. Whether this helps depends on how strongly they shift and what the receiver observes.

**Short answer:**

“I compare different parameter-dependent preparation families. The Gibbs populations change with the field and can carry sensitivity. I am not applying a fixed parameter-independent noise channel to the same ground-state family and finding increased QFI.”

**Follow-up:** Both reduced preparations can be mixed. The result is for a finite model and operating window, not a universal advantage of mixedness. The plot does not include optimization of cooling time or state-preparation resources. If the field is uncertain, a prior-weighted or worst-case precision objective would be a useful next step, but the current plots are pointwise comparisons.

### 19. “Are you free to choose any Kraus operators?”

**Intuition:** Different Kraus descriptions can be different mathematical accounts of the same observable map. Choosing another physical noise process changes the map itself.

**Short answer:**

“No. I first choose a physically motivated completely positive, trace-preserving map. Kraus operators are one representation of that map, and different Kraus sets can represent exactly the same observable channel. Choosing a different physical process is a separate modelling decision.”

**Follow-up:** For a trace-preserving map, $\sum_a K_a^\dagger K_a=I$. A loss model may require a vacuum or failure output to preserve total probability. A unitary or isometric change of Kraus representation does not create a new observable effect. In the thesis, erasure, dephasing, coherent mixing and modal loss represent plausible mechanisms, but the aggregate counts do not prove that these are the unique maps realized by the apparatus. I therefore use the uncalibrated stages for conditional sensitivity analysis, not as fitted process tomography. See Appendices E–G and K–M.

**Avoid:** “I had freedom, so I invented some Kraus operators.” Say instead: “I selected standard channel families corresponding to plausible physical mechanisms and made their unmeasured parameters explicit.”

### 20. “What exactly would VQ-SPADE add?”

**Intuition:** Ordinary SPADE measures using a fixed set of spatial patterns. VQ-SPADE would train the patterns presented to the detector so they align with the state’s spectral components.

**Short answer:**

“SPADE measures a fixed modal basis. VQ-SPADE would add a trainable optical transformation that aims to rotate an unknown state's eigenbasis into the resolved measurement basis. The readout could then supply spectral populations, analogous to VQSE.”

**Follow-up:** Mode populations are not generally eigenvalues. Even in an eigenbasis, aggregating modes yields sums of eigenvalues. The proposal needs resolved outputs, repeated preparations, an expressive controllable transformation and loss calibration. Diagonalization serves spectral estimation; it is not automatically the measurement that maximizes CFI for every sensing parameter. This was proposed, not implemented. See Appendix I.

**Tiny example — populations versus eigenvalues:** The matrices $\rho_A=\begin{pmatrix}0.5&0\\0&0.5\end{pmatrix}$ and $\rho_B=\begin{pmatrix}0.5&0.4\\0.4&0.5\end{pmatrix}$ both give probabilities $(0.5,0.5)$ in this basis. But their eigenvalues are $(0.5,0.5)$ and $(0.9,0.1)$. The same measured populations can therefore hide different spectra.

### 21. “What did you personally contribute?”

**Intuition:** Separate the established ingredients from what you built and tested with them. That makes the contribution precise without requiring a priority claim.

**Short answer:**

“I independently implemented and benchmarked the variational spectral-estimation workflow, including the adaptive auxiliary Hamiltonian and selected small stochastic-reconfiguration training tests. I studied preparation, noise and restricted access in the magnetometer. For the optical data, I developed a calibrated sequential channel description and clarified what the archive can identify. I also proposed VQ-SPADE as a future extension.”

**Follow-up:** VQSE, QFI, natural gradient and SPADE are established methods. Your contribution is their implementation, study, integration and the stated proposal. A priority claim such as “first” requires a separate, defensible literature review; it is unnecessary for a strong answer about your work.

### 22. “If you could request one more measurement, what would it be?”

**Intuition:** Choose the new observable that separates the explanations you are currently unable to distinguish. More copies of the same count do not necessarily resolve that ambiguity.

**Short answer:**

“I would first decide which ambiguity we want to remove. For example, separate fundamental and first-order port counts would give much more information than the aggregate stream. To identify efficiency I would also need incident flux; to study coherence I would need another modal basis or a phase-sensitive measurement.”

**Follow-up:** There is no single extra scalar measurement that identifies the entire channel. For transfer calibration, inject known modes and record all outputs. For background, use source-blocked acquisitions. For jitter, synchronize pointing measurements with counts. State which of these addresses the specific mechanism under discussion.

## Further questions that expose important distinctions

### 23. “If VQ-SPADE diagonalizes the state, does it automatically attain QFI?”

**Intuition:** Identifying what a state is made of is different from finding the measurement most sensitive to how it changes.

**Short answer:**

“No. The eigenbasis is useful for spectral estimation, but the optimal local sensing measurement depends on the derivative of the state as well. VQ-SPADE would supply ingredients for information estimation; diagonalization alone does not guarantee a QFI-optimal detector.”

**Follow-up:** For a regular single-parameter model, a measurement in the symmetric logarithmic derivative's eigenbasis can attain the QFI locally. The SLD satisfies

$$
\partial_\theta\rho=\frac{L_\theta\rho+\rho L_\theta}{2}.
$$

It need not share the eigenbasis of $\rho$. A unitary state family can keep all eigenvalues constant while its eigenvectors rotate and carry nonzero QFI. A fixed measurement in the reference state's eigenbasis can miss that first-order rotation. This is an important distinction for the VQ-SPADE proposal. See [MathBackground.tex](../TeXtured/chapters/MathBackground.tex).

### 24. “How can you choose the best measurement if the parameter is unknown?”

**Intuition:** First locate the target approximately; then choose a more sensitive measurement around that estimate.

**Short answer:**

“The QFI benchmark is local, and its optimal measurement can depend on the parameter. An adaptive strategy can use an initial estimate to choose later measurements. A globally robust fixed measurement is another design choice. The local QFI alone does not solve that design problem.”

**Follow-up:** Include the photons or state copies used for the preliminary estimate in the resource budget. Multiple unknown parameters can create competing measurement requirements. Do not infer simultaneous attainability of every single-parameter bound.

### 25. “How can a thermal state depend on an unknown field? Doesn't preparation require knowing it?”

**Intuition:** A thermometer responds to an unknown temperature without being told its value. A probe equilibrating in an unknown field can likewise respond to that field.

**Short answer:**

“The field physically enters the probe's Hamiltonian. If the probe equilibrates with a bath at controlled temperature, its populations respond to the actual field, even if we do not know it. The simulation evaluates this response at different field values.”

**Follow-up:** Numerically preparing the exact Gibbs state at every parameter is a model of equilibration, not a complete experimental preparation protocol. Equilibration time, temperature uncertainty and changing fields matter. Likewise, knowing the numerical ground state at each field is not by itself a hardware recipe for preparing it. The thesis's curves do not include these resource costs.

### 26. “If the sources are incoherent, why does your state have coherences?”

**Intuition:** Random relative phase between two sources does not erase the spatial structure of each source's own field.

**Short answer:**

“Incoherence between the star and companion removes interference terms between those source contributions. But a displaced source is itself a superposition of HG modes, so its density matrix can have off-diagonal entries in that basis. Coherence is basis-dependent.”

**Follow-up:** In the source mixture $(1-\epsilon)|\psi_0\rangle\langle\psi_0|+\epsilon|\psi_d\rangle\langle\psi_d|$, there are no cross terms between the sources. Each term can still contain HG-basis coherences. This does not mean the experiment directly measured those coherences. See [Astrophysical.tex](../TeXtured/chapters/Astrophysical.tex).

### 27. “What does fidelity have to do with QFI? Why keep discarded probability?”

**Intuition:** Fidelity measures how similar two states are. QFI describes how quickly that similarity falls when the parameter changes a little.

**Short answer:**

“The variational method compares nearby states through fidelity quantities. Truncation gives access to only part of their spectrum, so we use bounds that account for the missing weight. The local-QFI interpretation comes from taking the small-parameter-displacement limit.”

**Follow-up:** With root fidelity $f(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1$, the regular local relation is

$$
F_Q(\theta)=\lim_{\delta\to0}\frac{8[1-f(\rho_\theta,\rho_{\theta+\delta})]}{\delta^2}.
$$

Using squared fidelity changes the corresponding prefactor. For subnormalized positive operators, generalized root fidelity adds the missing-weight contribution $\sqrt{(1-\operatorname{Tr}\rho)(1-\operatorname{Tr}\sigma)}$. Renormalizing retained components would instead condition away that information. At finite $\delta$, the thesis bounds the finite-displacement functional; do not silently label every numerical endpoint an exact local-QFI bound. See [Methods.tex](../TeXtured/chapters/Methods.tex).

### 28. “Do more informative surviving photons guarantee a better sensor?”

**Intuition:** Keeping only excellent measurements is not necessarily efficient if you throw almost everything else away.

**Short answer:**

“No. Information per surviving photon and information per launched photon are different resource conventions. To compare complete receivers, I must also include success probability, losses and acquisition time.”

**Follow-up:** If success occurs with probability $\eta(\theta)$, the full classical record contains information from whether success occurred as well as the conditional output. For nonzero branch probabilities,

$$
F_{\rm total}=\frac{[\partial_\theta\eta]^2}{\eta(1-\eta)}
+\eta F_{\rm success}+(1-\eta)F_{\rm failure}.
$$

An undifferentiated failure flag has no additional conditional information, so $F_{\rm failure}=0$. If $\eta$ is parameter-independent, the first term vanishes. Conditioning can raise information per retained event without improving the complete resource-accounted experiment.

### 29. “What is the adaptive Hamiltonian in VQSE? Does it change the sensor?”

**Intuition:** You adjust the training objective used to find the basis, not the physical magnetic field being sensed.

**Short answer:**

“It is an auxiliary cost Hamiltonian used by the eigensolver. The adaptive construction changes this training objective as optimization proceeds, including updates based on measured dominant outcomes. It is separate from the physical Hamiltonian that prepares and encodes the sensor state.”

**Follow-up:** This is an implementation of an existing VQSE strategy, not a new physical interaction. Its purpose is to help trainability; it does not establish that every ansatz avoids barren plateaus or local minima. The full adaptive objective and the SR metric are different tools. See [VQSE.tex](../TeXtured/chapters/VQSE.tex).

### 30. “If measuring a quantum state destroys it, how do you train VQSE?”

**Intuition:** You repeat the preparation and measure a fresh sample, rather than reading the same photon or register again and again.

**Short answer:**

“Training assumes repeated access to the state-preparation procedure. Each circuit execution uses a new preparation, and outcome frequencies estimate the cost. The finite-shot uncertainty and number of preparations are part of the computational resources.”

**Follow-up:** This does not clone an arbitrary unknown state. VQSE uses one input-state copy per circuit execution, but overlap routines elsewhere in the information-estimation pipeline can require multiple state registers. Keep those resource claims separate.

### 31. “If the count models were rejected, what result remains valid?”

**Intuition:** A model can predict the average height of a distribution while getting its spread or tails wrong.

**Short answer:**

“Rejection concerns the tested models as descriptions of individual count observations. It does not imply that every mean prediction is useless. I report mean-response modelling separately and assess its predictive calibration using held-out setting means.”

**Follow-up:** For example, two count distributions can share mean ten but have very different probabilities of zero or thirty. Good mean prediction is a limited result, not proof of the complete likelihood. This is why I distinguish mean validation from experimental channel reconstruction and single-count statistical adequacy.

### 32. “Does zero local Fisher information mean the data contain no information at all?”

**Intuition:** At the bottom of a symmetric valley, the slope is zero, but moving a finite distance still changes the height.

**Short answer:**

“Zero regular local Fisher information can mean that probabilities do not change at first order at the reference point. They may still change at higher order or distinguish more distant parameters. The usual local precision analysis needs care at such a point.”

**Follow-up:** This is relevant to the initial basis in the animation. The two drawn states are finitely separated, while the CFI is evaluated from derivatives at the reference parameter. Vanishing-probability outcomes can introduce additional singular-limit issues, so do not extrapolate the zero-slope intuition to every boundary model.

## Thermal preparation — a guided question bank

This section is deliberately more gradual than the others. Start with questions **33–37**, then **39–45**. Questions **46–52** prepare you for the harder experimental and statistical follow-ups. The two-level example is an explanatory calculation, **not** the six-spin result from the thesis.

### The picture to keep in mind

At a given magnetic field, the Hamiltonian defines energy levels and energy eigenstates. Ground-state preparation occupies the lowest level. Gibbs preparation distributes probability over several levels, favouring lower energies. Change the field and both the levels and their states can change. At a fixed bath temperature, the equilibrium probabilities respond as well.

Your calculation then discards two of the six probe spins. The sensor's QFI measures how the resulting four-spin state responds to a small field change.

**Three separate objects:**

| Object | Role |
|---|---|
| Unknown field $h_x$ | The parameter to estimate; it changes the Hamiltonian. |
| Controlled inverse temperature $\beta$ | The preparation setting, held fixed along each plotted field curve. |
| Inaccessible probe spins $E$ | Two spins whose outcomes are unavailable; they are not the external thermal bath. |

A useful sentence to remember is: **“Temperature changes how the probe is populated; the unknown field changes what those populations and states look like.”**

### 33. “What is a Gibbs state, in simple terms?”

**Intuition:** At equilibrium, lower-energy states are more probable, but finite temperature allows excited states to be occupied too.

**Short answer:**

“A Gibbs state is the equilibrium state associated with a Hamiltonian at a specified temperature. It assigns each energy eigenstate a probability that decreases exponentially with its energy.”

**Follow-up:** If $H(h_x)|E_k(h_x)\rangle=E_k(h_x)|E_k(h_x)\rangle$, then

$$
\rho_\beta(h_x)=\frac{e^{-\beta H(h_x)}}{Z(h_x,\beta)}
=\sum_k p_k(h_x,\beta)|E_k(h_x)\rangle\langle E_k(h_x)|,
\qquad p_k=\frac{e^{-\beta E_k}}{Z}.
$$

This is diagonal in the **energy eigenbasis at that field**. It is not generally diagonal in the computational, HG or any other fixed basis.

### 34. “What is beta? Why is beta five colder than beta two?”

**Intuition:** Beta measures how strongly the preparation suppresses excitation.

**Short answer:**

“Beta is inverse temperature: $\beta=1/(k_B T)$. A larger beta gives a stronger preference for low-energy states. Therefore beta five is colder than beta two.”

**Follow-up:** The physically relevant comparison is temperature versus the energy gaps. The Boltzmann factor contains $\beta\Delta E$. Plot conventions use $J=1$, or the dimensionless quantity $\beta J$. Without specifying the physical energy scale $J$, these numbers are not temperatures in kelvin.

### 35. “What is the partition function? Does it describe another physical process?”

**Intuition:** First assign every state an unnormalized weight; then divide by the sum so the probabilities add to one.

**Short answer:**

“The partition function is $Z=\sum_k e^{-\beta E_k}$. Here its immediate role is normalization. It changes with the field because the energy levels change with the field.”

**Follow-up:** Forgetting the derivative of $Z$ would give the wrong derivative of the Gibbs probabilities. A common shift of all energy levels changes $Z$ but leaves the normalized probabilities unchanged: energy differences determine their relative weights.

### 36. “Can you give a tiny example where thermal populations carry information?”

**Intuition:** If the spacing between two energy levels changes, the equilibrium fraction in the upper level changes. That fraction can reveal the spacing.

**Short answer:**

“Consider two fixed eigenstates with energies zero and an unknown positive gap $\Delta$. At zero temperature the probe always occupies the ground state, so this particular state does not tell us the gap. At finite temperature the excited-state probability depends on the gap, which we can estimate from repeated energy-basis outcomes.”

**Follow-up — optional calculation:** At fixed beta,

$$
p_{\rm exc}(\Delta)=\frac{1}{1+e^{\beta\Delta}},\qquad
\partial_\Delta p_{\rm exc}=-\beta p_{\rm exc}(1-p_{\rm exc}).
$$

The energy basis is fixed in this example, so its classical Fisher information equals the state's QFI:

$$
F_\Delta=\frac{(\partial_\Delta p_{\rm exc})^2}{p_{\rm exc}(1-p_{\rm exc})}
=\beta^2p_{\rm exc}(1-p_{\rm exc}).
$$

It is positive at finite beta and tends to zero in both the very hot and very cold limits for fixed $\Delta>0$. Thus more thermal occupation does not imply more information without limit. In your TFIM, eigenvectors also depend on the field, so the ground-state reference itself has sensitivity; this example isolates just the population mechanism.

### 37. “What exactly changes with the field: the probabilities or the eigenvectors?”

**Intuition:** The field can change both the mixture's weights and the quantum states being mixed.

**Short answer:**

“Both can change. The energy eigenstates respond to the field, and their energy gaps change the Gibbs weights. These are two ways a thermal state can become distinguishable when the field changes.”

**Follow-up:** At fixed beta, for differentiable energy branches,

$$
\partial_{h_x}p_k=-\beta p_k\left(\partial_{h_x}E_k-
\sum_jp_j\partial_{h_x}E_j\right).
$$

Only energy slopes relative to their thermal average affect the populations. For a full-rank smooth state family, QFI has a population contribution $\sum_k(\partial p_k)^2/p_k$ and an additional contribution from eigenvector changes. The eigenpairs relevant after partial trace are those of the **reduced density matrix**, not simply the full energy eigenpairs.

### 38. “Is thermal preparation just adding more noise to the ground state?”

**Intuition:** A preparation rule that follows field-dependent energy levels is different from blindly randomizing an already prepared state.

**Short answer:**

“In this study, no. I compare equilibrium Gibbs preparation with ground-state preparation and with a separate fixed depolarizing channel. They have different field-dependent state families, so their mixedness has different physical origins.”

**Follow-up:** The statement that a parameter-independent channel cannot increase QFI applies when processing the **same input family**. Equilibration in a Hamiltonian containing the unknown field is a field-dependent physical process. See question 18 for the data-processing distinction. Do not say that thermal noise is always helpful or that the data-processing inequality fails.

### 39. “What is fixed while you trace each thermal curve?”

**Intuition:** Choose one temperature setting and sweep the field; then repeat the sweep at another temperature.

**Short answer:**

“Along each displayed curve, beta, the geometry and the accessible subsystem are fixed. The horizontal axis varies the field. QFI uses the derivative with respect to that field, with beta held constant.”

**Follow-up:** This differs from choosing $\beta(h_x)$ to maintain a fixed purity. That would be another path through state space and would add a term involving $d\beta/dh_x$ to the derivative. The thesis discusses such controls separately; do not use their interpretation for slides 9–10.

### 40. “Are the two discarded spins the bath that thermalizes the sensor?”

**Intuition:** The bath prepares the probe; limited access determines how much of that prepared probe you observe.

**Short answer:**

“No. The full six-spin probe is assigned a Gibbs state. I then trace out two of its spins because the observer cannot access them. Those two spins are not the external bath used to establish the Gibbs preparation.”

**Follow-up:** The calculation specifies an equilibrium state rather than explicitly simulating a bath and its thermalization dynamics. Preparation and restricted readout are separate modelling steps.

### 41. “Is your four-spin state the Gibbs state of a four-spin Hamiltonian?”

**Intuition:** A subsystem cut out of an interacting equilibrium system still reflects its interactions with the rest.

**Short answer:**

“Not generally. I prepare the Gibbs state of the interacting six-spin system and then trace out two spins. This need not equal the Gibbs state obtained by thermally preparing four isolated spins.”

**Follow-up:** In general,

$$
\operatorname{Tr}_E\left[\frac{e^{-\beta H_{SE}}}{Z_{SE}}\right]
\ne\frac{e^{-\beta H_S}}{Z_S}.
$$

If the Hamiltonian separates into noninteracting subsystem and environment terms, the usual factorization recovers the isolated Gibbs state. An effective Hamiltonian can describe the reduced equilibrium state, but it need not be the bare four-spin Hamiltonian.

### 42. “Are you comparing a pure state with a mixed state?”

**Intuition:** A globally pure state can already look mixed when only part of it is accessible.

**Short answer:**

“The global ground-state preparation is pure, but its four-spin reduction can be mixed because of entanglement with the other spins. The plotted comparison is therefore between two reduced preparations, both of which can be mixed.”

**Follow-up:** A mixed reduced ground state is not automatically a finite-temperature state of the isolated subsystem. Purity and temperature are different concepts. The comparison is about preparation history and field response, not a blanket contest between purity and mixedness.

### 43. “What do beta two and beta five actually demonstrate?”

**Intuition:** One curve illustrates an off-peak benefit; the other also has a stronger maximum.

**Short answer:**

“At beta two, the thermal preparation has a lower maximum but more QFI over part of the field range beyond the ground-state peak. At beta five, it also exceeds the reduced ground-state peak. These are two concrete preparation choices with different operating-range trade-offs.”

**Follow-up — numbers only if asked:** In the thesis's periodic $N=6,n=4,J=1$ sweep, the ground-subsystem maximum is 3.926. Thermal maxima are 2.607 at beta two and 4.847 at beta five. The latter is about 23.5% higher than the ground-subsystem maximum. These maxima occur at their respective fields; do not confuse a comparison of maxima with a pointwise ratio at one field.

The observed curves support the effect. Field-dependent low-energy populations provide the physical explanation, but they do not by themselves predict every reduced-state peak or crossing without calculating the full model.

### 44. “If cooling helps, should beta go to infinity?”

**Intuition:** At sufficiently low temperature the excited populations disappear, so a finite-temperature advantage need not persist all the way to zero temperature.

**Short answer:**

“Not necessarily. At a fixed field with a unique gapped ground state, the Gibbs state approaches the ground state as beta becomes very large. A finite-temperature advantage therefore does not imply that further cooling always improves sensitivity.”

**Follow-up:** Under the corresponding smooth, gapped conditions, the field response approaches the ground-state response. Near degeneracies or closing gaps, limits require care. At an exact ground-energy degeneracy, the Gibbs limit is the normalized projector onto that eigenspace, not an arbitrarily selected pure ground state. A maximum over a varying field range can behave differently from pointwise convergence at a fixed field.

### 45. “What happens at extremely high temperature?”

**Intuition:** If all levels are populated almost equally, their relative weights carry little information about how the energy spectrum changes.

**Short answer:**

“For this finite-dimensional equilibrium model, beta tends to zero and the Gibbs state tends to the maximally mixed state. It becomes independent of the field, so its field QFI tends to zero. Infinite heating does not produce a better magnetometer.”

**Follow-up:** At beta zero, $\rho_N=I/2^N$ and its reduction is $I/2^n$. This statement is about the equilibrium family in the thesis, not every possible driven high-temperature sensing protocol.

### 46. “What if the temperature is not known precisely?”

**Intuition:** If both field and temperature change populations, an observed population change may have more than one cause.

**Short answer:**

“The displayed curves assume controlled, known beta. If temperature is uncertain, it becomes a nuisance parameter that should be calibrated or jointly estimated. The field precision can be worse than the fixed-temperature benchmark.”

**Follow-up:** For a specified measurement with a regular two-parameter classical Fisher matrix, the effective information for the field with unknown beta is the Schur complement

$$
F_{hh}^{\rm eff}=F_{hh}-\frac{F_{h\beta}^2}{F_{\beta\beta}},
$$

when $F_{\beta\beta}>0$ and the relevant matrix is invertible. Correlated responses reduce identifiable field information. A quantum multiparameter analysis additionally has measurement-compatibility issues; do not interpret the formula as automatic joint attainability of the QFIM bound.

### 47. “How could a thermal state be prepared physically or on a circuit?”

**Intuition:** Equilibration uses an environment; a circuit representation also needs a source of mixing if it starts pure.

**Short answer:**

“A physical route is to let the probe equilibrate with a controlled-temperature environment under the relevant Hamiltonian. A circuit route could use an enlarged system and discard ancillas, or another mixed-state preparation procedure. The numerical Gibbs matrix alone is not a hardware preparation demonstration.”

**Follow-up:** A unitary acting only on a pure probe preserves purity and cannot create its global Gibbs mixture. A purification can represent a Gibbs state on a larger register, but preparing that purification efficiently is an additional problem. The pipeline's dynamical circuit thumbnail is not an implemented end-to-end Gibbs preparation protocol.

### 48. “Is this a thermal initial state followed by unitary sensing evolution?”

**Intuition:** Ask whether the field is already encoded in the equilibrium state or is encoded later through time evolution. Those are different experiments.

**Short answer:**

“The displayed thermal curves use the equilibrium family of the field-dependent Hamiltonian itself. At every field I calculate its Gibbs state and then restrict access. They are not the same as preparing one fixed thermal state and subsequently evolving it under an unknown field for a chosen time.”

**Follow-up:** The two constructions are

$$
\rho_{\rm eq}(h_x)=e^{-\beta H(h_x)}/Z(h_x,\beta)
$$

and, for a different protocol,

$$
\rho(h_x,t)=U_{h_x}(t)\rho_\beta(h_{\rm ref})U_{h_x}^\dagger(t).
$$

In the second, the initial state is fixed with respect to the sensed field. Its QFI and resource accounting can differ. This distinction prevents the slide-6 circuit example from being mistaken for the protocol producing slides 9–10.

### 49. “Have you proved thermal preparation is better in an unknown environment?”

**Intuition:** A higher curve in one interval gives a reason to consider that preparation there, not a guarantee for every unknown field or disturbance.

**Short answer:**

“I showed higher pointwise sensitivity in certain field intervals. This motivates thermal preparation when the expected field lies in those intervals. I did not optimize a universal preparation for an arbitrary environment or prior distribution.”

**Follow-up:** A next study could define the expected field range, nuisance parameters and a task-level objective, such as Bayesian estimation error or worst-case precision. Simply averaging QFI is not generally equivalent to minimizing expected estimation error. Temperature robustness, detector noise and uncertain field location are distinct issues.

### 50. “Is the thermal comparison fair once preparation time and energy are included?”

**Intuition:** A sensitive preparation that takes much longer to produce may allow fewer useful measurements per second.

**Short answer:**

“The comparison fixes the Hamiltonian and accessible subsystem and compares their state QFI. It does not include a full preparation-time or energy budget. A practical advantage would need that additional accounting.”

**Follow-up:** For approximately independent cycles, a first resource-aware comparison would account for the number of repetitions achievable in a fixed total time, including preparation, encoding and readout. Equilibration, cooling and ground-state preparation can have different costs. A larger per-state QFI alone does not settle that comparison.

### 51. “Is the benefit explained by higher purity, entropy or entanglement?”

**Intuition:** Purity describes a state at one field; QFI describes how the state changes when the field changes.

**Short answer:**

“None of those quantities alone determines the QFI. Two families can have the same purity at a field but different derivatives with respect to it. The relevant ingredient is distinguishability under field changes, after accounting for restricted access.”

**Follow-up:** A family of pure states can be completely constant and have zero QFI, or rotate with the field and have nonzero QFI, while purity remains one in both cases. Entanglement can matter in sensing but is not a substitute for evaluating the actual state family. Equal purity also does not imply equal preparation cost.

### 52. “What checks make you trust the thermal advantage?”

**Intuition:** Compare like with like, then check that the result survives numerical choices and obeys the physical information bounds.

**Short answer:**

“I compare the same geometry, accessible spins and field convention. The thesis evaluates local SLD QFI and checks it against the full parent family. The thermal advantage is reported for these finite-system curves, not as an asymptotic law.”

**Follow-up — checks to explain or perform when needed:** Check Gibbs normalization and positivity, derivative accuracy, eigenvalue tolerances, field-grid resolution and temperature conventions. Check pointwise data processing within each family:

$$
F_Q[\operatorname{Tr}_E\rho_{\beta,N}(h_x)]\leq F_Q[\rho_{\beta,N}(h_x)].
$$

Do not claim a numerical convergence sweep you have not documented. In the quoted beta-five example, the local maximum 4.847 is below the full thermal maximum 8.456; this is consistent with the bound but a comparison of maxima alone does not establish the pointwise inequality.

### A 30-second explanation to practise first

“At finite temperature the probe occupies several energy levels, with probabilities set by their energy differences. When the magnetic field changes, those probabilities and the energy eigenstates can change. That response can carry information even where the reduced ground-state response is weak. I compare these preparation families after restricting access to four spins. The advantage is specific to the field range and temperature; it is not a claim that arbitrary noise or heating improves the same sensor state.”

### Keep these three distinctions clear

- **Temperature is controlled; field is estimated.** Each plotted curve keeps beta fixed.
- **Global preparation comes before partial trace.** The discarded probe spins are not the preparation bath.
- **A thermal preparation family is not a fixed noisy processing of the ground-state family.** This is why the comparison does not violate QFI data processing.

Primary thesis references for this section: [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex), especially “What is being compared” and “Temperature sweep at fixed accessible size”; [NoiseAnalysisAppendix.tex](../TeXtured/chapters/NoiseAnalysisAppendix.tex) for parameter derivatives along matched-purity paths; [Methods.tex](../TeXtured/chapters/Methods.tex) for the separate dynamical circuit construction. The two-level example and proposed practical checks are explanatory additions, not new reported experiment results.

## Real quantum magnetometers and how to motivate the model

### 53. “What is an actual quantum magnetometer?”

**Intuition:** Use a magnetic-field-dependent quantum response as a calibrated indicator of the field.

**Short answer:**

“A quantum magnetometer uses a quantum system whose energy splittings or spin dynamics depend on the magnetic field. We prepare it, let it respond to the field, and read that response. An atomic-vapour magnetometer is a concrete example: optical measurements of atomic spins reveal the field.”

**Follow-up:** In a simple precession description, $\omega_L=\gamma B$. Measuring the frequency gives the field through a calibrated gyromagnetic ratio. This illustrates a real transduction mechanism; it is not the same preparation and interacting Hamiltonian as your Gibbs-state TFIM calculation. [NIST: atomic magnetometer principles](https://tf.nist.gov/ofm/smallclock/MAG_principles.html).

### 54. “Can you give an example already used in space?”

**Intuition:** The application is real even though the particular sensor architecture differs from your model.

**Short answer:**

“ESA's Juice spacecraft carries MAGSCA, a rubidium-based quantum sensor within its magnetometer instrument. It reads a magnetic-field-dependent resonance using optical pumping and quantum interference. That gives a concrete example of quantum magnetometry in a space mission.”

**Follow-up:** ESA reported commissioning measurements in space in 2023. This is evidence of a deployed quantum sensing principle, not a demonstration of your thermal Ising-chain mechanism. Do not imply that MAGSCA switches between the beta-two and beta-five responses in the thesis. [ESA: MAGSCA aboard Juice](https://www.esa.int/ESA_Multimedia/Images/2023/11/Quantum-based_MAGSCA_aboard_Juice).

### 55. “Could your periodic Ising model represent magnetometers around CERN?”

**Intuition:** Closing a line of interacting spins into a ring is a statement about their couplings, not just where the sensors are located.

**Short answer:**

“CERN provides a real application for precise magnetic-field measurements, but a set of probes distributed around an accelerator is not automatically a periodic Ising chain. My ring assumes particular interactions between neighbouring spins, including the first and last spins.”

**Follow-up:** A periodic TFIM has a closing interaction such as $-JZ_NZ_1$ in addition to the other neighbour couplings. Independent magnetometers positioned around a circular tunnel need not have any such interaction. They can also experience different local fields, whereas the illustrated model uses a common transverse field parameter. Use CERN to motivate the measurement task, not to justify the interaction graph.

A documented historical example is the use of NMR probes in LEP tunnel magnets for field monitoring and energy calibration. [CERN report](https://cds.cern.ch/record/359915).

### 56. “Why did you use a periodic Ising chain rather than a detailed instrument model?”

**Intuition:** A controlled small model lets you isolate the effects you want to understand before adding the details of a device.

**Short answer:**

“The interacting spin model lets me vary preparation, noise and restricted access while retaining an exact numerical reference. Periodic boundaries provide one controlled geometry and remove the end sites of an open chain. I use it as a sensing benchmark, not as a complete model of an existing instrument.”

**Follow-up:** Periodic boundaries do not remove finite-size effects. Realizing a similar sensor requires identifying physical spin degrees of freedom, engineering the assumed interactions, coupling the unknown field to the relevant operator, and implementing preparation and readout. The thesis's comparison of geometries does not establish that a physical ring is the best deployable device.

### 57. “Could temperature select a narrow sensitive region or a wider operating range in space?”

**Intuition:** Treat temperature as a preparation setting that changes the response curve, then choose a setting suited to the expected field region.

**Short answer:**

“The model suggests that possibility: different thermal preparations give different field-sensitivity profiles. If a physical probe realizes comparable dynamics and supports controlled thermal preparation, temperature could help match the response to its operating range. This is a design motivation, not a demonstrated spacecraft operating mode.”

**Follow-up:** The beta-two curve has an off-peak advantage over the reduced ground-state reference; beta five also has a higher peak. Neither result establishes that temperature can place the peak at any desired field or continuously choose any desired width. A real implementation needs calibrated energy scales, preparation time, temperature stability, readout and a defined field prior or operating interval. See thermal questions 39, 43 and 49–50.

### 58. “Can we initialize the probe thermally on Earth and then send it into space?”

**Intuition:** An initial state remembers how it was prepared; it does not automatically re-equilibrate to every new field encountered later.

**Short answer:**

“An initial thermal preparation alone would not realize the equilibrium family plotted in the thesis at every later field. The probe would need controlled re-preparation or equilibration in the local field. Otherwise, I must model its actual time evolution from the fixed initial state.”

**Follow-up:** A perfectly isolated probe under unitary evolution preserves its global eigenvalues. It cannot generally adjust those eigenvalues to the Gibbs weights of a new Hamiltonian merely because it moves to a new location. A bath can enable equilibration, but its coupling and relaxation time must be specified. For a rapidly changing field, a nonequilibrium sensing model may be needed. This is the distinction in question 48.

### 59. “Does heating an atomic magnetometer reproduce your Gibbs-state result?”

**Intuition:** A device's physical temperature can change many things besides the spin populations assumed in the model.

**Short answer:**

“Not automatically. An optically pumped atomic magnetometer actively prepares its spin state, so its sensing state need not be a Gibbs state of the field Hamiltonian. A temperature control in a real device cannot be identified with my model's beta without checking the preparation mechanism.”

**Follow-up:** Optical pumping in atomic magnetometers is described by [NIST](https://tf.nist.gov/ofm/smallclock/MAG_principles.html). The thesis's beta controls a specified equilibrium density matrix. Translating that result requires modelling the actual device rather than assuming that every heated quantum sensor has the same thermal response.

### 60. “How would you convert your QFI curves into sensitivity in tesla?”

**Intuition:** A model parameter must first be calibrated against a physical field; then preparation and measurement resources determine practical precision.

**Short answer:**

“I need the physical relation between the model's field parameter and the magnetic field in tesla. QFI transforms with the square of that parameter-conversion factor. I would then include the number of independent repetitions, cycle time and measurement efficiency.”

**Follow-up:** If the plotted parameter is $x=h_x/J$ and $x=x(B)$, with all other controls fixed,

$$
F_B=F_x\left(\frac{dx}{dB}\right)^2.
$$

The relevant coupling and energy scale must be specified before quoting a field precision. A dimensionless QFI peak by itself is not a sensitivity in tesla per square-root hertz, a response bandwidth, or an instrument specification. A wider interval of field values with useful QFI is also different from a wider temporal bandwidth.

## Channel model — hard questions

### 61. “If the complete channel is not identifiable, what is scientifically useful about your model?”

**Intuition:** A map of all possible failure stages can be useful even when the available observations locate only some of them.

**Short answer:**

“Its value is structural and diagnostic. It separates source preparation, optical propagation, accessible modes, measurement, readout and count statistics. This lets me state which quantities the present data identify, calculate conditional information loss at explicit checkpoints, and specify the calibrations a future experiment would need.”

**Follow-up:** The model preserves normalization by retaining vacuum or failure outcomes, separates QFI from measurement-dependent CFI, and avoids interpreting detector processing as a change to the optical state. It is also modular: a measured transfer matrix or loss calibration can replace a provisional stage without rebuilding the whole inference pipeline. The experimentally supported result is the population-level mean response and a conditional throughput scale, not reconstruction of the complete optical channel.

**Avoid:** Calling the model a uniquely reconstructed or fully validated apparatus description. A good phrase is **“a physically structured forward model and sensitivity workbench.”**

### 62. “Why did you choose this order of channels? Would another order change the result?”

**Intuition:** Rotating a state and then removing coherence need not give the same result as removing coherence and then rotating it.

**Short answer:**

“The order represents one plausible physical sequence from propagation to measurement. Some stages, such as dephasing, coherent mixing and mode-dependent loss, do not generally commute, so changing their order can change the predicted probabilities. The archived aggregate counts do not identify that order.”

**Follow-up:** The chosen sequence should therefore be read as part of the provisional workbench. A calibrated apparatus model could replace, remove or reorder stages. The stable contribution is the framework that keeps those assumptions explicit and propagates them to QFI, CFI and counts. Testing alternative orders would be a useful robustness analysis, but it was not used to claim a uniquely identified optical mechanism.

### 63. “Are the erasure and failure maps actually valid quantum channels?”

**Intuition:** Probability that disappears from the measured modes must go somewhere in the enlarged output space.

**Short answer:**

“Yes, when they are defined on an enlarged Hilbert space containing orthogonal vacuum or failure states. Their Kraus operators transfer the missing probability into those states, making the maps completely positive and trace preserving.”

**Follow-up:** A linear expression for the common erasure map is

$$
\mathcal S_\eta(X)
=\eta X+(1-\eta)\operatorname{Tr}(X)
|\mathrm{vac}\rangle\langle\mathrm{vac}|.
$$

For a normalized input state this reduces to $\eta\rho+(1-\eta)|\mathrm{vac}\rangle\langle\mathrm{vac}|$. Similarly, modal loss can use a transmitted operator $L=\sum_j\sqrt{\tau_j}|HG_j\rangle\langle HG_j|$ together with failure Kraus operators $\sqrt{1-\tau_j}|\mathrm{fail}\rangle\langle HG_j|$. Keeping the failure branch prevents hidden postselection and preserves total probability.

### 64. “Did you demonstrate that detector cross-talk is the main information bottleneck?”

**Intuition:** A result inside an assumed model tells us what would happen if that model were correct; it does not by itself establish that the apparatus has that mechanism.

**Short answer:**

“I demonstrated that it is the dominant bottleneck within the stated conditional model. The value $\chi=0.0035$ comes from an external calibration, while symmetry of the complete confusion matrix is assumed. The aggregate stream cannot independently validate that full readout map.”

**Follow-up:** The result is still useful because it shows how even small leakage from a bright $HG_0$ port can overwhelm a weak first-order signal, especially near zero separation. Experimentally establishing that this is the dominant loss would require a measured transfer matrix from known injected modes, resolved output ports and background calibration. Describe the reported QFI/CFI ratios as **conditional information-retention calculations**, not a measured decomposition of the instrument's information loss.

### 65. “How did you construct the assumed source density matrix?”

**Intuition:** Each detected photon is attributed either to the centred bright source or to the displaced faint source. We mix those alternatives as probabilities because the two sources have no stable relative phase.

**Short answer:**

“I modelled the star and planet as two mutually incoherent point sources with a Gaussian point-spread function. Conditional on a one-photon event, the centred star prepares the fundamental HG mode, while the displaced planet prepares a displaced Gaussian expanded in the HG basis. Their relative intensities give the weights of a statistical mixture.”

**Follow-up:** With the star defining the origin and $\epsilon$ the faint-source fraction,

$$
\rho_S(d_a,\epsilon)
=(1-\epsilon)|HG_0\rangle\langle HG_0|
+\epsilon|\psi_{d_a}\rangle\langle\psi_{d_a}|.
$$

For the one-axis scan,

$$
|\psi_{d_a}\rangle
=\sum_{n=0}^{\infty}e^{-q/2}
\frac{\alpha^n}{\sqrt{n!}}|HG_n\rangle,
\qquad
\alpha=\frac{d_a}{2},
\qquad q=|\alpha|^2.
$$

Therefore the displaced-source modal probabilities are $e^{-q}q^n/n!$, and the ideal aggregate first-order probability is $p_1=\epsilon q e^{-q}$ in the one-axis model. Mutual source incoherence removes terms such as $|HG_0\rangle\langle\psi_{d_a}|$, but the projector $|\psi_{d_a}\rangle\langle\psi_{d_a}|$ can still contain off-diagonal HG coherences. The state has rank at most two even though the displaced wavefunction has support on infinitely many HG modes.

**Numerical implementation:** The infinite HG expansion was evaluated with a finite cutoff and an explicit tail or complement outcome. Increasing the maximum order from 8 to 12 changed the calculated QFI by at most $5.1\times10^{-12}$ relative over the validation grid, so the reported result was not controlled by the cutoff. The construction assumes a Gaussian PSF, known programmed $d_a$ and $\epsilon$, mutual incoherence, and bright-source alignment; those are source-model assumptions rather than quantities reconstructed from the aggregate counts.

### 66. “How did you test the channels in practice? Did you generate synthetic data?”

**Intuition:** We tested whether the assumed mechanism gives coherent forward predictions and whether the observable statistical layer predicts held-out data. We did not recover every hidden mechanism from one aggregate detector stream.

**Short answer:**

“I numerically propagated the source density matrix through the assumed channel sequence, converted the output probabilities into predicted counts, and compared the population-level predictions with the experimental setting means. I also removed individual channel effects in identity ablations. Synthetic count datasets were generated for bootstrap goodness-of-fit tests of the statistical count models, but not to claim recovery of all quantum-channel parameters.”

**Follow-up — four distinct checks:**

1. **Forward simulation.** For every $(d_a,\epsilon)$, the code constructed $\rho_S$, applied the assumed displacement or jitter, dephasing, coherent mixing, modal loss and accessible-mode maps, performed the SPADE POVM, applied classical readout confusion, and converted the resulting probability into an expected count. Provisional optical parameters were fixed; throughput, background, offset and calibration terms were fitted.
2. **Identity ablations.** Individual effects were replaced by their identity limits—for example zero jitter, no dephasing, no mixing, unit transmission or no confusion—and the downstream fit was repeated. This measured sensitivity of inferred quantities such as throughput to each assumption. It did not identify the corresponding physical mechanism.
3. **Held-out real-data prediction.** Grouped five-fold tests held out checkerboard cells, complete displacement rows and complete source-ratio columns. The target was the mean of the 100 real counts at each setting. This tested interpolation and structured prediction of setting means, not process tomography or the full single-count distribution.
4. **Synthetic and resampled counts.** Parametric bootstraps generated discrete synthetic datasets from fitted NB1, Poisson--lognormal or benchmark models, refitted each dataset, and compared simulated discrepancies with the observed discrepancy. These tests rejected the tested models as complete descriptions of the individual $10\,\mathrm{ms}$ counts. The empirical bootstrap instead resampled the 100 observed repetitions within each setting; those are resampled measurements, not fully synthetic observations.

**Additional numerical checks:** The source and channel calculations retained normalization through vacuum or failure outcomes. SLD QFI agreed with an independent finite-fidelity calculation to within a maximum relative difference of $0.322\%$ at the tested nonzero settings, and the HG-cutoff convergence check was much smaller than the reported effects.

**Avoid:** “Synthetic data validated the physical channels.” The correct conclusion is: **“Forward simulations, ablations and consistency checks tested the assumed channel implementation; held-out data validated the mean-response layer; the individual optical channels remain unidentifiable from the archived aggregate counts.”**

### Suggested wording for the slide and spoken transition

**Real-world motivation — one possible slide line:**

“Quantum magnetometry in space: MAGSCA aboard ESA's Juice.”

Use the ESA source above if this factual example is placed on a slide. Keep it visually separate from the Ising-ring schematic so it does not imply that MAGSCA is built from your model.

**One sentence to explain the schematic:**

“The periodic Ising chain is a controlled model of an interacting quantum probe.”

**For the thermal-result slide — a prospective design lesson:**

“Temperature as a preparation control: matching sensitivity to the expected field range.”

**A short spoken bridge:**

“Quantum magnetometers are already relevant to space missions. Here I use a controlled interacting-spin model to ask a preparation question: can changing temperature give a response better suited to the expected field range? The curves show that it can in this model, while a physical implementation would require its own preparation and readout analysis.”

Avoid calling the ring “a magnetometer around CERN” or saying “we heat the space sensor to choose any peak or range.” Those claims go beyond the model. The existing slide files have not been changed by this addition.

## How to practise

Answer the first sentence directly, give one physical or statistical reason, then pause. Do not deliver every caveat before answering the question. If asked for an unmeasured quantity, distinguish what is known from what would need a new experiment.

For your first rehearsal, take questions 1, 7, 8, 14, 18 and 21 in random order. Aim for 20–40 seconds per short answer. Use the equations only for a follow-up.

Most thesis-specific answers above are grounded in [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex), [ExoplanetExperimentAppendix.tex](../TeXtured/chapters/ExoplanetExperimentAppendix.tex), [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex), [Methods.tex](../TeXtured/chapters/Methods.tex), [VQSE.tex](../TeXtured/chapters/VQSE.tex), and [Conclusions.tex](../TeXtured/chapters/Conclusions.tex). Suggested future tests are explicitly prospective.
