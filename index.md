# TERMIS - Thermodynamics for EneRgy and Mechanical engIneering Students

Thes notes are for engineering students interested in thermodynamics and its applications in energy-related fields such as power plant and refrigeration engineering. Many excellent books on the topic exist, yet the material presented here takes a distinct approach.

First, the notes covers not only classical thermodynamics of pure substances but also fluid mechanics to a degree. Thermodynamics as an isolated field describes properties of macroscopic matter, but not how matter moves. Fluid mechanics alone, on the other hand, describes local balances for mass, momentum, and energy in a flow but not how energy relates to measurable properties such as pressure and density. Only together do thermodynamics and fluid mechanics provide a closed macroscopic theory that can be used to analyse refrigeration cycles, power plants, and reciprocating engines. 

Second, the notes aim to build a rigorous foundation for the topic. After discussing the properties of pure substances, the equations of fluid motion are derived from first principles and the closure problem of the equations is embraced, not dismissed. The closure is addressed by inspecting quasistatic flows, leading to discovery of entropy and the establishment of the classical thermodynamic framework. Unlike in typical textbooks, here entropy is found through Carath&eacute;odory's argument rather than via arguments involving Carnot machines. From the closed set of fluid equations, simplified engineering balance equations for mass, momentum, angular momentum, energy, and entropy are derived rigorously with respect to a control volume. This chosen path not only provides the common equations but also clear physical interpretations for the appearing terms. Instead of falling into the common misinterpretation of mechanical work rate as a specific enthalpy difference, the reader will observe it to arise from stress distribution on moving solid surfaces.

Finally, instead of steam tables or non-standard spreadsheets, modern programming tools are leveraged throughout the notes. Thermodynamic data is accessed through Python libraries, and example scripts are provided to create thermodynamic diagrams and to analyse power-plant cycles.

Consequently, certain prerequisites are expected of the reader. Standard single- and multivariable calculus provide the baseline on which the mathematical aspects of thermodynamics and fluid mechanics are built on. Comprehension of Python scripts helps in following the computational examples. In both areas, use of large language models as personal AI study assistants is strongly encouraged. For an enthuastic reader, such tools can explain code excerpts and derivations of equations with exhaustive detail, as well as help recall the baseline calculus tools.

This somewhat unique approach of combining thermodynamics and fluid mechanics is acknowledged pedagogically. To make the notes as accessible as possible yet appropriately challenging, each section heading is color-coded to indicate the depth of the discussion that follows:

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

Some sections unavoidably contain material at varying depths. Nevertheless, a reader interested in traditional energy engineering topics such as computation of pure-substance properties from thermodynamic state, interpretation of the fluid equations, and steady-flow analysis of power plant and refrigeration cycles may well follow only the <span class="elementary"></span>-colored sections. A reader interested in the rigorous derivation of the fluid equations, explanations for why surface-force density is expressed with a stress tensor, how entropy emerges from analysis of quasistatic processes, and how control-volume analysis of the fluid equations combined with fundamenta thermodynamic identities reduces to the everyday engineering formulae for energy and entropy balances usable in power plant analysis is encouraged to study the <span class="intermediate"></span>- and <span class="advanced"></span>-colored sections as well. To help readers gauge their progress on which ever path they choose to follow, the beginning of each chapter contains a list of learning goals to aim for, with core, intermediate, and advanced levels indicated in color.

With these words, I wish you an interesting journey to the world of engineering.


