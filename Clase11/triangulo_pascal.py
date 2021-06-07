# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:28:31 2021

@author: User
"""

# -*- coding: UTF-8 -*-
 
# función para el calculo de pascal
# tiene que recibir el numero de lineas que tendra
def trianguloPascal(n):
 
    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]
 
    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):
        linea = [1]
 
        for j in range(0,len(lista[i])-1):
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        linea += [1]
        lista.append(linea)
    return lista

n=5
resultado = trianguloPascal(n)
 
