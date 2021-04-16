#busqueda_en_listas.py

# def busqueda_binaria(lista, x, verbose = False):
#     '''Búsqueda binaria
#     Precondición: la lista está ordenada
#     Devuelve -1 si x no está en lista;
#     Devuelve p tal que lista[p] == x, si x está en lista
#     '''
#     if verbose:
#         print(f'[DEBUG] izq |der |medio')
#     pos = -1 # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if verbose:
#             print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
#         if lista[medio] == x:
#             pos = medio     # elemento encontrado!
#             break
#         elif lista[medio] > x:
#             der = medio - 1 # descarto mitad derecha
#         else:               # if lista[medio] < x:
#             izq = medio + 1 # descarto mitad izquierda
#     return pos

#%%
def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve posicion para que la lista siga ordenada si x no está en lista;
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
        
    l = len(lista)
    pos = -1 
    izq = 0
    der = l - 1
    
    #Antes que nada me dijo los extremos 
    if x <= lista[0]:
        pos = 0
    elif x >= lista[l-1]:
        pos = l
    else:
        while izq <= der:
            medio = (izq + der) // 2
            if verbose:
                print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
            if lista[medio] == x:
                pos = medio     # elemento encontrado!
                break
            elif lista[medio] > x:
                der = medio - 1 # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1 # descarto mitad izquierda
        if pos==-1:
            print(f'El elemento no esta en la lista')
            pos = izq
            #La posicion izquierda siempre termina señalando
            #el numero mayor siguiente a x, que es justamente
            #Donde tengo que insertar mi nuevo valor
            
    return pos

#%% 

def insertar(lista, x, verbose = False):
    pos = donde_insertar(lista, x, verbose)
    if x in lista:
        pass
    else:
        lista.insert(pos,x)
    return lista, pos
