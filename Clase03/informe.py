#Informe.py

import csv

camion = []
precio = {}
costo_total=0.00
ganancia=0.00
balance=0.00

def leer_camion(nombre_archivo):
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    una lista con nombre, cajones y precio
    '''
    camion =[]
    lote = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(header, fila))
            try:
                camion.append(record)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
                print(record)
    return camion
    
def leer_precios(nombre_archivo):
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    un diccionario con nombre y precio
    '''
    precio = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precio[row[0]] = float(row[1])
            except IndexError:
                print(f"warning 2")
    return precio
    
#camion = leer_camion("../Data/camion.csv")
camion = leer_camion("../Data/fecha_camion.csv")
precio = leer_precios("../Data/precios.csv")

i=0
for i,row in enumerate(camion):
    try:
        costo_total += (int(camion[i]["cajones"]))*(float(camion[i]["precio"]))
        ganancia += (int(camion[i]["cajones"]))*(precio[(camion[i]["nombre"])])
    except KeyError:
        print(f"warning 3") 

balance=ganancia-costo_total
print(f"El costo total es de ${costo_total:0.2f}")
print(f"La ganacia total es de ${ganancia:0.2f}")
print(f"El balance es de ${balance:0.2f}  \n")
