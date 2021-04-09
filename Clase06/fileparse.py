# fileparse.py

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    
    * nombre archivo: Se le pasa el archivo a parsear (ej: nombre_archivo = "archivo.csv").
    * select: Opcional (default=None), se le pasa una lista de nombres de las columnas a considerar. (ej: select = ['columna 1', 'columna 3']).
    * types: Opcional (default=None), se le pasa una lista con los tipos de datos que se quieren de cada columna (ej: select = [str, int]).
    * has_headers: Opcional (default=True), se le pasa has_headers=False si el archivo no contiene encabezado, entocnes la funcion devuelve lista de tuplas.
    
    '''
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
            
        registros = []
        for fila in filas:
            if not fila:
                continue
           
            if indices:
                fila = [fila[index] for index in indices]

            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)

            registros.append(registro)

    return registros