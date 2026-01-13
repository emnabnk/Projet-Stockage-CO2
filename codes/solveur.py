import numpy as np
from scipy.integrate import solve_ivp

alpha = 0.4
beta = 0.08
gamma = 0.04
delta = 0.03
K = 40.0


# Fonction S(C_T)
def S(C_T):
    return alpha * C_T * (1 - C_T / K)

# Système d'équations
def carbon_system(t, y):
    C_A, C_T, C_S = y
    dCA = -S(C_T) + beta * C_T + delta * C_S
    dCT = S(C_T) - (beta + delta + gamma) * C_T
    dCS = gamma * C_T - delta * C_S + delta * C_T
    return [dCA, dCT, dCS]

# Conditions initiales
y0 = [400.0, 300.0, 200.0]

# Intégration
sol = solve_ivp(carbon_system, [0, 50], y0, t_eval=np.linspace(0, 50, 500))
somme = sol.y[0]+sol.y[1]+sol.y[2]
# Tracer les résultats
plt.plot(sol.t, sol.y[0], label='C_A (Atmosphère)')
plt.plot(sol.t, sol.y[1], label='C_T (Arbres)')
plt.plot(sol.t, sol.y[2], label='C_S (Sols)')
plt.plot(sol.t,somme)
plt.xlabel('Temps')
plt.ylabel('Quantité de carbone')
plt.legend()
plt.title('Évolution des stocks de carbone')
plt.grid()
plt.show()

