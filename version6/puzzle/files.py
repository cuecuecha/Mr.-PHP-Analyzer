#!/usr/bin/python
import os
import re
class files():
	pass

def get_files (route): # it gets and saves paths in file
	out = open("/opt/mrphpanalyzer/file/out", 'w' ) #it opens o creates file "out" 
	if re.match(r'.*\..*$' , route): #only one file  
                out.write( "{}\n".format(route) ) #it writes paths in file "out"
        else:
		for root,directorio,files in os.walk(route): #it finds all paths from project
                	for fl in [a for a in files if a.lower().endswith("php")]: #it selects files with extension php
                        	file=(os.path.join(root, fl)) 
				out.write( "{}\n".format(file) ) #it writes paths in file "out"
	out.close()

def get_listfiles (): #it adds paths to list 
	list=[]
	with open("/opt/mrphpanalyzer/file/out","r") as s:
                for line in s.readlines():  #it reads line for line
                        line = line.strip()
			list.append(line) #every path is added to list "line"

	return list

	
