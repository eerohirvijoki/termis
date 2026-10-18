# State of Pure Substances
In this chapter, relations between the state variables of pure substances are first illustrated with phase diagrams. Then mathematical expressions and numerical libraries are introduced to model the experimentally observed state relations with equations of state. Finally, computation of quantities needed in developing the thermodynamic theory is discussed.

## Learning goals

- This is 
- a list of
- learning goals

## <span class="elementary"></span> The p-v-T phase diagram
In mechanics, matter is classified into solid states that can sustain shape under shearing forces and into fluid states that cannot. In thermodynamics, fluid states are classified not only into liquid and gas states but subclassified further into superheated vapor and supercritical fluid states. In short, superheated vapor is gaseous while supercritical fluid has characteristics of both liquid and gas. Also mixtures of solid, liquid, and gas states in common thermodynamic equilibrium are encountered. 

## <span class="elementary"></span> The p-v and v-T diagrams, vapor quality
Most engineering applications involve fluids at pressures above that of the triple line. To represent the fluid state and the associated isotherms and isobars quantitatively, the 

## <span class="elementary"></span> Equations of state
Mathematically, a general two-dimensional surface in a three-dimensional space with coordinates 

::::{proof:example}
:label: vdw-ideal-gas-limit
Writing the Van der Waals model as

$$
(p+a_s\rho^2)(v-b_s)=R_sT,
$$

one can interpret the parameter $a_s$ as a correction to pressure associated with intermolecular interactions that scale quadratically with respect to gas density. The parameter $b_s$ can be interpreted to account for reduction in accessible volume due to finite molecular size.

Writing the equation further as

$$
pv\left(1+\frac{a_s\rho^2}{p}\right)
\left(1-\frac{b_s}{v}\right)=R_sT,
$$

one observes the Van der Waals model to reduce to the ideal gas equation when both $p\gg a_s\rho^2$ and $v\gg b_s$ hold true.
::::


## <span class="advanced"></span> Numerical libraries
Engineering applications such as steam power plants and heat pumps involve not only the gaseous phase of substances but also the liquid phase and the liquid-vapor phase mixture. While the two-parameter models have historical value in predicting parameter regimes needed for designing experimental measurements, they lack the accuracy needed in the most demanding of the applications. Fortunately, the theoretical framework of thermodynamics enables constructing multiparameter substance models that can be fitted to experimental data with good accuracy. Several libraries and software implementations of such models exist. 

## <span class="elementary"></span> Thermal expansion and compressibility coefficients
The thermodynamic framework outlined in Fig. XX

## <span class="intermediate"></span> Compressibility factor and reduced variables
While numerical libraries provide high accuracy, the ideal gas model remains a convenient tool for rapid engineering estimates and analytical derivations due to its mathematical simplicity. 

## <span class="elementary"></span> Summary
Pure substances, such as oxygen, carbon dioxide, and distilled water,
exhibit qualitatively similar phase behaviour despite having widely
different critical temperatures and pressures. 
