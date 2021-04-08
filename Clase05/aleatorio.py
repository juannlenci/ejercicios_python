import random

#% 
#podemos simular que tiramos los dados muchas veces y ver cuántas
#de esas veces obtuvimos cinco dados iguales

def tirar():
    '''
    Devuelve lista de la tirada de 5 dados
    '''
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 

    return tirada

def es_generala(tirada):
    '''
    Devuelve TRUE si tirada de 5 dados son iguales
    '''

    for i in range(1,7): #del 1 al 6
        cant = tirada.count(i)
        if cant == 5:
            return True
    
    return False

N = 1000000  

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')