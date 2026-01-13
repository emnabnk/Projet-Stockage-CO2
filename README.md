# Modeling Carbon Dioxide Storage in Forests

This project was conducted as part of the **MAM3 Numerical Analysis 2** course at **Polytech Nice Sophia** (Université Côte d'Azur) for the 2024-2025 academic year.

## Authors
* Ben Khalifa Emna
* Giovanni Honakoko
* Ziad Zineb 

## Project Summary
The objective of this project is to study the dynamics of carbon exchanges between the atmosphere, tree biomass (trees), and forest soils. In the context of climate change, we developed a dynamic model based on **Ordinary Differential Equations (ODEs)** to numerically evaluate carbon flows and the system's equilibrium states using advanced numerical methods.

## Theoretical Model
The system considers three main compartments:
* $C_A(t)$: Atmospheric carbon ($CO_2$) 
* $C_T(t)$: Carbon stored in tree biomass 
* $C_S(t)$: Carbon stored in soils 

### System Equations
The exchanges between these compartments are governed by the following system of differential equations:
1. $\frac{dC_A}{dt} = -S(C_T) + \beta C_T + \delta C_S$ 
2. $\frac{dC_T}{dt} = S(C_T) - \beta C_T - \delta C_T - \gamma C_T$ 
3. $\frac{dC_S}{dt} = \gamma C_T - \delta C_S + \delta C_T$

Where $S(C_T) = \alpha C_T(1 - \frac{C_T}{K})$ represents photosynthetic sequestration (logistic model).

## Implemented Numerical Methods
To solve this non-linear system, several numerical methods were tested and compared:

### Explicit Methods
* **Explicit Euler**: Built at each time step via an iterative formula.
* **Adams-Bashforth (Order 2)**: A multi-step method using previous terms to calculate the next.
* **Runge-Kutta 2 (Heun's Method)**: Determined to offer the best compromise between stability and convergence speed.
* **Explicit Newton**: Retained as the most optimal for solving non-linear equations in practice.

### Implicit Methods
* **Implicit Euler**: Solved line by line using the 1D Newton method to handle the quadratic equation for $C_T^{(n+1)}$.

## Analysis and Results
Simulations demonstrate that over time, trees and soils store less carbon, resulting in an increase in atmospheric carbon.

### Parametric Analysis
The impact of each parameter was observed:
* **$\alpha$ (Sequestration)**: As $\alpha$ increases, $C_A$ decreases while $C_T$ and $C_S$ increase.
* **$\beta$ (Respiration)**: Higher $\beta$ leads to increased $C_A$ and decreased $C_T$ and $C_S$.
* **$\gamma$ (Litter Production)**: Increasing $\gamma$ causes a sharp decrease in $C_T$ and an increase in $C_S$ due to tree-to-soil transfer.
* **$\delta$ (Decomposition)**: Higher decomposition rates increase $C_A$ and decrease $C_T$ and $C_S$.

## Technologies Used
* **Language**: Python
* **Libraries**: `scipy.integrate` (`solve_ivp` used as a reference), `numpy`, `matplotlib`.

## Conclusion and Perspectives
The model highlights the forests' role as a carbon sink. To improve realism, future versions could include the effect of oceans ($C_O(t)$), accounting for phytoplankton and coastal ecosystems like mangroves.
