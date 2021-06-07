# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:47:44 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
#%%
def main():
    minx = 0
    maxx = 300
    
    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])
        
    a, b = ajuste_lineal_simple(superficie, alquiler)
    
    grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
    grilla_y = grilla_x*a + b
    
    #Errores
    errores = alquiler - (a*superficie + b)
    err=f'ECM: {(errores**2).mean():0.4f}'
    
    #Ploteo
    plt.scatter(x = superficie, y = alquiler, label="Datos")
    plt.title('precio_alquiler ~ superficie')
    plt.plot(grilla_x, grilla_y, c = 'green', label="Modelo")
    plt.xlabel('Superficie (en metros cuadrados)')
    plt.ylabel('Alquiler (en miles de pesos)')
    plt.legend(loc='upper left')
    
    plt.annotate(err,
                xy=(200,10),
                xycoords='data',
                xytext=(0, 0),
                textcoords='offset points',
                fontsize=16)
    plt.show()
   

    
    
if __name__ == '__main__':
    main()