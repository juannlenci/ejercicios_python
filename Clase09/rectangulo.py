# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:41:41 2021

@author: User
"""
import numpy as np

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

class rectangulo(Punto):
        def __init__(self, p1, p2):
            self.punto1 = p1
            self.punto2 = p2
            
        def base(self):
            self.base = abs(self.punto1.x -self.punto2.x)
            return self.base

        def altura(self):
            self.altura = abs(self.punto1.y -self.punto2.y)
            return self.altura        
        
        def area(self):
            self.area = self.altura
            return self.area        
        
        def __str__(self):
            return f'({self.punto1},{self.punto2})'
    
        def __repr__(self):
            return f'Rectangulo({self.punto1},{self.punto2})'