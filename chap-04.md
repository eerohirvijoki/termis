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

## <span class="elementary"></span> Specific heats
The first step in the process of uncovering the thermodynamic framework involves relating heat to the fluid's state variables. Typically, one associates heating a substance with an increase in the substance temperature or boiling it at constant temperature. Conversely, cooling a substance is associated with either reducing its temperature or causing it to condense at constant temperature. The specific details of a heating or a cooling process vary, though. To illustrate them consider two different processes described in {numref}`fig-heating-cylinder-constant-v` and {numref}`fig-heating-cylinder-constant-p`.

::::{figure}
:label: fig-heating-cylinder
:align: center
:width: 100%

(fig-heating-cylinder-constant-v)=
:::{image} ./figs/fig-heating-cylinder-constant-v.svg
:alt: Substance heated in a constant volume cylinder with spatially homogenous initial and final states between which the pressure, temperature, density, and fluid velocity within may vary spatially and temporally. The load to keep the piston in place varies over time.
:width: 90%
:::

(fig-heating-cylinder-constant-p)=
:::{image} ./figs/fig-heating-cylinder-constant-p.svg
:alt: Substance heated in a cylinder with spatially homogenous initial and final states that share a common pressure. The external load on the piston is kept constant and equal to the initial equilibrium value. Consequently, the cylinder volume changes over time due to force imbalance on the piston. Between the initial and final time, pressure, temperature, density, and fluid velocity within may vary spatially and temporally.
:width: 90%
:::

Two different ways to heat a fluid.
::::


The resulting responses in the water temperature with respect to heat added per unit mass when progressing through subsequent equilibrium states.

::::{figure} ./figs/fig-heat-delta-T-isochoric.svg
:label: fig-heat-delta-T-isochoric
:align: center
:width: 80%
Water temperature when heated from $T=0^\circ\text{C}$ through equilibrium states with constant volume.
::::

In the first case, substance
::::{figure} ./figs/fig-heat-delta-T-isobaric.svg
:label: fig-heat-delta-T-isobaric
:align: center
:width: 80%
Water temperature when heated from $T=0^\circ\text{C}$ through equilibrium states with constant pressure.
::::

Definitions for the specific heat capacities
:::{math}
\begin{aligned}
c_v&=\lim_{\Delta T\to 0}\frac{Q/m}{\Delta T}, \qquad \text{heat added at constant volume},\\
c_p&=\lim_{\Delta T\to 0}\frac{Q/m}{\Delta T}, \qquad \text{heat added at constant pressure}.
\end{aligned}
:::

The specific heats $c_v$ and $c_p$ for water are illustrated in {numref}`fig-cv-cp-H2O`, and one recognizes the isocontours of both $c_v$ and $c_p$ to be almost perfectly vertical in a region where temperature is high enough and water vapor is dilute enough (low density, high specific volume). This indicates that the specific heats in the ideal gas region approximately depend on temperature only. For gases, this is a commonly used approximation, and often even a constant value is sufficient over a large temperature range. The specific heats can be computed with both pyromat and coolprop libraries, and only in the single-phase regions. They are not defined in the phase-change regions.

::::{figure}
:label: fig-cv-cp-H2O
:align: center
:width: 100%

(fig-cv-H2O)=
:::{image} ./figs/fig-cv-H2O.svg
:alt: Isochoric specific heat for water.
:width: 80%
:::

(fig-cp-H2O)=
:::{image} ./figs/fig-cp-H2O.svg
:alt: Isobaric specific heat for water.
:width: 80%
:::

Isocontours of specific heats $c_v$ and $c_p$ for water in a $v$-$T$ diagram.
::::

::::{proof:example}
The specific heats can be computed with both the pyromat and coolprop libraries. The script below serves as a demonstration:
```{literalinclude} python/example-cv-cp-evaluation.py
:language: python
:start-line: 0
:end-line: 35
:linenos:
```
At the requested state point both pyromat and coolprop return $c_v=2.23\,\text{kJ}/\text{kg}/\text{K}$ and $c_p=4.00\,\text{kJ}/\text{kg}/\text{K}$. The values can be confirmed from {numref}`fig-cv-cp-H2O`.
::::


## <span class="elementary"></span> First law
The first step in the process of uncovering the thermodynamic framework involves relating heat to the fluid's state variables. Typically, one associates heating a substance with an increase in the substance temperature or boiling it at constant temperature. Conversely, cooling a substance is associated with either reducing its temperature or causing it to condense at constant temperature. The specific details of a heating or a cooling process vary, though. Heating a gas in a rigid bottle increases the gas temperature while its volume remains constant. If the gas is initially in a thermal equilibrium state, and is let to achieve a new thermal equilibrium state after heating has been cut off, the material volume of the gas has not changed. Therefore, no mechanical work is performed, and the applied heat is converted primarily into internal energy, and into gravitational potential energy to a minor degree. Heating a soft elastic gas balloon, on the other hand, causes the balloon to expand while the temperature increases. As the balloon expands, the material volume of the gas changes over time, and the forces causing the volume change do mechanical work. Once a new equilibrium state is eventually achieved after cutting the heat off, the total heat applied is distributed between a change in the gas internal energy and work performed, and to a small degree a change in the gravitation potential energy. In both cases, valuable information of the subtances response to heating can be obtained by careful design of the heating experiment.

Consider the experiment illustrated in {numref}`fig-heating-cylinder` that is performed in outer space to eliminate gravitational effects. Fluid is enclosed into a cylinder with a movable piston of mass $m_p$. Denote the fluid surface height at the piston level with $z_p(t)$, the piston velocity with $v_p(t)=dz_p/dt$, the contact surface with the fluid with $A_p(t)$, and the fluid volume material volume with $V(t)$. Let $F_\text{f}(t)$ denote the friction force between the piston and the cylinder surface. Assume that a perfectly controllable external force of magnitude of $F_\text{ext}(t)$ can be exerted to the piston perpendicular to its surface from the outside. 

Denote with $U(t)$ and $KE(t)$ the total internal and kinetic energy of the fluid within $V(t)$ at time $t$
:::{math}
U(t)=\int_{V(t)}\rho u dV, \qquad KE(t)=\int_{V(t)}\frac{1}{2}\rho|\bm{v}|^2dV,
:::
During a time interval $t\in[t_0,t_1]$, denote with $\dot{Q}$ and $Q$ the heat rate and the total heat applied into the fluid
:::{math}
\dot{Q}(t)=\int_{\partial V(t)}(-\bm{q})\cdot\bm{\hat{n}}dA+\int_{V(t)}q_VdV, \qquad Q=\int_{t_0}^{t_1}\dot{Q}dt,
:::
and with $\dot{W}$ and $W$ the mechanical work rate and the total work performed by the fluid
:::{math}
\dot{W}(t)=-\int_{\partial V(t)}\bm{v}\cdot\bm{\sigma}\cdot\bm{\hat{n}}dA=-\int_{A_p(t)}v_p \sigma_{zz}dA, \qquad W=\int_{t_0}^{t_1}\dot{W}dt.
:::
The second follows from the fluid velocity on a solid surface mathching the surface velocity, meaning $\bm{v}|_{A_p(t)}=v_p(t)\bm{\hat{z}}$. In the absence of gravity, the energy balance {numref}`eq-total-energy-balance-material-volume` integrated over a time interval $t\in[t_0,t_1]$ then reads
:::{math}
\Delta U+\Delta KE=Q-W,
:::
where $\Delta U=U(t_1)-U(t_0)$ and $\Delta KE=KE(t_1)-KE(t_0)$ are the changes in the total internal energy and kinetic energy over the time interval $t\in[t_0,t_1]$.

Initially, at time $t_0$, the substance is in a thermal equilibrium state with a uniform temperature $T(\bm{x},t_0)=T_0$, pressure $p(\bm{x},t_0)=p_0$, density $\rho(\bm{x},t_0)=\rho_0$, and a zero velocity $\bm{v}(\bm{x},t_0)=\bm{0}$. The external force on the piston is set to exactly balance the force the fluid exerts to the piston due to pressure $F_\text{ext}(t_0)=p_0A_p$ and the friction force is balanced out $F_\text{f}(t_0)=0$. Once heating is applied over the time interval $t\in[t_0,t_\ast]$, temperature, density, and pressure within the fluid become non-homogenous, and the increased pressure within the fluid pushes the piston into motion. After the heating is stopped at time $t_\ast$, the fluid takes a while to find a new equilibrium state at time $t_1$, and the piston moves to a point where the new fluid equilibrium pressure again balances the external force. 

The piston movement during the interval $t\in[t_0,t_1]$ obeys Newton's second law
:::{math}
m\underbrace{\frac{dv_p}{dt}}_{\substack{\text{piston}\\\text{accele-}\\\text{ration}}}=\overbrace{-\underbrace{\int_{A_p(t)}\sigma_{zz}dA}_{\substack{\text{Total contact force}\\\text{from the piston}\\\text{to the fluid}}}}^{\substack{\text{Total contact force}\\\text{from the fluid}\\\text{to the piston}}}-F_\text{ext}-F_f
:::
The change in the kinetic energy of the piston over the interval $t\in[t_0,t_1]$ is computed to be
:::{math}
\begin{aligned}
\frac{m_p}{2}\left(v_p(t_1)^2-v_p(t_0)^2\right)&=\int_{t_0}^{t_1}m\frac{dv_p}{dt}v_pdt\\
&=\int_{t_0}^{t_1}\left[-\int_{A_p(t)}\sigma_{zz}dA-(F_\text{ext}+F_\text{f})\right]v_pdt\\
&=-\int_{t_0}^{t_1}\int_{A_p(t)}v_p\sigma_{zz}dAdt-\int_{t_0}^{t_1}(F_\text{ext}+F_\text{f})v_pdt
\end{aligned}
:::
Since the piston velocity at the beginning and at the end is zero, the change in the kinetic energy over the interval $t\in[t_0,t_1]$ vanishes and one finds
:::{math}
\int_{t_0}^{t_1}(F_\text{ext}+F_\text{f})v_p(t)dt=-\int_{t_0}^{t_1}\int_{A_p(t)}v_p\sigma_{zz}dAdt=W.
:::
If the external force is adjusted so that the sum of it and the friction force, throughout the interval $t\in[t_0,t_1]$, equals the force from the initial fluid equilibrium pressure, then 
:::{math}
F_\text{ext}+F_\text{f}=p_0A \quad \implies \quad \int_{t_0}^{t_1}(F_\text{ext}+F_\text{f})v_p(t)dt=p_0(V(t_1)-V(t_0)).
:::
Since the fluid velocity at the beginning and end of the interval vanishes, also the change in the total kinetic energy vanishes. In this specially tailored case, the change in the fluids internal energy is seen to equal
:::{math}
\Delta U=Q-p_0(V(t_1)-V(t_0)), \qquad \text{expansion against constant force}. 
:::
If the external force instead is controlled to retain the piston in place at all times, then no work is performed and the time integrated energy balance reduces to
:::{math}
\Delta U=Q, \qquad \text{no surface movement}. 
:::

In these specically controlled experiments, one has managed to convert the difficult looking stress contribution into a simple expression involving only equilibrium fluid variables. If also the total heat applied $Q$ could be related to the fluids equilibrium state variables, the path to associating internal energy in terms of state variables would be open. This can be done in terms of specific heats.






## <span class="elementary"></span> Quasistatic processes and the first law of thermodynamics
The application of three fundamental conservation principles over a material volume, namely the conservation of mass, momentum, and energy, provided local partial differential equations {numref}`eq-fluid-equations` for the time rate of change of density, velocity, and specific internal energy. Assuming an equation of state of the form $p=p(\rho,T)$ to exist, pressure can be expressed in terms of density and temperature. The fluid equations then involve four local unknown fields, ($\rho,T,u,\bm v$), but provide evolution equations for only three of them ($\rho,u,\bm v$). An additional relation expressing the specific internal energy in terms of the thermodynamic state variables is therefore required to close the equations. The first step in finding such a relation involves identifying different contributions to the fluid's energy balance and defining quasistatic processes, during which certain terms in the energy balance can be neglected.

Over a time-dependent material volume $V(t)$, the energy balance {numref}`eq-energy-balance-material-volume` links the heat rate and the mechanical deformation work rate to the rate at which the internal energy of the material volume changes
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\rho udV}_{\substack{\text{Rate of change}\\\text{of internal energy}}}=\underbrace{\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA}_{\substack{\text{Net rate of heat received}\\\text{through the boundary}}}+\underbrace{\int_{V(t)}q_VdV}_{\substack{\text{Net rate of heat}\\\text{absorbed}\\\text{volumetrically}}}+\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}}.
:::
On the right, recall the expression {numref}`eq-constitutive-relations` for stress $\bm{\sigma}=-p\bm{I}+\bm{\tau}$. Using the vector identity $\bm{I}:\nabla\bm{v}=\nabla\cdot\bm{v}$, one may write
:::{math}
\bm{\sigma}:\nabla\bm{v}=-p(\nabla\cdot\bm{v})+\bm{\tau}:\nabla\bm{v}.
:::
Using the identity {numref}`eq-rho-identity` with $\bm{f}=1/\rho$, and the equation {numref}`eq-fluid-equations` for density, one fids that the time rate of change of a macroscopic material volume to corresponds to the volume integral of the velocity field divergence
:::{math}
\frac{dV(t)}{dt}=\frac{d}{dt}\int_{V(t)}dV=\int_{V(t)}\rho\frac{D\rho^{-1}}{Dt}dV=\int_{V(t)}\nabla\cdot\bm{v}dV.
:::
Defining then the volume-averaged pressure $\bar{p}(t)$ over the material volume $V(t)$ as
:::{math}
\bar{p}(t)=\frac{1}{V(t)}\int_{V(t)}pdV,
:::
allows one to decompose the contribution from the local deformations to the energy balance into three different terms
:::{math}
\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}}=-\underbrace{\bar{p}\frac{dV}{dt}}_{\substack{\text{Expansion}\\\text{work rate}}}-\underbrace{\int_{V(t)}\delta p\,\nabla\cdot\bm{v}dV}_{\substack{\text{Pressure deviation}\\\text{deformation work rate}}}+\underbrace{\int_{V(t)}\bm{\tau}:\nabla\bm{v}dV}_{\substack{\text{Viscosity related}\\\text{deformation work rate}}},
:::
where $\delta p=p-\bar{p}$ is the local pressure deviation from the volumetric average. The three contributions represent rates of mechanical energy change associated with the average pressure and overall volumetric expansion, local pressure variations coupled to local volumetric deformation, and viscous stresses acting during deformation.


Denoting with $U$ and $\dot{Q}$ the total internal energy of the material volume and the net rate of heat into the volume, and with $\dot{W}_{\delta p}$ and $\dot{W}_{\tau}$ the rates of mechanical energy change from pressure variations and viscous effects, respectively
:::{math}
\begin{aligned}
U&=\int_{V(t)}\rho udV,\\
\dot{Q}&=\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA+\int_{V(t)}q_VdV,\\
\dot{W}_{\delta p}&=\int_{V(t)}\delta p\,\nabla\cdot\bm{v}dV,\\
\dot{W}_{\tau}&=\int_{V(t)}(-\bm{\tau}):\nabla\bm{v}dV,
\end{aligned}
:::
the energy balance over the material volume can be expressed as
:::{math}
\frac{dU}{dt}=\dot{Q}-\bar{p}\frac{dV}{dt}-\dot{W}_{\delta p}-\dot{W}_{\tau}.
:::

Quasistatic processes are then theoretical limit processes in which the fluid state remains close to homogenous and contributions from $\dot{W}_{\delta p}$ and $\dot{W}_\tau$ to the energy balance become vanishingly small compared to the contribution from $\bar{p}dV/dt$ or $\dot{Q}$. Essentially, at the theoretical quasistatic limit
:::{math}
\frac{|\dot{W}_{\delta p}|}{\max(|\dot{Q}|,|\bar{p}\frac{dV}{dt}|)}\to 0,\qquad \frac{|\dot{W}_{\tau}|}{\max(|\dot{Q}|,|\bar{p}\frac{dV}{dt}|)}\to 0.
:::
Physically this corresponds to processes in which mechanical equilibration occurs on time scales much shorter than the time scale on which the volume-averaged thermodynamic state of the fluid evolves. Pressure disturbances are assumed to relax rapidly, leaving the pressure nearly uniform throughout the material volume. The fluid may still undergo deformation to enable a change in its overall volume, but its rate of deformation is sufficiently small for the viscous contribution to the energy balance to become negligible. Small temperature gradients may persist to enable heat transfer but the relative temperature variation throughout the bulk of the fluid remains small. Thus, the volume-averaged thermodynamic state remains close to an experimentally measurable equilibrium state. Even the gravity induced hydrostatic pressure gradient could be removed by conducting the processes in space or on the low Earth orbit. As the spatial variations in pressure, density, and temperature become negligible, their volume averages approach the corresponding uniform values. The experimentally measured equilibrium equation of state is therefore approached in the form
:::{math}
\bar{p}(t)\to p(\bar{\rho}(t),\bar{T}(t)),
:::
where $\bar{\rho}(t)$ and $\bar{T}(t)$ are the macroscopically measurable volume-averaged density and temperature
:::{math}
\bar{\rho}(t)=\frac{1}{V(t)}\int_{V(t)}\rho\,dV=\frac{m}{V(t)}, \qquad \bar{T}(t)=\frac{1}{V(t)}\int_{V(t)}T\,dV.
:::
An example process approximating the quasitatic limit is illustrated in {numref}`fig-quasistatic-process`. 
:::{figure} ./figs/fig-quasistatic-process.svg
:label: fig-quasistatic-process
:align: center
:width: 90%
Sand is slowly poured from a beaker onto the piston-like lid of a cylinder containing gas, gradually increasing the external load. Heating or cooling may be applied simultaneously. The slow loading and moderate heating or cooling allows the gas to remain close to mechanical and thermodynamical equilibrium, with nearly uniform pressure and only small spatial variations in its thermodynamic state.
::::
At the quasistatic limit, the energy balance simplifies greatly and reduces to
:::{math}
\frac{dU}{dt}=\dot{Q}-\bar{p}\frac{dV}{dt},
:::
In this form, the energy balance is referred to as the first law of thermodynamics. Since the mass of the fluid within the material is constant over time, defining the density-weighted specific internal energy over the material volume and the heat rate per unit mass into the volume with 
:::{math}
\bar{u}(t)=\frac{1}{m}\int_{V(t)}\rho u dV, \qquad \dot{\bar{q}}(t)=\frac{\dot{Q}(t)}{m},
:::
the first law can be stated also per unit mass in the form
:::{math}
:label: eq-first-law-per-unit-mass
\frac{d\bar{u}}{dt}=\dot{\bar{q}}-\bar{p}\frac{d\bar{v}}{dt}=\dot{\bar{q}}+\frac{\bar{p}}{\bar{\rho}^2}\frac{d\bar{\rho}}{dt},
:::
where $\bar{v}(t)=V(t)/m=1/\bar{\rho}(t)$ is the average specific volume. In textbooks, the first law is often presented in time-integrated form
:::{math}
\Delta U=Q-W_p,
:::
where the terms correspond to integrals between two time instants $t_0$ and $t_1$
:::{math}
\Delta U=\int_{t_0}^{t_1}\frac{dU}{dt}dt, \qquad Q=\int_{t_0}^{t_1}\dot{Q}dt, \qquad W_p=\int_{t_0}^{t_1}\bar{p}(t)\frac{dV}{dt}dt.
:::

The following sections in this chapter will discuss exclusively limiting quasistatic processes. With $\bar{\rho}$, $\bar{v}$, $\bar{T}$, $\bar{p}$, $\bar{u}$, and $\dot{\bar{q}}$ understood to denote the average fluid state, the average specific internal energy, and the specific heat rate in such processes, the explicit overbar notation will be dropped for clarity until further notice. 


::::{proof:example}
For a class of gravity-free, isotropic flows with no heat transfer, the fluid equations reduce from the spatio-temporal partial differential equations to time-dependent ordinary differential equations for spatially homogeneous fluid variables. The ratio of viscous work rate to the average-pressure work rate is then observed to be proportional to the ratio of viscous relaxation time and the macroscopic time scale of the fluid motion.
    
Assume the fluid velocity field to be isotropic and given by
:::{math}
:enumerated: false
\bm{v}(\bm{x},t)=\frac{v(t)}{L}\bm{x},
:::
with $v(t)$ a time-dependent function. Assume further density $\rho(\bm{x},t)=\bar{\rho}(t)$, temperature $T(\bm{x},t)=\bar{T}(t)$, pressure $p(\bm{x},t)=\bar{p}(t)$, and specific internal energy $u(\bm{x},t)=\bar{u}(t)$ all to be spatially homogeneous but time-dependent. Since $\nabla\cdot\bm{v}=3(v/L)$, substituting the ansatz to equation for density results in
:::{math}
:enumerated: false
\frac{1}{\rho}\frac{D\rho}{dt}=-\nabla\cdot\bm{v}\quad \implies \quad \frac{1}{\bar{\rho}}\frac{d\bar{\rho}}{dt}=-3\frac{v}{L}.
:::
Since $\nabla\bm{x}=(\nabla\bm{x})^T=\bm{I}$, one observes $\bm{D}=\bm{0}$, and the stress tensor becomes isotropic $\bm{\sigma}=(-p+3\zeta (v/L))\bm{I}$ and spatially homogeneous. Under the ansatz, the gravity-free Cauchy's momentum equation then results in
:::{math}
:enumerated: false
\rho\frac{D\bm{v}}{Dt}=\nabla\cdot\bm{\sigma} \quad \implies \quad \left(\frac{1}{L}\frac{dv}{dt}+\frac{v^2}{L^2}\right)\bm{x}=\bm{0} \quad\implies\quad \frac{dv}{dt}+\frac{v^2}{L}=0.
:::
Using the equation for density, the equation for specific internal energy then becomes
:::{math}
:enumerated: false
\rho\frac{Du}{Dt}=\bm{\sigma}:\nabla\bm{v} \quad \implies\quad \frac{d\bar{u}}{dt}=\frac{\bar{p}}{\bar{\rho}^2}\frac{d\bar{\rho}}{dt}+9\frac{\zeta}{\bar{\rho}}\frac{v^2}{L^2}
:::
The original system of partial differential equation has now been reduced to a system of ordinary differential equations. Further, the ratio of viscous work rate to the average-pressure work rate now becomes
:::{math}
:enumerated: false
\frac{|\dot{W}_{\tau}|}{|\bar{p}\,dV/dt|}=3\frac{\zeta}{\bar{p}}\frac{|v|}{L}\sim \frac{t_\text{viscous}}{t_\text{macro}},
:::
where $t_\text{vicous}\sim \zeta/\bar{p}$ is a characteristic viscous time scale for the problem and $t_\text{macro}\sim L/|v|$ is the time scale associated with the macroscopic motion of the fluid. As long as the macroscopic time scale is much longer than the viscous time scale, the viscous work rate can be neglected, leading to a quasistatic limiting description of the fluid.
::::



## <span class="elementary"></span> Specific heats and heat rate in quasistatic processes
The second step in the process of establishing a relation between the specific internal energy and the state variables involves experimentally relating the specific heat rate $\dot{q}$ to the volume averaged fluid state variables. In that case, the entire right side of the first law {numref}`eq-first-law-per-unit-mass` becomes free of the details of fluid motion, at the quasistatic limit. More specifically, experiments with fluids restricted to single phase states that approximate quasistatic processes show that the specific heat rate can be well approximated by a linear expression in the rates of change of the state variables. At the quasistatic limit this experimental observation from approximate quasistatic processes is then assumed to hold accurately. Ultimately, the observation enables a lift-off from the temporal realm and construction of a thermodynamic theory framework.

To formalize the idea, define a general single-phase quasistatic process in the space of state variables, represented in terms of the pair $(\rho,T)$, $(T,p)$, or $(\rho,p)$, over a time interval $t\in[t_0,t_1]$ as the curve
:::{math}
t\mapsto c(t)=\left\{\begin{aligned}
&(\rho(t),T(t))\\
&(T(t),p(t))\\
&(\rho(t),p(t))
\end{aligned}\right..
:::
Only two of the state variables are ever needed to define the state and the curve $c(t)$ in single phase since the equation of state provides the third. Such a process can be visualized by drawing a curve in a $v$-$T$ or $p$-$v$ diagram and letting the time variable $t$ serve as the path parameter. 

Along such quasistatic process curves, there are three different representations for the specific heat rate that remain linear in the rates of change of the state variables
:::{math}
:label: eq-dot-q-initial-representations
\dot{q}=\left\{\begin{aligned}
&q_{T,\rho}(T,\rho)\frac{dT}{dt}+q_{\rho,T}(T,\rho)\frac{d\rho}{dt},\\
&q_{T,p}(T,p)\frac{dT}{dt}+q_{p,T}(T,p)\frac{dp}{dt},\\
&q_{\rho,p}(\rho,p)\frac{d\rho}{dt}+q_{p,\rho}(\rho,p)\frac{dp}{dt}.
\end{aligned}\right.
:::
The reason again is the equation of state that determines the time rate of change the third variable in terms of the time rates of change of the other two state variables. Differentiating an equation of state $\rho(p,T)$ with respect to time and using the isobaric thermal expansion coefficient $\beta_p$ and the isothermal compression coefficient $\kappa_T$ as in {numref}`eq-dv-pT-differential` leads to a relation between the time derivatives of the state variables
:::{math}
:label: eq-differential-equation-of-state
\frac{1}{\rho}\frac{d\rho}{dt}=-\beta_p\frac{dT}{dt}+\kappa_T\frac{dp}{dt}.
:::
Therefore for example 
:::{math}
\begin{aligned}
q_{T,\rho}\frac{dT}{dt}+q_{\rho,T}\frac{d\rho}{dt}&=q_{T,\rho}\frac{dT}{dt}+\rho q_{\rho,T}\frac{1}{\rho}\frac{d\rho}{dt}\\
&=q_{T,\rho}\frac{dT}{dt}+\rho q_{\rho,T}\left(-\beta_p\frac{dT}{dt}+\kappa_T\frac{dp}{dt}\right)\\
&=\underbrace{(q_{T,\rho}-\rho q_{\rho,T}\beta_p)}_{=q_{T,p}}\frac{dT}{dt}+\underbrace{\rho q_{\rho,T}\kappa_T}_{=q_{p,T}}\frac{dp}{dt}.
\end{aligned}
:::
This shows that the coefficient functions appearing in the different representations {numref}`eq-dot-q-initial-representations` for the specific heat rate are related through the equation of state. Overall, one finds the relations
:::{math}
:label: eq-q-Tprho-relations
\begin{aligned}
q_{T,p}&=q_{T,\rho}-\rho\beta_p q_{\rho,T}=-\rho\beta_p q_{\rho,p},\\
q_{p,T}&=\rho\kappa_T q_{\rho,T}=q_{p,\rho}+\rho\kappa_T q_{\rho,p}.
\end{aligned}
:::

Understanding how a specific heat rate linear in the rates of state variables can generally appear, one may then inspect specific quasistatic processes. A quasistatic heating process that keeps the density $\rho$ (and the specific volume $v$) constant over time is most conveniently described with the curve $c(t)=(\rho,T(t))$ and illustrated in {numref}`fig-quasistatic-heating-isochoric`. In such case, the experimentally measurable response of the fluid to the heat it receives reduces to
:::{math}
\dot{q}=q_{T,\rho}\frac{dT}{dt}.
:::
Under such processes, the ratio of the measured heat rate per unit mass to the measured rate of temperature change is referred to as isochoric specific heat $c_v(\rho,T)$, meaning $q_{T,\rho}=c_v$. If the pressure $p$ in a quasistatic heating process is kept constant instead of density,  as in {numref}`fig-quasistatic-heating-isobaric`, the most convenient curve for the process description is $c(t)=(p,T(t))$. In such case, the experimentally measurable response of the fluid to the heat it receives then reduces to
:::{math}
\dot{q}=q_{T,p}\frac{dT}{dt}.
:::
In such case, the ratio of the measured heat rate per unit mass to the measured rate of temperature change is referred to as isobaric specific heat $c_p(\rho,T)$, meaning $q_{T,p}=c_p$. 

::::{figure}
:label: fig-quasistatic-heating
:align: center
:width: 100%

(fig-quasistatic-heating-isochoric)=
:::{image} ./figs/fig-quasistatic-heating-isochoric.svg
:alt: Isochoric quasistatic heating process.
:width: 80%
:::

(fig-quasistatic-heating-isobaric)=
:::{image} ./figs/fig-quasistatic-heating-isobaric.svg
:alt: Isobaric quasistatic heating process.
:width: 80%
:::

Two common quasistatic heating processes. In an isochoric process, the volume is constant. In an isobaric process, pressure remains constant instead.
::::

With $q_{T,\rho}=c_v$ and $q_{T,p}=c_p$ inferred from measurements, the equations {numref}`eq-q-Tprho-relations` then provide the rest of the proportionality coefficients, and the response of the fluid to the heat it receives in a quasistatic process while remaining in single phase can be expressed as
:::{math}
:label: eq-dot-q-expressions}
\dot{q}=\left\{\begin{aligned}
&c_v\frac{dT}{dt}+\frac{c_v-c_p}{\rho\beta_p}\frac{d\rho}{dt},\\
&c_p\frac{dT}{dt}+(c_v-c_p)\frac{\kappa_T}{\beta_p}\frac{dp}{dt},\\
&-\frac{c_p}{\rho\beta_p}\frac{d\rho}{dt}+c_v\frac{\kappa_T}{\beta_p}\frac{dp}{dt}.
\end{aligned}\right.
:::

The specific heats $c_v$ and $c_p$ for water are illustrated in {numref}`fig-cv-cp-H2O`, and one recognizes the isocontours of both $c_v$ and $c_p$ to be almost perfectly vertical in a region where temperature is high enough and water vapor is dilute enough (low density, high specific volume). This indicates that the specific heats in the ideal gas region approximately depend on temperature only. For gases, this is a commonly used approximation, and often even a constant value is sufficient over a large temperature range. The specific heats can be computed with both pyromat and coolprop libraries, and only in the single-phase regions. They are not defined in the phase-change regions.

::::{figure}
:label: fig-cv-cp-H2O
:align: center
:width: 100%

(fig-cv-H2O)=
:::{image} ./figs/fig-cv-H2O.svg
:alt: Isochoric specific heat for water.
:width: 80%
:::

(fig-cp-H2O)=
:::{image} ./figs/fig-cp-H2O.svg
:alt: Isobaric specific heat for water.
:width: 80%
:::

Isocontours of specific heats $c_v$ and $c_p$ for water in a $v$-$T$ diagram.
::::

::::{proof:example}
The specific heats can be computed with both the pyromat and coolprop libraries. The script below serves as a demonstration:
```{literalinclude} python/example-cv-cp-evaluation.py
:language: python
:start-line: 0
:end-line: 35
:linenos:
```
At the requested state poin both pyromat and coolprop return $c_v=2.23\,\text{kJ}/\text{kg}/\text{K}$ and $c_p=4.00\,\text{kJ}/\text{kg}/\text{K}$. The values can be confirmed from {numref}`fig-cv-cp-H2O`.
::::
