# Local Quantum Metrology Under Reduction, Temperature, and Noise

## Projects 1, 7, and 9

**Dataset version:** saved `.npz` outputs generated between August 22 and August 25, 2026.

## Executive Summary

Projects 1, 7, and 9 form one coherent study of local quantum metrology in the transverse-field Ising model (TFIM). The parameter to estimate is the transverse field `h_x`. The common question is not simply how much QFI the full system contains, but how much information remains in an accessible subsystem after part of the probe is discarded, and how this answer changes when mixedness has different physical origins.

The three projects have distinct roles:

- **Project 1** establishes the clean, ground-state local-metrology baseline. It quantifies how exact subsystem SLD QFI and the TQFI quantities change with total size `N` and accessible size `n`.
- **Project 7** follows the thermal route from hot Gibbs states toward the ground-state regime and defines an operational thermal-crossover scale `beta_star`.
- **Project 9** compares three subsystem-level state families: the reduced ground state, a depolarized ground state reduced after noise, and a thermal state reduced after preparation. It separates the effect of *how* mixedness is produced from the effect of mixedness alone.

The strongest conclusions supported by the current data are:

1. **Accessible local QFI grows strongly with both system size and accessible subsystem size.** In the sampled open-chain scaling sequence `(N,n)=(4,2),(6,4),(8,6)`, the peak exact subsystem SLD QFI rises from `2.859` to `5.919` to `9.472`. At fixed `N=8`, increasing the accessible subsystem from `n=2` to `n=7` raises the peak from `3.247` to `10.062`, reaching the full-system value when only one qubit is traced out.
2. **Partial trace is the central metrological loss mechanism.** Exact subsystem SLD QFI never exceeds the corresponding full-system SLD QFI in the saved outputs, as required by data processing. The size of that loss depends strongly on the retained subsystem and on boundary conditions.
3. **Depolarizing noise is the clean monotonic damaging baseline.** At fixed geometry, increasing depolarizing strength steadily lowers the reduced QFI peak without changing the underlying critical structure qualitatively.
4. **Thermal preparation before partial trace can be beneficial relative to the reduced ground-state subsystem.** This is a comparison between two distinct parameterized families, not a violation of QFI monotonicity. In Project 9 Preset E at `beta=5`, the peak `thermal_sub` SLD QFI is `4.847`, above the reduced-ground-state `subsystem` peak `3.926`; in the anti-periodic boundary-condition run, `thermal_sub > subsystem` at every sampled field point.
5. **The structure of mixedness matters.** Entanglement-induced mixedness, structureless depolarization, and thermal population of low-lying excitations are not interchangeable descriptions of a mixed subsystem. States with similar or even matched reduced purity need not have the same QFI.
6. **Boundary conditions can change the qualitative hierarchy of channels.** They reshape the finite-size low-energy spectrum, hence the location and usefulness of thermal sensitivity. This is especially visible in the anti-periodic runs.

There are two important limits on the claims:

- The existing finite-size sequences are small and deliberately change both `N` and `n`; they establish a clear trend but **not a universal asymptotic scaling exponent**.
- At the finite displacement used here, `reduced_lower_tqfi` sometimes lies above exact local SLD QFI. It must therefore be called a finite-displacement TQFI quantity, not a certified pointwise lower bound on SLD QFI. The `reduced_sub_qfi_bound` is the empirically conservative lower comparator in the current saved data.

## 1. Common Experimental Language

All projects study the finite TFIM Hamiltonian `H(h_x)` and estimate the field `h_x`. For every selected field value, the code constructs a state family, evaluates its exact SLD QFI with respect to `h_x`, and evaluates fidelity-based TQFI quantities from the pair

```text
rho(h_x), rho(h_x + delta_h_x_tqfi).
```

The most important methodological rule is that a TQFI quantity must be compared with the SLD QFI of **the same state family on the same Hilbert space**. Therefore:

- local TQFI quantities are compared with `qfi_SLD_subsystem_analytical`;
- `qfi_SLD_full_reference_analytical` is a reference ceiling and a data-processing check, not the primary TQFI comparator;
- when channels are compared, all primary curves are reduced to the same `n`-qubit subsystem before comparison.

### 1.1 The QFI quantities used in the report

| Quantity | Role in this work | How it should be used |
| --- | --- | --- |
| Exact subsystem SLD QFI | `qfi_SLD_subsystem_analytical` | Primary local metrological benchmark. |
| Exact full-system SLD QFI | `qfi_SLD_full_reference_analytical` or `pure__sld_qfi` | Reference ceiling before information is discarded. |
| `reduced_sub_qfi_bound` | Superfidelity-derived finite-displacement lower quantity | Conservative local TQFI comparator in the present data. |
| `reduced_lower_tqfi` | Truncation-based finite-displacement TQFI quantity | Useful diagnostic and operational crossover observable, but not a universally valid pointwise SLD lower bound at the chosen finite `delta`. |
| `H_delta` | Maximum of two finite-displacement lower quantities | Do not use as a strict lower SLD bound because it inherits any `lower_tqfi` overshoot. |

This distinction is not cosmetic. Across the latest Project 1 and Project 7 files, the subsystem SLD is always no larger than the full-system SLD, and `reduced_sub_qfi_bound` never exceeds the local SLD. By contrast, `reduced_lower_tqfi` has finite-displacement overshoots. The largest observed excesses are `0.112` in the latest Project 1 size sweep, `1.068` in the latest Project 1 subsystem-size sweep, and `1.071` in the open-boundary Project 7 data.

For the thesis, exact SLD should carry the main quantitative conclusions. TQFI results should be reported as a second layer: a finite-displacement, truncation-aware proxy whose tightness is itself part of the result.

### 1.2 Data sets used

The report uses the most recent saved output for each label:

- Project 1: `project1_scaling_N_20260822_162213.npz` and `project1_scaling_n_20260822_162301.npz`.
- Project 7: all six outputs dated `20260823`, covering Presets A, B, and C.
- Project 9: all twenty-one outputs dated `20260825`, covering Presets A through E.

Project 1 and Project 7 use `delta_h_x_tqfi=0.1` and truncation rank `m=2`. Project 9 uses `delta_h_x=0.05` and normally `m=3`. Exact SLD QFI can be compared when the physical state families agree; raw TQFI magnitudes should not be pooled across projects without accounting for these different finite-displacement and truncation choices.

## 2. The Quantum Processes to Draw

The clearest thesis diagrams should depict **state preparation and reduction**, not merely a generic box called "noise". The following layouts are precise blueprints for the diagrams.

### 2.1 Project 1: entanglement-induced subsystem mixedness

```text
h_x --> H_N(h_x) --> prepare |psi_0(h_x)> --> rho_G(h_x)
                                                |
                                                | Tr_E
                                                v
                                      rho_sub(h_x) on S
                                                |
                                                v
                          local SLD QFI and local TQFI quantities
```

- `S` is the kept `n`-qubit subsystem.
- `E` is the discarded environment of `N-n` qubits.
- `rho_G(h_x)=|psi_0(h_x)><psi_0(h_x)|` is globally pure.
- `rho_sub(h_x)=Tr_E[rho_G(h_x)]` is mixed solely because `S` is entangled with `E`.
- There is no external noise map in this diagram. The partial trace itself is the information-discarding operation.

### 2.2 Project 9 depolarizing branch: a genuine fixed channel before reduction

```text
h_x --> H_N(h_x) --> rho_G(h_x) --> Lambda_P^(N) --> rho_dep,N(h_x; P)
                                                        |
                                                        | Tr_E
                                                        v
                                             rho_dep,S(h_x; P)
                                                        |
                                                        v
                                             local SLD QFI / TQFI
```

- `Lambda_P^(N)` is a full-system depolarizing channel with fixed probability `P`.
- The channel is parameter independent when `P` is fixed.
- The full-to-local comparison therefore obeys data processing:

  ```text
  F_Q[rho_dep,S(h_x;P)] <= F_Q[rho_dep,N(h_x;P)].
  ```

- This is the correct control for unstructured, Hamiltonian-blind external mixing.

### 2.3 Project 7 and Project 9 thermal branch: thermal preparation before reduction

```text
h_x --> H_N(h_x) --> Gibbs preparation at fixed beta --> rho_th,N(h_x; beta)
                                                            |
                                                            | Tr_E
                                                            v
                                                 rho_th,S(h_x; beta)
                                                            |
                                                            v
                                                 local SLD QFI / TQFI
```

with

```text
rho_th,N(h_x;beta) = exp[-beta H_N(h_x)] / Z(h_x,beta).
```

The key point for the diagram caption is:

> Thermal preparation is not, in general, a parameter-independent quantum channel applied to the ground-state family. The Hamiltonian and therefore the Gibbs state both depend on `h_x`.

Consequently, there is no theorem requiring

```text
F_Q[rho_th,S(h_x;beta)] <= F_Q[rho_sub(h_x)].
```

Those are distinct encoded families. The valid data-processing comparison is instead

```text
F_Q[rho_th,S(h_x;beta)] <= F_Q[rho_th,N(h_x;beta)],
```

which is satisfied by every current Project 9 sample.

This is the precise meaning of the statement that thermal preparation can be beneficial **before** partial trace: the full thermal family is prepared first, then only the same local subsystem is retained. It does not mean that a parameter-independent thermal noise channel increases QFI of a fixed already-encoded reduced state.

### 2.4 Project 9 matched-purity control: a protocol, not a fixed physical channel

```text
h_x --> rho_sub(h_x) --> target purity gamma_sub(h_x)
                          |                      |
                          | choose P(h_x)        | choose beta(h_x)
                          v                      v
                    Lambda_P(h_x)[rho_G]    rho_th,N(h_x;beta(h_x))
                          |                      |
                          +------ Tr_E ----------+
                                      |
                                      v
                    equal-purity reduced comparison families
```

Matched-purity mode controls the reduced purity at each `h_x`. It is valuable for asking whether channel structure matters at matched mixedness, but it is not a fixed-noise experiment: `P` and `beta` are functions of `h_x`. The derivative must follow this controlled path, including the `dP/dh_x` or `d beta/dh_x` contribution. The current Project 9 implementation includes these chain-rule terms.

## 3. Project 1: Clean Local Scaling Baseline

### 3.1 Question and design

Project 1 isolates the information loss caused by tracing out qubits from the ground state. It contains no external noise channel. Its role is to establish how the critical response is shared between the full probe and the accessible subsystem.

The latest saved data cover:

- a size sequence with open boundaries and `n=N-2`;
- an accessible-subsystem sequence with `N=8`, open boundaries, and `n=2,...,7`.

### 3.2 Size sequence: `N=4,6,8` with `n=N-2`

| `(N,n)` | Peak subsystem SLD QFI | Peak full SLD QFI | Local/full peak ratio | Peak `lower_tqfi` | Peak `sub_qfi_bound` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(4,2)` | `2.859` at `h_x=0.508` | `4.393` at `0.427` | `0.651` | `1.963` | `1.419` |
| `(6,4)` | `5.919` at `0.631` | `6.780` at `0.631` | `0.873` | `3.164` | `1.408` |
| `(8,6)` | `9.472` at `0.712` | `10.062` at `0.712` | `0.941` | `4.440` | `1.326` |

The local peak grows strongly over the sampled sizes. More importantly, its fraction of the full-system peak grows from about `65%` to `94%`. This occurs because the discarded environment remains two qubits while the retained subsystem grows with `N`; the scaling sweep therefore shows a combined effect of larger total systems and a larger accessible fraction.

This is a useful finite-size result, but it should not be written as a universal scaling exponent. Three points with changing `n/N` do not separate intrinsic size scaling from the changing size of the accessible region.

### 3.3 Accessible-subsystem sequence at fixed `N=8`

| `n` | Peak subsystem SLD QFI | Fraction of full SLD peak |
| ---: | ---: | ---: |
| `2` | `3.247` | `0.323` |
| `3` | `5.154` | `0.512` |
| `4` | `6.932` | `0.689` |
| `5` | `8.389` | `0.834` |
| `6` | `9.472` | `0.941` |
| `7` | `10.062` | `1.000` |

This is the cleanest local-information result in the whole study. Retaining more qubits produces a rapid, monotonic recovery of the critical response. By `n=7`, tracing a single qubit does not reduce the peak SLD QFI within the displayed precision for this finite system.

The SLD maximum moves toward the full-system peak as `n` increases. This shows that access to a larger region restores both the height and the location of the metrologically relevant critical feature.

### 3.4 What the TQFI quantities add

At the local-SLD peak, the `lower_tqfi`/SLD ratio in the two Project 1 sweeps ranges from roughly `0.42` to `0.96`; the corresponding `sub_qfi_bound`/SLD ratio ranges from about `0.05` to `0.60`. Thus the bounds are informative but can be loose, especially when the reduced state is strongly mixed or the truncation does not capture the response optimally.

The conclusion is not that one bound is always preferable. Rather:

- exact subsystem SLD QFI is the baseline when classical exact diagonalization is available;
- `sub_qfi_bound` is the safer conservative TQFI quantity in these saved data;
- `lower_tqfi` is useful for its truncation-based construction, but its finite-`delta` overshoots require careful language.

### 3.5 Project 1 figures to include

Use [project1_plots.ipynb](/home/ronin/Dev/space/QCES/cqes/project1_plots.ipynb).

**Main-text figure P1.1:** Preset A small multiples, "Local bounds and exact subsystem SLD", one panel for each `(N,n)`. This establishes the local-versus-global critical scaling story.

**Main-text figure P1.2:** Preset B exact subsystem-SLD overlay versus `n`. It is the clearest visual proof that access to a larger subsystem restores QFI.

**Supplementary figure P1.S1:** Separate Viridis heatmaps for exact subsystem SLD, `lower_tqfi`, and `sub_qfi_bound` for the `n` sweep. These track peak movement and bound tightness without forcing four distinct quantities into a single heatmap.

## 4. Project 7: Thermal Crossover to Local Metrological Recovery

### 4.1 Question and design

Project 7 asks how the local response changes as the full probe is thermally prepared at increasing inverse temperature and then reduced to the same subsystem. It compares a ground-state row with thermal rows at

```text
beta = 0.1, 0.25, 0.5, 1, 2, 5, 10, 25, 50.
```

The runner stores `beta_star`: the interpolated temperature scale at which the **peak `reduced_lower_tqfi`** reaches `90%` of the ground-state `lower_tqfi` peak. This is an operational finite-displacement definition, not a universal thermodynamic transition temperature.

### 4.2 Core open-chain result

For `N=6`, `n=4`, open boundaries:

| State | Peak `lower_tqfi` | Peak local SLD QFI | Peak full SLD QFI |
| --- | ---: | ---: | ---: |
| Ground state | `5.019` | `6.014` | `6.782` |
| `beta=1` | `0.747` | `1.714` | `2.730` |
| `beta=2` | `1.440` | `2.792` | `4.292` |
| `beta=5` | `3.987` | `6.151` | `9.578` |
| `beta=10` | `6.164` | `8.962` | `16.916` |

The stored crossover is

```text
beta_star = 6.216
```

for the chosen `90%` `lower_tqfi` criterion. Cooling strongly restores local metrological sensitivity and moves the thermal peak from the edge of the scan toward the finite-size critical region.

The fact that thermal SLD peaks can exceed the ground-state peak is physically possible in this finite-size setting. The thermal family gains field sensitivity from both eigenvector changes and field-dependent populations of low-lying excitations. Around the open-chain peak at `h_x=0.547`, the first excitation gap is only about `0.038`, so even `beta=50` is not yet uniformly in the ground-state limit across the scanned field interval. The maximization over `h_x` can select a low-gap region at each beta.

This must be phrased carefully: the data demonstrate a finite-temperature spectral-susceptibility effect over the finite scan, not that a Gibbs state remains more informative than the ground state at every fixed field as `beta -> infinity`.

### 4.3 Size and boundary-condition crossover scales

| Geometry | Stored `beta_star` from `lower_tqfi` |
| --- | ---: |
| Open, `N=4`, `n=2` | `5.170` |
| Open, `N=6`, `n=4` | `6.216` |
| Periodic, `N=6`, `n=4` | `3.122` |
| Anti-periodic, `N=6`, `n=4` | `0.517` |

The open-chain finite-size comparison suggests that a larger system needs a somewhat colder Gibbs state to reach the selected local TQFI recovery threshold. Boundary conditions have an even larger effect: periodic boundaries recover on a lower beta scale than open boundaries, while anti-periodic boundaries behave qualitatively differently because their low-energy sector is altered.

The anti-periodic result is scientifically interesting but should be presented together with its spectrum and scan-window caveat. Its thermal local SLD is maximal at the left scan boundary `h_x=0.1`, and the first two gaps there are approximately `0.0295`. The appropriate claim is that anti-periodic boundary conditions create exceptionally strong low-field thermal susceptibility in the sampled window; it is not yet a claim about a bulk critical exponent.

### 4.4 Project 7 figures to include

Use [project7_plots.ipynb](/home/ronin/Dev/space/QCES/cqes/project7_plots.ipynb).

**Main-text figure P7.1:** Preset A "Recovery of peak local metrological information" versus beta. This is the cleanest direct visualization of the thermal-crossover question and the `90%` reference line.

**Main-text figure P7.2:** The ground-state local-bounds/subsystem-SLD panel together with the thermal overlay for `lower_tqfi`. It shows how the field location of the response evolves as the state cools.

**Main-text figure P7.3:** The `beta_star` summary across the three boundary conditions. Use it to motivate the spectral role of boundary conditions, not as a universal phase diagram.

**Supplementary figure P7.S1:** Separate SLD and TQFI tightness heatmaps across beta. They make clear that the peak can move and that TQFI tightness is not uniform across the sweep.

## 5. Project 9: Channel Structure After Full-System Preparation

### 5.1 Question and design

Project 9 compares three primary `n`-qubit families on equal footing:

```text
subsystem  = Tr_E[rho_G]
depol_sub  = Tr_E[Lambda_P^(N)(rho_G)]
thermal_sub = Tr_E[rho_th,N(beta)]
```

The primary output is exact SLD QFI on each reduced family. Full-system `pure`, `depolN`, and `thermalN` curves are retained as diagnostic references.

There are two modes:

- **Fixed-noise mode** fixes `P` or `beta`. It is the main physical experiment.
- **Matched-purity mode** chooses `P(h_x)` and `beta(h_x)` to match reduced purity. It is a structural control rather than the default physical model.

All latest Project 9 files pass the required full-to-local consistency checks at every sampled field:

```text
thermal_sub <= thermalN,
depol_sub <= depolN,
subsystem <= pure.
```

This validates the corrected SLD derivatives used in the current channel comparison.

### 5.2 Preset A: matched-purity finite-size control

| `(N,n)` | Peak pure SLD | Peak subsystem SLD | Subsystem/pure ratio |
| --- | ---: | ---: | ---: |
| `(4,2)` | `4.388` | `3.215` | `0.733` |
| `(6,4)` | `6.771` | `6.013` | `0.888` |
| `(8,6)` | `10.057` | `9.436` | `0.938` |

The local scaling trend agrees with Project 1: larger retained systems preserve a larger fraction of the full critical response. The latest Project 9 data now include the `N=8` control, so the three-point trend is complete.

However, this preset is a **consistency control**, not the strongest channel-separation result. Purity matching drives the matched parameters to essentially ground-state values:

- `P_matched` is approximately `4e-9` to `1.5e-8`;
- `beta_matched` ranges from `500` to `1.2e5`.

Accordingly, `subsystem`, `depol_sub`, and `thermal_sub` coincide to numerical precision. The valid conclusion is that the matched-family derivative and reduction are consistent in this near-pure regime. It is not evidence that the three physical noise mechanisms are generally equivalent.

### 5.3 Preset B: accessible-subsystem size under fixed noise

For `N=6`, periodic boundaries, and the fixed-noise baseline, the peak subsystem SLD QFI behaves as follows:

| `n` | `subsystem` | `depol_sub` | `thermal_sub` |
| ---: | ---: | ---: | ---: |
| `1` | `0.972` | `0.722` | `0.348` |
| `2` | `2.134` | `1.724` | `0.688` |
| `3` | `3.164` | `2.672` | `1.040` |
| `4` | `3.926` | `3.419` | `1.393` |
| `5` | `4.344` | `3.865` | `1.741` |

The hierarchy at the principal peak is clear:

```text
subsystem >= depol_sub > thermal_sub
```

for this particular `beta=1` baseline. Yet that peak ordering is not the whole story. In every `n` run, `thermal_sub` exceeds `subsystem` over broad off-peak field intervals. For `n=4`, for example, the largest pointwise thermal advantage is `0.456` at `h_x=1.686`, even though the thermal peak remains lower.

This distinction between peak ordering and field-resolved ordering is important for the thesis. A channel can be inferior for the maximum achievable QFI while being superior in a different operating-field region.

### 5.4 Preset C: boundary-condition dependence

At fixed `N=6`, `n=4`:

| Boundary condition | Peak `subsystem` | Peak `depol_sub` | Peak `thermal_sub` |
| --- | ---: | ---: | ---: |
| Open | `6.014` | `5.287` | `1.714` |
| Periodic | `3.926` | `3.419` | `1.393` |
| Anti-periodic | `1.293` | `1.096` | `1.892` |

The anti-periodic branch provides the clearest thermal advantage: `thermal_sub` exceeds `subsystem` at all `60/60` sampled field points and has a larger peak, `1.892` versus `1.293`. Its thermal peak occurs at the lower edge of the field scan, again emphasizing that this advantage is tied to the boundary-condition-dependent low-energy spectrum.

### 5.5 Preset D: depolarizing strength

With `N=6`, `n=4`, periodic boundaries, and only `P` varied:

| `P` | Peak `depol_sub` | Change from `P=0` |
| ---: | ---: | ---: |
| `0.00` | `3.926` | `0%` |
| `0.05` | `3.661` | `-6.7%` |
| `0.10` | `3.419` | `-12.9%` |
| `0.20` | `2.953` | `-24.8%` |
| `0.30` | `2.499` | `-36.4%` |

This is the clean baseline result. Depolarization lowers the local QFI smoothly and monotonically. The ground-subsystem and thermal curves remain unchanged in this preset, as they should, because only `P` is varied.

### 5.6 Preset E: thermal inverse-temperature sweep

With `N=6`, `n=4`, periodic boundaries, fixed depolarization `P=0.1`, and varying beta:

| `beta` | Peak `thermal_sub` | Peak field | Relation to peak `subsystem=3.926` |
| ---: | ---: | ---: | --- |
| `0.2` | `0.152` | `0.100` | strongly suppressed |
| `0.5` | `0.729` | `0.100` | suppressed |
| `1.0` | `1.393` | `0.792` | suppressed |
| `2.0` | `2.607` | `1.076` | suppressed peak, but pointwise crossings occur |
| `5.0` | `4.847` | `1.036` | `23.5%` above the subsystem peak |

This is the headline thermal result. At `beta=5`, thermal preparation on the full probe followed by partial trace gives a local peak QFI larger than the peak of the reduced ground-state subsystem. It also exceeds `subsystem` at `40/60` sampled field points. At the same time, it remains below its own full-system thermal parent:

```text
peak thermal_sub = 4.847 < peak thermalN = 8.456.
```

Therefore the effect is both physically allowed and numerically consistent. It arises because low-lying thermal populations respond strongly to `h_x`; it is not a data-processing violation.

The useful, precise thesis statement is:

> For the finite TFIM geometries and field windows studied here, thermal preparation before partial trace can enhance the local SLD QFI relative to the entanglement-induced reduced ground-state subsystem. The enhancement is regime dependent, strongest at larger beta in the present sweep, and constrained by the full thermal-state QFI.

Do not replace this with the stronger but false statement that temperature or thermal noise is generically beneficial.

### 5.7 Project 9 figures to include

Use [project9_plots.ipynb](/home/ronin/Dev/space/QCES/cqes/project9_plots.ipynb).

**Main-text figure P9.1:** Preset B peak SLD QFI versus subsystem size `n`, with `subsystem`, `depol_sub`, and `thermal_sub`. This is the cleanest joint scaling and channel-structure plot.

**Main-text figure P9.2:** Preset D peak SLD QFI versus depolarizing probability `P`. It establishes the monotonic unstructured-noise baseline.

**Main-text figure P9.3:** Preset E peak SLD QFI versus beta. This should be the central thermal-benefit figure. State explicitly in the caption that every point is a maximum over the `h_x` sweep and show the peak locations in a companion panel or table.

**Main-text figure P9.4:** One field-resolved Preset E run at `beta=5`, plotting `subsystem`, `depol_sub`, and `thermal_sub` together. It prevents the peak-only narrative from hiding where the thermal advantage occurs.

**Main-text figure P9.5:** Preset C field-resolved boundary-condition panels. The anti-periodic panel is the most visually compelling example of channel ordering changing with spectral structure.

**Supplementary figure P9.S1:** Preset A matched-purity control with stored `P_matched` and `beta_matched` metadata. Use it to document why the curves coincide.

**Supplementary figure P9.S2:** The consistency-audit output or a compact table verifying `thermal_sub <= thermalN`, `depol_sub <= depolN`, and `subsystem <= pure`.

## 6. Cross-Project Conclusions for the Thesis

### 6.1 Local metrology is controlled by accessible degrees of freedom

Project 1 gives the baseline answer: exact local SLD QFI increases rapidly when more qubits are accessible. Project 9 confirms the same behavior after channel preparation. The physical message is not simply "larger Hilbert space gives larger QFI." It is more specific:

> The critical metrological response is spatially distributed. Partial trace removes a variable fraction of the response, and the retained fraction grows strongly with the size of the accessible subsystem.

The existing sequences support monotonic finite-size and subsystem-size trends. They do not yet establish whether the asymptotic growth is extensive, superextensive, or follows a particular critical exponent. To make an exponent claim, one would need a controlled sequence with fixed `n/N` or fixed `n`, more values of `N`, common boundary conditions, and a finite-size scaling analysis of peak height and peak shift.

### 6.2 Different sources of mixedness have different metrological fingerprints

The same local density-matrix dimension can arise through three distinct mechanisms:

1. **Entanglement-induced mixedness:** discard a correlated environment from a globally pure ground state.
2. **Depolarizing mixedness:** apply a Hamiltonian-blind full-system channel, then discard the environment.
3. **Thermal mixedness:** populate the spectrum of the parameter-dependent Hamiltonian, then discard the environment.

Projects 7 and 9 show that these mechanisms are not interchangeable. Purity alone cannot predict local QFI. Depolarization removes information broadly and monotonically. Thermal preparation can redistribute sensitivity into population changes of low-energy levels, making it favorable in some field and boundary-condition regimes. Entanglement-induced mixedness is the physically clean baseline but is not always the local optimum among distinct state families.

### 6.3 Thermal advantage is real, conditional, and needs the correct comparison

The current data support a carefully bounded claim:

- `thermal_sub` can exceed `subsystem` pointwise and in peak height;
- this occurs after thermal preparation of the full system and then partial trace;
- it is strongest in the low-gap parts of the sampled spectrum and can move toward the critical region as beta increases;
- it does not violate monotonicity because the valid comparison is `thermal_sub <= thermalN`, not `thermal_sub <= subsystem`.

The word "beneficial" must always include its reference:

```text
beneficial relative to the reduced ground-state subsystem at fixed accessible size,
not an unconditional increase under a parameter-independent noise channel.
```

### 6.4 TQFI and SLD tell complementary but not identical stories

SLD QFI is the exact local differential metric used for the main physical comparisons. TQFI quantities are finite-displacement observables and expose whether a low-rank or fidelity-based description retains the same metrological feature.

The saved data show that tightness is state and geometry dependent. In particular, the truncation-based `lower_tqfi` can overshoot the differential SLD at finite delta, while `sub_qfi_bound` remains conservative in the current arrays. This is a useful methodological conclusion, not merely a nuisance:

> A TQFI protocol should be validated against the exact local SLD on small systems before it is extrapolated to settings where exact SLD is unavailable.

### 6.5 Boundary conditions are a spectral-control resource

The boundary-condition results are not a secondary technical detail. They change gaps, low-energy sectors, peak positions, and the thermal crossover scale. In the present finite systems, they can even reverse the ordering between the reduced ground-state and reduced thermal families.

The thesis narrative can therefore frame boundary conditions as a controlled way of changing the spectral mechanism through which thermal populations encode `h_x`.

## 7. What to State Carefully and What to Do Next

### Statements supported now

- Exact local SLD QFI grows with accessible subsystem size in the sampled finite systems.
- Keeping all but one qubit can recover essentially all of the full-system peak QFI in the tested `N=8` and `N=6` periodic cases.
- Depolarizing noise suppresses local QFI monotonically as `P` grows.
- Thermal preparation before partial trace can outperform the reduced ground-state subsystem in specific finite-size, field, temperature, and boundary-condition regimes.
- The mechanism of mixedness matters independently of the reduced Hilbert-space dimension.
- The current Project 9 SLD implementation passes the relevant full-to-local QFI monotonicity checks.

### Statements that need qualification

- Do not claim a universal QFI scaling exponent from the present small size sweeps.
- Do not say thermal noise is always beneficial, or that it increases QFI under a fixed channel acting on the same encoded family.
- Do not compare local TQFI values directly with global SLD QFI.
- Do not call `lower_tqfi` a strict pointwise lower SLD bound at the current finite displacements.
- Do not infer a bulk transition from a peak that sits at the edge of the finite field scan.

### Recommended next calculations

1. Extend Project 9 Preset E to `beta=10,25,50` and inspect pointwise convergence to the reduced ground-state family at fixed `h_x`. This will separate finite-temperature enhancement from the true large-beta limit.
2. Repeat the main size sweep at fixed `n/N` and, separately, fixed `n`. Add at least one larger feasible size with the memory-aware worker cap. Fit only after the scaling protocol is controlled.
3. For Project 7, save both the existing operational `beta_star` and a second crossover based on exact local SLD or on `sub_qfi_bound`. This will distinguish physical thermal recovery from finite-displacement TQFI behavior.
4. For boundary-condition figures whose thermal peak lies at `h_x=0.1`, extend the field window downward or justify the lower bound analytically. A boundary maximum is a prompt for scan validation, not a final peak location.
5. Add a compact spectrum panel showing the first excitation gap alongside the thermal-QFI peak for the strongest thermal-enhancement examples. This will make the low-gap mechanism immediately persuasive.

## Takeaway

The central outcome of the combined projects is that local quantum metrology cannot be characterized by mixedness alone. What matters is the full sequence of physical processes that produces the accessible state: critical ground-state preparation, spectral thermal population, external depolarization, and information loss through partial trace.

Project 1 establishes how much critical information survives locally. Project 7 shows that temperature controls a crossover in local sensitivity and that this crossover is spectrum dependent. Project 9 demonstrates that thermal preparation can, in selected regimes, outperform the reduced ground-state subsystem while depolarization remains uniformly detrimental. Together, these results support a practical design principle for finite quantum sensors:

> Preserve access to the relevant subsystem, engineer the low-energy spectrum, and distinguish structured thermal preparation from structureless noise. The origin of mixedness is itself a metrological resource variable.
