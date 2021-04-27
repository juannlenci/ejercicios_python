# fileparse.py

#%%

def parse_csv(filas, select = None, types = None, has_headers=True, silence_errors = False):
    '''
    Parsea un objeto o iterable que se comporte como un archivo, en una lista
    de registros.
    
    * filas:
        Se le pasa el objeto o iterable que se comporte como un archivo
        (ej: filas = ['Columna 1,Columna 2,Columna 3','1,2,3']
    * select:
        Opcional (default=None)
        se le pasa una lista de nombres de las columnas a considerar.
        (ej: select = ['columna 1', 'columna 3']).
    * types:
        Opcional (default=None)
        se le pasa una lista con los tipos de datos que se quieren de cada columna.
        El tamaño debe ser igual al de las columnas totales o seleccionadas.
        (ej: types = [str, int]).
    * has_headers:
        Opcional (default=True)
        se le pasa has_headers=False si el archivo no contiene encabezado,
        entonces la funcion devuelve lista de tuplas.
    * silence_errors:
        Opcional (default=False)
        se le pasa silence_errors=True para silencial los errores.
        
    OBS: Si se quiere parsear un archivo, se debe abrir en programa antes:
    
    with open(nombre_archivo, encoding="utf8") as file:
        lista_de_registros = parse_csv(file)    
        
    '''
    
    registros = []      
    indices = []    

    for n_fila, fila in enumerate(filas, start=1):  
   
        fila = fila.strip().split(",") #Separo por comas
        if has_headers and n_fila == 1:
            encabezados = fila

            if select:
                try:
                    if has_headers:
                        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                        encabezados = select
                    else:
                        raise RuntimeError("Para seleccionar, necesito encabezados.")
                        
                except Exception as e:
                    if silence_errors == False:
                        print('Hubo un error. Porque...', e)
                    select = None
                    indices = []
            else:
                indices = []       

        else:
            try:
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
                if registro:
                    registros.append(registro)

    return registros
