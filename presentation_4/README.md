# Presentation 4

[Presentation PDF](main.pdf) · [Main-slide overview](overview.png) · [Appendix overview](appendix_overview.png) · [Animation steps](animation_overview.png)

Dark Beamer presentation using `presentation_academic`'s navy background, teal/coral accents, Latin Modern fonts and canvas layout. Section names have moved from the heading to the footer. There is no speaking script. Slide 6 has a compact Beamer note containing reference formulas; it is hidden in the projected PDF.

There are **18 main slides and 13 appendix slides**. Slide 3 has six successive measurement-basis overlays, so the PDF contains **36 pages**. Advance normally through angles 0°, 30°, 45°, 60°, 75° and 90°. Two mixed-state Bloch vectors remain fixed while the labelled measurement axis rotates and the CFI marker approaches the fixed QFI limit. All six pages retain slide number 3 / 18; no animation-capable PDF viewer is required.

## Editable style controls

The top of [main.tex](main.tex) exposes:

```tex
\newcommand{\TitleRuleColor}{Teal}
\newcommand{\TitleRulePercent}{100}
\newcommand{\TitleRuleThickness}{2pt}
```

The percentage is relative to the 14.4 cm title/content width. The same controls apply to the cover. Colours, fonts, heading positions and footer formatting are in [theme.tex](theme.tex). The first argument of each `\heading` supplies its footer section name.

## Slide order

| Slide | Material | Origin |
|---|---|---|
| 1 | Thesis title; ASI collaboration | Academic 1 |
| 2 | Fisher information and distinguishability | Academic 2 |
| 3 | Measurement basis and CFI/QFI, six overlays | Presentation 3, slide 3 |
| 4 | Mixed states, spectral truncation, VQSE and TQFI | One 17 pt truncation formula; VQSE, PCA and TQFI expanded |
| 5 | Aims: QFI/TQFI methods and two applications | New |
| 6 | Numerical simulation and quantum-circuit workflow | Enlarged figures; formulas in reference notes |
| 7 | Quantum Magnetometry | Application title |
| 8 | Finite Ising magnetometer | Former slide 5 |
| 9 | Thermal preparation at βJ = 2 | Former slide 7 |
| 10 | Temperature and peak sensitivity at βJ = 5 | Former slide 8 |
| 11 | Exoplanet Detection | Application title |
| 12 | Direct imaging and spatial modes | Former slide 10 |
| 13 | Blank SPADE detector slide | Former slide 9 |
| 14 | Recorded counts and identifiability | Former slide 11 |
| 15 | Why quantum channels: populations and coherence | Simplified optical introduction |
| 16 | Physical channel choices and fitted classical calibration | Simplified forward model |
| 17 | Observed and modelled setting means | Top panels of the requested channel-workbench figure |
| 18 | Four contributions: sensing pipeline, preparation/noise study, SPADE channel analysis, proposed VQ-SPADE | Revised contribution summary |
| A–J | Existing ten appendices | Preserved |
| K | Kraus representation freedom | Former main slide 15 |
| L | Mode-dependent loss and completeness proof | Former main slide 16 |
| M | Information-retention table | Former main slide 17 |

The closing variational-method statement now refers to the numerical benchmark developed in this sequence. QFI geometry for optimization remains available in Appendix B.

## Figures and scientific interpretation

- **Measurement overlays:** native TikZ in [assets/measurement_overlay.tex](assets/measurement_overlay.tex). Both vectors have Bloch radius 0.8 and lie inside the Bloch sphere, separated by 25° for visibility. The enlarged right-hand view labels them ρ and ρ(θ), and labels the rotating dashed axis “meas. basis”. The exact local CFI curve is evaluated at θ = 0 (radians): it rises from 0 to QFI = 0.64 as the basis rotates from 0° to 90°. Drawing two finite-separated states does not replace the local derivative with a finite difference. Appendix J gives the model and derivation.
- **Parallel workflow:** preparation → restricted access → spectral estimation → information. Exact partial trace and an unmeasured environment reproduce the same accessible-system statistics. Numerical eigendecomposition is the PCA-like counterpart of VQSE. Implementations can be exchanged at compatible interfaces; the stages do not generally commute. Ground-state, Gibbs and dynamical preparation are alternative branches. Unitary evolution alone does not generate a Gibbs state from a pure input; the gate thumbnails are illustrative, not an end-to-end thermal-preparation circuit.
- **Thermal plots:** compare each Gibbs state directly with the ground state on the same axes. Teal shading marks higher Gibbs QFI on the right of the crossings (βJ = 2: hₓ/J ≈ 1.111; βJ = 5: hₓ/J ≈ 0.880), obtained by linear interpolation of the plotted CSV samples. Slide 9 emphasizes a wider off-peak operating range; slide 10 emphasizes stronger local sensitivity near the thermal peak. The βJ = 2 overlay and large numerical callouts have been removed from slide 10. Temperature is the changing preparation control; usefulness depends on the expected field range, not a universal thermal advantage. Curves are rebuilt from [assets/thermal_plots.tex](assets/thermal_plots.tex).
- **Thesis images:** the supplied direct-imaging, count, circuit and output plots are included without modifying the original assets. Circuit/output thumbnails illustrate workflow stages; their fine print is not intended for presentation reading.

## Simplified optical story

Slides 15–17 now follow a short sequence: describe populations and coherences → choose physically motivated channels and calibrate the count response → compare modelled and observed setting means. Kraus operators are named as the representation of the optical stages without introducing their algebra in the main talk. The three former technical slides are preserved at the very end as Appendices K–M.

The result slide uses only the top two panels of `spade_plausible_channel_workbench.png`. LaTeX clips the copied original image; no heatmap values, axes or colour bars are changed. The observed and modelled panels use matching count scales. The common pattern is a central minimum and a rising response with separation and source ratio.

The claim is an **in-sample comparison of setting means**. The thesis appendix’s Provisional Channel Workbench section fixes example optical values and fits throughput, background, displacement offset and coupling. Agreement of the mean response does not identify those optical mechanisms, establish an experimental QFI, or validate the full single-count distribution. The calibration-validation appendix remains available for questions.

## Formula reference notes

The `pipeline` frame (slide 6) contains a `\note{\scriptsize ...}` block with the Hamiltonian, evolution, preparation, partial trace and spectral formulas. These are source-level Beamer notes, not a speaking script. The theme uses `\setbeameroption{hide notes}`; they do not appear in the projected PDF.

## Remaining visual

**TODO — slide 10:** add the detector photograph or schematic in the `spade-detector` frame. An `includegraphics` example is commented in [main.tex](main.tex). The projected slide is intentionally blank apart from its title, accent and footer.

**Optional refinement — slide 6:** replace the supplied gate thumbnails with a matched end-to-end circuit export if desired. No additional plot is required to use the current slide.

## Build

From the thesis workspace:

```sh
sh presentation_4/build.sh
```

The build compiles the two-page thermal figure and runs Beamer twice. All required assets are copied into this folder; previous presentations and thesis sources are unchanged. Intermediate LaTeX files are stored in `build/`.

Validation: clean LaTeX logs, embedded fonts, all text within page bounds, verified slide numbering and numerical annotations. All pages rendered and reviewed, including the complete overlay sequence. See [validation report](build/validation_report.txt).
