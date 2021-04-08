# cadenas.py

cont = 0

cadena = "Ejemplo con for"
for c in cadena:
    print('caracter:', c)
    if c == "o":
        cont = cont + 1
print('Cantidad de "o":', cont)
