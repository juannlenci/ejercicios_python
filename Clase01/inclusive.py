# inclusive.py

frase = input("ingrese frase: ")
palabras = frase.split(" ")

cont = 0

for palabra in palabras:
    aux = palabra
    if len(palabra) > 2:
        if aux[-1] == "o":
            dim = len(aux)
            aux = aux[:(dim-1)]+"e"
        elif aux[-2] == "o":
            dim = len(aux)
            aux = aux[:(dim-2)]+"e"+aux[-1]
        else:
            pass
        palabras[cont] = aux
        cont = cont+1

cont=0
frase_t = " ".join(palabras)
print(frase_t)
