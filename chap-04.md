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

## <span class="elementary"></span> Energy balance between two equilibrium states and the first law
As the first step in the process of uncovering the thermodynamic framework, one investigates the time integral of the total energy balance {numref}`eq-total-energy-balance-material-volume` over a material volume from one spatially homogenous stationary equilibrium state to another. Between the initial and final states, heating or cooling of the volume is allowed. The fluid may also move in complicated patterns inside the volume, but the movement of the volume boundary is controlled by a specifically tailored external force. A relation is then discovered that associates the change in fluid's specific internal energy to the heat applied per unit mass and the changes in the state variables. In this analysis, gravitational acceleration is omitted to allow formation of spatially homogenous equilibrium states. If necessary, experiments could be conducted in space to suppress gravitational effects on equilibrium states. 

For flow processes within a material volume $V(t)$ from one homogenous stationary equilibrium state at time $t_0$ to another at time $t_1$, denote with $U(t)$ and $KE(t)$ the instantaneous total internal and kinetic energies
:::{math}
U(t)=\int_{V(t)}\rho u dV, \qquad KE(t)=\int_{V(t)}\frac{1}{2}\rho|\bm{v}|^2dV.
:::
Denote with $\dot{Q}(t)$ and $Q$ the instantaneous heat rate and the total heat applied to the volume over the interval $t\in[t_0,t_1]$
:::{math}
\dot{Q}(t)=\int_{\partial V(t)}(-\bm{q})\cdot\bm{\hat{n}}dA+\int_{V(t)}q_VdV, \qquad Q=\int_{t_0}^{t_1}\dot{Q}dt,
:::
and with $\dot{W}(t)$ and $W$ the instantaneous mechanical contact work rate and the total contact work performed by the fluid over the same time interval
:::{math}
\dot{W}(t)=-\int_{\partial V(t)}\bm{v}\cdot\delta\bm{F}_s=-\int_{\partial V(t)}\bm{v}\cdot\bm{t}dA, \qquad W=\int_{t_0}^{t_1}\dot{W}dt.
:::
While the differential surface force $\delta\bm{F}_s$ is exerted onto the fluid, the minus sign in the work rate $\dot{W}$ accounts for the work the fluid does against the exerted force. In the absence of gravity, the total energy balance {numref}`eq-total-energy-balance-material-volume`, when integrated over the time interval $t\in[t_0,t_1]$, then provides
:::{math}
:label: eq-first-law-macroscopic
\Delta U=Q-W,
:::
where $\Delta U=U(t_1)-U(t_0)$ is the change in the total internal energy of the material volume. The change in the total kinetic energy $\Delta KE=KE(t_1)-KE(t_0)=0$ vanishes for the fluid is assumed to be at rest both in the initial and final equilibrium states. In literature, the equation {numref}`eq-first-law-macroscopic` is often referred to as the first law of thermodynamics in closed systems with varying interpretations. Here the equation is strictly used to describe energy conservation in the absence of gravitational effects between two homogenous equilibrium states that are at rest.

Consider then two experiments illustrated in {numref}`fig-heating-cylinder`. A fluid is confined in a cylinder with a movable piston. Initially, at time $t_0$, the fluid is at rest and in a thermodynamic equilibrium state with spatially homogenous temperature and pressure. The external force needed to maintain the piston in place corresponds to the equilibrium pressure of the fluid. Heating (or cooling) is then applied at the fluid boundary which causes temperature gradients to develop in the fluid. Through local thermal expansion (or shrinking), density gradients form, the fluid begins to move a little, and small pressure gradients develop. Depending on whether the external force is adjusted over time or not, the piston may stay in place as in {numref}`fig-heating-cylinder-constant-v` or move as in {numref}`fig-heating-cylinder-constant-p`. Once heat is turned off the fluid begins to settle as viscous effects and heat conductivity locally turn velocity and temperature gradients into internal energy, until a new spatially homogenous equilibrium state is reached at some later time $t_1$.
::::{figure}
:label: fig-heating-cylinder
:align: center
:width: 100%

(fig-heating-cylinder-constant-v)=
:::{image} ./figs/fig-heating-cylinder-constant-v.svg
:alt: Cylinder volume kept constant. The external force to keep the piston in place varies over time.
:width: 90%
:::

(fig-heating-cylinder-constant-p)=
:::{image} ./figs/fig-heating-cylinder-constant-p.svg
:alt: Cylinder volume is allowed to change. The external force to the piston remains constant.
:width: 90%
:::

Heating a substance in a cylinder. The initial and final states of the substance at times $t_0$ and $t_1$ are stationary and homogenous equilibrium states. Between the initial and final states, the substance is not necessarily in thermodynamical or mechanical equilibrium but can move and have spatially variying properties.
::::


On solid surfaces, the fluid velocity $\bm{v}|_{\partial V(t)}$ matches the surface velocity. If the external force $F(t)$ exerted onto the piston is carefully adjusted to exactly match the surface force the fluid exerts to the piston as in {numref}`fig-heating-cylinder-constant-v`, no net force is applied to the piston and it will not move. In such case the surface velocity of the fluid is zero at all times and the fluid performs no work. The energy balance between the initial and final equilibrium states then reduces to
:::{math}
:label: eq-delta-U-constant-V
(\Delta U)_{v_0}=(Q)_{v_0},
:::
where the notation $(\cdot)_{v}$ refers to a flow process where the average specific volume over the material volume remains constant (both mass and total volume remain fixed). The result implies that all of the heat applied is converted into fluid's internal energy in a constant volume. If the external force does not match the surface force, the piston experience a non-zero net force and begins to move. Consequently, the part of the fluid's surface touching the piston moves as well. On the piston surface, the fluid velocity is therefore $\bm{v}|_{A_p}=v_p\bm{\hat{z}}$ where $v_p(t)$ denotes the velocity of the piston with respect to the cylinder axis of orientation. Neither the work rate $\dot{W}(t)$ nor the total work $W$ the fluid does remain zero then. 

To relate the work the fluid does to the external force, one uses Newton's second law, according to which the piston velocity $v_p$ satisfies the differential equation
:::{math}
m_p\underbrace{\frac{dv_p}{dt}}_{\substack{\text{Piston}\\\text{accele-}\\\text{ration}}}=\overbrace{-\bm{\hat{z}}\cdot\underbrace{\int_{A_p(t)}\bm{t}dA}_{\substack{\text{Contact force}\\\text{exerted by}\\\text{the piston}\\\text{to the fluid}}}}^{\substack{\text{Component of the}\\\text{contact force exerted}\\\text{by the fluid to the}\\\text{piston into the direction}\\\text{of the piston movement}}}-F.
:::
A change in the kinetic energy of the piston over the interval $t\in[t_0,t_1]$ then becomes
:::{math}
\begin{aligned}
\frac{m_p}{2}\left(v_{p,1}^2-v_{p,0}^2\right)&=\int_{t_0}^{t_1}m_p\frac{dv_p}{dt}v_pdt=\int_{t_0}^{t_1}\left[-\bm{\hat{z}}\cdot\int_{A_p(t)}\bm{t}dA-F\right]v_pdt\\
&=-\int_{t_0}^{t_1}\int_{A_p(t)}\bm{v}\cdot\bm{t}dAdt-\int_{t_0}^{t_1}Fv_pdt,
\end{aligned}
:::
where the condition $\bm{v}|_{A_p}=v_p\bm{\hat{z}}$ for the fluid velocity at the piston boundary was used. Since the piston velocity at the beginning and at the end is zero, the change in its kinetic energy over the interval $t\in[t_0,t_1]$ vanishes. Consequently
:::{math}
\int_{t_0}^{t_1}Fv_pdt=-\int_{t_0}^{t_1}\int_{A_p(t)}\bm{v}\cdot\bm{t}dAdt=W.
:::
If the external force, throughout the interval $t\in[t_0,t_1]$, equals the force from the initial fluid equilibrium pressure, then 
:::{math}
F(t)=p_0A_p \quad \implies \quad \int_{t_0}^{t_1}Fv_pdt=p_0A_p\int_{t_0}^{t_1}v_pdt=p_0(V_1-V_0).
:::
The change in the fluids internal energy then equals 
:::{math}
:label: eq-delta-U-constant-p
(\Delta U)_{p_0}=(Q)_{p_0}-p_0(\Delta V)_{p_0}, 
:::
where the notation $(\cdot)_p$ refers to a process between two equilibrium states against a constant external force that equals the force from fluid's initial and final equilibrium pressure. In such process, the applied heat is divided between a change in the internal energy and volumetric expansion work against constant external pressure.

The initial and final states in the expreriments illustrated in {numref}`fig-heating-cylinder` are spatially homogenous equilibrium states, and the experiments can be carried out for arbitrary amounts of fluid mass. A homogenous macroscopic volume in thermal equilibrium one may describe in terms of intensive quantities as well. Defining heat added per unit mass as $q=Q/m$, the results from the two experiments can therefore be summarized as
:::{math}
:label: eq-delta-u-specific-constant-v-p
\begin{aligned}
(\Delta u)_v&=(q)_v,\\
(\Delta u)_p&=(q)_p-p(\Delta v)_p.
\end{aligned}
:::
Although the the experiment leading to these results was conducted specifically using a cylinder and a piston, the result applies to arbitrary geometries. General requirement is that the expansion happens against a constant external pressure which is required to match the initial equilibrium pressure of the fluid.

General flow processes between two equilibrium states do not happen at constant volume or against a constant external pressure. Instead, both volume and pressure of the final equilibrium state can differ from the initial state values. Nevertheless, the changes in the state quantities between two general equilibrium states can be constructed from the changes in sequential processes that happen at constant volume and against constant external pressure. To understand this, consider a general heating process between two equlibrium states
:::{math}
\begin{pmatrix}
T\\
p\\
v\\
u
\end{pmatrix} \underset{q}{\to} 
\begin{pmatrix}
T+\Delta T\\
p+\Delta p\\
v+\Delta v\\
u+\Delta u
\end{pmatrix}.
:::
Construct then a two-stage process that first heats the substance so that the external pressure is constant, and then heats the substance at constant volume
:::{math}
\begin{pmatrix}
T\\
p\\
v\\
u
\end{pmatrix}
\underset{(q)_p}{\to}
\begin{pmatrix}
T+(\Delta T)_p\\
p\\
v+(\Delta v)_p\\
u+(\Delta u)_p
\end{pmatrix}
\underset{(q)_{v+\Delta v}}{\to}
\begin{pmatrix}
T+(\Delta T)_p+(\Delta T)_{v+\Delta v}\\
p+(\Delta p)_{v+\Delta v}\\
v+(\Delta v)_p\\
u+(\Delta u)_p+(\Delta u)_{v+\Delta v}
\end{pmatrix}
:::

For the two-stage process to end up in the same state as the one-stage process, the total changes in the temperature and specific internal energy must satisfy
:::{math}
\begin{aligned}
\Delta T&=(\Delta T)_{v+\Delta v}+(\Delta T)_p,\\
\Delta u&=(\Delta u)_{v+\Delta v}+(\Delta u)_p,
\end{aligned}
:::
while $(\Delta p)_{v+\Delta v}=\Delta p$ and $(\Delta v)_{p}=\Delta v$. The total change in the specific internal energy can then be manipulated into
:::{math}
\begin{aligned}
\Delta u&=\frac{(\Delta u)_{v+\Delta v}}{(\Delta T)_{v+\Delta v}}(\Delta T)_{v+\Delta v}+\frac{(\Delta u)_p}{(\Delta T)_p}(\Delta T)_p\\
&=\frac{(\Delta u)_{v+\Delta v}}{(\Delta T)_{v+\Delta v}}\Delta T+\left[\frac{(\Delta u)_p}{(\Delta T)_p}-\frac{(\Delta u)_{v+\Delta v}}{(\Delta T)_{v+\Delta v}}\right]\frac{(\Delta T)_p}{(\Delta v)_p}\Delta v.
\end{aligned}
:::
Substituting {numref}`eq-delta-u-specific-constant-v-p`, one finds an expression for the change in the specific internal energy in a general process that is proportional to the changes in the temperature and the specific volume
:::{math}
:label: eq-delta-u-delta-T-delta-v
\Delta u=\frac{(q)_{v+\Delta v}}{(\Delta T)_{v+\Delta v}}\Delta T+\left[\left(\frac{(q)_p}{(\Delta T)_p}-\frac{(q)_{v+\Delta v}}{(\Delta T)_{v+\Delta v}}\right)\frac{(\Delta T)_p}{(\Delta v)_p}-p\right]\Delta v.
:::
This is the first clue that changes in specific internal energy between two equilibrium states could potentially be related purely to the fluid's state variables and changes in them. 

## <span class="elementary"></span> Specific heats
The second step towards the thermodynamics framework involves relating the heat applied during a process from one equilibrium state to another to the state variables and the changes in them. This is achieved with quantities referred to as specific heats.

When pure water is heated at constant volume as in {numref}`fig-heating-cylinder-constant-v` from one equilibrium state to another, the temperature is observed to change as shown in {numref}`fig-heat-delta-T-isochoric`. Starting from the triple line $T=0.01^\circ\text{C}$ at the saturated liquid state ($v=0.001\,\text{m}^3/\text{kg}$), the temperature of the liquid water begins to increase in reaction to the added heat per unit mass. If the starting point for heating is shifted from the saturated liquid state towards the saturated vapor end of the triple line ($v=206\,\text{m}^3/\text{kg}$), the behaviour differs. The curve behaves first smoothly, then a sharp turn appears, after which the curve behaves smoothly again. The initial state for such curves lies in the liquid-vapor two-phase region, and the change in the curve behaviour corresponds to crossing either the saturated liquid or saturated vapor curve into the single phase region. Similar behaviour is observed for other pure substances as well.

::::{figure} ./figs/fig-heat-delta-T-isochoric.svg
:label: fig-heat-delta-T-isochoric
:align: center
:width: 100%
Water temperature when heated from temperature of $T=0.01^\circ\text{C}$ through subsequent equilibrium states close to each other that all share the same volume.
::::

If pure water is heated as in {numref}`fig-heating-cylinder-constant-p` instead, from one equilibrium state to another against a constant external pressure, the temperature response to the applied heat per unit mass differs. As shown in {numref}`fig-heat-delta-T-isobaric`, for pressure values below that of the critical point, the temperature first increases as heat is added but then suddenly flattens out completely, before continuing to rise again. For pressure values above that of the critical point, the curve rises constantly instead, with no flat segment. The part of the curve before the flat segment corresponds to temperature rise in the liquid phase, the flat segment to the phase change from saturated liquid to saturated vapor that happens at constant temperature and pressure, and the rising curve after the flat segment to temperature rise in gaseous phase.

::::{figure} ./figs/fig-heat-delta-T-isobaric.svg
:label: fig-heat-delta-T-isobaric
:align: center
:width: 100%
Water temperature when heated from $T=0.01^\circ\text{C}$ through subsequent equilibrium states with constant pressure.
::::

::::{proof:example}
From {numref}`fig-heat-delta-T-isobaric` one may observe that it requires approximately $420\,\text{kJ}$ of heat to increase the temperature of $1\,\text{kg}$ of liquid water from $0^\circ\text{C}$ to $100^\circ\text{C}$ at a pressure of $1\,\text{bar}$. After the temperature of $100^\circ\text{C}$ has been achieved, boiling the $1\,\text{kg}$ of water then takes approximately an additional $2260\,\text{kJ}$ of heat. 
::::

The temperature rise between two equilibrium states in single phase, either at common volume or against a constant external pressure, is characterized by the local slope of the curves in {numref}`fig-heat-delta-T-isochoric` and {numref}`fig-heat-delta-T-isobaric`. It is appealing to consider the heat per unit mass one needs to increase the temperature of a substance by one Kelvin, and the response to heating is therefore described with the inverse of the local slope, which defines the specific heats
:::{math}
:label: eq-specific-heats-definitions
\begin{aligned}
c_v&=\lim_{(\Delta T)_v\to 0}\frac{(q)_v}{(\Delta T)_v},\\
c_p&=\lim_{(\Delta T)_p\to 0}\frac{(q)_p}{(\Delta T)_p}.
\end{aligned}
:::
Since the slopes of the curves in {numref}`fig-heat-delta-T-isochoric` and {numref}`fig-heat-delta-T-isobaric` are not constant, both $c_v$ and $c_p$ are functions of the fluid's thermodynamic state. They describe the heat required per unit temperature change under the specified constraint, and are not defined in the phase-change regions. 

For water, the specific heats $c_v$ and $c_p$ are illustrated in {numref}`fig-cv-cp-H2O`. One recognizes the isocontours of both $c_v$ and $c_p$ to be almost perfectly vertical in a region where temperature is high enough and water vapor is dilute enough (low density, high specific volume). This indicates that the specific heats in the ideal gas region approximately depend on temperature only. For gases, this is a commonly used approximation, and often even a constant value is sufficient over a large temperature range. The accurate values of the specific heats can be computed with both pyromat and coolprop libraries.

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


## <span class="elementary"></span> Quasistatic processes and preliminary differential forms for specific internal energy and heat
The equation {numref}`eq-delta-u-delta-T-delta-v` for the change in the specific internal energy between two stationary homogenous equilibrium states involves changes in the state variables but also ratios of the heat applied per unit mass to the corresponding two-stage temperature changes. The specific heats {numref}`eq-specific-heats-definitions` that characterize these ratios are defined as limits at which the temperature changes vanish. The third step towards the thermodynamic framework resolves this conflict by constructing the finite change in the specific internal energy between two equilibrium states as a sum of many small changes between sequential equilibrium states that are close to each other. In the limit where the small changes shrink to infinitesimal ones, and their number grows towards infinity, the sequential equilibrium states form a continuous path through the thermodynamic manifold of equilibrium states, and the finite change in the specific internal energy becomes a path integral. Consequently, preliminary differential forms for the specific internal energy and heat are introduced. Later, the preliminary differential form for heat enables the discovery of entropy and the development of the thermodynamic framework.

Assume that a material volume of fluid is subjected to a sequence of changes that all start and end up in stationary and homogenous equilibrium states that are close to each other. 
:::{math}
\begin{pmatrix}
T_0\\
p_0\\
v_0\\
u_0
\end{pmatrix} \underset{q_0}{\to} \dots \underset{q_{i-1}}{\to}
\begin{pmatrix}
T_i\\
p_i\\
v_i\\
u_i
\end{pmatrix}
\underset{q_{i}}{\to}
\begin{pmatrix}
T_{i+1}\\
p_{i+1}\\
v_{i+1}\\
u_{i+1}
\end{pmatrix}
\underset{q_{i+1}}{\to} \dots \underset{q_{N-1}}{\to}
\begin{pmatrix}
T_N\\
p_N\\
v_N\\
u_N
\end{pmatrix}
:::
Let the process between two sequential states $i$ and $i+1$ be contain two stages, the first a process against a constant external pressure and the second a process at constant volume
:::{math}
\begin{pmatrix}
T_i\\
p_i\\
v_i\\
u_i
\end{pmatrix}
\underset{(q)_{p_i}}{\to}
\begin{pmatrix}
T_i+(\Delta T)_{p_i}\\
p_i\\
v_i+(\Delta v)_{p_i}\\
u_i+(\Delta u)_{p_i}
\end{pmatrix}
\underset{(q)_{v_i+\Delta v_i}}{\to}
\begin{pmatrix}
T_i+(\Delta T)_{p_i}+(\Delta T)_{v_i+\Delta v_i}\\
p_i+(\Delta p)_{v_i+\Delta v_i}\\
v_i+(\Delta v)_{p_i}\\
u_i+(\Delta u)_{p_i}+(\Delta u)_{v_i+\Delta v_i}
\end{pmatrix}
=
\begin{pmatrix}
T_{i+1}\\
p_{i+1}\\
v_{i+1}\\
u_{i+1}
\end{pmatrix}.
:::
The total changes in temperature and specific internal energy are sums of the changes between the subsequent states
:::{math}
\begin{aligned}
\Delta T&=\sum_{i=0}^{N-1}\Delta T_i=\sum_{i=0}^{N-1}\left[(\Delta T)_{v_i+\Delta v_i}+(\Delta T)_{p_i}\right]\\
\Delta u&=\sum_{i=0}^{N-1}\Delta u_i=\sum_{i=0}^{N-1}\left[(\Delta u)_{v_i+\Delta v_i}+(\Delta u)_{p_i}\right]
\end{aligned}
:::
and the changes is pressure and specific between each state satisfy
:::{math}
\begin{aligned}
(\Delta v)_{p_i}&=\Delta v_i,\\
(\Delta p)_{v_i+\Delta v_i}&=\Delta p_i.
\end{aligned}
:::
One may then apply equation {numref}`eq-delta-u-delta-T-delta-v` for each process from state $i$ to state $i+1$, and the total change in the specific internal energy can be written
:::{math}
\begin{aligned}
\Delta u&=\sum_{i=1}^{N-1}\Bigg(\frac{(q)_{v_i+\Delta v_i}}{(\Delta T)_{v_i+\Delta v_i}}\Delta T_i\\
&\quad+\left[\left(\frac{(q)_{p_i}}{(\Delta T)_{p_i}}-\frac{(q)_{v_i+\Delta v_i}}{(\Delta T)_{v_i+\Delta v_i}}\right)\frac{(\Delta T)_{p_i}}{(\Delta v)_{p_i}}-p_i\right]\Delta v_i\Bigg)
\end{aligned}
:::
At the limit where the number of sequential equilibrium states $N\to \infty$ grows to infinity, the changes $(\Delta T)_{p_i}\to 0$, $(\Delta T)_{v_i+\Delta v_i}\to 0$, $\Delta v_i$ all become infinitesimal. Consequently
:::{math}
\begin{aligned}
\frac{(q)_{p_i}}{(\Delta T)_{p_i}}&\to c_p, 
&\frac{(q)_{v_i+\Delta v_i}}{(\Delta T)_{v_i+\Delta v_i}}, &\to c_v, 
&\frac{(\Delta T)_{p_i}}{(\Delta v)_{p_i}}&\to\left(\frac{\partial T}{\partial v}\right)_p
\end{aligned}
:::
The sum of the changes in the state variables nevertheless remain finite. Consequently, the change in the internal energy become a path integral over a curve $C(t)\mapsto(p(t),T(t),v(t))$ that describes a path in the thermodynamic state variable space solely trough equilibrium states.
:::{math}
\Delta u\to \int_C\left[c_vdT+\left((c_p-c_v)\left(\frac{\partial T}{\partial v}\right)_p-p\right)dv\right] 
:::
:::{math}
\begin{aligned}
\Delta p&\to \int_C dp\\
\Delta T&\to \int_C dT\\
\Delta v&\to \int_C dv\\
\end{aligned}
:::
In thermodynamics, such process is referred to as quasistatic. No real quasistatic processes exist in reality, though. An example that approximates such process is illustrated in {numref}`fig-quasistatic-process`.
:::{figure} ./figs/fig-quasistatic-process.svg
:label: fig-quasistatic-process
:align: center
:width: 90%
Sand is slowly poured from a beaker onto the piston-like lid of a cylinder containing a substance, gradually increasing the external load. Heating or cooling may be applied simultaneously. The slow loading and moderate heating or cooling allows the substance to remain close to mechanical and thermodynamical equilibrium at all times, with nearly uniform pressure and only small spatial variations in its thermodynamic state.
::::






