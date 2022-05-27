import numpy as np
numeros= []
epsilon=0.0001
def cargoLista():
    with open("tp2_datos10.txt","r") as archivo:
        global numeros 
        numeros = archivo.readlines()
    for i in range(len(numeros)):
        numeros[i] = numeros[i].rstrip()
        numeros[i] = int(numeros[i])
    archivo.close()
    print(numeros)

def converge(act, ant):
    for i in range(len(numeros)):
        if(abs(act[i] - ant[i]) > epsilon):
            return False
    return True

def Prob_primera_recurrencia():
    global numeros
    retornos = np.zeros(len(numeros))  # array de retornos

    frecuenciaActual = np.zeros_like(retornos)  # array de prob
    frecuenciaAnterior = np.zeros_like(retornos)  # array de prob
    
    # total de retornos por simbolo
    total_retornos = 0
    # ultimos retornos valor discernible
    ultimo_retorno = -1
    t_actual = 0
    print(len(numeros))
    simboloActual = numeros[t_actual]
    simbolo = 0
    ultimo_retorno = t_actual
    total_retornos = total_retornos + 1
    
    while (t_actual+1 < len(numeros) or not converge(frecuenciaActual,frecuenciaAnterior )):
        t_actual += 1
        frecuenciaAnterior = frecuenciaActual
        #print("act ",t_actual,"len numeros", len(numeros))
        simboloActual = numeros[t_actual]
        cantPasos = t_actual - ultimo_retorno
        if(simboloActual == simbolo):   
            retornos[cantPasos] = retornos[cantPasos] + 1 
            ultimo_retorno = t_actual   
            total_retornos = total_retornos+1     
        frecuenciaActual[:] = np.divide(retornos[:], total_retornos)
    return frecuenciaActual

def Media_recurrencia():
    global numeros
    retornos = np.ones_like(numeros)*-1
    media = np.ones_like(retornos)
    t_actual = 0
    simboloActual = numeros[t_actual]
    while (t_actual+1 < len(numeros)):
       t_actual+=1
       simboloActual = numeros[t_actual]       
       retornos[simboloActual]+=1
    for i in range(len(numeros)):
       if(retornos[i] > 0):
           media[i] = t_actual / retornos[i]
    return media


cargoLista()
v = Prob_primera_recurrencia()
m = Media_recurrencia()
np.set_printoptions(precision=4)
print("recurrencia de  0 en n(",len(numeros),") pasos :\n" + str(v))
print("media de recurrencia de todos los simbolos:\n" + str(m))