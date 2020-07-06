#!/usr/bin/env python
import scan
import os
from pathlib import *
from datetime import datetime

datetime = datetime.now()
date = datetime.date().strftime("%Y-%m-%d_")
time = datetime.time().strftime("%H:%M")

path = str(Path.home())
path += "/scanLogFile.txt"
if not os.path.exists(path):
	with open(path, "a") as logFile:
		logFile.write("\t\t\t#####LOG_FILE#####\n")

def logFile(ip):
	scanIpMac = scan.scan(ip)		
	scanMacList = []
	for item in scanIpMac:		
		scanMacList.append(item["mac"])
	macList = []
	with open(path, "r") as logFile:
		for line in logFile:
			if line.startswith("[ignor]"):
				line = line.split()
				macList.append(line[-1])
	newMacList = list(set(scanMacList) - set(macList))
	
	
	
	if len(newMacList) > 0:
		for item in newMacList:
			userInput = str(input("Игнорировать хочт с MAC-адресом " + item["mac"] " (y/n)").lower())
			if userInput == "y":
				with open(path, "a") as logFile:
					logFile.write("[ignore]" + date + time + 

try:
	logFile("192.168.1.1/24")
except PermissionError:
	print("Необходимы права Супер-пользователя")
