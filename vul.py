#!/usr/bin/python
import os
import re
import files
import generatecsv
import datetime
import generateHtml
class get_vul:
	pass

def get_xss():

	#n= re.compile(r"(?<!(trim\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	#o = re.compile(r"(?<!(htmlentities\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	#no = re.compile(r"(?<!(htmlspecialchars\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	#p = re.compile(r"(?<!(strip\_tags\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I) 

	q = re.compile(r">.*?<\s*\/?[\w\s]+>",re.I) #Unquoted HTML breaking with closing tag
	r = re.compile(r"[\"\'].*?>",re.I) #HTML breaking
	s = re.compile(r"<base\b.+?\bhref\b.+?>",re.I) # Common JavaScript injection points (forms)
	t = re.compile(r"\bon\w+\s*=",re.I) #HTML event handler

	n=re.compile(r"#.+?\)[\"\s]*>",re.I) #HTML breaking
	o= re.compile(r">.*?<\s*\/?[\w\s]+>]",re.I) #HTML breaking
	p= re.compile(r"\/\/output",re.I) #PHP output stream
	u = re.compile(r"<base\b.+?\bhref\b.+?>",re.I) #Base URL
	v = re.compile(r"<(form|button|input|keygen|textarea|select|option)",re.I) # Common JavaScript injection points (forms)
	lexpresiones = [v]
	#file=["php/w3af-moth/webroot/moth/w3af/core/wml_parser/form_sql_injection.php"]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				#if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
			#if re.match(r'([^(htmlespecialchars)]|([^(strip_tags)])|([^(trim)])|([^(htmlentities)]))(\$\_(GET|POST|REQUEST)\[(\"|\')[aA-zZ]+(\"|\')])',line):
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'1','xss',line,fs)


def get_lfi_rfi():
	table=[]
	#m= re.compile(r"(?<!(include\s))(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	n= re.compile(r"\.\.[\/\\]",re.I) # Directory traversal
	o= re.compile(r"%2e%2e[\/\\]",re.I) #Directory traversal urlencoding
	p = re.compile(r"%c0%ae[\/\\]",re.I) #Directory traversal urlencoding
	r = re.compile(r"\/etc\/[.\/]*(passwd|shadow|master\.passwd)",re.I)
	t = re.compile(r"(?<!\w)(boot\.ini|global\.asa|sam)\b",re.I) #Common Windows files
	u = re.compile(r"\bfile_(get|put)_contents\b.*?\(.*\)",re.I) #Critical PHP function file_get_contents/file_put_contents
	y = re.compile(r"include(_once)?\(.*?;",re.I) #Critical PHP function include
	x = re.compile(r"\brequire(_once)?\(.*?;",re.I) #Critical PHP function require
	#RFI
	a = re.compile(r"\(\)\s*\{.*?;\s*\}\s*;",re.I) #Shellshock (CVE-2014-6271)
	#b = re.compile(r"(\b(do|while|for)\b.*?\([^)]*\).*?\{)|(\}.*?\b(do|while|for)\b.*?\([^)]*\))",re.I) #C-style loops
	c = re.compile(r"[=(].+?\?.+?\:",re.I) #C-style ternary operator
	d = re.compile(r"\\u00[a-f0-9]{2}",re.I) #Octal entity
	#e = re.compile(r"\\x0*[a-f0-9]{2}",re.I) # Hex entity
	#f = re.compile(r"\\\d{2,3}",re.I) #Unicode entity
	g = re.compile(r"\/\/input",re.I) #PHP input stream
	#h = re.compile(r"<\?(?!xml\s)",re.I) #PHP opening tag
	i = re.compile(r"\bcall_user_func\b.*?\(.+?\)",re.I) #Critical PHP function call_user_func
	#j = re.compile(r"\bcreate_function\b.*?\(.+?\)",re.I) 
	k = re.compile(r"\beval\b.*?(\(.+?\)|\{.+?\})",re.I) #Critical function eval
	l = re.compile(r"\bexec\b.*?\(.+?\)",re.I) #Critical function exec
	axa = re.compile(r"\bmove_uploaded_file\b.*?\(.+?\)",re.I)
	#axb = re.compile(r"\bpassthru\b.*?\(.+?\)",re.I) #Critical PHP function 'passthru'
	axc = re.compile(r"\bp(roc_)?open\b.*?\(.+?\)",re.I) #Critical PHP function 'popen/proc_open'
	axd = re.compile(r"shell_exec.*?\(.+?\)",re.I) #critical PHP function 'shell_Exec'
	axe = re.compile(r"system\s\(.+?\)") # Critical PHP function 'system'
	axf = re.compile(r"\bpreg_(replace|match)\b.*?\(.+?\)") #Critical PHP function 'preg_match/preg_replace'
	axg = re.compile(r"\{\s*\$\s*\{.+?\}\s*\}",re.I) #PHP complex curly syntax
	axh = re.compile(r"\bexec\b.+?\bxp_cmdshell\b",re.I)#MSSQL code execution 'xp_cmdshell'
	lexpresiones = [axh]
	#file=["php/w3af-moth/webroot/moth/w3af/core/wml_parser/form_sql_injection.php"]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				#if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
			#if re.match(r'([^(htmlespecialchars)]|([^(strip_tags)])|([^(trim)])|([^(htmlentities)]))(\$\_(GET|POST|REQUEST)\[(\"|\')[aA-zZ]+(\"|\')])',line):
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'2','lfi_rfi',line,fs)



def get_insecureSI():
	n= re.compile(r"(?<!(basename\(\s))\$\_FILES(\[.*\])",re.I)
	lexpresiones = [n]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'3','insecure_send_information',line,fs)


def get_pathTraversal():
	n= re.compile(r"\.\.[\/\\]",re.I) #Directory traversal
	o= re.compile(r"%(c0\.|af\.|5c\.)",re.I) #Directory traversal unicode + urlencoding
	p = re.compile(r"%2e%2e[\/\\]",re.I) #Directory traversal urlencoding
	q = re.compile(r"%c0%ae[\/\\]",re.I) #Directory traversal unicode + urlencoding
	lexpresiones = [q]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'4','path_traversal',line,fs)


def get_sqli():
	n= re.compile(r"find_in_set.*?\(.+?,.+?\)",re.I) #Common MySQL function 'find_in_set'
	o= re.compile(r"\bmysql.*?\..*?user\b",re.I) # MySQL information disclosure 'mysql.user'
	p = re.compile(r"\bunion\b.+?\bselect\b",re.I) #Common SQL command 'union select'
	q = re.compile(r"\bupdate\b.+?\bset\b",re.I) #Common SQL command 'update' *********************
	r = re.compile(r"\bdrop\b.+?\b(database|table)\b",re.I) #Common SQL command 'drop'
	t = re.compile(r"\bload_file\b.*?\(.+?\)",re.I) #MySQL file disclosure 'load_file'
	u = re.compile(r"\bload\b.*?\bdata\b.*?\binfile\b.*?\binto\b.*?\btable\b",re.I) #MySQL file disclosure 'load data' #nocachonada
	v = re.compile(r"\bselect\b.*?\binto\b.*?\b(out|dump)file\b",re.I) #MySQL file write 'into outfile' #nocachonada
	x = re.compile(r"(SELECT\s)(group_)?concat(_ws)?\b.*?\(.+?\)",re.I) #MySQL function 'concat'
	y = re.compile(r"(SELECT\s)(char_|bit_)?length\b.*?\(.+?\)",re.I) #Common SQL function 'length'
	z = re.compile(r"(SELECT\s)(un)?hex\b.*?\(.+?\)",re.I) #Common SQL function 'hex/unhex'
	a = re.compile(r"(select\s.*from\s)",re.I)
	b = re.compile(r"(select\s)(current_)?user\b.*?\(.*?\)",re.I) #Common SQL function 'user'
	c = re.compile(r"(select\s)version\b.*?\(.*?\)",re.I) #Common SQL function 'version'
	d = re.compile(r"\bselect\s.*where\b.+?(\b(not_)?(like|regexp)\b|[=<>])",re.I) # Common SQL comparison 'where'
	e = re.compile(r"\binsert\b.+?\binto\b.*?\bvalues\b.*?\(.+?\)",re.I) #Common SQL command 'insert'
	f = re.compile(r"\bselect\b.+?\bfrom\b",re.I) # Common SQL command 'select'
	g = re.compile(r"\bpg_database\b",re.I) #PgSQL information disclosure 'pg_database'
	h = re.compile(r"(SELECT\s)(current_)?database\b.*?\(.*?\)",re.I) #Common SL command 'select database'
	lexpresiones = [h]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'5','sqli',line,fs)


def get_commandInjection():
	n = re.compile(r"^system\s\(",re.I) #function system
	o = re.compile(r"[^_]exec\(.*\)",re.I)  #command exec
	p = re.compile(r"query\(.*\)",re.I) #function query
	r = re.compile(r"shell_exec\(",re.I) #function execute commands
	s = re.compile(r"\bp(roc_)?open\b.*?\(.+?\)",re.I) #Critical PHP function 'popen/proc_open'
	j = 0
	data = ""
	lexpresiones = [s]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):	
						j = j+1
						data += "<tr>\n"
						data += "<td>1</td>\n"				
						data += "<td>commandInjection</td>\n"				
						data += "<td>"+line+"</td>\n"				
						data += "<td>"+fs+"</td>\n"				
						data += "<td>3</td>\n"				
						data += "<td>23,23</td>\n</tr>"				
						print(fs)
						print(line)
	#					generatecsv.get_namecsv(str(datetime.date.today()),'6','commandInjection',line,fs)
	#generateHtml.get_createhtml(j,data)


def get_sessionCookie():
	n = re.compile(r"setcookie\(.*\)",re.I) 
	o= re.compile(r"session_set_cookie_params",re.I)
	#p = re.compile(r"\$\_COOKIE",re.I)
	lexpresiones = [p]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
						print(fs)
						print(line)
						generatecsv.get_namecsv(str(datetime.date.today()),'7','weakCookie',line,fs)
