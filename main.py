#!/usr/bin/python
import version
import argparse
import files
parser = argparse.ArgumentParser(description='Encontrar rutas de archivos con extension php')
parser.add_argument('-m' ,required=True, nargs=1,  help="Ruta inicial")
parser.add_argument('--ayuda', action="store_true", help="Listar acciones")
argumentos = parser.parse_args()

if argumentos.m :
	files.get_files(argumentos.m[0])
	version.get_version()
    	

if argumentos.ayuda:
        print '''
               	Obtencion de rutas de archivos con extension php

                Opciones:
                1.
                2. 
        '''

