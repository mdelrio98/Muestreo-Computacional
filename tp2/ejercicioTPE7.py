import numpy as np
numeros= []

total = 0
def cargoLista():
    with open("Beethoven.txt","r") as archivo:
        global numeros 
        numeros = archivo.readlines()
        m_prob = np.zeros((len(numeros),2))
        for i in range(len(numeros)):
            if(not np.any(m_prob[:,0]==numeros[i])):
                m_prob[i][0] = numeros[i].rstrip()
                m_prob[i][0] = int(numeros[i])
            m_prob[i][1] = numeros.count(m_prob[i][0])/ len(numeros)
    archivo.close()
    print(m_prob)                                                                                                                   


cargoLista()