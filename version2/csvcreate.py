#!/usr/bin/python
import csv
import sqlite3

class open_csv:
	pass

def get_csv(id,name,date,version,line,funcob,alt):
	with open(name+"_"+date+'.csv', 'a') as csvfile:
	    filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    filewriter.writerow(['ID',  'NAME',  'DATE',       'VERSION',  'LINE',                    'OBSOLETE FUNCTION',    'ALTERNATIVE'])
	    filewriter.writerow([id,  name,  date,  version,   line,  funcob,   alt])
def create_report ():
	int=[]
        connection= sqlite3.connect("Fraudatanalyzer.db")
        cursor= connection.cursor()         
	for e in cursor.execute('SELECT reports_vul_func.re_vul_func_id AS id,  reports.name AS name, reports.date_hour AS date, reports.version AS version, reports_vul_func.line AS line, functions.function AS funcob, functions.alternative AS alt FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report INNER JOIN functions ON functions.function_id = reports_vul_func.functionob'):
		data=list(e)
		int.append(data)
	#print int
	for n in range(len(int)):
		t=int[n]
		get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
		
        connection.commit()
#create_report()
