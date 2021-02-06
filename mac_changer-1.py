import subprocess

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:22:44:66:88:99"])
subprocess.call(["ifconfig","eth0","up"])

print("---------->>>>>>>>>>")