#tablamult.py

tabla=[]
num= list(range(10))
header = (f'    {num[0]:^3d}{num[1]:^3d}{num[2]:^3d}{num[3]:^3d}{num[4]:^3d}{num[5]:^3d}{num[6]:^3d}{num[7]:^3d}{num[8]:^3d}{num[9]:^3d}')
print(header)
guion = "-"
separacion = ((f'{guion:-^34s}'))
print(separacion)

for n_fila, fila in enumerate(num):
    tabla.clear()
    cont = 0
    tabla.append(0)
    for row in enumerate(num):
        cont = n_fila + cont
        tabla.append(cont)
        
    print (f'{num[n_fila]:^3d}:{tabla[0]:^3d}{tabla[1]:^3d}{tabla[2]:^3d}{tabla[3]:^3d}{tabla[4]:^3d}{tabla[5]:^3d}{tabla[6]:^3d}{tabla[7]:^3d}{tabla[8]:^3d}{tabla[9]:^3d}')
