import subprocess

interface = "eth0"
mac_address = "00:11:22:33:44:55"

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])

print("---------->>>>>>>>>>")