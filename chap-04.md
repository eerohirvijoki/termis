---
numbering:
  enumerator: "4.%s"
  heading_1: true
  heading_2: true
  heading_3: true
---

# 4 Thermodynamic closure
This chapter establishes the thermodynamic framework that culminates in the Helmholtz and Gibbs specific free energy functions $f$ and $g$ for pure substances. Once these functions are known in terms of their natural variables, the other thermodynamic properties can be obtained through differentiation. This provides the theoretical foundation for thermodynamic property libraries such as pyromat and coolprop. More fundamentally, the differential relations connecting  the specific internal energy $u$, enthalpy $h$, and entropy $s$ to the fluid's state variables temperature $T$, density $\rho$ or specific volume $v$, and pressure $p$ provide the thermodynamic closure required by the fluid equations. The resulting theory is later put to work in deriving convenient engineering relations, and the positioning of this chapter within the overall roadmap is illustrated in {numref}`fig-roadmap-chap-04`.

:::{figure} ./figs/fig-roadmap-chap-04.svg
:label: fig-roadmap-chap-04
:align: center
:width: 100%
The positioning of the chapter content with respect to the roadmap.
:::

Establishing this framework involves considering a restricted class of quasistatic fluid flows for which viscous contributions to the energy balance can be neglected. Under these conditions, the fluid's energy balance takes the form of the first law of thermodynamics. It provides the basis for introducing the specific internal energy as a state function of the thermodynamic variables and relating its derivatives to experimental data obtained during heating of the substance. A related state function, the specific enthalpy, also emerges and plays a fundamental role in energy engineering applications involving steady-flow devices.

An observation that, in every neighbourhood of an equilibrium state, there exist states that cannot be reached from it through a quasistatic process without addition or removal of heat, together with Carathéodory's theorem from mathematics, establishes the existence of entropy as a state function. This provides the foundation for the second law of thermodynamics. Although the mathematical argument establishing the existence of entropy is treated as an advanced topic, entropy and the second law are core results of thermodynamics. Once entropy has been introduced, the differential relations between the thermodynamic state functions and their natural variables lead to the specific Helmholtz and Gibbs free energies.

The chapter also develops supplementary theoretical foundations underlying these results. The fluid energy balance is first rearranged to classify mechanical contributions volumetric work pressure perturbations, and viscous dissipation, providing a basis for defining quasistatic processes. The path dependence of heat and volumetric work, together with the path independence of the change in internal energy in quasistatic processes, then provide the mathematical justification for internal energy to be a state function. These arguments are discussed in detail in the intermediate and advanced sections, while their results are summarized in the core sections. Readers primarily interested in the core engineering path may therefore skip the intermediate and advanced sections and focus on using the resulting thermodynamic relations to compute properties for a given state.

## Learning goals

The learning goals for this chapter are listed below. The goals to support the core path include the following.

- <span class="elementary"></span> This a learning goal on the core path.

The goals to support the intermediate and advanced paths are:

- <span class="intermediate"></span> This is an intermediate learning goal.

- <span class="advanced"></span> This is an advanced learning goal.

## <span class="elementary"></span> Quasistatic processes and the first law of thermodynamics
The investigation of three fundamental physics principles over a material volume, namely the conservation of mass, momentum, and energy, provided local partial differential equations {numref}`eq-fluid-equations` for the time rate of change of density, velocity, and specific internal energy. Assuming an equation of state of the form $p=p(\rho,T)$ to exists, these equations involve four local quantities, ($\rho,T,u,\bm v$), but provide evolution equations for only three of them ($\rho,u,\bm v$). An additional relation connecting the internal energy to the thermodynamic state is therefore required to close the equations. The first step in finding such a relation involves identifying different contributions to the fluid's energy balance and defining quasistatic processes, during which certain terms in the energy balance can be neglected.

Over a time-dependent material volume $V(t)$, the energy balance {numref}`eq-energy-balance-material-volume` links the heat rate and the mechanical deformation work rate to the rate at which the internal energy of the material volume changes
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\rho udV}_{\substack{\text{Rate of change}\\\text{of internal energy}}}=\underbrace{\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA}_{\substack{\text{Net rate of heat received}\\\text{through the boundary}}}+\underbrace{\int_{V(t)}q_VdV}_{\substack{\text{Net rate of heat}\\\text{absorbed}\\\text{volumetrically}}}+\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}}.
:::
On the right, recall the expression {numref}`eq-constitutive-relations` for stress $\bm{\sigma}=-p\bm{I}+\bm{\tau}$. Using the vector identity $\bm{I}:\nabla\bm{v}=\nabla\cdot\bm{v}$ enables one to write
:::{math}
\bm{\sigma}:\nabla\bm{v}=-p(\nabla\cdot\bm{v})+\bm{\tau}:\nabla\bm{v}.
:::
Using the identity {numref}`eq-rho-identity` with $\bm{f}=1/\rho$, and the equation {numref}`eq-fluid-equations` for density, reveals the time rate of change of a macroscopic material volume to correspond to the volume integral of the velocity field divergence
:::{math}
\frac{dV(t)}{dt}=\frac{d}{dt}\int_{V(t)}dV=\frac{d}{dt}\int_{V(t)}\rho\frac{1}{\rho}dV=\int_{V(t)}\nabla\cdot\bm{v}dV
:::
Defining the average pressure $\bar{p}(t)$ over the material volume $V(t)$ as
:::{math}
\bar{p}(t)=\frac{1}{V(t)}\int_{V(t)}pdV,
:::
then let's one classify the contribution from the local deformations to the energy balance into three different terms
:::{math}
\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}}&=-\underbrace{\bar{p}\frac{dV}{dt}}_{\substack{\text{Expansion}\\\text{work rate}}}+\underbrace{\int_{V(t)}\delta p\,\nabla\cdot\bm{v}dV}_{\substack{\text{Pressure deviation}\\\text{deformation work rate}}}+\underbrace{\int_{V(t)}\bm{\tau}:\nabla\bm{v}dV}_{\substack{\text{Viscosity related}\\\text{deformation work rate}}},
:::
where $\delta p=\bar{p}-p$ is the local pressure deviation from the volumetric average. The terms involve contributions from viscous effects, from local pressure variations that couple to the local rate of volumetric expansion, and from the average pressure and the overall rate of volumetric expansion.


Denoting with $U$ and $\dot{Q}$ the total internal energy of the material volume and the rate of heat into the volume, and with $\dot{W}_{\delta p}$ and $\dot{W}_{\tau}$ the rates of mechanical energy change from pressure variations and viscous effects, respectively
:::{math}
\begin{aligned}
U&=\int_{V(t)}\rho udV,\\
\dot{Q}&=\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA+\int_{V(t)}q_VdV,\\
\dot{W}_{\delta p}&=\int_{V(t)}\delta p\,\nabla\cdot\bm{v}dV,\\
\dot{W}_{\tau}&=\int_{V(t)}\bm{\tau}:\nabla\bm{v}dV,
\end{aligned}
:::
the energy balance over the material volume can now be expressed as
:::{math}
\frac{dU}{dt}=\dot{Q}-\bar{p}\frac{dV}{dt}-\dot{W}_{\delta p}-\dot{W}_{\tau}.
:::

Quasistatic processes are defined as processes in which the spatial variations in pressure and the velocity field relax on time scales much shorter than the time scale on which the volume-averaged state evolves, while thin layers on the boundary of the volume may remain with finite temperature gradients to enable heat transfer into the volume from its surroundings. In such processes, the volume-averaged state approaches the experimentally measured equilibrium equation of state
:::{math}
\bar{p}(t)\to p(\bar{\rho}(t),\bar{T}(t)),
:::
and the mechanical work rates related to pressure deviation and viscous effects are small compared to the heat rate, the expansion work rate, or both
:::{math}
\frac{|\dot{W}_{\delta p}|}{\max(|\dot{Q}|,|\bar{p}\frac{dV}{dt}|)}\to 0,\qquad \frac{|\dot{W}_{\tau}|}{\max(|\dot{Q}|,|\bar{p}\frac{dV}{dt}|)}\to 0.
:::
In such case, the quasistatic energy equation reads
:::{math}
\frac{dU}{dt}=\dot{Q}-\bar{p}\frac{dV}{dt},
:::
and is referred to as the first law of thermodynamics. In textbooks, this equation is often presented in time-integrated form
:::{math}
\Delta U=Q-W
:::
with the terms corresponding to integrals between two time instants $t_0$ and $t_1$
:::{math}
\Delta U=\int_{t_0}^{t_1}\frac{dU}{dt}dt,\qquad Q=\int_{t_0}^{t_1}\dot{Q}dt,\qquad W=\int_{t_0}^{t_1}\bar{p}(t)\frac{dV}{dt}dt.
:::

