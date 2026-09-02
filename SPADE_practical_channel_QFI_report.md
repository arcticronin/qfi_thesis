# Corrected SPADE Practical-Channel and QFI Report

## Scope and verdict

The change of perspective is scientifically useful: the experiment should be
described as a sequence of quantum, optical, detection, and count-statistical
channels, and information should be compared only after those channels are
specified. This is a stronger formulation than treating two detector readings
as an experimental density matrix or calling a fitted scale an unconditional
detector efficiency.

The corrected analysis does **not**, however, support the earlier numerical
claim that the fixed reference channel fits the data. Three implementation
problems changed that conclusion:

1. the Hermite-Gauss displacement was scaled as though the sorter were aligned
   to the midpoint, whereas the paper aligns it to the brighter source;
2. the 100 independent 10 ms repeats in the data were compared with the
   paper's one-second photon number without first summing the repeats;
3. a Gaussian quasi-likelihood was used for counts whose setting means are only
   about 7--19, producing non-integer and sometimes negative bootstrap data.

After correcting all three, the best fixed-channel value is
`eta = 0.05094`, but its goodness-of-fit bootstrap gives
`p = 0.00498`. The fixed channel is rejected, so this `eta` is only the
optimum of a rejected model and **must not be reported as a measurement**.
More flexible deterministic mean models improve the visual fit but are also
rejected by discrete-count bootstraps. A physics-informed **hierarchical mean
channel** does produce a useful positive result: after adding a stochastic
calibration field, it predicts held-out setting means with standardized-error
SD `1.00--1.04` and `93.5--94.7%` coverage for nominal 95% intervals. Thus the
mean response can be modeled credibly, although the fitted `eta` claim and a
complete parametric model for every 10 ms count still do not survive.

## What the paper and dataset actually define

The reference paper is [spade.pdf](../../../../thesis/papers/spade.pdf). It aligns
the demultiplexer to the brighter source and records

```text
n1 = C_HG01 + C_HG10.
```

For each `(epsilon, d_a)` setting, it combines 100 independent measurements of
10 ms each into a one-second count. The available array has shape
`21 x 25 x 100`; its final axis contains those individual 10 ms counts.

| Raw-data property | Corrected value |
| --- | ---: |
| Separation range `d_a = d/w0` | `-0.66667` to `0.66667` |
| Relative-intensity range `epsilon` | `0.00427` to `0.09593` |
| Repeats per setting | `100` |
| Duration per repeat | `0.010 s` |
| Mean `n1` per repeat | `6.93` to `19.44` |
| Median zero-separation count per repeat | `8.17` |
| Median Fano factor `Var(n1)/E[n1]` | `2.497` |
| Largest signed-distance asymmetry | `3.84` counts |

![Raw data and count-noise diagnostics](../exoplanets/figures/spade_raw_diagnostics.png)

Only the aggregate first-order result is present. The file does not contain
HG00 counts, separate HG01/HG10 streams, higher-order outputs, source-blocked
background, incident-photon counts, or an independent sorter cross-talk
matrix. Consequently, background, flux, survival, and HG00 leakage are partly
degenerate in this record.

## Correct bright-source-aligned HG model

Let `d_a = d/w0`. For the alignment used in the paper, the displaced weak
source has coherent-state amplitude

```text
alpha = d_a / 2,             q = |alpha|^2 = d_a^2 / 4.
```

The modal probabilities of that displaced Gaussian are therefore

```text
P_HG00 = exp(-q),
P_HG1  = q exp(-q),
P_HGn  = exp(-q) q^n / n!.
```

For an incoherent bright source at the origin and a displaced weak source with
relative weight `epsilon`, the ideal aggregate first-order probability is

```text
p1 / eta = epsilon q exp(-q).
```

The superseded code used `q = d_a^2/16`. That is a factor-of-four error in the
small-separation first-order response and corresponds to a different spatial
origin convention. All current inference, channel, helper, fitting, and QFI
implementations now use `q = d_a^2/4`.

## Exposure accounting and paper-style calibration

The paper plots the sum of the 100 repeats and quotes a detected photon number
`eta n` of roughly `40,000--80,000` during one second. Accordingly, the
paper-style regression must use

```text
n1_one_second = sum(i=1..100, n1_i),
```

not the average 10 ms count. With the corrected aggregation, the median
zero-separation baseline is `817` counts per second. A pooled quadratic model

```text
n1 = chi_eff (eta n) + c epsilon d_a^2
```

gives the following conditional values:

| Assumed one-second `eta n` | Effective baseline fraction `chi_eff` | Response `c` | `R^2` |
| ---: | ---: | ---: | ---: |
| `40,000` | `0.020743 +/- 0.000109` | `27,282.7 +/- 430.1` | `0.88499` |
| `80,000` | `0.010371 +/- 0.000054` | `27,282.7 +/- 430.1` | `0.88499` |

![One-second paper-style calibration](../exoplanets/figures/spade_paper_calibration.png)

These fractions are **effective baseline fractions**, not measurements of pure
HG00-to-HG1 cross-talk. For comparison, the paper's independent cross-talk
value `chi = 0.0035` would contribute only 140 or 280 baseline counts for the
two quoted photon numbers, whereas the fitted offset is about 830 counts.
Dark/background counts, flux normalization, drift, mismatch, or data-selection
differences can all contribute to this discrepancy.

The earlier per-curve comparison silently applied the one-second `eta n` to a
10 ms mean. It was therefore off by a factor of 100 and is superseded.

## The practical-channel perspective

The physically useful abstraction is the composition

```text
source state
  -> propagation/survival
  -> alignment and PSF mismatch
  -> mode-sorter cross-talk/loss
  -> detector response
  -> discrete count process.
```

For the ideal source state,

```text
rho = (1-eta)|vac><vac|
    + eta[(1-epsilon)|psi_0><psi_0|
          + epsilon|psi_d><psi_d|].
```

This one-photon spatial mixture has support across infinitely many HG basis
vectors, but it is a mixture of only two pure one-photon states and hence has
rank at most two in that sector. Infinite basis support and matrix rank are not
the same statement.

An experimentally accessible low-mode reduction should be a flagged quantum
channel, for example

```text
E_M(rho) = P_M rho P_M
         + Tr[(I-P_M)rho] |fail><fail|,
```

where `P_M` projects onto the measured modes. The failure flag preserves the
probability outside the accessible subspace. Renormalizing a `2 x 2` block and
discarding the missing probability can artificially inflate information.

This construction makes a meaningful distinction:

| Quantity | Meaning | Available from current data? |
| --- | --- | --- |
| Source-state QFI | Ultimate information before the instrument | Yes, from an assumed source model |
| Full ideal-SPADE CFI | Information in all ideal HG outcomes | Yes, from the assumed ideal model |
| Accessible-channel QFI/CFI | Information after a calibrated low-mode channel | Only conditionally |
| Count CFI | Information after readout and count noise | Only for a specified accepted count model |
| Experimental QFI | QFI reconstructed from sufficient experimental state data | No |

The current aggregate count grid can test a forward model, but it cannot
tomographically reconstruct `rho` or identify all components of the channel.

## Discrete count models

The corrected fixed-channel code uses a Poisson/NB1 family. At `F = 1` it is
exactly Poisson; for `F > 1` it is a negative-binomial distribution
parameterized so that

```text
E[Y] = mu,                   Var[Y] = F mu.
```

This preserves non-negative integer counts in fitting and bootstrapping and is
much more appropriate than a Gaussian model that can generate negative counts.
It is not, however, the final readout law. When the setting means are treated
as saturated nuisance parameters, NB1 gives `F = 2.4188` and negative log
likelihood `153,969.7`. A Poisson-lognormal model gives log-rate
`sigma = 0.3765` and negative log likelihood `153,893.2`, an AIC improvement of
`153.0`.

The Poisson-lognormal model correctly reproduces the number of zero counts, but
it still underestimates variance heterogeneity and median within-setting
skewness (`p = 0.00664` and `p = 0.0133` in 300-simulation two-sided checks).
Therefore, the hierarchical mean analysis below uses empirical standard errors
of the 100 repeats and honest held-out prediction. For final uncertainty
propagation on this dataset, resampling the observed repeats is safer than
pretending that either one-parameter count family is exact.

## Corrected fixed reference scenario

The reference assumptions now explicitly apply to one 10 ms acquisition:

| Fixed assumption | Value |
| --- | ---: |
| Illustrative incident photons per 10 ms | `40,000` |
| HG00-to-HG1 leakage | `0.0035` |
| HG1 transmission | `0.9965` |
| Higher-order-to-HG1 leakage | `0` |
| Dark/background count | `0` |
| Alignment offset | `0` |
| PSF-width scale | `1` |
| Epsilon power | `1` |
| Fano factor | `2.6` |

`40,000` per 10 ms is an explicit illustrative normalization, not the paper's
one-second `eta n`. Under this assumption, the fitted optimum is:

| Conditional fixed-model result | Value |
| --- | ---: |
| `eta_hat` | `0.0509391` |
| Conditional 99.9% profile interval | `[0.0505743, 0.0513051]` |
| Setting-mean Pearson discrepancy | `4327.62` |
| Bootstrap median discrepancy | `524.73` |
| Discrete bootstrap simulations | `200` |
| Corrected bootstrap p-value | `1/201 = 0.00498` |

The narrow interval describes curvature *inside the rejected scenario*; it is
not an uncertainty interval for physical efficiency. The implied detected
normalization is about `2,038` photons per 10 ms, or `203,800` per second,
which is also inconsistent with directly identifying this illustrative input
with the paper's `40,000--80,000` detected photons per second.

![Rejected fixed model and effective affine comparison](../exoplanets/figures/spade_model_comparison.png)

## Effective mean models do not yet close the gap

Several less restrictive mean surfaces were fitted to determine whether the
failure was only the fixed calibration. Each model used a fitted NB1 Fano
factor and was tested by refitting simulated discrete datasets.

| Effective model | `R^2` | Fitted `F` | Mean Pearson | Bootstrap median | Bootstrap `p` |
| --- | ---: | ---: | ---: | ---: | ---: |
| Affine background + first order | `0.89355` | `2.4796` | `1271.1` | `524.5` | `1/101` |
| Source/calibration deformation | `0.90911` | `2.4710` | `1097.7` | `519.8` | `1/101` |
| Added higher-order tail | `0.91650` | `2.4673` | `1025.1` | `523.1` | `1/101` |

All three remain rejected at the resolution of 100 bootstrap simulations. The
source/calibration fit drives the PSF scale to its lower bound (`0.6`), while
the tail fit requires a negative tail coefficient. Those are warnings that
the added flexibility is absorbing structure rather than identifying a
credible optical mechanism. The affine curve is still useful as a descriptive
summary, but not as an accepted generative channel.

The repeat index does not show evidence of a common drift mode: the standard
deviation of the across-setting standardized repeat average is `0.0427`,
essentially the independent-repeat expectation `0.0436`, and its lag-one
correlation is `0.044`. The rejected models instead leave spatially correlated
setting-to-setting residuals. This points to coupling/flux calibration that
changes with nominal position and intensity, plus setting-dependent
overdispersion. The aggregate array lacks the metadata needed to identify the
mechanism uniquely.

## A predictively validated hierarchical mean channel

The better model keeps the corrected physical response as its center:

```text
mu0(d_a, epsilon) = B + A epsilon q exp(-q),
q = (d_a - delta)^2 / 4.
```

It then represents the residual coupling/calibration as a multiplicative
stochastic field,

```text
log[mu(d_a, epsilon) / mu0(d_a, epsilon)]
    ~ Matern-3/2 Gaussian process + independent setting scatter.
```

The GP is not being called a new quantum effect. It is a classical calibration
channel placed after the ideal HG response. This is preferable to forcing
position/intensity-dependent coupling into `eta`, PSF width, or a negative
higher-order amplitude.

| Hierarchical-channel component | Fitted value |
| --- | ---: |
| Background `B` per 10 ms | `8.23045` counts |
| First-order response `A` | `1225.58` counts |
| Displacement offset `delta` | `0.009824 w0` |
| Effective ratio `B/A` | `0.006716` |
| Correlated log-response SD | `0.05248` (about `5.25%`) |
| Independent setting log-response SD | `0.02520` (about `2.52%`) |
| Correlation length in `d_a` | `0.0597 w0` |
| Correlation length in `epsilon` | `0.0228` |

`B/A` is only a leakage-like effective ratio; it becomes an optical cross-talk
probability only if background is negligible and the first-order transmission
normalization is known.

![Hierarchical channel and grouped holdout validation](../exoplanets/figures/spade_hierarchical_channel.png)

The primary evidence is grouped five-fold cross-validation. Every fold refits
the physical mean, variance law, GP amplitudes, and length scales without using
the held-out means.

| Held-out structure | Mean-count RMSE | Standardized residual SD | Nominal 95% coverage |
| --- | ---: | ---: | ---: |
| Interleaved checkerboard cells | `0.606` | `1.004` | `93.52%` |
| Complete distance rows | `0.734` | `1.041` | `94.67%` |
| Complete epsilon columns | `0.609` | `1.009` | `93.71%` |

The residual widths are essentially one and the coverage is close to nominal,
including when entire rows or columns are withheld. On the complete grid, the
GP marginal Mahalanobis discrepancy is `527.10` for `518` approximate degrees
of freedom (`1.018` per degree of freedom; conditional `p = 0.381`). Because
the GP hyperparameters were estimated from the same grid, that p-value is only
a secondary diagnostic; the held-out results are the stronger evidence.

This is the “nice result” supported by the present record: a calibrated,
predictive response channel for the **100-repeat setting mean**. It does not
make photon survival identifiable, and it does not make the remaining
individual-count tail mismatch disappear. For uncertainty at the recorded
settings, empirical repeat resampling should accompany this mean channel.

## Identifiable sequential-channel fit

The final fit implements the perspective shift directly:

```text
source state
  -> erasure/survival channel
  -> flagged accessible-mode reduction (HG0, HG1, fail)
  -> externally fixed stochastic readout matrix
  -> background and setting-dependent coupling calibration
  -> empirical repeated-count observation layer.
```

The source uses the paper convention `alpha = d_a/2`. The accessible-mode map
is trace preserving: probability outside HG0/HG1 is sent to an explicit
`fail` flag rather than discarded and renormalized. The readout uses the
paper's independently reported `chi = 0.0035` as a *symmetric sensitivity
assumption*,

```text
R = [[0.9965, 0.0035, 0],
     [0.0035, 0.9965, 0],
     [0,      0,      1]].
```

Its columns sum to one. The paper does not supply a complete transfer matrix,
so symmetry is not claimed as measured. An additive background is fitted
instead of forcing the full zero-separation baseline to be optical cross-talk.

`H_data` contains neither launched photons nor an absolute HG1 coupling
calibration. The identifiable scale is therefore

```text
T = N_in eta
```

per 10 ms repeat. The smooth coupling field is constrained to weighted
geometric mean one. That convention prevents it from absorbing the global
scale, but it does not turn `T` into an absolute efficiency.

| Sequential-channel result | Value |
| --- | ---: |
| Fixed paper cross-talk `chi` | `0.0035` |
| Raw physical-base background per 10 ms | `3.9099` counts |
| Raw physical-base `T` per 10 ms | `1234.43` |
| Calibrated conditional `T` per 10 ms | `1304.25` |
| Conditional repeat-bootstrap 95% interval | `[1295.88, 1313.06]` |
| Conditional repeat-bootstrap 99.9% interval | `[1291.23, 1315.92]` |
| Grouped cross-fit envelope | `[1251.49, 1359.47]` |

The bootstrap resamples the 100 observed 10 ms repetitions within each
setting while freezing nuisance calibration. Its narrow interval is
conditional statistical uncertainty; the wider grouped cross-fit envelope is
the more useful indication of calibration and transport sensitivity.

| Held-out structure | Mean-count RMSE | Standardized residual SD | Nominal 95% coverage |
| --- | ---: | ---: | ---: |
| Interleaved checkerboard cells | `0.608` | `1.018` | `93.71%` |
| Complete distance rows | `0.752` | `1.061` | `95.05%` |
| Complete epsilon columns | `0.610` | `1.023` | `93.52%` |

![Identifiable sequential-channel fit](../exoplanets/figures/spade_identifiable_quantum_channel.png)

The fitted conditional scale corresponds to `130,425` per second, above the
paper's quoted detected-photon range `40,000--80,000` per second (`400--800`
per stored repetition). This is a diagnostic, not an eta estimate: the paper
quotes `eta n`, while the current file provides neither launched `n` nor enough
auxiliary outputs to reproduce its normalization. If an independent launched
photon measurement later becomes available, the conversion is simply

```text
eta = 1304.25 / N_in_per_10ms.
```

Varying `chi` from `0` to `0.0065` changes the raw throughput only from about
`1226` to `1242`, but trades the inferred background from `8.23` down to `0.16`
counts. Throughput is comparatively stable; the background/cross-talk split is
not identifiable from the aggregate stream.

## Replaceable plausible-channel workbench

The analysis also includes an explicitly provisional model for phenomena that
the present file cannot calibrate: Gaussian alignment jitter, HG-basis
dephasing, coherent HG0/HG1 mixing, mode-dependent erasure into `fail`, an
asymmetric stochastic readout, background, and overdispersed counts. These are
physically valid channels, but their example values are **invented sensitivity
placeholders**, not fitted discoveries.

Each parameter in
[`spade_plausible_channels.example.json`](../exoplanets/spade_plausible_channels.example.json)
has four fields: value, provenance status, phenomenon represented, and the
measurement needed to calibrate it. The fit policy freezes all such values and
fits only `T`, background, displacement offset, and a zero-mean coupling
field. Authors can replace a placeholder with a measured number and rerun the
same fit and QFI pipeline without editing the model code.

The deliberately provisional default sequence is:

```text
random displacement (sigma = 0.01 w0; invented)
  -> HG dephasing (visibility = 0.98; invented)
  -> coherent HG0/HG1 rotation (theta = 0.01 rad; invented)
  -> modal transmissions (t0 = 0.99, t1 = 0.97; invented)
  -> HG0-to-HG1 readout = 0.0035 (paper)
  -> reverse readout = 0.0035 (invented symmetry assumption).
```

This example gives `T = 1342.35` per 10 ms and a grouped cross-fit envelope of
about `[1289.62, 1399.11]`. The change from `1304.25` is exactly why these
numbers must retain their provenance labels: invented modal loss and mixing
can be traded against the throughput scale. The workbench reports one-at-a-time
identity ablations so that this dependence is visible rather than buried.

![Replaceable provisional-channel fit and sensitivity](../exoplanets/figures/spade_plausible_channel_workbench.png)

## QFI and information retention

With the corrected bright-source convention, numerical validation of the
ideal quantum model gives:

| Check | Result |
| --- | ---: |
| Full ideal-SPADE `CFI / QFI` over representative settings | `0.99899` to `1.00000` |
| First-order-only `CFI / QFI` | `0.78434` to `0.94485` |
| Maximum SLD-vs-fidelity QFI relative difference | `0.322%` |
| Maximum HG cutoff change, order 8 to 12 | `5.1e-12` relative |

![Ideal information retained by accessible HG outcomes](../exoplanets/figures/spade_information_retention.png)

This supports the conceptual point: low-order SPADE retains a large fraction
of the separation information in the sub-Rayleigh regime, while full ideal
SPADE nearly saturates the source-state QFI. It does **not** validate the
current experiment's post-channel information. The hierarchical model
validates the experimental mean response, but its calibration field is a
nuisance process whose behavior during an unknown-source measurement protocol
must be specified before assigning a post-channel CFI. Information ratios
after the physical/count channel therefore remain sensitivity calculations,
not an experimental QFI.

The implemented ladder makes the accessible-mode distinction explicit. Across
nine representative corrected-convention settings:

| Information after channel | Fraction of source-state QFI |
| --- | ---: |
| Flagged HG0/HG1 accessible-state QFI | `0.99777--1.00000` |
| Resolved accessible-outcome CFI | `0.99681--1.00000` |
| Ideal binary HG1/not-HG1 CFI | `0.78434--0.99778` |
| Binary CFI after assumed `chi=0.0035` confusion | `0.00134--0.57026` |

The last range becomes very small near zero separation because a fixed
HG0-to-HG1 leakage baseline is locally insensitive to `d` and dilutes the
binary score. These are model calculations per surviving photon, not an
information estimate reconstructed from the recorded counts. The numerical
ordering provides a data-processing check: source QFI is no smaller than
flagged-channel QFI, which is no smaller than implemented measurement CFI.

The plausible-channel workbench repeats this calculation after its random
displacement, dephasing, coherent mixing, and modal-loss maps. Those results
are explicitly conditional on the JSON registry. Once independent channel
measurements replace the placeholders, the same calculation becomes a
calibrated QFI/CFI sensitivity statement.

## What additional data would make the inference identifiable

The highest-value additions are:

1. the original HG01 and HG10 streams separately, preserving acquisition
   order and timestamps;
2. simultaneous or interleaved HG00 counts so `n0 + n1` can normalize the
   first-order frequency as in the paper;
3. source-blocked detector counts and detector dead-time/afterpulse data;
4. single-mode injection measurements forming the relevant sorter cross-talk
   matrix, with uncertainties;
5. incident or detected photon-flux monitoring for every setting;
6. calibration uncertainty for `epsilon`, displacement, and `w0`;
7. higher-order outputs or, at minimum, a calibrated probability for the
   unobserved failure sector.

With these measurements, survival, sorter leakage, background, and detector
response can be constrained independently instead of being traded against one
another in a single aggregate count surface.

## Reproducibility

The corrected scripts are in `cqes/exoplanets`. The principal commands are:

```bash
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_calibration_analysis.py
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_eta_conditional_inference.py
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_quantum_channel_inference.py
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_channel_explorer.py
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_qfi_validation.py
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_hierarchical_channel.py \
  --output cqes/exoplanets/results/spade_hierarchical_channel.json --bootstrap 300
PYTHONPATH=. conda run -n space python -m cqes.exoplanets.spade_identifiable_quantum_channel \
  --bootstrap 1000 --full-restarts 2 --cv-restarts 0 \
  --output cqes/exoplanets/results/spade_identifiable_quantum_channel.json
PYTHONPATH=. conda run -n space python -m cqes.exoplanets.spade_plausible_channel_workbench \
  --registry cqes/exoplanets/spade_plausible_channels.example.json \
  --bootstrap 1000 --full-restarts 2 --cv-restarts 0 \
  --output cqes/exoplanets/results/spade_plausible_channel_workbench.json
PYTHONPATH=. conda run -n space python cqes/exoplanets/spade_generate_figures.py
```

The machine-readable plot summary is
[`spade_corrected_summary.json`](../exoplanets/results/spade_corrected_summary.json).
The full hierarchical fit and held-out predictions are in
[`spade_hierarchical_channel.json`](../exoplanets/results/spade_hierarchical_channel.json).
The identifiable sequential fit and information ladder are in
[`spade_identifiable_quantum_channel.json`](../exoplanets/results/spade_identifiable_quantum_channel.json).
The replaceable provisional-channel run is in
[`spade_plausible_channel_workbench.json`](../exoplanets/results/spade_plausible_channel_workbench.json).
The regression checks are in
[`test_spade_corrected_model.py`](../tests/test_spade_corrected_model.py).

## Final conclusion

The perspective change makes sense and should be kept. Thinking in terms of a
flagged accessible-mode channel, followed by calibrated readout and a discrete
count process, is the right way to connect SPADE measurements to QFI without
overclaiming.

The present data support three narrower conclusions: the corrected ideal model
confirms that low-order SPADE can retain substantial source information; the
aggregate measurements contain a separation-dependent first-order signal; and
a physics-informed hierarchical model predicts the 100-repeat setting means
well under grouped holdout tests. That is a validated practical **mean-response
channel**. The explicit sequential model sharpens it to a conditional
throughput `T = N_in eta = 1304.25` per 10 ms under the stated readout and
coupling convention. It is not a unique efficiency or an experimental QFI;
absolute eta requires independent launched flux and modal throughput.

The provisional workbench is the update path for the paper's authors. It can
already propagate plausible loss, jitter, coherent mixing, dephasing, and
readout phenomena, but it keeps every invented number visibly labelled. As
calibrations arrive, replacing those numbers—not silently refitting them from
the same aggregate count surface—will turn the framework from a diagnostic
sensitivity model into a defensible calibrated quantum-channel experiment.

The remaining weak point is now localized: simple one-parameter discrete
families do not reproduce all of the individual-count variance and tail
structure. I would use empirical repeat resampling for the current analysis
and prioritize separate HG01/HG10, HG00, flux, and background streams for the
next acquisition. Refining the rejected fixed-model `eta` would be much less
valuable than resolving those calibration and readout components.
