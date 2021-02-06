import subprocess
import optparse
import re

def get_user_input():
	parse_object = optparse.OptionParser()
	parse_object.add_option("-i","--interface",dest = "interface" , help = "enter your inteface")
	parse_object.add_option("-m","--mac", dest = "mac_address" , help = "enter mac address")

	return parse_object.parse_args()

print("------------->>>>>>>>")

def change_mac_address(user_interface,user_mac_address):
	subprocess.call(["ifconfig",user_interface,"down"])
	subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
	subprocess.call(["ifconfig",user_interface,"up"])


def control_new_mac(interface):

	ifconfig = subprocess.check_output(["ifconfig",interface])
	new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

	if new_mac:
		return new_mac.group(0)
	else:
		return None




(user_input , arguments) = get_user_input()
change_mac_address(user_input.interface , user_input.mac_address)
your_mac=control_new_mac(str(user_input.interface))

if your_mac==user_input.mac_address:
	print("your mac address is changed")

else:
	print("error")

#$python mac_changer-4 -i eth0 -m 00:11:22:33:44:55
#$python mac_changer-4 --interface eth0 --mac 00:11:22:33:44:55 