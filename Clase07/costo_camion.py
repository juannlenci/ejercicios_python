#!/usr/bin/env python3

#%%costo_camion.py
from informe import leer_camion

def costo_camion(nombre_archivo):
    costo_total = 0
    camion = leer_camion(nombre_archivo)
    for fila in camion:
        costo_total = costo_total + (fila["cajones"]*fila["precio"])
    print(f'Costo total: ${costo_total:0.2f}')
    return

def main(parametros):
    nombre_archivo = parametros[1]
    costo_camion(nombre_archivo)
    return
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]}' 'archivo_camion')
    main(sys.argv)
