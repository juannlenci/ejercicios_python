# -*- coding: utf-8 -*-
#torre_control.py

"""
Created on Fri May 14 13:18:04 2021
@author: JLenci
"""

class TorreDeControl:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, n_vuelo_arribo):
        '''Encola el elemento n_vuelo_arribo.'''
        self.arribos.append(n_vuelo_arribo)
 
    def nueva_partida(self, n_vuelo_partida):
        '''Encola el elemento n_vuelo_partida.'''
        self.partidas.append(n_vuelo_partida)
        
    def esta_vacia(self):
        return self.largo_vuelos() == 0     
    
    def asignar_pista(self):
         if self.esta_vacia():
             return print('No hay vuelos en espera.')  
         if len(self.arribos):
             pista = self.arribos.pop()
             return print('El vuelo', pista, 'aterrizó con éxito.')
         else:
             pista = self.partidas.pop()
             return print('El vuelo', pista, 'despegó con éxito.')
    
    def largo_vuelos(self):
        return len(self.arribos) + len(self.partidas)

    def ver_estado(self):
        '''devuelve el estado de los vuelos.'''
        print(f'Vuelos esperando para aterrizar: {self.arribos}')
        print(f'Vuelos esperando para aterrizar: {self.partidas}')

