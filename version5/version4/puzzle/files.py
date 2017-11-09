#!/usr/bin/python
import os

class files():
	pass

def get_files (route): #get and save paths in file
	out = open("/opt/mrphpanalyzer/file/out", 'w' ) #open o create file "out" 
	for root,directorio,files in os.walk(route): #it find all paths from project
                for fl in [a for a in files if a.lower().endswith("php")]: #it select files with extension php
                        file=(os.path.join(root, fl)) 
			out.write( "{}\n".format(file) ) #it write paths in file "out"
	out.close()

def get_listfiles (): #it add paths to list 
	list=[]
	with open("/opt/mrphpanalyzer/file/out","r") as s:
                for line in s.readlines():  #it read line for line
                        line = line.strip()
			list.append(line) #every path is added to list "line"

	return list

	
