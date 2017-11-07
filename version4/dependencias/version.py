#!usr/bin/python

import re
import files
import sqlite3
class file_version:
	pass

def open_file (file):
	table=[]
	version=["7","5","4"]
	expression=[]
	connection= sqlite3.connect("../base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	for v in range(len(version)):
        	if version[v] is "7":
                	for e in cursor.execute('SELECT expression FROM versions WHERE version=7'):
                        	c=list(e)
                        	expression.append(c[0])
        	elif version[v] is "5":
                	for e in cursor.execute('SELECT expression FROM versions WHERE version=5'):
                        	c=list(e)
                        	expression.append(c[0])
        	elif version[v] is "4":
                	for e in cursor.execute('SELECT expression FROM versions WHERE version=4'):
                        	c=list(e)
                        	expression.append(c[0])
		with open(file,"r") as f:
       			for line in f.readlines():
           			line = line.strip()
          			if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
           			if line[0] == '#': continue
				if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
				for x in range(len(expression)):
					if re.match(expression[x], line):
						table.append(version[v])
						#print line
						#print expression[x]
		if expression:
			del expression[:]
	cursor.close()			        
	return table


def get_version ():
	list =[]
	version =["7","5","4"]
	#file=["php/w3af-moth/webroot/moth/w3af/core/wml_parser/form_sql_injection.php"]
	file=files.get_listfiles()
        for v in range(len(version)):
		if list:
			for s in range(len(list)):
		        	if list[s]!= version[v-1]:
					for f in range(len(file)):
                                		table = open_file(file[f]) 
                                		for t in range(len(table)):
                                        		if table[t]== version[v]:
                                                		list.append(version[v])
                                                		break 
		else:
			for f in range(len(file)):
                               	table = open_file(file[f]) 
                               	for t in range(len(table)):
                                       	if table[t]== version[v]:
                                               	list.append(version[v])
                                              	break
	for s in range(len(list)):
		if list[s] == "7":
			ve= "7"
			break
		elif list[s] == "5":
			ve= "5"
			break
		elif list[s] == "4":
			ve= "4"
			break

	#print "la version es: php"
	#print ve		
	#print list
        return ve

#get_version()


