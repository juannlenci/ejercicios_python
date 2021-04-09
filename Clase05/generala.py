#generala.py

import random

def tirada_inicial():
    '''
    Devuelve lista de la tirada de 5 dados
    '''
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada


def num_dados(tirada):
    '''
    Recibe las tiradas, y devuelve los dados
    que más se repiten 
    '''
    #lista_cant devuelve la cantidad de dados que hay con un numero
    #y lo devuelve en el indice [numero-1]
    lista_cant = []
    for n,i in enumerate(range(1,7),start=0): #del 1 al 6
        lista_cant.append(tirada.count(i))
    
    #Hago diccionario qcuyas claves es el numero de dado
    #y su valor la cantidad de veces que salio, lo uso para checkear
    #dict_cant=dict(zip(range(1,7),lista_cant))
    
    cantidad = max(lista_cant)
    dado_max = (lista_cant.index(max(lista_cant)) + 1)
    
    dados_separados = [dado_max]*cantidad
    
    #print(dict_cant)
    #print(dados_separados)
    return dados_separados

def nueva_tirada(nueva_tirada):
    '''
    Recibe solo los dados separados y vuelve a tirar el resto
    devuelve lista con nueva tirada
    '''
    cant_tirada = 5 - len(nueva_tirada)
    for i in range(cant_tirada):
        nuevo_numero = random.randint(1,6)
        nueva_tirada.append(nuevo_numero)
        #print(nuevo_numero)
    return nueva_tirada


def es_generala(tirada):
    '''
    Recibe la tirada y devuelve True si tirada de
    5 dados son iguales
    '''
    for i in range(1,7): #del 1 al 6
        cant = tirada.count(i)
        if cant == 5:
            return True  
    return False
    
N = 1000000
G = 0
servida = 0

for i in range(N):
    tirada_1 = tirada_inicial()
    tirada_2 = (nueva_tirada(num_dados(tirada_1)))
    tirada_3 = (nueva_tirada(num_dados(tirada_2)))
    
    servida = servida + es_generala(tirada_1)
    G = G + es_generala(tirada_3)
    
    '''
    TESTEO
    if (es_generala(tirada_1))==1:
       print("SERVIDA", tirada_1)
    if (es_generala(tirada_3))==1:
        print(tirada_3)
    '''
    
prob1 = G/N
prob2 = servida/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob1:.6f}.')
print(f'Tiré {N} veces, de las cuales {servida} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob2:.6f}.')