# -*- coding: utf-8 -*-
#mareas_fft.py
"""
Created on Tue May 11 13:22:16 2021

@author: Juan Lenci
"""
import pandas as pd
import os

def main():
    directorio = '../Data'
    archivo_mareas = 'OBS_SHN_SF-BA.csv'
        
    fname = os.path.join(directorio,archivo_mareas)
    df = pd.read_csv(fname, index_col=['Time'], parse_dates=True)
    
    dh = df['12-25-2014':].copy()
    
    delta_t = 0#-1 # tiempo que tarda la marea entre ambos puertos
    delta_h = 0#19.476191 # diferencia de los ceros de escala entre ambos puertos
    #Para delta_h busque cual es la diferencia de la media en cada puerto
    
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

if __name__ == '__main__':
    main()

