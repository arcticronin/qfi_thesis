Beamer defence presentation

Open [main.pdf](main.pdf) for the finished presentation, or [main.tex](main.tex) to edit it. The deck has **11 main slides for 12 minutes**, plus **4 backup slides**. The language is English. The design uses a 16:9 canvas, navy background, warm white text, teal result highlights, and coral for experimental limitations.

Files:

- `main.tex`: slide content and embedded Beamer notes.
- `main.pdf`: compiled audience deck, with backup slides following the conclusion.
- `overview.png`: thumbnail overview of the 11 main slides.
- `build.sh`: two-pass build with intermediate files isolated in `build/`.
- `theme.tex`: fonts, colours, absolute-layout helpers, and footer.
- `speaker_notes.md`: a complete English script, timings, delivery guidance, and likely questions.
- `assets/thermal_advantage.pdf`: a vector scientific plot independently reproduced from the stated thesis Hamiltonian and checked against the headline values.
- `assets/tfim_curves.csv`: the values used for that plot.
- `assets/distinguishability.pdf`: a clearly identified conceptual illustration.
- `make_figures.py`: reproducible figure generation using NumPy, SciPy, and Matplotlib. It does not call TeX.

The source uses standard Beamer, TikZ, Latin Modern, graphicx, amsmath, amssymb and booktabs. It has no external theme, shell-escape requirement, bibliography build, or external institution-logo dependency; the ASI logo is bundled in `assets/asi.pdf`. Author and supervisor names and the formal thesis title were read from the thesis metadata. The short presentation title is intentionally easier to follow than the formal title, which remains on slide 1.

**Compiled and visually reviewed on 9 September 2026.** All 15 pages were rendered and inspected. Successive passes fixed line-break syntax, overflowing text, cramped statistics, diagram wrapping, and a backup-table overlap. The final build has no LaTeX errors, warnings, or overfull/underfull boxes. Rebuild after editing with:

```sh
sh presentation/build.sh
```

Run that command from the repository root, or run `sh build.sh` inside `presentation/`. Both passes are required for stable TikZ page coordinates. Beamer notes are hidden by default. The plain-text script is immediately usable. To create a separate notes version later, change `hide notes` in `theme.tex` to `show notes`; keep the audience version free of notes.

To regenerate figure assets in a Python environment with the dependencies installed:

```sh
python make_figures.py
```

Content choices and provenance:

| Main slide | Thesis source | Presentation choice |
|---|---|---|
| 1 | Intro; preamble/data | Formal title retained beneath a spoken-story title |
| 2 | MathBackground | Explain QFI through local distinguishability; omit derivation |
| 3 | Methods; VQSE | Show the learning loop; attribute the established algorithms |
| 4–5 | NoiseAnalysis, Project 9 | Use the consistent periodic N=6, n=4 comparison |
| 6 | Astrophysical | Explain spatial modes without creation operators |
| 7 | ExoplanetExperiment, dataset description | Distinguish sampling quantity from observable completeness |
| 8 | ExoplanetExperiment, sequential model | Group the detailed channel sequence into four stages |
| 9 | ExoplanetExperimentAppendix, hierarchical validation | Show rounded coverage and preserve the held-out mean target |
| 10 | ExoplanetExperimentAppendix, information comparison | Compare rows using the same nine-point grid; preserve normalization |
| 11 | Conclusions | Summarize implemented work, findings, and future acquisition |

Mathematical details, thermal data processing, complete validation metrics and the proposed VQ-SPADE requirements are in the backup slides. Leave the conclusion visible during questions and navigate to backups only when useful.

The optical information percentages on slide 10 are **conditional model values**, not measured experimental QFI, and their ranges run across settings rather than describing uncertainty intervals. The lower retained fraction includes both binary aggregation and the assumed readout confusion. The main deck does not quote the cross-fit envelope as a confidence interval. The periodic thermal comparison avoids the open-chain retained-subsystem inconsistency identified in the source review. The source-ratio convention still needs reconciliation in the thesis analysis; the slides do not invent a conversion or claim the archived data settle it.

Rehearse once with the script, then once from the slides alone. Aim to reach the thermal result by 4:05, the experimental record by 6:25, and the conclusion by 11:00. The timed script is a speaking aid, not text to place on screen.

Cover updated on 11 September 2026: the ASI emblem is the only logo, replacing the decorative orbit graphic. The slide content and timing are otherwise retained.
