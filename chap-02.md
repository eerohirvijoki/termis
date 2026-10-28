---
numbering:
  enumerator: "2.%s"
  heading_1: true
  heading_2: true
  heading_3: true
---

# 2 Properties of Pure Substances

This chapter first introduces relations between state variables of pure substances using illustrative phase diagrams. The diagrams provide the reader an overview of how substances generally behave, and what common features are shared among them. Predictive models are then introduced, first with simple analytical equations of state, then through numerical property libraries. The analytical models serve to explain observations in the phase diagrams, help in design of experimental measurements of unknown substances, and support intuition of substance behaviour. The numerical property libraries, on the other hand, are the gold standard for engineering modeling and provide accuracy when required. From the property observations and models, the reader is introduced to the state-variable response coefficients that are needed later in developing the thermodynamic framework. Finally, the principle of corresponding states is discussed to help in predicting properties of unknown substances with the properties of known substances' data. The positioning of this chapter within the overall roadmap is illustrated in {numref}`fig-roadmap-chap-02`.

:::{figure} ./figs/fig-roadmap-chap-02.svg
:label: fig-roadmap-chap-02
:align: center
:width: 100%

The positioning of the chapter content with respect to the roadmap.
:::


## Learning goals

The learning goals for this chapter are listed below. The goals to support the core path are:

- <span class="elementary"></span> The reader identifies locations of critical point, triple line, and phase transition lines in phase diagrams of pure substances.
- <span class="elementary"></span> The reader recalls the different phases of ordinary matter, the transitions between them, and is able to sketch phase diagrams.
- <span class="elementary"></span> The reader calculates vapor quality of a state point on a given $p$-$v$ or $v$-$T$ diagram.
- <span class="elementary"></span> The reader uses simple analytical equations of state to evaluate state variables.
- <span class="elementary"></span> The reader predicts substance's critical point with a Van der Waals model or another two-parameter model from measurements.
- <span class="elementary"></span> The reader uses pyromat or coolprop to evaluate substance state variables and vapor quality.
- <span class="elementary"></span> The reader estimates the isobaric thermal expansion and the isothermal compressibility coefficients from $p$-$v$ or $v$-$T$ diagrams and computes them with pyromat or coolprop.
- <span class="elementary"></span> The reader calculates the compressibility factor from given data to estimate the validity of ideal gas model.
- <span class="elementary"></span> The reader uses the principle of corresponding states to to predict properties of a substance with the help other substance's data.

The goals to support the intermediate and advanced paths are:

- <span class="intermediate"></span> The reader fits two-parameter models to experimentally observed critical point data.
- <span class="intermediate"></span> The reader uses total differentials to derive relations between partial derivatives.
- <span class="advanced"></span> The reader estimates saturation properties with two-parameter models subjected to the Maxwell construct.
- <span class="advanced"></span> The reader programs a python script utilizing pyromat or coolprop to create a $p$-$v$ or a $v$-$T$ diagram.

(sec-pvT-diagram)=
## <span class="elementary"></span> The p-v-T phase diagram
In mechanics, matter is classified into solid states that can sustain shape under shearing forces and into fluid states that cannot. In engineering thermodynamics, fluid states are classified not only into liquid and gas states but subclassified further into superheated vapor and supercritical fluid states. In short, superheated vapor is gaseous while supercritical fluid has characteristics of both liquid and gas. Also mixtures of solid, liquid, and gas states in common thermodynamic equilibrium are encountered. In a three-dimensional space with pressure $p$, specific volume $v$, and temperature $T$ as coordinates, thermodynamic states of a pure substance form a two-dimensional, so-called $p$-$v$-$T$ surface. Schematic illustrations of such surfaces are provided in {numref}`fig-pvT`, with temperature and pressure isocontours, i.e., isotherms and isobars, drawn with black and white dashed curves.

::::{figure}
:label: fig-pvT
:align: center
:width: 100%

(fig-pvT-expanding)=
:::{image} ./figs/fig-pvT-expanding.svg
:alt: Substance that expands during melting
:width: 100%
:::

(fig-pvT-contracting)=
:::{image} ./figs/fig-pvT-contracting.svg
:alt: Substance contracting during melting
:width: 100%
:::

Schematic $p$-$v$-$T$ diagrams for pure substances that expand (top) or contract (bottom) during melting.
::::

Important classifiers are observed in {numref}`fig-pvT`. First is the critical point with pressure $p_\text{crit}$, temperature $T_\text{crit}$, and specific volume $v_\text{crit}$. At temperatures above that of the critical point, a gaseous state is referred to as gas and cannot be condensed into a liquid by increasing the pressure alone. This has important consequences for the design of engineering applications that often rely on phase transitions. At temperatures below that of the critical point, a gaseous state is labelled as superheated vapor and can be condensed into liquid by increasing the pressure alone. If both pressure and temperature are above those of the critical point, the fluid state is labelled as supercritical. Second is the triple line that, if projected onto the $p$-$T$ plane, is observed to reduce into a single point. This indicates that the triple line is characterized by a single pressure value $p_\text{trp}$, a single temperature value $T_\text{trp}$, and a range of values for specific volume. For pressure values below that of the triple line, a stable liquid phase does not exist. Further important classifiers in {numref}`fig-pvT` are the thick colored curves that separate single-phase regions from two-phase regions and, when projected onto the $p$-$T$ plane, form the two-colored co-existence curves representing mixtures of two phases. For convenience, the labels for the single-phase regions, the mixture-phase regions, and the names of the transitions between them are illustrated also in {numref}`fig-pvT-labels`.

:::::{figure} ./figs/fig-pvT-labels.svg
:label: fig-pvT-labels
:align: center
:width: 100%
Labels of the single-phases regions and the transitions between them.
:::::

Following the isobars and isotherms on the $p$-$v$-$T$ surface, one may build understanding of the substance behaviour. For pressure values below that of the triple line, keeping the pressure constant while decreasing the temperature of a gas results in reduction of the gas volume, until vapor begins to deposit into a solid. A phase-mixture of gaseous vapor and solid in a thermodynamic equilibrium then forms, with pressure and temperature common for both phases. If volume is then reduced while keeping the temperature constant, also pressure remains constant until all of the vapor is deposited into solid. After that, further reduction of temperature at constant pressure can continue while the substance state remains in solid phase, leading typically to minor reduction in the substance volume. 

For pressure values above that of the triple line but below that of the critical point, keeping the pressure constant while decreasing the gas temperature again leads to decrease in the gas volume, until the vapor starts condensing into liquid. A phase-mixture of liquid and vapor then forms, with pressure and temperature common for both phases. If the volume is then reduced while keeping temperature constant, pressure remains constant until all vapor has condensed into liquid. Reducing temperature at constant pressure can then continue, until liquid at some point begins to freeze into solid. For many substances, the phase-mixture of solid and liquid under constant temperature and pressure reduces in volume upon freezing but for some, like water, freezing leads to expansion in substance volume instead. This behaviour is observed also in {numref}`fig-pvT`. Once all of the liquid has frozen into solid, temperature can be further reduced at constant pressure, leading again typically to a reduction of the substance volume. At pressures above that of the critical point, no phase boundary nor coexistence curve exists between gas- and liquid-like phases. Instead, the transition is continuous and happens in a single phase. 

The phase-mixture regions might seem somewhat exotic at first but are not. A region where two phases coexist in equilibrium can be obtained, e.g., by placing a kettle filled with liquid water on a stove and turning the heat on. Once the water starts boiling, water vapor forms and fills the remaining space under the kettle lid, pushing air out. A mass of water then exists within a volume in both liquid and vapor states, sharing a common temperature and pressure. Because liquid water has higher density than water vapor, gravity separates the liquid and vapor phases into physically different regions within the kettle. As a system, the water in the kettle nevertheless has one mass and one volume, and therefore, as a system, can be assigned a single specific volume or density value, corresponding to a state. In this respect the triple line is a unique collection of states. As the line separates two phase-transition regions, matter on the line can exist simultaneously in all three primary phases, as solid, liquid, and gaseous vapor.

(sec-pv-vT-diagrams)=
## <span class="elementary"></span> The p-v and v-T diagrams, vapor quality
Many engineering applications involve fluids at pressures above that of the triple line, though exceptions do exist. For practical reasons of data availability, the discussion here is limited to pressure values above the triple line. To represent the fluid state and the associated isotherms and isobars quantitatively, the $p$–$v$ and $v$–$T$ projections replace the schematic $p$–$v$–$T$ surface, as shown for water in {numref}`fig-pv-vT-H2O`. Particular attention is given to the two-phase region, representing mixtures of liquid and vapor, and to the behaviour of temperature and pressure isocontours in the $p$–$v$ and $v$–$T$ planes.

::::{figure}
:label: fig-pv-vT-H2O
:align: center
:width: 120%

(fig-pv-T-H2O)=
:::{image} ./figs/fig-pv-T-H2O-annotated.svg
:alt: The p-v diagram for water
:width: 90%
:::

(fig-vT-p-H2O)=
:::{image} ./figs/fig-vT-p-H2O-annotated.svg
:alt: The v-T diagram for water
:width: 90%
:::

The $p$-$v$ (top) and $v$-$T$ (bottom) diagrams for water,
with critical point and triple line indicated.
::::

In the $p$-$v$ and $v$-$T$ diagrams of {numref}`fig-pv-vT-H2O`, the red curve denotes the saturated liquid states, while the green curve represents the saturated vapor states. The two curves start from the opposing ends of the triple line and meet at the critical point. Together they form the saturation curve which, together with the triple line, encloses the liquid-vapor two-phase region. Elsewhere a fluid state exists in single phase. Although {numref}`fig-pv-vT-H2O` is specific to water, the same definitions and qualitative behavior apply to all pure substances, with only values differing. 

As disccussed in connection with the $p$-$v$-$T$ surface, temperature and pressure both remain constant during a phase transition when volume change is not constrained. This is reflected in both the $p$-$v$ and the $v$-$T$ diagram. In the $p$-$v$ diagram, isotherms are horizontal in the two-phase region, and the phase transition appears as a horizontal line between the saturated liquid and saturated vapor states. In the $v$-$T$ diagram, the roles are reversed. Isobars are vertical within the two-phase region, and the phase transition appears as a vertical line between the saturated liquid and saturated vapor states.

What changes during a phase transition is the specific volume of a substance, and a quantity referred to as vapor quality. In a volume $V$ containing mass $m$ in a two-phase state, the liquid will occupy a volume $V_\text{liq}$ and have mass $m_\text{liq}$ while the vapor will occupy a volume $V_\text{vap}$ and have mass $m_\text{vap}$. Naturally, the volumes and masses sum together according to

:::{math}
    V_\text{liq}+V_\text{vap}=V, \qquad 
    m_\text{liq}+m_\text{vap}=m.
:::

On the saturated liquid curve, no vapor exists at all while on the saturated vapor curve, only vapor exists. To reflect this behaviour, vapor quality is defined as the ratio of the vapor mass to the total fluid mass

:::{math}
    x=\frac{m_\text{vap}}{m}=\frac{m_\text{vap}}{m_\text{liq}+m_\text{vap}}.
:::

The liquid and vapor parts have specific volumes corresponding to the respective states at the saturated liquid and vapor curves 

:::{math}
    v_\text{liq}=\frac{V_\text{liq}}{m_\text{liq}}, \qquad 
    v_\text{vap}&=\frac{V_\text{vap}}{m_\text{vap}}, 
:::

and a state in the two-phase region, having vapor quality $x$, has a specific volume of

:::{math}
	v&=\frac{V}{m}=\frac{V_\text{liq}}{m}+\frac{V_\text{vap}}{m}=\frac{m_\text{liq}}{m}\frac{V_\text{liq}}{m_\text{liq}}+\frac{m_\text{vap}}{m}\frac{V_\text{vap}}{m_\text{vap}}\\
	&=(1-x)v_\text{liq}+x\,v_\text{vap}
:::

Conversely, the vapor quality in the two-phase region can be determined from the specific volume with

:::{math}
    x=\frac{v-v_\text{liq}}{v_\text{vap}-v_\text{liq}}.
:::

Chosen isocontours of the vapor quality defined in this manner are drawn in the $p$-$v$ and $v$-$T$ diagrams of water in {numref}`fig-pv-vT-H2O` with black dashed lines. One should remember that the vapor quality is specified only within the two-phase region and with values $x\in[0,1]$.

::::{proof:example}
:label: vapor-quality-from-pv-diagram

Hot steam at $T=150^\circ\text{C}$ is produced for an industrial process by boiling water with an electric resistance heater within a pressure vessel. The pressure vessel has a volume of $1000\,\ell$ and the liquid water inside is observed to occupy a volume of $200\,\ell$. Estimate the mass of water vapor inside the pressure vessel and calculate the vapor quality for the water in the vessel.

From the $p$-$v$ diagram in {numref}`fig-pv-T-H2O`, one can estimate the specific volumes of saturated liquid and saturated vapor using the $150^\circ\text{C}$ isotherm and the saturated liquid and vapor curves:
$$
	v_\text{liq}&\approx 1\times 10^{-3}\,\text{m}^3\,\text{kg}^{-1}, &
	v_\text{vap}&\approx 4\times 10^{-1}\,\text{m}^3\,\text{kg}^{-1}.
$$
Using the definition of specific volume, the masses of liquid water and water vapor are then calculated from the volumes and the specific volumes
$$
	m_\text{liq}&=\frac{V_\text{liq}}{v_\text{liq}}\approx 200\,\text{kg}, &
	m_\text{vap}&=\frac{V_\text{vap}}{v_\text{vap}}=\frac{V-V_\text{liq}}{v_\text{vap}}\approx 2\,\text{kg},
$$
and the total mass of water inside the pressure vessel can be calculated to be $m\approx202\,\text{kg}$. The specific volume for the water inside the vessel is therefore $v=V/m\approx 5\times 10^{-3}\,\text{m}^3\,\text{kg}^{-1}$ and the vapor quality is calculated to be
$$
	x=\frac{v-v_\text{liq}}{v_\text{vap}-v_\text{liq}}\approx 0.01.
$$
The points from which the values used are obtained are illustrated below.

:::{image} ./figs/example-fig-pv-T-H2O-annotated.svg
:align: center
:width: 100%
:::


::::

::::{proof:example}
:label: vapor-temperature

A pressure vessel with a volume of $30\,\text{m}^3$ contains $1000\,\text{kg}$ of water at a pressure of $p=10\,\text{bar}$. What is the temperature of water in the vessel? At what temperature would all water in the vessel become vapor?

The specific volume of water in the vessel is $v=V/m=0.03\,\text{m}^3\,\text{kg}^{-1}$. From the $v$-$T$ diagram in {numref}`fig-vT-p-H2O`, one finds the temperature at this specific volume and pressure of $10\,\text{bar}$ to be $T\approx 180^\circ\text{C}$. Both the volume of the pressure vessel and the mass of water inside it remain fixed even if temperature were to change. The temperature at which all of the water inside would be vapor, is then found on the green saturated vapor curve at the given specific volume, corresponding to $T\approx 280^\circ\text{C}$. Both state points are illustrated below.

:::{image} ./figs/example-fig-vT-p-H2O-annotated.svg
:align: center
:width: 95%
:::

::::


(sec-simple-equations-of-state)=
## <span class="elementary"></span> Simple equations of state
Mathematically, a general two-dimensional surface in a three-dimensional space with coordinates $p$, $v$, and $T$, can be represented by an equation of the form
:::{math}
    f(p,v,T)=0.
:::
Experimental observations illustrated in {numref}`sec-pvT-diagram` and {numref}`sec-pv-vT-diagrams` show that, in the two-phase regions, pressure and temperature can both stay constant while the specific volume varies. While real phase transitions may exhibit delayed boiling or condensation due to kinetic effects and the absence of nucleation sites, the equilibrium phase boundaries nevertheless provide an accurate approximation for most engineering applications. Within such boundaries, pressure and temperature therefore satisfy a relation of the form
:::{math}
    g(p,T)=0,
:::
and, for a fixed temperature or pressure, the specific volume parametrizes the two-phase mixture states. 

Across the boundaries between single- and two-phase regions, the derivatives of the state surface change abruptly. This is observed in the $p$-$v$ and $v$-$T$ diagrams for water in {numref}`fig-pv-vT-H2O`, where the isotherms and isobars vary smoothly outside the liquid–vapor region but change direction abruptly on the saturation curves. Because of this, it is practically impossible to represent the entire state surface by a single analytic equation that behaves smoothly everywhere. Therefore, mathematical expressions referred to as equations of state are developed with constrained applicability domains. 

The arguably simplest equation of state, found experimentally and applicable for dilute gases, is referred to as the ideal gas equation 
:::{math}
    pv=R_sT.
:::
The constant $R_s=R/M$ is gas specific, with $R=8.3145\,\text{J}\,\text{mol}^{-1}\,\text{K}^{-1}$ the universal gas constant and $M$ the molar mass of the gas. The mathematical form of the equation implies that the ideal gas isotherms in a $p$-$v$ diagram look like hyperbolas on a linear-linear scale. Taking logarithms from both sides of the equation and rearranging leads to 
:::{math}
\log_{10}p=\log_{10}(R_sT)-\log_{10}v.
:::
In a $p$-$v$ diagram using a log-log scale, the ideal gas isotherms would therefore appear as straight downward trending lines with a slope of -1. This behavior is observed in the $p$-$v$ diagram of water in {numref}`fig-pv-T-H2O`. The slope of the $700^\circ\text{C}$ isotherm is very close to -1 throughout while for lower temperatures, the slope is quite close to -1 if the pressure is low enough. The qualitative agreement with observations suggests the ideal gas equation to be a reasonable model, at least in certain parts of the fluid region.

Close to the saturated vapor curve or near the critical point, the real isotherms deviate significantly from the hyperbolas of the ideal gas model (the straight downward sloping lines in log-log scale). Such deviations become important in engineering applications operating at high pressures or near phase transitions, where the ideal gas model may produce large errors. Therefore more accurate models for the gaseous phase have been developed. Historically, the most influential has been the Van der Waals equation of state
:::{math}
    p=\frac{R_sT}{v-b_s}-\frac{a_s}{v^2}, \qquad \left\{\begin{aligned}
    a_s&=\frac{27}{64}\frac{R_s^2T_\text{crit}^2}{p_\text{crit}},\\
    b_s&=\frac{R_sT_\text{crit}}{8p_\text{crit}}.
\end{aligned}\right.
:::
Further improvements include for example the Dieterici equation of state
:::{math}
    p=\frac{R_sT}{v-b_s}\exp\left(-\frac{a_s}{vR_sT}\right), \qquad \left\{\begin{aligned}
    a_s&=4e^{-2}\frac{R_s^2T_\text{crit}^2}{p_\text{crit}},\\
    b_s&=e^{-2}\frac{R_sT_\text{crit}}{p_\text{crit}},
    \end{aligned}\right.
:::
and the Redlich-Kwong equation of state
:::{math}
    p=\frac{R_sT}{v-b_s}-\frac{a_s}{\sqrt{T} v(v+b_s)}, \qquad \left\{\begin{aligned}
    a_s&=\frac{1}{9(2^{1/3}-1)}\frac{R_s^2 T^{5/2}_\text{crit}}{p_\text{crit}},\\
    b_s&=\frac{2^{1/3}-1}{3}\frac{R_sT_\text{crit}}{p_\text{crit}},
    \end{aligned}\right.
:::
Of these the Van der Waals and Redlich–Kwong models belong to the class of cubic equations of state while all three belong to the family of two-parameter models. The equations are modifications of the ideal gas equation to account for molecular interaction effects and finite molecular size, and reduce to the ideal gas model at appropriate limits. 

::::{proof:example}
The cubic nature of the Van der Waals equation is revealed when trying to solve for specific volume from given pressure and temperature values
:::{math}
:enumerated: false
&p=\frac{R_sT}{v-b_s}-\frac{a_s}{v^2}\\
&\implies v^3-\left(b_s+\frac{R_sT}{p}\right)v^2+\frac{a_s}{p}v-a_sb_s=0.
:::
Similarly for the Redlich-Kwong model, one finds a cubic equation for specific volume
:::{math}
:enumerated: false
&p=\frac{R_sT}{v-b_s}-\frac{a_s}{\sqrt{T}v(v+b_s)}\\
&\implies v^3-\frac{R_sT}{p}v^2+\left(\frac{a_s}{p\sqrt{T}}-\frac{R_sTb_s}{p}-b_s^2\right)v-\frac{a_sb_s}{p\sqrt{T}}=0.
:::
::::

::::{proof:example}
Writing the Van der Waals model as
:::{math}
:enumerated: false
(p+a_s\rho^2)(v-b_s)=R_sT,
:::

one may interpret the parameter $a_s$ as a correction to pressure associated with intermolecular interactions that scale quadratically with respect to gas density. The parameter $b_s$ can be interpreted to account for reduction in accessible volume due to finite molecular size. Writing the equation further as

:::{math}
:enumerated: false
pv(1+a_s\rho^2/p)(1-b_s/v)=R_sT,
:::

one observes the Van der Waals model to reduce to the ideal gas equation when both $p\gg a_s\rho^2$ and $v\gg b_s$ hold true.

::::

The Van der Waals equation, the Dieterici equation, and the Redlich-Kwong equation all describe state surfaces of type $f(p,v,T)=0$ and improve upon the ideal gas equation. They nevertheless fall short of correct behaviour when the nature of the state surface changes abruptly from the gaseous state to the two-phase liquid-vapor mixture state where pressure and temperature follow a relation of the form $g(p,T)$ instead. The shortfall is demonstrated in {numref}`fig-pv-T-CO2-eos-comparison` for carbon dioxide using the Redlich-Kwong equation. Also the corresponding isotherms predicted by ideal gas model are shown. For temperatures above $30.98^\circ\text{C}$, the critical temperature of CO$_2$, the Redlich-Kwong isotherms align quite well with the measured data. The isotherm corresponding to the critical temperature at specific volumes smaller than the critical point volume, and the predicted location of the critical point, are slightly off. The explanation for the critical point discrepancy is provided in {numref}`sec-fitting-two-parameter-models`. Below the critical temperature, the Redlich-Kwong isotherms show unphysical behaviour between the experimental saturated liquid and vapor states. A region exists where pressure increases with increasing volume, whereas the correct isotherms remain flat. This unphysical behaviour below the critical point temperature is exhibited by all two-parameter models. Notably, the ideal gas isotherms near the critical point perform significantly worse.

:::{figure} ./figs/fig-pv-T-CO2-eos-comparison-annotated.svg
:label: fig-pv-T-CO2-eos-comparison
:align: center
:width: 90%
Selected isotherms for CO$_2$ calculated from ideal gas and Redlich-Kwong models and compared to experimental data.
:::


Although the two-parameter models predictions are slightly off near the critical point and behave incorrectly in the two-phase region, the historical importance of the models is significant. The understanding of substance properties has developed gradually over time, and even rough estimates of the pressure and temperature below which it is possible to liquefy a gas are valuable when mapping the thermodynamic properties of an unknown substance. With the help of two-parameter models, it is possible to estimate the parameters $a_s$ and $b_s$ from measurements performed in the single-phase gaseous region. The parameters $a_s$ and $b_s$ can then be used to estimate the critical point location and the estimates used to design the devices with which experimental measurements are carried out to obtain accurate data. Combining the two-parameter model with a so-called Maxwell construction, even saturation properties can be estimated, as demonstrated in {numref}`sec-maxwell-construction`. When more accurate modeling is required, one may resort to thermodynamic data libraries introduced in {numref}`sec-pyromat-coolprop`.

::::{proof:example}

Assuming a gas to obey the Redlich–Kwong equation of state, one may determine the model coefficients by measuring the pressure of the gas inside a rigid container at two different temperatures. Given state points $(p_1,v,T_1)$ and $(p_2,v,T_2)$, one finds

:::{math}
:enumerated: false
&\left.\begin{aligned}
p_1&=\frac{R_sT_1}{v-b_s}-\frac{a_s}{\sqrt{T_1} v(v+b_s)}\\
p_2&=\frac{R_sT_2}{v-b_s}-\frac{a_s}{\sqrt{T_2} v(v+b_s)}
\end{aligned}\right\}\implies 
\begin{aligned}
b_s&=v-\frac{R_sT_1\sqrt{T_1}-R_sT_2\sqrt{T_2} }{p_1\sqrt{T_1}-p_2\sqrt{T_2}}\\
a_s&=\frac{(p_1T_2-p_2T_1)\sqrt{T_2}\sqrt{T_1}}{T_1\sqrt{T_1}-T_2\sqrt{T_2}} v(v+b_s)
\end{aligned}
:::

Once the values for $a_s$ and $b_s$ are known, the critical temperature and pressure predicted by the Redlich-Kwong model are obtained from

:::{math}
:enumerated: false
T_\text{crit}&=\left(\frac{3(2^{1/3}-1)^2a_s}{R_sb_s}\right)^{2/3}, &
p_\text{crit}&=\frac{2^{1/3}-1}{3}\frac{R_sT_\text{crit}}{b_s}
:::

At a specific volume of $v=0.10\,\text{m}^3/\text{kg}$, the pressure of methane at $T_1=-20^\circ\text{C}$ has been measured at $p_1=12.61\,\text{bar}$. At the same volume at temperature $T_2=50^\circ\text{C}$, the pressure has been measured at $p_2=16.40\,\text{bar}$. The Redlich-Kwong model then predicts the critical temperature and pressure of methane to be $T_\text{crit}=-91.54^\circ\text{C}$ and $p_\text{crit}=40.50\,\text{bar}$. The estimates are reasonably close to the experimentally measured values of $T_\text{crit}=-82.59^\circ\text{C}$ and $p_\text{crit}=45.99\,\text{bar}$.

::::

(sec-fitting-two-parameter-models)=
## <span class="intermediate"></span> Fitting of two-parameter equations of state
The two-parameter equations of state are designed to better fit experimental observations near the critical point than the ideal gas model. For example, as visible in {numref}`fig-pv-T-CO2-eos-comparison`, the Redlich-Kwong model achieves a reasonably good accuracy in that the model-specific isotherms appear to closely resemble the experimental data, apart from the clear difference in the two-phase region. The success of the various two-parameter models to do so relies on how the parameters $a_s$ and $b_s$ are chosen. 

In a $p$-$v$ diagram of a pure substance, the experimental isotherm passing through the critical point exhibits a stationary inflection point at the critical point. Mathematically this means that both the first and the second derivative of pressure with respect to specific volume are zero at the critical point. For the two parameter models to reflect this experimental observation, the model-predicted critical point is required to reproduce the experimentally observed sationary inflection point at critical point temperature and pressure. Consequently the model-predicted value for the critical point specific volume is typically somewhat off the experimental value. Mathematically, one requires three conditions to hold
:::{math}
\left(\frac{\partial p}{\partial v}\right)_T\Big|_{(T=T_\text{crit},p=p_\text{crit})}=0,\\
:::
:::{math}
\left(\frac{\partial^2 p}{\partial v^2}\right)_T\Big|_{(T=T_\text{crit},p=p_\text{crit})}=0,\\
:::
:::{math}
p(v,T_\text{crit})=p_\text{crit},
:::
which provide the model-specific parameters $a_s(T_\text{crit},p_\text{crit})$ and $b_s(T_\text{crit},p_\text{crit})$ as well as the model prodicted critical volume $v_\text{crit}=v(T_\text{crit},p_\text{crit})$ as functions of the experimental critical point temperature and pressure. 

(example-vdw-coefficients)=
::::{proof:example}
For the Van der Waals model, the first and second derivatives of pressure with respect to specific volume at constant temperature become

:::{math}
:enumerated: false
\left(\frac{\partial p}{\partial v}\right)_T&=-\frac{R_sT}{(v-b_s)^2}+\frac{2a_s}{v^3},\\ 
\left(\frac{\partial^2 p}{\partial v^2}\right)_T&=\frac{2R_sT}{(v-b_s)^3}-\frac{6a_s}{v^4}.
:::

Requiring both derivatives to vanish when pressure and temperature correspond to the critical point values, one may solve for
:::{math}
:enumerated: false
\left.\begin{aligned}
-\frac{R_sT_\text{crit}}{(v_\text{crit}-b_s)^2}+\frac{2a_s}{v_\text{crit}^3}&=0\\
\frac{2R_sT_\text{crit}}{(v_\text{crit}-b_s)^3}-\frac{6a_s}{v_\text{crit}^4}&=0
\end{aligned}\right\}
\implies
\left\{\begin{aligned}
a_s&=\frac{9R_sT_\text{crit}v_\text{crit}}{8}\\
b_s&=\frac{v_\text{crit}}{3}
\end{aligned}\right.,
:::
where $v_\text{crit}=v(p_\text{crit},T_\text{crit})$ is not the measured value of the critical point but the value implicitly determined from the equation of state at the model predicted critical point
:::{math}
:enumerated: false
p_\text{crit}=\frac{R_sT_\text{crit}}{v_\text{crit}-b_s}-\frac{a_s}{v_\text{crit}^2}.
:::
Substitugint the expressions for $a_s$ and $b_s$ to the equation of state at the model-predicted critical point provides
:::{math}
:enumerated: false
\left.\begin{aligned}
p_\text{crit}&=\frac{R_sT_\text{crit}}{v_\text{crit}-b_s}-\frac{a_s}{v_\text{crit}^2}\\
a_s&=\frac{9R_sT_\text{crit}v_\text{crit}}{8}\\
b_s&=\frac{v_\text{crit}}{3}
\end{aligned}\right\}
\implies
v_\text{crit}=\frac{3}{8}\frac{R_sT_\text{crit}}{p_\text{crit}}.
:::

Substituting the model-predicted critical point specific volume back to the expressions for the Van der Waals coefficients, one finally obtains
:::{math}
:enumerated: false
a_s=\frac{27}{64}\frac{R_s^2T_\text{crit}^2}{p_\text{crit}}, \qquad
b_s=\frac{R_sT_\text{crit}}{8p_\text{crit}}.
:::

::::


(sec-maxwell-construction)=
## <span class="advanced"></span> Estimation of saturation properties with two-parameter equations of state

The predictive capability of the two-parameter equation-of-state models is improved when they are used together with the so-called Maxwell construction which replaces the unphysical portion of the modeled isotherm with a constant-pressure segment, producing a relation of the form $g(p,T)=0$. The associated constraints for the construction are
:::{math}
:label: eq:chap-02:maxwell-construction
\int_{v_\text{liq}(T)}^{v_\text{vap}(T)} p(v,T)dv&=p_\text{sat}(T)(v_\text{vap}(T)-v_\text{liq}(T)),\\
p(v_\text{liq}(T),T)&=p_\text{sat}(T),\\
p(v_\text{vap}(T),T)&=p_\text{sat}(T),
:::
where $p_\text{sat}(T)$ is the model-specific saturation pressure at a temperature $T$ below the critical temperature, reflecting the $g(p,T)=0$ condition. The corresponding model-specific saturated liquid and vapor volumes $v_\text{liq}(T)$ and $v_\text{vap}(T)$ define the phase boundaries between which the two-phase mixture is predicted to exist. Solving the system of equations {eq}`eq:chap-02:maxwell-construction` for a specific equation of state $p(v,T)$ can be performed numerically using iterative methods but the process requires care to avoid the nontrivial solution where $v_\text{vap}(T)=v_\text{liq}(T)$ and $p_\text{sat}(T)$ remains the initial guess. A practical approach involves converting the original system of three equations into a root-finding problem for one equation. 

As seen in {numref}`fig-pv-T-CO2-eos-comparison` for the Redlich-Kwong model, the two-parameter-model isotherms in a $p$-$v$ diagram exhibit a local minimum and maximum in pressure as a function of specific volume in the physically valid region $v>b_s$ when the temperature is below that of the critical point. Geometrically, for a given temperature $T$, the model-specific saturation pressure $p_\text{sat}(T)$ from the Maxwell construction must exist between these local minimum and maximum pressure values and be non-negative. This means 
:::{math}
p_\text{sat}(T)\in[\max(0,p_{\min}(T)),p_{\max}(T)],
:::
where the $p_{\min}(T)$ and $p_{\max}(T)$ are obtained from
:::{math}
\left(\frac{\partial p}{\partial v}\right)_T=0 \quad \implies \quad \left\{\begin{aligned}&v_{\min(p)}(T)\\&v_{\max(p)}(T)\end{aligned}\right. \quad \implies \quad \left\{\begin{aligned}p_{\min}(T)&=p(v_{\min(p)}(T),T)\\p_{\max}(T)&=p(v_{\max(p)}(T),T)\end{aligned}\right.,
:::
with $v_{\min(p)}(T)$ and $v_{\max(p)}(T)$ corresponding to the local pressure minimum and maximum locations for the isotherm $T$. With the model-predicted saturation pressure guaranteed to exist within a fixed interval, one proceeds by guessing a value $p_\text{sat}^\ast(T)$ and solving for specific volumes that satisfy the equation of state. In the physically valid region $v>b_s$, the shape of the isotherm guarantees three roots of which the smallest and largest correspond to the saturated liquid and vapor specific volumes $v_\text{liq}^\ast(T)$ and $v_\text{vap}^\ast(T)$ with respect to the guessed saturation pressure $p_\text{sat}^\ast(T)$ 
:::{math}
p(v,T)=p_\text{sat}^\ast(T) \quad \implies \quad \left\{\begin{aligned}&v_\text{liq}^\ast(T)\\&v_\text{vap}^\ast(T)\end{aligned}\right..
:::
Finally, one evaluates the expression
:::{math}
\Delta^\ast(T)=p_\text{sat}^\ast(T)(v_\text{vap}^\ast(T)-v_\text{liq}^\ast(T))-\int_{v_\text{liq}^\ast(T)}^{v_\text{vap}^\ast(T)} p(v,T)dv,
:::
to check whether $\Delta^\ast(T)=0$. If not, one refines the guess for $p_\text{sat}^\ast(T)$ with an appropriate bracketing method, recomputes $v_\text{liq}^\ast(T)$, $v_\text{vap}^\ast(T)$, and $\Delta^\ast(T)$ and iterates until $\Delta^\ast(T)=0$ is reached.

::::{proof:example}

Finding the local minimum and maximum of a Redlich-Kwong isotherm below the critical temperature is equivalent to solving for the roots of a quartic polynomial
:::{math}
:enumerated: false
&p(v,T)=\frac{R_sT}{v-b_s}-\frac{a_s}{\sqrt{T}v(v+b_s)}\\
&\implies \left(\frac{\partial p}{\partial v}\right)_T=-\frac{R_sT}{(v-b_s)^2}+\frac{a_s}{\sqrt{T}}\frac{2v+b_s}{v^2(v+b_s)^2}\\
&\implies v^4+2\left(b_s-\frac{a_s}{R_sT\sqrt{T}}\right)v^3+b_s^2\left(1+\frac{3a_s}{b_sR_sT\sqrt{T}}\right)v^2-\frac{a_sb_s^3}{R_sT\sqrt{T}}=0.
:::
After solving for the roots and selecting $v_{\min(p)}(T)$ and $v_{\max(p)}(T)$ from them, the corresponding pressure values $p_{\min}(T)$ and $p_{\max}(T)$ are obtained. After a value $p_\text{sat}^\ast(T)$ for the saturation pressure has been guessed, the specific volumes satisfying the Redlich-Kwong equation of state are found as roots of a cubic polynomial
:::{math}
:enumerated: false
&p_\text{sat}^\ast(T)=\frac{R_sT}{v-b_s}-\frac{a_s}{\sqrt{T}v(v+b_s)}\\
&\implies v^3-\frac{R_sT}{p_\text{sat}^\ast(T)}v^2+\left(\frac{a_s}{p_\text{sat}^\ast(T)\sqrt{T}}-\frac{R_sTb_s}{p_\text{sat}^\ast(T)}-b_s^2\right)v-\frac{a_sb_s}{p_\text{sat}^\ast(T)\sqrt{T}}=0.
:::
The roots provide the values $v_\text{liq}^\ast(T)$ and $v_\text{vap}^\ast(T)$. One may then analytically calculate the integral
:::{math}
:enumerated: false
\int_{v_\text{liq}^\ast(T)}^{v_\text{vap}^\ast(T)} p(v,T)dv&=R_sT\ln\left(\frac{v_\text{vap}^\ast(T)-b_s}{v_\text{liq}(T)-b_s}\right)\\
&\quad-\frac{a_s}{b_s\sqrt{T}}\ln\left(\frac{v_\text{vap}^\ast(T)}{v_\text{liq}^\ast(T)}\frac{v_\text{liq}^\ast(T)+b_s}{v_\text{vap}^\ast(T)+b_s}\right),
:::
and evaluate the expression
:::{math}
:enumerated: false
\Delta^\ast(T)=p_\text{sat}^\ast(T)(v_\text{vap}^\ast(T)-v_\text{liq}^\ast(T))-\int_{v_\text{liq}^\ast(T)}^{v_\text{vap}^\ast(T)} p(v,T)dv.
:::

The algorithm can now be programmed into a python scipt that uses the methods roots and brentq from numpy and scipy libraries to find roots of polynomials and bracket roots of nonlinear functions

```{literalinclude} python/example-redlich-kwong-saturation.py
:language: python
:start-line: 0
:end-line: 63
:linenos:
```

Running the script results in Redlich-Kwong estimates $p_\text{sat}(12^\circ\text{C})=50.9\,\text{bar}$, $v_\text{liq}(12^\circ\text{C})=1.47\,\ell/\text{kg}$, and $v_\text{vap}(12^\circ\text{C})=6.28\,\ell/\text{kg}$ that are reasonably close to the measured values, as visible from the figure below. 

:::{image} ./figs/example-fig-redlich-kwong-saturation-annotated.svg
:align: center
:width: 95%
:::

::::


(sec-pyromat-coolprop)=
## <span class="elementary"></span> Pyromat and CoolProp data libraries
Engineering applications such as steam power plants and heat pumps involve not only the gaseous phase of substances but also the liquid phase and the liquid-vapor phase mixture. While the two-parameter models have historical value in predicting parameter regimes needed for designing experimental measurements, they lack the accuracy needed in the most demanding of the applications. Fortunately, the theoretical framework of thermodynamics enables constructing multiparameter substance models that can be fitted to experimental data with good accuracy. Several libraries and software implementations of such models exist. The ones introduced here are [pyromat](https://pypi.org/project/PYroMat/) and [coolprop](https://pypi.org/project/CoolProp/), which both are open source, offer a user-friendly python interface, and have extensive documentation. Both libraries can be installed using pip, the package installer for python.

To use pyromat, one imports the library and reverts to SI-units, if desired. By default, pyromat uses non-SI units for pressure (bar), molar quantities (kmol), and energy (kJ). In engineering applications, such units are often common, though. Then one instantiates a multiphase model for the desired substance and computes thermodynamic quantities by calling individual quantity methods such as p (pressure), v (specific volume), d (density), T (temperature), and x (vapor quality) or by calling the state method that evaluates all quantities from a given input quantity pair: 

```{literalinclude} python/example-pyromat-pvTx.py
:language: python
:start-line: 0
:end-line: 21
:linenos:
```

The library has separate methods for critical point and triple line information, and for evaluation of saturation properties given only temperature (or pressure):

```{literalinclude} python/example-pyromat-pvTx.py
:language: python
:start-line: 23
:end-line: 33
:linenos:
:lineno-match:
```

The acceptable input parameter pairs for the methods, that can be formed from the state variables $p$, $v$, $\rho$, $T$, and $x$, are listed in {numref}`tab:chap-02:pyromat-variable-pairs` together with their applicability domains (single-phase or two-phase). The full documentation and introdyctory tutorial are available at [http://pyromat.org/documentation.html](http://pyromat.org/documentation.html).

:::{table} Acceptable pyromat input parameter pairs formable from the variables $p$, $v$, $\rho$, $T$, and $x$.
:label: tab:chap-02:pyromat-variable-pairs
:align: center
:class: booktabs

| Variable pair | Input pair | Single-phase | Two-phase |
|:---|:---|:---:|:---:|
| $(p,T)$ | p and T | Yes | No |
| $(\rho,T)$ | d and T | Yes | Yes |
| $(v, T)$ | v and T | Yes | Yes |
| $(\rho, p)$ | d and p | Yes | Yes |
| $(v, p)$ | v and p | Yes | Yes |
| $(x, T)$ | x and T | No | Yes |
| $(x, p)$ | x and p | No | Yes |
:::


To use coolprop, one imports both the library and a specific AbstractState class from it. The SI-units will be used by default, needing no specific configuration. A multiphase model for the desired substance is then instantiated from the AbstractState class. Before any thermodynamic quantities can be computed, though, the substance state has to be specified. This happens by calling the method update and passing it not only the variables but also an input key that informs the library which variables have been passed. Once the state has been updated, quantity values are accessed through separate methods such as p (pressure), T (temperature), rhomass (density), and Q (vapor quality).

```{literalinclude} python/example-coolprop-pvTx.py
:language: python
:start-line: 0
:end-line: 13
:linenos:
:lineno-match:
```

Like pyromat, also coolprop has methods for critical point and triple line information, although with different syntax. However, coolprop does not have separate methods for saturation properties. Instead, they are evaluated by pairing vapor quality and temperature as inputs.

```{literalinclude} python/example-coolprop-pvTx.py
:language: python
:start-line: 15
:end-line: 31
:linenos:
:lineno-match:
```

The acceptable input parameter pairs and their corresponding input keys for the update-method, that can be formed from the state variables $p$, $v$, $\rho$, $T$, and $x$, are listed in {numref}`tab:chap-02:coolprop-variable-pairs`. The full documentation is available at [https://coolprop.org](https://coolprop.org).

:::{table} Acceptable coolprop input parameter pairs from the variables $p$, $v$, $\rho$, $T$, and $x$ and the required key. Applicability domain of the pairs.
:label: tab:chap-02:coolprop-variable-pairs
:align: center
:class: booktabs

| Variable pair | Input Key | Single-phase | Two-phase |
|:---|:---|:---:|:---:|
| $(p,T)$ | PT\_INPUTS | Yes | No |
| $(\rho,T)$ | DmassT\_INPUTS | Yes | Yes |
| $(\rho, p)$ | DmassP\_INPUTS | Yes | Yes |
| $(x, T)$ | QT\_INPUTS | No | Yes |
| $(p, x)$ | PQ\_INPUTS | No | Yes |
| $(\rho, x)$ | DmassQ\_INPUTS | No | Yes for $\rho<\rho_c$ |
:::



## <span class="advanced"></span> Plotting phase diagrams with data libraries
The pyromat-library accepts input as scalars, as numpy-arrays, or as a mixture of the two. The output is always a numpy-array, even in case of scalar input. This enables convenient data queries for multiple states with one call but must be kept in mind if outputs from scalar input queries are used in further calculations that do not accept or accept numpy-arrays. The array inputs and outputs are particularly useful for visualization of the data, as demonstrated in {numref}`plot-isotherms-saturation-curve`. 

(plot-isotherms-saturation-curve)=
::::{proof:example}

Selected isotherms together with the saturation curves can be conveniently drawn into a $p$-$v$ diagram using the in vectorized output from pyromat. To properly handle the potential two-phase region, values on the saturation curves are queried separately and added to the vectors using the concatenate method from numpy in the following manner:
```{literalinclude} python/example-pyromat-pv-isotherms-and-saturation-curve.py
:language: python
:start-line: 0
:end-line: 53
:linenos:
```

Running the script results in a figure shown below:

:::{image} ./figs/example-fig-pyromat-pv-isotherms-and-saturation-curve.svg
:align: center
:width: 95%
:::

::::

Unlike pyromat, coolprop does not support numpy-arrays. Hence all inputs and outputs are always scalar-valued. On the other hand, coolprop provides a large collection of different substances while pyromat presently has only a few different substances implemented. Both libraries have their uses, and are best learned by practicing.


## <span class="elementary"></span> Thermal expansion and compressibility coefficients
The relations between the state variables $p$, $v$, and $T$ can be approximated with the simple equations of state from {numref}`sec-simple-equations-of-state` or evaluated accurately with the data libraries introduced in {numref}`sec-pyromat-coolprop`. The framework outlined in {numref}`fig-roadmap`, however, contains not only $p$, $v$, and $T$ but also energy-related quantities such as internal energy $u$, enthalpy $h$, and entropy $s$ that are needed in practical calculations involving power plants and heat pumps. Unlike $p$, $v$, and $T$, the energy-related quantities cannot be obtained from direct measurements. Instead, their experimental determination relies on observing how the measurable variables $p$, $v$, and $T$ change relative to each other when a substance is heated or compressed. 

In single-phase regions, where pressure, specific volume, and temperature relate to each other via the surface equation $f(p,v,T)=0$, such changes are described with the isobaric thermal expansion coefficient $\beta_p$ and the isothermal compressibility coefficient $\kappa_T$ that are defined as relative changes in volume with respect to temperature and pressure

:::{math}
\beta_p=\frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_p=-\frac{1}{\rho}\left(\frac{\partial \rho}{\partial T}\right)_p,\\
:::
:::{math}
\kappa_T=-\frac{1}{v}\left(\frac{\partial v}{\partial p}\right)_T=\frac{1}{\rho}\left(\frac{\partial \rho}{\partial p}\right)_T.
:::


The coefficient $\beta_p$ can be determined by measuring the volume of a substance at several temperatures while keeping the pressure constant, and the coefficient $\kappa_T$ by measuring volume at several pressures while temperature is fixed. They can therefore be determined from existing $p$-$v$ and $v$-$T$ diagrams by examining the slopes of the isotherms and isobars, or calculated more accurately with the help of the data libraries. For most substances $\beta_p>0$ and $\kappa_T>0$, meaning that volume typically increases with temperature at constant pressure and decreases with pressure at constant temperature.

In the two-phase mixture region, pressure and temperature on the $p$-$v$-$T$ surface are not independent but satisfy the saturation relation of the form $g(T,p)=0$. Consequently, the usual definitions of $\beta_p$ and $\kappa_T$ as independent single-phase response coefficients do not apply. The slope of the coexistence curve

:::{math}
\left(\frac{dp}{dT}\right)_{\text{sat}},
:::

nevertheless characterises how pressure and temperature vary along the two-phase equilibrium states.


In applications, measured values for the heat expansion and compressibility coefficients can be leveraged also to estimate changes in the state variables. In single phase regions, specific volume can be interpreted as a function $v(p,T)$ of pressure and temperature. Differentiating the function results in the total differential for specific volume

:::{math}
dv&=\left(\frac{\partial v}{\partial T}\right)_pdT+\left(\frac{\partial v}{\partial p}\right)_Tdp\\
&=v\beta_pdT-v\kappa_T dp.
:::

Small changes $\Delta p=p_1-p_0$ and $\Delta T=T_1-T_0$ in pressure and temperature from a reference state $(p_0,T_0,v_0)$ therefore provide a small change $\Delta v=v_1-v_0$ in specific volume, which can be approximated with the relation

:::{math}
\frac{\Delta v}{v_0}\approx \beta_p|_{(p_0,T_0)}\Delta T-\kappa_T|_{(p_0,T_0)} \Delta p.
:::


::::{proof:example}
For water at pressure of $225\,\text{bar}$ and temperature of $376^\circ\text{C}$, one may draw tangents to the corresponding isotherm and isobar in the $p$-$v$ and $v$-$T$ diagrams and estimate the tangent slopes from the resulting triangles as below 

:::{image} ./figs/example-fig-kappa-pv-annotated.svg
:align: center
:width: 90%
:::

:::{image} ./figs/example-fig-beta-vT-annotated.svg
:align: center
:width: 90%
:::

The isobaric thermal expansion coefficient and the isothermal compressibility coefficient at the specified state are then calculated to be
:::{math}
:enumerated: false
\beta_p&\approx\frac{1}{v}\frac{\Delta v}{\Delta T}=0.263\,\text{K}^{-1}\\
\kappa_T&\approx-\frac{1}{v}\frac{\Delta v}{\Delta p}=0.119\,\text{bar}^{-1}
:::
::::

::::{proof:example}

An adjustable cylinder with a reference volume of $V_0=25.8\,\ell$ contains $6\,\text{kg}$ of unknown substance at a temperature of $T_0=162^\circ\text{C}$. At this state, the isobaric thermal expansion and isothermal compressibility coefficients have been experimentally determined to be $\beta_p=0.031\,\text{K}^{-1}$ and $\kappa_T=0.015\,\text{bar}^{-1}$. 

If the cylinder volume is held fixed ($\Delta V=0$) while the temperature increases by $\Delta T=1^\circ\text{C}$, the resulting change in the pressure will be approximately
:::{math}
:enumerated: false
&\frac{\Delta V}{V_0}=\beta_p\Delta T-\kappa_T\Delta p,\\
&\implies \Delta p\approx \frac{\beta_p}{\kappa_T}\Delta T=2.067\,\text{bar}.
:::
If the cylinder volume is compressed by $\Delta V=-1.3\,\ell$ and the pressure is observed to increase by $\Delta p=8.8\,\text{bar}$, the resulting change in temperature will be approximately
:::{math}
:enumerated: false
&\frac{\Delta V}{V_0}=\beta_p\Delta T-\kappa_T\Delta p,\\
&\implies \Delta T=\frac{1}{\beta_p}\frac{\Delta V}{V_0}+\frac{\kappa_T}{\beta_p}\Delta p=2.633^\circ\text{C}.
:::
::::


::::{proof:example}

The isobaric thermal expansion coefficient $\beta_p$ and the isothermal compressibility coefficient $\kappa_T$ can be computed with pyromat or coolprop

Coolprop offers direct methods for evaluating the coefficients:

```{literalinclude} python/example-beta-kappa-pyromat-coolprop.py
:language: python
:start-line: 29
:end-line: 47
:linenos:
```

Running the script provides values $\beta_p = 0.262058\,\text{K}^{-1}$ and $\kappa_T = 0.11624\,\text{bar}^{-1}$. Pyromat does not offer direct methods but one may approximate derivatives with a finite difference rule $df/dx\approx (f(x+\delta x)-f(x))/\delta x$ using a small enough step size:

```{literalinclude} python/example-beta-kappa-pyromat-coolprop.py
:language: python
:start-line: 0
:end-line: 27
:linenos:
:lineno-match:
```

Running the script results in $\beta_p = 0.261266\,\text{K}^{-1}$ and $\kappa_T= 0.116053\,\text{bar}^{-1}$ that are very close to the estimates obtained with coolprop. Values from both libraries are close to the values obtained visually from the $p$-$v$ and $v$-$T$ diagrams.

::::

## <span class="intermediate"></span> Differential relations between state variables

The isobaric thermal expansion coefficient $\beta_p$ and the isothermal compressibility coeffcient $\kappa_T$ that describe the relative changes in volume with respect to temperature and pressure, respectively, are examples of differential relations between the state variables applicable in single-phase regions. They are not the only differential relations, though, as one could equally investigate the differential dependency of pressure on temperature at a fixed volume. It turns out, however, that all other derivatives can be expressed in terms of $\beta_p$ and $\kappa_T$.

Assuming the existence of a smooth $p$-$v$-$T$ surface represented by the single-phase equation $f(p,v,T)=0$, one may, at least locally, define any of the functions $p(v,T)$, $v(T,p)$, and $T(p,v)$. Calculating total differentials of these functions, one finds the following relations between the differential changes in pressure, specific volume, and temperature

:::{math}
dp=\left(\frac{\partial p}{\partial v}\right)_Tdv+\left(\frac{\partial p}{\partial T}\right)_v dT,\\
:::
:::{math}
dv=\left(\frac{\partial v}{\partial T}\right)_pdT+\left(\frac{\partial v}{\partial p}\right)_T dp,\\
:::
:::{math}
dT=\left(\frac{\partial T}{\partial p}\right)_vdp+\left(\frac{\partial T}{\partial v}\right)_p dv.
:::

As the differentials $dp$, $dv$, and $dT$ are the same on both sides of the equations, one may algebraically rearrange the equations and find relations between the partial derivatives. For example, one may manipulate the differential resulting from the function $v(T,p)$ into

:::{math}
dv&=\left(\frac{\partial v}{\partial T}\right)_pdT+\left(\frac{\partial v}{\partial p}\right)_T dp & &\implies & &\left\{\begin{aligned}
dp&=\frac{1}{\left(\frac{\partial v}{\partial p}\right)_T}dv-\frac{\left(\frac{\partial v}{\partial T}\right)_p}{\left(\frac{\partial v}{\partial p}\right)_T}dT,\\
dT&=\frac{1}{\left(\frac{\partial v}{\partial T}\right)_p}dv-\frac{\left(\frac{\partial v}{\partial p}\right)_T }{\left(\frac{\partial v}{\partial T}\right)_p}dp.\end{aligned}\right.
:::

Comparing the manipulated expressions with the differentials resulting directly from differentiation of the functions $p(v,T)$ and $T(p,v)$, one identifies relations between the partial derivatives and confirms them to be expressible in terms of $\beta_p$ and $\kappa_T$. For example the different expressions for pressure differential $dp$ provide
:::{math}
\left.\begin{aligned}
dp&=\frac{1}{\left(\frac{\partial v}{\partial p}\right)_T}dv-\frac{\left(\frac{\partial v}{\partial T}\right)_p}{\left(\frac{\partial v}{\partial p}\right)_T}dT\\
dp&=\left(\frac{\partial p}{\partial v}\right)_Tdv+\left(\frac{\partial p}{\partial T}\right)_v dT\end{aligned}\right\}
\implies 
\left\{\begin{aligned}
\left(\frac{\partial p}{\partial T}\right)_v&=-\frac{\left(\frac{\partial v}{\partial T}\right)_p}{\left(\frac{\partial v}{\partial p}\right)_T}=\frac{\beta_p}{\kappa_T},\\
\left(\frac{\partial p}{\partial v}\right)_T&=\frac{1}{\left(\frac{\partial v}{\partial p}\right)_T}=-\frac{1}{v\kappa_T},
\end{aligned}\right.
:::
while the different expressions for temperature differential $dT$ provide
:::{math}
\left.\begin{aligned}
dT&=\frac{1}{\left(\frac{\partial v}{\partial T}\right)_p}dv-\frac{\left(\frac{\partial v}{\partial p}\right)_T }{\left(\frac{\partial v}{\partial T}\right)_p}dp,\\
dT&=\left(\frac{\partial T}{\partial p}\right)_vdp+\left(\frac{\partial T}{\partial v}\right)_p dv\end{aligned}\right\}
\implies 
\left\{\begin{aligned}
\left(\frac{\partial T}{\partial v}\right)_p&=-\frac{\left(\frac{\partial v}{\partial p}\right)_T}{\left(\frac{\partial v}{\partial T}\right)_p}=\frac{\kappa_T}{\beta_p},\\
\left(\frac{\partial T}{\partial p}\right)_v&=\frac{1}{\left(\frac{\partial v}{\partial T}\right)_p}=\frac{1}{v\beta_p}.
\end{aligned}\right.
:::

The mutual derivatives between $p$, $v$, and $T$ are therefore all expressible in terms of $\beta_p$ and $\kappa_T$ and related to each other. Particularly one finds that for any permuted combination of $\{x,y,z\}\in\{p,v,T\}$ with $x\neq y\neq z$, one finds two useful rules
:::{math}
\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial x}\right)_z=1, \qquad \left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y=-1.
:::

::::{proof:example}

The formula containing the product of three permuted partial derivatives can be verified using coolprop. For water at $p=225\,\text{bar}$ and $T=376^\circ\text{C}$ one may calculate the partial derivatives with the following script:
```{literalinclude} python/example-partial-derivatives-coolprop.py
:language: python
:start-line: 0
:end-line: 26
:linenos:
:lineno-match:
```

Running the script results in the values
:::{math}
:enumerated: false
\left(\frac{\partial p}{\partial T}\right)_\rho&=2.25445\,\text{bar}\,\text{K}^{-1}\\
\left(\frac{\partial T}{\partial \rho}\right)_p&= -0.0153139\,\text{K}\,\text{m}^3\,\text{kg}^{-1}\\
\left(\frac{\partial \rho}{\partial p}\right)_T& = 28.9651\,\text{kg}\,\text{m}^{-3}\,\text{bar}^{-1}
:::
Confirming that the triple product between the partial derivatives is valid
:::{math}
:enumerated: false
\left(\frac{\partial p}{\partial T}\right)_\rho \left(\frac{\partial T}{\partial \rho}\right)_p \left(\frac{\partial \rho}{\partial p}\right)_T=-1
:::
::::

## <span class="elementary"></span> Compressibility factor, reduced variables, and the principle of corresponding states
Where data libraries provide high accuracy, the ideal gas model can remain a convenient tool for rapid engineering estimates and analytical derivations due to its mathematical simplicity. To determine when the ideal gas model can be expected to perform sufficiently well, the so-called compressibility factor 
:::{math}
Z = \frac{pv}{R_sT},
:::
can be used as a dimensionless metric to quantify deviation from ideal behaviour. As the name suggests, the factor compares the volume $v$ the substance occupies in relation to the volume $R_sT/p$ an ideal gas at the same temperature and pressure would occupy. The closer the value of $Z$ is to unity, the better the ideal gas model is expected to describe the substance properties. On the other hand, if $Z$ clearly deviates from unity, then the ideal gas model likely should be abandoned in favor of the more complex equations of state or data libraries. For water, the $Z$-value is illustrated in a $v$-$T$ diagram in {numref}`fig-vT-Z-H2O`.

:::{figure} ./figs/fig-vT-Z-H2O.svg
:label: fig-vT-Z-H2O
:align: center
:width: 90%
The value of compressibility factor for water.
:::

Diagrams involving the compressibility factor are usually expressed in terms of the so-called reduced variables that are dimensionless and normalized to the critical state values

:::{math}
T_r=\frac{T}{T_\text{crit}},\qquad
p_r=\frac{p}{p_\text{crit}},\qquad
v_r=\frac{v}{v_\text{crit}}.
:::

When illustrated for different substance, as in {numref}`fig-compressibility-factor` for methane $\text{CH}_4$, nitrogen $\text{N}_2$, and carbon dioxide $\text{CO}_2$, the compressibility factor reveals approximately similar behaviour for many substances, even with significantly different critical states. Even the phase transitions across the liquid-vapor two-phase state, visible on the diagram as strictly vertical segments, seem similar for different substances. 

:::{figure} ./figs/fig-compressibility-factor.svg
:label: fig-compressibility-factor
:align: center
:width: 90%
Selected reduced temperature ($T_r$) isotherms of common gases illustrating the similarity of $Z$ of the gases.
:::


This observation is referred to as the principle of corresponding states and it tells that many fluids have approximately similar compressibility factors and deviate from ideal to roughly same degree when compared at the same reduced temperature and pressure. It is for this reason that the Van der Waals, Dieterici, and Redlich-Kwong equations of state can be applied to many substances with relatively good accuracy. The observation can also be used to estimate properties of a substance with respect to some other substance that behaves similarly in reduced coordinates.
::::{proof:example}
In the {numref}`example-vdw-coefficients`, the parameters $a_s$, $b_s$ and the model-specific critical volume $v_\text{crit}$ for the Van der Waals model were shown to be
:::{math}
:enumerated: fale
a_s=\frac{27}{64}\frac{R_s^2T_\text{crit}^2}{p_\text{crit}}, \qquad b_s=\frac{1}{8}\frac{R_sT_\text{crit}}{p_\text{crit}}, \qquad v_\text{crit}=3b_s.
:::
Writing the Van der Waals equation in terms of reduced variables provides
:::{math}
:enumerated: false
p_\text{crit}p_r=\frac{R_sT_\text{crit}T_r}{v_\text{crit}v_r-b_s}-\frac{a_s}{v_\text{crit}^2}\frac{1}{v_r^2}.
:::
Substituting $a_s$, $b_s$, and $v_\text{crit}$ then provides
:::{math}
:enumerated: false
p_r=\frac{8T_r}{3v_r-1}-\frac{3}{v_r^2}.
:::
In terms of reduced variables, the Van der Waals equation is seen to contain no substance-dependent parameters. The same applies also to Redlich-Kwong and Dieterici equations of state. All substances that are reasonably well approximated with any of these model are therefore immerdiately observed to obey the principle of corresponding states.
::::

::::{proof:example}
In {numref}`fig-compressibility-factor`, carbon dioxide and methane are observed to have similar compressibility factors in terms of reduced variables. One should therefore be able to use state variable data of methane to estimate the state variables of carbon dioxide, and vice versa. 

Given the critical point temperature $T_{\text{crit},\text{CO}_2}$ and density $\rho_{\text{crit},\text{CO}_2}$ for carbon dioxide, a temperature $T_{\text{CO}_2}$ and density $\rho_{\text{CO}_2}$ define reduced variables
:::{math}
:enumerated: false
T_r=\frac{T_{\text{CO}_2}}{T_{\text{crit},\text{CO}_2}}, \qquad \rho_r=\frac{\rho_{\text{CO}_2}}{\rho_{\text{crit},\text{CO}_2}}.
:::
Given the critical point temperature $T_{\text{crit},\text{CH}_4}$ and density $\rho_{\text{crit},\text{CH}_4}$ for methane, the corresponding state temperature $T_{\text{CH}_4}$ and density $\rho_{\text{CH}_4}$ of methane are
:::{math}
:enumerated: false
T_{\text{CH}_4}=T_rT_{\text{crit},\text{CH}_4}, \qquad \rho_{\text{CH}_4}=\rho_r\rho_{\text{crit},\text{CH}_4}.
:::
Using these values, the corresponding state pressure $p_{\text{CH}_4}$ for methane can be calculated with data libraries. Given the critical point pressure $p_{\text{crit},\text{CH}_4}$ for methane, the corresponding state reduced pressure is then found from 
:::{math}
:enumerated: false
p_r=\frac{p_{\text{CH}_4}}{p_{\text{crit},\text{CH}_4}}.
:::
With the reduced pressure known the critical point pressure $p_{\text{crit},\text{CO}_2}$ of carbon dioxide can be used to estimate the carbon dioxide pressure
:::{math}
:enumerated: false
p_{\text{CO}_2}=p_rp_{\text{crit},\text{CO}_2}.
:::

This process is implemented in the script below to estimate the pressure $p_{\text{CO}_2}$ of carbon dioxide at a temperature of $T_{\text{CO}_2}=20^\circ\text{C}$ and density of $\rho_{\text{CO}_2}=230\,\text{kg}\,\text{m}^{-3}$. The estimate is also compared to accurate value and ideal gas estimate.

```{literalinclude} python/example-corresponding-states.py
:language: python
:start-line: 0
:end-line: 40
:linenos:
:lineno-match:
```

Running the script results in the following pressure values for carbon dioxide 
:::{math}
:enumerated: false
p_{\text{CO}_2,\text{corr. state value}} &= 59.3999\,\text{bar}\\
p_{\text{CO}_2,\text{accurate value}} &= 57.2904\,\text{bar}\\
p_{\text{CO}_2,\text{ideal gas value}} &= 127.38\,\text{bar}
:::

The value estimated with the principle of corresponding states is quite close to the correct value, while the ideal gas estimate is far off.
::::



## Summary
Pure substances, such as oxygen, carbon dioxide, and distilled water, exhibit qualitatively similar phase behaviour despite having widely different critical temperatures and pressures. Their thermodynamic states can be mapped experimentally in $p$-$v$-$T$ space and represented in projections such as $p$-$v$ and $v$-$T$ diagrams. Simple two-parameter equations of state, such as the Van der Waals model, can reproduce the main features of this behaviour, while multi-parameter equations of state implemented in data libraries such as pyromat and provide accurate property data.

For two-parameter equations of state, the model parameters can be related to the critical state by requiring the isotherm to have a stationary inflection point at the critical point. Measured critical-state data can then be used to determine the model parameters, or the parameters can be estimated from measurements away from the critical point. Together with the Maxwell construction, a two-parameter model can also be used to estimate saturation states. The approximately universal behaviour of different substances can be illustrated using reduced variables and the compressibility factor which reveals similar behaviour for different fluids at corresponding reduced temperatures and pressures.

The thermodynamic state can also be described locally through differential response coefficients. The isobaric thermal expansion coefficient $\beta_p$ and the isothermal compressibility $\kappa_T$ characterize the response of specific volume to changes in temperature and pressure, respectively. Both can be estimated from local slopes in $p$-$v$ and $v$-$T$ diagrams or calculated directly from property data. These coefficients will later provide the connection between experimentally measured thermodynamic response and the differential relations needed to construct the thermodynamic framework.

