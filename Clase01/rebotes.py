# rebotes.py


h = 100 #Altura Inicial en metros
a = 3/5 #Atenuacion 
reb = 10 #Cantidad de rebotes
i = 1

while (reb > 0):
    h=h*a
    print('Rebote', end=' ')    
    print(i, end=' ')
    print(round(h,2))    
    i=i+1
    reb=reb-1
    