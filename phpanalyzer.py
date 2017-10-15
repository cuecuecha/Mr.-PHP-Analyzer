#!/usr/bin/python
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Options', help='Options')
parser.add_argument('-r', nargs=1, help="path")
parser.add_argument('--actions', action="store_true", help="Actions list")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
argumentos = parser.parse_args()

if argumentos.m :
        for ruta,directorio,archivos in os.walk(argumentos.m[0]):
                for archivo in [a for a in archivos if a.lower().endswith("php")]:
                        print('file %s \n\t (full_path %s)') % (archivo,os.path.join(ruta, archivo))

if argumentos.ayuda:
        print '''
                Vulnerabilities available: 

                Options:
                1. xss
                2. 
        '''
