
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
		      backgroundColor: "rgba(2,117,216,1)",
		      borderColor: "rgba(2,117,216,1)",
		      data: [36, 0, 8, 41, 21, 4, 0, 0],
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
		          max: 200,
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
		      data: [36, 0,8, 0,0,0,0,0],
		      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
		    }],
		  },
		});
	