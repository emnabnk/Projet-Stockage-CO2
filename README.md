# Modeling Carbon Dioxide Storage in Forests

[cite_start]This project was conducted as part of the **MAM3 Numerical Analysis 2** course at **Polytech Nice Sophia** (Université Côte d'Azur) for the 2024-2025 academic year[cite: 3, 4, 26, 27].

## Authors
* [cite_start]Ben Khalifa Emna [cite: 2]
* [cite_start]Giovanni Honakoko [cite: 2]
* [cite_start]Ziad Zineb [cite: 2]

## Project Summary
[cite_start]The objective of this project is to study the dynamics of carbon exchanges between the atmosphere, tree biomass (trees), and forest soils[cite: 21]. [cite_start]In the context of climate change, we developed a dynamic model based on **Ordinary Differential Equations (ODEs)** to numerically evaluate carbon flows and the system's equilibrium states using advanced numerical methods[cite: 22, 23].

## Theoretical Model
The system considers three main compartments:
* [cite_start]$C_A(t)$: Atmospheric carbon ($CO_2$) [cite: 51]
* [cite_start]$C_T(t)$: Carbon stored in tree biomass [cite: 52]
* [cite_start]$C_S(t)$: Carbon stored in soils [cite: 53]

### System Equations
[cite_start]The exchanges between these compartments are governed by the following system of differential equations[cite: 54]:
1. [cite_start]$\frac{dC_A}{dt} = -S(C_T) + \beta C_T + \delta C_S$ [cite: 56]
2. [cite_start]$\frac{dC_T}{dt} = S(C_T) - \beta C_T - \delta C_T - \gamma C_T$ [cite: 56]
3. [cite_start]$\frac{dC_S}{dt} = \gamma C_T - \delta C_S + \delta C_T$ [cite: 56]

[cite_start]Where $S(C_T) = \alpha C_T(1 - \frac{C_T}{K})$ represents photosynthetic sequestration (logistic model)[cite: 57].

## Implemented Numerical Methods
[cite_start]To solve this non-linear system, several numerical methods were tested and compared[cite: 71]:

### Explicit Methods
* [cite_start]**Explicit Euler**: Built at each time step via an iterative formula[cite: 95, 96].
* [cite_start]**Adams-Bashforth (Order 2)**: A multi-step method using previous terms to calculate the next[cite: 100, 102].
* [cite_start]**Runge-Kutta 2 (Heun's Method)**: Determined to offer the best compromise between stability and convergence speed[cite: 107, 321].
* [cite_start]**Explicit Newton**: Retained as the most optimal for solving non-linear equations in practice[cite: 89, 114].

### Implicit Methods
* [cite_start]**Implicit Euler**: Solved line by line using the 1D Newton method to handle the quadratic equation for $C_T^{(n+1)}$[cite: 127, 137, 151].

## Analysis and Results
[cite_start]Simulations demonstrate that over time, trees and soils store less carbon, resulting in an increase in atmospheric carbon[cite: 170, 171].

### Parametric Analysis
[cite_start]The impact of each parameter was observed[cite: 323, 324]:
* [cite_start]**$\alpha$ (Sequestration)**: As $\alpha$ increases, $C_A$ decreases while $C_T$ and $C_S$ increase[cite: 364, 365, 366].
* [cite_start]**$\beta$ (Respiration)**: Higher $\beta$ leads to increased $C_A$ and decreased $C_T$ and $C_S$[cite: 405, 406, 407].
* [cite_start]**$\gamma$ (Litter Production)**: Increasing $\gamma$ causes a sharp decrease in $C_T$ and an increase in $C_S$ due to tree-to-soil transfer[cite: 498, 499].
* [cite_start]**$\delta$ (Decomposition)**: Higher decomposition rates increase $C_A$ and decrease $C_T$ and $C_S$[cite: 451, 452].

## Technologies Used
* [cite_start]**Language**: Python [cite: 153]
* [cite_start]**Libraries**: `scipy.integrate` (`solve_ivp` used as a reference), `numpy`, `matplotlib`[cite: 153, 154, 155].

## Conclusion and Perspectives
[cite_start]The model highlights the forests' role as a carbon sink[cite: 34]. [cite_start]To improve realism, future versions could include the effect of oceans ($C_O(t)$), accounting for phytoplankton and coastal ecosystems like mangroves[cite: 508, 510, 511].
