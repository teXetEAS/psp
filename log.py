#!/usr/bin/env python
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

def logScan(targetIp, targetMac):
	with open(path, "a") as logFile:
		logFile.write("\n[+] " + date + time + " " + targetIp + "/" + targetMac + "\n")
		
def logSniff(resalt):
	with open(path, "a") as logFile:
		logFile.write(resalt + "\n")
	
