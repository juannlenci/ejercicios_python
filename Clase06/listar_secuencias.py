# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:02:12 2021

@author: User
"""
from copy import deepcopy



def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s
#%%
def listar_secuencias(n):
    sec_bin=[]
    aux = []
    
    #sec_bin.append([0]*n)
    aux = [0]*n


    
    for n, i in enumerate(range((2**n))):
         if n == 0:
             sec_bin.append(aux)
             print(aux, n)

         else:
             aux1 = deepcopy(incrementar(aux))
             sec_bin.append(aux)
             print(aux, n)
    print(n)
    return sec_bin
