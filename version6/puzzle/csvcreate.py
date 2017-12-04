#!/usr/bin/python
import csv
import sqlite3
import generateHtml
import os
class open_csv:
	pass 

def first_line(name,date): #creation of report file
	fl="/opt/mrphpanalyzer/reports/"+name+"_"+date+'.csv'
        r=open(fl, 'w')
        r.write("ID  NAME   			          	FILE                 					LINE                        ALTERNATIVE \n")
        r.close()
def get_csv(name,date,id,funcob,file,line,alt): #insertion of the information in report file in csv format
	fl="/opt/mrphpanalyzer/reports/"+name+"_"+date+'.csv'
	with open(fl, 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    	filewriter.writerow([id, funcob, file, line, alt])
def get_report_func (): #it collects all selected information of data base  
	int=[]
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
	for e in cursor.execute('SELECT  MAX(date_hour) FROM reports'): #it selects the current date and saves in list date
		date=e[0]
	for e in cursor.execute("SELECT  reports.name AS name, reports.date_hour AS date, functions.function_id AS id, functions.function AS funcob, reports_vul_func.file AS file, reports_vul_func.line AS line, functions.alternative AS alt FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report INNER JOIN functions ON functions.function_id = reports_vul_func.functionob WHERE date_hour = '%s'" %date):		
		data=list(e)
		int.append(data) #it selects name, date-hour, function_id, function, file, line and alternative, this information saves in list int
	return int
        connection.commit()

def get_report_vul (): #it collects all selected information of data base
        vit=[]
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor() 
	for e in cursor.execute('SELECT  MAX(date_hour) FROM reports'): #it selects the current date and saves in list date
                date=e[0]        
        for e in cursor.execute("SELECT  reports.name AS name, reports.date_hour AS date, names_vul.name_vul_id AS id, names_vul.name AS funcob, reports_vul_func.file AS file, reports_vul_func.line AS line, recommendations.liga AS alt FROM reports_vul_func INNER JOIN reports ON reports.report_id = reports_vul_func.report INNER JOIN vulnerabilities ON vulnerabilities.vulnerability_id = reports_vul_func.vulnerability INNER JOIN names_vul ON names_vul.name_vul_id = vulnerabilities.name INNER JOIN recommendations ON recommendations.recommendation_id = vulnerabilities.recommendation WHERE date_hour = '%s'" %date):
                data=list(e)
                vit.append(data) #it selects name, data_hour, name_vul_id, vulnerability, line, recommendation and file, this information saves in list vit 
        return vit
        connection.commit()

def create_report(opcion):
        vulx = " "
        vuldx = " "
	if opcion is "10": #this option gets the report file of the vulnerabilities and obsolete functions
		int=get_report_func()
		vit=get_report_vul()
		if int: #if the list int has elements,it will create report file with obsolete functions 
			first_line(int[0][0],int[0][1]) #it takes the first element of the  two-dimensional arrangement 
        		for n in range(len(int)): 
                		t=int[n]
                		get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6]) 
                        	vulx += '<tr>\n'
                        	vulx += '<td>'+str(t[4])+'</td>\n'
                        	vulx += '<td>'+str(t[5])+'</td>\n'   
                        	vulx += '<td>'+str(t[6])+'</td>\n</tr>' 
                	generateHtml.tablefhtml(vulx,generateHtml.creareporte(),"obs") 
                	generateHtml.scriptable("obs", generateHtml.creareporte())
			if vit: #if the list int and vit have elements, it will create report file with obsolete functions and vulnerabilities 
				for n in range(len(vit)):
                			t=vit[n]
                			get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
			else: # the list int has elements but vit does not have element, it will create report file with obsolete functions 
				print "it did not find vulnerabilities"
		else: #if the list int does not have elements but vit has element, it will create report file with vulnerabilities
			print "it dit not find obsolete functions"
			if vit:
                                for n in range(len(vit)):
                                        t=vit[n]
                                        get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
                        else: # if the list int and vit do not elements, it will not create report file
                                print "it dit not find vulnerabilities"
	elif opcion is "11":
		vit=get_report_vul()
		if vit:
                	first_line(vit[0][0],vit[0][1])
			for n in range(len(vit)):
                        	t=vit[n]
                        	get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
		else:
			print "it dit not find vulnerabilities"
	elif opcion is "12":
		int=get_report_func()
		if int:
			first_line(int[0][0],int[0][1])
                	for n in range(len(int)):
                        	t=int[n]
                        	get_csv(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
                        	vulx += '<tr>\n'
                        	vulx += '<td>'+str(t[3])+'</td>\n'
                        	vulx += '<td>'+str(t[4])+'</td>\n'   
                        	vulx += '<td>'+str(t[2])+'</td>\n'   
                        	vulx += '<td>'+str(t[5])+'</td>\n</tr>' 
	        	generateHtml.tablefhtml(vulx,generateHtml.creareporte(),"obs") 
	        	generateHtml.scriptable("obs", generateHtml.creareporte())
		else:
			print "it dit not find obsolete functions"

