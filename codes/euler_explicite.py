import numpy as np
import matplotlib.pyplot as plt


alpha = 0.4
beta = 0.08
gamma = 0.04
delta = 0.03
K = 40.0


def euler_explicite(f, y0, t0, tf, N):
    t = np.linspace(t0, tf, N+1)
    y = np.zeros((N+1, len(y0)))
    y[0] = y0
    h = (tf - t0) / N

    for n in range(N):
        y[n+1] = y[n] + h * f(t[n], y[n])

    return t, y



def systeme(t,y):
    CA, CT, CS = y
    S = alpha * CT * (1 - CT/K)
    dCA = -S + beta * CT + delta * CS
    dCT = S - beta * CT - delta * CT - gamma * CT
    dCS = gamma * CT - delta * CS + delta * CT
    return np.array([dCA, dCT, dCS])



# Conditions initiales
y0 = [400.0, 300.0, 200.0]  # CA0, CT0, CS0
t0=0
tf=100
N=1000


t, y = euler_explicite(systeme, y0, t0, tf, N)
CA, CT, CS = y[:, 0], y[:, 1], y[:, 2]

# Visualisation
plt.figure(figsize=(10, 6))
plt.plot(t, CA, label='CA(t) ')
plt.plot(t, CT, label='CT(t) ')
plt.plot(t, CS, label='CS(t) ')
plt.xlabel('Temps')
plt.ylabel('Quantité de carbone')
plt.title('Évolution des stocks de carbone avec la méthode Euler explicite')
plt.legend()
plt.grid()
plt.show()
