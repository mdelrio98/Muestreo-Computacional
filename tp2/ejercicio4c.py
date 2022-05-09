#ejercicio 6 4c en montecarlo  
# Para cada símbolo, calcule la probabilidad que se emitan 2
#símbolos símbolos consecutivos iguales (en estado estacionario)

from random import *
vInicial_acum = [0, 1, 1]
#                 1               2              3
prob_acum = [[0.50, 1, 1], [0.33, 0.66, 1], [0, 1, 1]]
epsilon = 0.000001
simbolos = 3

def converge(act, ant):
    for i in range(simbolos):
        if(abs(ant[i] - act[i]) < epsilon):
            return True
    return False

def first_symbol():
    r = random()
    if (r <= 0.33):
        return 1
    if (r > 0.33 and r <= 0.66):
        return 2
    return 3

def sig_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        if (r < prob_acum[s_ant-1][i]):
            return i+1
    return -1

def Calcular_Prob():
    exitos = [0, 0, 0]  # cantidad de emisiones de cada simbolo 1 2 3
    V = [0, 0, 0]  # Vector de estado actual
    V_ant = [-1, 0, 0]  # Vector de estado anterior
    mensajes=1              # cantidad de mensajes emitidos
    T_MIN = 100000
    a = first_symbol()
    #print("a ",a)
    while not converge(V, V_ant) or (mensajes < T_MIN):
        s= sig_symbol(a)
        #print("a ",a)
        #print("s ",s)
        if(s==a):
            exitos[s-1]+=1
        mensajes += 1
        V_ant = V
        a=s
        for i in range(len(V)):
            V[i] = exitos[i]/mensajes
    return V

v = Calcular_Prob()
print(v)