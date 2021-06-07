# -*- coding: utf-8 -*-
"""
Created on Fri May 21 18:43:44 2021

@author: User
"""

# ticker.py

from vigilante import vigilar
import csv
import informe
import formato_tabla

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def imprimir_informe(data, formateador):
    '''
    Imprime adecuadamente una tabla de una lista de tuplas
    (nombre, cajones, precio, cambio).
    '''
    rowdata = [ str(data["nombre"]), str(data["precio"]), str(data["volumen"])]
    formateador.fila(rowdata)    

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt):
    formateador = formato_tabla.crear_formateador(fmt)
    camion = informe.leer_camion('../Data/camion.csv')
    filas = parsear_datos(vigilar('../Data/mercadolog.csv'))
    filas = filtrar_datos(filas, camion)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for fila in filas:
        imprimir_informe(fila, formateador)

if __name__ == '__main__':
    camion_file = '../Data/camion.csv'
    log_file = '../Data/mercadolog.csv'
    fmt = 'txt' #Puede ser "txt", "csv", "html"
    ticker(camion_file, log_file, fmt)