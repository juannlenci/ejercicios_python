#!/usr/bin/env python3

#%%Informe.py
from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    una lista con nombre, cajones y precio
    '''
    with open(nombre_archivo, encoding="utf8") as file:
            camion = parse_csv(file, select=["nombre","cajones","precio"], types=[str, int, float])

    return camion

def leer_precios(nombre_archivo):    
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    un diccionario con nombre y precio
    '''
    with open(nombre_archivo, encoding="utf8") as file:
            precio = dict(parse_csv(file, types=[str, float], has_headers=False))

    return precio

def hacer_informe(lista_camion,dict_precios):
    '''
    Se le pasan lista de camion con nombre, cajones y precio, y
    diccionario de precios y devuelve una lista con el informe
    '''
    informe = []
    
    for n_fila, fila in enumerate(lista_camion):
        precios = (dict_precios[(lista_camion[n_fila]["nombre"])])-lista_camion[n_fila]["precio"]
        fila_informe = (lista_camion[n_fila]["nombre"], lista_camion[n_fila]["cajones"], lista_camion[n_fila]["precio"], precios)
        informe.append(fila_informe)
    return informe

def imprimir_informe(informe):
    '''
    Se le pasan informe generado e imprime la tabla
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    nombre_campo = (f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print (nombre_campo)
    separacion = "---------- ---------- ---------- ----------"
    print (separacion)
    
    for nombre, cajones, precio, cambio in informe:
        signo_precio = "$ " + str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {signo_precio:>10s} {cambio:>10.2f}')
    return

def main(parametros):
    '''
    Se le pasan los parametros nombre de programa, nombre de archivos de camion
    y de precios, crea el informe y lo imprime
    '''
    nombre_archivo_camion = parametros[1]
    nombre_archivo_precios = parametros[2]
    
    camion = leer_camion(nombre_archivo_camion)
    precio = leer_precios(nombre_archivo_precios)
    
    informe = hacer_informe(camion, precio)
    imprimir_informe(informe)
    return

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    main(sys.argv)

