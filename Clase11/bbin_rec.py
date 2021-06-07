# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:21:25 2021

@author: User
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio]== e:
            res = True
        elif lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[medio:], e)
    return res