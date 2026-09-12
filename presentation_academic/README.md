Academic Beamer defence — alternative version

Open [main.pdf](main.pdf). This independently editable copy preserves the navy, teal and coral design of `../presentation/`, with **12 main slides for a 12-minute English defence**, followed by **4 backup slides**. The original deck retains its content; all versions now use ASI alone on the cover.

Differences from the original:

- Full official thesis title on the cover and in PDF metadata.
- ASI collaboration and *Quantum Computers for Space Exploration* credit. The ASI emblem comes from the thesis `asi.svg`; the requested `logo-ai4st.png` is the separate AI4ST programme logo. Only the ASI emblem is displayed on the cover.
- Academic titles and prose throughout.
- VQSE explained through its analogy with PCA, spectral decompositions and a trained basis rotation, without loss functions.
- Thermal comparison at **beta J = 2**, displayed through **h_x/J = 2**. The thermal peak is lower (2.607 versus 3.926); the shaded region shows higher off-peak QFI. Usefulness under field uncertainty depends on the expected operating range.
- A new slide distinguishes probability vectors, diagonal density matrices, coherences and channels. The following slide explains the model's value for coherent optics, modular calibration and information accounting.

Files:

- [main.tex](main.tex): slide content and short embedded presenter notes.
- [theme.tex](theme.tex): visual design and layout helpers.
- [speaker_notes.md](speaker_notes.md): revised English script, timings and likely questions.
- [overview.png](overview.png): contact sheet of all 12 main slides.
- [build.sh](build.sh): two-pass PDF build, with intermediate files in `build/`.
- [make_figures.py](make_figures.py): NumPy/SciPy/Matplotlib reproduction of the TFIM curves and conceptual distinguishability figure.
- [assets/tfim_curves.csv](assets/tfim_curves.csv): exact sampled QFI data, with the thermal column labelled beta2. The CSV retains the original 60-point sampling interval [0.1, 2.5]; the plotted view is cropped at 2.

Build from the thesis root:

```sh
sh presentation_academic/build.sh
```

Or run `sh build.sh` inside this folder. Both LaTeX passes are needed for TikZ's remembered page coordinates. Beamer notes are hidden in the audience PDF. Figure regeneration is separate: run `python make_figures.py` in an environment containing NumPy, SciPy and Matplotlib.

Source correspondence:

| Slides | Thesis source |
|---|---|
| 1 | Intro; preamble/data; thesis logo assets |
| 2–3 | MathBackground; Methods; VQSE |
| 4–5 | NoiseAnalysis, periodic six-spin / four-accessible-spin comparison |
| 6 | Astrophysical |
| 7–9 | ExoplanetExperiment, dataset limitations and sequential channel framework |
| 10–11 | ExoplanetExperimentAppendix, grouped validation and conditional information comparison |
| 12 | Conclusions |

The PCA comparison is an analogy between spectral decompositions: probability weights are not variances. VQSE supplies retained components for fidelity-based bounds; the finite-step quantity and exact SLD QFI remain distinct. The new channel slide is a two-outcome illustration, not a reconstruction from archived counts. A probability vector does not determine coherence or a unique quantum channel.

The optical retention values remain conditional model results on a common nine-point grid, per photon surviving common loss. Their ranges describe settings, not confidence intervals; the lower range includes both binary reporting and assumed port confusion. The predictive validation target remains the mean of 100 repetitions. These scope statements are retained in the slides and speaking notes.

Leave the conclusion visible during questions. Reach the thermal result at 3:55, the classical/quantum bridge at 7:00, and the conclusion at 11:25. The script is a rehearsal aid; confirm the 12-minute duration aloud.

Validation completed on 10 September 2026: all 16 PDF pages rendered and visually reviewed; no LaTeX warnings or overfull/underfull boxes; all fonts embedded; extracted text within page boundaries. The English speaking text contains approximately 1,311 words, leaving time for figures and pauses within the 12-minute allocation. The cover logo was subsequently updated across all versions at the author's request.

Cover updated on 11 September 2026: ASI only, with the unused portion of the logo panel removed.
