# Mechanics of fluids
The equations of motion describing the evolution of simple fluids, as those often encountered in engineering applications, are derived here. The derivation process involves first introducing the Leibniz rule for differentiating integrals, and then applying it to the conservation laws of mass, momentum, and energy. The process is mathematically more involved than what is typically encountered in thermodynamics courses, and is not expected to be digested fully during first reading. Instead, the purpose of this chapter is to build a detailed and rigorous enough of a foundation that can be later recalled and leveraged together with thermodynamic relations to analyze common engineering applications. 

## Learning goals

- This is 
- a list of
- learning goals


## <span class="intermediate"></span> The flow map of a vector field
Assume the vector field 

## <span class="intermediate"></span> Differential line-, surface, and volume elements
Consider a coordinate triplet 

## <span class="advanced"></span> Rank-2 tensors
Similarly as the initial position of a pollen grain dropped into a flowing fluid is mapped into a new position over time, also the vectors 

## <span class="advanced"></span> Evolution of differential elements
Now return to the expression 

## <span class="advanced"></span> Leibniz rule for differentiating integrals
Deriving equations for the evolution of fluid quantities requires differentiating volume integrals over domains that flow with the fluid velocity 

## <span class="elementary"></span> Conservation of mass
Consider a volume 

## <span class="elementary"></span> Conservation of momentum
According to Newton's second law, the rate of change of linear momentum of a body equals the net forces acting on it. The forces acting on a volume of fluid include gravity that is distributed throughout the fluid volume, and mechanical contact force that is distributed on the surface of the body. Since the total force must be finite, yet distributed over the body volume and surface, both the body and surface force need to be treated differentially while the total force is an integral of the differential force. 


## <span class="elementary"></span> Conservation of angular momentum
For point masses, the definition 

## <span class="elementary"></span> Conservation of energy
A differential volume 

## <span class="elementary"></span> Constitutive relations for stress and heat flux
The conservation principles of mass, momentum, and energy discussed above lead to local differential equations from which the local time rate of change of fluid's density, velocity, and internal energy ought to be computed. 

## <span class="elementary"></span> Summary
The motion of a fluid can be described by following individual points along the flow and studying how differential line, surface, and volume elements evolve. 
