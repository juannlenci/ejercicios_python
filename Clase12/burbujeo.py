# -*- coding: utf-8 -*-
#burbujeo.py
"""
Created on Thu Jun  3 13:11:32 2021

@author: Juannlenci
"""


def ord_burbujeo(lista, verbose=False):
    """Ordena una lista de elementos según el método de burbujeo.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    
    for pasada in range(len(lista)-1,0,-1):
        if verbose:
            print("DEBUG: ", pasada)
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            if verbose:
                print("DEBUG: ", lista)

"""
En este caso se realizan n-1 Pasadas, en la primera se realizan
n-1 comparaciones, en la segunda n-2 y asi hasta la ultima que
realiza 1 sola compracion. Por lo tanto 
T(N) ~ (N**2)/2 + N/2 - N ~ N^2
y en el peor de los casos realiza la misma cantidad de intercambios.
y en el mejor de los casos no se realiza intercambios.
"""

