#propagar.py

def propagar(lista):
    '''
    recibe un vector con 0's, 1's y -1's y devuelve un
    vector en el que los 1's se propagaron a sus vecinos con 0.
    '''
    l=len(lista)
    #Uso 2 ciclos for, ya q en el segundo solo cambio los fosforos contiguos 
    #Y en el primero vuelvo a hacerlo hasta que se complete la propagacion
    for j in enumerate(lista,start=0): 
        for i, e in enumerate(lista,start=0): 
            if (e == 0): #Verifico si el fosforo esta apagado
                if (i == 0) and (lista[i+1]==1): #El caso de q sea el primer elemento, miro solo el proximo
                    lista[i] = 1
                elif (i == l-1) and (lista[i-1]==1): #El caso de q sea el ultimo elemento, miro solo el anterior
                    lista[i] = 1
                elif (lista[i+1]==1)or(lista[i-1]==1): #Todos los demas casos miro proximo y anterior
                    lista[i] = 1
    return lista
    