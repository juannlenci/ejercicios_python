#envido.py
import random

def envido31(cartas):
    '''
    Recibe 3 cartas y devuelve TRUE si envido es 31
    necesito 5 y 6 o 7 y 4 
    '''
    for i in range(3):
        if cartas[i][0] == 5: #Reviso q haya un 5
            for n in range(3):
                if cartas[n][0] == 6: #Reviso q haya un 6
                    if cartas[i][1] == cartas[n][1]: #Reviso q sean del mismo palo
                        #print(cartas)
                        return True
        if cartas[i][0] == 7: #Reviso q haya un 7
            for n in range(3):
                if cartas[n][0] == 4: #Reviso q haya un 4
                    if cartas[i][1] == cartas[n][1]: #Reviso q sean del mismo palo
                        #print(cartas)
                        return True  
    return False

def envido32(cartas):
    '''
    Recibe 3 cartas y devuelve TRUE si envido es 32
    necesito 7 y 5 
    '''
    for i in range(3):
        if cartas[i][0] == 7: #Reviso q haya un 7
            for n in range(3):
                if cartas[n][0] == 5: #Reviso q haya un 5
                    if cartas[i][1] == cartas[n][1]: #Reviso q sean del mismo palo
                        #print(cartas)
                        return True
    return False
    
def envido33(cartas):
    '''
    Recibe 3 cartas y devuelve TRUE si envido es 32
    necesito 7 y 6 
    '''
    for i in range(3):
        if cartas[i][0] == 7: #Reviso q haya un 7
            for n in range(3):
                if cartas[n][0] == 6: #Reviso q haya un 6
                    if cartas[i][1] == cartas[n][1]: #Reviso q sean del mismo palo
                        #print(cartas)
                        return True
    return False
    
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

#print(naipes)
#cartas = (random.sample(naipes,k=3))

N = 1000000
E31 = 0
E32 = 0
E33 = 0

for i in range(N):
    cartas = (random.sample(naipes,k=3))
    E31 = E31 + envido31(cartas)
    E32 = E32 + envido32(cartas)
    E33 = E33 + envido33(cartas)
    
prob31 = E31/N
prob32 = E32/N
prob33 = E33/N
print(f'Reparti {N} veces')
print(f'{E31} saqué 31 de Envido.')
print(f'{E32} saqué 32 de Envido.')
print(f'{E33} saqué 33 de Envido.')

print(f'probabilidad de sacar 31 de envido {prob31:.6f}.')
print(f'probabilidad de sacar 32 de envido {prob32:.6f}.')
print(f'probabilidad de sacar 33 de envido {prob33:.6f}.')



