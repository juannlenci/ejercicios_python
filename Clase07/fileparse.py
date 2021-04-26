# fileparse.py

#%%
# import csv

# def parse_csv(nombre_archivo, select = None, types = None, has_headers=True, silence_errors = False):
#     '''
#     Parsea un archivo CSV en una lista de registros.
    
#     * nombre archivo:
#         Se le pasa el archivo a parsear (ej: nombre_archivo = "archivo.csv").
#     * select:
#         Opcional (default=None)
#         se le pasa una lista de nombres de las columnas a considerar.
#         (ej: select = ['columna 1', 'columna 3']).
#     * types:
#         Opcional (default=None)
#         se le pasa una lista con los tipos de datos que se quieren de cada columna
#         (ej: types = [str, int]).
#     * has_headers:
#         Opcional (default=True)
#         se le pasa has_headers=False si el archivo no contiene encabezado, entocnes la funcion devuelve lista de tuplas.
#     * silence_errors:
#         Opcional (default=False)
#         se le pasa silence_errors=True para silencial los errores.
#     '''
#     with open(nombre_archivo, encoding="utf8") as f:
#         filas = csv.reader(f)               
 
#         # Lee los encabezados del archivo, Si ti tiene encabezados, los selecciono
#         if has_headers:
#             encabezados = next(filas)

#         if select:   
#             try:
#                 if has_headers:
#                     indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#                     encabezados = select
#                 else:
#                     #Levanto una excepcion
#                     raise RuntimeError("Para seleccionar, necesito encabezados.")
                    
#             except Exception as e:
#                 if silence_errors == False:
#                     print('Hubo un error. Porque...', e)
#                 select = None
#                 indices = []
#         else:
#             indices = []   
            
#         registros = []      
#         for n_fila, fila in enumerate(filas, start=1):  

#             try:
#                 ex = False
#                 if not fila:
#                     continue
                
#                 if indices:    
#                     fila = [fila[index] for index in indices]

#                 if types:
#                     fila = [func(val) for func, val in zip(types, fila)]
                    
#                 if has_headers:
#                     registro = dict(zip(encabezados, fila))
#                 else:
#                     registro = tuple(fila)
                    
#             except ValueError as e:
#                 ex = True
#                 if silence_errors == False:
#                     print(f'Fila {n_fila}: No pude interpretar {fila}\n por... {e}')

#             if ex==False:
#                 registros.append(registro)

#     return registros
#%%
import csv

def parse_csv(file, select = None, types = None, has_headers=True, silence_errors = False):
    '''
    Parsea un  archivo, objeto o iterable  en una lista de registros.
    
    parse_csv(file, select, types, has_headers, silence_errors)
    
    * file:
        Se le pasa el archivo, objeto o iterable a parsear (ej: file = "archivo.csv").
    * select:
        Opcional (default=None)
        se le pasa una lista de nombres de las columnas a considerar.
        (ej: select = ['columna 1', 'columna 3']).
    * types:
        Opcional (default=None)
        se le pasa una lista con los tipos de datos que se quieren de cada columna
        (ej: types = [str, int]).
    * has_headers:
        Opcional (default=True)
        se le pasa has_headers=False si el archivo no contiene encabezado, entocnes la funcion devuelve lista de tuplas.
    * silence_errors:
        Opcional (default=False)
        se le pasa silence_errors=True para silencial los errores.
    '''
    #with open(nombre_archivo, encoding="utf8") as f:
    #    filas = csv.reader(f)               

    # Si tiene encabezados, los selecciono
    if has_headers:
        encabezados = file[0].split(",")

    if select:   
        try:
            if has_headers:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                #Levanto una excepcion
                raise RuntimeError("Para seleccionar, necesito encabezados.")

        except Exception as e:
            if silence_errors == False:
                print('Hubo un error. Porque...', e)
            select = None
            indices = []
    else:
        indices = []   

    registros = []
    n_fila = 0
    for fila in file:
        if has_headers and n_fila==0: #Si tiene header, no lo leo
            n_fila += 1 
        else:
            try:
                fila = fila.split(",")
                ex = False
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
    
            except ValueError as e:
                ex = True
                if silence_errors == False:
                    print(f'Fila {n_fila}: No pude interpretar {fila}\n por... {e}')
    
            if ex==False:
                registros.append(registro)
            n_fila += 1 


        
    return registros