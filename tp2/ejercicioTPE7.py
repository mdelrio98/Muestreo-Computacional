import numpy as np
numeros= []
def cargoLista():
    with open("tp2_datos10.txt","r") as archivo:
        global numeros 
        numeros = archivo.readlines()
    for i in range(len(numeros)):
        numeros[i] = numeros[i].rstrip()
        numeros[i] = int(numeros[i])
    archivo.close()
    print(numeros)
