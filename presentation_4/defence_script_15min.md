# Thesis defence — 15-minute speaking script

**Luca Manzi · English · presentation_4 · 19 main slides**

Read only the **Spoken script** sections aloud. Bracketed directions are silent cues. **Details to keep in mind** are preparation for questions, not additional material for the timed talk. The spoken text is approximately 1560 words. Timings include pointing, slide changes and short pauses; rehearse aloud to calibrate them to your pace. Do not read the equations in the technical notes symbol by symbol.

This script follows the current main deck. The detailed sections after each spoken passage are preparation material and are not intended to be delivered verbatim.

The central thread is: **a sensor must retain useful sensitivity through preparation, restricted access and measurement, over the range where it will operate.**

## Timing map

| Slide | Topic | Duration | Clock |
|---|---|---:|---|
| 1 | Opening | 0:30 | 0:00–0:30 |
| 2 | Two applications | 0:30 | 0:30–1:00 |
| 3 | Classical Fisher information | 0:50 | 1:00–1:50 |
| 4 | Measurement animation and QFI | 1:00 | 1:50–2:50 |
| 5 | Mixed states and spectral estimation | 1:05 | 2:50–3:55 |
| 6 | Numerical and circuit pipeline | 1:05 | 3:55–5:00 |
| 7 | Magnetometry divider | 0:05 | 5:00–5:05 |
| 8 | Magnetometer model | 0:55 | 5:05–6:00 |
| 9 | Broader thermal sensitivity | 1:00 | 6:00–7:00 |
| 10 | Stronger thermal peak | 0:55 | 7:00–7:55 |
| 11 | Exoplanet divider | 0:05 | 7:55–8:00 |
| 12 | Imaging problem and SPADE | 0:50 | 8:00–8:50 |
| 13 | Mode probabilities and cross-talk | 0:45 | 8:50–9:35 |
| 14 | Available data and the original TQFI goal | 1:05 | 9:35–10:40 |
| 15 | From probabilities to quantum states | 0:45 | 10:40–11:25 |
| 16 | Physical source state | 0:45 | 11:25–12:10 |
| 17 | The receiver as a channel sequence | 0:55 | 12:10–13:05 |
| 18 | Mean-response result and implications | 1:00 | 13:05–14:05 |
| 19 | Conclusions | 0:55 | 14:05–15:00 |

## Slide 1 — Opening

### Spoken script

Good morning. My thesis studies how to assess the sensitivity of quantum sensors when we include the conditions under which they actually operate.

The work was developed in collaboration with the Italian Space Agency. 

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** 
- The magnetometer is a numerical model and a circuit-method benchmark. The optical application uses a completed laboratory experiment motivated by exoplanet imaging; it is not an astronomical detection of a real exoplanet.
- Your contribution combines implementations, numerical studies, data interpretation and a future proposal. These have different evidential status throughout the talk.

## Slide 2 — Applications

### Spoken script
The question I tried to answer is: how much information about an unknown parameter can we actually access?

I will connect two applications: 
- quantum magnetometery, where I aim to estimate a magnetic field using an interacting spin model
- and a problem of exoplanet detection, where I need to resolve a faint source which is very close to a bright star, using spatial mode measurements

To approach these applications I developed a common workflow which combines numerical simulation, quantum circuits and experimental data

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** The magnetometer asks “what happens when I change the design?” The optical record asks “what can these particular measurements tell me about the design?”

The two applications do not both demonstrate experimental TQFI. The numerical study benchmarks metrological quantities; the archived optical counts do not reconstruct an optical state or its TQFI. Presenting this asymmetry explicitly strengthens the scientific story.

## Slide 3 — Classical Fisher information

### Spoken script

Before discussing the applications, we need to introduce some concepts, for example fisher information.

[Point to the probability distributions.]

An unknown parameter, such as a magnetic field, determines the distribution of possible measurement outcomes.

Consider a small change in the parameter.

We can have different situations: on the left this change barely changes the distribution, so the measurement tells us very little, while in the right case the same change produces a distinguishable response, so the measurement is more informative.

Fisher information quantifies the sensitivity of the distribution to this parameter. So it is how much information a specific fixed measurement reveals about an unknown parameter.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Imagine two slightly different field values. If their outcome distributions overlap almost completely, many repetitions are needed to tell them apart. Fisher information quantifies local distinguishability, not brightness alone.

For a fixed measurement with probabilities (p(x\mid\theta)),

$$
F_C(\theta)=\sum_x\frac{[\partial_\theta p(x\mid\theta)]^2}{p(x\mid\theta)}.
$$

The classical Cramér–Rao bound is $\operatorname{Var}(\hat\theta)\geq 1/[N F_C(\theta)]$ for $N$ independent repetitions and an appropriate locally unbiased estimator, under regularity assumptions. Large Fisher information is a precision benchmark, not a guarantee that an arbitrary finite-sample estimator attains the bound. “Local” means around a parameter value; it does not establish global identifiability.

Source: [MathBackground.tex](../TeXtured/chapters/MathBackground.tex).

## Slide 4 — Fisher information and measurements

### Spoken script

[Start at zero degrees. Point to the two coloured vectors.]

Let's visualize how fisher information changes.

These vectors illustrate states at two parameter values. Keep the states fixed, and rotate only the measurement basis, where we project those states.

[Advance through thirty and forty-five degrees.]
[Advance through sixty and seventy-five degrees.]

The classical Fisher information increases as the projections are farther away (the states are more distnguishable).


[Advance to ninety degrees. Pause at the meeting of the curves.]

Here, the CFI reaches the maximum, that defines the quantum Fisher information, which is the best local sensitivity available from the state over all measurements. The key takeway is that QFI is intrinsic to the quantum state and it's independent on the measurement basis.

The state has not become more informative. We have become better at reading it.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Think of looking at a small movement from different directions: one view may hide a change that another reveals. The quantum example concerns changes in outcome probabilities, not literally a two-dimensional geometric shadow.

The current animation uses **mixed states**, with Bloch radius $r=0.8$, and evaluates Fisher information locally at $\theta=0$. For the illustrated equatorial family,

$$
\rho_\theta=\tfrac12[I+r(\cos\theta\,\sigma_x+\sin\theta\,\sigma_z)],
\qquad
F_Q=r^2=0.64,
$$

$$
F_C(\varphi)=\frac{r^2\sin^2\varphi}{1-r^2\cos^2\varphi}.
$$

- The two vectors have a visible finite separation for illustration. The plotted information is **not** computed as their finite difference.
- At the initial basis, probabilities have zero first derivative at the reference point. They can still change at second order over a finite displacement.
- For $r<1$, the CFI depends on the measurement basis as shown. In the pure-state limit $r\to1$, generic projective bases in this plane attain the QFI; singular zero-probability settings require care with limits.
- The optimal basis can depend on the unknown parameter. Local attainability does not imply one globally optimal, immediately known measurement.

Reference: Appendix J of the deck and [measurement_overlay.tex](assets/measurement_overlay.tex).

## Slide 5 — Mixed states

### Spoken script

We also have to introduce mixed states. They are statistical mixtures of quantum states, described by a density matrix, used to describe real quantum sensors.

Why study them? Real sensors interact with their environment, and may be only partially accessible. Mixed states exact QFI is hard to compute and is less explored in the literature.



How: we use a truncated density matrix

[Point to the truncated density matrix.]

considering only the dominant $m$ eigenvalues lambda and eigenvectors $\psi$

This is similar to PCA.

To do that on quantum computers, we use a VQSE, the Variational Quantum State Eigensolver, a quantum circuit.

With the truncated density matrix we compute the TQFI, Truncated Quantum Fisher Information, which gives the upper and lower bounds of the QFI.

Intuitively, we compare nearby states using a compact spectral description to estimate how distinguishable they are.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Fidelity is a similarity measure for states. We estimate how quickly nearby states become distinguishable, using selected spectral components and accounting for the part we did not retain. Truncation simplifies the description; it is not permission to ignore its uncertainty.

$$
\rho_m=\sum_{i=1}^{m}\lambda_i|v_i\rangle\langle v_i|,
\qquad \lambda_1\geq\cdots\geq\lambda_d.
$$

- A mixed state need not represent ignorance about a unique underlying ensemble: ensemble decompositions are nonunique. Entanglement with an unobserved system also produces a mixed reduced state.
- **Truncation is a chosen computational strategy, not a requirement for describing mixed states.** The matrix above is generally subnormalized: $\operatorname{Tr}\rho_m\leq1$. Renormalizing it would change the quantities entering the stated bounds.
- Large eigenvalue weight does not automatically mean that all parameter sensitivity is retained. Dependence of both eigenvalues and eigenvectors matters.
- The thesis treats truncated-fidelity and generalized-fidelity bounds at finite displacement; their local-QFI interpretation requires the appropriate small-displacement limit. TQFI is not simply “calculate ordinary QFI after deleting small eigenvalues.” Use Appendix A if challenged.
- VQSE changes the measurement basis, not the input state's eigenvalues. Its numerical outputs are approximate and depend on ansatz expressivity, optimization and sampling. The established method is from the literature; your contribution is its implementation, benchmarking and integration.
- The introduction calls mixed-state QFI less explored. Do not turn that into “nobody has studied mixed states.”

Sources: [Methods.tex](../TeXtured/chapters/Methods.tex), [VQSE.tex](../TeXtured/chapters/VQSE.tex).

## Slide 6 — Parallel numerical and quantum-circuit workflow

### Spoken script

This is the computational structure I developed.

It follows two parallel flows: a numerical simulation and a quantum circuit. 

First we make a starting state evolve with a Hamiltoninan

Then to have a mixed state, we restric access: in the numerical simulation we take a partial trace, in the quantum circuit we ignore some qubits.

Then we compute the spectrum (which as we said in the quantum circuit case is done with VQSE) and with this we compute the lower bound of the QFI.

The two flows are designed to be interchangable at every checkpoint.

I also tested a natural-gradient update on  VQSE benchmark. The intuition is to scale parameter updates by how much they change the quantum state.

Fisher geometry therefore plays two roles: it quantifies distinguishability for sensing, and it can guide the optimization used in spectral estimation.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** A training parameter is a knob. Equal turns of two knobs need not move the quantum state equally far. Natural gradient accounts for that unequal effect when choosing an update; the sensing QFI and the training metric refer to different parameters.

- Partial trace obeys ($\rho_S=\operatorname{Tr}_E\rho_{SE}$). Marginal measurement statistics on $S$ agree whether $E$ is traced out mathematically or simply unobserved. Conditioning on an outcome in $E$ is a different operation.
- Interchangeable implementations do **not** imply interchangeable stage order; channels generally do not commute.
- Exact matrix calculations, Trotterized dynamics and variational spectral estimation have different approximation errors. “Validated against numerical references” is more defensible than an unconditional “perfectly matching.”
- Unitary evolution of a pure state does not prepare a global Gibbs state. The dynamical circuit example and the ground/Gibbs preparation branches are distinct.
- Do not claim a demonstrated hardware quantum advantage. This establishes and benchmarks a route to variational estimation.
- The updated VQSE benchmark compares BFGS, Adam and a deterministic damped Bures natural gradient on a small mixed-state problem. It supports a scoped numerical comparison, not a general speedup claim.
- Natural gradient uses a state-space metric, whereas Newton's method uses the objective Hessian. The relevant metric is with respect to trainable ansatz parameters, not the sensed magnetic field. Here the Bures metric treats the mixed output state directly; a scalable hardware version would need an appropriate sampled estimator. See Appendices B and C.1 and [VQSE.tex](../TeXtured/chapters/VQSE.tex).

Source: [Methods.tex](../TeXtured/chapters/Methods.tex).

## Slide 7 — Quantum Magnetometry

### Spoken script

Let me first show what this framework tells us about a quantum magnetometer.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Use this divider as a breath and a change of subject. There is no extra concept to explain here.

This is a transition slide. Advance immediately after the sentence.

## Slide 8 — A noisy quantum magnetometer

### Spoken script

Quantum magnetometry has real applications: NMR probes monitored accelerator fields at CERN's LEP, and ESA's Juice carries a rubidium-based quantum magnetometer.

Here I use a controlled interacting-spin model, the transverse-field Ising chain. The ring represents spin couplings, not probes placed around an accelerator.

[Point to the six sites, then the two dashed sites.]

The field changes the probe state. Of six spins, only four are accessible; tracing out the other two can leave a mixed state.

I compare ground-state preparation, thermal preparation and depolarization. The aim is to understand which preparation gives useful sensitivity over the intended field range.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** A reduced state gives exactly the predictions needed for measurements on the spins you can access, even when those spins are correlated with the rest. It is not the state obtained by physically removing two spins and allowing the remaining system to re-equilibrate.

The plotted examples use (N=6), (n=4), periodic boundaries and (J=1). The general methods chapter also discusses open chains; do not mix their Hamiltonian summation limits with this ring.

For a fixed, parameter-independent partial trace or noise channel, QFI cannot increase. More accessible qubits can recover information hidden in the larger probe. However, changing the **preparation family** is not an application of that same data-processing comparison.

This is a finite model: say “sensitivity peak” or “near the critical region,” not a true finite-system thermodynamic singularity. Here “local QFI” may also refer to the accessible subsystem; distinguish that from locality in the estimated parameter when answering questions.

Real-instrument references: [CERN's LEP NMR probes](https://cds.cern.ch/record/359915) and [ESA's MAGSCA aboard Juice](https://www.esa.int/ESA_Multimedia/Images/2023/11/Quantum-based_MAGSCA_aboard_Juice). These motivate magnetometry; neither is presented as a realization of the thermal Ising-chain model.

Source: [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex).

## Slide 9 — Thermal preparation broadens the sensitive range

### Spoken script

Here, white is the reduced ground-state reference and green is the reduced thermal preparation at inverse temperature beta equal to two.

[Point first to the white maximum, then to the shaded region on the right.]

The thermal state does not win at the highest ground-state peak. Its advantage appears away from that optimum, where the green curve remains above the white curve.

Imagine that the field is not known well enough to place the sensor exactly at its best operating point. A narrow, high peak may be less useful than a response that remains informative across the relevant interval.

For a future space sensor with controlled thermal preparation, this could motivate choosing temperature to match the expected field range.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** A sharp peak is useful when you know where to operate. A wider useful response can matter when the field is uncertain. The plots illustrate that trade-off; they do not compute a universal optimum over unknown fields.

- ($\beta=1/(k_B T)$): larger beta means lower temperature. Plot labels use ($\beta J$); the numerical convention is ($J=1$).
- The global Gibbs state ($e^{-\beta H(h_x)}/Z(h_x)$) is prepared **before** tracing out two spins. It is not generally the Gibbs state of the isolated four-spin Hamiltonian.
- The shaded region marks pointwise higher QFI in this example. You did not establish a globally optimal Bayesian or minimax preparation for an arbitrary prior over fields. “Useful when the field is uncertain” is a design interpretation of the curves, not a completed prior-weighted optimization.
- Thermal populations depend on the field; this can supply information in addition to changes of eigenvectors. This is not evidence that arbitrary heating or parameter-independent noise improves QFI.

Sources: [NoiseAnalysis.tex](../TeXtured/chapters/NoiseAnalysis.tex), [NoiseAnalysisAppendix.tex](../TeXtured/chapters/NoiseAnalysisAppendix.tex).

## Slide 10 — Cooling strengthens the sensitivity peak

### Spoken script

Now I lower the temperature, increasing beta to five.

[Point to the green peak.]

For this preparation and accessible subsystem, the thermal peak is also higher than the reduced ground-state peak.

The intuition is that low-energy excited states are not necessarily useless background. Their populations change with the magnetic field, and that change can carry information.

Together, these plots show two possible benefits: broader sensitivity away from the ground-state optimum, or stronger sensitivity around a favourable operating region.

This is not a universal claim that mixed states are better. It shows why preparation must be evaluated against the intended sensing task, rather than judged only by purity or by proximity to the ground state.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Thermal preparation gives several energy levels field-dependent populations. Those populations can act as additional indicators of the field. Their benefit must be compared with the other changes caused by temperature.

For the reported (N=6,n=4,\beta=5) periodic example, the thesis gives a 23.5% higher peak. Keep this as a question-answer detail; the main slide deliberately avoids large numerical callouts.

The comparison is between the **reduced ground-state family** and the **reduced globally thermal family**. Both accessible states can be mixed. The field derivative acts on the field-dependent Gibbs preparation, including its populations. No fixed noisy processing of the same ground-state family is claimed to increase QFI. The preparation resources and equilibration time are not optimized by these plots.

## Slide 11 — Exoplanet Detection

### Spoken script

The second application moves from a controlled sensor model to an optical experiment.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** This divider changes the physical platform while preserving the question about accessible information.

Change pace slightly; this is the start of the second application, not a new mathematical introduction.

## Slide 12 — The exoplanet problem

### Spoken script
Consider a bright star and a faint exoplanet.

To detect the exoplanet we can use direct imaging, which records photon positions. If they are separated enough, they can be resolved, if they are too close, the rayleigh diffraction limit prevents us from resolving the two intensities.

A better approach is sorting the light into spatial modes, to clearly separate the contirbution of the star and the exoplanet.

This connects to the earlier measurement animation: changing the measurement basis can reveal information that another measurement misses.

As mode sorter we used SPADE.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** The optical sorter combines amplitudes before detection. That changes what is measured; merely processing the resulting camera intensities differently would not generally implement the same measurement.

The sorter outputs are labelled by modes. The companion also contributes to the fundamental mode. Neither output labels which source emitted the photon.

SPADE does not defeat all diffraction limits or identify the source of each photon. Its advantage is parameter- and model-dependent measurement sensitivity. Alignment, brightness ratio, throughput, background and readout matter.

Mutual incoherence of star and companion does not mean that their spatial density matrix is diagonal in an arbitrary HG basis. An individual displaced source occupies a coherent superposition of HG modes; an incoherent source mixture can retain off-diagonal entries in that basis.

Sources: [Astrophysical.tex](../TeXtured/chapters/Astrophysical.tex), [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex).

## Slide 13 — SPADE, Hermite-Gauss modes and cross-talk

### Spoken script

SPADE maps the spatial photon wavefunction into spatial Hermite-Gaussian modes.

With SPADE aligned to the star, most of the bright light enters the fundamental mode. We define the probability of this outcome as $p_0$

The exoplanet contributes to higher modes, we define $p_1$ the probability of the two first-order modes.

[Point to the fundamental and first-order modes.]

There's a probability that a detector confuses the modes. We model this with a classical cross-talk channel, with probability $\chi$.

The reported first-order exoplanet signal therefore might include some events from the star.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Suppose an illustrative acquisition sends 10,000 events to the fundamental outcome and 10 to the first-order outcome. A 0.1% leak from the bright outcome contributes about 10 false first-order events—already comparable to the weak signal. These are illustrative numbers, not the measured dataset.

For ideal mode outcomes,

$$
p_0=\operatorname{Tr}(M_0\rho),\qquad
p_1=\operatorname{Tr}(M_1\rho),
$$

$$
M_0=|HG_{00}\rangle\langle HG_{00}|,\qquad
M_1=|HG_{01}\rangle\langle HG_{01}|+|HG_{10}\rangle\langle HG_{10}|.
$$

The slide uses an assumed symmetric readout model. The pair $(\chi,1-\chi)$ gives the weights for reporting outcome 1 from inputs 0 and 1. It is one row of the full confusion matrix, not a quantum state or a complete channel by itself.

The symmetric readout assumption gives

$$
p_1^{\rm rep}=\chi p_0+(1-\chi)p_1.
$$

- The companion also contributes to (HG_{00}). Neither port exclusively identifies photon origin.
- Higher modes and loss require an additional outcome; generally $p_0+p_1\neq1$ unless a binary normalization/conditioning convention has explicitly been imposed.
- Chi here is **classical reported-port confusion**, not coherent amplitude mixing. The latter requires a pre-measurement optical model.
- The thesis takes 0.0035 from an external reported cross-talk calibration. Equal reverse leakage and an unaffected failure outcome are assumptions, not a fully measured transfer matrix.
- A fixed classical post-processing channel can reduce CFI but does not change the pre-measurement state's QFI.

## Slide 14 — What the experiment recorded

### Spoken script

The ASI Matera simulated the system in the lab with lasers. 
They collected first order counts, at different relative intensities $\epsilon$ and separation $d$.

[Point to the individual acquisition and the averaged map.]

I developed a quantum channel model connecting the optical state to the recorded counts.

With further calibration this framework could help designing a basis better suited to the actual receiver

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Repeating the same measurement sharpens the mean without necessarily telling you more kinds of things. A hundred repeated totals do not automatically reveal the separate contributions to each total.

The record has 525 settings, 100 repetitions per setting and 10 ms per exposure: 52,500 observations, not necessarily 52,500 photons. Separate ($HG_{00}$), ($HG_{01}$), ($HG_{10}$), higher-mode and loss records are absent.

Without an independent incident-flux calibration, count scale does not separate flux from efficiency. Without basis rotations or phase-sensitive observables, the record does not identify HG coherences. Repetition improves knowledge of the measured mean but does not add a new kind of observable.

The experimental TQFI protocol is not identifiable from this record. This does not prevent a conditional TQFI calculation from an assumed state and channel model. The fitted quantities describe the observed count response. They do not determine the complete optical channel.

## Slide 15 — From probabilities to quantum states

### Spoken script

[Move from left to right.]

Let us connect probabilities with quantum states.

For two modes, we collect their classical probabilities in a vector. We can also write those probabilities on the diagonal of a density matrix.

But an optical state can have additional entries: coherences between those modes. The same populations can therefore belong to different quantum states.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Modal probabilities describe how often outcomes occur. Coherences describe relations between modal amplitudes that a different measurement can reveal. Rewriting the probability vector as a diagonal matrix does not recover these relations.

The slide uses two **individual** modes, labelled $a$ and $b$, with

$$
q_a,q_b\geq0
\qquad
q_a+q_b=1
\qquad
|c|^2\leq q_aq_b
$$

The last condition ensures positivity of the two-mode density matrix. The symbols $q_a,q_b$ are illustrative mode populations, not the scalar displacement quantity $q=d_a^2/4$ used in the source model.

- These are not the measured pair $(p_0,p_1)$ from slide 13. There, $p_1$ combines two first-order modes and further modes or failure events may remain. The full receiver keeps a complement outcome.
- The middle and right panels compare possible state descriptions. They are not successive physical operations that create coherence from measured counts. Setting $c=0$ is one possible state compatible with these populations.
- The probabilities belong on the diagonal of a **state**. The classical transition probabilities belong in the **channel matrix**. Do not embed the weights $(\chi,1-\chi)$ and describe the result as the optical state.
- The two-mode readout example is

$$
R_\chi=
\begin{pmatrix}
1-\chi&\chi\\
\chi&1-\chi
\end{pmatrix}
\qquad
\boldsymbol q^{\rm rep}=R_\chi\boldsymbol q
$$

- In the actual low-mode model, the corresponding three-outcome matrix leaves the failure outcome unchanged. Both the symmetry and that isolation are assumptions.
- A stochastic matrix fixes only the classical transition probabilities. It does not determine how a quantum channel acts on coherences. Appendix F gives an explicit quantum extension and explains its non-uniqueness.
- A density matrix is a state. A quantum channel $\mathcal E$ is a map acting on density matrices. Merely writing a probability vector as a diagonal matrix does not specify such a map.

Source: [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex), classical and quantum descriptions. Appendix F of the deck gives the technical extension.

## Slide 16 — The optical source state

### Spoken script

Where do those coherences come from in this experiment?

[Point to the two source contributions.]

The star and exoplanet are independent sources, so we describe them as a statistical mixture.

However, the exoplanet wavefunction, which is a sum of several HG modes, might contain coherences.

The collected $p_1$ is proportional to the trace of $\psi_{d_a}$, so it has no information on the coherences.

In this way we have defined the optical state that enters SPADE.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Each photon is attributed probabilistically to one of two mutually incoherent sources. Mutual incoherence removes interference between the source alternatives; it does not remove the spatial-mode structure of each source.

The conditional one-photon source model is

$$
\rho_S(d_a,\epsilon)
=(1-\epsilon)|HG_{00}\rangle\langle HG_{00}|
+\epsilon|\psi_{d_a}\rangle\langle\psi_{d_a}|.
$$

For the one-axis Gaussian model,

$$
|\psi_{d_a}\rangle
=\sum_{n=0}^{\infty}c_n(d_a)|HG_n\rangle,
\qquad
c_n=e^{-q/2}\frac{\alpha^n}{\sqrt{n!}},
\quad \alpha=\frac{d_a}{2},\quad q=|\alpha|^2.
$$

The ideal first-order population is consequently $p_1=\epsilon q e^{-q}$ in the one-axis convention.

- There are no cross terms $|HG_{00}\rangle\langle\psi_{d_a}|$ between the two source alternatives.
- The term $|\psi_{d_a}\rangle\langle\psi_{d_a}|$ can nevertheless contain off-diagonal HG terms $|HG_m\rangle\langle HG_n|$ for $m\neq n$.
- The density matrix has rank at most two even though the displaced spatial wavefunction has support on infinitely many HG modes. Rank and basis support are different concepts.
- The numerical calculation uses a finite HG cutoff and a complement outcome. Cutoff convergence was checked independently.
- The slide is conditional on a Gaussian PSF, known programmed $d_a$ and $\epsilon$, mutual source incoherence and alignment to the bright source.

Sources: [Astrophysical.tex](../TeXtured/chapters/Astrophysical.tex), [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex).

Here $\epsilon=I_B/(I_A+I_B)$ is the faint-source photon fraction. The contrast $I_B/I_A$ approximates it only when the companion is much fainter. The model uses $d_a=d/w_0$ for dimensionless separation.

## Slide 17 — From the optical state to counts

### Spoken script

Now we describe what happens to the optical state when it goes through SPADE and the detector.

[Follow the sequence from left to right.]

What happens before the optical state enters SPADE is described by a series of quantum channels, that include loss, alignment and changes to the modes.

Then SPADE produces outcome probabilities. After the measurement, readout cross-talk and background and calibration then determine the predicted mean counts.

The benefit is that each physical effect has its own place.

We computed the QFI at each step to asses where we are losing the most information. As a result we found that after the cross-talk effect, the ratio CFI/QFI drops from 90% to 57%.



### Details to keep in mind

Detailed examples are in Appendices P--R. Appendix P separates optical dephasing from classical readout, Appendix Q follows a physical photon-loss channel through to the fitted count response, and Appendix R shows the complete receiver flow. The main slide shows only the stage ordering and physical roles.

**Intuition — preparation only, not extra spoken text:** A probability vector records the diagonal seen by one measurement. A quantum channel is needed when the device can also change the off-diagonal information that another measurement could reveal.

In a two-mode illustration,

$$
\rho=\begin{pmatrix}q_a&c\\c^*&q_b\end{pmatrix},
\qquad
\mathcal D_v(\rho)
=\begin{pmatrix}q_a&vc\\vc^*&q_b\end{pmatrix}.
$$

The dephasing example uses a real visibility $0\leq v\leq1$. A direct HG measurement sees the same populations before and after this map. A later coherent mode transformation can turn coherence into a population difference. With a known transformation and suitable inputs, populations can therefore carry indirect information about dephasing. The present aggregate record and incomplete calibration do not identify $v$ independently.

Classical readout cross-talk instead acts on the measurement output:

$$
\boldsymbol p^{\rm rep}=R_\chi\boldsymbol p,
\qquad
p_1^{\rm rep}=\chi p_0+(1-\chi)p_1.
$$

Other stages remain part of the complete receiver model:

- Before measurement: common loss, alignment or jitter, dephasing, coherent mode mixing, mode-dependent loss and accessible-mode reduction.
- Measurement: $p_y=\operatorname{Tr}(M_y\rho)$.
- After measurement: readout confusion, additive background, calibration variation and repeated-count statistics.
- A background parameter may contain dark counts, ambient background or unresolved leakage; the current record cannot separate them.
- The quantum-channel description is useful for propagation, QFI analysis and testing alternative measurements. It is not evidence that every channel parameter was learned from this dataset.

The Kraus formalism and its non-uniqueness are available in Appendices E, K and L if the quantum-information examiner asks. They are not needed in the main spoken explanation.

Source: [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex), [ExoplanetExperimentAppendix.tex](../TeXtured/chapters/ExoplanetExperimentAppendix.tex).

Common survival is counted once. Conditional modal probabilities are multiplied by $T=N_{\mathrm{in}}\eta$. The example dephasing and mixing parameters are fixed sensitivity assumptions. They were not fitted from these counts. QFI comparisons use a common per-surviving-photon normalization and parameter-independent channels.

## Slide 18 — The model captures the mean count pattern

### Spoken script

[Compare the observed and modelled maps.]

The assumptions of the previous quantum-to-classical model were fitted to reproduce the ASI data. 

Here I show the comparison of the mean counts for different distances and intensity ratios.

This supports the model's practical use. The channel description also lets us study how optical imperfections affect sensitivity.

With this model we can also identify which extra measurements would help for a future experiment.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Predicting the average and explaining every fluctuation are different tasks. Two distributions can share a mean while having different spreads. Matching the mean is useful, but supports a narrower conclusion than identifying the full apparatus.

- The displayed panels are the **provisional workbench's observed and modelled setting means**, compared on the data used for fitting. Do not call this plot alone a held-out validation.
- The separate hierarchical calibration model was checked by holding out checkerboard cells, complete distance rows and complete source-ratio columns. Nominal 95% intervals covered 93.52%, 94.67% and 93.71% of the held-out setting means. These are the Appendix H results, not a validation statistic for the two provisional-workbench panels shown here.
- Reproducing means is not reproducing the distribution of individual counts. The thesis finds overdispersion and rejects the tested simple deterministic count models as complete descriptions of individual exposures.
- Avoid “the channels were fitted” and “I reconstructed the experimental QFI.” Instead: **“The optical channels were specified; the observable count response was calibrated.”** A model-based QFI remains conditional on the specified state and channels.
- More measurements help only if they resolve relevant ambiguities: separate ports address modal aggregation; known flux and loss outcomes address efficiency; phase-sensitive or rotated-basis measurements address coherence; controlled mode injection constrains transfer properties. Complete channel identification can require several calibrated inputs as well as outputs.

The prediction target is the mean of 100 repetitions, expressed as counts per 10 ms. The Gaussian-process correction is classical calibration variation. Mean prediction does not establish the distribution of every individual count or reconstruct experimental QFI.

## Slide 19 — Conclusions

### Spoken script

To conclude, I developed numerical and quantum-circuit methods for studying quantum sensor under noise.

For the magnetometer, the useful preparation depends on the field range where the sensor will operate.

For SPADE, we derived also a physical channel framework. 

VQ-SPADE is the proposed next step, using a trainable optical transformation to learn the state's eigenbasis. It requires additional data from ASI.

Across both applications, the central question is how preparation, access and measurement determine the information we can use.

Thank you.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** End by separating implemented methods, numerical findings, data interpretation and a future proposal. The common lesson is the chain from preparation to the recorded measurement.

- The numerical and circuit implementations were compared against exact references; finite numerical precision, Trotter error and variational convergence still matter.
- VQ-SPADE would learn an approximate eigenbasis, subject to optical control, calibration and optimization limits. The archived experiment did not implement it. Diagonalization alone is also insufficient for TQFI. Nearby states and additional overlap measurements are required.
- The main talk ends here. The following optional responses are outside the 15-minute budget.

## Backup Slide — Appendix N: Quantum Cramér–Rao bound

### Spoken script

For a fixed measurement, the classical Cramér–Rao bound says that the variance of a locally unbiased estimator is at least one over the number of independent repetitions times the classical Fisher information.

The QFI is the maximum classical Fisher information over all measurements. Replacing the measurement-dependent information by this maximum gives the quantum Cramér–Rao bound:

$$
\operatorname{Var}(\hat\theta)\geq\frac{1}{N\mathcal F_Q(\theta)},
\qquad
\Delta\theta\geq\frac{1}{\sqrt{N\mathcal F_Q(\theta)}}.
$$

It is therefore an ideal local precision benchmark. Reaching it still requires an appropriate measurement and an efficient estimator; the optimal measurement can itself depend on the unknown parameter.

### Details to keep in mind

- The bound assumes a differentiable one-parameter model, independent repetitions, regularity and local unbiasedness.
- Since $\mathcal F_C(M)\leq\mathcal F_Q$, a particular measurement obeys

  $$
  \operatorname{Var}(\hat\theta)
  \geq\frac{1}{N\mathcal F_C(M)}
  \geq\frac{1}{N\mathcal F_Q}.
  $$

- For a single parameter, measuring in an SLD eigenbasis can attain the QFI locally under the usual conditions. This does not imply one fixed, globally optimal measurement for every parameter value.
- The QCRB concerns estimator variance, not absolute error in a single experimental run.

## Backup Slide — Appendix C: Adaptive VQSE training

### Spoken script

This plot makes the adaptive training schedule explicit. In the upper panel, the white curve is the objective optimized at each outer iteration; the dashed curves evaluate the same variational state against the local and global Hamiltonians separately.

The lower panel shows why the optimized objective changes during the run. We start with the local objective, then quadratically transfer weight to the global objective. The white vertical lines mark refreshes of the global target basis states.

Therefore the white curve is useful for monitoring the scheduled optimization, but it is not by itself a fixed-loss convergence curve. To assess spectral accuracy, we compare the estimated eigenvalues with the exact numerical spectrum.

### Intuition

Think of the optimization as learning in two stages. The local Hamiltonian first gives the circuit an easier directional signal; the global Hamiltonian then evaluates whether the learned basis places the dominant spectral weight in the desired computational-basis states. The lower panel is the mixing dial between those two tasks.

- The state is a balanced, non-diagonal two-qubit mixed state with a rank-3 target. The result is a deterministic simulator demonstration, not a hardware benchmark.
- A global-target refresh does not necessarily create a visible jump: a jump occurs only if the selected target basis states actually change.
- The adaptive cost changes because the Hamiltonian changes. Use the leading-eigenvalue error on the next slide for a fixed accuracy metric.

## Backup Slide — Appendix C.1: BFGS, Adam and Bures natural gradient

### Spoken script

Here I compare three optimizers from the same initial circuit parameters on the same adaptive VQSE problem: BFGS, Adam, and a deterministic damped Bures natural gradient.

[Point to the upper-left panel.]

This is the fixed metric: the L2 error of the three leading estimated eigenvalues relative to the exact spectrum. BFGS and the Bures natural gradient both reduce it to the few-$10^{-3}$ range in this run, while Adam remains farther away.

[Point to the lower-left panel.]

The final-spectrum panel shows the same outcome directly: BFGS and Bures-NG closely reproduce the three exact leading eigenvalues.

[Point to the lower-right panel.]

The most visible difference is in parameter motion. BFGS has intermittent large and small Euclidean updates, whereas the Bures natural-gradient updates become smooth and steadily decrease after the initial adjustment.

The reason is geometric preconditioning. The update is

$$
\Delta\boldsymbol\theta=-\eta\,(G_{\mathrm{Bures}}+\lambda I)^{-1}\nabla C.
$$

The Bures metric is the mixed-state geometry associated with quantum Fisher information. It rescales directions by how much they move the physical density matrix, rather than treating every circuit parameter as having the same physical scale.

### Intuition

Two circuit knobs can be turned by the same angle while moving the quantum state by very different amounts. Ordinary parameter-space updates can therefore overstep in sensitive directions or make little progress in redundant ones. The Bures metric acts like a map of those unequal distances: damping prevents unstable inversion, and the inverse metric rescales the gradient before the update.

- The upper-right adaptive objective should not be read as a fixed-loss race, because the local-to-global Hamiltonian schedule changes it over time.
- BFGS is also curvature-aware; its jagged update norms here are not proof that BFGS is intrinsically unstable. In this benchmark it is restarted at each outer adaptive stage while the objective changes.
- The smoother Bures-NG trajectory is an observation for this state, ansatz and damping choice, not a general guarantee of faster convergence.
- This exact Bures-metric construction uses full density matrices and is appropriate for a small deterministic simulator. A hardware version would require a sampled metric estimator or another scalable approximation.

## Optional responses for questions

### “Is the quantum natural gradient just Newton's method?” — Appendix B

“They share the idea of transforming the gradient using a matrix. But Newton's method uses curvature of the objective, while the quantum natural gradient uses the geometry of the state family. It scales a parameter step by how much that step changes the quantum state.”

$$
\Delta\boldsymbol\alpha
=-\eta\,(F^{\mathrm{ans}}+\lambda I)^{-1}\nabla C.
$$

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

- First rehearse **only** the spoken sections, including the five overlay advances on slide 3. The technical notes and intuition boxes are not a second spoken paragraph.
- Clock checkpoints: start magnetometry near **5:05**, exoplanets near **7:55**, and conclusions near **14:10**.
- If running late, omit the modularity sentence on slide 6 and shorten the future-measurement examples on slide 18. Preserve the distinctions between populations/eigenvalues, assumptions/fits, and demonstrated/proposed work.
- On plots, name the axes or curves, point to the relevant feature, then state its implication. Give the audience a moment to look before continuing.
- Do not rush the final sentence. Finish with the conclusion slide visible.

## Further question preparation

See [defence_questions.md](defence_questions.md) for 60 questions with short oral answers, intuitive explanations and technical follow-ups. Especially useful follow-ups are questions 23–28: eigenbasis versus sensing basis, unknown parameters, thermal preparation, coherence, fidelity and photon-resource accounting.

For a slower introduction to thermal preparation, see questions 33–52 in [defence_questions.md](defence_questions.md), including a two-level example and a 30-second oral explanation. These are preparation notes, not additions to the timed talk.

Real-instrument examples and suggested slide wording are in questions 53–60 of [defence_questions.md](defence_questions.md). They distinguish MAGSCA and NMR probes from the periodic Ising model, and explain the preparation requirements for a possible temperature-controlled space sensor.

## Backup Slide — Appendix O: Modal populations and spectral information

### Spoken script

This slide explains the gap between the original idea and the available data.

[Move from the measured populations to the middle panel.]

TQFI needs dominant eigenvalues and eigenvectors. SPADE gives populations in a fixed mode basis.

These would coincide if that basis matched the state's eigenbasis. In general, we cannot assume that it does.

The dominant spectral subspace is therefore a different object from a fixed selection of low-order HG modes.

### Details to keep in mind

**Intuition — preparation only, not extra spoken text:** Looking at the diagonal of a matrix in one basis is not the same as diagonalizing the matrix. They agree only when that basis is an eigenbasis.

SPADE gives access to mode populations

$$
p_j=\langle HG_j|\rho|HG_j\rangle.
$$

If

$$
\rho=\sum_j\lambda_j|HG_j\rangle\langle HG_j|,
$$

then $p_j=\lambda_j$ and the retained approximation is

$$
\rho_r=\sum_{j=0}^{r-1}p_j|HG_j\rangle\langle HG_j|,
\qquad \operatorname{rank}(\rho_r)\leq r.
$$

- An HG cutoff is a basis truncation. To reproduce the dominant rank-$r$ spectral truncation used by TQFI, the chosen modes must be eigenvectors and must correspond to the $r$ largest eigenvalues. Diagonality alone does not establish this ordering.
- Aggregating $HG_{01}$ and $HG_{10}$ into one value $p_1$ gives their sum, not two separate eigenvalues.
- “Known total normalization” means that the full trial count is accounted for. It does not mean rescaling the retained probabilities to sum to one. The truncated operator may have trace below one. Keep the omitted weight when evaluating the fidelity bounds. A normalized postselected state would answer a different question.
- Observing selected modes is a projection or coarse-graining operation; it is not the partial trace used in the magnetometer.
- VQ-SPADE proposes a trainable unitary that maps the state's eigenvectors onto resolved HG outputs. This is an ideal target that requires a sufficiently expressive transformation and successful optimization. It is kept for the conclusion and Appendix I.

Sources: [ExoplanetExperiment.tex](../TeXtured/chapters/ExoplanetExperiment.tex), [Conclusions.tex](../TeXtured/chapters/Conclusions.tex).

## Backup Slide — Appendix P: Dephasing and readout

### Spoken script

This example shows why the order of the stages matters.

Dephasing reduces the off-diagonal coherence while keeping the immediate mode populations unchanged. A later mode rotation could turn that coherence into a measurable population difference.

Readout confusion acts after measurement and redistributes the reported outcomes.

The two maps describe different physical effects, even when the final recorded counts cannot tell them apart.

### Details to keep in mind

- The displayed map uses a real $0\leq v\leq1$ and is a valid two-mode dephasing channel.
- Its strength is not independently identified by the available data. A known mode rotation and suitable inputs could make it testable in a future experiment.
- The symmetric confusion model remains a classical post-measurement assumption.
- Appendix F distinguishes different quantum extensions of the same classical response. Appendices E and K discuss different Kraus representations of one fixed channel.

## Backup Slide — Appendix Q: Photon loss and measured counts

### Spoken script

Here is one concrete physical channel used in the receiver model: photon loss.

With probability $\eta$, the photon survives and reaches SPADE. With probability $1-\eta$, it is transferred to the vacuum outcome. Including that vacuum branch makes this a normalized quantum channel.

The experiment did not record the incident photon flux, so the loss probability $\eta$ cannot be fitted separately. The counts instead constrain the effective throughput $T=N_{\rm in}\eta$.

After SPADE, the predicted mean also contains a fitted background $B$. Dark counts can contribute to this background, but so can stray light and modal leakage. Therefore $B$ is an effective detector background, not a measurement of the dark-count rate alone.

This example shows why the stages are separated: photon loss acts on the quantum state, whereas background counts enter after the measurement.

### Details to keep in mind

- The loss map is an erasure channel because the missing probability is placed in an orthogonal vacuum outcome.
- On a finite one-photon mode space, one Kraus representation is $K_0=\sqrt{\eta}\,I$ for survival and $K_j=\sqrt{1-\eta}\,|\mathrm{vac}\rangle\langle HG_j|$ for loss from each mode. Their completeness relation makes the map trace preserving.
- For separation-independent $\eta$, the QFI per incident photon is $\eta\mathcal F_Q(\rho_S)$, while the conditional state of a surviving photon is still $\rho_S$.
- The fitted quantity is $T=N_{\rm in}\eta$, not $\eta$ itself. An independent incident-flux measurement would be needed to separate them.
- The fitted $B$ can combine detector dark counts, stray light, bright-mode leakage and other unresolved baseline contributions. Source-blocked measurements would be needed to identify the dark-count contribution.
- The mean model is $\mu=B+Tg(d,\epsilon)p^{\rm rep}_1$. The individual counts are overdispersed, so this equation describes their mean rather than asserting a simple Poisson distribution.

## Backup Slide — Appendix R: Complete receiver pipeline

### Spoken script

This diagram shows the complete direction of the model.

We begin with the assumed source state. Photon loss is a quantum channel acting on that state. SPADE then converts the optical state into measurement probabilities.

After measurement, cross-talk acts on the classical outcome probabilities. Background and calibration convert the reported first-order probability into a predicted mean count, which is finally compared with the recorded data.

The separation is useful because these stages do not describe the same object. Optical channels act on density matrices, SPADE produces probabilities, and the detector model produces count statistics. It also tells us which quantities can be calibrated or replaced independently.

### Details to keep in mind

- Photon loss and any other pre-measurement optical effects act on $\rho$.
- SPADE is represented by a POVM, with $p_1=\operatorname{Tr}(M_1\rho)$.
- The cross-talk matrix $R_\chi$ is a classical stochastic map acting after the POVM.
- The final mean is $\mu=B+Tg(d,\epsilon)p^{\rm rep}_1$, where $T=N_{\rm in}\eta$.
- The data constrain the final count response and some effective combinations of parameters; they do not reconstruct every preceding channel independently.
