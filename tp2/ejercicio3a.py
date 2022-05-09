#ejercicio 6 3a en montecarlo  inicial 0  prob en paso 1 2 y 3
from random import *
#import numpy as np
vInicial_acum = [0, 1, 1]
#                 0               1               2
prob_acum = [[0.25, 0.75, 1], [0.75, 1, 1], [0, 0.5, 1]]
epsilon = 0.000001
simbolos = 3

def converge(act, ant):
    for i in range(simbolos):
        if(abs(ant[i] - act[i]) < epsilon):
            return True
    return False

def sig_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        if (r < prob_acum[s_ant][i]):
            return i
    return -1

def Calcular_Prob():
    exitos = [0, 0, 0]  # cantidad de emisiones de cada paso 1 2 3
    V = [0, 0, 0]  # Vector de estado actual
    V_ant = [-1, 0, 0]  # Vector de estado anterior
    mensajes=1              # cantidad de mensajes emitidos
    T_MIN = 100000
    t3 = 0
    while not converge(V, V_ant) or (mensajes < T_MIN):
        #print("t3",t3)
        t2 = sig_symbol(t3)
        #print("t2",t2)
        t1 = sig_symbol(t2)
        #print("t1",t1)
        s = sig_symbol(t1)              
        #print("s",s)
        if(t3==0):# tiempo 0
            if(t2==0):
                exitos[0] += 1 # tiempo 1
            if(t1==0):
                exitos[1] += 1 # tiempo 2
            if(s==0):
                exitos[2] += 1 # tiempo 3
        mensajes += 1
        V_ant = V
        t2=t3
        t1=t2
        s=t1
        for i in range(len(V)):
            V[i] = exitos[i]/mensajes
    return V

v = Calcular_Prob()
print(v)