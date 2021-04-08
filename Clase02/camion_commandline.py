# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    costo_total = 0.00
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                costo_total = costo_total+(float(row[1])*float(row[2]))
            except ValueError:
                print(f"warning")
    return costo_total
    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo = costo_camion (nombre_archivo)
#costo = costo_camion ("../Clase02/missing.csv")
print(f'Costo total: ${costo:0.2f}')
