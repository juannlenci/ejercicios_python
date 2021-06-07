# -*- coding: utf-8 -*-
#vida.py
"""
Created on Sat May  8 20:39:30 2021

@author: Juan Lenci
"""
from datetime import date

def segundos_vividos(fecha_nacimiento):
    
    dia = int(fecha_nacimiento[:2])
    mes = int(fecha_nacimiento[3:5])
    año = int(fecha_nacimiento[6:])
    
    nacimiento = date(año, mes, dia)
    hoy = date.today()

    dias =  hoy - nacimiento
    segundos = dias.total_seconds()
    print(
    f'Desde {nacimiento}(A las 00:00) hasta hoy {hoy}(A las 00:00) hay: {segundos}s')

if __name__ == '__main__':
    fecha_nacimiento = "01/04/1998" #Ingrese dd/mm/YYYY
    segundos_vividos(fecha_nacimiento)