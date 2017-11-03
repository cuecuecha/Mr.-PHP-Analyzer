#!/usr/bin/python

import version
import argparse
import files
import report
import csvcreate
parser = argparse.ArgumentParser(description='Find vulnerabilities in php code')
parser.add_argument('-r' , nargs=1,  help="root")
parser.add_argument('-v' , nargs=1, help="vulnerability")
parser.add_argument('--sos', action="store_true", help="actions list")
option = parser.parse_args()

if option.r and option.v:
	files.get_files(option.r[0])
	v=version.get_version()
	if option.v[0] is "1":
		report.create_reportlist()
		report.create_re_vulist("2")
		csvcreate.create_report("11")			
	elif option.v[0] is "2":
		if v is "7":
			print"Didn't find obsolete functions"    	
		else:
			report.create_reportlist()
        		report.create_re_funclist()
        		csvcreate.create_report("12")
	elif option.v[0] is "4":
		report.create_reportlist()
                report.create_re_vulist("3")
                csvcreate.create_report("11")

	elif option.v[0] is "6":
		report.create_reportlist()
                report.create_re_vulist("5")
                csvcreate.create_report("11")

	elif option.v[0] is "7":
		report.create_reportlist()
                report.create_re_vulist("6")
                csvcreate.create_report("11")

	elif option.v[0] is "8":
		report.create_reportlist()
                report.create_re_vulist("7")
                csvcreate.create_report("11")

if option.sos:
        print '''
               	Herzlich willkommen bei Mr.-PHPAnalyzer
		Mr.-PHPAnalyzer find vulnerabilities in php code 

                Options:

                1. XSS
                2. OBSOLETE FUNCTIONS
		3. SQLi
		4. SESSION'S COOKIES
		5. SEND SENSIBLE INFORMATION
		6. LFI & RFI
		7. PATH TRAVERSAL
		8. COMMAND INJECTION
		9. SOURCE CODE INJECTION
		
        '''

