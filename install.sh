#!/bin/bash

# finding the way...
#solo root puede ejecutar el script
if [[ $EUID -ne 0 ]]; then
	echo -e "\n \033[0;31mDebe ejecutarse como root \033[0m\n" 1>&2
	exit 1
fi
	echo "Creating file /opt/mrphpanalyzer" 
		mkdir -pm 777 /opt/mrphpanalyzer
	echo "Moving necessary files to /opt/mrphpanalyzer"
		cp -rf ./* /opt/mrphpanalyzer
		cp ./mrphpanalyzer /bin/
		chmod 777 /bin/mrphpanalyzer
	echo "Installing to database..."
		cd /opt/mrphpanalyzer/base
		python basecreate.py
		rm basecreate.py
	echo "Finished installation... Are you ready?"


