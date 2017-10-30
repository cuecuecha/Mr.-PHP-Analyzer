#!usr/bin/python

import re
import time
import version
import function
import sqlite3
class file_report:
        pass

v=version.get_version()
fl=function.get_function(v)
def create_reportlist ():
	data_report=[]
	report=[]
	file = open("out", "r") 
        lione = file.readline()
        e=lione.split("/")
	file.close()
	data_report.append(e[0])
	data_report.append(time.strftime("%c"))
	#data_report.append(time.strftime("%H:%M:%S"))
	data_report.append(v)
	d_r=tuple(data_report)
	report.append(d_r)
        connection= sqlite3.connect("Fraudatanalyzer.db")
        cursor= connection.cursor()
	cursor.executemany('INSERT INTO reports(name, date_hour, version) VALUES (?,?,?)', report)
	#for e in cursor.execute('SELECT * FROM reports'):
	#	print e 
        connection.commit()
	
#create_reportlist()

def create_re_vul_funclist():
	data_report=[]
	line=[]
	expression=[]
	lines_id=[]
        vul=[]
	exp_func=[]
	id_function=[]
	lines=fl[0]
	funce=fl[1]
	connection= sqlite3.connect("Fraudatanalyzer.db")
        cursor= connection.cursor()
	for o in range(len(funce)):
        	for e in cursor.execute("SELECT  function_id, expression FROM functions WHERE function = '%s'" %funce[o]):
               		f=e[0]
			id_function.append(f)
			ex=e[1]
                        exp_func.append(ex)
	for e in cursor.execute("SELECT  report_id, MAX(date_hour) FROM reports ORDER BY date_hour DESC"):
        	r=list(e)
		id_report=r[0]
	for e in range(len(exp_func)):
		for l in range(len(lines)):
			if re.match(exp_func[e], lines[l]):
				line.append(lines[l])
				expression.append(exp_func[e])
	for ln, ex in zip(line, expression):
                lines_id.append("%s\n%s" % (ln, ex))
	exp_lin=list(set(lines_id))
	for ld in range(len(exp_lin)):
		d=exp_lin[ld].split("\n")
		for e in cursor.execute("SELECT  function_id FROM functions WHERE expression = '%s'" %d[1]):
                        r=list(e)
                	id_func=r[0]
			d.append(id_func)
			del d[1]
			d.append(id_report)
		t=tuple(d)
		data_report.append(t)
	cursor.executemany('INSERT INTO reports_vul_func(line, functionob, report) VALUES (?,?,?)', data_report)
	#for e in cursor.execute('SELECT * FROM reports_vul_func'):
         #       print e 
        connection.commit()
#create_re_vul_funclist()	
