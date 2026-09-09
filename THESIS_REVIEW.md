Master's thesis source review — 9 September 2026

Reviewed all nine requested chapters and appendices. Also read `Methods.tex` and its included `VQSE.tex` to check definitions and cross-chapter consistency, and inspected the main document's final-version settings. No LaTeX compilation was performed. No thesis source files were changed. Comments and instructions inside the thesis were treated as document content, not as requests to execute them.

The central conclusions are carefully qualified: Gibbs preparation is distinguished from a fixed noise channel, and conditional optical-model information is distinguished from information reconstructed experimentally. The main remaining concerns are a subsystem-geometry mismatch, statistical reproducibility and uncertainty wording, and several mathematical qualifications.

Items below distinguish confirmed inconsistencies from points needing clarification. The numerical experiments and statistical fits were not comprehensively rerun. One small independent TFIM calculation was performed to investigate the inconsistent tables.

1. **High priority — different retained subsystems are presented as the same open-chain comparison.**

   Locations: [NoiseAnalysis.tex:286](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:286), [NoiseAnalysis.tex:376](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:376), [Methods.tex:44](/home/ronin/Dev/thesis/TeXtured/chapters/Methods.tex:44).

   The first table gives a refined ground-state local peak of 5.935 at field 0.646 for open N=6, n=4. The thermal-study baseline gives 6.014 for the same stated sizes and boundary conditions. A grid change cannot explain a grid maximum exceeding the refined maximum in the same peak region.

   I independently constructed the stated J=1 Hamiltonian, differentiated the ground state analytically, traced out the complement, and evaluated spectral SLD QFI. Retaining sites {0,1,2,3} gives a peak of **6.0140947 at 0.6309911**. Retaining sites {1,2,3,4} gives **5.9353062 at 0.6460600**. The full-system peak is 6.7878718 at 0.6197855.

   These results reproduce both reported local peaks through different subsystem positions. This strongly indicates that Project 1 uses a central block while Project 7 uses an end block. Methods currently specifies the end block. Explicitly list the retained site set for every study, qualify the shared-subsystem language, and check the associated figure captions. Do not simply replace one number with the other: each can be correct for its own geometry.

2. **High priority — the contrast parameter has two incompatible definitions.**

   Locations: [Astrophysical.tex:13](/home/ronin/Dev/thesis/TeXtured/chapters/Astrophysical.tex:13), [Astrophysical.tex:21](/home/ronin/Dev/thesis/TeXtured/chapters/Astrophysical.tex:21), [ExoplanetExperiment.tex:80](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:80).

   The theoretical definition is epsilon = I_B/(I_A+I_B), but the text says the approximation I_B/I_A is used throughout. The dataset description calls epsilon the faint intensity divided by the bright intensity while citing the exact fraction definition. The density operators subsequently use epsilon as an exact mixture weight.

   Introduce r=I_B/I_A and retain epsilon=r/(1+r) as the mixture fraction. State which quantity the dataset axis actually contains and where conversion occurs. If 0.09593 is a ratio r, the corresponding fraction is about 0.08753; substituting r as the fraction overstates the faint component by about 9.6%. This is material alongside sub-percent information-retention claims. The text alone does not establish whether the numerical implementation also contains this error.

3. **High priority — the cross-fit envelope is incorrectly described as a rigorous uncertainty interval.**

   Location: [ExoplanetExperiment.tex:413](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:413).

   The footnote calls the envelope a “robust, statistically rigorous uncertainty interval.” A spread of fitted values across grouped folds does not automatically have a confidence level or calibrated coverage for T. The appendix more appropriately describes it as sensitivity to calibration and held-out prediction.

   Replace the footnote with: “Nuisance parameters describe features needed by the model other than the target quantity. The grouped cross-fit envelope summarizes variation in the throughput estimate across the specified fits; it is a sensitivity summary, not a confidence interval.” Define exactly how the endpoints were constructed. Keep the separate conditional bootstrap interval explicitly conditional.

4. **High priority — the main predictive and throughput fits are not yet reproducible from the written method.**

   Locations: [ExoplanetExperiment.tex:380](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:380), [ExoplanetExperiment.tex:411](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:411), [ExoplanetExperimentAppendix.tex:189](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperimentAppendix.tex:189).

   The GP prior and latent mean are supplied, but the observation likelihood for the 100-repeat means, the fitted variance law mentioned in the validation caption, and the fitting objective are not written down. It is unclear whether the fit is to means or log-means and how repeat-level sampling uncertainty enters prediction intervals.

   There are also two different mean constructions: (B+A p1) exp(f+xi) and B+T g p_reported,1. The first multiplies the baseline by the calibration field; the second leaves B additive. Explain that these are separate fitted models and how the second is fitted, rather than implying a direct algebraic reparameterization.

   Specify the kernel including coordinate scaling; observation likelihood/variance; estimation procedure; parameter constraints; train/test fold rule; prediction-interval construction; and transformation from the raw T=1234.43 to calibrated T=1304.25. State whether “zero weighted mean” applies to log(g), with the weights defined. A positive multiplicative g cannot itself have zero weighted mean. A zero-mean log field fixes a geometric normalization, not an arithmetic mean of g equal to one. These conventions are necessary to interpret the reported throughput.

5. **Mathematical correction — restrict the QFI/Bures identity to regular points.**

   Locations: [MathBackground.tex:253](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:253), [MathematicalAppendix.tex:98](/home/ronin/Dev/thesis/TeXtured/chapters/MathematicalAppendix.tex:98).

   H=4g_B is stated without qualification. At rank-changing points, the SLD QFI at the point can differ from the Bures/fidelity limit. Omitting zero-denominator terms defines the spectral SLD value but does not remove this distinction. The optical chapter correctly excludes d_a=0, yet the appendix it cites does not explain why the limiting quantity differs.

   Add the constant-rank/regularity qualification and explain that the point value and the neighboring limit must be distinguished. A simple example is rho(theta)=diag(1-theta^2,theta^2): at theta=0 the first derivative vanishes and spectral SLD QFI is zero, while the fidelity difference quotient tends to 4. This issue is established in [Šafránek, Discontinuities of the quantum Fisher information and the Bures metric](https://arxiv.org/abs/1612.04581).

   The same qualification belongs wherever the fidelity limit is identified with local SLD QFI, including Methods. The background's final sentence about finite-difference bounds should also agree with NoiseAnalysis's careful distinction between bounds on the finite-displacement functional and bounds on exact SLD QFI.

6. **Mathematical correction — the QCRB explanation reverses the direction of the precision bound.**

   Location: [MathBackground.tex:129](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:129).

   “Practical receivers and variational bounds need to stay below this limit” follows a lower bound on variance. Estimator variance must be at or above the QCRB under its assumptions; measurement CFI is at or below QFI. Fidelity upper bounds can also lie above QFI in the appropriate limiting comparison.

   Suggested replacement: “Under the stated assumptions, estimator variance cannot fall below the QCRB, while the CFI of any fixed measurement cannot exceed the QFI.”

7. **Mathematical clarification — SLD support language excludes necessary matrix elements if read literally.**

   Location: [MathBackground.tex:139](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:139).

   Saying the SLD is “defined on the support” is incomplete for a state whose support rotates. Matrix elements connecting the support to the kernel contribute whenever lambda_k+lambda_l>0. Only the kernel-to-kernel block is arbitrary. The later spectral formula is correct; align the prose with it. Otherwise a reader could wrongly drop the terms carrying pure-state QFI.

8. **Conceptual correction — mixedness is not always ignorance about an underlying local pure state.**

   Location: [MathBackground.tex:35](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:35).

   The ontic/epistemic paragraph says a mixed state means the exact state is unknown, including when the system is entangled with an environment. A reduced density operator can be completely known even though the subsystem is mixed. For an entangled global state, interpreting the local mixture as mere ignorance of a pre-existing local pure state is not generally justified.

   Distinguish a statistical preparation mixture from a reduced state of an entangled system, while retaining the useful point that observable predictions depend on the parameterized density operator, not on a chosen ensemble decomposition. Present the philosophical terminology as interpretation-dependent or omit it.

9. **Mathematical correction — the Berry-curvature statement misses a factor and convention.**

   Location: [MathematicalAppendix.tex:79](/home/ronin/Dev/thesis/TeXtured/chapters/MathematicalAppendix.tex:79).

   The imaginary part of Q is proportional to Berry curvature, rather than simply equal to it. With A_mu=i<psi|partial_mu psi> and Omega_mu,nu=partial_mu A_nu-partial_nu A_mu, Omega_mu,nu=-2 Im Q_mu,nu. Define the convention or say that the imaginary part “encodes the Berry curvature.” See the explicit convention in [Experimental measurement of the quantum geometric tensor using coupled qubits in diamond](https://academic.oup.com/nsr/article/7/2/254/5644057).

10. **Mathematical clarification — statistical coupling and measurement incompatibility are different.**

    Locations: [MathBackground.tex:189](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:189), [MathematicalAppendix.tex:87](/home/ronin/Dev/thesis/TeXtured/chapters/MathematicalAppendix.tex:87).

    Off-diagonal QFIM entries describe cross-sensitivity and affect inversion when several parameters are unknown. They do not by themselves establish incompatible optimal measurements. The latter involves the SLDs and the allowed measurement setting. In the appendix, specify the regular asymptotic collective-measurement setting when using weak commutativity as a compatibility condition; it is not a general promise of a common optimal single-copy POVM.

11. **Sampling statement — a sufficient Hoeffding bound is presented as necessary scaling.**

    Location: [NoiseAnalysisAppendix.tex:49](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysisAppendix.tex:49).

    The preceding theorem correctly gives a sufficient sample count proportional to 1/lambda_m^2. The prose then calls this the “required sample size.” This is stronger than what was proved. Multiplicative concentration bounds can yield sufficient relative-error scaling proportional to 1/lambda_m for positive probabilities. Say “this sufficient Hoeffding bound grows as...” and require lambda_m>0. Also distinguish sampling error around the measured diagonal probabilities from variational bias relative to true eigenvalues.

12. **Verification theorem — state its domain and what the error measures.**

    Location: [NoiseAnalysisAppendix.tex:52](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysisAppendix.tex:52).

    The cost bound contains E_(m+1), so it needs m<2^n and a nonzero energy-gap denominator. For the general ordered auxiliary Hamiltonian introduced in VQSE, also require C<=E_(m+1) before squaring the positive lower bound in the derivation, or use max(E_(m+1)-C,0)^2. For the final global cost with a flat upper spectrum this condition is automatic, but the appendix does not restrict the theorem to that case. This qualification follows directly from the inequality before squaring in the [VQSE paper's derivation](https://www.nature.com/articles/s41534-022-00611-6).

    Finally, epsilon_v is an eigenvector residual norm, not a direct angle or infidelity. Calling it “alignment error” can mislead near degenerate eigenvalues. It vanishes for any exact eigenvector and needs spectral-gap assumptions to certify closeness to a particular vector.

13. **Numerical evidence — comparing maxima does not establish pointwise data processing.**

    Location: [NoiseAnalysis.tex:580](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:580).

    The inequality 4.847<8.456 compares two maxima, potentially at different fields. It is consistent with data processing but does not demonstrate F_local(h)<=F_full(h) at every sampled field. The chapter says that the pointwise check was performed; report its maximum violation and numerical tolerance, or explicitly call the displayed equation a peak comparison. This would substantiate the claimed validation without requiring more figures.

14. **Reproducibility — fully specify the optical information test grids and derivative tolerances.**

    Location: [ExoplanetExperimentAppendix.tex:285](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperimentAppendix.tex:285).

    The nine-point ladder is specified, but the twelve-point set is only described as three signed distances and four source fractions. List those values. Report the fidelity displacement, SLD/pseudoinverse tolerance, numerical tail treatment, and the settings producing the largest 0.322% disagreement. Cutoff convergence alone does not establish derivative convergence. This matters because the full-SPADE departure from optimality is itself only about 0.1% at the stated worst point; the two error measures should not be conflated.

15. **Final-document setting — work-in-progress mode is still enabled.**

    Location: [thesis.tex:23](/home/ronin/Dev/thesis/TeXtured/thesis.tex:23).

    `\WIPtrue` is active. The template uses this flag for draft information on the title page and in page footers. Disable WIP for the submitted version. `\CENSORtrue` is also active; check whether censoring is intended. The declaration is listed in `includeonlysmart` but its actual `\include` is commented out; include it if required by the university. These are observations about the current configuration, not changes made during this review.

Additional findings in the included Methods/VQSE material:

- [Methods.tex:29](/home/ronin/Dev/thesis/TeXtured/chapters/Methods.tex:29): all-up/all-down and all-plus product states are limiting descriptions, not exact finite-field ground states throughout the ferromagnetic and paramagnetic regimes. State the thermodynamic symmetry-breaking qualification and the h/J->0 or infinity limits. The finite-chain ground-state treatment elsewhere is more careful.
- [Methods.tex:166](/home/ronin/Dev/thesis/TeXtured/chapters/Methods.tex:166): SLD QFI also needs only rho and its derivative; it does not inherently require a known encoding generator. Describe fidelity methods as avoiding explicit derivative/SLD evaluation, rather than contrasting them with an alleged generator requirement.
- [VQSE.tex:121](/home/ronin/Dev/thesis/TeXtured/chapters/VQSE.tex:121): define the plotted “infidelity,” input-state family, n, m, optimization budget, and whether points summarize repeated seeds. These details are needed to support the implementation/benchmark claims.
- [VQSE.tex:260](/home/ronin/Dev/thesis/TeXtured/chapters/VQSE.tex:260): the caption first uses L=8 for a TFIM and then defines L as the RBM hidden/visible ratio, referencing circuit-layer notation. Use separate symbols for chain length, circuit depth, and RBM hidden-unit ratio and give each actual value.

Language and presentation corrections:

| Location | Current wording or issue | Suggested change |
|---|---|---|
| [Intro.tex:22](/home/ronin/Dev/thesis/TeXtured/chapters/Intro.tex:22) | “In colder finite-system regime” | “In colder finite-system regimes” |
| [Intro.tex:24](/home/ronin/Dev/thesis/TeXtured/chapters/Intro.tex:24) | “poor conditioned” | “poorly conditioned” |
| [Intro.tex:26](/home/ronin/Dev/thesis/TeXtured/chapters/Intro.tex:26) | “question was if” | “question was whether”; likewise in Conclusions:14 |
| [MathBackground.tex:122](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:122) | “Def.” refers to an equation label | Use “Eq.”; likewise the “Definition” reference at line 136 |
| [MathBackground.tex:162](/home/ronin/Dev/thesis/TeXtured/chapters/MathBackground.tex:162) | `$H_{ij}$is` | Add a space before “is” |
| [ExoplanetExperiment.tex:139](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:139) | Run-on sentence followed by “That is how...” | “In a chosen basis, a classical probability vector can be embedded as a diagonal density matrix. A general density matrix may additionally contain off-diagonal coherences.” |
| [ExoplanetExperiment.tex:243](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:243) | “distintion” | “distinction” |
| [ExoplanetExperiment.tex:351](/home/ronin/Dev/thesis/TeXtured/chapters/ExoplanetExperiment.tex:351) | “The median value Fano factor” | “The median Fano factor” |
| [NoiseAnalysis.tex:199](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:199) | “In this case d is...” | Put d in math mode; preferably use 2^n directly to avoid the optical-distance notation |
| [NoiseAnalysis.tex:267](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:267) | “Values and locations are using refined maximum” | “Peak values and locations were obtained by local continuous refinement.” |
| [NoiseAnalysis.tex:324](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:324) | “approximated local peaks positions” | “estimated local peak positions” |
| [NoiseAnalysis.tex:484](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysis.tex:484) | “informativity changes” | “changes in QFI” |
| [NoiseAnalysisAppendix.tex:4](/home/ronin/Dev/thesis/TeXtured/chapters/NoiseAnalysisAppendix.tex:4) | Announces three supporting details | There are four sections; include the graphical-calculus material |

Use consistent British or American spelling, consistent “Hermite–Gaussian,” and one form of “cross-talk.” The repeated explanations that the SPADE data do not reconstruct a channel are scientifically useful, but can be shortened where the same qualification appears several times within a few paragraphs. Preserve them in the summary, parameter-provenance discussion, and conclusions.

Static verification completed:

- Checked all 11 chapter source files, including Methods and VQSE.
- Found no duplicate labels or unresolved literal chapter references in the scan (including optional infobox labels).
- All 64 scanned citation occurrences resolve to keys in the bibliography.
- All 38 scanned graphics references resolve to existing files under the document root or figures directory.
- No LaTeX compiler, bibliography processor, or document build was run. These source checks do not verify rendered layout, page breaks, equation overflow, or image readability.
