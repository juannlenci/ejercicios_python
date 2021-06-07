# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:32:34 2021

@author: User
"""
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)

df = pd.read_csv(fname)

df.head(1)

df.columns
#%%
dg = df[['nombre_com','altura_tot', 'diametro', 'inclinacio']]
dg
dg.describe()
#%%Para valores unicos
df['nombre_com'].unique()

#%%
#cuales son ombú?
df['nombre_com'] == 'Ombú'

#contarlos
(df['nombre_com'] == 'Ombú').sum()
#%%
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.head(10)
#%%
#Filtros booleanos
#selecciono filas
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

#selecciono columnas
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]

#miro
df_jacarandas.tail(10)
df_jacarandas.describe()

#copio si lo quiero modificar:
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

#%%

import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
s2.plot()