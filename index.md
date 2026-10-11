# TERMIS - Thermodynamics for EneRgy and Mechanical engIneering Students

This book is for engineering students interested in thermodynamics and its applications in energy-related fields such as power plant and refrigeration engineering. Many excellent books on the topic exist, yet the material presented here takes a distinct approach.

First, the book covers not only classical thermodynamics of pure substances but also fluid mechanics to a degree. Thermodynamics as an isolated field describes properties of macroscopic matter, but not how matter moves. Fluid mechanics alone, on the other hand, describes local balances for mass, momentum, and energy in a flow but not how energy relates to measurable properties such as pressure and density. Only together do thermodynamics and fluid mechanics provide a closed macroscopic theory that can be used to analyse refrigeration cycles, power plants, and reciprocating engines. 

Second, the book aims to build a rigorous foundation for the topic. After discussing the properties of pure substances, the equations of fluid motion are derived from first principles and the closure problem of the equations is embraced, not dismissed. The closure is addressed by inspecting quasistatic flows, leading to discovery of entropy and the establishment of the classical thermodynamic framework. Unlike in typical textbooks, entropy is found through Carath&eacute;odory's argument rather than via arguments involving Carnot machines. From the closed set of fluid equations, simplified engineering balance equations for mass, momentum, angular momentum, energy, and entropy are derived rigorously with respect to a control volume. This chosen path not only provides the common equations but also clear physical interpretations for the appearing terms. Instead of falling into the common misinterpretation of mechanical work rate as a specific enthalpy difference, the reader will observe it to arise from stress distribution on moving solid surfaces.

Finally, instead of steam tables or non-standard spreadsheets, modern programming tools are leveraged throughout the book. Thermodynamic data is accessed through Python libraries, and example scripts are provided to create thermodynamic diagrams and to analyse power-plant cycles.

Consequently, certain prerequisites are expected of the reader. Standard single- and multivariable calculus provide the baseline on which the mathematical aspects of thermodynamics and fluid mechanics are built on. Comprehension of Python scripts helps in following the computational examples. In both areas, use of large language models as personal AI study assistants is encouraged.

This somewhat unique approach is acknowledged pedagogically. To make the book as accessible as possible yet appropriately challenging, each section heading is color-coded to indicate the depth of the discussion to come:

<div class="level-list">
  <div class="level-list-item">
    <span class="elementary"></span>
    <div>Covers core content such as thermodynamic diagrams, balance equations, and rudimentary power-plant analysis.</div>
  </div>
  <div class="level-list-item">
    <span class="intermediate"></span>
    <div>Covers intermediate content such as short programming examples and mathematical core ideas.</div>
  </div>
  <div class="level-list-item">
    <span class="advanced"></span>
    <div>Covers advanced content such as more involved programming examples and deep mathematical explanations.</div>
  </div>
</div>

A reader not interested in deep mathematical details may well follow only the <span class="elementary"></span>-colored sections. A reader ready for full immersion is encouraged to study the <span class="intermediate"></span>- and <span class="advanced"></span>-colored sections as well. To help readers gauge their progress, the beginning of each chapter contains a list of learning goals to aim for, with core, intermediate, and advanced levels indicated in color.


