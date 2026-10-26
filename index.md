---
title: TERMIS - Thermodynamics for EneRgy and Mechanical engIneering Students
---

These notes are for readers interested in fundamentals of energy engineering, with primary applications in power plants, refrigeration, and reciprocating engines. Many excellent books on the topic exist, yet the material presented here takes a distinct approach.

First, the notes develop classical thermodynamics of pure substances and fluid mechanics together. Thermodynamics alone describes properties of macroscopic matter but not how matter moves. Fluid mechanics, on the other hand, describes local balances for mass, momentum, and energy in a flow but not how energy relates to measurable properties. Together, thermodynamics and fluid mechanics form a closed macroscopic theory that connects measurable properties to the behaviour of engineering systems. 

Second, the notes develop the theory from first principles. After introducing the properties of pure substances, the equations of fluid motion are derived and their closure problem is addressed through the study of quasistatic flows. This leads to the establishment of entropy and the classical thermodynamic framework. Unlike many conventional textbooks, these notes introduce entropy through Carath&eacute;odory's argument rather than reasoning based on Carnot machines. The resulting closed theory then provides a rigorous basis for deriving control-volume balances of mass, momentum, angular momentum, energy, and entropy, while clarifying the physical meaning of the appearing terms. Mechanical work rates emerge from stresses acting on moving solid surfaces, rather than being identified as specific enthalpy differences, and irreversible entropy generation is quantified with viscosity and heat conductivity.

Finally, modern programming tools are used throughout the notes. Thermodynamic properties are accessed through Python libraries, and example scripts are provided for plotting thermodynamic diagrams and analysing power and refrigeration cycles.

The reader is expected to have a working knowledge of single- and multivariable calculus, which provides the mathematical foundation for thermodynamics and fluid mechanics. Familiarity with Python helps in following the computational examples, although the code examples can also serve as starting points for learning. Large language models can be useful study assistants for understanding code, working through derivations, and reviewing mathematical concepts. Their explanations should nevertheless be checked against the notes and the underlying mathematics.

The unconventional combination of thermodynamics and fluid mechanics is reflected in the structure of the notes. To accommodate readers with different interests and levels of mathematical preparedness, section headings are colour-coded according to the depth of the discussion:

<div class="level-list">
  <div class="level-list-item">
    <span class="elementary"></span>
    <div>Core: essential concepts, governing equations, and standard engineering applications.</div>
  </div>
  <div class="level-list-item">
    <span class="intermediate"></span>
    <div>Intermediate: additional reasoning and examples that deepen understanding of the core material.</div>
  </div>
  <div class="level-list-item">
    <span class="advanced"></span>
    <div>Advanced: extended derivations, more demanding mathematical arguments, and further computational exploration.</div>
  </div>
</div>

Some sections contain material at more than one level. Nevertheless, readers primarily interested in conventional energy engineering applications can focus on the core sections, which develop the concepts needed to:

- determine the thermodynamic state of a pure substance;
- apply mass, energy, and entropy balances to engineering systems;
- analyse power and refrigeration cycles using engineering balance equations.

Readers seeking a deeper theoretical understanding are encouraged to study the intermediate and advanced sections as well. These develop the tools needed to derive the fluid equations from first principles, explain the role of the stress tensor in describing contact forces, establish entropy through rigorous analysis of quasistatic processes, and derive familiar engineering energy and entropy balances from the underlying theory.

Each chapter begins with learning goals for the core, intermediate, and advanced levels, helping readers choose a suitable path and assess their progress.

With these words, I wish you an interesting journey into the world of engineering.

