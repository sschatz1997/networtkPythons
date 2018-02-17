import time
from time import sleep
import os

linuxV = "DISTRO"#this is changed by setup.py

if linuxV == "ubuntu":#they both use ifconfig
	linuxV = "debian"
if linuxV == "debian9": 
	ipset = 'D9'
else:
	ipset = 'ifconfig eth0 >> /test/infconfig.txt'

os.system("sudo ping -c 3 8.8.8.8 > pingresults.txt")


os.system("ifconfig eth0  > /test/ifconfig.txt")	
config = os.stat('/test/ifconfig.txt')
counter = 0 
time.sleep(15)
statinfo = os.stat('/test/pingresults.txt')
state = 'false'

while (state  != 'true') and (counter < 3):
	if  statinfo.st_size < 200:
		print("network is down")
		state = 'false'
		os.system("sudo service networking restart")
		time.sleep(2)
		counter += 1
		
	else:
		print("network is up")
		state = 'true'
		
	if counter == 2 and config.st_size <= 354:
		print("No ip address assigned")

	if counter == 3:
		print("network can't be restarted")	 

os.system("date >> pingresults.txt")
