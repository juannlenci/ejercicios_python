#arboles.py

import csv

arboles =[]
especies =[]
ejemplares = {}

def leer_parque(nombre_archivo, parque):
    '''
    Se le pasa nombre de archivo y parque y
    devuelve unas lista con los datos de cada
    arbol del parque elegido
    '''
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
    '''
    Toma una lista de arboles de un parque y
    devuelve conjunto de especies que figuran
    en la lista
    '''
    especies_totales =[]
    especie=set(especies_totales)
    for n_fila, fila in enumerate(lista_arboles, start=0):
        especie_aux=(lista_arboles[n_fila]["nombre_com"])
        especie.add(especie_aux)
    return especie
    
def contar_ejemplares(lista_arboles):
    '''
    Toma una lista de arboles de un parque y
    devuelve un diccionario en el que las especies 
    sean las claves y tengan como valores asociados
    la cantidad de ejemplares en esa especie en la lista dada.
    '''
    ejemplar =[]
    especie = especies(lista_arboles)
    
    #Genero lista de especies
    ejemplar = list(especie)
    #Genero lista de ceros que voy a usar como contadores    
    cont = [0]*(len(ejemplar))
    #Genero diccionario con clave especies y cantidad inicial=0
    ejemplares = dict(zip(ejemplar, cont))

    for n_fila, fila in enumerate(lista_arboles, start=0):
        #la magia
        ejemplares[(lista_arboles[n_fila]["nombre_com"])] += 1
    return ejemplares

def obtener_alturas(lista_arboles, especie):
    '''
    Toma una lista de arboles de un parque y una especie y
    devuelve una lista con las alturas de los ejemplares
    de esa especie en la lista.
    '''
    alturas =[]
    for n_fila, fila in enumerate(lista_arboles, start=0):
        if (lista_arboles[n_fila]["nombre_com"]) == especie:
            alturas.append(float(lista_arboles[n_fila]["altura_tot"]))
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    '''
    Toma una lista de arboles de un parque y una especie y
    devuelve una lista con las inclinaciones de los ejemplares
    de esa especie en la lista.
    '''
    inclinaciones =[]
    for n_fila, fila in enumerate(lista_arboles, start=0):
        if (lista_arboles[n_fila]["nombre_com"]) == especie:
            inclinaciones.append(int(lista_arboles[n_fila]["inclinacio"]))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    '''
    Toma una lista de arboles de un parque y
    devuelve la especia que tiene el ejemplar
    mas inclinado y su inclinacion.
    '''
    esp_inclinada = []
    especie = list(especies(lista_arboles))
    cont=0
    
    for n_fila, fila in enumerate(especie, start=0):
        inclinaciones = obtener_inclinaciones(lista_arboles,especie[n_fila])
        if (max(inclinaciones) > cont):
            name = especie[n_fila]
            cont = max(inclinaciones)
    
    esp_inclinada = [name,cont]
    return esp_inclinada

def especie_promedio_mas_inclinada(lista_arboles):
    '''
    Toma una lista de arboles de un parque y
    devuelve la especie que en promedio tiene
    la mayor inclinación y el promedio calculado.
    '''
    prom_inclinada = []
    
    especie = list(especies(lista_arboles))
    
    cont=0
    
    for n_fila, fila in enumerate(especie, start=0):
        inclinaciones = obtener_inclinaciones(lista_arboles,especie[n_fila])
        promedio = (sum(inclinaciones))/(len(inclinaciones))
        if (promedio > cont):
            name = especie[n_fila]
            cont = promedio
    
    prom_inclinada = [name,cont]
    return prom_inclinada

    
#%%
#Leer Archivo
parque = "GENERAL PAZ"
arboles = leer_parque ("../Data/arbolado-en-espacios-verdes.csv",parque)
print(f"En el parque {parque} hay un total de {len(arboles)} arboles")

#%%
#Especies
especie = especies(arboles)
print(f"En el parque {parque} hay un total de {len(especie)} especies")

#%%
#Ejemplares
ejemplares = contar_ejemplares(arboles)
especies_a_mostrar= 5;
#Imprimir Ejemplares
#(No me salio usando el most_common e invente esta forma)
ejemplares_list = list(zip(ejemplares.values(), ejemplares.keys()))
ejemplares_list.sort(reverse=True)
print(f"En el parque {parque} las {especies_a_mostrar} Especies mas comunes son:")

headers = ('Especie', 'Cant.')
nombre_campo = (f'{headers[0]:>20s} {headers[1]:^5s}')
print (nombre_campo)
separacion = "-------------------- -----"
print (separacion)

for n_fila, fila in enumerate(ejemplares_list, start=0):
    print(f"{ejemplares_list[n_fila][1]:>20s} {ejemplares_list[n_fila][0]:^5d}") 
    
    if n_fila == especies_a_mostrar-1:
        break

#%%
#Alturas

arbol_altura = "Jacarandá" 
alturas = obtener_alturas(arboles,arbol_altura)
print (f"En el parque {parque} la altura maxima de {arbol_altura} es de {max(alturas)} mts")
promedio = (sum(alturas))/(len(alturas))
print (f"En el parque {parque} la altura promedio de {arbol_altura} es de {promedio:0.2f} mts")

#%%
#Inclinaciones

arbol_inclinacion = "Jacarandá" 
inclinaciones = obtener_inclinaciones(arboles,arbol_inclinacion)
print (f"En el parque {parque} la inclinacion maxima de {arbol_inclinacion} es de {max(inclinaciones)}°")

#%%
#Especie mas inclinada

esp_inclinada = especimen_mas_inclinado(arboles)
print (f"En el parque {parque} la inclinacion maxima es de la especie {esp_inclinada[0]} con {esp_inclinada[1]}°")

#%%
#Especie mas inclinada promedio

prom_inclinada = especie_promedio_mas_inclinada(arboles)
print (f"En el parque {parque} la inclinacion promedio maxima es de la especie {prom_inclinada[0]} con {prom_inclinada[1]}°")

