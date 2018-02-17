import time
import os

userinput = input("What linux distro are you using?  ")
linuxversion = str.lower(userinput)

if linuxversion == "debian":
	debianV = input("Debian 9? y/n")
	if debianV == "n":
		os.system("sed -i 's/DISTRO/debian/g' *")
	else:
		os.system("sed -i 's/DISTRO/debian9/g' *")			
