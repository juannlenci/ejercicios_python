#geringoso.py

cadena = input("ingrese palabra a taducir: ")
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
print(capadepenapa)