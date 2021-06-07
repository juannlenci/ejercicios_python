# -*- coding: utf-8 -*-
#listar_imgs.py

"""
Created on Mon May 10 11:39:11 2021
@author: Juan Lenci
"""

import os


def listar_imgs(directorio):
    '''
    Parameters
    ----------
    directorio : str
        Se le pasa el directorio al que se le quiere listar los archivos.
        Imprime todos los archivos en el directorio
    '''

    tipo = ".png"
    os.chdir(directorio[1])

    for root, dirs, files in os.walk("."):
       for name in files:
           if tipo in name:
               print(os.path.join(root,name))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    listar_imgs(sys.argv)
    