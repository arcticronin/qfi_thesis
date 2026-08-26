# Diagramming the Local-Metrology State Families

This note gives a precise language for the state families in the noise-analysis chapter.

> A parameter-dependent state preparation and a parameter-independent noise channel are different kinds of arrows.

The diagrams use a string-diagram-inspired convention:

~~~text
state preparation:       h ──► [ source ] ──► ρ(h)
fixed CPTP channel:      ρ ──► [ Λ ] ──► Λ(ρ)
restricted access:       ρ_SE ──► [ discard E ] ──► ρ_S
~~~

Here \(h_x\) is the field to be estimated, \(S\) is the accessible subsystem, and \(E\) is the inaccessible complement of the finite TFIM probe.

## 1. The common final operation

All three branches end with the same reduction map:

~~~text
                    ┌────────────────┐
ρ_SE ──────────────►│ Tr_E / discard  │──────────────► ρ_S
                    └────────────────┘
~~~

\[
\mathcal R_S(\rho_{SE})\coloneqq\operatorname{Tr}_E(\rho_{SE}).
\]

This is a parameter-independent CPTP map. It represents restricted access; \(E\) need not be a physical thermal bath.

## 2. Ground-state baseline

~~~text
h_x ──► H_N(h_x) ──► [ ground-state preparation ] ──► ρ_G,N(h_x)
                                                               │
                                                               ▼
                                                             [ Tr_E ]
                                                               │
                                                               ▼
                                                        ρ_sub(h_x)
~~~

\[
h_x\longmapsto\rho_{\mathrm{G},N}(h_x)
=|\psi_0(h_x)\rangle\langle\psi_0(h_x)|,
\qquad
\rho_{\mathrm{sub}}(h_x)=\operatorname{Tr}_E[\rho_{\mathrm{G},N}(h_x)].
\]

The first arrow is a state-family preparation rule, not a noise channel. The local state is mixed because \(S\) can be correlated with \(E\).

## 3. Depolarizing branch: a fixed channel after preparation

~~~text
h_x ──► [ ground-state preparation ] ──► ρ_G,N(h_x)
                                                    │
                                                    ▼
                                           [ Λ_P^(N) ]  fixed P
                                                    │
                                                    ▼
                                           ρ_dep,N(h_x; P)
                                                    │
                                                    ▼
                                                  [ Tr_E ]
                                                    │
                                                    ▼
                                           ρ_dep,S(h_x; P)
~~~

\[
\rho_{\mathrm{dep},S}(h_x;P)
=
\operatorname{Tr}_E\!\left[
\Lambda_P^{(N)}(\rho_{\mathrm{G},N}(h_x))
\right].
\]

For fixed \(P\), \(\Lambda_P^{(N)}\) is one CPTP map for the entire parameter sweep. Its Stinespring dilation can be drawn as

~~~text
ρ_G,N ────────────────┐
                       ▼
                [ U_P on N ⊗ B_dep ] ──► [ discard B_dep ] ──► Λ_P^(N)(ρ_G,N)
|0⟩⟨0|_Bdep ──────────┘
~~~

or written as

\[
\Lambda_P^{(N)}(\rho)=
\operatorname{Tr}_{B_{\mathrm{dep}}}\!\left[
U_P(\rho\otimes|0\rangle\langle0|_{B_{\mathrm{dep}}})U_P^\dagger
\right].
\]

The dilation ancilla \(B_{\mathrm{dep}}\) is not the same system as the finite TFIM complement \(E\). The former realizes the depolarizing channel; the latter is discarded because it is inaccessible.

Because \(\Lambda_P^{(N)}\) and \(\operatorname{Tr}_E\) are parameter independent for fixed \(P\),

\[
\mathcal F_Q[\rho_{\mathrm{dep},S}]
\leq
\mathcal F_Q[\rho_{\mathrm{dep},N}].
\]

## 4. Thermal branch in the thesis: equilibrium preparation, then restricted access

~~~text
h_x ──► H_N(h_x) ──► [ Gibbs preparation at fixed β ] ──► ρ_th,N(h_x; β)
                                                                  │
                                                                  ▼
                                                                [ Tr_E ]
                                                                  │
                                                                  ▼
                                                         ρ_th,S(h_x; β)
~~~

\[
\rho_{\mathrm{th},N}(h_x;\beta)
=
\frac{e^{-\beta H_N(h_x)}}{Z(h_x,\beta)},
\qquad
\rho_{\mathrm{th},S}(h_x;\beta)
=
\operatorname{Tr}_E[\rho_{\mathrm{th},N}(h_x;\beta)].
\]

Do **not** draw this as

~~~text
ρ_G,N(h_x) ──► [ Λ_β ] ──► ρ_th,N(h_x; β)
~~~

unless you introduce an explicit bath dynamics.

The global Gibbs state is a parameter-dependent preparation rule:

\[
\mathcal G_\beta:\quad
H_N(h_x)\longmapsto
\frac{e^{-\beta H_N(h_x)}}{Z(h_x,\beta)}.
\]

It creates a different encoded state family; it is not the fixed channel used in the depolarizing branch.

For every *fixed* \(h_x\), one can formally define a replacement channel

\[
\Phi_{\beta,h_x}(X)
=
\operatorname{Tr}(X)\rho_{\mathrm{th},N}(h_x;\beta).
\]

This channel has a Stinespring dilation, but its unitary dilation depends on \(h_x\). It is therefore a different channel at every point in the sweep, not one parameter-independent channel acting on the ground-state family.

The valid data-processing comparison is within the thermal family:

\[
\mathcal F_Q[\rho_{\mathrm{th},S}(h_x;\beta)]
\leq
\mathcal F_Q[\rho_{\mathrm{th},N}(h_x;\beta)].
\]

Also, the local reduced thermal state is generally not the bare Gibbs state of the accessible Hamiltonian:

\[
\operatorname{Tr}_E[\rho_{\mathrm{th},N}]
\neq
\frac{e^{-\beta H_S}}{\operatorname{Tr}(e^{-\beta H_S})}.
\]

Interactions and correlations across the \(S\)--\(E\) boundary remain encoded in the reduction.

## 5. Combined main-text diagram

This is the recommended comparative diagram.

~~~text
                                      ┌──────────────────────────────► ρ_sub(h_x)
                                      │                                  ▲
h_x ──► H_N(h_x) ──► ground state ρ_G,N(h_x) ──► [ Tr_E ] ───────────────┘
                                      │
                                      │ [ fixed depolarizing channel Λ_P^(N) ]
                                      ▼
                                ρ_dep,N(h_x; P) ──► [ Tr_E ] ──► ρ_dep,S(h_x; P)


h_x ──► H_N(h_x) ──► [ Gibbs preparation at fixed β ] ──► ρ_th,N(h_x; β)
                                                                 │
                                                                 ▼
                                                               [ Tr_E ]
                                                                 │
                                                                 ▼
                                                        ρ_th,S(h_x; β)
~~~

The visual message is:

- Ground and thermal branches are different preparation families.
- Depolarization is a fixed channel after ground-state preparation.
- Partial trace is the common final operation.
- Do not use the same channel-box symbol for \(\Lambda_P^{(N)}\) and Gibbs preparation.

## 6. Matched-purity control

~~~text
h_x ──► ρ_sub(h_x) ──► target purity γ_sub(h_x)
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
      choose P(h_x)             choose β(h_x)
            │                         │
            ▼                         ▼
       ρ_dep,S(h_x; P(h_x))   ρ_th,S(h_x; β(h_x))
~~~

This is a selected path through state space, not a fixed channel. The SLD derivative must therefore include the derivatives of \(P(h_x)\) or \(\beta(h_x)\).

## 7. Optional future model: genuine finite-time thermalization

A true bath-dynamics study would have a different diagram:

~~~text
ρ_in ──► [ encode h_x ] ──► ρ(h_x)
                                 │
                                 ▼
                   [ Φ_β,t^(h_x): bath coupling for time t ]
                                 │
                                 ▼
                         ρ_open(h_x; β, t)
~~~

For example,

\[
\Phi_{\beta,t}^{(h_x)}=e^{t\mathcal L_{\beta,h_x}},
\]

where \(\mathcal L_{\beta,h_x}\) is a detailed-balance Lindblad generator. This requires a bath/coupling model, a time scale, and an explanation of whether the generator depends on \(h_x\). It is a different project from global Gibbs preparation.

## Diagramming checklist

Before labelling a box a noise channel, ask:

1. Does it act on the same input state at every \(h_x\)?
2. Are its parameters fixed through the sweep?
3. Is it one CPTP map independent of the estimated parameter?

If yes, draw it as a channel box, as for fixed depolarization.

If no because the state is constructed from \(H_N(h_x)\), draw it as a preparation box, as for Gibbs preparation.

## Further reading

- [Talkner and Hänggi, Reviews of Modern Physics 92, 041002 (2020)](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.92.041002) explains why a reduced equilibrium state need not be the bare Gibbs state of the subsystem.
- [Wang et al., Light: Science & Applications 11, 194 (2022)](https://www.nature.com/articles/s41377-022-00887-5) discusses the distinction between thermalization and generalized Gibbs behavior in integrable systems.

