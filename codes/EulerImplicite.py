import numpy as np
import matplotlib.pyplot as plt

# Coefficients - Scénario de déforestation
alpha = 0.4    # Diminution forte de la photosynthèse
beta = 0.08     # Hausse brutale de la mortalité
delta = 0.04    # Augmentation du transfert vers les sols
gamma = 0.03    # Décomposition accélérée
K = 40        # Réduction de la capacité de stockage

def f_Ca(t,CT,CS):
    return -alpha*CT *(1-CT/K) + beta*CT+ delta*CS

def df_Ca(t,x):
    return 0

def f_Ct(t, CT):
    return - (alpha / K) * CT**2 + (alpha - beta - delta - gamma) * CT

def df_Ct(t,x):
    return -2* (alpha/K)*x+(alpha-beta-delta-gamma)

def f_Cs(t,CS):
    return gamma*CT - delta * CS + delta*CT

def df_Cs(t,x):
    return -delta

def Newton_explicit(f, df, x0, t, max_iter, eps):
    x = x0
    for k in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < eps:
            return x, k
        if dfx == 0:
            raise ZeroDivisionError("La dérivée est nulle, impossible de continuer.")
        x = x - fx / dfx
    return x, k

def euler_implicite(f, df, Ct0, t0, tf, N):
    t = np.linspace(t0, tf, N + 1)
    Ct = np.zeros(N + 1)
    Ct[0] = Ct0
    h = (tf - t0) / N
    for n in range(N):
        t_next = t[n+1]
        Ct_n = Ct[n]
        F = lambda Ct_next: Ct_next - (Ct_n + h * f(t_next, Ct_next))
        dF = lambda Ct_next: 1 - h * df(t_next, Ct_next)
        Ct_next, _ = Newton_explicit(F, dF, Ct_n, t_next, max_iter=1000, eps=1e-6)
        Ct[n+1] = Ct_next
   
    return t, Ct



# Conditions initiales
CA0 = 400   # Atmosphère
CT0 = 300   # Arbres
CS0 = 200  # Sols
#les bornes temporelles
t0 = 0
tf = 100
#nombre de pas
N = 1000
h = (tf - t0) / N

t,C_T = euler_implicite(f_Ct,df_Ct,CT0,t0,tf,N)
CT = C_T[N]
_,C_S = euler_implicite(f_Cs,df_Cs,CS0,t0,tf,N)
CS = C_S[N]

C_A = np.zeros(N + 1)
C_A[0] = CA0
for i in range(N):
    C_A[i+1] = C_A[i] + h*f_Ca(t,C_T[i],C_S[i])


plt.plot(t, C_T, label="C_T(t)")
plt.plot(t,C_S,label="C_S(t)")
plt.plot(t,C_A,label="C_A(t)")
plt.xlabel("Temps (année)")
plt.ylabel("Concentrations (GTc)")
plt.grid(True)
plt.legend()
plt.title("Évolution de C_T")

plt.show()
