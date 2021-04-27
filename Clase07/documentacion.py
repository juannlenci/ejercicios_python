# -*- coding: utf-8 -*-
#documentacion.py
#%%
def valor_absoluto(n):
    '''
    Calcula el valor absoluto de un numero

    Pre: n, debe ser un numero.
    Pos: Se devuelve el valor el valor absoluto del numero.
    '''
    if n >= 0:
        return n
    else:
        return -n
#%%    
def suma_pares(l):
    '''
    Calcula la suma de los numeros pares de un iterable.
    
    Pre: l debe ser un iterable y sus elementos numeros
    Pos: Devuelve la suma de los elementos pares.
    '''    
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
#%%
def veces(a, b):
    '''
    Calcula el producto de dos numeros enteros.
    
    Pre: a y b deben ser numeros enteros
    Pos: Devuelve el producto entre a y b.
    '''    
    res = 0 
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
#%%
def collatz(n):
    '''
    Si el numero, es par lo divide por 2.
    Si el numero es impar lo multiplica por 3 y le suma una unidad
    Hasta que el resultado sea 1
    
    Pre: n debe ser entero y mayor que 0.
    Pos: Devuelve la cantidad de operaciones realizadas
    '''   
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res