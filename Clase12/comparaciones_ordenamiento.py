# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:51:12 2021

@author: User
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#%%BURBUJEO
def ord_burbujeo(lista, verbose=False):
    """Ordena una lista de elementos según el método de burbujeo.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    comps = 0 # inicializo en cero la cantidad de comparaciones

    for pasada in range(len(lista)-1,0,-1):
        if verbose:
            print("DEBUG: ", pasada)
        for i in range(pasada):
            comps+=1 #1 Comparacion en el IF de abajo
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            if verbose:
                print("DEBUG: ", lista)
    return comps
#%%INSERCION
def ord_insercion(lista, verbose=False):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comps = 0 # inicializo en cero la cantidad de comparaciones

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comps += 1
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        if verbose:
            print("DEBUG: ", lista)
    return comps

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
#%%SELECCION
def ord_seleccion(lista, verbose = False):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comps = 0 # inicializo en cero la cantidad de comparaciones

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p,comps = buscar_max(lista, 0, n, comps)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        if verbose:
            print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    return comps

def buscar_max(lista, a, b,comps):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        comps+=1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comps

#%%EXPERIMENTO
def generar_lista(N, seed):
    random.seed(seed)
    lista=[]
    for i in range (N):
        num=random.randint(1, 1000)
        lista.append(num)
    return lista


def experimento_seleccion_promedio(lista, k):
    comps_tot = 0
    for i in range(k):
            comps_tot += ord_seleccion(lista)
    comps_prom = comps_tot / k
    return comps_prom

def experimento_insercion_promedio(lista, k):
    comps_tot = 0
    for i in range(k):
            comps_tot += ord_insercion(lista)
    comps_prom = comps_tot / k
    return comps_prom

def experimento_burbujeo_promedio(lista, k):
    comps_tot = 0
    for i in range(k):
            comps_tot += ord_burbujeo(lista)
    comps_prom = comps_tot / k
    return comps_prom

def main():
    N = 256
    k = 100
    
    largo = np.arange(N) + 1
    comparaciones_seleccion = np.zeros(N)
    comparaciones_insercion = np.zeros(N)
    comparaciones_burbujeo = np.zeros(N)
    
    for i, n in enumerate(largo):
        seed=n
        lista = generar_lista(n ,seed) # genero lista de largo n
        comparaciones_seleccion[i] = experimento_seleccion_promedio(lista, k)
      
    for i, n in enumerate(largo):
        seed=n
        lista = generar_lista(n ,seed) # genero lista de largo n 
        comparaciones_insercion[i] = experimento_insercion_promedio(lista, k)
        
    for i, n in enumerate(largo):
        seed=n
        lista = generar_lista(n,seed) # genero lista de largo n
        comparaciones_burbujeo[i] = experimento_burbujeo_promedio(lista, k)

    plt.plot(largo,comparaciones_seleccion,'r--',label = 'Seleccion')
    plt.plot(largo,comparaciones_insercion, 'g',label = 'Insecion')
    plt.plot(largo,comparaciones_burbujeo, 'b',label = 'Burbujeo')

    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad")
    plt.legend()
#%%
if __name__ == '__main__':
    main()