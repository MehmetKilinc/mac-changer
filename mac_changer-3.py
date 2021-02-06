import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest = "interface" , help = "enter your inteface")
parse_object.add_option("-m","--mac", dest = "mac_address" , help = "enter mac address")

(user_inputs , arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address


print("------------->>>>>>>>")


subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])

#python mac_changer-3 -i eth0 -m 00:11:22:33:44:55
#python mac_changer-3 --interface eth0 --mac 00:11:22:33:44:55