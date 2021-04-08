#termometro.py
'''
import random

N = 99
mu = 0
sigma = 0.2
temp = 37.5

mediciones = []

for i in range(N):
    error = random.normalvariate(mu,sigma)
    mediciones.append(temp + error)

mediciones.sort()

maximo = max(mediciones)
minimo = min(mediciones)
promedio = sum(mediciones)/N
media = mediciones[49]

print(f'El valor maximo es {maximo:0.2f}°')
print(f'El valor minimo es {minimo:0.2f}°')
print(f'El valor promedio es {promedio:0.2f}°')
print(f'El valor medio es {media:0.2f}°')
'''
import random
import numpy as np

N = 999
mu = 0
sigma = 0.2
temp = 37.5

mediciones = []

for i in range(N):
    error = random.normalvariate(mu,sigma)
    mediciones.append(temp + error)

mediciones.sort()

maximo = max(mediciones)
minimo = min(mediciones)
promedio = sum(mediciones)/N
media = mediciones[int(N/2)]

print(f'El valor maximo es {maximo:0.2f}°')
print(f'El valor minimo es {minimo:0.2f}°')
print(f'El valor promedio es {promedio:0.2f}°')
print(f'El valor medio es {media:0.2f}°')

array = np.array(mediciones)
np.save("../Data/Temperaturas.npy",array)


