import numpy as np
import matplotlib.pyplot as plt

def euler_explicite(f, y0, t0, tf, N):
    t = np.linspace(t0, tf, N+1)
    y = np.zeros((N+1, len(y0)))
    y[0] = y0
    h = (tf - t0) / N
    for n in range(N):
        y[n+1] = y[n] + h * f(t[n], y[n])
    return t, y

def systeme_param(alpha, beta, gamma, delta, K):
    def systeme(t, y):
        CA, CT, CS = y
        S = alpha * CT * (1 - CT / K)
        dCA = -S + beta * CT + delta * CS
        dCT = S - (beta + delta + gamma) * CT
        dCS = gamma * CT - delta * CS + delta * CT
        return np.array([dCA, dCT, dCS])
    return systeme

def simulation(parametre, valeurs):
    params = {
        'alpha': 0.4,
        'beta': 0.08,
        'gamma': 0.04,
        'delta': 0.03,
        'K': 40.0
    }

    y0 = [400, 300, 200]
    t0, tf, N = 0, 100, 1000

    plt.figure(figsize=(15, 4))

    for val in valeurs:
        params[parametre] = val
        systeme = systeme_param(**params)
        t, y = euler_explicite(systeme, y0, t0, tf, N)
        CA, CT, CS = y[:, 0], y[:, 1], y[:, 2]

        plt.subplot(1, 3, 1)
        plt.plot(t, CA, label=f"{parametre}={val}")
        plt.title("CA(t)")
        plt.xlabel("Temps"); plt.ylabel("CA"); plt.grid()

        plt.subplot(1, 3, 2)
        plt.plot(t, CT, label=f"{parametre}={val}")
        plt.title("CT(t)")
        plt.xlabel("Temps"); plt.ylabel("CT"); plt.grid()

        plt.subplot(1, 3, 3)
        plt.plot(t, CS, label=f"{parametre}={val}")
        plt.title("CS(t)")
        plt.xlabel("Temps"); plt.ylabel("CS"); plt.grid()

    plt.subplot(1, 3, 1)
    plt.legend()
    plt.tight_layout()
    plt.suptitle(f"Effet de {parametre}", fontsize=14, y=1.05)
    plt.show()

# Exemple d'utilisation :
simulation("alpha", [0.2, 0.4, 0.6, 0.8])
