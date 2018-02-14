import time
from time import sleep
import os

os.system("ping -c 3 8.8.8.8 >> pingresults.txt")

time.sleep(15)
statinfo = os.stat('pingresults.txt')
state = 'false'
		

while state  != 'true':
	if  statinfo.st_size < 200:
		print("network is down")
		os.system("rm pingresults.txt")
		state = 'false'
		os.system("service network restart")
		time.sleep(2)
	else:
		print("network is up")
		state = 'true'

