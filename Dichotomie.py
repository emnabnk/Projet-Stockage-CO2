

def dichotomie(f, a, b, eps=1e-6, Nmax=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Erreur : f(a) et f(b) doivent être de signes opposés")

    k = 0
    c = (a + b) / 2
    fc = f(c)

    while abs(fc) > eps and k < Nmax:
        k += 1
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        fc = f(c)

    return c


def f_CT_stationnaire(CT, alpha, beta, delta, gamma, K):
    return alpha * CT * (1 - CT / K) - CT * (beta + delta + gamma)


#Paramètres que l'on impose
alpha = 0.5
beta = 0.05
delta = 0.02
gamma = 0.03
K = 10.0


def f(CT):
    return f_CT_stationnaire(CT, alpha, beta, delta, gamma, K)


CT_eq = dichotomie(f, a=0.01, b=K - 0.01)
print(f"Valeur stationnaire de CT : {CT_eq:.6f}")
