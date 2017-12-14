#!/usr/bin/python
# -*- coding: utf-8 -*-
from webbrowser import open_new_tab
import datetime
import time
import os.path
from random import randint
# -*- coding: utf-8 -*-
__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"
class get_html:
	pass

times = datetime.datetime.now().strftime("%a%Y%m%d-%H%M%S")
ahora = datetime.datetime.now().strftime("%a%Y%m%d-%H")
nombreArchivo = times+'.html'
#funcion para crear reporte

def creareporte():
	reporte = open('/opt/mrphpanalyzer/reportesHTML/'+nombreArchivo,'a')
	return reporte



#funcion donde se crea sólo el header del reporte
def headerhtml(reporte):
	ahora = datetime.datetime.now().strftime("%a%Y%m%d-%H")
	nombreArchivo = ahora+'.html'
	header = """
			<!DOCTYPE html>
			<html lang="en">

			<head>
			  <meta charset="utf-8">
			  <meta http-equiv="X-UA-Compatible" content="IE=edge">
			  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
			  <meta name="description" content="">
			  <meta name="author" content="">
			  <title>Mr. PHP Analyzer</title>
			  <!-- Bootstrap core CSS-->
			  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
			  <!-- Custom fonts for this template-->
			  <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
			  <!-- Page level plugin CSS-->
			  <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">
			  <!-- Custom styles for this template-->
			  <link href="css/sb-admin.css" rel="stylesheet">
			  <link href="css/style.css" rel="stylesheet">
  			  <link rel="shortcut icon" type="text/css" href="img/pirate.ico">

			</head>

			<body class="fixed-nav sticky-footer bg-dark" id="page-top">
			  <!-- Navigation-->
			  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
			  <img src="img/pirate.png" style="width: 4%;"> 
			    <a class="navbar-brand" href="index.html">Mr. PHP Analyzer</a>
			    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
			      <span class="navbar-toggler-icon"></span>
			    </button>
			    <div class="collapse navbar-collapse" id="navbarResponsive">
			      <ul class="navbar-nav navbar-sidenav" id="exampleAccordion" style="top: 16px;">
			        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Current Report">
			          <a class="nav-link" href="{}">
			            <i class="fa fa-fw fa-dashboard"></i>
			            <span class="nav-link-text">Current Report</span>
			          </a>
			        </li>
			        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="History">
			          <a class="nav-link" href="history.html">
			            <i class="fa fa-fw fa-area-chart"></i>
			            <span class="nav-link-text">History</span>
			          </a>
			        </li>
			      </ul>
			      <ul class="navbar-nav sidenav-toggler">
			        <li class="nav-item">
			          <a class="nav-link text-center" id="sidenavToggler">
			            <i class="fa fa-fw fa-angle-left"></i>
			          </a>
			        </li>
			      </ul>

			    </div>
			  </nav>
			  <div class="content-wrapper">
			    <div class="container-fluid">
			      <!-- Breadcrumbs-->
			      <div class="breadcrumb" style="height: auto;">
			        <img class="img-responsive" src="img/cert.png" alt="UNAM-CERT" style="display: block; margin:auto; width: 25%;">
			      </div>
			   """
	reportes = header.format(nombreArchivo)
	reporte.write(reportes)   

#funcion donde sea crea el canvas de las gráficas
def graphic(reporte):
	reporte.write("""
		<div class="row">
		  <div class="col-lg-8">
		    <!-- Example Bar Chart Card-->
		    <div class="card mb-3">
		      <div class="card-header">
		        <i class="fa fa-bar-chart"></i> Vulnerabilities</div>
		      <div class="card-body">
		        <div class="row">
		          
		            <canvas id="myBarChart" width="100" height="50"></canvas>
		          

		        </div>
		      </div>
		      <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
		    </div>
		    <!-- Card Columns Example Social Feed-->
		    
		  </div>
		  <div class="col-lg-4">
		    <!-- Example Pie Chart Card-->
		    <div class="card mb-3">
		      <div class="card-header">
		        <i class="fa fa-pie-chart"></i>Stadistics</div>
		      <div class="card-body">
		        <canvas id="myPieChart" width="100%" height="150"></canvas>
		      </div>
		      <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
		    </div>
		  </div>
		</div>
		""")

#funcion donde reune los datos para la gráficas

def jsgraphic(vulnes):
	reporte = open('/opt/mrphpanalyzer/reportesHTML/js/sb-admin-charts.js','w')
	
	reporte.write("""
		// Chart.js scripts
		// -- Set new default font family and font color to mimic Bootstrap's default styling
		Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
		Chart.defaults.global.defaultFontColor = '#292b2c';
		// -- Area Chart Example

		// -- Bar Chart Example
		var ctx = document.getElementById("myBarChart");
		var myLineChart = new Chart(ctx, {
		  type: 'bar',
		  data: {
		    labels: ["SQLi", "XSS", "Session Cookie", "Send S. Info", "LFI&RFI", "P. Traversal", "I. Comandos","I. Código"],
		    datasets: [{
		      label: "Revenue",
		      backgroundColor: ['#F58C46', '#FBF302', '#3D8CFA', '#FBAD54', '#F5BE82', '#26C328', '#FD0000', '#FB5138'],
		      borderColor: "rgba(2,117,216,1)",
		      data: [%s, %s, %s, %s, %s, %s, %s, 0],
		    }],
		  },
		  options: {
		    scales: {
		      xAxes: [{
		        time: {
		          unit: 'unit'
		        },
		        gridLines: {
		          display: false
		        },
		        ticks: {
		          maxTicksLimit: 15
		        }
		      }],
		      yAxes: [{
		        ticks: {
		          min: 0,
		          max: %s,
		          maxTicksLimit: 5
		        },
		        gridLines: {
		          display: true
		        }
		      }],
		    },
		    legend: {
		      display: false
		    }
		  }
		});
		// -- Pie Chart Example
		var ctx = document.getElementById("myPieChart");
		var myPieChart = new Chart(ctx, {
		  type: 'pie',
		  data: {
		    labels: ["SQLi", "XSS", "Session Cookie", "Send S. Info", "LFI&RFI", "P. Traversal", "I. Comandos","I. Código"],
		    datasets: [{
		      data: [%s, %s,%s, %s,%s,%s,%s,0],
		      backgroundColor: ['#F58C46', '#FBF302', '#3D8CFA', '#FBAD54', '#F5BE82', '#26C328', '#FD0000', '#FB5138'],
		    }],
		  },
		});
	"""%(str(vulnes.get('1')),str(vulnes.get('2')), str(vulnes.get('3')),str(vulnes.get('4')),str(vulnes.get('5')),
		str(vulnes.get('6')),str(vulnes.get('7')), str(max(vulnes.values())),
		str(vulnes.get('1')),str(vulnes.get('2')), str(vulnes.get('3')),str(vulnes.get('4')),str(vulnes.get('5')),
		str(vulnes.get('6')),str(vulnes.get('7'))
		) )

#funcion donde imprime el total de cada vulnerabilidad
def cardhtml(tvul, reporte):
	reporte.write("""
		%s
		"""%tvul)


#funcion para crearl la tabla de funcions obsoletas
def tablefhtml(table,reporte, option):
	tob="""
	<div class="card mb-3" id="tab{}" style="display:none;">
	  <div class="card-header">
	    <i class="fa fa-table"></i>Table of Functions Obsoletes</div>
	  <div class="card-body">
	    <div class="table-responsive">
	      <table class="table table-bordered" id="dataTable9" width="100%" cellspacing="0">
	        <thead>
	          <tr>
	            <th>File</th>
	            <th>Function Obsolete</th>
	            <th>Function Alternative</th>
	          </tr>
	        </thead>
	        <tfoot>
	          <tr>
	            <th>File</th>
	            <th>Function Obsolete</th>
	            <th>Function Alternative</th>
	          </tr>
	        </tfoot>
	        <tbody>
	          {}
	        </tbody>
	      </table>
	    </div>
	  </div>
	  <div class="card-footer small text-muted">Updated {}</div>
	</div>
	

	"""



	
	#js = estadisticas.format()
	reportes = tob.format(option,table,times)
	reporte.write(reportes)


#funcion para crear la tabla de cada vulnerabilidad
def tablehtml(table,reporte, option):
	n="""
	<div class="card mb-3" id="tab{}" style="display:none;">
	  <div class="card-header">
	    <i class="fa fa-table"></i>Table of Vulnerabilities</div>
	  <div class="card-body">
	    <div class="table-responsive">
	      <table class="table table-bordered" id="dataTable{}" width="100%" cellspacing="0">
	        <thead>
	          <tr>
	            <th>Line Number</th>
	            <th>Path</th>
	            <th>Affected strings</th>
	          </tr>
	        </thead>
	        <tfoot>
	          <tr>
	          <th>Line Number</th>
	          <th>Path</th>
	          <th>Affected strings</th>
	          </tr>
	        </tfoot>
	        <tbody>
	          {}
	        </tbody>
	      </table>
	    </div>
	  </div>
	  <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
	</div>
	

	"""



	
	#js = estadisticas.format()
	reportes = n.format(option,option,table)
	reporte.write(reportes)





def footer(reporte):
	reporte.write("""
		<footer class="sticky-footer">
		  <div class="container">
		    <div class="text-center">
		      <small>Copyright © Mr. PHP Analyzer 2017</small>
		    </div>
		  </div>
		</footer>
		<!-- Scroll to Top Button-->
		<a class="scroll-to-top rounded" href="#page-top">
		  <i class="fa fa-angle-up"></i>
		</a>

		</div>
		<!-- Bootstrap core JavaScript-->
		<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
		<!-- Core plugin JavaScript-->
		<script src="vendor/jquery-easing/jquery.easing.min.js"></script>
		<!-- Page level plugin JavaScript-->
		<script src="vendor/chart.js/Chart.min.js"></script>
		<script src="vendor/datatables/jquery.dataTables.js"></script>
		<script src="vendor/datatables/dataTables.bootstrap4.js"></script>
		<!-- Custom scripts for all pages-->
		<script src="js/sb-admin.min.js"></script>
		<script src="js/sb-admin-charts.js"></script>
		<script src="js/sb-admin-tables.js"></script>
	""")


def scriptable(option,reporte):
	reporte.write("""
		<script>
			var sd%s = document.getElementById('tab%s');
			function id%s() {
			if (sd%s.style.display === 'none') {
				sd%s.style.display = 'block';
				}else {
					sd%s.style.display = 'none';
				}
			}

		</script>
		"""%(option,option,option,option,option,option))


def scriptsearchtable(option):
	reporte = open('/opt/mrphpanalyzer/reportesHTML/js/sb-admin-tables.js','a')
	reporte.write("""
			$(document).ready(function() {
			  $('#dataTable%s').DataTable();
			});
		"""%option)


def escribereporte(reporte, info):
	reporte.write("""
		%s
		"""%info)

def listfiles():
	print("\n\nREPORTE HTML\n\n")
	os.system('find /opt/mrphpanalyzer/reportesHTML/'+nombreArchivo)
	print("\n\n\n")