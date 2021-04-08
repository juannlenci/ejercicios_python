#arboles.py

import csv
from pprint import pprint

arboles =[]
especies =[]
ejemplares = {}

def leer_parque(nombre_archivo, parque):
    arboles =[]
    #El encoding="utf8" lo agrego para evitar "UnicodeDecodeError"
    with open (nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        header = next(rows)
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(header, fila))
            try:
                if (record["espacio_ve"])==parque:
                    arboles.append(record)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return arboles
    
def especies(lista_arboles):
    especies_totales =[]
    especie=set(especies_totales)
    for n_fila, fila in enumerate(lista_arboles, start=0):
        especie_aux=(lista_arboles[n_fila]["nombre_com"])
        especie.add(especie_aux)
    return especie
    
def contar_ejemplares(lista_arboles):
    ejemplar =[]
    especie = especies(lista_arboles)
    
    #Genero lista de especies
    ejemplar = list(especie)
    #Genero lista de ceros que voy a usar como contadores    
    cont = [0]*(len(ejemplar))
    #Genero diccionario
    ejemplares = dict(zip(ejemplar, cont))

    for n_fila, fila in enumerate(lista_arboles, start=0):
        #la magia
        ejemplares[(lista_arboles[n_fila]["nombre_com"])] += 1
    return ejemplares

def obtener_alturas(lista_arboles, especie):
    alturas =[]
    for n_fila, fila in enumerate(lista_arboles, start=0):
        altura.append = (lista_arboles[n_fila]["altura"])
    return alturas

arboles = leer_parque ("../Data/arbolado-en-espacios-verdes.csv","GENERAL PAZ")
especie = especies(arboles)
ejemplares = contar_ejemplares(arboles)

#pprint(arboles)
print(f"El total de arboles: {len(arboles)}")
#pprint(especie)
print(f"El total de especies: {len(especie)}")

#Revisar para hacer con most_common
ejemplares_list = list(zip(ejemplares.values(), ejemplares.keys()))
ejemplares_list.sort(reverse=True)
print(f"Las Especies mas comunes son:")
print(f"Cant.   Especie")

#pprint(ejemplares_list)
for n_fila, fila in enumerate(ejemplares_list, start=0):
    print(ejemplares_list[n_fila])
    if n_fila == 5-1:
        break
 
 #SEGUIR CON ALTURAS