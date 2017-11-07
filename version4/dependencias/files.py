#!/usr/bin/python
import os

class files():
	pass

def get_files (route):
	#file =[]
	out = open( "/root/mrphpanalyzer/archivos/out", 'w' )
	for root,directorio,files in os.walk(route):
                for fl in [a for a in files if a.lower().endswith("php")]:
                        file=(os.path.join(root, fl))
			out.write( "{}\n".format(file) )
	out.close()

#get_files("php")

def get_listfiles ():
	list=[]
	with open("/root/mrphpanalyzer/archivos/out","r") as s:
                for line in s.readlines():
                        line = line.strip()
			list.append(line)
	#print list
	return list
#get_listfiles()

#def delete_file ():
	
