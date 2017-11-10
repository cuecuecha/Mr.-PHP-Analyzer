#!usr/bin/python

import re
import files
import sqlite3
class file_version:
	pass

def open_file (file): #it match regular expression with every line from file  
	table=[]
	version=["7","5","4"] #available  versions 
	expression=[] 
	connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db") #connection to database
        cursor= connection.cursor()
	for v in range(len(version)):
        	if version[v] is "7":
                	for e in cursor.execute('SELECT expression FROM versions WHERE version=7'):
                        	c=list(e)
                        	expression.append(c[0]) #it add all regular expressions from only one version (for example: version 7) to list "expression"
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
          			if re.match(r'^\s*$', line): continue #if line is empty, continue with the next one
           			if line[0] == '#': continue
				if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
				for x in range(len(expression)):
					if re.match(expression[x], line): #if regular expression to match with line, it add current version to list "table" 
						table.append(version[v])
		if expression: #if list isn't empty, it remove all elements from list "expression" 
			del expression[:]
	cursor.close()	#disconnect from database		        
	return table


def get_version (): #it get version 
	list =[]
	version =["7","5","4"]
	file=files.get_listfiles() #list from the paths
        for v in range(len(version)):
		if list: #if list has elements, it check the current element isn't smaller that past element 
			for s in range(len(list)):
		        	if list[s]!= version[v-1]:
					for f in range(len(file)): 
                                		table = open_file(file[f]) #it call function open_file with every path form list "file" 
                                		for t in range(len(table)): 
                                        		if table[t]== version[v]: #if some element from table to match with current element from version, it will add current version to list 
                                                		list.append(version[v])
                                                		break 
		else: #if only list is empty: 
			for f in range(len(file)):
                               	table = open_file(file[f]) 
                              	for t in range(len(table)):
                                       	if table[t]== version[v]:
                                               	list.append(version[v])
                                              	break
	if list: #if list has elements, it can find the version
		for s in range(len(list)):
			if list[s] == "7": #if only list has some "7" the version is 7
				ve= "7"
				break
			elif list[s] == "5": #if only list has some "5" the version is 5 
				ve= "5"
				break
			elif list[s] == "4": #if only list has some "4" the version is 4
				ve= "4"
				break
	else: #if don't find some version, default version is "5"
		ve="5"

        return ve



