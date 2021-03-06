# -*- coding: utf-8 -*-
# formato_tabla.py

"""
Created on Thu May 13 14:23:54 2021
@author: JLenci
"""

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
      
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
            
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print("<tr>", end='')
        for d in headers:
            print("<th>", end='')
            print(d, end='')
            print("</th>", end='')
        print("</tr>", end='')
        print()

    def fila(self, data_fila):
        print("<tr>", end='')
        for d in data_fila:
            print("<td>", end='')
            print(d, end='')
            print("</td>", end='')
        print("</tr>", end='')
        print()

def crear_formateador(fmt):
    if fmt == 'txt':
        return FormatoTablaTXT()
    elif fmt == 'csv':
        return FormatoTablaCSV()
    elif fmt == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    pass