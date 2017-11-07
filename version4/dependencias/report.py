#!usr/bin/python


import re
import time
import version
import function
import vulnerability
import sqlite3
class file_report:
        pass

def create_reportlist ():
	data_report=[]
	report=[]
	file = open("/root/mrphpanalyzer/archivos/out", "r") 
        lione = file.readline()
        e=lione.split("/")
	file.close()
	data_report.append(e[2])
	data_report.append((time.strftime("%c")))
	data_report.append(version.get_version())
	d=tuple(data_report)
	report.append(d)
        connection= sqlite3.connect("/root/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
	cursor.executemany('INSERT INTO reports(name, date_hour, version) VALUES (?,?,?)', report)
	#for e in cursor.execute('SELECT * FROM reports'):
	#	print e 
        connection.commit()
	
#create_reportlist()
def get_re_now():
	connection= sqlite3.connect("/root/mrphpanalyzer/base/Fraudatanalyzer.db")
        cursor= connection.cursor()
	for e in cursor.execute("SELECT  report_id, MAX(date_hour) FROM reports"):
                r=list(e)
                id_report=r[0]
	return id_report
	connection.commit()
def create_re_funclist():
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
	connection= sqlite3.connect("/root/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
	for o in range(len(funce)):
        	for e in cursor.execute("SELECT  function_id, expression FROM functions WHERE function = '%s'"  %funce[o]):
               		f=e[0]
			id_function.append(f)
			ex=e[1]
                        exp_func.append(ex)
	for lf in range(len(lines)):
        	h=lines[lf].split("\n")
       		lineh.append(h[0])
		fileh.append(h[1])
	for e in range(len(exp_func)):
		for l in range(len(lineh)):
			if re.match(exp_func[e], lineh[l]):
				line.append(lineh[l])
				expression.append(exp_func[e])
	for ln, ex, fn in zip(line, expression, fileh):
                lines_id.append("%s\n%s\n%s" % (ln, ex, fn))
	exp_lin=list(set(lines_id))
	#print exp_lin
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
	cursor.executemany('INSERT INTO reports_vul_func(line, file, functionob, report) VALUES (?,?,?,?)', data_report)
	#for e in cursor.execute('SELECT * FROM reports_vul_func'):
        #        print e 
        connection.commit()

def create_re_vulist(vul):
        vl=vulnerability.get_vulnerability(vul)
        id_report=get_re_now()
        data_report=[]
	id_vul=[]
        linev=[]
        filev=[]
        connection= sqlite3.connect("/root/mrphpanalyzer/base/Fraudatanalyzer.db")
	connection.text_factory=str
        cursor= connection.cursor()
        for ld in range(len(vl)):
		linev.append(vl[ld][2])
	for d in range(len(linev)):
   		for e in cursor.execute("SELECT  vulnerability_id FROM vulnerabilities WHERE expression = '%s'" %linev[d]):
                	r=list(e)
                        id_vul=r[0]
			filev.append(id_vul)
	for l in range(len(vl)):
                vl[l].append(id_report)
        	vl[l].append(filev[l])
		del vl[l][2]
		t=tuple(vl[l])
                data_report.append(t)
	#print data_report
        cursor.executemany('INSERT INTO reports_vul_func(line, file, report, vulnerability) VALUES (?,?,?,?)', data_report)
       	#for e in cursor.execute('SELECT * FROM reports_vul_func'):
        #	print e 

        connection.commit()


#create_re_funclist()	
#create_re_vulist()
#get_re_now()

