
import version
import argparse
import files
import report
import csvcreate
import vulnerability
import generateHtml
import os
import threading
# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"
parser = argparse.ArgumentParser(description='Finds vulnerabilities in php code')
parser.add_argument('-r' , nargs=1,  help="path")
parser.add_argument('-v' , nargs=1, help="vulnerability")
parser.add_argument('--sos', action="store_true", help="actions list")
option = parser.parse_args()
try:
	a=option.r[0].rsplit("/")
	pag=a[-2]
except TypeError:
	print ""
if option.r and option.v: #if option.r and option.v have some value, it will run functions depending of the options 
	files.get_files(option.r[0])
	v=version.get_version()
	if option.v[0] is "1": #for the option sqli, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
		report.create_re_vulist("1")
		csvcreate.create_report("11")
		generateHtml.footer(generateHtml.creareporte())	
	elif option.v[0] is "2": #for the option xss, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
		report.create_re_vulist("2")
		csvcreate.create_report("11")	
		generateHtml.footer(generateHtml.creareporte())		
	elif option.v[0] is "3": #for the option session's cookies, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
	        report.create_re_vulist("3")
	        csvcreate.create_report("11")
		generateHtml.footer(generateHtml.creareporte())
	elif option.v[0] is "4": #for the option send sensible information, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
		report.create_re_vulist("4")
		csvcreate.create_report("11")
		generateHtml.footer(generateHtml.creareporte())
	elif option.v[0] is "5": #for the option LFI & RFI, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
                report.create_re_vulist("5")
                csvcreate.create_report("11")
                generateHtml.footer(generateHtml.creareporte())
	elif option.v[0] is "6": #for the option path traversal, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
                report.create_re_vulist("6")
                csvcreate.create_report("11")
                generateHtml.footer(generateHtml.creareporte())
	elif option.v[0] is "7": #for the option command injection, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
                report.create_re_vulist("7")
                csvcreate.create_report("11")
                generateHtml.footer(generateHtml.creareporte())
	elif option.v[0] is "8": #for the option code injection, only this vulnerability
		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
		generateHtml.list_files(option.r[0],generateHtml.creareporte())
		report.create_reportlist()
		report.create_re_vulist("8")
		csvcreate.create_report("11")
		generateHtml.footer(generateHtml.creareporte())

	elif option.v[0] is "9": #for the option obsolete functions only these
		if v is "7":
			print"Didn't find obsolete functions"    	
		else:
        		generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
        		generateHtml.list_files(option.r[0],generateHtml.creareporte())
			report.create_reportlist()
        		report.create_re_funclist()
        		csvcreate.create_report("12")
        		generateHtml.footer(generateHtml.creareporte())	


elif option.r: #if option.r has some value but option.v does not have, it will run functions of all vulnerabilities  
	generateHtml.headerhtml(generateHtml.creareporte(), a[-2])
	generateHtml.list_files(option.r[0],generateHtml.creareporte())
	generateHtml.graphic(generateHtml.creareporte())
	#prov=["1","2","3","4","5","6","7","8"]
	files.get_files(option.r[0])
        v=version.get_version()
	report.create_reportlist()
	#for o in range(len(prov)):
        #	report.create_re_vulist(prov[o])
	threads = []
	thread = threading.Thread(target=report.create_re_vulist, args=("1",)) 
    	thread.start()
    	threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("2",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("3",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("4",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("5",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("6",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("7",))
        thread.start()
        threads.append(thread)
	thread = threading.Thread(target=report.create_re_vulist, args=("8",))
        thread.start()
        threads.append(thread)

	for thread in threads:
    		thread.join()

	if v is "7":
        	print"Didn't find obsolete functions"           
       	else:
		report.create_re_funclist()
		csvcreate.create_report("10")
		generateHtml.footer(generateHtml.creareporte())
			

if option.sos:
        print '''
               	Herzlich willkommen bei Mr.-PHPAnalyzer
		Mr.-PHPAnalyzer find vulnerabilities in php code 

                Options:

		1. SQLi
                2. XSS
		3. SESSION'S COOKIES
		4. SEND SENSIBLE INFORMATION
		5. LFI & RFI
		6. PATH TRAVERSAL
		7. COMMAND INJECTION
		8. SOURCE CODE INJECTION
                9. OBSOLETE FUNCTIONS
		
        '''

os.system('python /opt/mrphpanalyzer/puzzle/his.py')
try:
	generateHtml.listfiles()
except NameError:
	print ""

def nameProject():
	print a[-2]
