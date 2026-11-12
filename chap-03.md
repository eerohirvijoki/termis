---
numbering:
  enumerator: "3.%s"
  heading_1: true
  heading_2: true
  heading_3: true
---

# 3 Mechanics of fluids
This chapter derives the partial differential equations that describe the time evolution of a fluid's density $\rho(\bm{x},t)$, velocity $\bm{v}(\bm{x},t)$, and specific internal energy $u(\bm{x},t)$ as scalar and vector valued fields dependent on location $\bm{x}$ and time $t$. Later, these equations are used to formulate control-volume engineering models for analysis of power plant and refrigeration systems. The positioning of this chapter within the overall roadmap is illustrated in {numref}`fig-roadmap-chap-03`.

:::{figure} ./figs/fig-roadmap-chap-03.svg
:label: fig-roadmap-chap-03
:align: center
:width: 100%
The positioning of the chapter content with respect to the roadmap.
:::

The derivation of the evolution equations builds on the Leibniz rule for differentiating integrals over time-evolving volumes. Combined with the principles of mass, momentum, and energy conservation, the Leibniz rule enables conversion of fundamental physics principles to locally applicable partial differential equations for the fluid state fields. The discussion focuses on simple fluids often encountered in engineering applications, and the constitutive relations for stress and heat flux are motivated by experimental observations. As a concluding note, the set of partial differential equations obtained from the conservation principles is observed to contain more variables than there are equations for, necessitating a thermodynamic closure via state relations before practical energy engineering applications can be analyzed.

The application of the Leibniz rule to conservation principles involves standard vector calculus tools, such as the divergence theorem, and constitutes core knowledge for engineers. When applying the rule to the principles of momentum and energy conservation, the contact forces that contribute to the time rate of change of momentum and rate of mechanical work on surfaces are expressed in terms of a stress tensor. As tensors are typically not covered during ordinary differential and integral calculus classes, the chapter includes a brief introduction to them before presenting and interpreting the Leibniz rule.

As supplements to the core knowledge, the chapter includes a full derivation of the Leibniz rule, establishes the stress tensor as a physical necessity dictated by Newton's second law to describe contact forces on surfaces, and justifies the symmetry of the stress tensor by conservation of angular momentum. These intermediate and advanced topics are designed for readers seeking deeper theoretical foundation and are not expected to be fully mastered on a first reading. Readers primarily interested in the core engineering path may skip the intermediate and advanced sections and focus on the derivation process of the evolution equations.


## Learning goals

- This is 
- a list of
- learning goals


## <span class="elementary"></span> Tensors of rank-2
In fluid and solid mechanics, forces on surfaces that result from contact of material bodies require infinitesimal representation
:::{math}
:label: eq-differential-surface-force
\delta\bm{F}_s=\bm{t}dA.
:::
Here $dA$ is a differential area the differential contact force $\delta\bm{F}_s$ acts on while $\bm{t}$ is the traction describing the local direction and magnitude for the force per unit area, having units of $\text{Pa}$. This setting is illustrated in {numref}`fig-surface-force`. The traction is a vector field and expressed generally as $\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}$, with $\bm{\sigma}$ a rank-2 tensor field referred to as stress, and the dot $(\cdot)$ representing tensor-vector contraction. This representation for contact forces is a direct consequence of Newton's second law and proved rigorously in {numref}`sec-stress-tensor`. 
:::{figure} ./figs/fig-surface-force.svg
:label: fig-surface-force
:align: center
:width: 50%

A differential surface force $\delta \bm{F}_s$ acting on a differential area $dA$ oriented with respect to an outward unit normal vector $\bm{\hat{n}}$ on a surface of a solid or fluid body.
:::

To apply the differential contact force and to study the principles of conservation of momentum and energy, one must first understand what kind of a mathematical object a rank-2 tensor field is, how it acts on vector fields through the contraction operator $(\cdot)$, and what calculus rules apply to it.

In Cartesian coordinates $\{x_i\}_{i=1}^3=\{x,y,z\}$, the position vector $\bm{x}$ is defined
:::{math}
\bm{x}=\sum_{i=1}^3x_i\bm{\hat{x}}_i,
:::
with $\{\bm{\hat{x}}_i\}_{i=1}^3=\{\bm{\hat{x}},\bm{\hat{y}},\bm{\hat{z}}\}$ the set of unit basis vectors for the coordinates. A vector field $\bm{a}(\bm{x},t)$ then has the representation
:::{math}
\bm{a}(\bm{x},t)=\sum_{i=1}^3a_i(\bm{x},t)\bm{\hat{x}}_i,
:::
where a coefficient $a_i(\bm{x},t)$ is a scalar function of the position $\bm{x}$ and time $t$, and associated with a direction $\bm{\hat{x}}_i$. A rank-2 tensor field $\bm{\sigma}(\bm{x},t)$ in the same Cartesian coordinates has the representation
:::{math}
\bm{\sigma}(\bm{x},t)=\sum_{i,j=1}^{3}\sigma_{ij}(\bm{x},t)\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,
:::
where a coefficient $\sigma_{ij}(\bm{x},t)$ is again a scalar function but now associated with not one but two directions, namely $\bm{\hat{x}}_i$ and $\bm{\hat{x}}_j$, connected via the operator $(\otimes)$. Similarly as the coefficient functions $a_i(\bm{x},t)$ of a vector field change upon changing of the coordinates, so do the coefficient functions $\sigma_{ij}(\bm{x},t)$ of a tensor field. The tensor field $\bm{\sigma}(\bm{x},t)$ nevertheless represents the same geometric object in every coordinate system, similarly as a vector field $\bm{a}(\bm{x},t)$ does. From here on, the explicit arguments for the fields will be dropped for compactness, unless otherwise specified.

The operator $\otimes$ appearing in the definition of $\bm{\sigma}$ is the tensor product. The tensor product of two vectors $\bm{a}$ and $\bm{b}$ is a dyad $\bm{a}\otimes\bm{b}$. For any three vectors $\bm{a}$, $\bm{b}$, and $\bm{c}$, and a scalar $f$, the tensor product satisfies the dyadic identities
:::{math}
\begin{aligned}
(f\bm{a})\otimes\bm{b}&=f(\bm{a}\otimes\bm{b})=\bm{a}\otimes(f\bm{b}) && \text{Scalar multiplication}\\
\bm{a} \otimes (\bm{b}+\bm{c}) &= \bm{a} \otimes \bm{b}+\bm{a}\otimes\bm{c} && \text{Right linearity}\\
(\bm{b}+\bm{c}) \otimes \bm{a} &= \bm{b} \otimes \bm{a}+\bm{c}\otimes\bm{a} && \text{Left linearity}\\
(\bm{a} \otimes \bm{b}) \cdot \bm{c} &= \bm{a}(\bm{b} \cdot \bm{c}) && \text{Right dyad-vector contraction} \\
\bm{c} \cdot (\bm{a} \otimes \bm{b}) &= (\bm{c} \cdot \bm{a})\bm{b} && \text{Left vector-dyad contraction}
\end{aligned}
:::
Further, the dyads $\bm{a}\otimes\bm{b}$ and $\bm{b}\otimes\bm{a}$ are equal if and only if $\bm{a}$ and $\bm{b}$ are linearly dependent.
::::{proof:example}
Consider the vectors
:::{math}
:enumerated: false
\begin{aligned}
\bm{a}&=2\bm{\hat{x}}-\bm{\hat{y}},\\
\bm{b}&=-\bm{\hat{x}}+\bm{\hat{y}},\\
\bm{c}&=3\bm{\hat{y}}+\bm{\hat{z}}.
\end{aligned}
:::
The left and right linearity together with the scalar multiplication rule provide
:::{math}
:enumerated:false
\begin{aligned}
\bm{a}\otimes\bm{b}&=(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}})+(2\bm{\hat{x}}-\bm{\hat{y}})\otimes\bm{\hat{y}}\\
&=(2\bm{\hat{x}})\otimes(-\bm{\hat{x}})+(-\bm{\hat{y}})\otimes(-\bm{\hat{x}})+(2\bm{\hat{x}})\otimes\bm{\hat{y}}+(-\bm{\hat{y}})\otimes\bm{\hat{y}}\\
&=-2\bm{\hat{x}}\otimes\bm{\hat{x}}+\bm{\hat{y}}\otimes\bm{\hat{x}}+2\bm{\hat{x}}\otimes\bm{\hat{y}}-\bm{\hat{y}}\otimes\bm{\hat{y}}.
\end{aligned}
:::
The right dyad-vector contraction rule gives
:::{math}
:enumerated: false
\begin{aligned}
(\bm{a}\otimes\bm{b})\cdot\bm{c}&=[(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})]\cdot(3\bm{\hat{y}}+\bm{\hat{z}})\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})[(-\bm{\hat{x}}+\bm{\hat{y}})\cdot(3\bm{\hat{y}}+\bm{\hat{z}})]\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})(3)\\
&=6\bm{\hat{x}}-3\bm{\hat{y}},
\end{aligned}
:::
while the left vector-dyad contraction rule gives
:::{math}
:enumerated: false
\begin{aligned}
\bm{c}\cdot(\bm{a}\otimes\bm{b})&=(3\bm{\hat{y}}+\bm{\hat{z}})\cdot[(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})]\\
&=[(3\bm{\hat{y}}+\bm{\hat{z}})\cdot(2\bm{\hat{x}}-\bm{\hat{y}})] (-\bm{\hat{x}}+\bm{\hat{y}})\\
&=(-\bm{\hat{x}}+\bm{\hat{y}})(-3)\\
&=3\bm{\hat{x}}-3\bm{\hat{y}},
\end{aligned}
:::
which clearly are two different vectors.
::::

The rules for the tensor product $\otimes$ imply that, in Cartesian coordinates, the right contraction of a rank-2 tensor $\bm{\sigma}$ with a vector $\bm{a}$ results in a vector
:::{math}
\bm{\sigma}\cdot\bm{a}=\sum_{i,j=1}^3\sigma_{ij}a_j\bm{\hat{x}}_i,
:::
while the left contraction results in a different vector
:::{math}
\bm{a}\cdot\bm{\sigma}=\sum_{i,j=1}^3a_i\sigma_{ij}\bm{\hat{x}}_j.
:::
The connection between the two is provided by the tensor transpose
:::{math}
\bm{\sigma}^\mathsf{T}=\sum_{i,j=1}^3\sigma_{ji}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,
:::
which satisfies the identity
:::{math}
\bm{\sigma}\cdot\bm{a}=\bm{a}\cdot\bm{\sigma}^\mathsf{T}.
:::
Consequently, the coefficients of a tensor $\bm{\sigma}$ in Cartesian coordinates can be accessed by contracting the tensor with the coordinate basis vectors from left and right
:::{math}
\sigma_{ij}=\bm{\hat{x}}_i\cdot\bm{\sigma}\cdot\bm{\hat{x}}_j.
:::

A rank-2 tensor of particular importance is the identity tensor that has the Cartesian coordinate representation 
:::{math}
\bm{I}=\sum_{i,j=1}^3\delta_{ij}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,
:::
where $\delta_{ij}$ is the Kronecker delta satisfying
:::{math}
\delta_{ij}=\left\{\begin{aligned}&1, &&\text{if}\quad i=j,\\&0, &&\text{if}\quad i\neq j.\end{aligned}\right.
:::
With respect to any vector $\bm{a}$, the identity tensor satisfies
:::{math}
\bm{I}\cdot\bm{a}=\bm{a}\cdot\bm{I}=\bm{a}.
:::

Where the tensor-vector contraction results in a vector, the tensor-tensor double contraction of rank-2 tensors $\bm{\sigma}$ and $\bm{\pi}$, denoted by $(:)$, results in a scalar
:::{math}
\bm{\sigma}:\bm{\pi}=\sum_{i,j=1}^3\sigma_{ij}\pi_{ij}.
:::
If one of the tensors is the identity tensor $\bm{I}$, the double contraction returns the trace of the tensor, expressed in Cartesian coordinates as
:::{math}
\text{tr}(\bm{\sigma})=\bm{I}:\bm{\sigma}=\bm{\sigma}:\bm{I}=\sum_{i=1}^3\sigma_{ii}.
:::


## <span class="elementary"></span> Calculus involving rank-2 tensors

In these notes, the calculus identities are expressed in Cartesian coordinates, unless stated otherwise. The identities written in vector and tensor notation without indices are nevertheless coordinate-independent, provided the differential operators are interpreted consistently.

From calculus classes, one recalls the vector-valued differential operator $\nabla$ with the Cartesian coordinate representation
:::{math}
\nabla=\sum_{i=1}^3\bm{\hat{x}}_i\frac{\partial}{\partial x_i}=\sum_{i=1}^3\bm{\hat{x}}_i\partial_i.
:::
The action of $\nabla$ on a scalar field $f$ produces its gradient, which is a vector field
:::{math}
\nabla f=\sum_{i=1}^3\partial_if\,\bm{\hat{x}}_i,
:::
represented by the coefficient functions $\partial_if$. Since $\nabla$ is a vector-valued operator, it can be paired with a vector field by the common vector dot-product $(\cdot)$ or the vector cross-product $(\times)$. A vector field $\bm{a}$ can be returned back to a scalar field by taking the divergence
:::{math}
\nabla\cdot\bm{a}=\sum_{i=1}^3\partial_ia_i,
:::
while the curl of a vector field results in another vector field
:::{math}
\nabla\times\bm{a}=\sum_{i,j,k=1}^3\varepsilon_{ijk}\partial_ia_j\bm{\hat{x}}_k.
:::
Here $\varepsilon_{ijk}$ is the alternating Levi-Civita symbol in three dimensions, familiar from the cross product of two vectors, and defined
:::{math}
\varepsilon_{ijk}=\left\{\begin{aligned}+&1, &&\text{if}\,(i,j,k)\,\text{is an even permutation of}\,(1,2,3),\\-&1, &&\text{if}\,(i,j,k)\,\text{is an odd permutation of}\,(1,2,3),\\&0,&&\text{otherwise}.\end{aligned}\right.
:::
The step up from vectors to tensors happens if $\nabla$ acts on a vector field without the $(\cdot)$ or $(\times)$ between. The gradient of a vector field $\bm{a}$ is formally expressed using the tensor product. In Cartesian coordinates, it results in
:::{math}
\nabla\bm{a}=\nabla\otimes\bm{a}=\sum_{i,j=1}^3\partial_i a_j\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,
:::
which is a rank-2 tensor field represented by the coefficient functions $\partial_i a_j$. Where the divergence of a vector field results in a scalar, the divergence of a tensor field $\bm{\sigma}$ results in a vector field and is defined
:::{math}
\nabla\cdot\bm{\sigma}=\sum_{i,j=1}^3\partial_i\sigma_{ij}\bm{\hat{x}}_j.
:::

::::{proof:example}
Consider a scalar field $f$ and a vector field $\bm{a}$ defined in Cartesian coordinates as
:::{math}
:enumerated: false
\begin{aligned}
f(\bm{x})&=x^2y+yz,\\
\bm{a}(\bm{x})&=xy\bm{\hat{x}}+yz\bm{\hat{y}}+zx\bm{\hat{z}}.
\end{aligned}
:::
The gradient of the scalar field is a vector field given by
:::{math}
:enumerated: false
\begin{aligned}
\nabla f
&=\frac{\partial f}{\partial x}\bm{\hat{x}}+\frac{\partial f}{\partial y}\bm{\hat{y}}+\frac{\partial f}{\partial z}\bm{\hat{z}}\\
&=2xy\bm{\hat{x}}+(x^2+z)\bm{\hat{y}}+y\bm{\hat{z}}.
\end{aligned}
:::
The divergence of the vector field returns a scalar field
:::{math}
:enumerated: false
\begin{aligned}
\nabla\cdot\bm{a}
&=\frac{\partial a_x}{\partial x}
+\frac{\partial a_y}{\partial y}
+\frac{\partial a_z}{\partial z}\\
&=y+z+x.
\end{aligned}
:::
whereas its curl returns another vector field
:::{math}
:enumerated: false
\begin{aligned}
\nabla\times\bm{a}
&=\left(\frac{\partial a_z}{\partial y}-\frac{\partial a_y}{\partial z}\right)\bm{\hat{x}}
+\left(\frac{\partial a_x}{\partial z}-\frac{\partial a_z}{\partial x}\right)\bm{\hat{y}}
+\left(\frac{\partial a_y}{\partial x}-\frac{\partial a_x}{\partial y}\right)\bm{\hat{z}}\\
&=-y\bm{\hat{x}}-z\bm{\hat{y}}-x\bm{\hat{z}}.
\end{aligned}
:::
The gradient of the vector field is instead a rank-2 tensor field. Its Cartesian coordinate representation is
:::{math}
:enumerated: false
\begin{aligned}
\nabla\bm{a}
&=\frac{\partial a_x}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{z}}\\
&\quad+\frac{\partial a_x}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{z}}\\
&\quad+\frac{\partial a_x}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{z}}\\
&=y\bm{\hat{x}}\otimes\bm{\hat{x}}+z\bm{\hat{x}}\otimes\bm{\hat{z}}\\
&\quad+x\bm{\hat{y}}\otimes\bm{\hat{x}}+z\bm{\hat{y}}\otimes\bm{\hat{y}}\\
&\quad+y\bm{\hat{z}}\otimes\bm{\hat{y}}+x\bm{\hat{z}}\otimes\bm{\hat{z}}.
\end{aligned}
:::
This illustrates how the action of the differential operator $\nabla$ produces different mathematical objects depending on how it is applied to a scalar, vector, or tensor field.
::::


The process of converting conservation principle of mass, momentum, and energy into local partial differential equations involves transforming surface integrals to volume integrals. Carrying out such tasks requires the action of $\nabla$ on products containing scalar-, vector-, and tensor-valued fields. The rules most needed are
:::{math}
:label: eq-divergence-rules
\begin{aligned}
\nabla\cdot(f\bm{a})&=\nabla f\cdot\bm{a}+f\nabla\cdot\bm{a},\\
\nabla\cdot(\bm{a}\otimes\bm{b})&=(\nabla\cdot\bm{a})\bm{b}+\bm{a}\cdot\nabla\bm{b},\\
\nabla\cdot(\bm{\sigma}\cdot\bm{a})&=(\nabla\cdot\bm{\sigma})\cdot\bm{a}+\bm{\sigma}:\nabla\bm{a}.
\end{aligned}
:::
They become powerful tools when combined with the divergence theorems for scalar and tensor fields
:::{math}
:label: eq-divergence-theorem
\begin{aligned}
\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA&=\int_V\nabla\cdot\bm{a}dV,\\
\int_{\partial V}\bm{\sigma}\cdot\bm{\hat{n}}dA&=\int_V\nabla\cdot\bm{\sigma}^\mathsf{T}dV,\\
\end{aligned}
:::
that convert a surface integral of a field over the boundary $\partial V$ of a volume $V$ into a volume integral of the field divergence.

::::{proof:example}
Consider a cubic volume 
:::{math}
:enumerated: false
V=\{(x,y,z)\in\mathbb{R}^3|0\leq x,y,z \leq L\},
:::
where $L$ is the side length of the cube and $A=L^2$ the area of each face. Assume also a vector field
:::{math}
:enumerated: false
\bm{a}=x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}.
:::
The surface integral of $\bm{a}\cdot\bm{\hat{n}}$ over the cube boundary $\partial V$ can be evaluated by considering the six faces of the cube. On each of the three faces at $x=L$, $y=L$, and $z=L$, one has $\bm{a}\cdot\bm{\hat{n}}=L$, whereas on the remaining three faces at $x=0$, $y=0$, and $z=0$, the term is zero. Consequently,
:::{math}
:enumerated: false
\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA=LA+LA+LA=3L^3.
:::
Since the divergence of $\bm{a}$ is a constant
:::{math}
:enumerated: false
\nabla\cdot\bm{a}=\frac{\partial x}{\partial x}+\frac{\partial y}{\partial y}+\frac{\partial z}{\partial z}=3,
:::
one immediately computes
:::{math}
:enumerated: false
\int_V\nabla\cdot\bm{a}\,dV=3V=3L^3.
:::
This demonstrates the divergence theorem for a vector field.

Consider the non-symmetric rank-2 tensor field
:::{math}
:enumerated: false
\bm{\sigma}=\bm{\hat{x}}\otimes\bm{a}.
:::
Using the right dyad-vector contraction rule, the surface integral becomes
:::{math}
:enumerated: false
\begin{aligned}
\int_{\partial V}\bm{\sigma}\cdot\bm{\hat{n}}dA
&=\int_{\partial V}(\bm{\hat{x}}\otimes\bm{a})\cdot\bm{\hat{n}}dA\\
&=\bm{\hat{x}}\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA\\
&=3L^3\bm{\hat{x}}.
\end{aligned}
:::
To evaluate the corresponding volume integral, first transpose the tensor:
:::{math}
:enumerated: false
\bm{\sigma}^\mathsf{T}=\bm{a}\otimes\bm{\hat{x}}.
:::
Using the product rule for the divergence of a dyad gives
:::{math}
:enumerated: false
\begin{aligned}
\nabla\cdot\bm{\sigma}^\mathsf{T}
&=\nabla\cdot(\bm{a}\otimes\bm{\hat{x}})\\
&=(\nabla\cdot\bm{a})\bm{\hat{x}}+\bm{a}\cdot\nabla\bm{\hat{x}}\\
&=3\bm{\hat{x}},
\end{aligned}
:::
where the second term vanishes because $\bm{\hat{x}}$ is a constant basis vector in Cartesian coordinates. Thus,
:::{math}
:enumerated: false
\int_V\nabla\cdot\bm{\sigma}^\mathsf{T}dV=3\bm{\hat{x}}V=3L^3\bm{\hat{x}},
:::
which equals the corresponding surface integral. Notice that $\nabla\cdot\bm{\sigma}=\bm{\hat{x}}$, which is different from $\nabla\cdot\bm{\sigma}^\mathsf{T}=3\bm{\hat{x}}$. The transpose in the tensor divergence theorem is therefore essential when the tensor is not symmetric.
::::


## <span class="intermediate"></span> Further identities involving tensors
Those interested in progressing beyond the core engineering path and to studying the implications of momentum conservation encounter also expressions involving tensor-vector cross products and tensor-tensor single dot-products. To define such operations, the following identities involving dyads, of which rank-2 tensor are linear combinations of, are needed
:::{math}
\begin{aligned}
(\bm{a}\otimes\bm{b})\times\bm{c}&=\bm{a}\otimes(\bm{b}\times\bm{c}) && \text{Right dyad-vector cross product}\\
\bm{a}\times(\bm{b}\otimes\bm{c})&=(\bm{a}\times\bm{b})\otimes\bm{c} && \text{Left vector-dyad cross product}\\
(\bm{a}\otimes\bm{b})\cdot(\bm{c}\otimes\bm{d})&=(\bm{b}\cdot\bm{c})(\bm{a}\otimes\bm{d}) && \text{Dyad-dyad dot product}
\end{aligned}
:::
Applying these identities, both the right and left tensor-vector cross-product can be evaluated. The results are new rank-2 tensors with Cartesian coordinate representations given by
:::{math}
\begin{aligned}
\bm{\sigma}\times\bm{a}&=\sum_{i,j,k,\ell=1}^3\varepsilon_{\ell k j}\sigma_{i\ell}a_k\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,\\
\bm{a}\times\bm{\sigma}&=\sum_{i,j,k,\ell=1}^3\varepsilon_{\ell ki}a_\ell \sigma_{kj}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j.
\end{aligned}
:::
Also the tensor-tensor dot-product of two rank-2 tensors $\bm{\sigma}$ and $\bm{\pi}$ results in a new rank-2 tensor
:::{math}
\bm{\sigma}\cdot\bm{\pi}=\sum_{i,j,k=1}^{3}\sigma_{ik}\pi_{kj}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,
:::
and particularly the dot product with the identity tensor results in
:::{math}
\bm{\sigma}\cdot\bm{I}=\bm{I}\cdot\bm{\sigma}=\bm{\sigma}.
:::
The calculus identity using the above definitions is
:::{math}
:label: eq-div-a-times-sigma
\nabla\cdot(\bm{a}\times\bm{\sigma})^\mathsf{T}=\bm{a}\times\nabla\cdot\bm{\sigma}^\mathsf{T}-\bm{\varepsilon}:(\bm{\sigma}\cdot\nabla\bm{a}),
:::
where the rank-3 antisymmetric Levi-Civita tensor $\bm{\varepsilon}$ is defined
:::{math}
\bm{\varepsilon}=\sum_{i,j,k=1}^3\varepsilon_{ijk}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j\otimes\bm{\hat{x}}_k,
:::
and the double dot product between the rank-3 tensor $\bm{\varepsilon}$ and any rank-2 tensor $\bm{\sigma}$ results in a vector
:::{math}
\bm{\varepsilon}:\bm{\sigma}=\sum_{i,j,k=1}^3\varepsilon_{ijk}\sigma_{jk}\bm{\hat{x}}_i.
:::
The Levi-Civita symbol $\varepsilon_{ijk}$ is antisymmetric with respect to changing any of its two indices. For example $\varepsilon_{ijk}=-\varepsilon_{ikj}=-\varepsilon_{jik}=-\varepsilon_{kji}$. Consequently, only for a symmetric rank-2 tensor $\bm{\pi}=\bm{\pi}^\mathsf{T}$,  one has
:::{math}
\bm{\varepsilon}:\bm{\pi}=\bm{0}.
:::

(example-eq-div-a-times-sigma)=
::::{proof:example}
Consider the position vector field
:::{math}
:enumerated: false
\bm{x}=x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}.
:::
Its gradient is the identity tensor, since
:::{math}
:enumerated: false
\nabla\bm{x}=\sum_{i,j=1}^3\partial_i x_j\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j=\sum_{i,j=1}^3\delta_{ij}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j=\bm{I}.
:::
Applying the calculus identity {numref}`eq-div-a-times-sigma` for the divergence of a vector-tensor cross product consequently gives
:::{math}
:enumerated: false
\begin{aligned}
\nabla\cdot((\bm{x}-\bm{x}_0)\times\bm{\sigma})^\mathsf{T}
&=(\bm{x}-\bm{x}_0)\times(\nabla\cdot\bm{\sigma}^\mathsf{T})\\
&\qquad -\bm{\varepsilon}:(\bm{\sigma}\cdot\nabla(\bm{x}-\bm{x}_0))\\
&=(\bm{x}-\bm{x}_0)\times(\nabla\cdot\bm{\sigma}^\mathsf{T})
-\bm{\varepsilon}:\bm{\sigma}.
\end{aligned}
:::
If the tensor $\bm{\sigma}$ is symmetric, the last term vanishes, leaving
:::{math}
:enumerated: false
\nabla\cdot((\bm{x}-\bm{x}_0)\times\bm{\sigma})^\mathsf{T}
=(\bm{x}-\bm{x}_0)\times(\nabla\cdot\bm{\sigma}^\mathsf{T}).
:::
This observation plays a key role in establishing the symmetry of the stress tensor from the argument that only the torque from forces can change the angular momentum of a body.
::::

## <span class="elementary"></span> Leibniz integral differentiation rule
The tool to convert physics principles to local partial differential equations that describe the evolution of fluids is generally referred to as the Leibniz integral differentiation rule. It describes how integrals of scalar- and vector-valued fields (in general case also tensor-valued fields) vary in time when evaluated over temporally evolving curves, surfaces, or volumes. The particular use case of the rule to derive the fluid evolution equations involves only volumes, in which case the rule is often referred to as the Reynolds transport theorem. The other important use case for the rule is encountered when deriving the control-volume balance equations needed in engineering applications. In the first case, the evolution of the volume follows the fluid's velocity field. In the second case, the moving volume of fluid is typically enclosed by a mechanical device such as a turbine or a compressor, with the movement of the fluid volume originating from, e.g., rotating turbine or compressor blades.

As the first step, one has to understand how a moving volume is described and how vector fields relate to it. For this, assume the vector field $\bm{v}(\bm{x},t)$ to describe which direction fluid is moving at point $\bm{x}$ at time $t$, and at what speed, i.e., the velocity of the fluid. Then drop a small grain of pollen into the fluid at a specific location $\bm{y}_0$ at time $t=t_0$. From that moment onwards, the position $\bm{y}(t)$ of the pollen grain will follow the fluid flow and obey the vector-valued ordinary differential equation subject to an initial condition
:::{math}
:label: eq:point-ODE
\frac{d\bm{y}(t)}{dt}=\bm{v}(\bm{y}(t),t), \qquad \bm{y}(t_0)=\bm{y}_0.
:::
Over time, the position $\bm{y}(t)$ draws a curve in space with the tangent vectors of the curve denoting the local and instantaneous velocity of the grain as in {numref}`fig-point-movement`.

:::{figure} ./figs/fig-point-movement.svg
:label: fig-point-movement
:align: center
:width: 80%
Movement of a point following a vector field.
:::

Since $\bm{v}(\bm{x},t)$ is a vector field, it can move not only the specific point $\bm{y}_0$ where the pollen grain was dropped but any point $\bm{x}$. This is formalized by defining the so-called flow map $\bm{\phi}_t(\bm{x})$ and requiring it to describe the solution to the ordinary differential equation {numref}`eq:point-ODE` with respect to any initial point
:::{math}
:label: eq-flowmap
\frac{d}{dt}\bm{\phi}_t(\bm{x})=\bm{v}(\bm{\phi}_t(\bm{x}),t), \qquad \bm{\phi}_{t_0}(\bm{x})=\bm{x}.
:::
The flow map $\bm{\phi}_t$ is a vector valued function that takes in a point $\bm{x}$ at time $t_0$ and outputs a new point $\bm{\phi}_t(\bm{x})$ that corresponds to the location of the position at a later time $t$ if it were to follow the vector field $\bm{v}(\bm{x},t)$. Consequently, the flow map can be used to describe how an arbitrary set of points $\Omega(t_0)$ recorded at time $t_0$ would follow the vector field and evolve into a new set of points $\Omega(t)=\{\bm{\phi}_t(\bm{x})|\bm{x}\in\Omega(t_0)\}$ at time $t$. This evolution is illustrated in {numref}`fig-flowmap` for a surface. 

:::{figure} ./figs/fig-flowmap.svg
:label: fig-flowmap
:align: center
:width: 100%
Movement of specific point $\bm{y}(t)$ and a set of points $\Omega(t)$ that form a surface according to the flow map $\bm{\phi}_t(\bm{x})$ of a vector field $\bm{v}(\bm{x},t)$. 
:::

For some velocity fields, it is possible to find analytical expressions for the flow map, but typically the map has to be constructed numerically by integrating the ordinary differential equation {numref}`eq:point-ODE` with respect to all initial locations of interest.
(example-flowmap-analytical)=
::::{proof:example}
The time-independent vector field $\bm{v}(\bm{x})=\omega(y\bm{\hat{x}}-x\bm{\hat{y}})+v_z\bm{\hat{z}}$, with $\omega$ and $v_z$ constants, has a flow map
:::{math}
:enumerated: false
\bm{\phi}_t(\bm{x})=\phi_t^x(\bm{x})\bm{\hat{x}}+\phi_t^y(\bm{x})\bm{\hat{y}}+\phi_t^{z}(\bm{x})\bm{\hat{z}},
:::
with the following component functions in the $x$-, $y$-, and $z$-directions
:::{math}
:enumerated: false
\begin{aligned}
\phi_t^x(\bm{x})&=\cos(\omega(t-t_0))x+\sin(\omega(t-t_0))y,\\
\phi_t^y(\bm{x})&=-\sin(\omega(t-t_0))x+\cos(\omega(t-t_0))y,\\
\phi_t^z(\bm{x})&=z+v_z(t-t_0).
\end{aligned}
:::
This can be verified by computing the time derivatives of the component functions
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}\phi_t^x(\bm{x})&=\omega[-\sin(\omega(t-t_0))x+\cos(\omega(t-t_0))y]=\omega \phi_t^y(\bm{x}),\\
\frac{d}{dt}\phi_t^y(\bm{x})&=- \omega[\cos(\omega(t-t_0))x+\sin(\omega(t-t_0))y]=-\omega\phi_t^x(\bm{x}),\\
\frac{d}{dt}\phi_t^{z}(\bm{x})&=v_z,
\end{aligned}
:::
so that the time derivative of the flow map can be identified as
:::{math}
:enumerated: false
\frac{d}{dt}\bm{\phi}_t(\bm{x})=\omega(\phi_t^y(\bm{x})\bm{\hat{x}}-\phi_t^x(\bm{x})\bm{\hat{y}})+v_z\bm{\hat{z}}=\bm{v}(\bm{\phi}_t(\bm{x})).
:::

The map describes a helical trajectory with constant angular velocity $\omega$ and translative velocity $v_z$ in the $z$-direction.
::::

Being now aware of the effects of vector fields on the movement of sets of points, assume the set of points to be a volume $V(t)$ that follows the flow of the vector field $\bm{u}(\bm{x},t)$ and is enclosed by a boundary $\partial V(t)$. The vector field $\bm{u}(\bm{x},t)$ is not necessarily the velocity of the fluid itself, denoted by $\bm{v}(\bm{x},t)$. For a volume $V(t)$ that follows the fluid, the two fields coincide. For a control volume, the boundary velocity is determined by how the control volume is selected and may differ from the fluid velocity. Assume then the existence of a scalar- or vector-valued field $\bm{f}(\bm{x},t)$. The time derivative of the integral of $\bm{f}$ over the volume $V(t)$ evolving according to $\bm{u}(\bm{x},t)$ is then given by the Leibniz rule
:::{math}
:label: eq-leibniz-rule-surface-form
\underbrace{\frac{d}{dt}\int_{V(t)}\bm{f}dV}_{\substack{\text{Time rate of change}\\\text{of an integral of}\,\bm{f}\\\text{calculated over the}\\\text{moving volume}}}=\underbrace{\int_{V(t)}\partial_t \bm{f}dV}_{\substack{\text{Integral of the local}\\\text{temporal change}\,\partial_t\bm{f}\\\text{calculated over the}\\\text{moving volume}}} +\underbrace{\int_{\partial V(t)}\bm{f}\underbrace{\bm{u}\cdot\bm{\hat{n}} dA}_{\substack{\text{Local rate of}\\\text{change of the}\\\text{volume from}\\\text{boundary}\\\text{movement}}}}_{\substack{\text{Contribution to the integral}\\\text{from boundary movement}}}.
:::
According to the rule, both the local temporal change in $\bm{f}$ as well as changes in the volume $V(t)$ itself contribute to the time derivative. Notably, even if the field $\bm{f}$ were stationary in time, the integral of it over a volume could still change in time if the volume would move and, at different times, occupy domains in space where the field $\bm{f}$ varies spatially. 

With the help of the divergence theorem {numref}`eq-divergence-theorem` and the vector calculus rules {numref}`eq-divergence-rules` involving the divergence of a rank-2 tensor field $\bm{u}\otimes\bm{f}$, the surface integral in the Leibniz rule {numref}`eq-leibniz-rule-surface-form` can be converted to a volume integral
:::{math}
\begin{aligned}
\int_{\partial V(t)}\bm{f}\bm{u}\cdot\bm{\hat{n}}dA&=\int_{\partial V(t)}(\bm{f}\otimes\bm{u})\cdot\bm{\hat{n}}dA\\
&=\int_{V(t)}\nabla\cdot(\bm{f}\otimes\bm{u})^\mathsf{T}dV\\
&=\int_{V(t)}\nabla\cdot(\bm{u}\otimes\bm{f})dV\\
&=\int_{V(t)}((\nabla\cdot\bm{u})\bm{f}+\bm{u}\cdot\nabla\bm{f})dV,
\end{aligned}
:::
so that the Leibniz rule can be expressed also in a pure volume form
:::{math}
:label: eq-leibniz-rule-volume-form
\frac{d}{dt}\int_{V(t)}\bm{f}dV=\int_{V(t)}\left(\partial_t \bm{f}+(\nabla\cdot\bm{u})\bm{f}+(\bm{u}\cdot\nabla)\bm{f}\right)dV.
:::
In this last form the Leibniz rule enables conversion of the physics principles of mass, momentum, and energy conservation into local partial differential equations. For those interested in progressing beyond the use of the Leibniz rule, and understanding also the derivation of it, the details are provided in the intermediate and advanced {numref}`sec-differential-elements`, {numref}`sec-differential-elements-evolution` and {numref}`sec-leibniz-rule-derivation`. Those more interested following the core engineering path may skip these section and jump directly to {numref}`sec-conservation-of-mass` that investigates the principle of mass conservation.

::::{proof:example}
The contribution of volume movement to the Leibniz rule is perhaps best illustrated with a scalar field $f(\bm{x},t)=f(x)$ that is stationary in time and depends only on the coordinate $x$, and assuming a vector field $\bm{u}(\bm{x},t)=u\bm{\hat{x}}$ with $u>0$ constant in time and space. Let the initial volume $V(0)$ have a cross section $A$ in the $y$-$z$ plane and a length $L$ in the $x$-direction. Set the volume to initially correspond to the set of points
:::{math}
:enumerated: false
V(0)=\{(x,y,z)\in\mathbb{R}^3|0\leq x\leq L,(y,z)\in A\}.
:::
For later times $t$, the vector field $\bm{u}(\bm{x},t)$ moves the volume into a new set of points
:::{math}
V(t)=\{(x,y,z)\in\mathbb{R}^3|ut\leq x\leq ut+L,(y,z)\in A\}
:::
It is then a matter of investigating how the integral
:::{math}
:enumerated: false
\int_{V(t)}fdV=A\int_{ut}^{ut+L}f(x)dx
:::
evolves in time when the volume changes. Graphically, the setting is illustrated below
:::{image} ./figs/example-fig-moving-rectangle.svg
:align: center
:width: 100%
:::
Assuming $f(x)$ to have an integral function $F(x)$ such that $dF(x)/dx=f(x)$, a direct computation of the left side of the Leibniz rule then provides
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}\int_{V(t)}fdV&=A\frac{d}{dt}\int_{ut}^{ut+L}f(x)dx\\
&=A\frac{d}{dt}(F(ut+L)-F(ut))\\
&=Auf(ut+L)-Auf(ut)
\end{aligned}
:::
The first term on the right corresponds to the rate $Au>0$ at which the moving volume gains volume through the boundary at $x=ut+L$, multiplied by the value of the function $f(x)$ at that boundary. The second term describes the corresponding loss of volume at the rate $-Au<0$ through the trailing boundary at $x=ut$, multiplied by the value of $f(x)$ there.

On the right side of the Leibniz rule only the boundary term survives since $\partial_tf(\bm{x})=0$. Further, the lateral boundary does not contribute since the velocity field is parallel to it and therefore has no component in the direction of its outward normal. On the boundary $x=ut+L$, one has $\bm{\hat{n}}=\bm{\hat{x}}$. On the boundary $x=ut$, one has $\bm{\hat{n}}=-\bm{\hat{x}}$ instead. Therefore
:::{math}
:enumerated: false
\int_{\partial V(t)}f\bm{u}\cdot\bm{\hat{n}}dA=Auf(ut+L)-Auf(ut),
:::
which exactly correspond to the left side of the Leibniz rule.
::::

(sec-differential-elements)=
## <span class="intermediate"></span> Differential line, surface, and volume elements

The derivation of the Leibniz integral differentiation formula relies on investigating how the flow map moves differential objects such as line, surface, and volume elements. Before setting such objects into motion, one has to understand how they are constructed in the first place. Here, the matter is approached using a geometric perspective.

Consider a general coordinate triplet $(\xi_1,\xi_2,\xi_3)$ that defines a point $\bm{x}$ in space. In other words, a location in space is a vector-valued function $\bm{x}(\xi_1,\xi_2,\xi_3)$ of the coordinates. A differential, vector-valued line element $d\bm{\ell}_{i}$, into the direction of the coordinate $\xi_i$, is generated by the change in the position $\bm{x}$ with respect to a differential change $d\xi_i$ in the coordinate $\xi_i$ via
:::{math}
d\bm{\ell}_{i}=\lim_{\epsilon\to0}\frac{\bm{x}(\xi_i+\epsilon d\xi_i,\xi_j,\xi_k)-\bm{x}(\xi_i,\xi_j,\xi_k)}{\epsilon}=\frac{\partial\bm{x}}{\partial \xi_i}d\xi_i.
:::
A differential, vector-valued, oriented surface element $d\bm{A}=\bm{\hat{n}}dA$ having a surface unit normal vector $\bm{\hat{n}}$, can be constructed by considering the oriented area two different differential line elements span. For example, the vector-valued line elements $d\bm{\ell}_{i}$ and $d\bm{\ell}_{j}$ create a vector valued oriented surface element $d\bm{A}_{k}$ via the cross-product
:::{math}
d\bm{A}_{k}=d\bm{\ell}_{i}\times d\bm{\ell}_{j}=\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}d\xi_i d\xi_j.
:::
Such element has a non-negative and scalar-valued but differential area
:::{math}
dA_{k}=\left|d\bm{A}_{k}\right|=\left|\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}\right|d\xi_i d\xi_j,
:::
and a non-differential unit normal vector
:::{math}
\bm{\hat{n}}_{k}=\frac{\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}}{\left|\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}\right|}.
:::

Finally, a differential volume element $dV$ can be constructed by considering the volume all three differential line elements span
:::{math}
dV=\left|d\bm{\ell}_{i}\times d\bm{\ell}_{j}\cdot d\bm{\ell}_{k}\right|=\left|\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}\cdot\frac{\partial \bm{x}}{\partial \xi_k}\right|d\xi_i d\xi_j d\xi_k.
:::
This construction is free of the way the coordinates $(\xi_1,\xi_2,\xi_3)$ are chosen. They can be the Cartesian coordinates or any curvilinear coordinates. Example coordinate-triplet isolines trough a point $\bm{x}$ and the possible vectors $\partial\bm{x}/\partial \xi_i$ they generate at the point $\bm{x}$ are illustrated in {numref}`fig-coordinate-vectors`. From the figure, one may observe the vectors to span finite areas and a finite volume. The areas and the volume become differential once the length along the vectors are scaled with the associated differentials $d\xi_i$.
:::{figure} ./figs/fig-coordinate-vectors.svg
:label: fig-coordinate-vectors
:align: center
:width: 100%
Coordinate lines and vectors that define differential line, surface, and volume elements.
:::

::::{proof:example}
A point $\bm{x}$ in space is described by the Cartesian coordinate triplet $(x,y,z)$ as
:::{math}
:enumerated: false
\bm{x}=x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}.
:::
The same point can be described using a cylindrical coordinate triplet $(r,\vartheta,z)$ as 
:::{math}
:enumerated: false
\bm{x}=r\cos\vartheta\bm{\hat{x}}+r\sin\vartheta\bm{\hat{y}}+z\bm{\hat{z}}.
:::
The Cartesian coordinates are seen to be be functions of the cylindrical ones via $x(r,\vartheta)=r\cos\vartheta$ and $y(r,\vartheta)=r\sin\vartheta$.
::::
::::{proof:example}
In cartesian coordinates $(x,y,z)$, the differential line elements are
:::{math}
:enumerated: false
d\bm{\ell}_{x}=\bm{\hat{x}}dx, \quad d\bm{\ell}_{y}=\bm{\hat{y}}dy, \quad d\bm{\ell}_{z}=\bm{\hat{z}}dz.
:::
They generate differential oriented surface elements such as
:::{math}
:enumerated: false
\begin{aligned}
d\bm{A}_{x}&=d\bm{\ell}_{y}\times d\bm{\ell}_{z}=\bm{\hat{y}}\times\bm{\hat{z}}dydz=\bm{\hat{x}}dydz,\\
d\bm{A}_{y}&=d\bm{\ell}_{z}\times d\bm{\ell}_{x}=\bm{\hat{z}}\times\bm{\hat{x}}dydz=\bm{\hat{y}}dzdx,
\end{aligned}
:::
and a differential volume element
:::{math}
:enumerated: false
dV=|d\bm{A}_x\cdot d\bm{\ell}_x|=|d\bm{A}_y\cdot d\bm{\ell}_y|=dxdydz.
:::
In cylindrical coordinates $(r,\vartheta,z)$, the differential line elements are computed to be
:::{math}
:enumerated: false
\begin{aligned}
d\bm{\ell}_{r}&=(\cos\vartheta\bm{\hat{x}}+\sin\vartheta\bm{\hat{y}})dr,\\
d\bm{\ell}_{\vartheta}&=(-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})d\vartheta,\\
d\bm{\ell}_{z}&=\bm{\hat{z}}dz.
\end{aligned}
:::
They generate differential oriented surface elements such as
:::{math}
:enumerated: false
\begin{aligned}
d\bm{A}_{z}&=d\bm{\ell}_{r}\times d\bm{\ell}_{\vartheta}\\
&=(\cos\vartheta\bm{\hat{x}}+\sin\vartheta\bm{\hat{y}})\times (-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})drd\vartheta\\
&=\bm{\hat{z}}rdrd\vartheta,
\end{aligned}
:::
and
:::{math}
:enumerated: false
\begin{aligned}
d\bm{A}_{r}&=d\bm{\ell}_{\vartheta}\times d\bm{\ell}_{z}\\
&=(-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})\times \bm{\hat{z}}d\vartheta dz\\
&=(r\sin\vartheta\bm{\hat{y}}+r\cos\vartheta\bm{\hat{x}})d\vartheta dz,
\end{aligned}
:::
from which a differential volume element can be computed
:::{math}
:enumerated: false
dV=|d\bm{A}_{z}\cdot d\bm{\ell}_{z}|=|d\bm{A}_r\cdot d\bm{\ell}_r|=rdrd\vartheta dz.
:::
::::

(sec-differential-elements-evolution)=
## <span class="advanced"></span> Evolution of differential elements
The initial position of a pollen grain, dropped into a flowing fluid, got mapped into a new position over time. Similarly, also the vectors $\partial\bm{x}/\partial \xi_i$ that generate the differential line, surface, and volume elements with respect to arbitrary coordinate system evolve in time if pushed forward by the flow map $\bm{\psi}_t$ of a vector field $\bm{u}(\bm{x},t)$. Here a deliberate distinction is made. The vector field $\bm{u}(\bm{x},t)$ and the associated $\bm{\psi}_t$ are not necessarily the velocity field $\bm{v}(\bm{x},t)$ and the flow map $\bm{\phi}_t$ of the fluid motion but any smooth general vector field and its flow map. The time-dependence in the orientation and length of the generating vectors $\partial\bm{x}/\partial \xi_i$ then compounds into changes in the differential objects the vectors generate, as illustrated in {numref}`fig-coordinate-vectors-movement`.
:::{figure} ./figs/fig-coordinate-vectors-movement.svg
:label: fig-coordinate-vectors-movement
:align: center
:width: 100%
Movement of the vectors generating differential line elements.
:::

The rate of change of the vectors along the flow can be computed using the chain rule for differentiation and the differential equation
:::{math}
\frac{d}{dt}\bm{\psi}_t(\bm{x})=\bm{u}(\bm{\psi}_t(\bm{x}),t),\quad \bm{\psi}_{t_0}(\bm{x})=\bm{x},
:::
that defines the flow map $\bm{\psi}_t$ for the vector field $\bm{u}(\bm{x},t)$. At a point $\bm{\psi}_t(\bm{x})$ at time $t$, changing the order of differentiation and applying the chain rule provides
:::{math}
\begin{aligned}
\frac{d}{dt}\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}&=\frac{\partial}{\partial \xi_i}\frac{d\bm{\psi}_t(\bm{x})}{dt}=\frac{\partial \bm{u}(\bm{\psi}_t(\bm{x}),t)}{\partial \xi_i}
=\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}\cdot\nabla\bm{u}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\nabla\bm{u}\right)^\mathsf{T}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i},
\end{aligned}
:::
where $(\nabla\bm{u})^\mathsf{T}|_{(\bm{\psi}_t(\bm{x}),t)}$ is the transpose of the rank-2 tensor field $\nabla\bm{u}$ evaluated at $\bm{\psi}_t(\bm{x})$ at time $t$. 

::::{proof:example}
Consider the time-independent vector field $\bm{u}(\bm{x},t)=ay\bm{\hat{x}}$, where $a$ is a constant with units of inverse time. The flow map $\bm{\psi}_t$ for this field is
:::{math}
:enumerated: false
\bm{\psi}_t(\bm{x})
=\left(x+ay(t-t_0)\right)\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}},
:::
where $\bm{x}=x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}$ denotes the initial position at time $t_0$. The vectors generating the differential line, surface, and volume elements are initially the Cartesian basis vectors. Their evolution can be computed by differentiating the flow map with respect to the initial coordinates:
:::{math}
:enumerated: false
\frac{\partial\bm{\psi}_t}{\partial x}
=\bm{\hat{x}},\qquad 
\frac{\partial\bm{\psi}_t}{\partial y}=a(t-t_0)\bm{\hat{x}}+\bm{\hat{y}},\qquad \frac{\partial\bm{\psi}_t}{\partial z}=\bm{\hat{z}}.
:::
Taking the time derivatives gives
:::{math}
:enumerated: false
\frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial x}=\bm{0},\qquad \frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial y}=a\bm{\hat{x}},\qquad \frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial z}=\bm{0}.
:::
The same result should follow from the velocity gradient tensor. Since the vector field is $\bm{u}=ay\bm{\hat{x}}$, its gradient and transpose are
:::{math}
:enumerated: false
\nabla\bm{u}=a\bm{\hat{y}}\otimes\bm{\hat{x}},
\qquad
(\nabla\bm{u})^\mathsf{T}=a\bm{\hat{x}}\otimes\bm{\hat{y}}.
:::
Using the evolution equation for the coordinate-generating vectors then gives
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial x}&=(\nabla\bm{u})^\mathsf{T}\cdot\bm{\hat{x}}=\bm{0},\\
\frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial y}&=(\nabla\bm{u})^\mathsf{T}\cdot\left(a(t-t_0)\bm{\hat{x}}+\bm{\hat{y}}\right)
=a\bm{\hat{x}},\\\frac{d}{dt}\frac{\partial\bm{\psi}_t}{\partial z}&=(\nabla\bm{u})^\mathsf{T}\cdot\bm{\hat{z}}
=\bm{0}.
\end{aligned}
:::
Both approaches therefore give identical rates of change for the three coordinate-generating vectors. In this example, the vector initially aligned with the $y$-axis progressively tilts towards the $x$-axis, while its length increases. The vectors initially aligned with the $x$- and $z$-axes remain unchanged.
::::

At the same point and time, the differential line, surface, and volume elements are defined
:::{math}
\begin{aligned}
d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{\partial \bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i,\\
d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}&=d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left|d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}\right|.
\end{aligned}
:::
The time rate of change of the line element only requires the substitution of the the rate of change of the vector generating it, resulting in
:::{math}
:label: eq-dl-dt
\begin{aligned}
\frac{d}{dt}d\bm{\ell}_{i}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i=\left(\nabla\bm{u}\right)^\mathsf{T}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i\\
&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{i}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}.
\end{aligned}
:::
One recognizes that the time derivative of the differential line-element is proportional to the element itself but modified by the action of the vector field gradient. This pattern repeats itself also in the time derivatives of the oriented surface element and the volume element. In case of the oriented surface element, the calculation is straightforward, leverages the previous result {numref}`eq-dl-dt`, but requires a bit more algebra, resulting in
:::{math}
:label: eq-dA-dt
\begin{aligned}
\frac{d}{dt}d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\left(d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\nonumber\\
&=\frac{d}{dt}d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times \frac{d}{dt}d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{i}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{\ell}_{i}\big|_{(\bm{\psi}_t(\bm{x}),t)}\times\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{j}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
\end{aligned}
:::
Again, the time rate of change is proportional to the element itself, operated on with a rank-2 tensor involving the vector field gradient. In case of the volume element, the calculation leverages both previous results {numref}`eq-dl-dt` and {numref}`eq-dA-dt`. Choose the ordering of the coordinate directions such that $d\bm{A}_k\cdot d\bm{\ell}_k>0$ initially. Since the flow map preserves orientation, this scalar product remains positive, and taking the absolute value can be omitted. A direct computation then provides
:::{math}
:label: eq-dV-dt
\begin{aligned}
\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\left(d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\nonumber\\
&=\frac{d}{dt}d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{d}{dt}d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot \left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\left((\nabla\bm{u})^\mathsf{T}\cdot d\bm{\ell}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left((\nabla\cdot\bm{u})dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
\end{aligned}
:::
Since the coordinate system $(\xi_1,\xi_2,\xi_3)$ is arbitrary, it can be chosen locally to be adapted to an arbitrary initial curve or oriented surface. In the case of a curve, one chooses one of the coordinates, for example $\xi_i$, to parametrize the initial curve, while keeping the other two coordinates fixed. In the case of an oriented surface, one chooses two coordinates, for example $\xi_i$ and $\xi_j$, to span the initial surface, while keeping the third coordinate $\xi_k$ fixed. The coordinate direction associated with $\xi_k$ can be chosen to point along the surface normal of the initial surface. The coordinate labels are then held fixed as the flow map $\bm{\psi}_t$ carries the initial curve or surface forward in time. The derived evolution equations therefore apply to differential line and surface elements of arbitrary orientation, independently of the coordinate chart used to represent them. Dropping the explicit coordinate labels, one obtains
:::{math}
:label: eq-dl-dA-dV-dt
\begin{aligned}
\frac{d}{dt}d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\frac{d}{dt}d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left((\nabla\cdot\bm{u})dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}.
\end{aligned}
:::
Note, however, that a single coordinate chart is not necessarily sufficient to describe an entire curve or surface. Instead, multiple coordinate patches may need to be used. 

Since $\nabla\cdot\bm{u}=\nabla\bm{u}:\bm{I}$, a common term, the gradient $\nabla\bm{u}$ of the vector field $\bm{u}$, appears in all of the time derivatives of the differential elements in {numref}`eq-dl-dA-dV-dt`. The proportionality of the time rate of change of each element to itself is encoded entirely by the rank-2 tensor $\nabla\bm{u}$. Interesting observations, regarding this term can be made that later help justify the form of the stress tensor. To illustrate the observations, decompose the tensor $\nabla\bm{u}$ into three separate parts
:::{math}
\nabla\bm{u}=\bm{D}+\frac{1}{3}(\nabla\cdot\bm{u})\bm{I}+\bm{\Omega}.
:::
Here the symmetric and traceless tensor $\bm{D}$ and the antisymmetric tensor $\bm{\Omega}$ are 
:::{math}
\begin{aligned}
\bm{D}&=\frac{1}{2}\left(\nabla\bm{u}+(\nabla\bm{u})^\mathsf{T}\right)-\frac{1}{3}(\nabla\cdot\bm{u})\bm{I},\\
\bm{\Omega}&=\frac{1}{2}\left(\nabla\bm{u}-(\nabla\bm{u})^\mathsf{T}\right).
\end{aligned}
:::
While the decomposition may appear superficial, each of the parts has a distinct role in generating and characterizing motion. The term $\tfrac{1}{3}(\nabla\cdot\bm{u})\bm{I}$ describes isotropic deformation, the term $\bm{D}$ describes deformation that is non-isotropic but volume-preserving, and the term $\bm{\Omega}$ describes rotation without deformation. This can be verified by tracking the movement of points $\bm{x}(t)$ in the flow of $\bm{u}(\bm{x},t)$.

(example-odeint)=
::::{proof:example}
The scipy-library offers the method odeint for numerical solution of ordinary differential equations. With the help of it, the flowmap can be computed numerically for arbitrary vector fields and the motion of individual points tracked over time. As an example, consider the numerical integration of the vector field $\bm{v}$ encountered in example {numref}`example-flowmap-analytical`. This can be performed as in the script below
```{literalinclude} python/example-flowmap-with-odeint.py
:language: python
:start-line: 0
:end-line: 49
:linenos:
```
Running the script results in a figure below that confirms the trajectory for the field $\bm{v}$ to be helical and to expand into $\bm{\hat{z}}$ direction at constant velocity. 
:::{image} ./figs/example-fig-flowmap-with-odeint.svg
:align: center
:width: 80%
:::
::::

(example-velocity-gradient-decomposition)=
::::{proof:example}
Consider the following three different velocity fields
:::{math}
:enumerated: false
\begin{aligned}
\bm{u}_D&=\frac{u_0}{L_0}(x\bm{\hat{x}}-y\bm{\hat{y}}),\\
\bm{u}_\Omega&=\frac{u_0}{L_0}(-y\bm{\hat{x}}+x\bm{\hat{y}}),\\
\bm{u}_\text{div}&=\frac{u_0}{L_0}(x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}).
\end{aligned}
:::
The field $\bm{u}_D$ pushes points away from the $x=0$ plane and towards the $y=0$ plane with speed proportional to the distance from the planes. The field $\bm{u}_\Omega$ rotates points counter clockwise about the $z$-axis. The field $\bm{u}_\text{div}$ pushes points away from origin with speed proportional to the distance from the origin. For each field, only one contribution to the velocity gradient tensor is non-zero. For the field $\bm{u}_D$, one may compute
:::{math}
:enumerated: false
\begin{aligned}
\bm{D}(\bm{u}_D)&=\frac{u_0}{L_0}(\bm{\hat{x}}\otimes\bm{\hat{x}}-\bm{\hat{y}}\otimes\bm{\hat{y}}),\\
\bm{\Omega}(\bm{u}_D)&=\bm{0},\\
\nabla\cdot\bm{u}_D&=0.
\end{aligned}
:::
For the field $\bm{u}_\Omega$, one computes instead
:::{math}
:enumerated: false
\begin{aligned}
\bm{D}(\bm{u}_\Omega)&=\bm{0},\\
\bm{\Omega}(\bm{u}_\Omega)&=\frac{u_0}{L_0}(\bm{\hat{x}}\otimes\bm{\hat{y}}-\bm{\hat{y}}\otimes\bm{\hat{x}}),\\
\nabla\cdot\bm{u}_\Omega&=0.
\end{aligned}
:::
Finally, for the field $\bm{u}_\text{div}$, one obtains
:::{math}
:enumerated: false
\begin{aligned}
\bm{D}(\bm{u}_\text{div})&=\bm{0},\\
\bm{\Omega}(\bm{u}_\text{div})&=\bm{0},\\
\nabla\cdot\bm{u}_\text{div}&=\frac{3u_0}{L_0}.
\end{aligned}
:::
To demonstrate that each part of the $\nabla\bm{u}$ tensor indeed corresponds to the stated motion, integrate points in space according to the differential equation
:::{math}
:enumerated: false
\frac{d\bm{x}(t)}{dt}=\bm{u}(\bm{x}(t)),
:::
until a time of $t=(2L_0/u_0)$ for each of the specified vector fields $\bm{u}$. For the integration, one may use a script similar as in {numref}`example-odeint`. The projection of a cube of points onto the $x$-$y$ plane, initially standing on its edge, changes in the following manner under the different vector fields
:::{image} ./figs/example-fig-D-Omega-div-flow-individually.svg
:align: center
:width: 100%
:::
The field $\bm{u}_D$ has indeed stretched the cube in the $x$-direction and squeezed it in the $y$-direction, corresponding to non-isotropic volume-preserving deformation. The field $\bm{u}_\Omega$ has rotated the square around the $z$-axis without deforming it. The field $\bm{u}_\text{div}$ has isotropically scaled the cube volume.

More diverse effects are observed for velocity fields that have more complicated spatial dependencies. For example, in the vector field
:::{math}
:enumerated: false
\bm{u}=u_0\frac{-y\bm{\hat{x}}+x\bm{\hat{y}}}{\sqrt{x^2+y^2}}+\frac{u_0}{L_0^2}(x^2\bm{\hat{x}}+y^2\bm{\hat{y}}+z^2\bm{\hat{z}}),
:::
the first term introduces constant tangential speed, while the second terms adds spatially varying deformation and dilatation. The vector field therefore generally has nonzero contributions from all three parts of the $\nabla\bm{u}$ tensor field. The motion corresponding to the field, projected onto the $x$-$y$ plane, is illustrated below.
:::{image} ./figs/example-fig-D-Omega-div-flow-complicated.svg
:align: center
:width: 50%
:::
::::


(sec-leibniz-rule-derivation)=
## <span class="advanced"></span> Derivation of the Leibniz rules
Equipped with the knowledge of how differential elements change under the flow of a vector field $\bm{u}(\bm{x},t)$, pushed forward by the flow map $\bm{\psi}_t$, one is ready to apply the associated formulae {numref}`eq-dl-dA-dV-dt` and compute time derivatives of integrals over curves, surfaces, and volumes that move along the flow of the field.

Define a time dependent curve $C(t)$, an oriented surface $S(t)$, and a volume $V(t)$ as images of some initial curve $C(t_0)$, surface $S(t_0)$, and volume $V(t_0)$ with respect to the flow map $\bm{\psi}_t$
:::{math}
\begin{aligned}
C(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in C(t_0)\},\\
S(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in S(t_0)\},\\
V(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in V(t_0)\}.
\end{aligned}
:::
Consider the following integrals over the time-dependent curve, surface, and volume
:::{math}
\begin{aligned}
\int_{C(t)}\bm{f}(\bm{x},t)\cdot d\bm{\ell}\big|_{\bm{x}},\\
\int_{S(t)}\bm{f}(\bm{x},t)\cdot d\bm{A}\big|_{\bm{x}},\\
\int_{V(t)}\bm{f}(\bm{x},t)dV\big|_{\bm{x}}.
\end{aligned}
:::
In the line and surface integrals, the field $\bm{f}$ must be a vector field. In the volume integral, the field $\bm{f}$ can more generally be scalar-, vector-, or even tensor-valued. Here, the integration label $\bm{x}$ is shown explicitly for the differential elements, for book-keeping. 

Perform then a change of integration labels with the help of the flow map so that 
:::{math}
\begin{aligned}
\int_{C(t)}\bm{f}(\bm{x},t)\cdot d\bm{\ell}\big|_{\bm{x}}&=\int_{C(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\int_{S(t)}\bm{f}(\bm{x},t)\cdot d\bm{A}\big|_{\bm{x}}&=\int_{S(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\int_{V(t)}\bm{f}(\bm{x},t)dV\big|_{\bm{x}}&=\int_{V(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}.
\end{aligned}
:::
On the left, the label $\bm{x}$ denotes the time-dependent domains $C(t)$, $S(t)$, and $V(t)$. On the right, the label $\bm{x}$ denotes the time-independent domains $C(t_0)$, $S(t_0)$, $V(t_0)$ instead, and the time dependence has been moved inside the integrals via the change of integration labels with the flow map. Since the integration domains no longer depend on time, computation of time derivatives of the integrals can be performed. Before that, use the chain rule and {numref}`eq-dl-dA-dV-dt` to compute the derivatives
:::{math}
\begin{aligned}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot \frac{d}{dt}d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
\end{aligned}
:::
:::{math}
\begin{aligned}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot \frac{d}{dt}d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+(\nabla\cdot\bm{u})\bm{f}-\bm{f}\cdot\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})-\bm{f}\cdot\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
\end{aligned}
:::
:::{math}
\begin{aligned}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}(\nabla\cdot\bm{u})\right)dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})\right)dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
\end{aligned}
:::
In the volume related term, if $\bm{f}$ is a scalar, then $\bm{u}\otimes\bm{f}$ reduces to $\bm{u}f$. Now, with the help of the formula above, calculate the time derivative of the line integral and transforms the integration labels back to the time dependent domain
:::{math}
:label: eq-leibniz-rule-line
\begin{aligned}
\frac{d}{dt}\int_{C(t)}(\bm{f}\cdot d\bm{\ell})\big|_{(\bm{x},t)}&=\int_{C(t_0)}\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\int_{C(t_0)}\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\int_{C(t)}\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{x},t)}.
\end{aligned}
:::
To calculate the time derivative of the surface integral, exactly the same steps are used. Transformation of the labeling to time-independent domain, calculation of the time derivative of the integrand and the surface element, and transformation back to the time-dependent labeling. This process results in
:::{math}
:label: eq-leibniz-rule-surface
\frac{d}{dt}\int_{S(t)}(\bm{f}\cdot d\bm{A})\big|_{(\bm{x},t)}=\int_{S(t)}\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})-\bm{f}\cdot\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{x},t)}.
:::
For the volume integral, the same steps provides the formula
:::{math}
:label: eq-leibniz-rule-volume
\frac{d}{dt}\int_{V(t)}(\bm{f}dV)\big|_{(\bm{x},t)}=\int_{V(t)}\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})\right)dV\right)\big|_{(\bm{x},t)}.
:::
Since the integration labels on both sides now are the same again, they are usually dropped. 

Each of the derived integral formulae have their place in fluid mechanics. In these notes, equation {numref}`eq-leibniz-rule-volume` is utilized to derive the fluid equations and to establish engineering balance equations over control volumes. Once fluid equations are established, the equation {numref}`eq-leibniz-rule-surface` can be used to prove the conservation of vorticity flux through a surface that moves with the fluid in inviscid barotropic flows, a result better known as Helmholtz's vortex theorem. The equation {numref}`eq-leibniz-rule-line`, on the other hand, could be used to prove Kelvin's circulation theorem for similar fluids. These theorems have important applications in studies of atmospheric flows.

As in these notes the time derivative of the volume integral has a major role, it is useful to convert the divergence term into a surface term for its physical interpretation. With the divergence theorem, one finds
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\bm{f}dV}_{\substack{\text{Time rate of change}\\\text{of an integral of}\,\bm{f}\\\text{calculated over the}\\\text{moving volume}}}=\underbrace{\int_{V(t)}\partial_t \bm{f}dV}_{\substack{\text{Integral of the local}\\\text{temporal change}\,\partial_t\bm{f}\\\text{calculated over the}\\\text{moving volume}}} +\underbrace{\int_{\partial V(t)}\bm{f}\underbrace{\bm{u}\cdot\bm{\hat{n}} dA}_{\substack{\text{Local rate of}\\\text{change of the}\\\text{volume from}\\\text{boundary}\\\text{movement}}}}_{\substack{\text{Contribution to the integral}\\\text{from boundary movement}}}.
:::

::::{proof:example}
The three-dimensional derivation of the Leibniz rule combines several mathematical steps. These steps can be illustrated also in a simpler and more familiar setting in one dimension.

To differentiate the time-dependent integral
:::{math}
:enumerated: false
\int_{a(t)}^{b(t)} f(x,t) dx,
:::
with $a(t)$ and $b(t)$ some time-dependent, well-behaving functions describing the positions of the integral boundaries in time $t$, assume any point $x\in[a(t),b(t)]$ to move with the speed $u(x,t)$. Let $\psi(x,t)$ be the flow map of $u(x,t)$ so that a point $x_0\in[a(t_0),b(t_0)]$ becomes a point $\psi(x_0,t)=x$ and $\partial_t\psi(x,t)=u(\psi(x,t),t)$. One may now write
:::{math}
:enumerated: false
\begin{aligned}
\int_{a(t)}^{b(t)} f(x,t) dx&=\int_{\psi(a(t_0),t)}^{\psi(b(t_0),t)}f(x,t)dx=\int_{a(t_0)}^{b(t_0)}f(\psi(x_0,t),t)d\psi(x_0,t)\\
&=\int_{a(t_0)}^{b(t_0)}f(\psi(x_0,t),t)\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0.
\end{aligned}
:::
To proceed, apply the chain rule to the derivative of the flow map
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}&=\frac{\partial^2\psi(x,t)}{\partial x\partial t}\Big|_{(x_0,t)}=\frac{\partial u(\psi(x,t),t)}{\partial x}\Big|_{(x_0,t)}\\
&=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}.
\end{aligned}
:::
One may now identify that 
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}d\psi(x_0,t)&=\frac{d}{dt}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0\\
&=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}d\psi(x_0,t),
\end{aligned}
:::
is analogous to the time derivative of a differential volume element with $\partial u/\partial x$ serving the role of velocity divergence. Considering that the time derivative of the composed function $f(\psi(x_0,t),t)$ can be written 
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}f(\psi(x_0,t),t)&=\frac{\partial f}{\partial t}\Big|_{(\psi(x_0,t),t)}+\frac{\partial f}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial \psi}{\partial t}\Big|_{(x_0,t)}\\
&=\left(\frac{\partial f}{\partial t}+u\frac{\partial f}{\partial x}\right)\Big|_{(\psi(x_0,t),t)},
\end{aligned}
:::
the time derivative of the integral becomes
:::{math}
:enumerated: false
\begin{aligned}
\frac{d}{dt}\int_{a(t)}^{b(t)} f(x,t) dx&=\int_{a(t_0)}^{b(t_0)}\frac{d}{dt}\left(f(\psi(x_0,t),t)\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}\right)dx_0\\
&=\int_{a(t_0)}^{b(t_0)}\left(\frac{\partial f}{\partial t}+u\frac{\partial f}{\partial x}+f\frac{\partial u}{\partial x}\right)\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0\\
&=\int_{a(t)}^{b(t)}\left(\frac{\partial f}{\partial t}+\frac{\partial(uf)}{\partial x}\right)\Big|_{(x,t)}dx\\
&=\int_{a(t)}^{b(t)}\frac{\partial f(x,t)}{\partial t}dx+\Big[u(x,t)f(x,t)\Big]_{x=a(t)}^{x=b(t)}.
\end{aligned}
:::
The result is the one-dimensional version of the Leibniz rule. 
Realizing that the speed function $u(x,t)$ at the boundary points satisfies $u(a(t),t)=da/dt$ and $u(b(t),t)=db/dt$ enables writing
:::{math}
:enumerated: false
\frac{d}{dt}\int_{a(t)}^{b(t)}f(x,t)dx=\int_{a(t)}^{b(t)}\frac{\partial f(x,t)}{\partial t}dx+f(b(t),t)\frac{db(t)}{dt}-f(a(t),t)\frac{da(t)}{dt},
:::
which recovers the familiar and well-known rule for differentiating one-dimensional integrals with changing boundaries.
::::

(sec-conservation-of-mass)=
## <span class="elementary"></span> Conservation of mass
Consider a time-dependent volume $V(t)$ of fluid moving according to the fluid's velocity field $\bm{v}(\bm{x},t)$ as in {numref}`fig-material-volume`. Such volume is tied to the fluid material and generally referred to as a material volume. Mass within it remains fixed in time, regardless of what happens to the volume shape. This is referred to as conservation of mass.
::::{figure} ./figs/fig-material-volume.svg
:label: fig-material-volume
:align: center
:width: 100%
Evolution of a material volume $V(t)$ attached to the flow of the fluid's velocity field $\bm{v}(\bm{x},t)$.
::::

This conservation of mass within any material volume has consequences for the fluid density field $\rho(\bm{x},t)$. A differential volume element $dV$ carries a differential mass of $\rho dV$ of the fluid. A macroscopic material volume $V(t)$ therefore carries the mass $\int_{V(t)}\rho dV$. Since the mass within a material volume remains constant in time, the time derivative of the mass must be zero.
:::{math}
\frac{d}{dt}\int_{V(t)}\rho dV=0.
:::
Next apply the Leibniz integral differentiation rule {numref}`eq-leibniz-rule-surface-form` and {numref}`eq-leibniz-rule-volume-form` by setting $\bm{f}=\rho$ and $\bm{u}=\bm{v}$. The time derivative of the mass within a material volume can then be expressed as 
:::{math}
\begin{aligned}
\underbrace{\frac{d}{dt}\int_{V(t)}\rho dV}_{\substack{\text{Rate of change of}\\\text{fluid mass in}\,V(t)}}&=\underbrace{\int_{V(t)}\partial_t\rho \,dV}_{\substack{\text{Contribution from}\\\text{local temporal}\\\text{density change}}}+\underbrace{\int_{\partial V(t)}\rho\underbrace{\bm{v}\cdot\bm{\hat{n}}dA}_{\substack{\text{Local rate of}\\\text{volume change}}}}_{\substack{\text{Contribution from}\\\text{boundary movement}}}\\
&=\int_{V(t)}\left(\partial_t\rho+\nabla\cdot(\bm{v}\rho)\right)dV.
\end{aligned}
:::
The boundary $\partial V(t)$ moves with the fluid and no fluid crosses it. The surface contribution accounts for the change in the integral caused by movement of the integration domain, not for mass transporting through the surface. Since the time derivative of mass must vanish, the integral on the right must be zero. However, the choice of the initial $V(t_0)$ is arbitrary, and the integral must therefore vanish for every volume $V(t)$. Consequently the integrand must be zero everywhere, which results in the partial differential equation for density
:::{math}
:label: eq-continuity
\partial_t\rho+\nabla\cdot(\bm{v}\rho)=0.
:::
This equation is often referred to as the continuity equation and it generally describes the changes in density in response to the fluid's velocity.

(example-density-change)=
::::{proof:example}
Consider a velocity field of the form
:::{math}
:enumerated: false
\bm{v}(\bm{x},t)=v(z)\bm{\hat{z}}
:::
describing one-dimensional time-independent flow into $\bm{\hat{z}}$-direction with speed $v(z)$ that may vary with respect to the coordinate $z$. Assuming that also the density is steady in time and changes only with respect to the coordinate $z$, the fluid's density equation reduces to
:::{math}
:enumerated: false
\partial_t\rho+\nabla\cdot(\bm{v}\rho) \quad \implies \quad \frac{d}{dz}(v(z)\rho(z))=0
:::
This means the scalar velocity $v(z)$ times the density $\rho(z)$ has to be a constant, and that density is given by
:::{math}
:enumerated: false
\rho(z)=\frac{\rho_0v_0}{v(z)}
:::
with $\rho_0$ and $v_0$ some constants. If the fluid at some location $z$ flows with slower speed, the density at that location must be higher to satisfy the conservation of mass. Conversely, if the fluid locally has a higher speed, the density must be lower.
::::

The physical law of mass conservation has a mathematical consequence that is found particularly convenient in sections that follow. According to the Leibniz rule {numref}`eq-leibniz-rule-volume-form` and the continuity equation {numref}`eq-continuity`, the time rate of change of the volume integral of a quantity $\rho\bm{f}$, where $\bm{f}$ may be any scalar, vector, or tensor field, can be computed as
:::{math}
\begin{aligned}
\frac{d}{dt}\int_{V(t)}\rho \bm{f} dV
&=\int_{V(t)}\left(\partial_t(\rho\bm{f})+\bm{v}\cdot\nabla(\rho\bm{f})+\rho\bm{f}\nabla\cdot\bm{v}\right)dV\\
&=\int_{V(t)}\left(\bm{f}(\partial_t\rho+\nabla\cdot(\bm{v}\rho))+\rho(\partial_t\bm{f}+\bm{v}\cdot\nabla\bm{f})\right)dV\\
&=\int_{V(t)}\rho(\partial_t\bm{f}+\bm{v}\cdot\nabla\bm{f})dV.
\end{aligned}
:::
Physically, the expression $\partial_t\bm{f}+\bm{v}\cdot\nabla\bm{f}$ describes the time rate of change of $\bm{f}$ at a point which moves according to the vector field $\bm{v}$. This can be verified by letting the flow map $\bm{\phi}_t$ of the vector field $\bm{v}$ do its job:
:::{math}
\frac{d}{dt}\bm{f}(\bm{\phi}_t(\bm{x}),t)=(\partial_t\bm{f}+\bm{v}\cdot\nabla\bm{f})\big|_{(\bm{\phi}_t(\bm{x}),t)}
:::
It is therefore common to refer to the scalar-valued differential operator 
:::{math}
:label: eq-material-derivative
\frac{D}{Dt}=\partial_t+\bm{v}\cdot\nabla, \qquad \text{Material derivative},
:::
as the material derivative. This term and operator are used extensively in fluid and solid mechanics texts. In terms of it, the following integral identity holds over material volumes
:::{math}
:label: eq-rho-identity
\frac{d}{dt}\int_{V(t)}\rho \bm{f} dV=\int_{V(t)}\rho\frac{D\bm{f}}{Dt}dV,
:::
and the continuity equation {numref}`eq-continuity` can be written also in the form
:::{math}
\frac{1}{\rho}\frac{D\rho}{Dt}=-\nabla\cdot\bm{v}.
:::
In this form, the equation indicates that a relative change in density along the fluid flow results from the velocity field diverging or converging, as observed also in {numref}`example-density-change`.

(example-acceleration-of-a-point)=
::::{proof:example}
The acceleration of a point $\bm{\phi}_t(\bm{x})$ following the velocity field $\bm{v}$ equals the material derivative of the velocity field evaluated along the trajectory at the same point:
:::{math}
:enumerated: false
\frac{d^2}{dt^2}\bm{\phi}_t(\bm{x})=\frac{d}{dt}\bm{v}(\bm{\phi}_t(\bm{x}),t)=(\partial_t\bm{v}+\bm{v}\cdot\nabla\bm{v})\big|_{(\bm{\phi}_t(\bm{x}),t)}=\frac{D\bm{v}}{Dt}\big|_{(\bm{\phi}_t(\bm{x}),t)}.
:::
::::

(sec-conservation-of-momentum)=
## <span class="elementary"></span> Conservation of momentum
According to Newton's second law, the time rate of change of linear momentum of a material volume equals the resultant force acting on it. This is the momentum balance for a material system. For the present discussion, the forces acting on a material volume consist of gravity and mechanical contact forces. Gravity acts throughout the volume as a body force and has a remote source, typically the mass of Earth. Mechanical contact forces act on the surface of the material volume and arise locally from direct contact of the volume with another material volume. Since the total force on a material volume is finite, yet distributed over the volume and its surface, local expressions for both gravity and contact force must be differential, and the total force expressed as integrals of the differential forces over the material volume and its surface.

Denote with $\bm{g}$ the gravitational acceleration. According Newton's second law, acceleration describes force per unit mass. Since a differential volume $dV$ of fluid contains a differential mass $\rho dV$, the differential body force from gravity on a differential volume of fluid is given by
:::{math}
\delta\bm{F}_b=\rho\bm{g}dV.
:::

Let then $dA$ be a differential area on the surface of the volume, oriented with respect to an outward surface unit normal vector $\bm{\hat{n}}$. Denote with the vector field $\bm{t}$ the force on the surface per unit area, referred to as traction. The differential contact force $\delta\bm{F}_s$ acting locally on a surface is then
:::{math}
\delta\bm{F}_s=\bm{t}dA.
:::
Both $\delta\bm{F}_b$ and $\delta\bm{F}_s$ are vector-valued differential quantities rather than ordinary vectors. Their integrals over a finite volume and surface, respectively, yield ordinary force vectors. The differential forces acting on a volume $V(t)$ with a boundary $\partial V(t)$ are illustrated in {numref}`fig-body-and-surface-forces` together with the surface outward unit normal.
:::{figure} ./figs/fig-body-and-surface-forces.svg
:label: fig-body-and-surface-forces
:align: center
:width: 55%
The differential surface and body forces $\delta\bm{F}_s$ and $\delta\bm{F}_b$ acting on a fluid volume.
:::

With $\bm{v}$ the fluid's velocity field, the differential amount of momentum the fluid carries in a differential volume $dV$ is $\rho\bm{v}dV$. For a macroscopic material volume $V(t)$ such as the one in {numref}`fig-material-volume`, Newton's second law then reads
:::{math}
:label: eq-newton
\underbrace{\frac{d}{dt}\int_{V(t)}\rho\bm{v}dV}_{\substack{\text{Time rate of change}\\\text{of momentum in}\,V(t)}} = \underbrace{\int_{V(t)}\delta\bm{F}_b}_{\substack{\text{Total body}\\\text{force on}\,V(t)}} + \underbrace{\int_{\partial V(t)}\delta\bm{F}_s}_{\substack{\text{Total surface}\\\text{force on}\,\partial V(t)}}.
:::
On the left, the material derivative identity {numref}`eq-rho-identity`, via setting $\bm{f}=\bm{v}$, enables one to move the time derivative inside the integral and to write
:::{math}
\frac{d}{dt}\int_{V(t)}\rho\bm{v}dV = \int_{V(t)}\rho\frac{D\bm{v}}{Dt}dV.
:::
On the right, the total body force is expressed as a volume integral but the total contact force involves a surface integral, which prevents immediately obtaining a local differential equation as in {numref}`sec-conservation-of-mass` in the case of mass conservation. 

A careful investigation of Newton's second law reveals that the traction acting on arbitrary surface must be expressible in terms of a rank-2 tensor $\bm{\sigma}$, referred to as Cauchy's stress tensor
:::{math}
\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}.
:::
The detailed arguments leading to this conclusion are presented in the advanced {numref}`sec-stress-tensor` for those interested. With the help of the stress tensor and the divergence theorem {numref}`eq-divergence-theorem`, the total force on a material fluid volume can then be written as a volume integral
:::{math}
\begin{aligned}
\int_{V(t)}\delta \bm{F}_b+\int_{\partial V(t)}\delta\bm{F}_s&=\int_{V(t)}\rho\bm{g}dV+\int_{\partial V(t)}\bm{\sigma}\cdot\bm{\hat{n}}dA\\
&=\int_{V(t)}(\rho\bm{g}+\nabla\cdot\bm{\sigma}^\mathsf{T})dV.
\end{aligned}
:::

Since Newton's second law holds for an arbitrary material volume, the integrands on the left and right sides of it must be equal everywhere. Consequently, the fluid velocity field must satisfy the following local partial differential equation
:::{math}
:label: eq-cauchy-without-symmetry
\rho\frac{D\bm{v}}{Dt}=\rho\bm{g}+\nabla\cdot\bm{\sigma}^\mathsf{T}.
:::
Finally, the requirement that the time rate of change of angular momentum of a material volume be accounted for solely by the torques of the body and surface forces further restricts the stress tensor to be symmetric, $\bm{\sigma}=\bm{\sigma}^\mathsf{T}$. The detailed arguments leading to this conclusion are presented in the intermediate {numref}`sec-symmetry-of-stress` for those interested. With respect to a symmetric stress tensor, on obtains
:::{math}
:label: eq-cauchy
\rho\frac{D\bm{v}}{Dt}=\rho\bm{g}+\nabla\cdot\bm{\sigma},
:::
commonly referred to as the Cauchy's momentum equation. After introducing a constitutive relation for $\bm{\sigma}$, the Cauchy momentum equation is seen to correspond to the famous Navier-Stokes equation.

::::{proof:example}
Recall from {numref}`example-acceleration-of-a-point` that the material derivative of the velocity field $\bm{v}$ at a point $\bm{\phi}_t(\bm{x})$ that moves with the fluid represents the local acceleration of the point $\bm{\phi}_t(\bm{x})$.
Cauchy's momentum equation then tells that the local acceleration is caused by gravity and divergence of the stress tensor
:::{math}
:enumerated: false
\frac{d^2}{dt^2}\bm{\phi}_t(\bm{x})=\frac{D\bm{v}}{Dt}\big|_{(\bm{\phi}_t(\bm{x}),t)}=\left(\bm{g}+\rho^{-1}\nabla\cdot\bm{\sigma}\right)\big|_{(\bm{\phi}_t(\bm{x}),t)}.
:::
The gravitational acceleration contributes to the local acceleration even if it is uniform throughout space. In contrast, a spatially uniform stress tensor has zero divergence and therefore produces no net contact force on a closed material volume.
::::
::::{proof:example}
Consider a fluid at rest, meaning that its velocity field vanishes, $\bm{v}(\bm{x},t)=\bm{0}$. Cauchy's momentum equation then reduces to
:::{math}
:enumerated: false
\rho\bm{g}+\nabla\cdot\bm{\sigma}=\bm{0}, \qquad \text{Fluid at rest}
:::
For a simple fluid at rest, the stress is isotropic and represented entirely by the thermodynamic pressure
:::{math}
:enumerated: false
\bm{\sigma}=-p\bm{I}, \qquad\text{Fluid at rest}
:::
Taking the vertical coordinate $z$ to be positive upwards, and assuming gravitational acceleration to be $\bm{g}=-g\bm{\hat{z}}$, Cauchy's momentum equation then provides the differential equation for hydrostatic pressure
:::{math}
:enumerated: false
\rho\bm{g}+\nabla\cdot(-p\bm{I})=\bm{0} \quad \implies \quad \frac{dp}{dz}=-\rho g.
:::
::::

(sec-stress-tensor)=
## <span class="advanced"></span> Cauchy's theorem and emergence of the stress tensor
In derivation of Cauchy's momentum equation, the traction vector on a surface of a material volume was assumed expressible as $\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}$ where $\bm{\sigma}$ is a rank-2 tensor referred to as stress and $\bm{\hat{n}}$ is the surface unit normal out from the volume. This assumption is far from trivial, a cornerstone for both fluid and solid mechanics, and therefore proved rigorously in this section. The requirement of $\bm{\sigma}$ to be symmetric is explained separately in {numref}`sec-symmetry-of-stress`. 

To understand why the traction vector must be a function of the unit surface normal in the first place, recall that surface forces represent the point-wise effect of contact between two material volumes. When one material volume causes a contact force on another, Newton's third law states that there must be a counter force of equal magnitude into the opposite direction at the exact same location of contact. Since the contact happens on a surface whose orientation is described by the unit outward normal vector, also the force and its counter force must be orientable with respect to the surface unit normal vector. Therefore, the traction generally is assumed to be a smooth vector field that depends on time and position as
:::{math}
\bm{t}=\bm{t}(\bm{x},t,\bm{\hat{n}}(\bm{x},t)).
:::

The linear dependence of traction on the unit surface normal is established in two phases. In both phases, the mean value theorem of vector fields is leveraged to express averages of volume and surface integrals in terms of their integrands over two particularly chosen domains. Hence the theorem is stated first. Let $\mathcal{V}$ and $\mathcal{A}$ be a bounded volumetric domain and surface with volume $V$ and area $A$, respectively. Let the vector field $\bm{f}$ be bounded and Riemann integrable on $\mathcal{V}$ and $\mathcal{A}$. The mean value theorem then states that the averages of $\bm{f}$ over $\mathcal{V}$ and $\mathcal{A}$ belong to the closures of the convex hulls of the images of the corresponding domains under the vector field $\bm{f}$, namely
:::{math}
:label: eq-mean-value-theorem
\begin{aligned}
\frac{1}{V}\int_\mathcal{V}\bm{f}dV &\in \overline{\text{conv}(\{\bm{f}(\bm{x})\mid\bm{x}\in \mathcal{V}\})},\\
\frac{1}{A}\int_\mathcal{A}\bm{f}dA &\in \overline{\text{conv}(\{\bm{f}(\bm{x})\mid\bm{x}\in \mathcal{A}\})}.
\end{aligned}
:::
The theorem may appear intimidating at first. It nevertheless constitutes a straightforward idea illustrated with the following example.
::::{proof:example}
Consider the two-dimensional domain 
:::{math}
:enumerated: false
\mathcal{A}=\{(x,y)\in\mathbb{R}^2\mid 0\leq x\leq 3, 0\leq y\leq 1\},
:::
with area $A=3$. Divide it into three non-overlapping subdomains
:::{math}
:enumerated: false
\begin{aligned}
\mathcal{A}_1&=\{(x,y)\in\mathbb{R}^2\mid 0\leq x < 1, 0\leq y\leq 1\},\\
\mathcal{A}_2&=\{(x,y)\in\mathbb{R}^2\mid 1\leq x < 2, 0\leq y\leq 1\},\\
\mathcal{A}_3&=\{(x,y)\in\mathbb{R}^2\mid 2\leq x \leq 3, 0\leq y\leq 1\},
\end{aligned}
:::
with each an equal area of $A_1=A_2=A_3=1$. 
:::{image} ./figs/example-fig-integral-identity-domain.svg
:align: center
:width: 60%
:::
Let the vector field $\bm{f}$ be piece-wise constant
:::{math}
:enumerated: false
\begin{aligned}
\bm{f}(\bm{x})=\left\{\begin{aligned}\bm{f}_1&=-\bm{\hat{x}}-\bm{\hat{y}}, && \bm{x}\in \mathcal{A}_1,\\
\bm{f}_2&=2\bm{\hat{y}}, && \bm{x}\in \mathcal{A}_2,\\
\bm{f}_3&=2\bm{\hat{x}}, && \bm{x}\in \mathcal{A}_3.\end{aligned}\right.
\end{aligned}
:::
The average of $\bm{f}$ is then
:::{math}
:enumerated: false
\begin{aligned}
\frac{1}{A}\int_A\bm{f}dA&=\frac{1}{A}\left(\bm{f}_1 A_1+\bm{f}_2 A_2+\bm{f}_3 A_3\right)\\
&=\frac{1}{3}\bm{\hat{x}}+\frac{1}{3}\bm{\hat{y}},
\end{aligned}
:::
and belongs to the closure of the convex hull of the set $\{\bm{f}_1,\bm{f}_2,\bm{f}_3\}$ indicated as the orange domain below.
:::{image} ./figs/example-fig-integral-identity-convex-hull.svg
:align: center
:width: 45%
:::
::::

Next, assume a time-dependent volumetric material domain $\mathcal{V}(t)$ with a volume $V(t)$ and an enclosing boundary surface $\partial\mathcal{V}(t)$. Split the boundary surface into touching subsets $\{\mathcal{A}_i(t)\}_{i}$ with respective areas $\{A_i(t)\}_i$ that together cover the entire boundary $\partial\mathcal{V}(t)$. Then use the identity {numref}`eq-rho-identity` and group the terms appearing in Newton's second law {numref}`eq-newton` as
:::{math}
:label: eq-regrouped-newton
\int_{\mathcal{V}(t)}\left(\rho\frac{D\bm{v}}{Dt}-\rho\bm{g}\right)dV=\sum_i\int_{\mathcal{A}_i(t)}\bm{t}dA,
:::
separating the volume and surface terms to the different sides. According to the mean value theorem {numref}`eq-mean-value-theorem`, there now exist time-dependent vectors $\bm{f}(t)$ and $\{\bm{t}_i(t)\}_i$ that belong to the closures of convex hulls
:::{math}
\begin{aligned}
\bm{f}(t)&\in\overline{\text{conv}\{(\rho(D\bm{v}/Dt)-\rho\bm{g})\big|_{(\bm{y},t)} \mid \bm{y}\in\mathcal{V}(t)\}},\\
\bm{t}_i(t)&\in\overline{\text{conv}\{\bm{t}(\bm{y},t,\bm{\hat{n}}(\bm{y},t)) \mid \bm{y}\in\mathcal{A}_i(t)\}},
\end{aligned}
:::
in terms of which the regrouped Newton's second law {numref}`eq-regrouped-newton` can be expressed as 
:::{math}
:label: eq-mean-value-newton
\bm{f}(t)V(t)=\sum_i\bm{t}_i(t)A_i(t).
:::
As the next steps, one considers specific choices for the material volume, and investigates the mean value form {numref}`eq-mean-value-newton` of Newton's second law while the chosen material volumes are shrunk to a single point. 

In the first phase, one requires the material volume $\mathcal{V}(t)$ at time $t=t_\ast$ to coincide with a cylindrical volume $\mathcal{V}_\epsilon$ that is centered at a point $\bm{x}$ and whose symmetry axis is aligned with the outward unit normal vector $\bm{\hat{n}}(\bm{x},t_\ast)$ of the surface on which one is to inspect the traction vector at time $t_\ast$ at point $\bm{x}$. Note that the surface of inspection is not the surface of the material volume but any arbitrary surface passing through $\bm{x}$. The volume $\mathcal{V}_\epsilon$ is labeled with $\epsilon$ for both the cylinder height $H(\epsilon)=\epsilon^2H_0$ and the radius $R(\epsilon)=\epsilon R_0$ are assumed dependent on a dimensionless parameter $\epsilon$ with $H_0$ and $R_0$ some finite height and radius. At the time $t_\ast$, the surface $\partial\mathcal{V}(t)$, corresponds to the cylinder surface $\partial\mathcal{V}_\epsilon$, and is split into three touching domains $\mathcal{A}_{\epsilon,n}$, $\mathcal{A}_{\epsilon,-n}$, and $\mathcal{A}_{\epsilon,r}$ corresponding to the top, bottom, and shell of the cylinder, respectively. The top and bottom areas of the cylinder are $A_{\epsilon,n}=A_{\epsilon,-n}=\pi R(\epsilon)^2$ while the shell area is $A_{\epsilon,r}=2\pi R(\epsilon)H(\epsilon)$, and the cylinder volume is $V_\epsilon=A_{\epsilon,n} H(\epsilon)$. The cylinder, the point $\bm{x}$, and the surface outward unit normal $\bm{\hat{n}}$ are illustrated in {numref}`fig-stress-momentum-cylinder` below.
::::{figure} ./figs/fig-stress-momentum-cylinder.svg
:label: fig-stress-momentum-cylinder
:align: center
:width: 60%
A cylindrical volume around a point $\bm{x}$ oriented with respect to a unit normal of a surface passing through the point $\bm{x}$.
::::
With respect to the volume $\mathcal{V}_\epsilon$, the mean value form {numref}`eq-mean-value-newton` of Newton's second law at time $t_\ast$ then reads
:::{math}
:label: eq-mean-value-newton-cylinder
\bm{f}_\epsilon V_\epsilon=(\bm{t}_{\epsilon,n}+\bm{t}_{\epsilon,-n})A_{\epsilon,n}+\bm{t}_{\epsilon,r}A_{\epsilon,r}
:::
where the vectors $\bm{f}_\epsilon$, $\bm{t}_{\epsilon,n}$, $\bm{t}_{\epsilon,-n}$, and $\bm{t}_{\epsilon,r}$ belong to the closures of the convex hulls
:::{math}
\begin{aligned}
\bm{f}_\epsilon &\in\overline{\text{conv}\{(\rho(D\bm{v}/Dt)-\rho\bm{g})\big|_{(\bm{y},t_\ast)} \mid \bm{y}\in\mathcal{V}_\epsilon\}},\\
\bm{t}_{\epsilon,n}&\in\overline{\text{conv}\{\bm{t}(\bm{y},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast)) \mid \bm{y}\in\mathcal{A}_{\epsilon,n}\}},\\
\bm{t}_{\epsilon,-n}&\in\overline{\text{conv}\{\bm{t}(\bm{y},t_\ast,-\bm{\hat{n}}(\bm{x},t_\ast)) \mid \bm{y}\in\mathcal{A}_{\epsilon,-n}\}},\\
\bm{t}_{\epsilon,r}&\in\overline{\text{conv}\{\bm{t}(\bm{y},t_\ast,\bm{\hat{r}}(\bm{y})) \mid \bm{y}\in\mathcal{A}_{\epsilon,r}\}}.
\end{aligned}
:::
Note that the outward unit normal of the top cylinder surface equals $\bm{\hat{n}}(\bm{x},t_\ast)$ and the outward unit normal of the bottom cylinder surface equals $-\bm{\hat{n}}(\bm{x},t_\ast)$. Then the equation {numref}`eq-mean-value-newton-cylinder` is divided by the area $A_{\epsilon,n}$, resulting in
:::{math}
\bm{f}_\epsilon \frac{V_\epsilon}{A_{\epsilon,n}}=\bm{t}_{\epsilon,n}+\bm{t}_{\epsilon,-n}+\bm{t}_{\epsilon,r}\frac{A_{\epsilon,r}}{A_{\epsilon,n}}
:::
Finally, the limit $\epsilon\to 0$ is taken. At this limit, the domains $\mathcal{V}_\epsilon$, $\mathcal{A}_{\epsilon,n}$, $\mathcal{A}_{\epsilon,-n}$, and $\mathcal{A}_{\epsilon,r}$ all collapse to the single point $\bm{x}$, the ratios $V_\epsilon/A_{\epsilon,n}\to 0$ and $A_{\epsilon,r}/A_{\epsilon,n}\to 0$ vanish, $\bm{f}_\epsilon$ and $\bm{t}_{\epsilon,r}$ remain finite and bounded, and 
:::{math}
\begin{aligned}
\lim_{\epsilon\to 0}\bm{t}_{\epsilon,n}&=\bm{t}(\bm{x},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast)),\\
\lim_{\epsilon\to 0}\bm{t}_{\epsilon,-n}&=\bm{t}(\bm{x},t_\ast,-\bm{\hat{n}}(\bm{x},t_\ast)).
\end{aligned}
:::
At this limit, Newton's second law therefore provides the condition
:::{math}
\bm{t}(\bm{x},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast))=-\bm{t}(\bm{x},t_\ast,-\bm{\hat{n}}(\bm{x},t_\ast)).
:::
Further, as the choice of the time $t_\ast$ is arbitrary, one may substitute $t_\ast$ with $t$.

Mathematically the result implies that the traction vector is odd with respect to the dependency on the unit normal of the surface it acts on. Physically the result reflects Newton's third law. A surface has outward side ($\bm{\hat{n}}$) and an inward side ($-\bm{\hat{n}}$). For any action on the outward side, there is always a corresponding reaction on the inward side, and of exactly the same magnitude but into opposite direction, as Newton's third law says. 

In the second phase, to establish the linearity of traction on the unit normal, one requests the time-dependent material volume $\mathcal{V}(t)$ at time $t=t_\ast$ to coincide with a trirectangular tetrahedron $\mathcal{V}_\epsilon$ that is attached to the point $\bm{x}$ from one corner. Further, the outward unit normal of the tetrahedron face with the largest surface area is set to align with the unit normal $\bm{\hat{n}}(\bm{x},t_\ast)$ while the unit normals of the remaining three faces are aligned with the negatives of the unit vectors $\{\bm{\hat{e}}_1(\bm{x}),\bm{\hat{e}}_2(\bm{x}),\bm{\hat{e}}_3(\bm{x})\}$ that form an orthogonal right-handed basis at the point $\bm{x}$. The distances of the tetrahedron corners along the vectors $\bm{\hat{e}}_i(\bm{x})$ from the point $\bm{x}$ are denoted with $L_i(\epsilon)=\epsilon L_{i,0}$. The setting is illustrated in {numref}`fig-stress-momentum-tetrahedron` below.
::::{figure} ./figs/fig-stress-momentum-tetrahedron.svg
:label: fig-stress-momentum-tetrahedron
:align: center
:width: 85%
A tetrahedral volume with one corner attached to a point $\bm{x}$ and the opposing face oriented with respect to the surface outward unit normal $\bm{n}(\bm{x})$.
::::

The tetrahedron boundary $\partial \mathcal{V}_\epsilon$ is split to account for the faces $\{\mathcal{A}_{\epsilon,i}\}_{i=1}^3$ and $\mathcal{A}_{\epsilon,n}$ with areas $\{A_{\epsilon,i}\}_{i=1}^3$ and $A_{\epsilon,n}$ that relate via
:::{math}
A_{\epsilon,i}=\bm{\hat{e}}_i(\bm{x})\cdot\bm{\hat{n}}(\bm{x},t_\ast)A_{\epsilon,n}.
:::
The mean value form {numref}`eq-mean-value-newton` over the tetrahedron then reads
:::{math}
:label: eq-mean-value-newton-tetra
\begin{aligned}
\bm{f}_\epsilon V_\epsilon&=\bm{t}_{\epsilon,n}A_{\epsilon,n}+\sum_{i=1}^3\bm{t}_{\epsilon,i}A_{\epsilon,i},\\
&=A_{\epsilon,n}\left(\bm{t}_n+\sum_{i=1}^3 (\bm{\hat{e}}_i(\bm{x})\cdot\bm{\hat{n}}(\bm{x},t_\ast))\bm{t}_{\epsilon,i}\right)
\end{aligned}
:::
where the vectors $\bm{f}_\epsilon$, $\bm{t}_{\epsilon,n}$, and $\{\bm{t}_{\epsilon,i}\}_{i=1}^3$ belong to the closures of convex hulls
:::{math}
\begin{aligned}
\bm{f}_\epsilon &\in\overline{\text{conv}\{(\rho(D\bm{v}/Dt)-\rho\bm{g})\big|_{(\bm{y},t_\ast)} \mid \bm{y}\in\mathcal{V}_\epsilon\}},\\
\bm{t}_{\epsilon,n}&\in\overline{\text{conv}\{\bm{t}(\bm{y},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast)) \mid \bm{y}\in\mathcal{A}_{\epsilon,n}\}},\\
\bm{t}_{\epsilon,i}&\in\overline{\text{conv}\{\bm{t}(\bm{y},t_\ast,-\bm{\hat{e}}_i(\bm{x})) \mid \bm{y}\in\mathcal{A}_{\epsilon,i}\}}.
\end{aligned}
:::
Dividing {numref}`eq-mean-value-newton-tetra` by the surface area $A_{\epsilon,n}$, and taking the limit $\epsilon\to 0$, the ratio $V_\epsilon/A_{\epsilon,n}\to 0$ vanishes while the vectors appoach $\bm{t}_{\epsilon,n}\to \bm{t}(\bm{x},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast))$ and $\bm{t}_{\epsilon,i}\to \bm{t}(\bm{x},t_\ast,-\bm{\hat{e}}_i(\bm{x}))$. The mean value form of Newton's second law over the tetrahedron therefore leads to the condition
:::{math}
\begin{aligned}
\bm{t}(\bm{x},t_\ast,\bm{\hat{n}}(\bm{x},t_\ast))&=-\sum_{i=1}^3 (\bm{\hat{e}}_i(\bm{x})\cdot\bm{\hat{n}}(\bm{x},t_\ast))\bm{t}(\bm{x},t_\ast,-\bm{\hat{e}}_i(\bm{x}))\\
&=\sum_{i=1}^3 (\bm{\hat{e}}_i(\bm{x})\cdot\bm{\hat{n}}(\bm{x},t_\ast))\bm{t}(\bm{x},t_\ast,\bm{\hat{e}}_i(\bm{x}))\\
&=\left(\sum_{i=1}^3 \bm{t}(\bm{x},t_\ast,\bm{\hat{e}}_i(\bm{x}))\otimes\bm{\hat{e}}_i(\bm{x})\right)\cdot\bm{\hat{n}}(\bm{x},t_\ast)
\end{aligned}
:::
where the second form results from the oddness of traction established in the first phase and the third from using the calculus rules. It is therefore confirmed that the traction vector is a linear map of the surface unit normal vector and can be expressed as
:::{math}
\bm{t}(\bm{x},t,\bm{\hat{n}}(\bm{x},t))=\bm{\sigma}(\bm{x},t)\cdot\bm{\hat{n}}(\bm{x},t),
:::
where $\bm{\sigma}(\bm{x},t)$ is a tensor field of rank-2, referred to as stress.

(sec-symmetry-of-stress)=
## <span class="intermediate"></span> Conservation of angular momentum and symmetry of the stress tensor
For point masses, the definition $d\bm{x}(t)/dt=\bm{v}(t)$ for velocity together with Newton's second law $md\bm{v}(t)/dt=\bm{F}(\bm{x}(t),t)$ imply a vector-valued equation $d\bm{L}/dt=\bm{T}$ between the angular momentum vector $\bm{L}=(\bm{x}(t)-\bm{x}_0)\times m\bm{v}(t)$ and the torque vector $\bm{T}=(\bm{x}(t)-\bm{x}_0)\times\bm{F}(\bm{x}(t),t)$ with respect to any stationary point $\bm{x}_0$. This principle of angular momentum balance is required to hold also for continuous matter. In ordinary matter, only the torques from forces acting on a material volume may contribute to the time rate of change of angular momentum of the material volume. As shown next, this requirement imposes an additional restriction on the stress tensor: it must be symmetric.

The differential amount of angular momentum a differential volume $dV$ of fluid carries with respect to a stationary point $\bm{x}_0$ is $\delta\bm{L}=(\bm{x}-\bm{x}_0)\times \rho\bm{v}dV$. With $\delta\bm{F}_b=\rho\bm{g}dV$ the differential body force acting on a differential volume $dV$ and $\delta\bm{F}_s=\bm{\sigma}\cdot\bm{\hat{n}}dA$ the differential surface force acting on a differential surface area $dA$, the differential torques with respect to the point $\bm{x}_0$ resulting from body and surface forces are $\delta\bm{T}_b=(\bm{x}-\bm{x}_0)\times\delta\bm{F}_b=(\bm{x}-\bm{x}_0)\times\rho\bm{g}dV$ and $\delta\bm{T}_s=(\bm{x}-\bm{x}_0)\times\delta \bm{F}_s=(\bm{x}-\bm{x}_0)\times\bm{\sigma}\cdot\bm{\hat{n}}dA$, respectively. For the time rate of change of angular momentum of the fluid within a macroscopic material volume $V(t)$ to equal the total torque on the volume, the following condition must hold
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\delta\bm{L}}_{\substack{\text{Time rate of}\\\text{change of angular}\\\text{momentum in}\,V(t)}}=\underbrace{\int_{V(t)}\delta\bm{T}_b}_{\substack{\text{Torque on}\,V(t)\\\text{from body}\\\text{forces}}}+\underbrace{\int_{\partial V(t)}\delta\bm{T}_s}_{\substack{\text{Torque on}\,\partial V(t)\\\text{from surface}\\\text{forces}}}.
:::

Since $V(t)$ is a material volume and $\delta\bm{L}=(\bm{x}-\bm{x}_0)\times\rho\bm{v}dV$ includes the density $\rho$ as a multiplier, one may use the identity {numref}`eq-rho-identity` with $\bm{f}=(\bm{x}-\bm{x}_0)\times\bm{v}$ to write the time derivative of the total angular momentum of the material volume as
:::{math}
\begin{aligned}
\frac{d}{dt}\int_{V(t)}\delta\bm{L}&=\frac{d}{dt}\int_{V(t)}(\bm{x}-\bm{x}_0)\times \rho\bm{v}dV\\
&=\int_{V(t)}\rho\frac{D}{Dt}[(\bm{x}-\bm{x}_0)\times\bm{v}]dV.
\end{aligned}
:::
Since the material derivative is a scalar-valued differential operator, it acts component-wise on vectors and obeys the ordinary product rule. Since $D\bm{x}_0/Dt=\bm{0}$ and $D\bm{x}/Dt=\bm{v}$, one then finds
:::{math}
\rho\frac{D}{Dt}[(\bm{x}-\bm{x}_0)\times\bm{v}]=(\bm{x}-\bm{x}_0)\times\rho\frac{D\bm{v}}{Dt}.
:::
Using now the version of Cauchy's momentum equation {numref}`eq-cauchy-without-symmetry` that does not assume a symmetric $\bm{\sigma}$, the time derivative of the angular momentum becomes
:::{math}
\frac{d}{dt}\int_{V(t)}\delta\bm{L}=\int_{V(t)}(\bm{x}-\bm{x}_0)\times\left(\rho\bm{g}+\nabla\cdot\bm{\sigma}^\mathsf{T}\right)dV
:::

Using the divergence theorem {numref}`eq-divergence-theorem`, the total torque on the material volume can be written as the following volume integral
:::{math}
\begin{aligned}
\int_{V(t)}\delta\bm{T}_b+\int_{\partial V(t)}\delta\bm{T}_s&=\int_{V(t)}(\bm{x}-\bm{x}_0)\times\rho\bm{g}dV+\int_{\partial V(t)}(\bm{x}-\bm{x}_0)\times\bm{\sigma}\cdot\bm{\hat{n}}dA\\
&=\int_{V(t)}((\bm{x}-\bm{x}_0)\times\rho\bm{g}+\nabla\cdot((\bm{x}-\bm{x}_0)\times\bm{\sigma})^\mathsf{T})dV\\
&=\int_{V(t)}((\bm{x}-\bm{x}_0)\times(\rho\bm{g}+\nabla\cdot\bm{\sigma}^\mathsf{T})-\bm{\varepsilon}:\bm{\sigma})dV.
\end{aligned}
:::
In the last step, the vector calculus identity {numref}`eq-div-a-times-sigma` was used as in the {numref}`example-eq-div-a-times-sigma`. If the time rate of change of angular momentum of every material volume is to equal the total torque acting on it, the stress tensor must satisfy $\bm{\varepsilon}:\bm{\sigma}=\bm{0}$ point-wise. This holds if and only if the stress tensor is symmetric
:::{math}
\bm{\sigma}^T=\bm{\sigma}.
:::
If the stress tensor were not symmetric, spurious effects could emerge, as illustrated in the example below.

::::{proof:example}
Consider a material volume $V(t)$, which at time instant $t_\ast$ coincides with a cube of side length $L$ centered at the origin. For simplicity, assume no body forces exist. Suppose that the stress tensor is spatially uniform, non-symmetric, and given by
:::{math}
\bm{\sigma}=\sigma\bm{\hat{x}}\otimes\bm{\hat{y}},
:::
where $\sigma$ is a constant with units of pressure. The traction acting on a surface with a unit normal $\bm{\hat{n}}$ is then $\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}=\sigma(\bm{\hat{y}}\cdot\bm{\hat{n}})\bm{\hat{x}}$. Consequently, only the faces of the cube with surface normals parallel to the $y$-axis contribute to the contact force and torque. The forces on the faces at $y=L/2$ and $y=-L/2$ with unit normals $\bm{\hat{n}}|_{y=L/2}=\bm{\hat{y}}$ and $\bm{\hat{n}}|_{y=-L/2}=-\bm{\hat{y}}$, respectively, are now straightforward to compute:
:::{math}
\begin{aligned}
\bm{F}|_{y=L/2}&=\int_{\substack{y=L/2,\\ -L/2\leq x,z\leq L/2}}\bm{\sigma}\cdot\bm{\hat{y}}dA\\
&=\int_{-L/2}^{L/2}\int_{-L/2}^{L/2}\sigma\bm{\hat{x}}dxdz\\
&=\sigma L^2\bm{\hat{x}},\\
\bm{F}|_{y=-L/2}&=\int_{\substack{y=-L/2,\\ -L/2\leq x,z\leq L/2}}\bm{\sigma}\cdot(-\bm{\hat{y}})dA\\
&=\int_{-L/2}^{L/2}\int_{-L/2}^{L/2}(-\sigma\bm{\hat{x}})dxdz\\
&=-\sigma L^2\bm{\hat{x}}.
\end{aligned}
:::
They are equal in magnitude and opposite in direction, resulting in zero net force on the cube. However, the forces act at different positions relative to the centre of the cube, inducing torque with respect to the origin $\bm{x}_0=\bm{0}$. The torques on the faces at $y=L/2$ and $y=-L/2$ are
:::{math}
\begin{aligned}
\bm{T}|_{y=L/2}&=\int_{\substack{y=L/2,\\ -L/2\leq x,z\leq L/2}}\bm{x}\times\bm{\sigma}\cdot\bm{\hat{y}}dA\\
&=\int_{-L/2}^{L/2}\int_{-L/2}^{L/2}\sigma\left(z\bm{\hat{y}}-\frac{L}{2}\bm{\hat{z}}\right)dxdz\\
&=-\frac{\sigma L^3}{2}\bm{\hat{z}}\\
\bm{T}|_{y=-L/2}&=\int_{\substack{y=-L/2,\\ -L/2\leq x,z\leq L/2}}\bm{x}\times\bm{\sigma}\cdot(-\bm{\hat{y}})dA\\
&=\int_{-L/2}^{L/2}\int_{-L/2}^{L/2}(-\sigma)\left(z\bm{\hat{y}}+\frac{L}{2}\bm{\hat{z}}\right)dxdz\\
&=-\frac{\sigma L^3}{2}\bm{\hat{z}}
\end{aligned}
:::
Although the net contact force was zero, the net torque from the forces does not vanish but is instead
:::{math}
\bm{T}=-\sigma L^3\bm{\hat{z}}
:::

This is incompatible with the balance of angular momentum. In the absence of body forces, since the divergence of the constant stress tensor vanishes, the time rate of change of the total angular momentum of the cube with respect to the origin at time $t_\ast$ vanishes
:::{math}
\frac{d\bm{L}}{dt}\big|_{t=t_\ast}=\int_{V(t_\ast)}\bm{x}\times(\underbrace{\nabla\cdot\bm{\sigma}^\mathsf{T}}_{=\bm{0}})\big|_{t=t_\ast}dV=\bm{0}.
:::
For comparison, a symmetric stress tensor
:::{math}
\bm\sigma=\sigma\left(\hat{\bm x}\otimes\hat{\bm y}+\hat{\bm y}\otimes\hat{\bm x}\right).
:::
would introduce additional forces and torques on the faces with normals aligned the $x$-axis that would exactly cancel the torque from the faces normal to the $y$-axis. 

This illustrates that stress symmetry does not imply the absence of shear stresses. Rather, it requires the complementary shear components to be equal, ensuring that the torques associated with the corresponding shear forces balance.
::::


## <span class="elementary"></span> Conservation of energy
Two physics principles, namely the conservation of mass and momentum, have been used so far, resulting in partial differential equations that describe the evolution of fluid's density and velocity. The fluid's thermodynamic state, however, cannot be described by density alone. A second independent thermodynamic property, such as temperature or pressure, is also needed. The final physics principle left to investigate is the energy balance. It turns out that no direct equation for temperature or pressure is found but an equation is obtained for the fluid's specific internal energy instead.

A differential volume $dV$ of fluid contains a differential amount $\tfrac{1}{2}\rho|\bm{v}|^2dV$ of kinetic energy. Using the material derivative identity {numref}`eq-rho-identity` with $\bm{f}=\tfrac{1}{2}|\bm{v}|^2$, the rate of change of fluid's kinetic energy in a material volume $V(t)$ then becomes
:::{math}
\frac{d}{dt}\int_{V(t)}\frac{1}{2}\rho|\bm{v}|^2dV=\int_{V(t)}\rho\frac{D}{Dt}\frac{1}{2}|\bm{v}|^2dV=\int_{V(t)}\rho\bm{v}\cdot\frac{D\bm{v}}{Dt}dV.
:::
Substituting the Cauchy momentum equation {numref}`eq-cauchy` for the material derivative of the velocity field, one may further write
:::{math}
:label: eq-local-rate-of-change-of-kinetic-energy
\begin{aligned}
\rho\frac{1}{2}\frac{D|\bm{v}|^2}{Dt}=\rho \bm{v}\cdot\frac{D\bm{v}}{Dt}&=\bm{v}\cdot\rho\bm{g}+\bm{v}\cdot\nabla\cdot\bm{\sigma}\\
&=\bm{v}\cdot\rho\bm{g}+\nabla\cdot(\bm{\sigma}\cdot\bm{v})-\bm{\sigma}:\nabla\bm{v},
\end{aligned}
:::
where the last step follows from the vector identity {numref}`eq-divergence-rules`. Then using the divergence theorem {numref}`eq-divergence-theorem` to convert the volume integral of $\nabla\cdot(\bm{\sigma}\cdot\bm{v})$ into a surface integral, one identifies the driving mechanisms for the rate of change of fluid's kinetic energy
:::{math}
:label: eq-material-rate-of-change-of-kinetic-energy
\begin{aligned}
\underbrace{\frac{d}{dt}\int_{V(t)}\frac{1}{2}\rho|\bm{v}|^2dV}_{\substack{\text{Rate of change}\\\text{of kinetic energy}}}&=\int_{V(t)}\bm{v}\cdot\rho\bm{g}dV+\int_{\partial V(t)}\bm{v}\cdot\bm{\sigma}\cdot\bm{\hat{n}}dA-\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV\\
&=\underbrace{\int_{V(t)}\bm{v}\cdot\delta\bm{F}_b}_{\substack{\text{Rate of mechanical}\\\text{work performed}\\\text{by body forces}}}+\underbrace{\int_{\partial V(t)}\bm{v}\cdot\delta\bm{F}_s}_{\substack{\text{Rate of mechanical}\\\text{work performed}\\\text{by surface forces}}}-\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}},
\end{aligned}
:::
The rate of change of the fluid's kinetic energy therefore does not equal simply the rate of work done by the body and surface forces. Instead, it includes also an additional volumetric term $\bm{\sigma}:\nabla\bm{v}$. In the advanced {numref}`sec-differential-elements-evolution`, the velocity gradient tensor $\nabla\bm{v}$ was observed to encode different types of fluid motion, namely rotation, isotropic deformation, and shearing deformation, represented by the antisymmetric and symmetric parts of the tensor $\nabla\bm{v}$, respectively. Since the stress tensor $\bm{\sigma}$ is symmetric, only the symmetric part of $\nabla\bm{v}$ contributes to the term $\bm{\sigma}:\nabla\bm{v}$, which therefore represents the rate of mechanical energy change from local deformation of the fluid against the stress.

Since the body force $\delta\bm{F}_b=\rho\bm{g}dV$ is assumed to originate from gravity alone, and the gravitational acceleration $\bm{g}=-\nabla G$ can be written as the negative gradient of a gravitational potential function $G(\bm{x})$ that represents gravitational energy per unit mass, it is possible to express the work rate from the gravitational body force as a time derivative of the fluid's gravitational potential energy. To see this, note that a differential volume $dV$ of the fluid contains a differential amount $\rho G dV$ of gravitational potential energy. Using the material derivative identity {numref}`eq-rho-identity` with $\bm{f}=G$, the time rate of change of the gravitational potential energy of the fluid in a material volume $V(t)$ then becomes
:::{math}
:label: eq-material-rate-of-change-of-potential-energy
\underbrace{\frac{d}{dt}\int_{V(t)}\rho G dV}_{\substack{\text{Time rate of change}\\\text{of gravitational}\\\text{potential energy}}}=\int_{V(t)}\rho\frac{DG}{Dt}dV=-\int_{V(t)}\bm{v}\cdot\rho\bm{g}dV=-\underbrace{\int_{V(t)}\bm{v}\cdot\delta\bm{F}_b}_{\substack{\text{Rate of mechanical}\\\text{work performed}\\\text{by gravitational}\\\text{body force}}},
:::
where $DG/Dt=\bm{v}\cdot\nabla G=-\bm{v}\cdot\bm{g}$ was used. The result illustrates that the effect of gravity can be interpreted equivalently either through the action of gravitational force or the change in the gravitational potential energy, just like in the mechanics of point masses. Combining this result with the time rate of change of kinetic energy, the time rate of change of the sum of kinetic and potential energy in a material volume of fluid becomes
:::{math}
:label: eq-material-rate-of-change-of-kinetic-and-potential-energy
\underbrace{\frac{d}{dt}\int_{V(t)}\rho\left(\frac{1}{2}|\bm{v}|^2+G\right)dV}_{\substack{\text{Time rate of change of}\\\text{kinetic and potential energy}}}=\underbrace{\int_{\partial V(t)}\bm{v}\cdot\delta\bm{F}_s}_{\substack{\text{Rate of mechanical}\\\text{work performed}\\\text{by surface forces}}}-\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}},
:::
In contrast to a point mass acted on only by gravity, the sum of kinetic and gravitational potential energy of a material volume of fluid is not generally constant. Surface forces and local deformations thoughout the entire fluid volume can transfer mechanical energy across the boundary and within the fluid.

The component of energy that has not been considered yet involves the microscopic structure of the fluid. Because of the microscopic structure, the fluid has internal energy $u(\bm{x},t)$ per unit mass, representing the microscopic rest-frame kinetic and potential energy of the particles of which the fluid consists of and of the bonds between the particles. The total energy the fluid contains is therefore the sum of the microscopic internal energy, the macroscopic kinetic energy, and the macroscopic gravitational potential energy. In {numref}`sec-boundary-heat-work`, the types of energy transferred through the boundary of a material volume were classified either as mechanical work or heat. The time rate of change of energy within a material volume should therefore equal the mechanical work rate of the forces acting on it supplemented with the rate of heat flowing into and getting absorbed within the volume. 

Heat transfer through a surface can generally be denoted with a heat flux vector $\bm{q}(\bm{x},t)$ that describes the direction of heat transfer and the rate of it per unit area. Local heat absorption or emission within the volume can be denoted with $q_V(\bm{x},t)$ denoting the rate per unit volume. Since the mechanical work rate from the gravitational body force exactly corresponds to the time rate of change of gravitational potential energy, the effect of gravity should be included into the total energy balance either as a potential energy term or as a mechanical work rate term but not as both, to avoid double counting. This is analogous with the energy balance of point masses where one may either write the time derivative of the sum of kinetic and potential energy to equal zero, or write the time derivative of the kinetic energy to equal the work rate from gravitational force. Accounting for gravity through the potential energy term, the mechanical work rate left in the energy balance results from the surface forces alone. Considering that a differential volume $dV$ contains a differential amount $\rho u dV$ of internal energy, the energy balance for a material volume $V(t)$ then reads
:::{math}
:label: eq-total-energy-balance-material-volume
\begin{aligned}
&\underbrace{\frac{d}{dt}\int_{V(t)}\rho\left(u+\frac{1}{2}|\bm{v}|^2+G\right)dV}_{\substack{\text{Time rate of change of internal,}\\\text{kinetic, and gravitational energy}}}\\
&=\underbrace{\int_{\partial V(t)}(-\bm{q})\cdot\bm{\hat{n}}dA}_{\substack{\text{Net rate of heat received}\\\text{through the boundary}}}+\underbrace{\int_{V(t)}q_VdV}_{\substack{\text{Net rate of heat}\\\text{absorbed}\\\text{volumetrically}}} +\underbrace{\int_{\partial V(t)}\bm{v}\cdot\delta\bm{F}_s}_{\substack{\text{Rate of mechanical}\\\text{work performed}\\\text{by surface forces}}}.
\end{aligned}
:::
The negative sign multiplying the heat flux $\bm{q}$ in the surface integral term accounts for the surface normal $\bm{\hat{n}}$ pointing outwards from the material volume $V(t)$. Heat flowing in per unit area is given by $-\bm{q}\cdot\bm{\hat{n}}$. Subtracting the time rate of change of kinetic and gravitational potential energy {numref}`eq-material-rate-of-change-of-kinetic-and-potential-energy` from the time rate of change of total energy {numref}`eq-total-energy-balance-material-volume`, the time rate of change of internal energy for the material volume becomes 
:::{math}
:label: eq-energy-balance-material-volume
\underbrace{\frac{d}{dt}\int_{V(t)}\rho udV}_{\substack{\text{Time rate of change}\\\text{of internal energy}}}=\underbrace{\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA}_{\substack{\text{Net rate of heat received}\\\text{through the boundary}}}+\underbrace{\int_{V(t)}q_VdV}_{\substack{\text{Net rate of heat}\\\text{absorbed}\\\text{volumetrically}}}+\underbrace{\int_{V(t)}\bm{\sigma}:\nabla\bm{v}dV}_{\substack{\text{Rate of mechanical}\\\text{energy change from}\\\text{local deformation}}},
:::
and consists of heat rate and the mechanical energy change from local deformation. Using the material derivative identity {numref}`eq-rho-identity` with $\bm{f}=u$ for the time derivative on the left
:::{math}
\frac{d}{dt}\int_{V(t)}\rho udV=\int_{V(t)}\rho\frac{Du}{Dt}dV,
:::
the divergence theorem {numref}`eq-divergence-theorem` for the heat flux term on the right
:::{math}
\int_{\partial V(t)}\bm{q}\cdot(-\bm{\hat{n}})dA=\int_{V(t)}(-\nabla\cdot\bm{q})dV,
:::
and requiring the energy balance {numref}`eq-energy-balance-material-volume` to hold for every material volume $V(t)$, one finds the local partial differential equation for the specific internal energy
:::{math}
:label: eq-internal-energy-equation
\rho\frac{Du}{Dt}=-\nabla\cdot\bm{q}+q_V+\bm{\sigma}:\nabla\bm{v}.
:::
This equation is often referred to as the fluid internal energy equation.

::::{proof:example}
The local kinetic-energy equation {numref}`eq-local-rate-of-change-of-kinetic-energy` shows that the rate of change of the fluid's specific kinetic energy along its motion originates from mechanical work performed by body and surface forces,
:::{math}
:enumerated: false
\rho\frac{D}{Dt}\frac{1}{2}|\bm{v}|^2=\bm{v}\cdot(\rho\bm{g}+\nabla\cdot\bm{\sigma}).
:::
In a fluid at rest, $\bm{v}=0$ and hence $D/Dt=\partial_t$ and $\nabla\bm{v}=0$. In such case, the kinetic energy therefore cannot change, while the equation for internal energy reduces to
:::{math}
:enumerated: false
\rho\partial_t u=-\nabla\cdot\bm{q}+q_V.
:::
Changes in internal energy can thus occur through heat transfer even when the fluid has no macroscopic motion. The coupling between macroscopic mechanical and microscopic internal energy occurs through the term $\bm{\sigma}:\nabla\bm{v}$ representing the mechanical energy change rate from deformation of the fluid. The term appears both in the local equation {numref}`eq-local-rate-of-change-of-kinetic-energy` for kinetic energy and {numref}`eq-internal-energy-equation` for the specific internal energy but with opposing signs. It therefore locally converts macroscopic kinetic energy into internal energy and back, depending on sign.
::::

::::{proof:example}
Consider a fluid undergoing free fall in a uniform gravitational field $\bm g=-g\bm{\hat z}$. Suppose that its velocity is spatially uniform, $\bm v(\bm x,t)=v(t)\bm{\hat z}$, with $dv/dt=-g$ constant, and that its stress tensor is spatially uniform. Also assume that there is no heat transfer or volumetric heating, $\bm q=\bm 0$ and $q_V=0$. Then
:::{math}
\nabla\bm v=\bm 0,\qquad
\nabla\cdot\bm\sigma=\bm 0.
:::
The momentum equation is therefore satisfied, while the internal energy equation reduces to
:::{math}
\frac{Du}{Dt}=0.
:::
Consequently, the specific internal energy in each material point moving with the fluid remains constant, even though its kinetic energy changes. In fact, with the gravitational potential being $G=gz$, the kinetic and gravitational potential energies satisfy
:::{math}
\frac{D}{Dt}\left(\frac{1}{2}|\bm v|^2+G\right)
=v\frac{dv}{dt}+gv=0.
:::
The material rates of change of kinetic and gravitational potential energy are therefore equal in magnitude and opposite in sign, without any change in internal energy. In the absence of local deformation, a fluid can undergo macroscopic acceleration without any mechanical energy transfer to its internal energy.
::::

## <span class="elementary"></span> Constitutive relation for stress
The conservation principles of mass, momentum, and energy discussed so far have led to local partial differential equations from which the local time rates of change of fluid density, velocity, and specific internal energy can be computed. To evaluate these expressions, additional relations are nevertheless needed to describe how stress $\bm{\sigma}$ and heat flux $\bm{q}$ depend on the local state and motion of the fluid. Such relations are called constitutive. Their form is restricted by physical principles such as invariance with respect to the choice of reference frame and the principle of isotropy in a fluid at rest, while the remaining constitutive behavior is typically determined experimentally.

For non-relativistic mechanics obeying Newton's laws, the principle of Galilean invariance requires the laws of motion to be invariant in all inertial frames. Consider two inertial observers whose reference frames move with constant relative velocity $\bm{v}_0$. If the position and velocity fields measured by the second observer are denoted with primes, the corresponding coordinates and velocity are related by
:::{math}
\bm{x}'=\bm{x}-\bm{v}_0t,\qquad
\bm{v}'=\bm{v}-\bm{v}_0.
:::
The material derivative is unchanged by this transformation,
:::{math}
\begin{aligned}
\frac{D'}{Dt'}
&=\frac{\partial}{\partial t'}+\bm{v}'\cdot\nabla'\\
&=\frac{\partial}{\partial t}+\bm{v}_0\cdot\nabla
+(\bm{v}-\bm{v}_0)\cdot\nabla\\
&=\frac{D}{Dt},
\end{aligned}
:::
so the material acceleration is the same in both frames. Consequently, Newton's laws require the physical forces acting on a given material volume to be the same in both frames. In particular, the contact force acting on a given surface, and hence the traction $\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}$, must remain unchanged. Since a uniform translation does not change the surface normal or area, the stress tensor itself must also remain unchanged. This requirement forces the stress to be independent of the absolute velocity $\bm{v}$, but not of the spatial variations of the velocity field that are represented by the velocity gradient tensor $\nabla\bm{v}$.

Another physical restriction follows from the isotropy of a fluid at rest. Since no spatial direction is distinguished in an undeforming fluid, the stress tensor must be isotropic and can therefore be represented as
:::{math}
\bm{\sigma}=-p\bm{I},
:::
where $p$ is the thermodynamic pressure. The minus sign accounts for the outward unit normal of the surface on which the traction must counter the compressive pressure in an undeforming fluid.

For a simple fluid, whose stress is assumed to be determined locally by the thermodynamic state variables $(\rho,T,p)$ and the local information of the velocity field, the constitutive dependence may consequently be written as
:::{math}
\bm{\sigma} = \bm{\sigma}(\rho, p, T, \nabla\bm{v}).
:::
In principle, the stress could depend also on higher derivatives of the velocity field and on the spatial derivatives of the thermodynamic state variables, but experimental observations of simple fluids can be explained to good accuracy with stress assumed to depend on the thermodynamic state and the velocity gradient only. Essentially, this representation is a modeling choice, not a physical law.

In the advanced {numref}`sec-differential-elements-evolution`, a detailed analysis of how points and differential elements such as line, surface, and volume elements evolve along the flow of the velocity field $\bm{v}$ was given. It was concluded that the velocity gradient tensor encoding fluid motion could be described in three parts
:::{math}
:label: eq-velocity-gradient-decomposition
\nabla\bm{v}=\bm{D}+\frac{1}{3}(\nabla\cdot\bm{v})\bm{I}+\bm{\Omega},
:::
where the symmetric and traceless rank-2 tensor $\bm{D}$ and the antisymmetric rank-2 tensor $\bm{\Omega}$ are
:::{math}
\begin{aligned}
\bm{D}&=\frac{1}{2}\left(\nabla\bm{v}+(\nabla\bm{v})^\mathsf{T}\right)-\frac{1}{3}(\nabla\cdot\bm{v})\bm{I},\\
\bm{\Omega}&=\frac{1}{2}\left(\nabla\bm{v}-(\nabla\bm{v})^\mathsf{T}\right).
\end{aligned}
:::
By tracking the evolution of points that define lines, surfaces, and volumes, the {numref}`example-velocity-gradient-decomposition` then illustrated how each of the parts of $\nabla\bm{v}$ corresponds to a different type of motion. The term $\tfrac{1}{3}(\nabla\cdot\bm{v})\bm{I}$ encodes the rate of isotropic volumetric expansion or shrinking, the term $\bm{D}$ the rate of non-isotropic, volume-preserving deformation, including shearing, and the term $\bm{\Omega}$ the rate of volume- and area-preserving rotation.

Of the decomposition for $\nabla\bm{v}$ only the deformation rates $\bm{D}$ and $\nabla\cdot\bm{v}$ can contribute to stress. To understand why the rotational part $\bm{\Omega}$ cannot, consider a fluid confined in a cylindrical annulus. Rotate both the inner and outer walls of the annulus with the same and constant angular velocity in the same direction as in {numref}`fig-cylinder-flow-rotation`. The fluid within is observed to rotate with exactly the same angular velocity at every point. In other words, the fluid undergoes rigid-body rotation, for which $\bm{D}=\bm{0}$ and $\nabla\cdot\bm{v}=0$ while only the antisymmetric part $\bm{\Omega}$ is non-zero. 
:::{figure} ./figs/fig-rotation.svg
:label: fig-cylinder-flow-rotation
:align: center
:width: 100%
Fluid flow in a cylindrical annulus with walls co-rotating with the same angular velocity. The fluid undergoes rigid-body rotation characterized by $\bm{\Omega}$, without tangential traction or torque at the walls being required to maintain the motion.
:::
If one observes the fluid from a frame rotating with the same angular velocity, the fluid appears at rest. Although this is a non-inertial frame, the centrifugal force acting on the fluid can be balanced by a radial pressure gradient, in the same way that gravity normally induces a hydrostatic pressure difference in a column of still fluid. The stress therefore remains isotropic, and the traction on the cylindrical wall is purely normal. No tangential traction, and hence no torque about the cylinder axis, is required to maintain the steady rigid-body rotation. This illustrates the principle of material frame indifference: the physical stress response cannot depend on the rigid-body rotation of the observer. Consequently, the dependency of stress on the velocity gradient can appear only through $\bm{D}$ and $\nabla\cdot\bm{v}$, and the stress can therefore be decomposed as
:::{math}
:label: eq-stress
\bm{\sigma} = -p\bm{I} + \bm{\tau}(\rho, p, T, \bm{D}, \nabla\cdot\bm{v}),
:::
where $\bm{\tau}$ represents the contribution associated with deformation and must vanish when both $\bm{D}$ and $\nabla\cdot\bm{v}$ are zero.

Further details are revealed if only the outer wall of the cylindrical annulus is spun as in {numref}`fig-cylinder-flow-shear`, or both walls are spun but in opposite directions. In such a case, shear is observed to develop in the flow, and a constant torque at the annulus walls proportional to the shearing rate is required to maintain the flow. This indicates that, for sufficiently small deformation rates, the additional stress contribution depends approximately linearly on $\bm{D}$. 
:::{figure} ./figs/fig-shear.svg
:label: fig-cylinder-flow-shear
:align: center
:width: 100%
Fluid flow in a cylindrical annulus with fixed inner and rotating outer cylindrical walls. A constant torque is required on the walls to maintain the flow, proportional to the shear rate characterized by the tensor $\bm{D}$.
:::
Similarly, studying the travel of sound waves in a pipe as illustrated in {numref}`fig-pipe-wave`, measurements of the wave amplitude attenuation over distance provide information about the stress response to volumetric deformation. In this case as well, the force is deduced to have a linear dependency on the volumetric deformation rate characterized by $\nabla\cdot\bm{v}$.
:::{figure} ./figs/fig-wave.svg
:label: fig-pipe-wave
:align: center
:width: 100%
A traveling wave in a fluid. The flow is characterized by $\nabla\cdot\bm{v}$, related to the volumetric deformation. The deformation attenuates in a long pipe, decreasing the wave amplitude.
:::
Together, experiments and measurements therefore indicate the following expression for the deformation-related contribution to the stress tensor
:::{math}
:label: eq-viscous-stress
\bm{\tau} = 2\mu \bm{D} + \zeta(\nabla \cdot \bm{v})\bm{I}.
:::
The expression is symmetric and therefore compatible with the requirement of angular momentum conservation discussed in the intermediate {numref}`sec-symmetry-of-stress`. Generally, $\bm{\tau}$ is called the viscous stress, and fluids obeying this linear relationship are classified as Newtonian fluids, with the viscous proportionality coefficients $\mu$ and $\zeta$ being properties of the fluid and generally functions of the thermodynamic state $(\rho, p, T)$. In contrast, non-Newtonian fluids exhibit a more complex, non-linear dependency on the rates of deformation.

::::{proof:example}
Consider a Newtonian fluid undergoing simple shear flow between two parallel plates separated by a distance $H$. The lower plate is stationary, while the upper plate moves with constant velocity $U\bm{\hat{x}}$. Neglecting edge effects, the velocity field is
:::{math}
:enumerated: false
\bm{v}=\dot{\gamma}y\bm{\hat{x}}, \qquad \dot{\gamma}=\frac{U}{H},
:::
where $\dot{\gamma}$ is the constant shear rate. The velocity gradient tensor is
:::{math}
:enumerated: false
\nabla\bm{v}=\dot{\gamma}\bm{\hat{y}}\otimes\bm{\hat{x}},
:::
and its decomposition into symmetric and antisymmetric parts gives
:::{math}
:enumerated: false
\begin{aligned}
\bm{D}&=\frac{\dot{\gamma}}{2}\left(\bm{\hat{x}}\otimes\bm{\hat{y}}+\bm{\hat{y}}\otimes\bm{\hat{x}}\right),\\
\bm{\Omega}&=\frac{\dot{\gamma}}{2}\left(\bm{\hat{y}}\otimes\bm{\hat{x}}-\bm{\hat{x}}\otimes\bm{\hat{y}}\right).
\end{aligned}
:::
Since $\nabla\cdot\bm{v}=0$, the Newtonian constitutive relation becomes
:::{math}
:enumerated: false
\bm{\sigma}=-p\bm{I}+\mu\dot{\gamma}\left(\bm{\hat{x}}\otimes\bm{\hat{y}}+\bm{\hat{y}}\otimes\bm{\hat{x}}\right).
:::
For example, the traction acting on a surface with unit normal $\bm{\hat{y}}$ is
:::{math}
:enumerated: false
\bm{t}=\bm{\sigma}\cdot\bm{\hat{y}}=-p\bm{\hat{y}}+\mu\dot{\gamma}\bm{\hat{x}}.
:::
The shear stress is therefore proportional to the shear rate, with
proportionality coefficient $\mu$. The complementary shear component
has the same magnitude, as required by the symmetry of the stress
tensor.

Finally, the stress power per unit volume is
:::{math}
:enumerated: false
\bm{\sigma}:\nabla\bm{v}=\mu\dot{\gamma}^{2}.
:::
It is positive and contributes to an increase in internal energy. In the absence of heat transfer and volumetric heating, the internal
energy equation consequently reduces to 
:::{math}
:enumerated: false
\rho\frac{Du}{Dt}=\mu\dot{\gamma}^{2}.
:::
Thus, mechanical energy supplied to maintain the shearing motion is converted into internal energy within the fluid.
::::


## <span class="elementary"></span> Constitutive relation for heat flux
Recall from {numref}`sec-boundary-heat-work` that heat is energy transferred through microscopic interactions between particles, and distinct from energy transferred through macroscopic mechanical work. In a fluid, the heat flux $\bm{q}$ describes the direction and rate per unit area of this energy transfer, measured in the frame moving with the fluid. It therefore describes heat transfer independently of the energy transported along with the macroscopic motion of the fluid.

To investigate how the heat flux depends on the thermodynamic state of the fluid, consider a fluid confined between two parallel surfaces maintained at different temperatures. Arrange the experiment so that the fluid remains at rest despite the temperature difference. For example, the surfaces may be horizontal, with the warmer surface above the colder one, so that the resulting density stratification is stable against buoyancy-driven motion. Even though the fluid remains stationary, heat is observed to flow from the warmer surface toward the colder one, as in {numref}`fig-heat-flux` below.

:::{figure} ./figs/fig-heat-flux.svg
:label: fig-heat-flux
:align: center
:width: 60%
Heat flows from higher to lower temperatures, with the local direction and rate per unit area indicated by the heat flux vector $\bm{q}$.
:::


By varying the temperatures of the surfaces and their separation, experiments further show that, for sufficiently small temperature differences, the magnitude of the heat flux is approximately proportional to the temperature difference divided by the separation distance, while the proportionality coefficient depends on the average fluid thermodynamics state between the plates surfaces. When interpreted locally, the ratio of temperature difference to the distance between the surfaces becomes the temperature gradient in the direction normal to the surfaces. Since an isotropic fluid has no preferred spatial direction, the proportionality relationship applies irrespective of the orientation of the temperature gradient. The resulting constitutive relation is therefore
:::{math}
:label: eq-fourier-law
\bm{q}=-\lambda\nabla T,
:::
where $\lambda$ is the thermal conductivity of the fluid and generally depends on its thermodynamic state. The thermal conductivity is positive for ordinary fluids, and the negative sign indicates that heat is transported from high temperature toward low temperature. This experimental constitutive relation is known as Fourier's law of heat conduction.

::::{proof:example}
Consider a stationary fluid layer between two parallel plates separated by a distance $H$. The lower plate is maintained at temperature $T_\text{low}$, while the upper plate is maintained at a higher temperature $T_\text{high}$. Assume that the arrangement is such that the resulting density stratification is stable and no macroscopic fluid motion occurs. After a while, also the thermodynamic properties of the settle and no longer change over time. 

Let the $y$-axis point vertically upwards, with the lower and upper plates located at $y=0$ and $y=H$, respectively. Also assume that there is no volumetric heating, $q_V=0$, and that the thermal conductivity $\lambda$ is constant. Since the fluid and its properties are stationary in time, the internal energy equation {numref}`eq-internal-energy-equation` reduces to
:::{math}
:enumerated: false
0=-\nabla\cdot\bm{q}.
:::
Combining this result with Fourier's law {numref}`eq-fourier-law` gives
:::{math}
:enumerated: false
\nabla\cdot(\nabla T)=0.
:::
Since the temperature varies only in the $y$-direction, the solution
satisfying the prescribed temperatures at the plates is
:::{math}
:enumerated: false
T(y)=T_\text{low}+\frac{T_\text{high}-T_\text{low}}{H}y, \quad y\in[0,H].
:::
The resulting heat flux is therefore
:::{math}
:enumerated: false
\bm{q}
=-\lambda\nabla T
=-\lambda\frac{T_\text{high}-T_\text{low}}{H}\bm{\hat{y}}.
:::
The heat flux is constant throughout the fluid layer and directed downwards, from the warmer upper plate toward the colder lower plate. The magnitude of the heat transfer rate through the upper plate of area $A$ into the fluid is consequently
:::{math}
:enumerated: false
\dot{Q}\big|_{y=H}=\lambda A\frac{T_\text{high}-T_\text{low}}{H}.
:::
Thus, the heat transfer rate increases with the thermal conductivity, the plate area, and the temperature difference, while decreasing with the distance between the plates.
::::

## Summary
The motion of a fluid can be described by following individual material points along the flow and studying how differential line, surface, and volume elements evolve. The velocity gradient tensor $\nabla\bm{v}$ describes the local evolution of these differential elements and can be decomposed into isotropic deformation, volume-preserving deformation, and rotation. The Leibniz integral differentiation rule then provides the connection between the local evolution of the fluid and conservation laws applied over finite material volumes.

Conservation of mass, momentum, and energy leads to the local equations
:::{math}
:label:eq-fluid-equations
\begin{aligned}
\frac{1}{\rho}\frac{D\rho}{Dt}&= -\nabla\cdot\bm{v},\\
\rho\frac{D\bm{v}}{Dt}&= \rho\bm{g}+\nabla\cdot\bm{\sigma},\\
\rho\frac{Du}{Dt}&= -\nabla\cdot\bm{q}+q_V+\bm{\sigma}:\nabla\bm{v},
\end{aligned}
:::
where the material derivative is defined as the differential operator
:::{math}
\frac{D}{Dt}= \frac{\partial}{\partial t}+\bm{v}\cdot\nabla.
:::
Conservation of angular momentum further requires the stress tensor to be symmetric $\bm{\sigma}^\mathsf{T}=\bm{\sigma}$. For a simple, Newtonian fluid, the stress and heat flux are described by the constitutive relations
:::{math}
:label: eq-constitutive-relations
\begin{aligned}
\bm{\sigma}&=-p\bm{I}+\bm{\tau},\\
\bm{\tau}&=2\mu\bm{D}+\zeta(\nabla\cdot\bm{v})\bm{I},\\
\bm{q}&=-\lambda\nabla T,
\end{aligned}
:::
where the traceless symmetric part of the velocity gradient tensor
:::{math}
:label: eq-D-tensor
\bm{D}=\frac{1}{2}\left(\nabla\bm{v}+(\nabla\bm{v})^{\mathsf T}\right)-\frac{1}{3}(\nabla\cdot\bm{v})\bm{I},
:::
describes the non-isotropic rate of deformation. The coefficients $\mu$ and $\zeta$ are referred to as shear and bulk viscosity, respectively, while $\lambda$ is the heat conductivity that all depend on the local thermodynamic state of the fluid.


The differential equations describe the evolution of density, velocity, and specific internal energy once the fluid state and its spatial gradients are known. Assuming an equation of state of the form $p=p(\rho,T)$ to exist, the equations provide a calculation method
:::{math}
\rho,\ T,\ u,\ \bm{v}
\quad\implies\quad
\partial_t\rho,\ \partial_t\bm{v},\ \partial_tu.
:::
However, the equations are not yet closed. The four unknown field quantities are density, velocity, specific internal energy, and temperature, but the conservation equations provide evolution equations only for the first three. The time evolution of temperature, $\partial_tT$, is missing. A further thermodynamic relation of the form $u=u(\rho,T)$ is therefore needed to connect the specific internal energy, density, and temperature. Together with the equation of state $p=p(\rho,T)$, this provides the thermodynamic closure of the conservation equations, which is the subject of the next chapter.
