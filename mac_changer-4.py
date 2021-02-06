import subprocess
import optparse

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

(user_input , arguments) = get_user_input()
change_mac_address(user_input.interface , user_input.mac_address)

#$python mac_changer-4 -i eth0 -m 00:11:22:33:44:55
#$python mac_changer-4 --interface eth0 --mac 00:11:22:33:44:55 