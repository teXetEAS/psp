#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arp_request
	answerdList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	parsIpMac = []
	for item in answerdList:
		parsDict = {"ip": item[1].psrc, "mac": item[1].hwsrc}
		parsIpMac.append(parsDict)
	return parsIpMac	

