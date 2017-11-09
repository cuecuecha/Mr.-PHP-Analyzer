#!/usr/bin/python
import csv
import sqlite3
import os
class open_csv:
	pass 

def first_line(name,date):
	fl="/opt/mrphpanalyzer/reportes/"+name+"_"+date+'.csv'
        r=open(fl, 'w')
        r.write("ID  NAME   			          	FILE                 					LINE                        ALTERNATIVE \n")
        r.close()
def get_csv(name,date,id,funcob,file,line,alt):
	fl="/opt/mrphpanalyzer/reportes/"+name+"_"+date+'.csv'
	with open(fl, 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    	filewriter.writerow([id, funcob, file, line, alt])
def get_report_func ():
	int=[]
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()         
	for e in cursor.execute('SELECT  MAX(date_hour) FROM reports'):
		date=e[0]
	for e in cursor.execute("SELECT  reports.name AS name, reports.date_hour AS date, functions.function_id AS id, functions.function AS funcob, reports_vul_func.file AS file, reports_vul_func.line AS line, functions.alternative AS alt FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report INNER JOIN functions ON functions.function_id = reports_vul_func.functionob WHERE date_hour = '%s'" %date):		
		data=list(e)		
		int.append(data)
	# esta consulta sirve para sacar el total de lineas con funciones obsoletas, para las vulnerabilidades se hace algo similar 		
	for e in cursor. execute("SELECT count(functionob) FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report WHERE date_hour='%s'" %date):
		nt=e[0]
	return int
        connection.commit()

def get_report_vul ():
        vit=[]
        connection= sqlite3.connect("opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor() 
	for e in cursor.execute('SELECT  MAX(date_hour) FROM reports'):
                date=e[0]        
        for e in cursor.execute("SELECT  reports.name AS name, reports.date_hour AS date, names_vul.name_vul_id AS id, names_vul.name AS funcob, reports_vul_func.file AS file, reports_vul_func.line AS line, recommendations.liga AS alt FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report INNER JOIN vulnerabilities ON vulnerabilities.vulnerability_id = reports_vul_func.vulnerability INNER JOIN names_vul ON names_vul.name_vul_id = vulnerabilities.name INNER JOIN recommendations ON recommendations.recommendation_id = vulnerabilities.recommendation WHERE date_hour = '%s'" %date):
                data=list(e)
                vit.append(data)
        return vit
        connection.commit()

def create_report(opcion):
	if opcion is "10":
		int=get_report_func()
		vit=get_report_vul()
		first_line(int[0][0],int[0][1])
        	for n in range(len(int)):
                	t=int[n]
                	get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
		for n in range(len(vit)):
                	t=vit[n]
                	get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
	elif opcion is "11":
		vit=get_report_vul()
                first_line(vit[0][0],vit[0][1])
		for n in range(len(vit)):
                        t=vit[n]
                        get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
	elif opcion is "12":
		int=get_report_func()
		first_line(int[0][0],int[0][1])
                for n in range(len(int)):
                        t=int[n]
                        get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
#create_report("12")

