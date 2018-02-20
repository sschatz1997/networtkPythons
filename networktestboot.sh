#! /bin/sh
# /etc/init.d/

sleep 20
xfce4-terminal -e 'sh -ic "python3 networktest.py"' -H


exit 1
