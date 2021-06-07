# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:44:51 2021

@author: User
"""

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
 
# from vigilante import vigilar            
# lines = vigilar('../Data/mercadolog.csv')
# naranjas = filematch(lines, 'Naranja')
# for line in naranjas:
#     print(line)
        