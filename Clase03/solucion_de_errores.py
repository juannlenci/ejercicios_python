#solucion_de_errores.py

#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de semantico tipo y estaba ubicado dentro del While.
#    Al colocar el ELSE: return False, solo revisa la primera letra de la palabra
# Lo corregi eliminando esa condicion y agregandola fuera del while, de esta forma si
#encuentra una a devuelve un Verdadero y sino, una vez terminada toda la palbra
# devuelve un falso
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        #else:
            #return False
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.2. Función tiene_a1()
#Comentario: El error era de tipo Sintax y estaba ubicado dentro del la funcion tiene_a.
#Falta de ":" en def, while e if. falta "==" en la comparacion del if y False en vez de "Falso"
#    A continuación va el código corregido

def tiene_a1(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a1('UNSAM 2020'))
print(tiene_a1('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error es de tipo, es necesario que lo que se pase sea un string
#El ejemplo no funciona en el caso de 1984 como Int.

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == "1":
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno("1984"))

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error es que la funcion suma no devuelve el valor C

def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.4. Función leer_camion()
#Comentario l definir registros = {} sólo una vez, fuera del loop,
#siempre estamos modificando el mismo, y al cambiarlo se actualizantambien
# sus referencias dentro del diccionario creado. Se solucioona definiendolo dentro del for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas: 
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)