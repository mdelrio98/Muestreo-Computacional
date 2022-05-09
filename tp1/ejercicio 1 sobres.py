from random import random
epsilon = 0.0001

def secFsifirstF():
    exitos = 0
    pruebas = 0
    prob_act = 0
    prob_ant = -1
    while (not converge(prob_ant,prob_act) or pruebas < 20):
        s1 = sacar_sobre()
        s2 = sacar_sobre()
        if s1 == 1 and s2 == 1:
            exitos=exitos+1
        pruebas=pruebas+1
        prob_ant = prob_act
        prob_act = exitos/pruebas
        #print("prob act",prob_act)
    return prob_act

def solounF():
    exitos = 0
    pruebas = 0
    prob_act = 0
    prob_ant = -1
    while (not converge(prob_ant,prob_act) or pruebas < 20):
        s1 = sacar_sobre()
        s2 = sacar_sobre()
        if (s1 == 1 and s2 == 0) or (s1 == 0 and s2 == 1):
            exitos=exitos+1
        pruebas=pruebas+1
        prob_ant = prob_act
        prob_act = exitos/pruebas
        #print("prob act",prob_act)
    return prob_act


def almenosunF():
    exitos = 0
    pruebas = 0
    prob_act = 0
    prob_ant = -1
    while (not converge(prob_ant,prob_act) or pruebas < 20):
        s1 = sacar_sobre()
        s2 = sacar_sobre()
        if s1 == 1 or s2 == 1:
            exitos=exitos+1
        pruebas=pruebas+1
        prob_ant = prob_act
        prob_act = exitos/pruebas
        #print("prob act",prob_act)
    return prob_act

def sacar_sobre():
    sobres_faciles = 3
    nsobres = 5
    r = random()
    if r < sobres_faciles/nsobres:
        return 1
    else:
        return 0

def converge(prob_ant,prob_act):
    if abs(prob_act - prob_ant) < epsilon:
        return True
    return False

x = almenosunF()
y = solounF()
z = secFsifirstF()
print ("A) ",x,"B)",y,"C)",z)



