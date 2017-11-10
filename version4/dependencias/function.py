import re
import files
import sqlite3
import generateHtml

# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"
class function_version:
        pass

def get_function (version):
        table=[]
        expression=[]
	function=[]
	alternative=[]
	funcob=[]
	functionlist=[]
	fl=[]
	fil=[]
	flfil=[]
	linex=[]
	lnum = 0
	fileslist=files.get_listfiles()
        connection= sqlite3.connect("../base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	if version is "4":
        	for e in cursor.execute("SELECT  expression FROM functions WHERE versionob = '%s'" %version):
                        c=list(e)
                        expression.append(c[0])
	if version is "5":
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
                                for x in range(len(expression)):
                                	if re.match(expression[x] , line):
                                        	fl.append(line)
                                        	lnum = lnum + 1
						fil.append(file)
			          		table.append(expression[x])
			          		
	tvulf = ""
	tvulf+='<div class="row">\n'
	tvulf+='  <div class="col-xl-3 col-sm-6 mb-3">\n'
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
	generateHtml.cardhtml(tvulf, generateHtml.creareporte())          		
	for f, l in zip(fl, fil):
                flfil.append("%s\n%s" % (f, l))
	linex.append(flfil)
	function=list(set(table))
	for f in range(len(function)):
		for e in cursor.execute("SELECT  function, alternative FROM functions WHERE expression = '%s'" %function[f]):
			c=list(e)
			funcob.append(c[0])
			alternative.append(c[1])
	for fc, al in zip(funcob, alternative):
		print("Tienes la funcion %s que es obsoleta, mejor cambiala por: %s." % (fc, al))
	linex.append(funcob)
	#print linex
	return linex
#get_function("5")
							
