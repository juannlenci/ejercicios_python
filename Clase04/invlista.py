# invlista.py

def invertir_lista(lista):
    '''
     Dada una lista devuelve otra que tiene los mismos
     elementos pero en el orden inverso.
    '''
    invertida = []
    l = len(lista)
    for i, e in enumerate(lista,start=1): 
        invertida.append (lista[l-i])
    return invertida