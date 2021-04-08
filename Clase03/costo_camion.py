#Costo_camion.py
import csv

def costo_camion(nombre_archivo):
    '''
    Se le pasa en nombre del archivo y 
    devuelve el costo total del camion
    '''
    costo_total = 0.00
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(header, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

#costo = costo_camion ("../Data/missing.csv")
costo = costo_camion ("../Data/fecha_camion.csv")
#costo = costo_camion ("../Data/camion.csv")
print(f'Costo total: ${costo:0.2f}')
