# -*- coding: utf-8 -*-
#random_walk.py

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()
maximos = []
caminatas = []
N = 100000

for i in range(12):
    pasos = randomwalk(N)
    maximo = max(abs(pasos))
    maximos.append(maximo)
    caminatas.append(pasos)
minimo = min(maximos)
maximo = max(maximos)
otra_caminata = []

for caminata in caminatas:
    if max(abs(caminata)) == maximo:
       cam_max = caminata
    if max(abs(caminata)) == minimo:
       cam_min = caminata
       
fig = plt.figure()
plt.subplot(2, 1, 1) 
for caminata in caminatas:
   plt.plot(caminata)
plt.title('Caminatas')
plt.xticks([]) # saca las marcas
plt.subplot(2, 2, 3)
plt.plot(cam_max)
plt.title('Caminata Maxima')
plt.xticks([])
plt.subplot(2, 2, 4)
plt.plot(cam_min)
plt.title('Caminata Minima')
plt.xticks([])
plt.show()