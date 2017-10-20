#!/usr/bin/python
import os
import re
import files
class get_vul:
	pass

def get_xss():
	list =[]
	table=[]
	n= re.compile(r"(?<!(trim\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	o = re.compile(r"(?<!(htmlentities\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	p = re.compile(r"(?<!(strip\_tags\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I) 
	q = re.compile(r">.*?<\s*\/?[\w\s]+>",re.I)
	r = re.compile(r"[\"\'].*?>",re.I) #HTML breaking
	s = re.compile(r"<base\b.+?\bhref\b.+?>",re.I) # Common JavaScript injection points (forms)
	t = re.compile(r"\bon\w+\s*=",re.I) #HTML event handler
	lexpresiones = [t]
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

def get_lfi_rfi():
	table=[]
	m= re.compile(r"(?<!(include\s))(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	n= re.compile(r"\.\.[\/\\]",re.I) # Directory traversal
	o= re.compile(r"%2e%2e[\/\\]",re.I) #Directory traversal urlencoding
	p = re.compile(r"%c0%ae[\/\\]",re.I)
	q = re.compile(r"\.(ht(access|passwd|group))|(apache|httpd)\d?\.conf",re.I)
	r = re.compile(r"\/etc\/[.\/]*(passwd|shadow|master\.passwd)",re.I)
	s = re.compile(r"%\w+%",re.I) #Windows environment variable pattern
	t = re.compile(r"(?<!\w)(boot\.ini|global\.asa|sam)\b",re.I) #Common Windows files
	u = re.compile(r"\bfile_(get|put)_contents\b.*?\(.+?\)",re.I) #Critical PHP function file_get_contents/file_put_contents
	v = re.compile(r"\breadfile\b.*?\(.+?\)",re.I) #Critical PHP function readfile
	y = re.compile(r"\binclude(_once)?\b.*?;",re.I) #Critical PHP function include
	x = re.compile(r"\brequire(_once)?\b.*?;",re.I) #Critical PHP function require
	#RFI
	a = re.compile(r"\(\)\s*\{.*?;\s*\}\s*;",re.I) #Shellshock (CVE-2014-6271)
	b = re.compile(r"(\b(do|while|for)\b.*?\([^)]*\).*?\{)|(\}.*?\b(do|while|for)\b.*?\([^)]*\))",re.I) #C-style loops
	c = re.compile(r"[=(].+?\?.+?\:",re.I) #C-style ternary operator
	d = re.compile(r"\\u00[a-f0-9]{2}",re.I) #Octal entity
	e = re.compile(r"\\x0*[a-f0-9]{2}",re.I) # Hex entity
	f = re.compile(r"\\\d{2,3}",re.I) #Unicode entity
	g = re.compile(r"\/\/input",re.I) #PHP input stream
	h = re.compile(r" <\?(?!xml\s)",re.I) #PHP opening tag
	i = re.compile(r"\bcall_user_func\b.*?\(.+?\)",re.I) #Critical PHP function call_user_func
	j = re.compile(r"\bcreate_function\b.*?\(.+?\)",re.I) 
	k = re.compile(r" \beval\b.*?(\(.+?\)|\{.+?\})",re.I) #Critical function eval
	l = re.compile(r"\bexec\b.*?\(.+?\)",re.I) #Critical function exec
	axa = re.compile(r"\bmove_uploaded_file\b.*?\(.+?\)",re.I)
	axb = re.compile(r"\bpassthru\b.*?\(.+?\)",re.I) #Critical PHP function 'passthru'
	axc = re.compile(r"\bp(roc_)?open\b.*?\(.+?\)",re.I) #Critical PHP function 'popen/proc_open'
	axd = re.compile(r"shell_exec.*?\(.+?\)",re.I) #critical PHP function 'shell_Exec'
	axe = re.compile(r"system.*?\(.+?\)") # Critical PHP function 'system'
	axf = re.compile(r"\bpreg_(replace|match)\b.*?\(.+?\)") #Critical PHP function 'preg_match/preg_replace'
	axg = re.compile(r"\{\s*\$\s*\{.+?\}\s*\}",re.I) #PHP complex curly syntax
	axh = re.compile(r"\bexec\b.+?\bxp_cmdshell\b",re.I)#MSSQL code execution 'xp_cmdshell'
	axi = re.compile(r"")
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