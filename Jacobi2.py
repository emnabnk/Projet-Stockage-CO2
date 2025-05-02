import numpy as np

#Exemple juste pour tester la fonction
alpha = 0.4
beta = 0.08
gamma = 0.04
delta = 0.03
K = 40.0



def S(CT):
    return alpha * CT * (1 - CT/K)

#Voir la théorie pour savoir comment A et b sont définis
A = np.array([
    [beta , delta],
    [gamma + delta, -delta]
])

b = np.array([alpha*K*((beta*gamma*delta)/alpha)*(1 - (beta+delta+gamma)/alpha),0])


# Méthode de Jacobi fait selon l'algorithme donné dans la leçon

def jacobi(A, b, x0, eps, Nmax):
    n = len(b)
    x = x0.copy()
    k = 0
    invD = np.diag(1.0 / np.diag(A))
    MatN = -np.triu(A, 1) - np.tril(A, -1)

    while np.linalg.norm(A @ x - b) / np.linalg.norm(b) > eps and k < Nmax:
        k += 1
        x = invD @ (MatN @ x - b)

    return x, k


x0 = np.array([50.0, 50.0])  #x0 avec des valeurs arbitraires
solution, iterations = jacobi(A, b, x0,eps=10e-6,Nmax=100)
CT_eq, CS_eq = solution
CA_eq = (beta*CT_eq + delta*CS_eq)/(alpha*(1 - CT_eq/K))

# Résultats
print(f"Solution trouvée après {iterations} itérations:")
print("CT =",CT_eq)
print("CS =",CS_eq)
print("CA =",CA_eq)

# Vérification
print("\nVérification des équations à l'équilibre:")
print(f"dCT/dt = {S(CT_eq) - beta*CT_eq - delta*CT_eq - gamma*CT_eq:.2e}")
print(f"dCS/dt = {gamma*CT_eq - delta*CS_eq + delta*CT_eq:.2e}")
print(f"dCA/dt = {-S(CT_eq) + beta*CT_eq + delta*CS_eq:.2e}")





























