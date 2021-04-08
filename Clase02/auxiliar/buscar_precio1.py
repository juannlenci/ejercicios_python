#buscar_precio.py

import csv

def leer_precios(nombre_archivo):
    #camion =[]
    precio = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                precio[row[0]] = float(row[1])
                #camion.append(lote)
            except IndexError:
                print(f"warning")
    return precio

#precio=buscar_precio("Frambuesa")
#print(f'Costo: ${precio:0.2f}')
