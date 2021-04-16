#plot_bbin_vs_bsec.py

import random
import matplotlib.pyplot as plt
import numpy as np

#%%

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps
#%% REVISAR COMPARACIONES

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones

    if verbose:
        print(f'[DEBUG] izq |der |medio')
        
    l = len(lista)
    pos = -1 
    izq = 0
    der = l - 1
    
    
    #Antes que nada me fijo los extremos 
    if x <= lista[0]:
        pos = 0
        comps += 1 #suma solo la comparacion de este if
    elif x >= lista[l-1]:
        pos = l
        comps += 2 #suma la comparacion de este if y el primero
    else:
        comps += 2 #suma la comparacion de los 2 if anteriores

        while izq <= der:
            comps += 2 #suma la comparacion de los 2 if posteriores
            medio = (izq + der) // 2
            if verbose:
                print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
            if lista[medio] == x:
                pos = medio     # elemento encontrado!
                comps -= 1 #Resto 1 comparacion que no voy a hacer porq
                #Ya se encontro el elemento
                break
            elif lista[medio] > x:
                der = medio - 1 # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1 # descarto mitad izquierda    
                
    return pos, comps
#%%
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)
#%%
m = 10000
k = 1000
#%%
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

#%%Experimento Secuencial
largos_sec = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_sec = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos_sec):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)


#%%Experimento binario
largos_bin = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_bin = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos_bin):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos_sec,comps_promedio_sec,label = 'Búsqueda Secuencial')
plt.plot(largos_bin,comps_promedio_bin,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.xlim(0,30)
plt.ylim(0,30)

plt.legend()