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
        headers = next(rows)
        
        select = ['nombre', 'cajones', 'precio']
        indices = [ headers.index(ncolumna) for ncolumna in select ]
        
        row = next(rows)
        camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]

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

camion = leer_camion('../Data/fecha_camion.csv')
costo = sum([ (int(s['cajones'])) * (float(s['precio'])) for s in camion ])

precios = leer_precios('../Data/precios.csv')
valor = sum([ (int(s['cajones'])) * precios[s['nombre']] for s in camion ])

balance=valor-costo
print(f"El costo total es de ${costo:0.2f}")
print(f"La ganacia total es de ${valor:0.2f}")
print(f"El balance es de ${balance:0.2f}  \n")
