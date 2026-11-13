---
numbering:
  enumerator: "4.%s"
  heading_1: true
  heading_2: true
  heading_3: true
---

# 4 Thermodynamic closure
This chapter establishes the thermodynamic framework that culminates in the Helmholtz and Gibbs specific free energy functions $f$ and $g$ for pure substances. Once these functions are known in terms of their natural variables, the other thermodynamic properties can be obtained through differentiation. This provides the theoretical foundation for thermodynamic property libraries such as pyromat and coolprop. More fundamentally, the differential relations connecting  the specific internal energy $u$, enthalpy $h$, and entropy $s$ to the fluid's state variables temperature $T$, density $\rho$ or specific volume $v$, and pressure $p$ provide the thermodynamic closure required by the fluid equations. The resulting theory is later put to work in deriving convenient engineering relations. The positioning of this chapter within the overall roadmap is illustrated in {numref}`fig-roadmap-chap-04`.

:::{figure} ./figs/fig-roadmap-chap-04.svg
:label: fig-roadmap-chap-04
:align: center
:width: 100%
The positioning of the chapter content with respect to the roadmap.
:::

Establishing this framework involves considering a restricted class of quasistatic fluid flows for which viscous contributions to the energy balance can be neglected. Under these conditions, the fluid's energy balance takes the form of the first law of thermodynamics. It provides the basis for introducing the specific internal energy as a state function of the thermodynamic variables and relating its derivatives to experimental data obtained during heating of the substance. A related state function, the specific enthalpy, also emerges and plays a fundamental role in energy engineering applications involving steady-flow devices.

An observation that, in every neighbourhood of an equilibrium state, there exist states that cannot be reached from it through a quasistatic process without addition or removal of heat, together with Carathéodory's theorem from mathematics, establishes the existence of entropy as a state function. This provides the foundation for the second law of thermodynamics. Although the mathematical argument establishing the existence of entropy is treated as an advanced topic, entropy and the second law are core results of thermodynamics. Once entropy has been introduced, the differential relations between the thermodynamic state functions and their natural variables lead to the specific Helmholtz and Gibbs free energies.

The chapter also develops supplementary theoretical foundations underlying these results. The fluid energy balance is first rearranged to distinguish mechanical and thermal contributions, providing a basis for defining quasistatic processes. The path dependence of heat and work, together with the path independence of the change in internal energy in quasistatic processes, then provide the mathematical justification for internal energy to be a state function. These arguments are discussed in detail in the intermediate and advanced sections, while their results are summarized in the core sections. Readers primarily interested in the core engineering path may therefore skip the intermediate and advanced sections and focus on using the resulting thermodynamic relations to compute properties for a given state.

## Learning goals

The learning goals for this chapter are listed below. The goals to support the core path include the following.

- <span class="elementary"></span> This a learning goal on the core path.

The goals to support the intermediate and advanced paths are:

- <span class="intermediate"></span> This is an intermediate learning goal.

- <span class="advanced"></span> This is an advanced learning goal.

## <span class="advanced"></span> Rearrangement of the energy balance
The conservation laws investigated over an arbitrary material volume provide local equations for the time rate of change of density, velocity, and specific internal energy. These equations involve four local quantities, ($\rho,T,u,\bm v$), but provide evolution equations for only three of them ($\rho,u,\bm v$). An additional relation connecting the internal energy to the thermodynamic state is therefore required to close the equations. The purpose of this section is to rearrange the energy balance to enable construction of such a relation from experimentally measurable data.

The energy balance over a material volume $V(t)$ links heat rate and mechanical deformation work rate to the rate at which internal energy of the volume changes
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\rho udV}_{\substack{\text{Rate of change}\\\text{of internal energy}}}=\underbrace{\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA}_{\substack{\text{Net rate of heat received}\\\text{through the boundary}}}+\underbrace{\int_{V(t)}q_VdV}_{\substack{\text{Net rate of heat}\\\text{absorbed}\\\text{volumetrically}}}+\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}}.
:::
As the mass $m=\int_{V(t)}\rho dV$ of the material volume $V(t)$ is constant in time, the time rate of change of the total internal energy on the left side of the energy balance becomes
:::{math}
\frac{d}{dt}\int_{V(t)}\rho udV=m\frac{d\bar{u}}{dt},
:::
where $\bar{u}$ is the density-weighted volume average of the local internal energy field, defined
:::{math}
\bar{u}=\frac{1}{m}\int_{V(t)}\rho u dV.
:::
Associating the heat and mechanical deformation work rates on the right of the energy balance with the values and time rates change of volume-averaged state variables and excess terms, provides a link between internal energy and experimentally measurable state variables. Further inspection of the energy balance at a limit where the excess terms can be considered negligible, and assuming the reduced energy balance to hold regardless of the material volume chosen, provides a relation for internal energy in terms of state variables, which can then be interpreted as a local thermodynamic relation.

This process begins with associating local field values to volume averages. Over a time-dependent material volume $V(t)$, the Neumann Green's function $G_N(\bm{x},\bm{x}',t)$ is defined as the solution to the time-dependent boundary-value problem
:::{math}
\begin{aligned}
    \nabla'^2G_N(\bm{x}',\bm{x},t)
    &=
    \frac{1}{V(t)}-\delta^3(\bm{x}'-\bm{x}),
    &&
    \bm{x},\bm{x}'\in V(t),\\
    \nabla'G_N(\bm{x}',\bm{x},t)\cdot\bm{\hat n}(\bm{x}',t)
    &=0,
    &&
    \bm{x}'\in\partial V(t).
\end{aligned}
:::
For a sufficiently smooth scalar field $f(\bm{x},t)$, the function $G_N$ provides the following identity between the function value and it's volume average $\bar{f}(t)=(1/V(t))\int_{V(t)}f(\bm{x},t)dV$
:::{math}
:label: eq-field-average-deviation
f(\bm{x},t)-\bar{f}(t)=\int_{V(t)}\nabla'G_N(\bm{x}',\bm{x},t)\cdot \nabla'f(\bm{x}',t)\,dV'.
:::
According to the identity, the local deviation of a scalar field from its volume averaged value relates to the field gradient in the entire volume, and is bounded by the maximum value of the gradient within the volume and a geometric factor
:::{math}
    |f(\bm{x},t)-\bar{f}(t)|\leq \int_{V(t)}|\nabla G_N|dV\,\max_{V(t)}|\nabla f|.
:::
::::{proof:example}
Verifying the identity~\eqref{eq:field-average-deviation} proceeds by multiplying the defining equation for $G_N$ and by $f$ and integrating it over the volume:
:::{math}
:enumerated: false
\begin{align*}
f(\bm{x},t)-\frac{1}{V(t)}
\int_{V(t)}f(\bm{x}',t)\,dV'
&=
\int_{V(t)}
	f(\bm{x}',t)
        \left[
            \delta^3(\bm{x}'-\bm{x})-\frac{1}{V(t)}
        \right]dV'\\
        &=
        -\int_{V(t)}
        f(\bm{x}',t)
        \nabla'^2G_N(\bm{x}',\bm{x},t)\,dV'\\
        &=
        -\int_{\partial V(t)}
        f(\bm{x}',t)
        \nabla'G_N(\bm{x}',\bm{x},t)
        \cdot\bm{\hat n}(\bm{x}',t)\,dA\\
        &\qquad
        +\int_{V(t)}
        \nabla'G_N(\bm{x}',\bm{x},t)
        \cdot\nabla'f(\bm{x}',t)\,dV'\\
        &=
        \int_{V(t)}
        \nabla'G_N(\bm{x}',\bm{x},t)
        \cdot\nabla'f(\bm{x}',t)\,dV'.
    \end{align*}
:::
On the second to last line, the boundary term vanishes because of the normal derivative of $G_N$ vanishes on the boundary.
::::

With the help of the Neumann Green's function, one is able to separate the mechanical deformation work rate in the energy balance into a term expressible in terms of volume-averaged state variables and their rates, and excess terms. For this to work, use first the identities $\bm{I}:\nabla\bm{v}=\nabla\cdot\bm{v}$, $\bm{I}:\bm{I}=3$, and $\bm{D}:\bm{I}=0$ to express the term $\bm{\sigma}:\nabla\bm{v}$ as
:::{math}
:label: eq-stress-work-decomposition
\bm{\sigma}:\nabla\bm{v}=-p\nabla\cdot\bm{v}+2\mu\bm{D}:\bm{D}+\zeta(\nabla\cdot\bm{v})^2,
:::
so that the mechanical deformation work rate in the energy balance is split into pressure and viscosity related contributions
\begin{align}
    \underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Mechanical deformation}\\\text{work rate}}}=-\underbrace{\int_{V(t)}p\nabla\cdot\bm{v}dV}_{\substack{\text{Pressure related}\\\text{deformation work rate}}}+\underbrace{\int_{V(t)}\left(2\mu\bm{D}:\bm{D}
    +\zeta(\nabla\cdot\bm{v})^2\right)dV}_{\substack{\text{Viscosity related}\\\text{deformation work rate}}}
\end{align}
Next use the Leibniz rule to realize that the divergence of the velocity is related to the rate of change of volume-averaged specific volume or density via
\begin{align}
    \int_{V(t)}\nabla\cdot\bm{v}\,dV
    =
    \frac{dV(t)}{dt}
    =
    m\frac{d\bar v(t)}{dt}
    =
    -\frac{m}{\bar{\rho}^2}
    \frac{d\bar{\rho}(t)}{dt},
\end{align}
where $\bar v(t)=V(t)/m$ is the volume-averaged specific volume and $\bar{\rho}(t)=1/\bar{v}(t)$ the corresponding volume-averaged density. If the pressure were constant over the volume $V(t)$, it could be directly pulled out of the integral of $p\nabla\cdot\bm{v}$, resulting in a term expressible in volume averages only. Generally this is not true, though, and a trick involving the Neumann Green's function is needed. For the trick, define the volume-averaged pressure
\begin{align}
    \bar{p}(t)=\frac{1}{V(t)}\int_{V(t)}p\,dV,
\end{align}
with the deviation in the local value from the volume average $\bar{p}$ being expressible in terms of the Neumann Green's function
\begin{align}
    p(\bm{x},t)-\bar{p}(t)=\int_{V(t)}\nabla'G_N(\bm{x}',\bm{x},t)\cdot\nabla'p(\bm{x}',t)\,dV'.
\end{align}
Then formally decompose the local pressure into average and a pressure deviation according to $p=\bar p+(p-\bar p)$. The average part can now be pulled out of the integral while the deviation provides a gradient-related correction term, resulting in
\begin{align}
    \underbrace{\int_{V(t)}p\nabla\cdot\bm v\,dV}_{\substack{\text{Pressure related}\\\text{deformation work rate}}}
    &=
    \bar p\int_{V(t)}\nabla\cdot\bm v\,dV
    +
    \int_{V(t)}(p-\bar p)\nabla\cdot\bm v\,dV\\
    &=
    \underbrace{m\bar p\frac{d\bar v}{dt}}_{\substack{\text{Average}\\\text{pressure}\\\text{related}\\\text{deformation}\\\text{work rate}}}
    +
    \underbrace{\int_{V(t)}
    \int_{V'(t)}
    (\nabla\cdot\bm v)
    \nabla'G_N\cdot\nabla'p\,
    dV'\,dV}_{\substack{\text{Local pressure deviation related}\\\text{deformation work rate}}}.
\end{align}

Denote the mass-specific average pressure deformation work rate, the pressure variation related deformation work rate, and the viscous contribution to the deformation work rate with
\begin{align}
    \label{eq:dot-w_p-expressions}
    \dot{\bar w}_p
    &=
    \bar p\frac{d\bar v}{dt}
    =
    -\frac{\bar p}{\bar{\rho}^2}
    \frac{d\bar{\rho}}{dt},\\
    \dot{\mathcal W}_{\delta p}
    &=
    \int_{V(t)}
    \int_{V'(t)}
    (\nabla\cdot\bm v)
    \nabla'G_N\cdot\nabla'p\,
    dV'\,dV,\\
    \dot{\mathcal W}_{\mu,\zeta}
    &=
    -\int_{V(t)}
    \left(
        2\mu\bm D:\bm D
        +
        \zeta(\nabla\cdot\bm v)^2
    \right)dV,
\end{align}
and the total deformation work rate contributing to the energy balance is then expressed
\begin{align}
    \int_{V(t)}
    \bm{\sigma}:\nabla\bm v\,dV
    =
    -m\dot{\bar w}_p
    -\dot{\mathcal W}_{\delta p}
    -\dot{\mathcal W}_{\mu,\zeta},
    \label{eq:stress-work-averaged}
\end{align}
The deformation work rate is now separated into a contribution expressed entirely in terms of volume-averaged state variables and two correction terms associated with spatial non-uniformity. The pressure-deviation term involves a product of the pressure and velocity gradients, while the viscous contribution is quadratic in the velocity gradient. Furthermore, since $\bm{D}:\bm{D}=\sum_{ij}D_{ij}^2\geq 0$, $(\nabla\cdot\bm{v})^2\geq 0$, and the viscous coefficients $\mu$ and $\zeta$ are non-negative, the viscous deformation work rate $\dot{\mathcal{W}}_{\mu,\zeta}$ is always non-positive. The pressure-deviation contribution $\dot{\mathcal{W}}_{\delta p}$, in contrast, may be positive or negative.
For the heat rate terms on the right of the energy balance, denote the total rate of heat received by the fluid as
\begin{align}
    \dot{\mathcal Q}
    &=
    \int_{\partial V(t)}
    \bm{q}\cdot(-\bm{\hat{n}})dA
    +
    \int_{V(t)}q_V\,dV=
    \int_{\partial V(t)}
    \lambda\nabla T\cdot\bm{\hat n}\,dA
    +
    \int_{V(t)}q_V\,dV.
\end{align}
The dependence of this functional on the state variables enters both through the thermal conductivity $\lambda$ and through the local volumetric energy-transfer rate $q_V$. Substituting the above expressions into the material-volume energy balance finally provides
\begin{align}
    \underbrace{m\frac{d\bar u}{dt}}
    _{\substack{\text{Rate of}\\\text{internal}\\\text{energy}\\\text{change}}}
    =
    \underbrace{\dot{\mathcal Q}}
    _{\substack{\text{Net rate}\\\text{of heat}\\\text{into the}\\\text{fluid}}}
    -
    \underbrace{m\dot{\bar w}_p}
    _{\substack{\text{Rate of}\\\text{work by}\\\text{average}\\\text{pressure}}}
    -
    \underbrace{\dot{\mathcal W}_{\delta p}}
    _{\substack{\text{Rate of}\\\text{work by}\\\text{pressure}\\\text{variations}}}
    -
    \underbrace{\dot{\mathcal W}_{\mu,\zeta}}
    _{\substack{\text{Rate of}\\\text{work by}\\\text{viscous}\\\text{forces}}}.
    \label{eq:energy-balance-macroscopic}
\end{align}
The important feature of this decomposition is that the first work term depends only on the macroscopic state variables, whereas the remaining terms are explicitly controlled by spatial gradients that can be assessed in an appropriate limit. As the next step, one this limit is considered to connect the heat rate $\dot{\mathcal{Q}}$ into rates of change of the volume-averaged state variables.
