#!/bin/bash
#Init
FILE="/tmp/out.$$"
GREP="/bin/grep"
#solo root puede ejecutar el script
if [[ $EUID -ne 0 ]]; then
	echo "Debe ejecutarse como root" 1>&2
	exit 1
fi
	echo "eres root"
