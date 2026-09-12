# Presentation 4

[Presentation PDF](main.pdf) · [Main-slide overview](overview.png) · [Appendix overview](appendix_overview.png) · [Animation steps](animation_overview.png)

Dark Beamer presentation using `presentation_academic`'s navy background, teal/coral accents, Latin Modern fonts and canvas layout. Section names have moved from the heading to the footer. This version contains slides only: no speaking script or speaker notes.

There are **17 main slides and 10 appendix slides**. Slide 3 has seven successive measurement-basis overlays, so the PDF contains **33 pages**. Advance normally through angles 0°, 15°, 30°, 45°, 60°, 75° and 90°. Two mixed-state Bloch vectors remain fixed while the labelled measurement axis rotates and the CFI marker approaches the fixed QFI limit. All seven pages retain slide number 3 / 17; no animation-capable PDF viewer is required.

## Editable style controls

The top of [main.tex](main.tex) exposes:

```tex
\newcommand{\TitleRuleColor}{Teal}
\newcommand{\TitleRulePercent}{7}
\newcommand{\TitleRuleThickness}{2pt}
```

The percentage is relative to the 14.4 cm title/content width. The same controls apply to the cover. Colours, fonts, heading positions and footer formatting are in [theme.tex](theme.tex). The first argument of each `\heading` supplies its footer section name.

## Slide order

| Slide | Material | Origin |
|---|---|---|
| 1 | Thesis title; ASI collaboration | Academic 1 |
| 2 | Fisher information and distinguishability | Academic 2 |
| 3 | Measurement basis and CFI/QFI, seven overlays | Presentation 3, slide 3 |
| 4 | VQSE and PCA analogy | Academic 3 |
| 5 | Finite Ising magnetometer | Academic 4 |
| 6 | Parallel numerical and circuit workflows | New; formulas from presentation 3, slide 6 |
| 7 | Thermal preparation at βJ = 2 | Presentation 3, slide 7 |
| 8 | Temperature and peak sensitivity at βJ = 5 | Original presentation, slide 5 |
| 9 | Blank SPADE detector slide | Presentation 3, slide 8 |
| 10 | Direct imaging and spatial modes | Academic 6, with resolved/unresolved plots |
| 11 | Recorded counts and identifiability | Academic 7, with single/mean sample plots |
| 12 | Classical probabilities and quantum states | Academic 8 |
| 13–17 | Sequential channel model, Kraus freedom, loss proof, information retention, conclusions | Presentation 3, slides 10–14 |
| A–J | All ten existing appendices | Presentation 3 |

The closing variational-method statement now refers to the numerical benchmark developed in this sequence. QFI geometry for optimization remains available in Appendix B.

## Figures and scientific interpretation

- **Measurement overlays:** native TikZ in [assets/measurement_overlay.tex](assets/measurement_overlay.tex). Both vectors have Bloch radius 0.8 and lie inside the Bloch sphere, separated by 25° for visibility. The enlarged right-hand view labels them ρ and ρ(θ), and labels the rotating dashed axis “meas. basis”. The exact local CFI curve is evaluated at θ = 0 (radians): it rises from 0 to QFI = 0.64 as the basis rotates from 0° to 90°. Drawing two finite-separated states does not replace the local derivative with a finite difference. Appendix J gives the model and derivation.
- **Parallel workflow:** preparation/encoding → restricted access → spectral estimation → information. Exact partial trace and an unmeasured environment reproduce the same accessible-system statistics. Numerical eigendecomposition is the PCA-like counterpart of VQSE. Implementations can be exchanged at compatible interfaces; the stages do not generally commute. Ground-state, Gibbs and dynamical preparation are alternative branches. Unitary evolution alone does not generate a Gibbs state from a pure input; the gate thumbnails are illustrative, not an end-to-end thermal-preparation circuit.
- **Thermal plots:** both use the same axis limits. The second includes the βJ = 2 reference, making the higher, more localized βJ = 5 response directly comparable. Only temperature changes between these thermal families. Curves are rebuilt from the existing exact-model CSV samples in [assets/thermal_plots.tex](assets/thermal_plots.tex). The view ends at hₓ/J = 2; the 40/60 statistic refers to the original full grid [0.1, 2.5], as stated on the slide. An uncertain-field choice still depends on the plausible range or prior; these curves establish no universal optimum.
- **Thesis images:** the supplied direct-imaging, count, circuit and output plots are included without modifying the original assets. Circuit/output thumbnails illustrate workflow stages; their fine print is not intended for presentation reading.

## Remaining visual

**TODO — slide 9:** add the detector photograph or schematic in the `spade-detector` frame. An `includegraphics` example is commented in [main.tex](main.tex). The projected slide is intentionally blank apart from its title, accent and footer.

**Optional refinement — slide 6:** replace the supplied gate thumbnails with a matched end-to-end circuit export if desired. No additional plot is required to use the current slide.

## Build

From the thesis workspace:

```sh
sh presentation_4/build.sh
```

The build compiles the two-page thermal figure and runs Beamer twice. All required assets are copied into this folder; previous presentations and thesis sources are unchanged. Intermediate LaTeX files are stored in `build/`.

Validation: clean LaTeX logs, embedded fonts, all text within page bounds, verified slide numbering and numerical annotations. All pages rendered and reviewed, including the complete overlay sequence. See [validation report](build/validation_report.txt).
