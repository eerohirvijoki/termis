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
\delta\bm{F}_s=\bm{\sigma}\cdot\bm{\hat{n}}dA.
:::
Here $\bm{\sigma}$ is a tensor field of rank-2 referred to as stress, $\bm{\hat{n}}$ is the outward unit normal vector from the body on which the infinitesimal contact force $\delta\bm{F}_s$ acts over the infinitesimal surface area $dA$ at a point $\bm{x}$, as illustrated in {numref}`fig-surface-force`, and the dot $(\cdot)$ represents tensor-vector contraction. The vector field $\bm{t}=\bm{\sigma}\cdot\bm{\hat{n}}$ is referred to as traction, represents force per unit area, and has units of $\text{Pa}$. This required representation for contact forces is a direct consequence of Newton's second law and proved rigorously in {numref}`sec-stress-tensor`. 

:::{figure} ./figs/fig-surface-force.svg
:label: fig-surface-force
:align: center
:width: 50%

A differential surface force $\delta \bm{F}_s$ acting on a differential area $dA$ oriented with respect to an outward unit normal vector $\bm{\hat{n}}$ on a surface of a solid or fluid body.
:::

To apply the infinitesimal contact force and to study the principles of conservation of momentum and energy, one must first understand what kind of a mathematical object a rank-2 tensor field is, how it acts on vector fields through the contraction operator $(\cdot)$, and what calculus rules apply to it.

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
(f\bm{a})\otimes\bm{b}&=f(\bm{a}\otimes\bm{b})=\bm{a}\otimes(f\bm{b}) && \text{Scalar multiplication}\\
\bm{a} \otimes (\bm{b}+\bm{c}) &= \bm{a} \otimes \bm{b}+\bm{a}\otimes\bm{c} && \text{Right linearity}\\
(\bm{b}+\bm{c}) \otimes \bm{a} &= \bm{b} \otimes \bm{a}+\bm{c}\otimes\bm{a} && \text{Left linearity}\\
(\bm{a} \otimes \bm{b}) \cdot \bm{c} &= \bm{a}(\bm{b} \cdot \bm{c}) && \text{Right dyad-vector contraction} \\
\bm{c} \cdot (\bm{a} \otimes \bm{b}) &= (\bm{c} \cdot \bm{a})\bm{b} && \text{Left vector-dyad contraction}
:::
Further, the dyads $\bm{a}\otimes\bm{b}$ and $\bm{b}\otimes\bm{a}$ are equal if and only if $\bm{a}$ and $\bm{b}$ are linearly dependent.
::::{proof:example}
Consider the vectors
:::{math}
:enumerated: false
\bm{a}&=2\bm{\hat{x}}-\bm{\hat{y}},\\
\bm{b}&=-\bm{\hat{x}}+\bm{\hat{y}},\\
\bm{c}&=3\bm{\hat{y}}+\bm{\hat{z}}.
:::
The left and right linearity together with the scalar multiplication rule provide
:::{math}
:enumerated:false
\bm{a}\otimes\bm{b}&=(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}})+(2\bm{\hat{x}}-\bm{\hat{y}})\otimes\bm{\hat{y}}\\
&=(2\bm{\hat{x}})\otimes(-\bm{\hat{x}})+(-\bm{\hat{y}})\otimes(-\bm{\hat{x}})+(2\bm{\hat{x}})\otimes\bm{\hat{y}}+(-\bm{\hat{y}})\otimes\bm{\hat{y}}\\
&=-2\bm{\hat{x}}\otimes\bm{\hat{x}}+\bm{\hat{y}}\otimes\bm{\hat{x}}+2\bm{\hat{x}}\otimes\bm{\hat{y}}-\bm{\hat{y}}\otimes\bm{\hat{y}}.
:::
The right dyad-vector contraction rule gives
:::{math}
:enumerated: false
(\bm{a}\otimes\bm{b})\cdot\bm{c}&=[(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})]\cdot(3\bm{\hat{y}}+\bm{\hat{z}})\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})[(-\bm{\hat{x}}+\bm{\hat{y}})\cdot(3\bm{\hat{y}}+\bm{\hat{z}})]\\
&=(2\bm{\hat{x}}-\bm{\hat{y}})(3)\\
&=6\bm{\hat{x}}-3\bm{\hat{y}},
:::
while the left vector-dyad contraction rule gives
:::{math}
:enumerated: false
\bm{c}\cdot(\bm{a}\otimes\bm{b})&=(3\bm{\hat{y}}+\bm{\hat{z}})\cdot[(2\bm{\hat{x}}-\bm{\hat{y}})\otimes(-\bm{\hat{x}}+\bm{\hat{y}})]\\
&=[(3\bm{\hat{y}}+\bm{\hat{z}})\cdot(2\bm{\hat{x}}-\bm{\hat{y}})] (-\bm{\hat{x}}+\bm{\hat{y}})\\
&=(-\bm{\hat{x}}+\bm{\hat{y}})(-3)\\
&=3\bm{\hat{x}}-3\bm{\hat{y}},
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
f(\bm{x})&=x^2y+yz,\\
\bm{a}(\bm{x})&=xy\bm{\hat{x}}+yz\bm{\hat{y}}+zx\bm{\hat{z}}.
:::
The gradient of the scalar field is a vector field given by
:::{math}
:enumerated: false
\nabla f
&=\frac{\partial f}{\partial x}\bm{\hat{x}}+\frac{\partial f}{\partial y}\bm{\hat{y}}+\frac{\partial f}{\partial z}\bm{\hat{z}}\\
&=2xy\bm{\hat{x}}+(x^2+z)\bm{\hat{y}}+y\bm{\hat{z}}.
:::
The divergence of the vector field returns a scalar field
:::{math}
:enumerated: false
\nabla\cdot\bm{a}
&=\frac{\partial a_x}{\partial x}
+\frac{\partial a_y}{\partial y}
+\frac{\partial a_z}{\partial z}\\
&=y+z+x.
:::
whereas its curl returns another vector field
:::{math}
:enumerated: false
\nabla\times\bm{a}
&=\left(\frac{\partial a_z}{\partial y}-\frac{\partial a_y}{\partial z}\right)\bm{\hat{x}}
+\left(\frac{\partial a_x}{\partial z}-\frac{\partial a_z}{\partial x}\right)\bm{\hat{y}}
+\left(\frac{\partial a_y}{\partial x}-\frac{\partial a_x}{\partial y}\right)\bm{\hat{z}}\\
&=-y\bm{\hat{x}}-z\bm{\hat{y}}-x\bm{\hat{z}}.
:::
The gradient of the vector field is instead a rank-2 tensor field. Its Cartesian coordinate representation is
:::{math}
:enumerated: false
\nabla\bm{a}
&=\frac{\partial a_x}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial x}\bm{\hat{x}}\otimes\bm{\hat{z}}\\
&\quad+\frac{\partial a_x}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial y}\bm{\hat{y}}\otimes\bm{\hat{z}}\\
&\quad+\frac{\partial a_x}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{x}}+\frac{\partial a_y}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{y}}+\frac{\partial a_z}{\partial z}\bm{\hat{z}}\otimes\bm{\hat{z}}\\
&=y\bm{\hat{x}}\otimes\bm{\hat{x}}+z\bm{\hat{x}}\otimes\bm{\hat{z}}\\
&\quad+x\bm{\hat{y}}\otimes\bm{\hat{x}}+z\bm{\hat{y}}\otimes\bm{\hat{y}}\\
&\quad+y\bm{\hat{z}}\otimes\bm{\hat{y}}+x\bm{\hat{z}}\otimes\bm{\hat{z}}.
:::
This illustrates how the action of the differential operator $\nabla$ produces different mathematical objects depending on how it is applied to a scalar, vector, or tensor field.
::::


The process of converting conservation principle of mass, momentum, and energy into local partial differential equations involves transforming surface integrals to volume integrals. Carrying out such tasks requires the action of $\nabla$ on products containing scalar-, vector-, and tensor-valued fields. The rules most needed are
:::{math}
\nabla\cdot(f\bm{a})&=\nabla f\cdot\bm{a}+f\nabla\cdot\bm{a},\\
\nabla\cdot(\bm{a}\otimes\bm{b})&=(\nabla\cdot\bm{a})\bm{b}+\bm{a}\cdot\nabla\bm{b},\\
\nabla\cdot(\bm{\sigma}\cdot\bm{a})&=(\nabla\cdot\bm{\sigma})\cdot\bm{a}+\bm{\sigma}:\nabla\bm{a}.
:::
They become powerful tools when combined with the divergence theorems for scalar and tensor fields
:::{math}
\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA&=\int_V\nabla\cdot\bm{a}dV,\\
\int_{\partial V}\bm{\sigma}\cdot\bm{\hat{n}}dA&=\int_V\nabla\cdot\bm{\sigma}^\mathsf{T}dV,\\
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
\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA&=LA+LA+LA=3L^3.
:::
Since the divergence of $\bm{a}$ is a constant
:::{math}
:enumerated: false
\nabla\cdot\bm{a}
=\frac{\partial x}{\partial x}
+\frac{\partial y}{\partial y}
+\frac{\partial z}{\partial z}
=3,
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
\int_{\partial V}\bm{\sigma}\cdot\bm{\hat{n}}dA
&=\int_{\partial V}(\bm{\hat{x}}\otimes\bm{a})\cdot\bm{\hat{n}}dA\\
&=\bm{\hat{x}}\int_{\partial V}\bm{a}\cdot\bm{\hat{n}}dA\\
&=3L^3\bm{\hat{x}}.
:::
To evaluate the corresponding volume integral, first transpose the tensor:
:::{math}
:enumerated: false
\bm{\sigma}^\mathsf{T}=\bm{a}\otimes\bm{\hat{x}}.
:::
Using the product rule for the divergence of a dyad gives
:::{math}
:enumerated: false
\nabla\cdot\bm{\sigma}^\mathsf{T}
&=\nabla\cdot(\bm{a}\otimes\bm{\hat{x}})\\
&=(\nabla\cdot\bm{a})\bm{\hat{x}}+\bm{a}\cdot\nabla\bm{\hat{x}}\\
&=3\bm{\hat{x}},
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
(\bm{a}\otimes\bm{b})\times\bm{c}&=\bm{a}\otimes(\bm{b}\times\bm{c}) && \text{Right dyad-vector cross product}\\
\bm{a}\times(\bm{b}\otimes\bm{c})&=(\bm{a}\times\bm{b})\otimes\bm{c} && \text{Left vector-dyad cross product}\\
(\bm{a}\otimes\bm{b})\cdot(\bm{c}\otimes\bm{d})&=(\bm{b}\cdot\bm{c})(\bm{a}\otimes\bm{d}) && \text{Dyad-dyad dot product}
:::
Applying these identities, both the right and left tensor-vector cross-product can be evaluated. The results are new rank-2 tensors with Cartesian coordinate representations given by
:::{math}
\bm{\sigma}\times\bm{a}=\sum_{i,j,k,\ell=1}^3\varepsilon_{\ell k j}\sigma_{i\ell}a_k\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j,\\
\bm{a}\times\bm{\sigma}=\sum_{i,j,k,\ell=1}^3\varepsilon_{\ell ki}a_\ell \sigma_{kj}\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j.
:::
Here $\varepsilon_{ijk}$ is the alternating Levi-Civita symbol in three dimensions, familiar from the cross product of two vectors, and defined
:::{math}
\varepsilon_{ijk}=\left\{\begin{aligned}+&1, &&\text{if}\,(i,j,k)\,\text{is an even permutation of}\,(1,2,3),\\-&1, &&\text{if}\,(i,j,k)\,\text{is an odd permutation of}\,(1,2,3),\\&0,&&\text{otherwise}.\end{aligned}\right.
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
\nabla\cdot(\bm{a}\times\bm{\sigma})^\mathsf{T}&=\bm{a}\times\nabla\cdot\bm{\sigma}^\mathsf{T}-\bm{\varepsilon}:(\bm{\sigma}\cdot\nabla\bm{a}),
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

::::{proof:example}
Consider the position vector field
:::{math}
:enumerated: false
\bm{x}=x\bm{\hat{x}}+y\bm{\hat{y}}+z\bm{\hat{z}}.
:::
Its gradient is the identity tensor, since
:::{math}
:enumerated: false
\nabla\bm{x}
=\sum_{i,j=1}^3\partial_i x_j
\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j
=\sum_{i,j=1}^3\delta_{ij}
\bm{\hat{x}}_i\otimes\bm{\hat{x}}_j
=\bm{I}.
:::
Applying the calculus identity for the divergence of a vector-tensor cross product consequently gives
:::{math}
:enumerated: false
\nabla\cdot(\bm{x}\times\bm{\sigma})^\mathsf{T}
&=\bm{x}\times(\nabla\cdot\bm{\sigma}^\mathsf{T})
-\bm{\varepsilon}:(\bm{\sigma}\cdot\nabla\bm{x})\\
&=\bm{x}\times(\nabla\cdot\bm{\sigma}^\mathsf{T})
-\bm{\varepsilon}:\bm{\sigma}.
:::
If the tensor $\bm{\sigma}$ is symmetric, the last term vanishes, leaving
:::{math}
:enumerated: false
\nabla\cdot(\bm{x}\times\bm{\sigma})^\mathsf{T}
=\bm{x}\times(\nabla\cdot\bm{\sigma}^\mathsf{T}).
:::
This observation plays a key role in establishing the symmetry of the stress tensor from the argument that only the torque from forces can change the angular momentum of a body.
::::

## <span class="elementary"></span> Leibniz integral differentiation rule
The tool to convert physics principles to local partial differential equations that describe the evolution of fluids is generally referred to as the Leibniz integral differentiation rule. It describes how integrals of scalar-, vector-, or tensor-valued fields vary in time when evaluated over temporally evolving curves, surfaces, or volumes. The particular use case of the rule to derive the fluid evolution equations involves only volumes, in which case the rule is often referred to as the Reynolds transport theorem. The other important use case for the rule is encountered when deriving the control-volume balance equations needed in engineering applications. In the first case, the evolution of the volume follows the fluid's velocity field. In the second case, the moving volume of fluid is typically enclosed by a mechanical device such as a turbine or a compressor, with the movement of the fluid volume originating from, e.g., rotating turbine or compressor blades.

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
The flow map $\bm{\phi}_t$ is a vector valued function that takes in a point $\bm{x}$ at time $t_0$ and outputs a new point $\bm{\phi}_t(\bm{x})$ that corresponds to the location of the potion at a later time $t$ if it were to follow the vector field $\bm{v}(\bm{x},t)$. Consequently, the flow map can be used to describe how an arbitrary set of points $\Omega(t_0)$ recorded at time $t_0$ would follow the vector field and evolve into a new set of points $\Omega(t)=\{\bm{\phi}_t(\bm{x})|\bm{x}\in\Omega(t_0)\}$ at time $t$. This evolution is illustrated in {numref}`fig-flowmap` for a surface. 

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
\bm{\phi}_t(\bm{x})&=\phi_t^x(\bm{x})\bm{\hat{x}}+\phi_t^y(\bm{x})\bm{\hat{y}}+\phi_t^{z}(\bm{x})\bm{\hat{z}},
:::
with the following component functions in the $x$-, $y$-, and $z$-directions
:::{math}
:enumerated: false
\phi_t^x(\bm{x})&=\cos(\omega(t-t_0))x+\sin(\omega(t-t_0))y,\\
\phi_t^y(\bm{x})&=-\sin(\omega(t-t_0))x+\cos(\omega(t-t_0))y,\\
\phi_t^z(\bm{x})&=z+v_z(t-t_0).
:::
This can be verified by computing the time derivatives of the component functions
:::{math}
:enumerated: false
\frac{d}{dt}\phi_t^x(\bm{x})&=\omega[-\sin(\omega(t-t_0))x+\cos(\omega(t-t_0))y]=\omega \phi_t^y(\bm{x}),\\
\frac{d}{dt}\phi_t^y(\bm{x})&=- \omega[\cos(\omega(t-t_0))x+\sin(\omega(t-t_0))y]=-\omega\phi_t^x(\bm{x}),\\
\frac{d}{dt}\phi_t^{z}(\bm{x})&=v_z,
:::
so that the time derivative of the flow map can be identified as
:::{math}
:enumerated: false
\frac{d}{dt}\bm{\phi}_t(\bm{x})=\omega(\phi_t^y(\bm{x})\bm{\hat{x}}-\phi_t^x(\bm{x})\bm{\hat{y}})+v_z\bm{\hat{z}}=\bm{v}(\bm{\phi}_t(\bm{x})).
:::

The map describes a helical trajectory with constant angular velocity $\omega$ and translative velocity $v_z$ in the $z$-direction.

::::

::::{proof:example}
The scipy-library offers the method odeint for numerical solution of ordinary differential equations. With the help of it, the flowmap of example {numref}`example-flowmap-analytical` can be computed also numerically. The script below performs numerical construction of the map for one initial location and illustrates the resulting trajectory
```{literalinclude} python/example-flowmap-with-odeint.py
:language: python
:start-line: 0
:end-line: 49
:linenos:
```
Running the script results in the figure below, confirming the tracjetory to be helical and to expand into $\bm{\hat{z}}$ direction at constant velocity.
:::{image} ./figs/example-fig-flowmap-with-odeint.svg
:align: center
:width: 80%
:::
::::

Being now aware of the effects of vector fields on the movement of sets of points, assume the set of points to be a volume $V(t)$ that follows the flow of the vector field $\bm{u}(\bm{x},t)$ and is enclosed by a boundary $\partial V(t)$. The vector field $\bm{u}(\bm{x},t)$ is not necessarily the velocity of the fluid itself, denoted by $\bm{v}(\bm{x},t)$. For a volume $V(t)$ that follows the fluid, the two fields coincide. For a control volume, the boundary velocity is determined by how the control volume is selected and may differ from the fluid velocity. Assume then the existence of a scalar-, vector-, or a tensor-valued field $\bm{f}(\bm{x},t)$. The time derivative of the integral of $\bm{f}$ over the volume $V(t)$ evolving according to $\bm{u}(\bm{x},t)$ is then given by the Leibniz rule
:::{math}
:label: eq:leibniz-rule-surface-form
\underbrace{\frac{d}{dt}\int_{V(t)}\bm{f}dV}_{\substack{\text{Time rate of change}\\\text{of an integral of}\,\bm{f}\\\text{calculated over the}\\\text{moving volume}\,V(t)}}&=\underbrace{\int_{V(t)}\partial_t \bm{f}dV}_{\substack{\text{Integral of the local}\\\text{temporal change}\,\partial_t\bm{f}\\\text{calculated over the}\\\text{moving volume}\,V(t)}} +\underbrace{\int_{\partial V(t)}\bm{f}\underbrace{\bm{u}\cdot\bm{\hat{n}} dA}_{\substack{\text{Local rate of}\\\text{change of the}\\\text{volume}\,V(t)\\\text{resulting from}\\\text{movement of}\\\text{boundary}\,\partial V(t)}}}_{\substack{\text{Net flow of}\,\bm{f}\,\text{into the}\\\text{volume}\,V(t)\,\text{due to the}\\\text{movement of the}\\\text{boundary}\,\partial V(t)}}.
:::
According to the rule, both the local temporal change in $\bm{f}$ as well as changes in the volume $V(t)$ itself contribute to the time derivative. Notable, even if the field $\bm{f}$ were stationary in time, the integral of it over a volume could still change in time if the volume would move and, at different times, occupy domains in space where the field $\bm{f}$ varies spatially. 

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
align: center
:width:100%
:::
Assuming $f(x)$ to have an integral function $F(x)$ such that $dF(x)/dx=f(x)$, a direct computation of the left side of the Leibniz rule then provides
:::{math}
:enumerated: false
\frac{d}{dt}\int_{V(t)}fdV&=A\frac{d}{dt}\int_{ut}^{ut+L}f(x)dx\\
&=A\frac{d}{dt}(F(ut+L)-F(ut))\\
&=Auf(ut+L)-Auf(ut)
:::
The first term on the right corresponds to the rate $Au>0$ at which the moving volume gains volume through the boundary at $x=ut+L$, multiplied by the value of the function $f(x)$ at that boundary. The second term describes the corresponding loss of volume at the rate $-Au<0$ through the trailing boundary at $x=ut$, multiplied by the value of $f(x)$ there.

On the right side of the Leibniz rule only the boundary term survives since $\partial_tf(\bm{x})=0$. Further, the lateral boundary does not contribute since the velocity field is parallel to it and therefore has no component in the direction of its outward normal. On the boundary $x=ut+L$, one has $\bm{\hat{n}}=\bm{\hat{x}}$. On the boundary $x=ut$, one has $\bm{\hat{n}}=-\bm{\hat{x}}$ instead. Therefore
:::{math}
:enumerated: false
\int_{\partial V(t)}f\bm{u}\cdot\bm{\hat{n}}dA=Auf(ut+L)-Auf(ut),
:::
which exactly correspond to the left side of the Leibniz rule.
::::

With the help of the divergence theorem and vector calculus rules the surface integral in the Leibniz rule can be converted to a volume integral containing generally three terms
:::{math}
:label: eq:leibniz-rule-volume-form
\frac{d}{dt}\int_{V(t)}\bm{f}dV&=\int_{V(t)}\left(\partial_t \bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})\right)dV\\
&=\int_{V(t)}\left(\partial_t \bm{f}+(\nabla\cdot\bm{u})\bm{f}+(\bm{u}\cdot\nabla)\bm{f}\right)dV
:::
It is this last form of the Leibniz rule that enables one to convert the physics principles of mass, momentum, and energy conservation into local partial differential equations.

For those interested in progressing beyond the use of the Leibniz rule, and to understand also the derivation of it, the details are provided in the intermediate and advanced {numref}`sec-differential-elements`, {numref}`sec-differential-elements-evolution` and {numref}`sec-leibniz-rule-derivation`. Those more interested following the core engineering path may skip these section and jump directly to {numref}`sec-conservation-of-mass` that investigates the principle of mass conservation.

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
dV&=\left|d\bm{\ell}_{i}\times d\bm{\ell}_{j}\cdot d\bm{\ell}_{k}\right|%\\
%&=|d\bm{A}_{k}\cdot d\bm{\ell}_{k}|\\
=\left|\frac{\partial \bm{x}}{\partial \xi_i}\times\frac{\partial \bm{x}}{\partial \xi_j}\cdot\frac{\partial \bm{x}}{\partial \xi_k}\right|d\xi_i d\xi_j d\xi_k.
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
d\bm{A}_{x}&=d\bm{\ell}_{y}\times d\bm{\ell}_{z}=\bm{\hat{y}}\times\bm{\hat{z}}dydz=\bm{\hat{x}}dydz,\\
d\bm{A}_{y}&=d\bm{\ell}_{z}\times d\bm{\ell}_{x}=\bm{\hat{z}}\times\bm{\hat{x}}dydz=\bm{\hat{y}}dzdx,
:::
and a differential volume element
:::{math}
:enumerated: false
dV=|d\bm{A}_x\cdot d\bm{\ell}_x|=|d\bm{A}_y\cdot d\bm{\ell}_y|=dxdydz.
:::
In cylindrical coordinates $(r,\vartheta,z)$, the differential line elements are computed to be
:::{math}
:enumerated: false
d\bm{\ell}_{r}&=(\cos\vartheta\bm{\hat{x}}+\sin\vartheta\bm{\hat{y}})dr,\\
d\bm{\ell}_{\vartheta}&=(-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})d\vartheta,\\
d\bm{\ell}_{z}&=\bm{\hat{z}}dz.
:::
They generate differential oriented surface elements such as
:::{math}
:enumerated: false
d\bm{A}_{z}&=d\bm{\ell}_{r}\times d\bm{\ell}_{\vartheta}\\
&=(\cos\vartheta\bm{\hat{x}}+\sin\vartheta\bm{\hat{y}})\times (-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})drd\vartheta\\
&=\bm{\hat{z}}rdrd\vartheta,
:::
and
:::{math}
:enumerated: false
d\bm{A}_{r}&=d\bm{\ell}_{\vartheta}\times d\bm{\ell}_{z}\\
&=(-r\sin\vartheta\bm{\hat{x}}+r\cos\vartheta\bm{\hat{y}})\times \bm{\hat{z}}d\vartheta dz\\
&=(r\sin\vartheta\bm{\hat{y}}+r\cos\vartheta\bm{\hat{x}})d\vartheta dz,
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
\frac{d}{dt}\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}&=\frac{\partial}{\partial \xi_i}\frac{d\bm{\psi}_t(\bm{x})}{dt}=\frac{\partial \bm{u}(\bm{\psi}_t(\bm{x}),t)}{\partial \xi_i}
=\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}\cdot\nabla\bm{u}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\nabla\bm{u}\right)^\mathsf{T}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i},
:::
where $(\nabla\bm{u})^\mathsf{T}|_{(\bm{\psi}_t(\bm{x}),t)}$ is the transpose of the rank-2 tensor field $\nabla\bm{u}$ evaluated at $\bm{\psi}_t(\bm{x})$ at time $t$. 
::::{proof:example}
Provide here a simple example that calculates the time rate of change of the basis vectors explicitly and via the vector field gradient observing them to be equal. 
::::


At the same point and time, the differential line, surface, and volume elements are defined
:::{math}
d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{\partial \bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i,\\
d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}&=d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left|d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}\right|.
:::
The time rate of change of the line element only requires the substitution of the the rate of change of the vector generating it, resulting in
:::{math}
:label: eq-dl-dt
\frac{d}{dt}d\bm{\ell}_{i}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i=\left(\nabla\bm{u}\right)^\mathsf{T}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{\partial\bm{\psi}_t(\bm{x})}{\partial \xi_i}d\xi_i\\
&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{i}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}.
:::
One recognizes that the time derivative of the differential line-element is proportional to the element itself but modified by the action of the vector field gradient. This pattern repeats itself also in the time derivatives of the oriented surface element and the volume element. In case of the oriented surface element, the calculation is straightforward, leverages the previous result {numref}`eq-dl-dt`, but requires a bit more algebra, resulting in
:::{math}
:label: eq-dA-dt
\frac{d}{dt}d\bm{A}_k\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\left(d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\nonumber\\
&=\frac{d}{dt}d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{\ell}_i\big|_{(\bm{\psi}_t(\bm{x}),t)}\times \frac{d}{dt}d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{i}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\times d\bm{\ell}_j\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{\ell}_{i}\big|_{(\bm{\psi}_t(\bm{x}),t)}\times\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}_{j}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
:::
Again, the time rate of change is proportional to the element itself, operated on with a rank-2 tensor involving the vector field gradient. In case of the volume element, the calculation leverages both previous results {numref}`eq-dl-dt` and {numref}`eq-dA-dt`, providing
:::{math}
:label: eq-dV-dt
\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\frac{d}{dt}\left(d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\nonumber\\
&=\frac{d}{dt}d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\frac{d}{dt}d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=d\bm{\ell}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot \left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&\quad+d\bm{A}_{k}\big|_{(\bm{\psi}_t(\bm{x}),t)}\cdot\left((\nabla\bm{u})^\mathsf{T}\cdot d\bm{\ell}_{k}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\nonumber\\
&=\left((\nabla\cdot\bm{u})dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
:::
Since the coordinate system $(\xi_1,\xi_2,\xi_3)$ is arbitrary, it can be chosen locally to be adapted to an arbitrary initial curve or oriented surface. In the case of a curve, one chooses one of the coordinates, for example $\xi_i$, to parametrize the initial curve, while keeping the other two coordinates fixed. In the case of an oriented surface, one chooses two coordinates, for example $\xi_i$ and $\xi_j$, to span the initial surface, while keeping the third coordinate $\xi_k$ fixed. The coordinate direction associated with $\xi_k$ can be chosen to point along the surface normal of the initial surface. The coordinate labels are then held fixed as the flow map $\bm{\psi}_t$ carries the initial curve or surface forward in time. The derived evolution equations therefore apply to differential line and surface elements of arbitrary orientation, independently of the coordinate chart used to represent them. Dropping the explicit coordinate labels, one obtains
:::{math}
:label: eq-dl-dA-dV-dt
\frac{d}{dt}d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left((\nabla \bm{u})^\mathsf{T}\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\frac{d}{dt}d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left(\left((\nabla\cdot\bm{u})\bm{I}-\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}&=\left((\nabla\cdot\bm{u})dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}.
:::
Note, however, that a single coordinate chart is not necessarily sufficient to describe an entire curve or surface. Instead, multiple coordinate patches may need to be used. 

Since $\nabla\cdot\bm{u}=\nabla\bm{u}:\bm{I}$, a common term, the gradient $\nabla\bm{u}$ of the vector field $\bm{u}$, appears in all of the time derivatives of the differential elements in {numref}`eq-dl-dA-dV-dt`. The proportionality of the time rate of change of each element to itself is encoded entirely by the rank-2 tensor $\nabla\bm{u}$. Interesting observations, regarding this term can be made that later help justify the form of the stress tensor. To illustrate the observations, decompose the tensor $\nabla\bm{u}$ into three separate parts
:::{math}
\nabla\bm{u}=\bm{D}+\frac{1}{3}(\nabla\cdot\bm{u})\bm{I}+\bm{\Omega}.
:::
Here the symmetric and traceless tensor $\bm{D}$ and the antisymmetric tensor $\bm{\Omega}$ are 
:::{math}
\bm{D}&=\frac{1}{2}\left(\nabla\bm{u}+(\nabla\bm{u})^\mathsf{T}\right)-\frac{1}{3}(\nabla\cdot\bm{u})\bm{I},\\
\bm{\Omega}&=\frac{1}{2}\left(\nabla\bm{u}-(\nabla\bm{u})^\mathsf{T}\right).
:::
While the decomposition may appear superficial, each of the parts has a distinct role in generating and characterizing motion. The term $\tfrac{1}{3}(\nabla\cdot\bm{u})\bm{I}$ describes isotropic deformation, the term $\bm{D}$ describes deformation that is non-isotropic but volume-preserving, and the term $\bm{\Omega}$ describes rotation without deformation. This can be verified by tracking the movement of points $\bm{x}(t)$ in the flow of $\bm{u}(\bm{x},t)$.

::::{proof:example}
Consider three different velocity fields
:::{math}
:enumerated: false
\bm{v}_D&=\frac{v_0}{L_0}(x\bm{\hat{x}}-y\bm{\hat{y}}),
&\bm{v}_\Omega&=\frac{v_0}{L_0}(-y\bm{\hat{x}}+x\bm{\hat{y}}),
&\bm{v}_\text{div}&=\frac{v_0}{L_0}(x\bm{\hat{x}}+y\bm{\hat{y}}),
:::
For each field, only one contribution to the velocity gradient tensor is non-zero
:::{math}
:enumerated: false
\bm{D}(\bm{v}_D)&=\frac{v_0}{L_0}(\bm{\hat{x}}\bm{\hat{x}}-\bm{\hat{y}}\bm{\hat{y}}), & \bm{\Omega}(\bm{v}_D)&=\bm{0}, & \nabla\cdot\bm{v}_D&=0,\\
\bm{D}(\bm{v}_\Omega)&=\bm{0}, & \bm{\Omega}(\bm{v}_\Omega)&=\frac{v_0}{L_0}(\bm{\hat{x}}\bm{\hat{y}}-\bm{\hat{y}}\bm{\hat{x}}), & \nabla\cdot\bm{v}_\Omega&=0, \\
\bm{D}(\bm{v}_\text{div})&=\bm{0}, & \bm{\Omega}(\bm{v}_\text{div})&=\bm{0}, & \nabla\cdot\bm{v}_\text{div}&=\frac{2v_0}{L_0}.
:::
Integrate then points in space according to the differential equation
:::{math}
:enumerated: false
\frac{d\bm{x}(t)}{dt}=\bm{v}(\bm{x}(t)),
:::
until a time of $t=v_0/(2L_0)$. A square of points, initially standing on it's corner, changes in the following manner under different vector fields
:::{image} ./figs/example-fig-D-Omega-div-flow-individually.svg
:align: center
:width: 100%
:::
The field $\bm{u}_D$ has stretched the square in the $x$-direction and squeezed it in the $y$-direction, corresponding to non-isotropic volume-preserving deformation. The field $\bm{u}_\Omega$ has rotated the square without deforming it. The field $\bm{u}_\text{div}$ has isotropically scaled the square volume.

More complicated combined effects are observed for velocity fields that have more complicated spatial dependencies. For example, the velocity field
:::{math}
:enumerated: false
\bm{u}=u_0\frac{-y\bm{\hat{x}}+x\bm{\hat{y}}}{\sqrt{x^2+y^2}}+\frac{u_0}{L_0^2}(x^2\bm{\hat{x}}+y^2\bm{\hat{y}}),
:::
results in non-uniform rotation and deformation.
:::{image} ./figs/example-fig-D-Omega-div-flow-complicated.svg
:align: center
:width: 50%
:::
::::


(sec-leibniz-rule-derivation)=
## <span class="advanced"></span> Derivation of the Leibniz rule
Equipped with the knowledge of how differential elements change under the flow of a vector field $\bm{u}(\bm{x},t)$, pushed forward by the flow map $\bm{\psi}_t$, one is ready to apply the associated formulae {numref}`eq-dl-dA-dV-dt` and compute time derivatives of integrals over curves, surfaces, and volumes that move along the flow of the field.

Define a time dependent curve $C(t)$, an oriented surface $S(t)$, and a volume $V(t)$ as images of some initial curve $C(t_0)$, surface $S(t_0)$, and volume $V(t_0)$ with respect to the flow map $\bm{\psi}_t$
:::{math}
C(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in C(t_0)\},\\
S(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in S(t_0)\},\\
V(t)&=\{\bm{\psi}_t(\bm{x})|\bm{x}\in V(t_0)\}.
:::
Assume a scalar-, vector-, or tensor-valued field $\bm{f}(\bm{x},t)$, and consider the following integrals over the time-dependent curve, surface, and volume
:::{math}
\int_{C(t)}\bm{f}(\bm{x},t)\cdot d\bm{\ell}\big|_{\bm{x}},\\
\int_{S(t)}\bm{f}(\bm{x},t)\cdot d\bm{A}\big|_{\bm{x}},\\
\int_{V(t)}\bm{f}(\bm{x},t)dV\big|_{\bm{x}}.
:::
Here, the integration label $\bm{x}$ is shown explicitly for the differential elements, for book-keeping. Perform then a change of integration labels with the help of the flow map so that 
:::{math}
\int_{C(t)}\bm{f}(\bm{x},t)\cdot d\bm{\ell}\big|_{\bm{x}}&=\int_{C(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\int_{S(t)}\bm{f}(\bm{x},t)\cdot d\bm{A}\big|_{\bm{x}}&=\int_{S(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)},\\
\int_{V(t)}\bm{f}(\bm{x},t)dV\big|_{\bm{x}}&=\int_{V(t_0)}\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}.
:::
On the left, the label $\bm{x}$ denotes the time-dependent domains $C(t)$, $S(t)$, and $V(t)$. On the right, the label $\bm{x}$ denotes the time-indepent domains $C(t_0)$, $S(t_0)$, $V(t_0)$ instead, and the time dependence has been moved inside the integrals via the change of integration labels with the flow map. Since the integration domains no longer depend on time, computation of time derivatives of the integrals can be performed. Before that, use the chainrule and {numref}`eq-dl-dA-dV-dt` to compute the derivatives
:::{math}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot \frac{d}{dt}d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
:::
:::{math}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot \frac{d}{dt}d\bm{A}\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+(\nabla\cdot\bm{u})\bm{f}-\bm{f}\cdot\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})-\bm{f}\cdot\nabla\bm{u}\right)\cdot d\bm{A}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
:::
:::{math}
&\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\frac{d}{dt}\bm{f}(\bm{\psi}_t(\bm{x}),t)dV\big|_{(\bm{\psi}_t(\bm{x}),t)}
+\bm{f}(\bm{\psi}_t(\bm{x}),t)\frac{d}{dt}dV\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}(\nabla\cdot\bm{u})\right)dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\left(\left(\partial_t\bm{f}+\nabla\cdot(\bm{u}\otimes\bm{f})\right)dV\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}
:::
Now, with the help of the formula above, calculate the time derivative of the line integral and transforms the integration labels back to the time dependent domain
:::{math}
:label: eq-leibniz-rule-line
\frac{d}{dt}\int_{C(t)}(\bm{f}\cdot d\bm{\ell})\big|_{(\bm{x},t)}&=\int_{C(t_0)}\frac{d}{dt}\left(\bm{f}(\bm{\psi}_t(\bm{x}),t)\cdot d\bm{\ell}\big|_{(\bm{\psi}_t(\bm{x}),t)}\right)\\
&=\int_{C(t_0)}\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{\psi}_t(\bm{x}),t)}\\
&=\int_{C(t)}\left(\left(\partial_t\bm{f}+\bm{u}\cdot\nabla\bm{f}+\bm{f}\cdot(\nabla\bm{u})^\mathsf{T})\right)\cdot d\bm{\ell}\right)\big|_{(\bm{x},t)}.
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
Since the integration labels on boths sides now are the same again, they are usually dropped. 

Each of the derived integral formulae have their place in fluid mechanics. In these notes, equation {numref}`eq-leibniz-rule-volume` is utilized to derive the fluid equations and to establish engineering balance equations over control volumes. Once fluid equations are established, the equation {numref}`eq-leibniz-rule-surface` can be used to prove the conservation of vorticity flux through a surface that moves with the fluid in inviscid barotropic flows, a result better known as Helmholtz's vortex theorem. The equation {numref}`eq-leibniz-rule-line`, on the other hand, could be used to prove Kelvin's circulation theorem for similar fluids. These theorems have important applications in studies of atmospheric flows.

As in these notes the time derivative of the volume integral has a major role, it is useful to convert the divergence term into a surface term for its physical interpretation. With the divergence theorem, one finds
:::{math}
\underbrace{\frac{d}{dt}\int_{V(t)}\bm{f}dV}_{\substack{\text{Time rate of change}\\\text{of an integral of}\,\bm{f}\\\text{calculated over the}\\\text{moving volume}\,V(t)}}&=\underbrace{\int_{V(t)}\partial_t \bm{f}dV}_{\substack{\text{Integral of the local}\\\text{temporal change}\,\partial_t\bm{f}\\\text{calculated over the}\\\text{moving volume}\,V(t)}} +\underbrace{\int_{\partial V(t)}\bm{f}\underbrace{\bm{u}\cdot\bm{\hat{n}} dA}_{\substack{\text{Local rate of}\\\text{change of the}\\\text{volume}\,V(t)\\\text{resulting from}\\\text{movement of}\\\text{boundary}\,\partial V(t)}}}_{\substack{\text{Net flow of}\,\bm{f}\,\text{into the}\\\text{volume}\,V(t)\,\text{due to the}\\\text{movement of the}\\\text{boundary}\,\partial V(t)}}.
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
\int_{a(t)}^{b(t)} f(x,t) dx&=\int_{\psi(a(t_0),t)}^{\psi(b(t_0),t)}f(x,t)dx=\int_{a(t_0)}^{b(t_0)}f(\psi(x_0,t),t)d\psi(x_0,t)\\
&=\int_{a(t_0)}^{b(t_0)}f(\psi(x_0,t),t)\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0.
:::
To proceed, apply the chainrule to the derivative of the flow map
:::{math}
:enumerated: false
\frac{d}{dt}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}&=\frac{\partial^2\psi(x,t)}{\partial x\partial t}\Big|_{(x_0,t)}=\frac{\partial u(\psi(x,t),t)}{\partial x}\Big|_{(x_0,t)}\\
&=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}.
:::
One may now identify that 
:::{math}
:enumerated: false
\frac{d}{dt}d\psi(x_0,t)&=\frac{d}{dt}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0\\
&=\frac{\partial u}{\partial x}\Big|_{(\psi(x_0,t),t)}d\psi(x_0,t),
:::
is analogous to the time derivative of a differential volume element with $\partial u/\partial x$ serving the role of velocity divergence. Considering that the time derivative of the composed function $f(\psi(x_0,t),t)$ can be written 
:::{math}
:enumerated: false
\frac{d}{dt}f(\psi(x_0,t),t)&=\frac{\partial f}{\partial t}\Big|_{(\psi(x_0,t),t)}+\frac{\partial f}{\partial x}\Big|_{(\psi(x_0,t),t)}\frac{\partial \psi}{\partial t}\Big|_{(x_0,t)}\\
&=\left(\frac{\partial f}{\partial t}+u\frac{\partial f}{\partial x}\right)\Big|_{(\psi(x_0,t),t)},
:::
the time derivative of the integral becomes
:::{math}
:enumerated: false
\frac{d}{dt}\int_{a(t)}^{b(t)} f(x,t) dx&=\int_{a(t_0)}^{b(t_0)}\frac{d}{dt}\left(f(\psi(x_0,t),t)\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}\right)dx_0\\
&=\int_{a(t_0)}^{b(t_0)}\left(\frac{\partial f}{\partial t}+u\frac{\partial f}{\partial x}+f\frac{\partial u}{\partial x}\right)\Big|_{(\psi(x_0,t),t)}\frac{\partial\psi}{\partial x}\Big|_{(x_0,t)}dx_0\\
&=\int_{a(t)}^{b(t)}\left(\frac{\partial f}{\partial t}+\frac{\partial(uf)}{\partial x}\right)\Big|_{(x,t)}dx\\
&=\int_{a(t)}^{b(t)}\frac{\partial f(x,t)}{\partial t}dx+\Big[u(x,t)f(x,t)\Big]_{x=a(t)}^{x=b(t)}.
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
Consider a volume 

## <span class="elementary"></span> Conservation of momentum
According to Newton's second law, the rate of change of linear momentum of a body equals the net forces acting on it. The forces acting on a volume of fluid include gravity that is distributed throughout the fluid volume, and mechanical contact force that is distributed on the surface of the body. Since the total force must be finite, yet distributed over the body volume and surface, both the body and surface force need to be treated differentially while the total force is an integral of the differential force. 

(sec-stress-tensor)=
## <span class="advanced"></span> Cauchy's theorem and emerge of the stress tensor

## <span class="intermediate"></span> Conservation of angular momentum and symmetry of the stress tensor
For point masses, the definition 

## <span class="elementary"></span> Conservation of energy
A differential volume 

## <span class="elementary"></span> Constitutive relations for stress and heat flux
The conservation principles of mass, momentum, and energy discussed above lead to local differential equations from which the local time rate of change of fluid's density, velocity, and internal energy ought to be computed. 

## Summary
The motion of a fluid can be described by following individual points along the flow and studying how differential line, surface, and volume elements evolve. 
