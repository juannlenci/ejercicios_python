#estimar_pi.py

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N = 1000000    
estimacion = 0    

for i in range(N):
    x,y = generar_punto()
    if (x*x+y*y) < 1.0 :
        estimacion = estimacion + 1
        
pi = (estimacion*4)/N
print(pi)