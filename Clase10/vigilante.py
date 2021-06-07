# -*- coding: utf-8 -*-
# vigilante.py
"""
Created on Fri May 21 00:36:07 2021

@author: Juannlenci
"""

#%%
# import os
# import time

# f = open('../Data/mercadolog.csv')
# f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.5)   # Esperar un rato y
#         continue          # vuelve al comienzo del while
#     fields = line.split(',')
#     nombre = fields[0].strip('"')
#     precio = float(fields[1])
#     volumen = int(fields[2])
#     if volumen > 1000:
#         print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

#%%
# import os
# import time

# def vigilar(nombre_archivo):
#     f = open(nombre_archivo)
#     f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
#     while True:
#         line = f.readline()
#         if line == '':
#             time.sleep(0.5)   # Esperar un rato y
#             continue          # vuelve al comienzo del while
#         fields = line.split(',')
#         nombre = fields[0].strip('"')
#         precio = float(fields[1])
#         volumen = int(fields[2])
#         lines = nombre, precio, volumen
#         yield  lines
#%%   10.6
# import os
# import time

# def vigilar(nombre_archivo):
#     f = open(nombre_archivo)
#     f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
#     while True:
#         line = f.readline()
#         if line == '':
#             time.sleep(0.5)   # Esperar un rato y
#             continue          # vuelve al comienzo del while
#         yield line   
 
# if __name__ == '__main__':
#     for line in vigilar('../Data/mercadolog.csv'):
#         fields = line.split(',')
#         nombre = fields[0].strip('"')
#         precio = float(fields[1])
#         volumen = int(fields[2])
#         if volumen > 1000:
#             print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
#%% 10.7
import os
import time

def vigilar(nombre_archivo):
    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line   

if __name__ == '__main__':
    import informe

    camion = informe.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')