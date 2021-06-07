# -*- coding: utf-8 -*-
#hojas_ISO.py
"""
Created on Mon May 31 11:44:48 2021

@author: Juanlenci
"""

def iso(n):
    if n == 0:
        ancho = 841
        largo = 1189
    if n > 0:
        ancho = int((max(iso(n-1))) / 2)
        largo = int(min(iso(n-1)))
    tam = ancho, largo
    return tam