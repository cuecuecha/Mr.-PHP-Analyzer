								MR.PHP ANALYZER

 -------------------------------W---I---L---L---K---O---M---M---E---N---!!!.........W---E---L---C---O---M---E---!!!.........------------------------

MR.PHP ANALYZER is a tool for to analyze apps create in PHP language with the objective to find vulnerabilities and to give remmensations for these,where it returns two reports of files, one in csv formt another in html format. 
It was creat of Saine-C.G and Jorge-A.C.H like part of the final project of PBSCG11.
This tool is to made in python, for GNU/Linux platforms. 
 
It can find the following vulnerabilities:

1.- XSS
2.- SQLi
3.- Weak Generation of Session Cookies
4.- Sending Sensitive Information through Unsafe Methods
5.- Implementation of Obsolete Functions
6.- LFI & RFI
7.- Path Traversal
8.- Command Injection
9.- Injection of Source Code

INSTALLATION......

	git clone https://github.com/cuecuecha/Mr.-PHP-Analyzer.git
	In root use:
	bash install.sh

HOW TO USE.......

	mrphpanalyzer -r path.of.the.project  -v number.of.the.vulnerability 
	
	NOTE: For to know the number of the vulnerability, to run mrphpanalyzer --sos
UNINSTALL.....

	In root git use:
		bash uninstall.sh

REPORTS OF FILES.....

1.- CSV
     Obtaining as data:
     ID, NAME, FILE, LINE, ALTERNATIVE

2.- HTML
    The report in html shows the vulnerabilities analyzed, in the case that everything is analyzed, it will show graphs that will help to identify the amount of each vulnerability.

Review the documentation for more detailed information on how to use the tool
