#!/usr/bin/python
# -*- coding: utf-8 -*-
import version
import argparse
import files
import vul
parser = argparse.ArgumentParser(description='Find file paths with php extension')
parser.add_argument('-m', nargs=1,  help="Path")
parser.add_argument('--vul', nargs=1,  help="Option of vulnerability")
parser.add_argument('--ayuda', action="store_true", help="Actions list")
parser.add_argument('--csv', nargs=1, action="store_true", help="Generate csv --cvs name")
argumentos = parser.parse_args()

if argumentos.m :
	files.get_files(argumentos.m[0])
	#version.get_version()
	#vul.get_xss()   	
	#vul.get_lfi_rfi()
	#vul.get_sqli()
	#vul.get_pathTraversal()
	#vul.get_commandInjection()
if argumentos.ayuda:
        print '''
               	Option --vul

                Opciones:
                1. All vulnerabilities
                2. sqli
                3. xss
                4. Generacion débil o inapropiada de cookies de seión
                5. Envio de información sensible a través de métodos inseguros
                6. Implementación de funciones depreciadas
                7. LFI y RFI
                8. Path Traversal
                9. Inyección de comandos
                10. Inyección de código fuente
        '''
if argumentos.vul:
	if argumentos.vul[0]=="1":
		vul.get_insecureSI()
		vul.get_xss()   	
		vul.get_lfi_rfi()
		vul.get_sqli()
		vul.get_pathTraversal()
		vul.get_commandInjection()
		vul.get_sessionCookie()
	elif  argumentos.vul[0]=="2":
		vul.get_sqli()
	elif  argumentos.vul[0]=="3":
		vul.get_xss()
	elif  argumentos.vul[0]=="4":
		vul.get_sessionCookie()
	elif  argumentos.vul[0]=="5":
		vul.get_insecureSI()
	elif  argumentos.vul[0]=="6":
		print("Aun no disponible")
	elif  argumentos.vul[0]=="7":
		vul.get_lfi_rfi()
	elif  argumentos.vul[0]=="8":
		vul.get_pathTraversal()
	elif  argumentos.vul[0]=="9":
		vul.get_commandInjection()
	elif  argumentos.vul[0]=="10":
		print("Aun no disponible")
	else:
		print("Option no valida")
