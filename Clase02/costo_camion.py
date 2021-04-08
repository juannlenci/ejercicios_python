#Costo_camion.py
import csv

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
costo = costo_camion ("../Data/camion.csv")
#costo = costo_camion ("../Data/missing.csv")
print(f'Costo total: ${costo:0.2f}')
