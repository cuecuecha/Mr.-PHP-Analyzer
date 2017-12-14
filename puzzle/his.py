#!usr/bin/python
# -*- coding: utf-8 -*-

__author__="Coronado Gozain Saine, Hernandez Cuecuecha Jorge Alberto"
__copyright__="Copyright 2017, UNAM-CERT"
__license__="UNAM CERT"
__version__="1.0"
__status__="Prototype"

import glob
reporte = open('/opt/mrphpanalyzer/reportesHTML/history.html','w')
a = glob.glob("/opt/mrphpanalyzer/reportesHTML/*.html")

reporte.write ("""
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

	   """)
b = " "
if a:
	for elem in a:
		if not "history.html" in elem:
			ap = '<a href="'+str(elem)+'">'+str(elem)+'</a> <br>'
			b += str(ap)
	reporte.write("""
		%s
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
	"""%str(b))

else: 
	reporte.write("""
		<h1>No hay archivos</h1>
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
