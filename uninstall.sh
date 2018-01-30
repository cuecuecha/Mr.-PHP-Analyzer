#!/bin/bash

# finding the way...
#solo root puede ejecutar el script
if [[ $EUID -ne 0 ]]; then
	echo -e "\n \033[0;31mDebe ejecutarse como root \033[0m\n" 1>&2
	exit 1
fi
	echo "
░░░███████ ]▄▄▄▄▄▄▄▄         'La autocrítica
▂▄▅█████████▅▄▃▂           ☻/   está muy bien,
███████████████████].     /▌     mientras no tenga
 ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..        /\      que ver con uno mismo﻿' "
	echo ""
	echo "Deleting file /opt/mrphpanalyzer" 
		rm -fr /opt/mrphpanalyzer
	echo "Uninstalling from your system"
		rm -f /bin/mrphpanalyzer
	echo "Finished uninstall"


