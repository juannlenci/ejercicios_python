#arboles.py

import csv
import numpy as np
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):
    '''
    Se le pasa nombre de archivo y devuelve una lista de
    diccionarios con los datos de cada arbol
    '''
    arboles =[]
    
    #El encoding="utf8" lo agrego para evitar "UnicodeDecodeError"
    with open (nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [ headers.index(ncolumna) for ncolumna in headers ]
        row = next(rows)
        arboles = [ { ncolumna: row[index] for ncolumna, index in zip(headers, indices) } for row in rows ]

    return arboles

def medidas_de_especies(especies,arboleda):
    '''
    Se le pasa lista de diccionarios con los datos de cada arbol
    y lista con especiaes y devuelve diccionario cuyas claves son las especies
    y sus valores es una lista de tuplas con alto y ancho de cada arbol de la
    especie.
    '''
    d ={}

    for n_especie, especie in enumerate(especies):
        T =[(int(arbol['altura_tot']),int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especies[n_especie]]
        d[especies[n_especie]] = T
    return d

arboleda = leer_arboles ("../Data/arbolado-en-espacios-verdes.csv")
especies = ['Eucalipto', 'Palo borracho rosado','Jacarandá']
diccionario = medidas_de_especies(especies,arboleda)

#%% Altos Jacarandas
h = np.array(diccionario["Jacarandá"])[:,0] #Selecciono solo alturas
d = np.array(diccionario["Jacarandá"])[:,1] #Selecciono solo diametros

plt.figure(1)
plt.hist(h,bins=25)
plt.xlabel("Altura [m]")
plt.ylabel("Cantidad")
plt.title("Histograma Altos Jacarandá")

#%% ScatterPlot 
colors = ["green","blue","red"]
for i, especie in enumerate(especies, start=0):
    altura = np.array(diccionario[especie])[:,0]
    diametro = np.array(diccionario[especie])[:,1]
    plt.figure(i+2)
    plt.scatter(diametro,altura,c=colors[i], alpha=.5, s=25, label=especie)
    plt.legend(loc='best', fontsize='small')
    plt.xlabel("Anchos [cm]")
    plt.ylabel("Altos [m]")
    plt.title(f"Relacion Altos-Diametros {especie}")

#%% ScatterPlot juntos
plt.figure(5)
plt.xlim(0 , 180)
plt.ylim(0 , 45)

for i, especie in enumerate(especies, start=0):
    altura = np.array(diccionario[especie])[:,0]
    diametro = np.array(diccionario[especie])[:,1]
    plt.scatter(diametro,altura,c=colors[i], alpha=.5, s=20, label=especie)
    plt.legend(loc='best', fontsize='x-small')
    plt.xlabel("Anchos [cm]")
    plt.ylabel("Altos [m]")
    plt.title("Relacion Altos-Diametros")
    
plt.show()
 