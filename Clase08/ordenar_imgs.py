# -*- coding: utf-8 -*-

#%%
import os
import datetime
import time

def crear_directorio():
    """
    Crea una carpeta con el nombre "NOMBRE_DIRECTORIO"
    en la direccion "root"
    Devuelve la direccion de esta nueva carpeta
    """
    NOMBRE_DIRECTORIO = 'imgs_procesadas'
    root = ".."
    os.chdir(root)
    os.mkdir(NOMBRE_DIRECTORIO)
    nueva_carpeta = (os.path.join(root,NOMBRE_DIRECTORIO))
    
    return nueva_carpeta

def renombrar(name):
    """
    Se le pasa el nombre de un archivo con el formato "nombre_AAAAMMDD.formato"
    y devuelve "nombre.formato"
    """
    name_aux = name.split(".")
    name = name_aux[0][:-9]
    tipo = "."+name_aux[1]
    return name + tipo

def mover(vieja_carpeta,nueva_carpeta, name):
    """
    vieja_carpeta: direccion de donde proviene el archivo
    nueva_carpeta: direccion donde se movera el archivo
    name: nombre del archivo.
    
    Mueve el archivo de vieja_carpeta a nueva_carpeta,
    cambiandole el nombre con la funcion renombrar().
    """
    nuevo_nombre = renombrar(name)
    os.rename(os.path.join(vieja_carpeta,name),(os.path.join(nueva_carpeta, nuevo_nombre)))
   
    return

def cambiar_fecha(root,name):
    """
    root: direccion de donde proviene el archivo
    name: nombre del archivo.
    
    Cambia la fecha de modificacion y de acceso del archivo
    segun su nombre indica
    """
    direccion_ini = os.getcwd()
    os.chdir(root)

    name_aux = name.split(".")
    fecha = name_aux[0][-8:]

    año = int(fecha[:4])
    mes = int(fecha[4:6])
    dia = int(fecha[6:])
    
    fecha_modifi = datetime.datetime(year = año, month = mes, day = dia)
    fecha_acceso = fecha_modifi

    ts_modifi = fecha_modifi.timestamp()
    ts_acceso = fecha_acceso.timestamp()

    os.utime(name, (ts_acceso, ts_modifi))

    stats_archivo = os.stat(name)
    time.ctime(stats_archivo.st_atime)
    
    os.chdir(direccion_ini) #Vuelvo a mi direccion inicial

    return

def main(directorio):
    '''
    directorio: lista, con nombre del programa en la posicion 0
    y directorio al que se le quiere listar los archivos en la posicion 1.
    
    Imprime todos los archivos en el directorio
    '''
    tipo = ".png"
    direccion_ini = directorio[1]
    os.chdir(direccion_ini)
    nueva_carpeta = crear_directorio() #Creo nueva carpeta
    os.chdir(direccion_ini)

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if tipo in name:
                cambiar_fecha(root, name)
                mover(root, nueva_carpeta, name)
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError:
                pass

if __name__ == '__main__':
    #OBS: ENTRAR EN EJERCICIOS_PYTHON  (python ordenar_imgs.py ../Data/ordenar)  
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    main(sys.argv)
