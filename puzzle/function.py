#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"

import re
import files
import sqlite3
import generateHtml

class function_version:
        pass

def get_function (version):
        table=[]
        expression=[]
	function=[]
	alternative=[]
	funcob=[]
	fl=[]
	fil=[]
	flfil=[]
	linex=[]
	lnum = 0
	fileslist=files.get_listfiles()
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	if version is "4": #if version is 4, it will get regular expression from version 4 and will add to list expression
        	for e in cursor.execute("SELECT  expression FROM functions WHERE versionob = '%s'" %version):
                        c=list(e)
                        expression.append(c[0])
	if version is "5": #if version is 5, it will get all regular expression and will add to list expression
		for e in cursor.execute("SELECT  expression FROM functions"):
                        c=list(e)
                        expression.append(c[0])
	for file in fileslist:
        	with open(file,"r") as f:
                	 for line in f.readlines():
                         	line = line.strip()
                                if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
                                if line[0] == '#': continue
                                if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
                                for x in range(len(expression)): # every regular expression compares with every line 
                                	if re.match(expression[x] , line): #if regular expression maches with line, it will add expression, line and file to differents list
                                        	fl.append(line)
						fil.append(file)
						lnum = lnum + 1
			          		table.append(expression[x])
	tvulf = ""
	tvulf+='<div class="row">\n'
	tvulf+='  <div class="col-xl-5 col-sm-6 mb-3">\n'
	tvulf+='    <div class="card text-white sqli o-hidden h-100" id="obs" onclick="idobs()">\n'
	tvulf+='       <div class="card-body">\n'
	tvulf+='          <div class="row">\n'
	tvulf+='              <div class="col-md-4">\n'
	tvulf+='                 <h2 style="text-align:center;">'+str(lnum)+'</h2>\n'
	tvulf+='              </div>\n'
	tvulf+='          <div class="col-md-8">\n'
	tvulf+='		<h2>Function Obsolete</h2>\n' 
	tvulf+='          </div>\n'
	tvulf+='        </dvi>\n'
	tvulf+='     </div>\n'
	tvulf+='  </div>\n'
	tvulf+='</div>\n'
	tvulf+='</div>\n'
	tvulf+='</div>\n'
	generateHtml.cardhtml(tvulf, generateHtml.creareporte())  #create card 
        generateHtml.scriptsearchtable("9")     #create script 

	for f, l in zip(fl, fil): #it joins fl and fil then the result adds to linex
                flfil.append("%s\n-n%s" % (f, l))
	linex.append(flfil) 
	function=list(set(table)) #it removes  repeated functions (expression) 
	for f in range(len(function)): #it gets function and alternative for the regular expression finded and adds diferents list
		for e in cursor.execute("SELECT  function, alternative FROM functions WHERE expression = '%s'" %function[f]):
			c=list(e)
			funcob.append(c[0])
			alternative.append(c[1])
	#for fc, al in zip(funcob, alternative): se puede contemplar para el modo verbose
	#	print("Tienes la funcion %s que es obsoleta, mejor cambiala por: %s." % (fc, al))
	linex.append(funcob) # it adds function to linex
	return linex #finally: [[line\n-nfile,line\n-nfunction,...line\nfunction],[function,function...function]]
							
