#diccionario_geringoso.py

def geringoso (cadena):
    capadepenapa = ''
    a   = "pa"
    e   = "pe"
    i   = "pi"
    o   = "po"
    u   = "pu"
    aux = ""

    for c in cadena:
        if c == "a":
            aux = c + a
        elif c == "e":
            aux = c + e
        elif c == "i":
            aux = c + i
        elif c == "o":
            aux = c + o 
        elif c == "u":
            aux = c + u
        else:
            aux = c
        capadepenapa = capadepenapa + aux
        aux=""
    return capadepenapa
 
def dic_geringoso (lista):
    lista_geringoso = []
    for palabra in lista:
        traduccion = geringoso(palabra)
        lista_geringoso.append(traduccion)
    dictionary_geringoso = dict(zip(lista, lista_geringoso))
    return dictionary_geringoso

lista = ["banana", "manzana", "mandarina"]
dictionary_geringoso = dic_geringoso(lista)
print(dictionary_geringoso)
