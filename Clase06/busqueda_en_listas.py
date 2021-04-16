#busqueda_en_listas.py

#%%
l=[]
for i in range(0,100):
    l.append(i)
    
def busqueda_lineal_ordenada(lista, e, verbose = False):
    '''Devuelve la posicion del primer numero mayor a "e" en una lista ordenada, de lo
    contrario devuelve -1.
    '''
    lista.sort()
    if verbose:
        print(f'[DEBUG] N')
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if verbose:
            print(f'[DEBUG] {z}')
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

print(busqueda_lineal_ordenada(l,46,True))
#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    lista.sort()
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
