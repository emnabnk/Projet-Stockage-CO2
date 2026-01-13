import numpy as np
import matplotlib.pyplot as plt
import time

alpha = 0.04
beta = 0.1
gamma = 0.03
delta = 0.01
K = 500.0

def systeme(t,y):
    CA, CT, CS = y
    S = alpha * CT * (1 - CT/K)
    dCA = -S + beta * CT + delta * CS
    dCT = S - beta * CT - delta * CT - gamma * CT
    dCS = gamma * CT - delta * CS + delta * CT
    return np.array([dCA, dCT, dCS])


##### METHODES EXPLICITES #####

def euler_explicite(f, x0, t0, tf, N):
    start = time.time()
    t = np.linspace(t0, tf, N+1)
    y = np.zeros((N+1, len(x0)))
    y[0] = x0
    h = (tf - t0) / N
    for n in range(N):
        y[n+1] = y[n] + h * f(t[n], y[n])
    stop = time.time()
    final_time=stop-start
    return t, y, final_time


def AdamsBashforth(f, x0, t0, tf, N):
    start = time.time()
    t = np.linspace(t0, tf, N+1)
    h = (tf - t0) / N
    y = np.zeros((N+1, len(x0)))

    # Initialisation : 1er pas avec Euler
    _ , y_euler,_ = euler_explicite(f, x0, t0, t0+h, 1)
    y[0] = x0
    y[1] = y_euler[1]
    for i in range(1, N):
        t[i+1] = t[i] + h
        y[i+1] = y[i] + h/2 * (3*f(t[i], y[i]) - f(t[i-1], y[i-1]))
    stop = time.time()
    final_time = stop-start
    return t, y, final_time

def RungeKutta2_explicite(f, x0, t0, tf, N):
    start = time.time()
    t = np.linspace(t0, tf, N+1)
    h = (tf - t0) / N
    y = np.zeros((N+1, len(x0)))
    y[0] = x0
    for i in range(N):
        t[i+1] = t[i] + h
        k1 = h * f(t[i],y[i])
        k2 = h* f(t[i]+h,y[i]+k1)
        y[i+1] = y[i] + 1/2 * (k1+k2)
    stop = time.time()
    final_time = stop-start
    return t,y, final_time



def graphique(Ca,Ct,Cs,t,methode):
    plt.plot(t, Ca, label='CA(t) (Atmosphère)')
    plt.plot(t, Ct, label='CT(t) (Arbres)')
    plt.plot(t, Cs, label='CS(t) (Sols)')
    #plt.plot(sol.t,somme)
    plt.xlabel('Temps')
    plt.ylabel('Quantité de carbone (Gt)')
    plt.legend()
    plt.title('Évolution des stocks de carbone avec '+methode)
    plt.grid()
    plt.show()



############## TESTS ##############

# Conditions initiales
x0 = [3250, 500, 5500]  # CA0, CT0, CS0  
t0=0
tf=600
N=6000


# Test Euler Explicite

t_euler, y_euler, time_euler = euler_explicite(systeme, x0, t0, tf, N)
CA, CT, CS = y_euler[:, 0], y_euler[:, 1], y_euler[:, 2]

graphique(CA,CT,CS,t_euler,"euler explicite")


# Test Adams Bashforth

t_AB, y_AB, time_AB = AdamsBashforth(systeme, x0, t0, tf, N)
CA_AB, CT_AB, CS_AB = y_AB[:, 0], y_AB[:, 1], y_AB[:, 2]

graphique(CA_AB,CT_AB,CS_AB,t_AB,"Adams Bashforth")


# Test Runge Kutta 2 explicite

t_RG, y_RG, time_RG = RungeKutta2_explicite(systeme, x0, t0, tf, N)
CA_RG, CT_RG, CS_RG = y_RG[:, 0], y_RG[:, 1], y_RG[:, 2]

graphique(CA_RG,CT_RG,CS_RG,t_RG,"Runge Kutta 2 explicite")


print("temps Euler Explicite : ",time_euler)
print("temps AdamsBashforth : ",time_AB)
print("temps RungeKutta : ",time_RG)



# Tests avec différents paramètres

def systeme_para(alpha, beta, gamma, delta, K):
    def systeme(t, y):
        CA, CT, CS = y
        S = alpha * CT * (1 - CT/K)
        dCA = -S + beta * CT + delta * CS
        dCT = S - beta * CT - delta * CT - gamma * CT
        dCS = gamma * CT - delta * CS + delta * CT
        return np.array([dCA, dCT, dCS])
    return systeme


def graph_para(liste,nom_parametre):
    for i in liste :
        if(nom_parametre == "alpha"):
            systeme_i = systeme_para(i,beta,gamma,delta,K)
        if(nom_parametre == "beta"):
            systeme_i = systeme_para(alpha,i,gamma,delta,K)
        if(nom_parametre == "gamma"):
            systeme_i = systeme_para(alpha,beta,i,delta,K)
        if(nom_parametre == "delta"):
            systeme_i = systeme_para(alpha,beta,gamma,i,K)
        if(nom_parametre == "K"):
            systeme_i = systeme_para(alpha,beta,gamma,delta,i)


        t_RG, y_RG, time_RG = RungeKutta2_explicite(systeme_i, x0, t0, tf, N)
        CA_RG, CT_RG, CS_RG = y_RG[:, 0], y_RG[:, 1], y_RG[:, 2]
        plt.subplot(1, 3, 1)
        plt.plot(t_RG, CA_RG, label=i)
        plt.title("CA(t)")
        plt.xlabel("Temps"); plt.ylabel("Quantité carbone (Gt)")

        plt.subplot(1, 3, 2)
        plt.plot(t_RG, CT_RG, label=i)
        plt.title("CT(t)")
        plt.xlabel("Temps"); plt.ylabel("Quantité carbone (Gt)")

        plt.subplot(1, 3, 3)
        plt.plot(t_RG, CS_RG, label=i)
        plt.title("CS(t)")
        plt.xlabel("Temps"); plt.ylabel("Quantité carbone (Gt)")
    plt.subplot(1,3,1)
    plt.legend()
    plt.grid()

    plt.subplot(1,3,2)
    plt.legend()
    plt.grid()

    plt.subplot(1,3,3)
    plt.legend()
    plt.grid()

    plt.suptitle("Effet du paramètre "+nom_parametre)
    plt.show()

# parametre alpha
para_alpha = [0.04, 0.5,1,10]
beta = 0.1
gamma = 0.03
delta = 0.01
K = 500

graph_para(para_alpha,"alpha")

# parametre beta
alpha = 0.04
para_beta = [0.001,0.1,5,10]
gamma = 0.03
delta = 0.01
K = 500

graph_para(para_beta,"beta")

# parametre gamma
alpha = 0.04
beta = 0.1
para_gamma = [0.03,0.8,5,15]
delta = 0.01
K = 500

graph_para(para_gamma,"gamma")

# parametre delta 
alpha = 0.04
beta = 0.1
gamma = 0.03
para_delta = [0.001,0.01,0.1,5]
K = 500

graph_para(para_delta,"delta")

# parametre K
alpha = 0.04
beta = 0.1
gamma = 0.03
delta = 0.01
para_K = [50,500,2000,3000]

graph_para(para_K,"K")

