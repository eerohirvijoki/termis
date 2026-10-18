# Introduction
This chapter first discusses how macroscopic matter is built from its microscopic constituents and how it interacts with its surroundings. The discussion leads to the concepts of internal energy and equilibrium state, to the definitions for different boundary types, and to concepts of heat and work. Here, these concepts are introduced without any equations. Later, mathematics will provide the language for quantitative interpretation of the same ideas. The chapter then proceeds to describe the state variables that are needed for the macroscopic description of matter. While doing so, the zeroth law of thermodynamics is encountered, providing an interpretation for temperature. Before closing, the chapter briefly discusses how description for the motion of matter can take two different viewpoints, setting the premise for later analysis of fluid motion. Finally, a roadmap to these notes is provided, together with a brief discussion on how thermodynamics and continuum mechanics are positioned with respect to each other. 

## Learning goals

Below one may find the learning goals for this chapter. Majority of the goals are chosen to support the core path, indicated in <span class="elementary"></span>-color:

- <span class="elementary"></span> The reader recognizes the microscopic origin of internal energy.
- <span class="elementary"></span> The reader differentiates a thermal equilibrium state from a non-equilibrium state.
- <span class="elementary"></span> The reader recognizes heat and work as energy in transfer and differentiates between the two.
- <span class="elementary"></span> The reader lists the different boundary types a system can have, and classifies interaction of systems with their surroundings with the help of the boundary types.
- <span class="elementary"></span> The reader is able to convert between the different volume-variable variants (density, specific volume, molar volume).
- <span class="elementary"></span> The reader provides an interpretation for pressure.

- <span class="elementary"></span> The reader recalls the zeroth law of thermodynamics
- <span class="elementary"></span> The reader uses a gas thermometer to estimate temperature with respect to a reference temperature.

In addition, one intermediate and one advanced goal are included to prepare also the readers interested in progressing beyond the core topics:

- <span class="intermediate"></span> The reader recognizes the difference between pressure and stress.
- <span class="advanced"></span> The reader differentiates between the Eulerian rate of change of velocity and the material (Lagrangian) rate of change of velocity for a flow.


## <span class="elementary"></span> Internal energy and equilibrium state 
Under close inspection, ordinary matter is observed to consist of particles such as atoms, molecules, and ions. All of these particles interact through forces that have origins in the Coulomb interactions between their charged constituents, namely electrons and nuclei. Even when particles carry no net electric charge, the internal distribution of positive and negative charge gives rise to effective interactions that can be attractive at moderate separations and strongly repulsive at very short separations. As a result, the interaction between two individual particles can be understood as a consequence of potential energy that has a minimum at a characteristic distance.

For a collection of particles, the collective effect of different interaction strengths and geometries leads to different macroscopic states. In a solid, particles typically reside close to each other and their preferred separations vibrating about equilibrium positions. In a liquid, particles reside close together and near their preferred separations but continually rearrange over time. In a gas, the average separation is large and interactions are weak except when particles briefly pass each other close by in an event that can be described as an instantaneous collision. For an illustration, the sketches in {numref}`fig-water-solid-liquid-vapor-molecules` show collections of water particles in various configurations. The macroscopic state of matter is therefore governed by a competition between the interparticle potential energy, which favours certain separations and arrangements, and the kinetic energy of the particles, which includes contributions from translational, rotational, and vibrational motion. The microscopic kinetic and interaction potential energies of the particles, excluding the center-of-mass kinetic energy, gravitational energy, and nuclear binding energy, are referred to as internal energy. In these notes, the symbol reserved to denote internal energy of a collection of particles is $U$. 

:::::{figure}
:label: fig-water-solid-liquid-vapor-molecules
:align: center
:class: my-subfigures grid grid-cols-5 items-end gap-2 

(water-solid)=
![Solid water](./figs/fig-water-frozen.png)

(water-melting)=
![Melting water](./figs/fig-water-melting.png)

(water-liquid)=
![Liquid water](./figs/fig-water-liquid.png)

(water-evaporating)=
![Evaporating water](./figs/fig-water-evaporating.png)

(water-gas)=
![Gaseous water](./figs/fig-water-gaseous.png)

Water in different configurations, with hydrogen bonds illustrated (cyan dashed lines).
:::::

As the motion of the particles in classical sense is governed by Newton's laws, the particles continually exchange energy and momentum through their interactions, the forces between them. A collection of particles is said to be in a thermodynamic equilibrium state when this exchange has led to a distribution of energies and configurations that appears time-independent when averaged over a short period of time. Although individual particles continue to move, interact, and exchange energy and momentum, the overall distribution of energies and configurations in an equilibrium state remains approximately steady in time. As the internal energy of a system describes the total kinetic and interaction potential energy in the system's rest frame, not the details of how the energy is distributed between the particles, it is defined for both equilibrium and non-equilibrium systems.


## <span class="elementary"></span> Boundary types, heat, and work
Consider two collections of particles, each of which has settled into its own equilibrium state. Regard each such collection as a system. A boundary between systems is any surface that separates them and determines the mechanisms by which energy can be transferred between the systems.

A diathermal boundary allows energy to be transferred in a way that can change the energy or configuration distributions of the particles within systems, without requiring macroscopic motion of the boundary in system's rest frame. When two systems are separated by a diathermal boundary, they are said to be in thermal contact. Typical examples include two solid objects touching each other, a thin metal wall separating two volumes of liquid, and a solid object surrounded by air or liquid water. The portion of net energy transfer across a diathermal boundary that is mediated by microscopic motion of particles is referred to as heat. Heat therefore describes energy in transfer and is not a property contained within a system. Energy transfer across a diathermal boundary can be mediated also by, e.g, electromagnetic fields. By contrast, an adiabatic boundary prevents all energy transfer that would alter the energy or configuration distributions of the particles within the systems without macroscopic motion of the boundary between them. Practical examples include thick insulation, vacuum gaps, Faraday cages, or thin highly reflective material layers.

When two systems are separated by a movable boundary, they are said to be in mechanical contact. A typical example is a movable piston in a cylinder that separates the volume of gas inside the cylinder chamber from the outsides of it. By contrast, a stationary rigid boundary does not move, preventing mechanical contact. The energy transferred across a mechanical contact through macroscopic motion of the boundary is referred to as mechanical work. Like heat, mechanical work is energy in transfer and is not a property contained within a system.

In general, work is any energy transfer across a boundary that is not heat, including mechanical and electromagnetic field work. A boundary can also combine different types, allowing both heat and work to be exchanged, or neither.


## <span class="elementary"></span> Density, specific volume, and molar volume
A macroscopic description of matter should be consistent with experimental observations while remaining as simple as possible and expressible in terms of a small number of variables. Although the state of matter is determined from the microscopic energy and configuration distributions, a macroscopic description should not depend on the detailed positions and motions of individual particles, but instead capture their collective effect.

As the forces between particles depend strongly on the distances between them, and the motion of each particle in response to these forces depends on its mass, the macroscopic state of matter can be expected to depend on the mass--volume ratio of the system. This motivates introducing macroscopic variables referred to as density $\rho$ and specific volume $v$ via

:::{math}
:label: eq:chap-01:density-specific-volume
\rho=\frac{m}{V}, \qquad  v=\frac{V}{m} 
:::

Density measures how closely packed the particles are within the boundary, while specific volume indicates how much space is available per unit mass of matter. 

As different materials consist of different types of particles with different particle masses, it is sometimes useful to describe the ratio of volume $V$ to the number of particles $N$ rather than to the total mass. The typical number of particles in a macroscopic volume, however, is large, so one uses the Avogadro constant $N_A=6.02214076\times 10^{23}\,\text{mol}^{-1}$ and the number of moles $n$ instead of the absolute number of particles. This leads to a macroscopic variable definition referred to as molar volume 
:::{math}
:label: eq:chap-01:molar-volume
    V_m=\frac{V}{n}=N_A\frac{V}{N}=Mv,
:::
where the link to specific volume is provided by the molar mass $M=m/n$ of the matter. 

Although macroscopic quantities, density, specific volume, and molar volume can be defined for a collection of particles whether or not it is in an equilibrium state. The SI-units for the space and mass related quantities are listed in {numref}`tab:chap-01:volume-mass-related-units`.

:::{table} Units of volume and mass related quantities.
:label: tab:chap-01:volume-mass-related-units
:align: center
:class: booktabs

| Symbol | Name | SI unit |
|:---:|:---:|:---:|
| $V$ | Volume | $\text{m}^3$ |
| $m$ | Mass | $\text{kg}$ |
| $\rho$ | Density | $\text{kg}\,\text{m}^{-3}$ |
| $v$ | Specific volume | $\text{m}^3\,\text{kg}^{-1}$ |
| $M$ | Molar mass | $\text{kg}\,\text{mol}^{-1}$ |
| $V_m$ | Molar volume | $\text{m}^3\,\text{mol}^{-1}$ |
:::

## <span class="elementary"></span> Pressure
Consider then a cylinder filled with gas and closed with a piston, as in {numref}`fig-pressure-piston-cylinder`. A gas particle that interacts with the piston changes its velocity over a short time interval and, according to Newton’s laws, imparts a small impulse to the piston. On macroscopic times scales, such collisions in a gas appear to occur extremely frequently, and the cumulative effect of many impulses produces a force that, on macroscopic time scales, appears continuous in time. To keep the piston from moving, an opposing force must be applied normal to the piston surface.

:::::{figure}
:label: fig-pressure-piston-cylinder
:align: center
:class: my-subfigures grid grid-cols-2 items-end gap-2

(pressure-piston)=
![Impulse from a particle](./figs/fig-pressure-piston.svg)

(pressure-cylinder)=
![A normal force on a cylinder piston](./figs/fig-pressure-cylinder.svg)

(a) A gas particle imparts impulse on a piston. (b) A force equivalent to the effect of the impulses is need to keep the piston in place.
:::::

The magnitude of this force depends on both the state of the gas and the area of the boundary over which the particles interact. This motivates defining pressure as a macroscopic property to characterize the mechanical effect of a system on its boundary. For a system, pressure is therefore defined as the normal component of the macroscopic force per unit area exerted by the particles of the system on a surface, namely
:::{math}
:label: eq:chap-01:pressure-as-normal-force
    \lim_{A\to 0}\frac{F_n}{A}=p.
:::
The SI-units for the pressure related quantities are listed in {numref}`tab:chap-01:pressure-related-units`. While the SI-unit for pressure is $\text{Pa}$, in engineering applications a more common unit is $1\,\text{bar}=10^5\,\text{Pa}$.

:::{table} Units of pressure related quantities.
:label: tab:chap-01:pressure-related-units
:align: center
:class: booktabs

| Symbol | Name | SI unit |
|:---:|:---:|:---:|
| $F$ | Force | $\text{N}$ |
| $A$ | Area | $\text{m}^2$ |
| $p$ | Pressure | $\text{Pa}\,(=\text{N}\,\text{m}^{-2})$ |
:::

If the piston is pushed inward by increasing the applied force, the volume of the gas decreases. For a sufficiently large compression, part of the gas may condense into a liquid, so that the cylinder contains both gas and liquid. Because of different densities for liquid and gas, gravity ultimately separates them, forming an interface. In equilibrium, the pressure in the gas on a flat interface is equal to the pressure in the liquid at the same location. Otherwise, a net force would act on the interface and it would move until equilibrium is restored. On a strongly curved liquid-gas interfaces, as in small bubbles or dropplets, also the surface tension playes a role, allowing for a small pressure difference between the liquid and gas phases. On both flat and curved surfaces, this shows that the surface on which pressure is defined does not need to be a solid wall like the surface of a piston. An imaginary surface, drawn within gas or liquid, suffices as well. In thermal equilibrium, the particles on either side of such a surface exchange momentum through the interparticle forces, giving rise to a normal force per unit area. Pressure is therefore a macroscopic property, not a property of a particular container wall enclosing the gas or liquid. In gases and liquids, it can nevertheless be applied and measured directly by compressing them in a cylinder with a piston. 



## <span class="intermediate"></span> A remark on solids and stress
While the interparticle forces acting across an imaginary surface within an equilibrium gas or liquid are strictly normal to that surface, regardless of the surface orientation, this is generally not true for solids, nor for liquids and gases in nonuniform motion. In a solid body, the forces transmitted across an internal imaginary surface through a point depend explicitly on the surface orientation. Consequently, the force per unit area at a given point is no longer invariant with direction and cannot be fully described by a single scalar value. Instead, a tensor-valued quantity $\bm{\sigma}$ called stress is introduced to account for both the magnitude and the direction of the force $\bm{F}$ relative to the orientation of the surface normal $\bm{\hat{n}}$.
:::{math}
    \lim_{A\to 0}\frac{\bm{F}}{A}=\bm{\sigma}\cdot\bm{\hat{n}}
:::

This directional dependence of internal forces is a result of a non-isotropic microscopic structure. For instance, extruded plastics possess molecular arrangements that are preferentially aligned with the direction of extrusion. Similarly, in cold-rolled steels, the microscopic metallic grains are mechanically forced to orient along the rolling direction. This microstructural realignment induces macroscopic anisotropy, rendering the material's mechanical strength, elasticity, and thermal response direction-dependent.

For an isotropic solid in an unloaded equilibrium state, such as unworked cast iron, the stress is isotropic and represented by pressure. However, the experimental measurement of this pressure differs from how one measures pressure in liquids and gases. Because a solid cannot rearrange its particles freely to transmit forces uniformly, one cannot submerge a sensor inside it. Instead, a surrounding gas or liquid is typically used as an intermediary. The gas or liquid transmits a uniform force over the solid's external boundary, ensuring that the induced internal force per unit area corresponds uniformly to the applied gas or liquid pressure. 

## <span class="elementary"></span> The zeroth law and temperature
Where pressure, more generally stress, characterizes macroscopic description of the mechanical interactions within a system and across a boundary, one can ask whether a macroscopic characterization exists for interactions across a thermal contact.  To explore this, suppose two systems are separated by a diathermal boundary and are otherwise isolated from external influences. The systems are able to exchange heat. After some time, the interaction across the boundary no longer produces any net heat exchange and the systems settle into a mutual equilibrium. The two systems are then said to be in thermal equilibrium. 

The zeroth law of thermodynamics states that thermal equilibrium is transitive: if system A is in thermal equilibrium with system C, and system B is also in thermal equilibrium with system C, then A and B are in thermal equilibrium with each other. 
The zeroth law enables defining a system property referred to as temperature: two systems are in thermal equilibrium if and only if they have the same temperature. The symbol usually chosen for the temperature defined in this way is $T$.

## <span class="elementary"></span> A gas thermometer
While the zeroth law enables defining the concept of temperature, it does not directly provide a way to measure or calculate it. A detour is needed. To quantify the temperature $T$ of a system, one may place a gas-filled bulb in thermal contact with the system, connect the gas to a manometer, as illustrated in {numref}`fig-gas-thermometer`, and make experimental observations.

:::::{figure}
:label: fig-gas-thermometer
:align: center

![](./figs/fig-gas-thermometer.svg)

A gas-filled bulb in thermal contact with a system and connected to a manometer. The manometer measures the gas pressure and volume.
:::::

According to the zeroth law, the gas in the bulb will reach thermal equilibrium with the system and thus have the same temperature $T$. By changing the volume of the gas by adjusting the amount of liquid in the manometer, while keeping the state of the system unchanged, one observes many different pairs of gas pressure $p$ and volume $V$ that all correspond to the same system temperature. This demonstrates that the temperature of the gas, which is the same as that of the system, depends on its pressure and volume in a reproducible way, justifying the existence of a functional relation
:::{math}
    T = f(p,V).
:::
Further experiments with sufficiently dilute gases show that, while the gas remains in thermal equilibrium with the system, its pressure and volume are inversely proportional to each other. This empirical observation implies the existence of a relation of the form
:::{math}
    pV = g(T),
:::
where $g(T)$ depends only on the temperature.

One may now choose a reference state for the gas and label its temperature, pressure, and volume as $T_\text{ref}$, $p_\text{ref}$, and $V_\text{ref}$, respectively. For any other state of the gas with pressure $p$ and volume $V$, the temperature $T$ then satisfies
:::{math}
    \frac{g(T)}{g(T_\text{ref})} = \frac{pV}{p_\text{ref}V_\text{ref}}.
:::
Since temperature has not yet been assigned a numerical scale, the functional form of $g(T)$ may be chosen by convention. A convenient choice is
:::{math}
    g(T) = \text{const}\times T,
:::
where the constant depends on the chosen gas and the specific experimental setup. This choice defines a temperature scale such that the temperature of the system can be determined by measuring the pressure and volume of the gas and comparing them to the reference values
:::{math}
    \frac{T}{T_\text{ref}} = \frac{pV}{p_\text{ref}V_\text{ref}}.
:::

It is common to choose the reference temperature to correspond to the state at which water can exist simultaneously in solid, liquid, and gas phases, and to assign it the value $T_\text{ref} = 273.16\,text{K}$. With this choice, the gas thermometer measures temperature on the Kelvin scale (K) which serves also as the SI-unit for temperature. Another commonly used temperature scale is the Celsius scale that is related to the Kelvin scale by a constant
:::{math}
    T[^\circ\text{C}]=T[\text{K}]-273.15.
:::

::::{proof:example}
:label: example:chap-01:gas-thermometer
A gas thermometer uses mercury with a density of $\rho_\text{Hg}=13.59\,\text{g}\,\text{cm}^{-3}$ as the liquid substance. The inner diameter of thermometer capillary is $d=1\,\text{m}$. With an ambient pressure of $p_\text{atm}=1.013\,\text{bar}$, a reference measurement corresponding to a temperature of $T_\text{red}=273.15\,\text{K}$ provides a value of $V_\text{ref}=4.19\,\text{cm}^3$ for the gas volume and a value of $h_\text{ref}=89\,\text{mm}$ for the mercury column height difference in the capillary. A measurement of a different sample provides a value of $h=45\,\text{mm}$ for the mercury column height difference.

To determine the sample temperature, one calculates the pressure inside the thermometer bulb implied by the measurements. As it equals the sum of ambient pressure and the hydrostatic pressure of the mercury column height, one finds

:::{math}
:enumerated: false
p_\text{ref}&=p_\text{atm}+\rho_\text{Hg} g h_\text{ref}=1.132\,\text{bar}\\
p&=p_\text{atm}+\rho_\text{Hg} g h=1.073\,\text{bar}
:::

The change in the gas volume from the reference state \(V_\text{ref}\) is calculated from the capillary cross sectional area and the change in the mercury column height

:::{math}
:enumerated: false
V=V_\text{ref}+\frac{1}{4}\pi d^2(h-h_\text{ref})=4.155\,\text{cm}^3.
:::

The temperature of the sample, as measured by the gas thermometer, then is
:::{math}
:enumerated: false
T=T_\text{ref}\frac{pV}{p_\text{ref}V_\text{ref}}=256.86\,\text{K}=-16.29^\circ\text{C}
::::


## <span class="elementary"></span> Extensive and intensive quantities
The volume, mass, and internal energy of a system are extensive quantities, meaning they depend on the amount of matter in the system. In contrast, density, specific volume, molar volume, pressure, specific internal energy, and temperature are intensive quantities, which do not depend on the system size. If two systems with identical properties are combined, the extensive variables sum, while the intensive variables remain unchanged. Theories describing the behaviour of matter usually rely on intensive quantities and variables. That in mind, plain upper-case symbols are reserved for extensive variables, upper-case symbols with a subscript $m$ are reserved for intensive variables expressed relative to the number of moles, and plain lower-case symbols are reserved for intensive variables expressed relative to the mass, as in {numref}`tab:chap-01:extensive-intensive-convention`. Temperature ($T$), pressure ($p$), and mass ($m$) are the primary exceptions to this symbolic convention.

:::{table} Extensive and intensive symbol conventions for matter-related quantities.
:label: tab:chap-01:extensive-intensive-convention
:align: center
:class: booktabs

| Type | Symbol | unit |
|:---|:---:|:---:|
| Extensive | $A$ | $[A]$ |
| Intensive (specific to mass) | $a$ | $[A]\,\text{kg}^{-1}$ |
| Intensive (specific to amount of substance) | $A_m$ | $[A]\,\text{mol}^{-1}$ |
:::

## <span class="advanced"></span> Matter in motion
Matter, be it gas, liquid, or solid, doesn't have to remain still. Also its shape can change. Liquids and gases flow, hence they are called fluids, while solids may bend elastically and oscillate back and forth, or deform inelastically. Typically the macroscopic scale of the volume the matter occupies is vast in comparison to the interparticle distances, and the time scale of motion one observes is orders of magnitudes longer than the average time between inter-particle collisions. Under such conditions, different parts of macroscopic volumes of matter can be treated as individual systems connected by boundaries, with each system remaining in thermodynamic equilibrium state but potentially in a different one from the neighbouring system's state. The matter then is said to remain in a local thermodynamic equilibrium and thermodynamic relations between state variables are assumed to hold locally.

In such macroscopic continuum approximation of matter, each subsystem of the macroscopic volume is assumed infinitesimally small. The state properties are described as continuous fields that smoothly depend on the point-wise location $\boldsymbol{x}$ and time $t$. To track matter in motion, one supplements the thermodynamic state fields with a velocity field, $\boldsymbol{v}(\boldsymbol{x},t)$, which describes the macroscopic speed and direction of matter at any given point and time. Evolution equations for the state fields are derived by applying conservation laws of mass, momentum, and energy to these moving subvolumes.

In classical mechanics of point particles and rigid bodies, one is accustomed to tracking the motion of a fixed mass subjected to a force. In continuum mechanics, this corresponds to tracking a volume containing a fixed mass, referred to as material volume, subject to a distribution of remote forces such as gravity acting through out the volume and local contact forces acting on the surface of the volume. In case of solids, the deformation of the object is limited by the material strength and an approach of trackin the point-wise deformation of the volume from its initial configuration is practical. Such view is generally referred to as Lagrangian view. In case of fluids that may flow indefinitely, tracking the deformation becomes cumbersome and eventually impossible. Due to lack of structural strength, a continuous flow may deform an initially well described cubic volume into an infinitely elongated and infinitesimally thin volume. As a remedy, one switches to observing how the properties of the fluid change when it flows through a fixed location chosen to make the observations convenient. Such view is referred to as Eulerian. 

In Lagrangian view, the velocity field $\boldsymbol{v}(\boldsymbol{x},t)$ is interpreted to move a point $\boldsymbol{x}(t)$ according to an ordinary differential equation

:::{math}
	\frac{d\boldsymbol{x}(t)}{dt}=\boldsymbol{v}(\boldsymbol{x}(t),t),
:::

generating integral curves of the velocity field that depend on the initial location for the point. The connection to Eulerian view is established through the acceleration of the point $\boldsymbol{x}(t)$

:::{math}
	\frac{d^2\boldsymbol{x}(t)}{dt^2}=\frac{d\boldsymbol{v}(\boldsymbol{x}(t),t)}{dt}=\partial_t\boldsymbol{v}(\boldsymbol{x}(t),t)+\boldsymbol{v}(\boldsymbol{x}(t),t)\cdot\nabla\boldsymbol{v}(\boldsymbol{x}(t),t).
:::

The first term $\partial_t\boldsymbol{v}$ on the right describes the local Eulerian rate of change of the velocity at a point while the second term $\boldsymbol{v}\cdot\nabla\boldsymbol{v}$ describes the additional local acceleration the moving point $\boldsymbol{x}(t)$ is subjected to in the Lagrangian view.

::::{proof:example}
:label: example:chap-01:lagrangian-acceleration

Consider the velocity field

:::{math}
:enumerated: false
\boldsymbol{v}(\boldsymbol{x})=v_0\boldsymbol{\hat{x}}+v_0\frac{xy}{L^2}\boldsymbol{\hat{y}}
:::

For a person watching the liquids or gases flowing according to the field, the flow appears stationary, unchanging as $\partial_t\boldsymbol{v}=0$ everywhere. A point $\boldsymbol{x}(t)=x(t)\boldsymbol{\hat{x}}+y(t)\boldsymbol{\hat{y}}$ moving with the flow of the velocity field nevertheless experiences the acceleration
:::{math}
:enumerated: false
\frac{d^2\boldsymbol{x}(t)}{dt^2}=(\boldsymbol{v}\cdot\nabla\boldsymbol{v})\big|_{\boldsymbol{x}(t)}=\frac{v_0^2}{L}\left(1+\frac{x(t)^2}{L^2}\right)\frac{y(t)}{L}\boldsymbol{\hat{y}}
:::

::::


## <span class="elementary"></span> A roadmap for the course
The continuum mechanics framework can be built on three core principles: the measurement of observable quantities; the fundamental conservation laws of mass, momentum, and energy; and the natural tendency of local differences in macroscopic quantities to smooth out over time in the absence of external influences. 

