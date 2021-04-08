# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:59:55 2021

@author: Juan Lenci
"""
#%%
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# figus_total = 670
# n_repeticiones = 100
# lista_figuritas = []


# def crear_album(figus_total):
#     album = np.zeros(figus_total, dtype=np.int64)
#     return album

# def album_incompleto(album):
#      return 0 in album
 
# def comprar_figu(figus_total):
#     figurita = random.randint(0,figus_total-1)
#     return figurita

# def cuantas_figus(figus_total):
#     cont = 0
#     album=crear_album(figus_total)
#     while album_incompleto(album):
#         figurita = comprar_figu(figus_total)
#         album[figurita] += 1
#         cont += 1
#     return cont

# for i in range(n_repeticiones):
#     contador = cuantas_figus(figus_total)
#     lista_figuritas.append(contador)

# print(f'{np.mean(lista_figuritas):0.2f}')
# #plt.hist(lista_figuritas,bins=25)
#%%
import random
import numpy as np
import matplotlib.pyplot as plt

figus_total = 670
n_repeticiones = 100
figus_paquete = 5
lista_paquetes = []


def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

def album_incompleto(album):
     return 0 in album

def comprar_paquete(figus_total, figus_paquete):
    figuritas = []
    for i in range(figus_paquete):
        figuritas.append(random.randint(0,figus_total-1))
    return figuritas

def cuantos_paquetes(figus_total, figus_paquete):
    cont_paquetes = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i] += 1
        cont_paquetes += 1
    return cont_paquetes

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

for i in range(n_repeticiones):
    contador = cuantos_paquetes(figus_total, figus_paquete)
    lista_paquetes.append(contador)
    
print(f'El promedio de paqietes comprados para llenar un album es: {np.mean(lista_paquetes):0.2f}')

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
