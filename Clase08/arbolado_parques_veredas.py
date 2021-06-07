# -*- coding: utf-8 -*-
#arbolado_parques_veredas.py.
"""
Created on Mon May 10 20:28:13 2021

@author: User
"""
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    directorio = '../Data'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'
    archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    
    fname_parques = os.path.join(directorio,archivo_parques)
    fname_veredas = os.path.join(directorio,archivo_veredas)
    
    df_parques = pd.read_csv(fname_parques)
    df_veredas = pd.read_csv(fname_veredas)
    
    cols_parques = ['altura_tot', 'diametro']
    cols_veredas = ['altura_arbol', 'diametro_altura_pecho']
    
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()
    
    df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura_arbol", "diametro": "diametro_altura_pecho"})
    
    df_tipas_parques = df_tipas_parques.assign(ambiente="parque")
    df_tipas_veredas = df_tipas_veredas.assign(ambiente="vereda")
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Diametros')
    sns.boxplot(ax=ax1,data=df_tipas,y='diametro_altura_pecho',x = 'ambiente',hue="ambiente", dodge=False)
    ax2.set_title('Alturas')
    sns.boxplot(ax=ax2,data=df_tipas,y='altura_arbol',x = 'ambiente',hue="ambiente", dodge=False)

if __name__ == '__main__':
    main()