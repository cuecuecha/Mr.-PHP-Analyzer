#!usr/bin/python


import re
import time
import version
import function
import vulnerability
import sqlite3
class file_report:
        pass

def create_reportlist (): #main information of report file (name, date_hour and version of the project)
	data_report=[]
	report=[]
	file = open("/opt/mrphpanalyzer/file/out", "r") #it gets name of the project
        lione = file.readline()
        e=lione.split("/")
	file.close()
	data_report.append(e[1])
	data_report.append((time.strftime("%c"))) #it gets date of the system
	data_report.append(version.get_version()) #it gets version of the project
	d=tuple(data_report) 
	report.append(d)
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
	cursor.executemany('INSERT INTO reports(name, date_hour, version) VALUES (?,?,?)', report) #it inserts information geted in the past into the data base  
	connection.commit()
	
def get_re_now(): #it gets the id of the tuple with current date
	connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	for e in cursor.execute("SELECT  report_id, MAX(date_hour) FROM reports"):
                r=list(e)
                id_report=r[0]
	return id_report
	connection.commit()
def create_re_funclist(): #it gets list of tuples with line, file, function and id_report, and it inserts it into data base 
	fl=function.get_function(version.get_version())
	id_report=get_re_now()
	data_report=[]
	line=[]
	expression=[]
	lines_id=[]
        vul=[]
	exp_func=[]
	id_function=[]
	lines=fl[0]
	funce=fl[1]
	lineh=[]
	fileh=[]
	connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
	for o in range(len(funce)):
        	for e in cursor.execute("SELECT  function_id, expression FROM functions WHERE function = '%s'"  %funce[o]): #it gets id and expression of the obsolete function
               		f=e[0]
			id_function.append(f)
			ex=e[1]
                        exp_func.append(ex)
	for lf in range(len(lines)): #it splits into two list (lineh and fileh)
        	h=lines[lf].split("\n-n")
       		lineh.append(h[0])
		fileh.append(h[1])
	for e in range(len(exp_func)): 
		for l in range(len(lineh)):
			if re.match(exp_func[e], lineh[l]):
				line.append(lineh[l])
				expression.append(exp_func[e])
	for ln, ex, fn in zip(line, expression, fileh): 
                lines_id.append("%s\n.n%s\n.n%s" % (ln, ex, fn))
	exp_lin=list(set(lines_id))
	for ld in range(len(exp_lin)):
		d=exp_lin[ld].split("\n.n")
		for e in cursor.execute("SELECT  function_id FROM functions WHERE expression = '%s'" %d[1]): #it gets id of the expressions
                        r=list(e)
                	id_func=r[0]
			d.append(id_func) #it adds id function into list d 
			del d[1] #it removes regular expression
			d.append(id_report)
		t=tuple(d) #the list becomes in tuple
		data_report.append(t)
	cursor.executemany('INSERT INTO reports_vul_func(line, file, functionob, report) VALUES (?,?,?,?)', data_report) #it inserts into data base 
        connection.commit()

def create_re_vulist(vul): #it gets list of tuples with line, file, vulnerability and id_report, and it inserts it into data base 
        vl=vulnerability.get_vulnerability(vul)
        id_report=get_re_now()
        data_report=[]
	id_vul=[]
        linev=[]
        filev=[]
        connection= sqlite3.connect("/opt/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
        for ld in range(len(vl)): #it gets regular expression and it adds it into linev 
		linev.append(vl[ld][2])
	for d in range(len(linev)):
   		for e in cursor.execute("SELECT  vulnerability_id FROM vulnerabilities WHERE expression = '%s'" %linev[d]): #it gets id of the vulnerability and it adds it into filev
                	r=list(e)
                        id_vul=r[0]
			filev.append(id_vul)
	for l in range(len(vl)): #it adds the id of the report and the id of the vulbnerability  
                vl[l].append(id_report)
        	vl[l].append(filev[l])
		del vl[l][2] #it removes regular expression
		t=tuple(vl[l]) #the list becomes in tuple
                data_report.append(t)
        cursor.executemany('INSERT INTO reports_vul_func(line, file, report, vulnerability) VALUES (?,?,?,?)', data_report)
        connection.commit()

