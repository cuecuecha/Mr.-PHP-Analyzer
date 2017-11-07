#!/usr/bin/python
# -*- coding: utf-8 -*-
from webbrowser import open_new_tab
import datetime
class get_html:
	pass

def createhtml(dato, data):
	ahora = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
	nombreArchivo = ahora + '.html'
	f = open('reportHTML/'+nombreArchivo,'a')
	wrapper = """
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
	</head>

	<body class="fixed-nav sticky-footer bg-dark" id="page-top">
	  <!-- Navigation-->
	  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
	    <a class="navbar-brand" href="index.html">Mr. PHP Analyzer</a>
	    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
	      <span class="navbar-toggler-icon"></span>
	    </button>
	    <div class="collapse navbar-collapse" id="navbarResponsive">
	      <ul class="navbar-nav navbar-sidenav" id="exampleAccordion">
	        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Current Report">
	          <a class="nav-link" href="index.html">
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
	      <div class="breadcrumb" style="height: 350px;">
	        <img class="img-responsive" src="img/cert.png" alt="UNAM-CERT" style="display: block; margin:auto; width: 25%;">
	      </div>
	      
	      <!-- Icon Cards-->
	      <div class="row">
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white sqli o-hidden h-100">
	            <div class="card-body">
	                <div class="col-md-4">
	                    <h1 style="text-align:center;">0</h1>
	                </div>
	                <div class="col-md-8">
	                    <h1>SQLi</h1>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white xss o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">0</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h1>XSS</h1>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white cookie o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-6">
	                        <h1 style="text-align:center;">26</h1>
	                    </div>
	                    <div class="col-md-6">
	                        <h4>G. débil Cookies</h4>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white sendinf o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">26</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h4>Send weak Info</h4>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white functd o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">{}</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h4>Deprecated Functions</h4>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white lfirfi o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">26</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h2>LFI & RFI</h2>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white pathtraversal o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">26</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h3>Path Traversal</h3>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white injecom o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;"></h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h4>Injection of commands</h4>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	        <div class="col-xl-3 col-sm-6 mb-3">
	          <div class="card text-white injectcode o-hidden h-100">
	            <div class="card-body">
	                <div class="row">
	                    <div class="col-md-4">
	                        <h1 style="text-align:center;">26</h1>
	                    </div>
	                    <div class="col-md-8">
	                        <h5>Injection of source code</h5>
	                    </div>
	                </div>
	            </div>
	          </div>
	        </div>
	      </div>

	      <div class="row">
	        <div class="col-lg-8">
	          <!-- Example Bar Chart Card-->
	          <div class="card mb-3">
	            <div class="card-header">
	              <i class="fa fa-bar-chart"></i> Bar Chart Example</div>
	            <div class="card-body">
	              <div class="row">
	                <div class="col-sm-8 my-auto">
	                  <canvas id="myBarChart" width="100" height="50" style="display: block; height: 299px; width: 554px;"></canvas>
	                </div>
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
	              <i class="fa fa-pie-chart"></i> Pie Chart Example</div>
	            <div class="card-body">
	              <canvas id="myPieChart" width="100%" height="100"></canvas>
	            </div>
	            <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
	          </div>
	        </div>
	      </div>
	      <!-- Vulnerabilities
	      -->

	    <div class="card mb-3">
	        <div class="card-header">
	          <i class="fa fa-table"></i>Table of Vulnerabilities
	         </div>
	        <div class="card-body">
	          <div class="table-responsive">
	            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
	              <thead>
	                <tr>
	                  <th>ID</th>
	                  <th>Vulnerability</th>
	                  <th>Path</th>
	                  <th>Deprecated Function</th>
	                  <th>Function Alternative</th>
	                </tr>
	              </thead>
	              <tfoot>
	                <tr>
	                  <th>ID</th>
	                  <th>Vulnerability</th>
	                  <th>Path</th>
	                  <th>Deprecated Function</th>
	                  <th>Function Alternative</th>
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
	    </div>



	    <!-- /.container-fluid-->
	    <!-- /.content-wrapper-->
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
	    <!-- Custom scripts for this page-->
	    <script src="js/sb-admin-datatables.min.js"></script>
	    <script>{}</script>
	  </div>
	</body>

	</html>

	"""



	estadisticas = """
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
		    labels: ["SQLi", "XSS", "GDCS", "M. inseguros", "F. Depreciadas", "LFI y RFI","P. Traversal", "I. Comandos","I. Código"],
		    datasets: [{
		      label: "Revenue",
		      backgroundColor: "rgba(2,117,216,1)",
		      borderColor: "rgba(2,117,216,1)",
		      data: [4215, 5312, 6251, 7841, 9821, 14984],
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
		          max: 15000,
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
		    labels: ["SQLi", "XSS", "GDCS", "M. inseguros", "F. Depreciadas", "LFI y RFI","P. Traversal", "I. Comandos","I. Código"],
		    datasets: [{
		      data: [12.21, 15.58, 11.25, 8.32],
		      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
		    }],
		  },
		});

	"""

	#js = estadisticas.format()
	todo = wrapper.format(dato,data,estadisticas)
	f.write(todo)
	f.close()




