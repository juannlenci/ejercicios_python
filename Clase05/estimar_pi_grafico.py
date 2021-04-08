import matplotlib.pyplot as plt
import random

def generar_punto():
    x = random.random()

N=10000
M=0
Xi = []
Yi = []
Xo = []
Yo = []

for i in range(N):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        Xi.append(x)
        Yi.append(y)
        M+=1
    else:
        Xo.append(x)
        Yo.append(y)
        
print(f'pi ~  {4*M/N:.5f}')

#%%
plt.clf()
plt.scatter(Xi,Yi,s=1)
plt.scatter(Xo,Yo,s=1)