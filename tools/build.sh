#!/bin/sh
# Arma la demo a partir del sistema de SebaChavez Car Service.
# Uso: sh tools/build.sh /ruta/a/Sebachavezcarervice/tools/base.html
set -e
D=$(dirname "$0")
python3 "$D/mk_demo.py" "$1" index.html
python3 "$D/demo_patch.py" index.html
