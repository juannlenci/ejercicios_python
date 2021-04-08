#Informe.py

import csv
camion = []
precio = {}
costo_total=0.00
ganancia=0.00
balance=0.00

def leer_camion(nombre_archivo):
    camion =[]
    lote = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                lote = {"nombre" : row[0],"cajones": int(row[1]),"precio": float(row[2])}
                camion.append(lote)
            except ValueError:
                print(f"warning 1")
    return camion
    
def leer_precios(nombre_archivo):
    precio = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precio[row[0]] = float(row[1])
            except IndexError:
                print(f"warning 2")
    return precio
    
camion = leer_camion("../Data/camion.csv")
precio = leer_precios("../Data/precios.csv")

i=0
for row in camion:
    try:
        costo_total += (camion[i]["cajones"])*(camion[i]["precio"])
        ganancia += (camion[i]["cajones"])*(precio[(camion[i]["nombre"])])
    except KeyError:
        print(f"warning 3")
    i=i+1   
balance=ganancia-costo_total
print(f"El costo total es de ${costo_total:0.2f}")
print(f"La ganacia total es de ${ganancia:0.2f}")
print(f"El balance es de ${balance:0.2f}  \n")
