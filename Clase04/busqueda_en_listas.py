#busqueda_en_listas.py

def buscar_u_elemento(lista, e):
    '''Recibe una lista y un elemento, Si el elemento está en la
    lista devuelve la ultima posición, de lo contrario devuelve -1.
    '''
    l=len(lista)
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista,start=1): 
        if lista[l-i] == e:   # recorremos la lista de atras a adelante
            pos = l-i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def buscar_n_elemento(lista, e):
    '''
    Recibe una lista y un elemento y devuelve la cantidad de veces
    que aparece el elemento en la lista
    '''

    cont  = 0 
    for i, z in enumerate(lista): 
        if z == e:   
            cont+=1
    return cont

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    m = lista[0] # Lo inicializo en el primer elemento
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    m = lista[0] # Lo inicializo en el primer elemento
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m