# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:50:15 2021

@author: Juannleci
Basado en la idea de Paula Galansino en slack
"""

def pascal(n, k):
    todo = []
    for i in range(n):
        lista_temporal = []
        todo.append(lista_temporal)
    if n == 0:
        res = 1
    else:
        if k == 0:
            res = pascal((n-1), k)
        elif k == n:
            res = pascal((n-1), (k-1))
        else:
            res = pascal((n-1), k) + pascal((n-1),(k-1))
    return res