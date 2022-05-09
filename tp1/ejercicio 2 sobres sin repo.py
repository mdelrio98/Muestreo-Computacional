from random import random
epsilon = 0.0001

def main():
    global sobres_faciles 
    sobres_faciles  = 3
    global nsobres 
    nsobres  = 5
    almenosunF()


def almenosunF():
    exitos = 0
    pruebas = 0
    prob_act = 0
    prob_ant = -1
    while (not converge(prob_ant,prob_act) or pruebas < 20):
        s1 = sacar_sobre()
        if s1 == 1:
            sobres_faciles=sobres_faciles-1
        else
            
        nsobres=nsobres-1
        s2 = sacar_sobre()
        if s1 == 1 or s2 == 1:
            exitos=exitos+1
        pruebas=pruebas+1
        prob_ant = prob_act
        prob_act = exitos/pruebas
        #print("prob act",prob_act)
    return prob_act

def sacar_sobre():
    r = random()
    if r < sobres_faciles/nsobres:
        return 1
    else:
        return 0

def converge(prob_ant,prob_act):
    if abs(prob_act - prob_ant) < epsilon:
        return True
    return False

x = main()
y = solounF()
z = secFsifirstF()
print ("A) ",x,"B)",y,"C)",z)