# SPADE Practical Channel and QFI Framework

## Purpose

This report describes a usable framework for analysing the available SPADE
data without claiming more than the measurements support. The practical goal
is not to extract a single, assumption-free detector efficiency or an
"experimental QFI" from the current file. The goal is to:

1. express the experiment as a sequence of physical and statistical channels;
2. use independent calibration values to fix selected channel components;
3. fit one or more remaining components to the actual repeated SPADE counts;
4. test whether that complete configuration could plausibly generate the data;
5. calculate the QFI and ideal-SPADE information for each configuration that
   remains compatible with the data.

This makes the work both scientifically cautious today and directly useful
when additional ASI calibration data become available.

## Executive Summary

The dataset is a `21 x 25 x 100` cube of repeated first-order SPADE counts,
where each datum is the aggregate `n1 = n_HG01 + n_HG10`. The scan ranges are
`d_a/w0 = -0.66667` to `0.66667` and `epsilon = 0.00427` to `0.09593`.

Three facts set the modelling requirements:

| Observation from the data | Value | Consequence for the model |
| --- | ---: | --- |
| Mean `n1` count | `6.93` to `19.44` | The first-order signal is small and sits on a sizeable baseline. |
| Median zero-distance count | `8.17` | A pure first-order ideal-SPADE model is inadequate; background and/or HG00 leakage is required. |
| Median Fano factor `Var(n1)/E[n1]` | `2.50` | Ideal Poisson noise (`F = 1`) is inadequate; use an overdispersed count-noise model. |
| Fano 5th to 95th percentile | `1.85` to `3.39` | The noise has setting-to-setting variation, so a single Fano factor is an approximation. |
| Largest signed-distance asymmetry | `3.84` counts | A small alignment/scan asymmetry may be present; signed scans should be retained. |

The central result is a constructive one. Under a fixed sequential channel
with `N_in = 40,000`, HG00-to-HG1 leakage `l0 = 0.002`, unit HG1
transmission, higher-sector leakage `ltail = 0.002`, and data-supported
Fano factor `F = 2.6`, the conditional fit gives:

| Conditional result | Value |
| --- | ---: |
| Photon survival MLE, `eta` | `0.10480` |
| `99.9%` profile interval | `[0.10408, 0.10553]` |
| Parametric-bootstrap p-value | `0.8060` |

This is not a universal measurement of `eta`. It says that this *complete
assumed configuration*, after fitting `eta`, generates count fluctuations and
mean patterns typical of the observed data. Changing a fixed calibration
constant changes the conditional eta estimate.

The corresponding ideal-Poisson test (`F = 1`) produces `eta = 0.11258` but
bootstrap `p = 0.00498`. It is rejected because the real repetitions fluctuate
much more than an ideal Poisson model predicts. This demonstrates why the
Fano noise channel must be explicit.

## What Was Actually Measured

The raw file is [H_data.npy](H_data.npy). It contains only one aggregate
measurement channel:

```text
H_data[d_index, epsilon_index, repetition] = n_HG01 + n_HG10
```

The following quantities are not present in the file:

- HG00 counts;
- separate HG01 and HG10 counts;
- higher-order modal counts;
- source-blocked dark/background counts;
- incident photons per acquisition;
- independent mode-injection measurements of sorter cross-talk;
- a detector/laser drift time series.

This is why the same observed `n1` baseline can arise from several mechanisms:
dark counts, HG00-to-HG1 leakage, incident flux, photon survival, and first
order transmission are partly degenerate. The framework keeps this limitation
visible instead of silently assigning all of the baseline to one mechanism.

## The Original Truncated-QFI Idea: Why It Was Attractive, and Why It Cannot Be Done From This Record

### The Idea

The original intuition was physically good. A displaced point-spread function
occupies an infinite Hermite-Gauss (HG) ladder, but in the sub-Rayleigh regime
the low HG orders carry the leading separation dependence. It is therefore
natural to ask whether a small number of accessible SPADE projections could
play the role of the important components of the infinite-dimensional spatial
state.

There are two possible meanings of "the two readings," and both are useful to
separate:

| Intended two-component object | What it would mean physically | What is actually stored |
| --- | --- | --- |
| `HG01` and `HG10` | Two orthogonal first-order SPADE outputs, spanning a two-dimensional first-order subspace | Only their sum `n1 = n_HG01 + n_HG10` is stored. |
| `HG00` and the aggregate first-order sector | A two-sector accessible subspace: reference mode plus the leading separation-sensitive sector | HG00 is not stored at all; only the aggregate first-order count is available. |

In either interpretation, the desired construction would be an
**accessible-mode reduction** of a spatial state. For a chosen projector
`P_acc`, for example onto HG00 and the first-order subspace, one would retain

```text
rho_acc(d, epsilon) = P_acc rho(d, epsilon) P_acc
```

and explicitly keep the complementary outcome `I - P_acc`. The success
probability of the accessible subspace is part of the experiment and cannot
be discarded. A complete physical description is therefore a measurement
instrument with both outcomes, not simply a normalized `2 x 2` matrix made
from two counts.

This would be scientifically interesting because it would quantify how much
of the ideal infinite-HG information remains in an experimentally accessible
low-mode subspace. It is closely related to the present comparison of
first-order SPADE CFI with the full-model QFI.

### What "Truncated QFI" Means in Projects 1, 7, and 9

[projects_1_7_9_report.md](../docs/projects_1_7_9_report.md) and
[classicalQFI.py](../qfi/classicalQFI.py) use "truncation" in a more specific
way. For a density-matrix pair `rho(theta)` and `rho(theta + delta)`, they
retain the `m` dominant **eigenvectors of `rho(theta)`**. With eigenvalue
crossing protection enabled, the same rank-`m` eigenspace projects the
displaced state before the finite-displacement fidelity/TQFI quantities are
calculated.

Those eigenvectors are the relevant "principal components": principal means
largest state eigenvalue, not largest count, and it does not mean a generic
PCA of measurement data. The key methodological rule from those projects is:
compare information quantities only for the same parameterized state family on
the same retained Hilbert space.

The following reductions must not be conflated:

| Reduction or truncation | Mathematical object retained | Meaning | Status for SPADE |
| --- | --- | --- | --- |
| Numerical HG cutoff | HG orders `0` through `N`, plus an unresolved tail | Controlled finite representation of an infinite optical state | Implemented with `N = 12`; convergence is checked. |
| Rank-`m` TQFI truncation | Top `m` eigenvectors of `rho(theta)` | Fidelity-based finite-displacement proxy on a selected state eigenspace | Used in the QFI projects; cannot be computed from `n1` alone. |
| Accessible HG projection | A specified physical mode projector such as `Pi_HG00 + Pi_HG1` | Information retained by a real low-mode measurement | A meaningful future SPADE experiment, but not reconstructible from this file. |
| Current record | One noisy aggregate count `n1` after the whole apparatus | A single classical observation channel | Supports likelihood/CFI modelling, not a reduced density matrix. |

The current `max_hg_order = 12` QFI calculation is therefore a **numerical
basis cutoff**, not a rank-two TQFI calculation. Conversely, the stored
first-order count is not a rank-one or rank-two quantum state.

### Why the Current Data Cannot Implement the Idea

To construct a data-derived two-mode or rank-`m` state, we would need, at a
minimum:

1. simultaneous HG00, HG01, HG10, and preferably higher-mode counts for every
   `(d_a, epsilon)` setting;
2. the total accepted-photon number or a calibrated per-trial normalization;
3. source-blocked background data and a calibrated readout-confusion matrix;
4. a definition of the accessible projector that is fixed independently of the
   parameter being estimated;
5. if the goal is a density matrix rather than a diagonal probability vector,
   phase-sensitive/tomographic information or a justified source-state model
   for the coherences.

The present file supplies none of items 1 to 3 in a form that resolves the
needed probabilities. It supplies only the final aggregate count `n1` after
loss, readout cross talk, background, and excess noise. Dividing `n1` by an
assumed photon number and defining `p0 = 1 - p1` would incorrectly absorb
vacuum, HG00 leakage, higher modes, dark counts, and missed photons into two
fictitious probabilities.

There is also a conceptual reason not to call the current SPADE ports
principal components: HG modes are a measurement basis chosen by the sorter.
They are not generally the eigenvectors of the mixed source state
`rho(d, epsilon)`. The two first-order ports are physically important
projections, but they are not automatically the two dominant eigenvectors
required by the rank-`m` TQFI construction.

### What We Need From ASI to Make the Accessible-Mode Protocol Work

ASI can turn the present model-based comparison into an experimentally
calibrated accessible-mode protocol. The required data separate into a
minimum set for a defensible multi-mode count/CFI experiment and an enhanced
set for a state-level or TQFI-style analysis.

| ASI data product | Why it is needed | Minimum use in the protocol | Needed for data-derived state/TQFI? |
| --- | --- | --- | --- |
| Raw counts for every measured mode at every setting | Gives the observed modal outcome vector, for example `n_00, n_01, n_10, ..., n_m` | Yes | Yes |
| Accepted trials, triggers, or independently calibrated incident photons per setting | Converts counts into probabilities and accounts for no-click events | Yes | Yes |
| A recorded complement outcome | Counts outside the selected mode set, including higher modes and no-click/loss | Yes | Yes |
| Source-blocked counts for every output channel | Separates dark/background counts from optical modal signal | Yes | Yes |
| Mode-injection calibration matrix | Measures `P(reported j | injected k)`, including loss and cross talk between all selected modes | Yes | Yes |
| Detector characterization | Exposure, gating, efficiency, dead time, saturation, afterpulsing, and time stamps | Yes | Yes |
| Repetition/drift metadata | Supports a realistic covariance, Fano, or time-correlation noise model | Yes | Yes |
| Source calibration | Actual `epsilon`, signed displacement, PSF widths, axis orientation, and acquisition stability | Yes | Yes |
| Coherence/tomography measurement or a validated coherence model | Determines off-diagonal density-matrix elements in the HG basis | No, a CFI analysis can use modal probabilities | Yes |
| Independent alignment reference | Separates source displacement from sorter displacement | Strongly recommended | Strongly recommended |

The smallest operational data record for each setting should look like:

```text
setting metadata:
  true signed displacement, epsilon, PSF/alignment settings, time stamp

per acquisition or binned block:
  trigger/accepted-photon count
  n_HG00, n_HG01, n_HG10, n_HG11, ..., n_selected
  n_complement_or_no_click
  detector flags and exposure/gating metadata

calibration runs:
  source blocked for each detector output
  inject each selected HG input mode and record every output
```

With this information, ASI does **not** need to reconstruct an arbitrary
infinite-dimensional state to make the practical protocol work. The immediate
experiment can estimate calibrated modal probabilities, fit a physical
channel, calculate the CFI of the actual measured POVM, and compare that CFI
with a clearly stated model QFI. Coherence-sensitive measurements become
necessary only for a data-derived density matrix or a data-derived TQFI.

### Can the Infinite HG System Be the Starting System, With Modes Through m as the Truncation?

**Yes, in principle, with an important change of language.** The spatial
single-photon Hilbert space is naturally an infinite HG system,

```text
H_spatial = span{|HG00>, |HG01>, |HG10>, |HG11>, ...},
```

with an additional vacuum sector when photon loss is modelled. Measuring a
finite set of modes is then a physically meaningful **accessible-mode
projection**, for example

```text
P_M = sum_(j in M) |HG_j><HG_j|,
M = {HG00, HG01, HG10, HG11, ... up to a declared modal order}.
```

The required measurement is not only `P_M`. It must include the complement
`I - P_M`, so the complete POVM is

```text
{Pi_HG00, Pi_HG01, Pi_HG10, ..., Pi_HGm, I - P_M}.
```

The complement carries the probability of higher modes, loss, and any
unmeasured outcome. Omitting it or normalizing only the selected counts
postselects the data and can discard separation information.

This is a good truncation **when it is described as a fixed HG measurement
subspace**, because:

1. HG modes are the actual optical projections implemented by SPADE;
2. near zero separation, low total HG order is physically motivated because
   higher-order populations enter at higher powers of displacement;
3. increasing the selected mode set gives a controlled experimental
   convergence test: compare the CFI for `{00}`, `{00, 01, 10}`, then all
   modes up to total order `m`;
4. a fixed, parameter-independent projector is a well-defined measurement
   protocol across the full scan.

It is **not** automatically a rank-`m` TQFI or a principal-component
truncation, because:

1. the selected HG modes are chosen by the measurement basis and modal order,
   not by the largest eigenvalues of `rho(d_a, epsilon)`;
2. the dominant eigenvectors of the source state can be superpositions of HG
   modes and can change with separation and source ratio;
3. counts in fixed HG modes determine diagonal probabilities only. They do not
   determine off-diagonal coherences needed for a general data-derived QFI;
4. in two dimensions, "up to m" must be defined explicitly. A natural choice
   is all modes with total order `q_x + q_y <= m`, which contains degenerate
   groups such as `HG10` and `HG01`; it is not a single ordered list of
   principal components.

The correct hierarchy of claims is:

| Available information | Valid analysis |
| --- | --- |
| Counts in every selected HG mode plus complement, calibrated readout, and total trials | Experimental modal-probability model and CFI of the real multi-outcome SPADE POVM |
| The above plus a validated physical source/channel model | Model QFI, ideal-SPADE CFI, and actual calibrated-POVM CFI can be compared |
| The above plus coherence-sensitive tomography or an independently justified density model | A reduced/accessibly projected density matrix can be constructed and its SLD QFI studied |
| Full state pair plus a fixed rank-`m` state eigenspace | The finite-displacement rank-`m` TQFI procedure used in the QFI projects |

So the experimental answer is: **measure the first HG modes because they are
the physically accessible low-order SPADE subspace, not because they are
automatically principal components.** Use their multi-outcome CFI as the
direct experimental information quantity. Use TQFI only if the state pair and
its retained eigenspace are actually available or justified.


### What We Can Say Instead

The present framework does the defensible version of the original idea:

```text
infinite HG source model
  -> numerically converged finite HG representation
  -> ideal full-SPADE CFI
  -> ideal first-order CFI
  -> imperfect recorded-n1 CFI
```

This tells us, conditionally on the model, how much information low-order
SPADE projections could retain and how much the real readout/noise chain
removes. It does not claim a data-derived two-component state or a
data-derived truncated QFI.

## Diagram-Ready Quantum Process Description

The channel model should be drawn as a sequence of quantum wires until the
measurement, followed by classical wires. This is the correct separation for
a diagram in the style of *Picturing Quantum Processes*.

```text
theta = (d_a, epsilon)
        |
        v
 [Source preparation] -- S --> [Loss] -- S,V --> [Sorter alignment] -- S,V --> [HG dephasing] -- S,V --> [SPADE POVM] -- Y --> [Count noise] --> n1
        rho_S(theta)             E_loss                 U_align                  E_phi                 M_Y              C_dark,F
                                      |                                            |
                                      v                                            v
                                   environment E_L                            environment E_phi

QFI checkpoints:
F_Q[rho_S]  >=  F_Q[E_loss(rho_S)]  =  F_Q[U_align E_loss(rho_S)]  >=  F_Q[E_phi U_align E_loss(rho_S)]
                                                                                     >=  F_CFI(Y) per launched photon

The final F_CFI(n1) is per acquisition after N_in trials and classical count noise.
Compare it with N_in F_Q only under the stated photon-number and noise assumptions.
```

`S` is the truncated spatial HG system; `V` is the vacuum sector introduced
by loss; and the two readout versions are:

```text
current record:   Y = {reported first-order, other} -> aggregate count n1
future protocol:  Y = {HG00, HG01, HG10, ..., HGm, complement} -> modal count vector n
```

The two environments need not be drawn when a compact diagram is needed, but
including them makes clear which operations are genuine open-system channels.

### Drawing Blocks and Their Meaning

| Draw this box | Mathematical map | Type | What enters the box | What exits the box | Where its parameters belong |
| --- | --- | --- | --- | --- | --- |
| Source preparation | `(d_a, epsilon) -> rho_S(d_a, epsilon)` | Parameter encoding, not noise | Separation, source ratio, PSF calibration | Spatial single-photon HG state | Source model and external calibration |
| Photon loss | `E_loss(rho) = sum_j K_j rho K_j^dagger` | CPTP quantum channel | `rho_S`, survival `eta` | Spatial state plus vacuum population | Eta may be fitted conditionally |
| Sorter alignment | `rho -> U_align rho U_align^dagger` | Parameter-independent unitary channel | Fixed sorter-axis displacement | Rotated spatial state | Profile only with an independent source reference |
| HG dephasing | `rho -> v rho + (1-v) diag_HG(rho)` | CPTP quantum channel | Coherence visibility `v` | Mixed spatial state | QFI sensitivity parameter; not identifiable from `n1` |
| Imperfect SPADE readout | `p(y|theta) = Tr[M_y rho]` | Quantum measurement / instrument | State and POVM confusion probabilities `l0`, `l1`, `ltail` | Classical outcome `Y` | Mode-injection calibration; not a state channel |
| Background and count noise | `Y -> n1` with `lambda1` and `Var(n1)=F lambda1` | Classical stochastic channel | Dark rate, input trials, Fano factor | Repeated count | Measured repetitions and detector/source calibration |

### Exact Labels for the Diagram

Use the following labels rather than a generic box called "noise":

```text
[Source encoding rho_S(d_a, epsilon)]
      -> [Erasure/loss E_loss, eta]
      -> [Static HG displacement U_align, delta_sorter]
      -> [HG dephasing E_phi, visibility]
      -> [Imperfect SPADE instrument M_Y, l0/l1/ltail]
      -> [Classical background + overdispersion C_dark,F]
      -> [Recorded aggregate count n1 = n_HG01 + n_HG10]
```

Important caption rules:

- Draw the loss and dephasing boxes as quantum processes with an optional
  environment wire.
- Draw sorter alignment as a unitary box: it does not reduce QFI by itself
  when it is parameter independent, but it can reduce the CFI of a fixed
  downstream SPADE measurement.
- Draw cross talk as part of the SPADE measurement box, not automatically as a
  quantum channel. It changes how modal occupancy is reported.
- Draw dark counts and Fano fluctuations after the measurement on a classical
  wire. They reduce count likelihood/CFI, not the pre-measurement state QFI.
- Mark the point immediately before the POVM as the post-quantum-channel QFI
  checkpoint. Mark the POVM output and final count as CFI checkpoints.
- Label the ideal POVM CFI "per launched photon" and the final noisy count CFI
  "per acquisition"; only a conditionally normalized comparison is valid.

### Which Quantities the Present Data Can Fit or Test

```text
Fixed channel assumptions + one fitted parameter
                   |
                   v
model count distribution for every (d_a, epsilon)
                   |
                   v
likelihood of all 52,500 recorded n1 values
                   |
                   v
conditional MLE, profile interval, bootstrap p-value
                   |
                   +--> QFI/CFI comparison for that accepted configuration
```

The fit tests whether the final classical record could have been generated by
the entire drawn process. It does not tomographically reconstruct the quantum
wire between boxes. That is exactly why all quantum-channel constants and all
classical count-noise constants must be stated next to the diagram.


## The Model in One Diagram

```text
Known controls                Quantum/source model                         Optical readout                 Recorded data

(d_a, epsilon)      -->      rho(d_a, epsilon; offset, width, coherence)  -->  SPADE confusion matrix  -->  n1 repetitions
                                      |                                           l0, l1, ltail                   |
                                      | HG-sector probabilities                                                   | noise model
                                      v                                                                               v
                               p0, p1, p_tail                                               lambda1       Var(n1) = F lambda1
                                      |                                                       |
                                      v                                                       v
                               photon survival eta                         dark + N_in eta (l0 p0 + l1 p1 + ltail p_tail)

Separate QFI branch:
rho(d_a, epsilon; eta, width, offset, coherence) --> F_Q
                                                     --> ideal full-SPADE CFI
                                                     --> ideal first-order SPADE CFI
```

The first line describes how the state depends on the scan coordinate. The
middle line describes the measured count channel. The final branch is the QFI
calculation. It uses the assumed quantum state before the noisy detector
readout and is not fitted directly from count variance.

## The Source Model and HG Truncation

For a source-ratio parameter `epsilon`, the source state is represented as

```text
rho = (1 - epsilon_eff) |HG00><HG00| + epsilon_eff |u_d><u_d|
```

where `|u_d>` is a displaced Gaussian point-spread function. The effective
scan parameters are

```text
d_eff       = (d_a - displacement_offset) / psf_width_scale
epsilon_eff = epsilon ** epsilon_power
mu          = d_eff**2 / 16
```

The probabilities that enter the count model are grouped into three sectors:

```text
p0     = 1 - epsilon_eff + epsilon_eff exp(-mu)
p1     = epsilon_eff mu exp(-mu)
p_tail = 1 - p0 - p1
```

Here `p1` represents the total first-order HG sector used by the current
measurement. `p_tail` represents all higher orders that are not directly
resolved in this record.

This sector grouping does **not** mean that the QFI calculation is a two-mode
model. In [spade_qfi_validation.py](spade_qfi_validation.py), the quantum
state is truncated at HG order 12, with a loss/vacuum sector where appropriate.
The truncation test shows numerical convergence by order 8 to 12 for the
representative cases. The data themselves still record only the aggregate
first-order outcome.

## Separate, Tunable Channels

The physically interpretable sequential mean-count model is

```text
lambda1 = dark + N_in eta (l0 p0 + l1 p1 + ltail p_tail)
```

where `lambda1` is the predicted mean observed first-order count for one
acquisition.

| Channel or component | Symbol | Function in the model | Data status now | What would calibrate it directly? |
| --- | --- | --- | --- | --- |
| Input brightness | `N_in` | Incident photons per acquisition | Must be fixed in a conditional eta fit | Source/trigger power calibration |
| Photon survival/loss | `eta` | Multiplies probabilities arriving at the detector | Fittable only conditional on other scale constants | Calibrated source flux plus optical/detector efficiency |
| Dark/background | `dark` | Additive counts | Degenerate with leakage in `n1` alone | Source-blocked acquisition |
| HG00-to-HG1 leakage | `l0` | Baseline caused by mode confusion | Must be assumed or calibrated | Inject HG00 and read HG1 channel |
| HG1 transmission | `l1` | Desired first-order response | Degenerate with `N_in eta` | Inject HG01/HG10 separately |
| Higher-to-HG1 leakage | `ltail` | Tail contamination of first-order record | Weakly constrained in this range | Higher-mode injection or additional modal outputs |
| Scan offset | `d0` | Shifts `d_eff` | Weakly fit from signed scans | Alignment reference measurement |
| PSF width | `w_scale` | Rescales separation | Broad fits can hit a bound | Independent PSF calibration |
| Epsilon calibration | `epsilon_power` | Maps nominal to effective source ratio | Can be explored but correlated with gain | Source-ratio calibration |
| Count noise | `F` | Sets `Var(n1) = F lambda1` | Identifiable from repetitions, approximately | Detector/source drift characterization |
| Coherence/dephasing | `visibility` | Suppresses off-diagonals of `rho` | Not identifiable from `n1` alone | Interferometric/state calibration or extra modes |

### Effective Explorer Parameterization

Because the current data cannot separately identify all physical components,
the modular explorer also supports the effective form

```text
lambda1 = B + A1 p1 + A_tail p_tail
```

with

```text
B      = dark + N_in eta l0             (approximately, at small separation)
A1     = N_in eta (l1 - l0)
A_tail = N_in eta (ltail - l0)
```

This is an honest data-facing parameterization. `B`, `A1`, and `A_tail` are
fit combinations; they must not be renamed as unique dark counts, leakage, or
efficiency without external information.

## Quantum-Channel Implementation: Completed Steps

The effective model remains useful for quick diagnosis, but it is now paired
with a physical quantum-channel implementation in
[spade_quantum_channel_inference.py](spade_quantum_channel_inference.py). It
uses the same truncated HG state and scan convention as the validated QFI
module, then composes the following maps in order:

```text
rho_source(d, epsilon)
  -> E_loss(eta)
  -> U_sorter(mode_sorter_displacement)
  -> E_dephase(visibility)
  -> imperfect SPADE POVM
  -> dark counts and Fano count noise
```

This deliberately separates quantum-state evolution from readout and detector
effects. Not every experimental imperfection should be forced into a quantum
channel: cross talk at the mode sorter is most naturally a measurement error,
and dark counts or overdispersion occur after the optical state has been
measured.

### Step 1: Physical State in a Truncated HG Basis

The implementation represents the source in the basis

```text
|vac>, |unresolved higher-order tail>, |HG00>, |HG1>, ..., |HG_N>
```

with `N = 12` by default. The tail basis state preserves trace under HG
truncation. It is an unresolved higher-order outcome, not a claim that all
higher orders are one physical mode.

This remains an effective one-axis HG ladder aligned with the scanned
displacement. The physical record is the aggregate `HG01 + HG10`; it does not
contain the two first-order modes separately. Therefore this implementation
does not claim a full two-dimensional modal state reconstruction. A future
two-dimensional channel model requires separate modal outputs or a calibrated
mapping from the two-dimensional sorter to the aggregate record.

### Step 2: Photon Loss as a Kraus Erasure Channel

Photon survival is represented by a completely positive trace-preserving
(CPTP) erasure channel. The retained-photon Kraus operator has amplitude
`sqrt(eta)` in every non-vacuum sector; a complementary set maps each photon
sector to `|vac>`. This produces the standard state

```text
rho_loss = eta rho_source + (1 - eta) |vac><vac|
```

for the vacuum-free source state used here. This is the correct place for eta
when eta means survival/detection of a launched photon.

### Step 3: Static Mode-Sorter Misalignment as a Unitary Channel

`mode_sorter_displacement` applies a parameter-independent HG displacement
unitary before the SPADE measurement. Physically, it describes a fixed
reference-axis offset between the optical field and the sorter. It is distinct
from `source_displacement_offset`, although the aggregate `n1` data will tend
to correlate the two. They should not be freely fitted together without an
alignment calibration.

### Step 4: HG-Basis Dephasing as a CPTP Channel

The dephasing channel is

```text
E_dephase(rho) = visibility rho + (1 - visibility) diag_HG(rho).
```

It suppresses coherences in the selected HG basis without changing diagonal
modal probabilities. The parameter is therefore a valid QFI sensitivity axis
but is not identifiable from an aggregate diagonal SPADE count alone.

### Step 5: Cross Talk as an Imperfect SPADE POVM

The recorded first-order event is described by a positive measurement operator

```text
M1 = l0 Pi_HG00 + l1 Pi_HG1 + ltail Pi_higher,
M_other = I - M1.
```

The predicted recorded probability is `Tr(M1 rho)`. This is more faithful than
calling sorter confusion a state channel: it represents how a physical modal
occupancy is reported by the measurement apparatus. With all `l` values in
`[0, 1]`, this is a valid binary POVM.

### Step 6: Classical Detector and Count-Noise Channel

The detector layer produces the observed mean and variance:

```text
lambda1 = dark + N_in Tr(M1 rho_loss)
Var(n1) = F lambda1.
```

Dark counts and Fano overdispersion change the likelihood and observed count
CFI. They do not alter the QFI of the optical state `rho_loss`.

### Channel Validation and Current Quantum Results

The quantum implementation has three important internal checks:

| Check | Result | Meaning |
| --- | ---: | --- |
| Loss-channel trace error | `2.22e-16` | The Kraus implementation preserves trace to machine precision. |
| Minimum density-matrix eigenvalue | `-5.12e-27` | Numerical zero; the propagated state is positive within floating-point precision. |
| Quantum-to-sector reduction error | `0.0` | With identity misalignment/dephasing, the new POVM exactly reproduces `l0 p0 + l1 p1 + ltail p_tail`. |

Consequently, the quantum model with the reference assumptions in
[spade_quantum_channel_assumptions.example.json](spade_quantum_channel_assumptions.example.json)
reproduces the previous conditional result:

| Quantity | Quantum-channel result |
| --- | ---: |
| Conditional photon-survival MLE | `0.10480` |
| `99.9%` profile interval | `[0.10408, 0.10553]` |
| Bootstrap p-value, 200 simulations | `0.8060` |

This agreement is a validation of the implementation, not a second independent
measurement. The extra channels are identity maps in this reference scenario.

The new information comparison is more revealing. Over the measured nonzero
grid for this same accepted scenario:

| Information quantity | Range | Interpretation |
| --- | ---: | --- |
| Post-channel QFI per launched photon | `1.09e-4` to `2.51e-3` | Information after the eta loss channel in the assumed state model. |
| Full ideal-SPADE CFI / QFI | `0.999934` to `1.000000` | Resolving the full retained HG basis remains nearly QFI-optimal. |
| Imperfect binary-readout CFI / QFI | `5.90e-4` to `0.53062` | HG00 leakage and first-order-only readout can discard substantial information. |
| Classical count CFI / (`N_in` QFI) | `2.62e-4` to `0.21778` | Additional loss from finite input scale, dark/readout effects, and Fano count noise. |

The low imperfect-readout fractions do not contradict the earlier ideal
first-order result of about `94.5%` to `98.6%`. The earlier result assumes a
perfect first-order projector. The new result includes the assumed `l0 =
0.002` leakage, which introduces a large HG00-derived baseline relative to the
small first-order signal and therefore reduces the information in the binary
recorded event.

### What the First Quantum Profiles Show

The module provides `profile_quantum_channel_parameter()` to scan one named
channel parameter while refitting eta and holding every other component fixed.
The first profiles demonstrate the intended use:

| Conditional profile | Count-likelihood result | QFI implication |
| --- | --- | --- |
| HG dephasing visibility `0`, `0.5`, `1` | Exactly flat likelihood and identical eta `0.10480` | The aggregate `n1` record cannot identify dephasing; at the reference setting the model QFI changes only from `0.00245187` to `0.00245203`. |
| Sorter displacement from `-0.04` to `0.04` with source offset fixed | Minimum occurs near zero; delta NLL is `15.1` at `-0.02` and `66.6` at `+0.02` | The data are sensitive to a fixed measurement-axis displacement only conditionally on the source reference. |

These are not final instrument calibrations. In particular, a free source
offset can trade off against a free sorter displacement. They show why the
quantum model must retain named channels and why each fit needs explicit
calibration constraints.

Run the quantum version with:

```bash
conda run -n space python -m cqes.exoplanets.spade_quantum_channel_inference \
  --assumptions cqes/exoplanets/spade_quantum_channel_assumptions.example.json \
  --bootstrap 1000 \
  --confidence 0.999 \
  --output /tmp/spade_quantum_channel_results.json
```

## What Is Fitted, What Is Fixed, and What Is Tested

| Analysis layer | Free quantities | Fixed quantities | Uses the real repeated data? | Main output |
| --- | --- | --- | --- | --- |
| Raw diagnostic | None | None | Yes | Baseline, symmetry, empirical variance, Fano factor |
| Paper-style calibration | Curve offsets/slopes or equivalent `chi`, `c` | Trial photon-number reference | Yes, setting means and SEM | Checks phenomenological quadratic/linear response |
| Effective channel fitting | `B`, `A1`, optional tail, geometry, `F` according to scenario | Parameters excluded from scenario | Yes, all 52,500 counts | Likelihood, AIC/BIC, profile likelihood, residual maps |
| Conditional eta inference | `eta` only | `N_in`, leakage, transmission, background, geometry, `F`, coherence | Yes, all 52,500 counts | Conditional MLE, profile interval, bootstrap p-value |
| Conditional quantum-channel inference | `eta` plus one explicitly profiled quantum channel, if justified | Remaining source, loss, POVM, and count-noise components | Yes, all 52,500 counts | Channel profile, conditional eta, bootstrap p-value, post-channel QFI/CFI maps |
| QFI sensitivity/design scan | None directly from `n1` | A chosen physical state/channel configuration | Optional overlay of data range | QFI and ideal-SPADE information fractions |

The practical logic is: **fix what ASI or an independent calibration knows;
fit what the present data can identify; then bootstrap the full configuration.**
The p-value asks whether data simulated from the fitted configuration have a
discrepancy at least as large as the real data. It does not prove that the
configuration is unique or physically true.

## Results from the Existing Analyses

### 1. Raw Data Diagnostics

[spade_analysis.py](spade_analysis.py) confirms that the naive ideal HG1
response with only one scale is not a usable data model. Its `R^2` is negative
(`-7.10`) because it predicts zero first-order count at zero separation while
the observed baseline is about eight counts.

The first-order count variance lies well above the mean at every setting. The
empirical median Fano factor is `2.497`, so the working likelihood uses

```text
n1 approximately Normal(lambda1, F lambda1)
```

for the present repeated-count regime. This quasi-Gaussian distribution is an
explicit approximation, not a claim of fundamental Gaussian photon counting.

### 2. Paper-Style Calibration and Physical Reparameterization

[spade_calibration_analysis.py](spade_calibration_analysis.py) compares

```text
n1 = a + b d_a**2
n1 = chi eta_n + c epsilon d_a**2
```

for each epsilon curve. The two forms are algebraically equivalent when both
parameters are free. The useful question is whether `chi` and `c` remain
consistent across curves and in a pooled fit.

For reference `eta_n = 40,000`, the pooled physical fit gives:

| Pooled quantity | Result |
| --- | ---: |
| Baseline `chi eta_n` | `8.297` counts |
| `chi` | `2.074e-4` |
| Response `c` | `272.83` |
| Pooled `R^2` | `0.8850` |
| Relative across-curve standard deviation of `chi` | `4.4%` |
| Relative across-curve standard deviation of `c` | `52.6%` |

Thus the baseline-like term is comparatively stable, while the response term
is not constant across all epsilon curves. This is useful evidence for the
need to explore epsilon calibration, geometry, readout effects, or unmodelled
noise. It is not evidence that `chi` alone has been uniquely measured.

### 3. Effective First-Order Channel Fits

[spade_channel_fitting.py](spade_channel_fitting.py) fits setting means with
empirical SEM weighting. The following results rank mean models only; their
weighted-Gaussian AIC/BIC values do not replace the full repeated-count noise
likelihood.

| Model | Main fitted additions | `R^2` | Delta AIC | Delta BIC | Interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| Ideal scaled HG1 | Scale only | `-7.1845` | `105612.3` | `105599.5` | Fails because the baseline is absent. |
| Affine readout | Baseline + HG1 contrast | `0.8858` | `80.0` | `71.4` | Establishes an approximately `8.18` count baseline. |
| Misaligned affine | Plus offset | `0.8863` | `71.7` | `67.5` | Only a small improvement. |
| Epsilon-power readout | Plus epsilon power | `0.8899` | `6.0` | `1.7` | Most of the mean-model improvement comes from epsilon response flexibility. |
| Misaligned epsilon-power | Plus offset and epsilon power | `0.8904` | `0.0` | `0.0` | Best of these mean models, but only marginally better by BIC than epsilon power alone. |

The best model has baseline `8.282` counts, HG1 scale `7716`, offset
`0.0073`, and epsilon power `1.201`. These are useful effective descriptors,
not unique optical calibrations.

### 4. Higher-Order Tail Sensitivity

[spade_physical_channel.py](spade_physical_channel.py) tests whether adding an
effective higher-order readout term can improve the mean fit.

| Effective model | `R^2` | AIC | Key result |
| --- | ---: | ---: | --- |
| Baseline plus HG1 | `0.8858` | `1301.2` | `B = 8.176`, `A1 = 4548.6` |
| Plus higher-order tail | `0.9127` | `1036.8` | Fit requires `A_tail = -221290`, which is not a physical positive leakage probability |

The tail model is a useful warning and sensitivity test, not a final channel
measurement: the negative contrast says that a freely flexible tail term is
absorbing structure the simple model cannot otherwise represent. Future fits
must impose physically calibrated bounds on `ltail` rather than interpret the
unconstrained negative coefficient literally.

### 5. Modular Repeated-Count Explorer

[spade_channel_explorer.py](spade_channel_explorer.py) fits all `52,500`
individual counts with a setting-dependent quasi-Gaussian likelihood. It is
the right tool for exploring constrained scenarios and profile scans.

| Scenario | Main freedom | Fitted Fano | Mean `R^2` | Important diagnostic |
| --- | --- | ---: | ---: | --- |
| `affine_readout` | Baseline, HG1 contrast, `F` | `2.587` | `0.8861` | Simple reference model |
| `source_calibration` | Plus offset, PSF scale, epsilon power | `2.582` | `0.8942` | PSF scale reaches its lower bound `0.6` |
| `tail_readout` | Plus tail contrast | `2.702` | `0.9056` | Tail contrast is negative and PSF scale is `0.709` |

The apparent BIC preference for the flexible tail scenario does not establish
the physical tail channel. Bound-hitting geometry and negative tail response
mean the unconstrained model is diagnosing missing calibration information.
The next use of this explorer should therefore be a profile likelihood with
ASI-supplied bounds or fixed values, not a broader unconstrained search.

### 6. Conditional Eta Fit and Configuration Test

[spade_eta_conditional_inference.py](spade_eta_conditional_inference.py) is
the clearest implementation of the intended use case: all channel components
except one are stated explicitly, and `eta` is fitted to the real data.

For this reference scenario:

```json
{
  "input_photons_per_acquisition": 40000,
  "dark_background_counts": 0.0,
  "hg00_to_hg1_leakage": 0.002,
  "hg1_to_hg1_transmission": 1.0,
  "higher_to_hg1_leakage": 0.002,
  "displacement_offset": 0.0,
  "psf_width_scale": 1.0,
  "epsilon_power": 1.0,
  "fano_factor": 2.6,
  "coherence_visibility": 1.0,
  "max_hg_order": 12
}
```

the fitted survival is `eta = 0.10480` with `99.9%` conditional profile
interval `[0.10408, 0.10553]`. The refitted Pearson statistic of the data is
`52171.9`, compared with bootstrap median `52440.2`, giving `p = 0.8060` in
200 parametric simulations.

The narrow interval measures statistical precision **conditional on every
listed assumption**. It does not include systematic uncertainty in `N_in`,
leakage, background, PSF scale, or epsilon calibration. A defensible final
eta result should report an envelope across independently justified channel
scenarios, not only one conditional interval.

For exactly the same optical assumptions but `F = 1`, the observed statistic
is `128880.9` while the bootstrap median is `52441.5`; `p = 0.00498` with
200 simulations. The value is at the finite-bootstrap resolution floor because
no simulated ideal-Poisson dataset is as discrepant as the real data. This
rejects the ideal-Poisson count-noise assumption, not eta by itself.

## QFI: What It Adds and What It Does Not

### The Legitimate Role of QFI Here

For any specified source/channel state `rho(d_a)`, the QFI is

```text
F_Q = QFI of rho with respect to d_a.
```

It is a theoretical per-photon information limit for the chosen model. It
answers: *if this physical configuration were correct, what is the maximum
information any measurement could extract about separation?*

It is not obtained by inserting the observed empirical variance into a QFI
formula. The dataset lacks the modal probabilities and photon normalization
required to reconstruct an experimental density matrix. The count record can
only validate or reject **assumed channel configurations** through likelihood
and bootstrap tests.

### QFI Validation Results

[spade_qfi_validation.py](spade_qfi_validation.py) uses QuTiP to calculate the
SLD QFI from the truncated density matrix and independently checks it with a
finite-fidelity calculation. At 12 regular representative points:

| Validation comparison | Result |
| --- | ---: |
| Largest SLD vs fidelity relative difference | `0.126%` |
| Full ideal-SPADE CFI / QFI | `0.999934` to `1.000000` |
| First-order ideal-SPADE CFI / QFI | `0.94479` to `0.98614` |

This establishes that, for the ideal truncated source model in the tested
sub-Rayleigh range:

1. the numerical QFI calculation is stable;
2. resolving the retained full HG basis is effectively QFI-optimal;
3. restricting an ideal measurement to the first-order SPADE sector retains
   about `94.5%` to `98.6%` of model QFI at the representative points.

At exactly `d_a = 0`, the model changes rank. The derivative SLD QFI and
finite-fidelity limit are non-regular there, so the code reports the point
separately rather than treating their mismatch as a software failure. Figures
and conclusions should focus on nonzero separation or explicitly annotate
this non-regular point.

### Where the Noisy Channel Meets QFI

For a configuration accepted by the count bootstrap, the code can produce:

| Quantity | Interpretation | Appropriate claim |
| --- | --- | --- |
| Post-loss `F_Q` per launched photon | Fundamental limit for the assumed post-loss quantum state | The model limit |
| Full ideal-SPADE CFI / `F_Q` | Information retained by a complete ideal HG measurement | Measurement-design efficiency |
| First-order ideal-SPADE CFI / `F_Q` | Information retained if only first order is used ideally | Value of adding higher modes |
| Effective count CFI | Information of the fitted noisy `n1` likelihood | A model diagnostic, not measured QFI |
| Effective count CFI divided by `N_in F_Q` | Conditional comparison after photon normalization | Only valid under all stated calibration assumptions |

The most informative QFI plots are therefore not nearly parallel curves over
only the measured distance range. They should show `first-order CFI / QFI` and
`full-SPADE CFI / QFI` over a wider separation range, with the experimental
range shaded. This shows where first-order-only SPADE is sufficient and where
higher modes become valuable. It is a design decision supported by the model,
not an overclaim about the present data.

## Recommended Practical Workflow

### A. Diagnose the Data First

1. Run `spade_analysis.py` and inspect baseline, signed-distance symmetry,
   variance-versus-mean, and Fano maps.
2. Do not assume `F = 1` if repeated-count data reject it.
3. Treat a nonzero `d_a = 0` count as background/leakage evidence, not as an
   ideal first-order signal.

### B. Use Effective Models to Discover Missing Physics

1. Run the named scenarios in `spade_channel_explorer.py`.
2. Use bounded profile likelihood scans, never only a frozen grid score.
3. Interpret bound-hitting and negative effective tail terms as missing
   calibration constraints, not as direct optical measurements.

### C. Turn ASI Information Into a Conditional Physical Fit

1. Copy [spade_eta_assumptions.example.json](spade_eta_assumptions.example.json).
2. Replace speculative values with independently measured `N_in`, source-blocked
   background, mode-injection leakage/transmission, PSF scale, and noise model.
3. Fix these values in the JSON and fit only eta, or a small explicitly stated
   subset of identifiable parameters.
4. Run a sufficiently large parametric bootstrap, normally at least several
   hundred simulations. A p-value is estimated with Monte Carlo uncertainty.

For a quantum-channel fit, use the quantum assumptions schema and retain the
channel order in the archived result:

```bash
conda run -n space python -m cqes.exoplanets.spade_quantum_channel_inference \
  --assumptions cqes/exoplanets/spade_quantum_channel_assumptions.example.json \
  --bootstrap 1000 \
  --confidence 0.999 \
  --output /tmp/spade_quantum_channel_results.json
```

Example:

```bash
conda run -n space python -m cqes.exoplanets.spade_eta_conditional_inference \\
  --assumptions cqes/exoplanets/my_asi_calibrated_assumptions.json \\
  --bootstrap 1000 \\
  --confidence 0.999 \\
  --output /tmp/spade_eta_results.json
```

### D. Use QFI as Validation and Design, Not as a Count Fit

1. For every channel scenario with an acceptable bootstrap result, compute
   QFI, full-SPADE CFI, and first-order CFI.
2. Check that full ideal-SPADE CFI remains below or equal to QFI, as it does in
   the validation script.
3. Report both the ideal `first-order CFI / QFI` and the imperfect-POVM
   `binary-readout CFI / QFI` to distinguish fundamental mode restriction from
   measured sorter cross talk.
4. Compare eta scenarios only after stating their input-photon and readout
   calibration assumptions.

## Existing Files and How to Use Them

| File | Role |
| --- | --- |
| [SPADE_visual_analysis.ipynb](notebooks/SPADE_visual_analysis.ipynb) | First entry point for raw count, baseline, symmetry, and noise plots. |
| [spade_analysis.py](spade_analysis.py) | Script version of raw data diagnostics. |
| [spade_calibration_analysis.py](spade_calibration_analysis.py) | Paper-style distance and epsilon calibrations with the offset-aware physical reparameterization. |
| [spade_channel_fitting.py](spade_channel_fitting.py) | Mean-model comparison and an explicit QFI ambiguity demonstration. |
| [spade_physical_channel.py](spade_physical_channel.py) | Maps effective fit parameters onto physical channel combinations and lists missing calibrations. |
| [spade_channel_explorer.py](spade_channel_explorer.py) | Modular repeated-count likelihood, bounded profiles, bootstrap machinery, and QFI sensitivity. |
| [SPADE_modular_channel_explorer.ipynb](notebooks/SPADE_modular_channel_explorer.ipynb) | Interactive exploration of named effective-channel scenarios. |
| [spade_eta_conditional_inference.py](spade_eta_conditional_inference.py) | Sequential fixed-channel eta fit, profile interval, bootstrap test, and QFI grids. |
| [SPADE_conditional_eta_results.ipynb](notebooks/SPADE_conditional_eta_results.ipynb) | Visual report for a chosen eta assumption file. |
| [spade_quantum_channel_inference.py](spade_quantum_channel_inference.py) | Quantum source, Kraus loss, unitary misalignment, dephasing, imperfect SPADE POVM, conditional eta fit, and QFI/CFI maps. |
| [spade_quantum_channel_assumptions.example.json](spade_quantum_channel_assumptions.example.json) | Explicit reference assumptions for the quantum-channel run. |
| [spade_qfi_validation.py](spade_qfi_validation.py) | QuTiP SLD/fidelity QFI validation and ideal-SPADE CFI comparison. |
| [SPADE_QFI_validation.ipynb](notebooks/SPADE_QFI_validation.ipynb) | Plots and explains the numerical QFI validation. |
| [SPADE_channel_QFI_results.ipynb](notebooks/SPADE_channel_QFI_results.ipynb) | Connects channel scenarios to their model QFI outputs. |
| [SPADE_modular_explorer.md](SPADE_modular_explorer.md) | Detailed channel scheme, component status, and QFI role. |
| [SPADE_channel_specification.md](SPADE_channel_specification.md) | Calibration handoff: which ASI measurement identifies which channel component. |
| [SPADE_QFI_readiness.md](SPADE_QFI_readiness.md) | Boundaries on what current data can and cannot establish as QFI. |
| [SPADE_QFI_procedure.md](SPADE_QFI_procedure.md) | Earlier end-to-end procedure and measurement requirements. |

### Earlier and Supporting Materials

| File or directory | Status in this report | Appropriate use |
| --- | --- | --- |
| [exoplanets_helper_functions.py](exoplanets_helper_functions.py) | Shared support code | Data loading, HG probability utilities, and legacy Fisher helper functions used by several workflows. |
| [notebooks/data_conversion.ipynb](notebooks/data_conversion.ipynb) | Data-preparation notebook | Documents conversion/preparation steps that produced supporting arrays. It is not the final count-channel inference. |
| [notebooks/data_validation.ipynb](notebooks/data_validation.ipynb) | Early data check | Useful for verifying array structure and loading assumptions before analysis. |
| [notebooks/analysis_notebook.ipynb](notebooks/analysis_notebook.ipynb) | Exploratory analysis | Historical interactive exploration; use the SPADE visual and modular notebooks for the current workflow. |
| [notebooks/QFI_notebook.ipynb](notebooks/QFI_notebook.ipynb) | QFI prototype | Early finite-difference/classical-QFI exploration. The QuTiP validation script is the authoritative current QFI check. |
| [notebooks/prova.ipynb](notebooks/prova.ipynb) | Scratch notebook | Keep as exploratory material; it is not part of the reproducible analysis chain. |
| [train/](train/) | Model/training inputs | Stores prepared `p0`, `p1`, distance, epsilon, and target-Fisher arrays for the earlier optimization workflow. |
| [models.py](models.py) and [eta_optimization_pytorch.py](eta_optimization_pytorch.py) | Earlier theory optimization | Fits `eta`/`delta` to precomputed Fisher-information targets through PyTorch. It does not fit the repeated `H_data.npy` count likelihood and must not be confused with the conditional eta inference in this report. |

The distinction is important: the current channel framework tests whether a
specified noisy physical configuration can generate the *observed count cube*.
The older PyTorch workflow optimizes agreement with a precomputed
Fisher-information target. Both can be useful model-development tools, but
they answer different questions.

## Conclusions and Boundaries

### What We Have Demonstrated

- The observed first-order SPADE counts require a baseline/cross-talk or
  background component and are overdispersed relative to Poisson counting.
- The dataset supports modular, constrained likelihood fits with repeated data
  rather than only curve-by-curve mean fits.
- Once a physical channel is specified, one component such as eta can be
  fitted conditionally and the complete configuration can be tested by
  parametric bootstrap.
- The same conditional test now operates on a composed quantum-channel model:
  loss is a Kraus map, sorter misalignment is unitary, dephasing is CPTP, and
  cross talk is an explicit imperfect SPADE POVM.
- The `F = 2.6` reference scenario is compatible with the data (`p = 0.806`),
  whereas the ideal-Poisson version is not (`p = 0.00498`).
- The truncated QFI implementation is numerically validated at regular points.
  Ideal full SPADE is nearly QFI-optimal in the model, while first-order-only
  SPADE retains most but not all of the model QFI.
- The quantum readout model shows why ideal first-order performance is not the
  same as real first-order performance: HG00 leakage can suppress binary
  recorded-count information well below the ideal first-order CFI.

### What We Cannot Claim Yet

- We cannot identify dark counts, input flux, eta, HG00 leakage, and HG1
  transmission separately from aggregate `n1` data alone.
- We cannot identify HG-basis dephasing from this diagonal aggregate count
  record, even though it is a valid physical channel and QFI sensitivity axis.
- We cannot jointly infer source offset and sorter displacement without an
  independent alignment reference.
- We cannot call the effective count CFI an experimentally measured QFI.
- We cannot infer coherence/dephasing from an HG1 aggregate count channel.
- We cannot interpret the unconstrained negative tail coefficient as a real
  negative leakage probability.
- We cannot treat a high bootstrap p-value as proof that the assumed channel
  is unique or physically correct.

### The Usable Next Step

The framework is ready for ASI calibration inputs. Each new independent
measurement removes one degeneracy. The most valuable additions are: incident
photons per acquisition, source-blocked background, HG00/HG1/higher-mode
injection calibration, separate HG01/HG10 and HG00 outputs, PSF/axis
calibration, and a time-resolved detector/source noise characterization.

After those values are supplied as bounds or fixed constants, rerun the
conditional channel fit, bootstrap it, and compare the resulting acceptable
eta/channel scenarios with their QFI and SPADE-information fractions. That is
the practical route from this data cube to a defensible model-validation and
measurement-design study.

## Reproducibility Notes

The numerical results in this report were reproduced in the `space` conda
environment with the current data and scripts. The key checks are:

```bash
conda run -n space python -m cqes.exoplanets.spade_analysis
conda run -n space python -m cqes.exoplanets.spade_calibration_analysis
conda run -n space python -m cqes.exoplanets.spade_channel_fitting
conda run -n space python -m cqes.exoplanets.spade_physical_channel
conda run -n space python -m cqes.exoplanets.spade_channel_explorer
conda run -n space python -m cqes.exoplanets.spade_qfi_validation
conda run -n space python -m cqes.exoplanets.spade_quantum_channel_inference \
  --assumptions cqes/exoplanets/spade_quantum_channel_assumptions.example.json
```

The conditional eta result uses an explicit assumptions file. Always archive
that file with any reported eta, p-value, count-CFI, or QFI comparison.
