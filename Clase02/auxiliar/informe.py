#Informe.py

import csv

def leer_camion(nombre_archivo):
    camion=[]
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
            except ValueError:
                print(f"warning")
    return camion
#costo = leer_camion ("../Data/camion.csv")
#costo = costo_camion ("../Data/missing.csv")
#print(f'Costo total: ${costo:0.2f}')
