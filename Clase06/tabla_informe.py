#Informe.py

import csv
camion = []
precio = {}
costo_total=0.00
ganancia=0.00
balance=0.00

def leer_camion(nombre_archivo):
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    una lista con nombre, cajones y precio
    '''
    camion =[]
    lote = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                lote = {"nombre" : row[0],"cajones": int(row[1]),"precio": float(row[2])}
                camion.append(lote)
            except ValueError:
                print(f"warning 1")
    return camion
    
def leer_precios(nombre_archivo):    
    '''
    Se le pasa el nombre del archivo a leer y devuelve
    un diccionario con nombre y precio
    '''
    precio = {}
    with open (nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precio[row[0]] = float(row[1])
            except IndexError:
                print(f"warning 2")
    return precio
    
def hacer_informe(lista_camion,dict_precios):
    '''
    Se le pasan lista de camion con nombre, cajones y precio, y
    diccionario de precios y devuelve una lista con el informe
    '''
    informe = []
    
    for n_fila, fila in enumerate(lista_camion):
        precios = (dict_precios[(camion[n_fila]["nombre"])])-lista_camion[n_fila]["precio"]
        fila_informe = (lista_camion[n_fila]["nombre"], lista_camion[n_fila]["cajones"], lista_camion[n_fila]["precio"], precios)
        informe.append(fila_informe)
    return informe

camion = leer_camion("../Data/camion.csv")
precio = leer_precios("../Data/precios.csv")

informe = hacer_informe(camion, precio)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
nombre_campo = (f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print (nombre_campo)
separacion = "---------- ---------- ---------- ----------"
print (separacion)

for nombre, cajones, precio, cambio in informe:
    signo_precio = "$ " + str(precio)
    print(f'{nombre:>10s} {cajones:>10d} {signo_precio:>10s} {cambio:>10.2f}')
