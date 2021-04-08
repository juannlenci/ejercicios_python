#arboles.py

import csv

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



#H =[int(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]
#T =[(int(arbol['altura_tot']),int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]
    