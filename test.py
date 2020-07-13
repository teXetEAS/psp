#!/usr/bin/env python
import scapy.all as scapy
import scan
import time

targetIp = "192.168.1.66"
routerIp = "192.168.1.1"

for item in scan.scan(routerIp + "/24"):
	if routerIp != item["ip"]:
		print(item)
	
