Presentation 3 — academic defence

[Open the presentation](main.pdf) · [Main-slide overview](overview.png) · [Appendix overview](appendix_overview.png)

This version uses a light background, Palatino headings and mathematical type, Source Sans Pro body text, and the thesis's Seaborn Set2 accents. There are **14 main slides and 10 appendix slides**. The complete English speaking script is in [speaker_notes.md](speaker_notes.md). All three presentation covers now display ASI alone; the other decks retain their existing slide content.

The narrative follows a physical question: how does information in a quantum state become information accessible in an experiment?

1. Define QFI as a local distinguishability limit and visualize its relation to measurement-dependent CFI with an exact mixed-qubit example.
2. Introduce VQSE through spectral extraction and the PCA analogy.
3. Connect the same geometry to quantum natural-gradient optimization.
4. Compare ground-state and thermal preparation in the same accessible spin subsystem.
5. Move to SPADE and distinguish the available counts from the unobserved optical state.
6. Construct the channel model, explain Kraus non-uniqueness, and prove a physical loss model valid.
7. Compare information retained at the receiver and conclude with acquisition requirements.

The main deck prioritizes the channel framework over the detailed calibration fit. Grouped predictive validation is retained in Appendix H, where it can be discussed with the AI faculty without interrupting the physical argument. Longer geometric and channel proofs also remain available for questions.

The 12-minute allocation includes pauses and pointing to figures. Rehearse using [the speaking script](speaker_notes.md); appendix slides are for questions.

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

Slide 8, the detector slide, is intentionally blank apart from its title and footer. Add the chosen image under `assets/` and use the commented `includegraphics` line in the frame labelled `spade-detector` in [main.tex](main.tex). The remaining slides are complete; this is the only reserved visual.

Scientific distinctions retained:

- **QNG versus Newton:** the ansatz QFIM measures distinguishability of states, whereas the Hessian measures objective curvature. Their update structures are analogous, but the matrices are not generally equal. The main slide does not claim a demonstrated QNG speedup in mixed-state VQSE. Appendix C shows the thesis's separate pure-state RBM/SR example, with its limited scope stated.
- **Kraus freedom versus model ambiguity:** the projector and random-phase-flip sets in slide 11 implement the same dephasing map on every input. This is representation freedom. Different quantum maps agreeing on measured populations are a separate identifiability issue, explained in Appendix F.
- **Physical justification versus mathematical validity:** slide 12 supplies Kraus operators for mode-dependent transmission and explicit failure events. Their completeness proves trace preservation; Kraus form ensures complete positivity. Mode-injection calibration is still required to establish the transmissions of the real apparatus. Algebra alone does not prove an experimental mechanism.
- **Thermal preparation:** beta J = 2 gives a lower sampled maximum (2.606593 versus 3.925954) but higher off-peak QFI over part of the field range. The plotted view ends at h_x/J = 2. Choice under an unknown field depends on its plausible range or prior; no universal average-performance optimum is claimed.
- **Information accounting:** channel data processing assumes parameter-independent downstream maps. The optical percentages use the same nine settings, per photon surviving common loss. They are conditional calculations, not experimental QFI estimates; the low range includes both aggregation and assumed confusion.
- **VQSE:** dominant state weights are analogous to PCA eigenvalues but are not variances. Spectral truncation supplies fidelity-based bounds; it does not guarantee that all parameter sensitivity lies in the dominant components.

Appendix:

| Label | Material |
|---|---|
| A | Fidelity bounds and the local-QFI limit |
| B | Ansatz metric, natural-gradient derivation and mixed-state scope |
| C | Thesis RBM stochastic-reconfiguration example |
| D | Thermal preparation and data processing |
| E | Kraus-isometry proof and the dephasing example |
| F | Classical-to-quantum channel embedding and non-identifiability |
| G | Complete positivity, failure outcomes and loss calibration |
| H | Grouped predictive calibration metrics |
| I | Proposed VQ-SPADE acquisition |
| J | Exact CFI/QFI calculation for the Bloch-plane example |

Build from the thesis root:

```sh
sh presentation_3/build.sh
```

The build creates both the thermal and measurement-sensitivity plots with PGFPlots, then compiles Beamer twice to resolve TikZ's remembered coordinates. Intermediate files are kept in `build/`. No external theme, Python plotting package or shell escape is needed.

Editable assets:

- [main.tex](main.tex): main deck and appendices.
- [theme.tex](theme.tex): colour palette, typography and page layout.
- [speaker_notes.md](speaker_notes.md): English script, 14-slide timing plan and likely questions.
- [assets/measurement_sensitivity.tex](assets/measurement_sensitivity.tex): exact Bloch-plane/CFI illustration.
- [assets/thermal_plot.tex](assets/thermal_plot.tex): vector plot specification with exact Set2 green and blue.
- [assets/tfim_curves.csv](assets/tfim_curves.csv): exact SLD data from the periodic six-spin model. The CSV retains all 60 original field samples; the displayed plot is cropped.
- [assets/sr_comparison.png](assets/sr_comparison.png): existing thesis figure, copied without alteration.
- The ASI logo is copied from the thesis assets through the previous deck. AI4ST is no longer displayed on any cover.

The primary content sources are the supplied thesis chapters, especially Mathematical Background, VQSE, Noise Analysis, Quantum Channel Model for SPADE, the Exoplanet Experiment Appendix and Conclusions. The dephasing equivalence and explicit loss Kraus operators are short derivations of the stated thesis maps, rather than new experimental results.

The new figure uses a full-rank qubit with Bloch radius 0.8, estimates its rotation angle theta locally at zero, and varies the measurement angle phi. The QFI is 0.64; the CFI at 45 degrees is 8/17 (approximately 0.47), and a 90-degree measurement attains QFI. This distinguishes measurement choices from directions in a multiparameter information ellipse. Appendix J derives the curve.
