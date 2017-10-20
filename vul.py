#!/usr/bin/python
import os
import re
import files
class get_vul:
	pass

def get_xss():
	list =[]
	table=[]
	m= re.compile(r"(?<!(include\s))(\$\_(POST|REQUEST|GET)\[.*\])",re.I) #LFI
	n= re.compile(r"(?<!(trim\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	o = re.compile(r"(?<!(htmlentities\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	p = re.compile(r"(?<!(strip\_tags\())(\$\_(POST|REQUEST|GET)\[.*\])",re.I)
	q = re.compile(r">.*?<\s*\/?[\w\s]+>",re.I)
	lexpresiones = [n,o,p,q]
	#file=["php/w3af-moth/webroot/moth/w3af/core/wml_parser/form_sql_injection.php"]
	file=files.get_listfiles()
	for fs in file:
		with open(fs,"r") as f:
			print(fs)
			for line in f.readlines():
				line = line.strip()
				if re.match(r'^\s*$', line): continue #If line is empty, continue with the next one
				if line[0] == '#': continue
				#if re.match(r'^(\/\*(\s*|.*?))|((\s*|.*?)\*\/)|(\/\/.*)$',line): continue
			#if re.match(r'([^(htmlespecialchars)]|([^(strip_tags)])|([^(trim)])|([^(htmlentities)]))(\$\_(GET|POST|REQUEST)\[(\"|\')[aA-zZ]+(\"|\')])',line):
				for i in range(0,len(lexpresiones)):
					if lexpresiones[i].search(line):						
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
	lexpresiones = [m,n,o,p,q,r,s,u,v,y,x]
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