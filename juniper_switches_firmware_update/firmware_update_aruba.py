import subprocess
import sys
import os
import time

print "Staging script for Juniper switches \n"
print "Scanning for active IP addresses \n"

while True:		
	starting_address = raw_input("Please enter X as starting address (192.168.0.X): ")
	if int(starting_address) < 256 and int(starting_address) >= 0:
		print ("The starting address is 192.168.0." + starting_address)
		break
	else:
		print ("The given starting address is out of range.")

while True:
	ending_address = raw_input("Please enter X as ending address (192.168.0.X): ")
	if int(ending_address) > int(starting_address) and int(ending_address) <= 255 and int(ending_address) > 0:
		print ("The ending address is 192.168.0." + ending_address)
		ending_address = ending_address + 1
		break
	else:
		print ("The given ending address is not possible.")
		continue

for x in range(int(starting_address),int(ending_address)):
	print ("Pinging 192.168.0." + str(x))
	HOST_UP = True if os.system("ping -c 1 192.168.0." + str(x)) is 0 else False
	if HOST_UP == True:
		print ("IP 192.168.0."+ str(x) + " is up")
		file = open("ip-addr.txt", "w")
		file.write("192.168.0." + str(x))
		file.close()
		print "Starting staging script (staging_script.sh)"
		var1 = "192.168.0." + str(x)
		print var1
		subprocess.call(['gnome-terminal', '-x','./staging_script.sh', var1])
	elif HOST_UP == False:
		print ("IP 192.168.0."+ str(x) + " is down")

read_file = open("ip-addr.txt", "r")
print read_file.readline()
print "End of script"