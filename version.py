#!usr/bin/python

import re
import files
class file_version:
	pass

def open_file (file):
	table=[]
	with open(file,"r") as f:
        	for line in f.readlines():
            		line = line.strip()
            		if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
            		if line[0] == '#': continue
			if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
			if re.match(r'^<\?\w*$',line): 
				table.append(1)	
			if re.match(r'^(\$.*?(\s=|\s=\s|=\s|=)mysql_.*?)|((\smysql_|mysql_).*)$', line): #extension mysql
				table.append("5")
			if re.match(r'^(.*?ereg.*?)$', line): #extension ereg
				table.append("5")
			if re.match(r'^(\$.*?(\s=|\s=\s|=\s|=)mssql_.*?)|((\smssql_|mssql_).*)$', line): #extension mssql
				table.append("5")
			if re.match(r'^(\$.*?(\s=|\s=\s|=\s|=)sybase_.*?)|((\ssybase_|sybase_).*)$', line): #extension sybase
				table.append("5")
			#expressions regulars php 5.3
			if re.match(r'(call_user_method((\(([\"\w\s\S\"]*)\))|_array(\(([\"\w\s\S\"]*)\))))',line): #Call a user method on an specific object
				table.append("5")
			if re.match(r'(define_syslog_variables(\(([\"\w\s\S\"]*)\)))',line): # Initializes all syslog related variables
				table.append("5")
			if re.match(r'(dl(\(([\"\w\s\S\"]*)\)))',line):# Loads a PHP extension at runtime
				table.append("5")
			if re.match(r'(mcrypt_generic_end(\(([\"\w\s\S\"]*)\)))',line):#  This function terminates encryption
				table.append("5")
			if re.match(r'(set_magic_quotes_runtime(\(([\"\w\s\S\"]*)\)))',line):#Sets the current active configuration setting of magic_quotes_runtime
				table.append("5")
			if re.match(r'(session_(register|unregister|is_registered)(\(([\"\w\s\S\"]*)\)))',line):#Register one or more global variables with the current session
				table.append("5")				
			if re.match(r'(set_socket_blocking)(\(([\"\w\s\S\"]*)\))',line):#Set blocking/non-blocking mode on a stream
				table.append("5")		
			if re.match(r'(split(|i))(\(([\"\w\s\S\"]*)\))',line):#Split string into array by regular expression
				table.append("5")	
			if re.match(r'(sql_regcase(\(([\"\w\s\S\"]*)\)))',line):#Make regular expression for case insensitive match
				table.append("5")
			if re.match(r'(mysql_db_query(\(([\"\w\s\S\"]*)\)))',line):#Selects a database and executes a query on it
				table.append("5")
			if re.match(r'(mysql_escape_string(\(([\"\w\s\S\"]*)\)))',line):#Escapes a string for use in a mysql_query
				table.append("5")

			#expressions regulars php 5.4
			if re.match(r'(mysql_list_dbs(\(([\"\w\s\S\"]*)\)))',line):#List databases available on a MySQL server
				table.append("5")

			#expressions regulars php 5.5
			if re.match(r'(preg_replace(\(([\"\w\s\S\"]*)\)))',line):#Perform a regular expression search and replace
				table.append("5")
			if re.match(r'(IntlDateFormatter\:\:setTimeZoneID(\(([\"\w\s\S\"]*)\)))',line):#Sets the time zone to use
				table.append("5")
			if re.match(r'(datefmt_set_timezone_id(\(([\"\w\s\S\"]*)\)))',line):#Sets the time zone to use
				table.append("5")
			if re.match(r'(mcrypt_(cbc|cfb|ecb|ofb)(\(([\"\w\s\S\"]*)\)))',line):# Encrypts/decrypts data in CBC|CFB|ECB|OFB mode
				table.append("5")
			if re.match(r'(iconv\.(input|output|internal)(_encoding))',line):#
				table.append("5")
			if re.match(r'(mbstring\.(http|internal)_(input|output|encoding))',line):#Defines default character code detection order.
				table.append("5")

			if re.match(r'^declare.?strict_types(\s=|=\s|\s=\s|=)1.*?$' , line): #scalar type declarations mode strict
				table.append("7")
			if re.match(r'^(function\s.*?(((int|float|bool|string)\s\$.*?)(,(int|float|bool|string)\s\$.*?)*)|(\$.*?(,\$.*?)*):(int|float|bool|string).*?)$' , line):  #return type declarations 
				table.append("7")
			if re.match(r'^(function\s.*?((int|float|bool|string)\s\$.*?)(,(int|float|bool|string)\s\$.*?)*)$' , line): #scalar type declarations mode coercive
				table.append("7")
			if re.match(r'^(\$.*?(\s=|=\s|\s=\s|=).*?(\s\?\?\s.*?)+)$' , line): # operator ?? null
				table.append("7")
			if re.match(r'^((.*?\s)+<=>.*?)$' , line): #operator <=>
				table.append("7")
			if re.match(r'^define\(.*?,\s((.*?\(.*)|\[)$' , line): #define for array
				table.append("7")
			if re.match(r'^(\$.*?->call.*?)|(.*?\$.*?->call.*?)$' , line): #function call
				table.append("7")
			if re.search(r'IntlChar::|random_byte|random_int|session_start\(\[' , line): #new functions
				table.append("7")



	print table
	return table
           	#option = map(lambda x: x.strip() ,line.split('=',1))

def get_version ():
	list =[]
	#file=["php/w3af-moth/webroot/moth/w3af/core/wml_parser/form_sql_injection.php"]
	file=files.get_listfiles()
	for f in range(len(file)):
		table = open_file(file[f])
		for l in range(len(table)):
    			if table[l] == "7":
				list.append("7")
				break
			elif table[l] == "4":
				list.append("4")
				break
	if list:
		for p in range(len(list)):
			if list[p] == "7":
				print "la version es php7+"
				break
			elif list[p]== "4":
				print "la version es php4"
				break
	else:
		print "la version es php5"
	print list


#get_version()


