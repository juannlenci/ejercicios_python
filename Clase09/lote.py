# -*- coding: utf-8 -*-
#lote.py
"""
Created on Thu May 13 12:16:12 2021
@author: Juan Lenci
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        costo = self.cajones * self.precio
        return costo
        
    def vender(self, cantidad):
        self.cajones -= cantidad
        
    def __str__(self):
        return f'({self.nombre}, {self.cajones}, {self.precio})'

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'