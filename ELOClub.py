#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#################################
#### Definicion de funciones ####
#################################

def calculo_variacion (resultado_esperado,resultado_obtenido,k):
    ''' Calculo la variacion de ELO teniendo en cuenta el resultado obtenido, el esperado y el coeficiente k '''
    Inc_Rating = (resultado_obtenido - resultado_esperado) * k
    return Inc_Rating

def calculo_Pd (D1, D2):
    ''' Calculo el porcentaje esperado del jugador frente a la media de sus rivales
    :param int D1: Rating del jugador
    :param int D2: Rating del rival (o media de los rivales)
    '''
    return 1 / (1 + 10 ** ((D2 - D1) / 400))


######################################

K = 10.0
D1 = input ("Introduzca rating del jugador: ")
D2 = input ("Introduzca rating medio de los rivales: ")
n = input ("Introduzca numero de partidas: ")
p = input ("Introduzca puntos obtenidos: ")

Pd = calculo_Pd(int(D1), int(D2));
Ar = calculo_variacion (Pd * float (n), float (p), K) #Variacion de rating --> Ar

print ('\n\nEl jugador tenia un porcentaje esperado de ' + str (Pd) )
print ('El jugador tenia una puntuacion esperada de ' + str ( round(Pd * float (n),1) ) + ' y ha obtenido ' + str(float(p)) + ' puntos')
print ('\nEl jugador ha obtenido una variacion de ELO de ' + str(Ar) + ' --> ' + str(round (Ar,0)) )
input()
