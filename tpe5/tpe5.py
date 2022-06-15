import math as ma
from random import *
epsilon = 0.000001
                #x1  x2
prob_ingreso = [1/3,2/3]
                        #x1        #x2
condicional_beta1 = [0.95,0.05],[0.05,0.95]
condicional_beta2 = [0.5,0.5],[0.5,0.5]

# def prob_marginal_Y(prob_ingreso, matriz_cond):
#     resultado=[]
#     for i in range(len(prob_ingreso)): #dejo fija la fila de la matriz
#         for j in range(2):
#             resultado[i]+=(prob_ingreso[i] * matriz_cond[i][j]) 
#     return resultado
#     #P(Y1)= P(X1)*P(Y1/X1) + P(X2)*P(Y1/X2)

def ruido_individual (matriz, n):
    result = 0
    for i in range(len(matriz)):
        result = result + (-(matriz[n][i]) * ma.log(matriz[n][i],2))
    return result

def ruido_canal(prob_ingreso, matriz_cond):
    ruido_resultado = 0
    for i in range(len(prob_ingreso)):
        ruido_indv = ruido_individual(matriz_cond,i)
        proba_marginal= prob_ingreso[i]
        ruido_resultado += (ruido_indv*proba_marginal)
    return ruido_resultado  

def emision_simbolo():
    r = random()
    if (r < 1/3):
        return 0
    else: 
        return 1

def converge(act, ant):
    if(abs(act - ant) > epsilon):
        return False
    return True

def pasarporcanal(x,cond):
    r=random()
    if(x==0):
        if(r < cond[0][0]): 
            return 0 
        else:
            return 1
    if(x==1):
        if(r < cond[1][0]): 
            return 0
        else: 
            return 1

def retransmision_estrategia1(matriz_cond):
    errores=0
    error_ant=-1
    error_act=0.0
    n=0
    while(not converge(error_act,error_ant)) or (n < 100000):
        x= emision_simbolo()# emision 1 vez
        sumar_unos_salida=0
        for i in range(3):#emito los 3 simbolos            
            y = pasarporcanal(x,matriz_cond)
            sumar_unos_salida = sumar_unos_salida + y #si x=1 y tengo 110 no hay error en la salida
        if  ((x==0 and sumar_unos_salida>=2) or (x==1 and sumar_unos_salida<=1)):#si hay error lo logea
            errores+=1 #determino si fue error esta secuencia
        n+=1
        error_ant=error_act
        error_act = errores/n     
    return error_act       


def retransmision_estrategia2(matriz_cond):
    errores=0
    error_ant=-1
    error_act=0.0
    n=0
    while(not converge(error_act,error_ant)) or (n < 100000):
        x= emision_simbolo()# emision 1 vez
        sumar_unos_salida=0
        for i in range(3):#emito los 3 simbolos            
            y = pasarporcanal(x,matriz_cond)
            sumar_unos_salida = sumar_unos_salida + y 
        if  ((x==0 and sumar_unos_salida != 0) or (x==1 and sumar_unos_salida != 3)):#si hay error lo logea
            errores+=1 #determino si fue error esta secuencia
        n+=1
        error_ant=error_act
        error_act = errores/n     
    return error_act     
    
    
def main():
    ruido_canal1= ruido_canal(prob_ingreso, condicional_beta1)
    ruido_canal2= ruido_canal(prob_ingreso, condicional_beta2)
    print("--------------------------------")
    print("ruido canal 1: ",ruido_canal1)
    print("ruido canal 2: ",ruido_canal2)
    c1_marg_Y1 = (prob_ingreso[0]* condicional_beta1[0][0]) + (prob_ingreso[1]* condicional_beta1[0][1])
    c1_marg_Y2 = (prob_ingreso[0]* condicional_beta1[1][0]) + (prob_ingreso[1]* condicional_beta1[1][1])
    c2_marg_Y1 = (prob_ingreso[0]* condicional_beta2[0][0]) + (prob_ingreso[1]* condicional_beta2[0][1])
    c2_marg_Y2 = (prob_ingreso[0]* condicional_beta2[1][0]) + (prob_ingreso[1]* condicional_beta2[1][1])
    print("--------------------------------")
    print("probabilidad marginal Y1 canal 1 ",c1_marg_Y1)
    print("probabilidad marginal Y2 canal 1 ",c1_marg_Y2)
    print("probabilidad marginal Y1 canal 2 ",c2_marg_Y1)
    print("probabilidad marginal Y2 canal 2 ",c2_marg_Y2)
    entropiaY= (-c1_marg_Y1 * ma.log(c1_marg_Y1,2)) + (-c1_marg_Y2 * ma.log(c1_marg_Y2,2))
    entropiaYc2 = (-c2_marg_Y1 * ma.log(c2_marg_Y1,2)) + (-c2_marg_Y2 * ma.log(c2_marg_Y2,2))
    infomutua_c1 = entropiaY - ruido_canal1
    infomutua_c2 = entropiaYc2 - ruido_canal2
    print("--------------------------------")
    print("Informacion mutua canal 1: ",infomutua_c1) 
    print("Informacion mutua canal 2: ",infomutua_c2)
    errorc1=retransmision_estrategia1(condicional_beta1)
    errorc2=retransmision_estrategia1(condicional_beta2)
    print("--------------------------------")
    print("Estrategia 1")# ESTRATEGIA 1 SE MANTIENE EL VALOR DE ERROR
    print("Prob error canal 1: ",errorc1)
    print("Prob error canal 2: ",errorc2)
    errorc1est2=retransmision_estrategia2(condicional_beta1)
    errorc2est2=retransmision_estrategia2(condicional_beta2)
    print("--------------------------------")
    print("Estrategia 2")# ESTRATEGIA 2 SE EMPEROA EL VALOR DE ERROR
    print("Prob error canal 1: ",errorc1est2)
    print("Prob error canal 2: ",errorc2est2)
    
main()