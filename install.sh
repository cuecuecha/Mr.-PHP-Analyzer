#!/bin/sh

# finding the way...

echo "Creating file /opt/mrphpanalyzer" 
	sudo mkdir -pm 777 /opt/mrphpanalyzer
echo "Moving necessary files to /opt/mrphpanalyzer"
	sudo cp -rf ./* /opt/mrphpanalyzer
	sudo cp ./mrphpanalyzer /bin/
	sudo chmod 777 /bin/mrphpanalyzer
echo "Installing to database..."
	cd /opt/mrphpanalyzer/base
	python basecreate.py
	rm basecreate.py
echo "Finished installation... Are you ready?"


