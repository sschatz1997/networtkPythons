import time
import os

userinput = input("What linux distro are you using? ")
linuxversion = str.lower(userinput)


if linuxversion == "debian":
	debianV = input("Debian 9? y/n ")
	if debianV == "n":
		os.system("sed -i 's/DISTRO/debian/g' *")
		intf = input("What interface are you using? ")
		interfaceName = str.lower(intf)
		prefix1 = "sed -i 's/INTRF/"
		sufix1 = "/g' *"
		interfaceR  = prefix1 + interfaceName + sufix1
		os.system(interfaceR)
	else:
		os.system("sed -i 's/DISTRO/debian9/g' *")			
		intf = input("What interface are you using? ")
		interfaceName = str.lower(intf)
		prefix1 = "sed -i 's/INTRF/"
		sufix1 = "/g' *"
		interfaceR  = prefix1 + interfaceName + sufix1
		os.system(interfaceR)
