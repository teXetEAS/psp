#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(inter):
	scapy.sniff(iface=inter, store=False, prn=procSniffPack)
	
def procSniffPack(pack):
	if pack.haslayer(http.HTTPRequest):
		if pack.haslayer(scapy.Raw):
			print(pack[scapy.Raw].load)
		
sniff("eth0")
