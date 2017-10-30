#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

class get_generatecvs:
	pass

def get_namecsv(name,id,vul,string,field):
	with open(name+'.csv', 'a') as csvfile:
	    filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    filewriter.writerow(['ID', 'Vulnerability', 'string', 'field'])
	    filewriter.writerow([id,vul,string,field])