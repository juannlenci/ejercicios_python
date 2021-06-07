# -*- coding: utf-8 -*-
#vida.py
"""
Created on Sat May  8 20:39:30 2021
@author: Juan Lenci
"""
from datetime import date

def fechas(fecha):
    
    dia = int(fecha[:2])
    mes = int(fecha[3:5])
    año = int(fecha[6:])
    
    aniversario = date(año, mes, dia)
    hoy = date.today()
#%%Contador de dias y segundos
    dias =  hoy - aniversario
    segundos = dias.total_seconds()

#%% Contador de meses   
    contar_meses = 0
    inicio = aniversario.year
    fin = hoy.year
    for i in range(inicio , fin+1):
        if i == inicio:
            contar_meses += 12-aniversario.month
        else:
            if i == fin:
                contar_meses += hoy.month
            else:
                contar_meses += 12
#%%Contadores
    contar_años = contar_meses/12
    
    contar_segundos = int(segundos)
    contar_minutos = int(segundos/60)
    contar_horas = int(contar_minutos/(60))
    contar_dias = int(contar_horas/24)
    contar_meses = int(contar_meses)
 #%% 
    ancho = 20
    guion = "-" * ancho
      
    print(f'Desde {fecha}(A las 00:00)')
    print(f'hasta hoy {hoy}(A las 00:00)')
    print(guion)
    print(f'{"Hay":^20s}')
    print(guion)
    print(f'{contar_años:<15f} Años')
    print(f'{contar_meses:<14d} Meses')
    print(f'{contar_dias:<15d} Dias')
    print(f'{contar_horas:<17d} Hs')
    print(f'{contar_minutos:<16d} Min') 
    print(f'{contar_segundos:<16d} Seg')
    
    input()
#%%
if __name__ == '__main__':
    aniversario = "21/09/2019" #Ingrese dd/mm/YYYY
    fechas(aniversario)