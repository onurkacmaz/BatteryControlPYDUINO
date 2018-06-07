#!/usr/bin/env python
#-*-coding:utf-8-*-
import psutil
import serial
import time
import schedule
import os
import platform

if os.name == 'nt':  # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == 'posix':
    from serial.tools.list_ports_posix import comports
#~ elif os.name == 'java':
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))

ports = serial.tools.list_ports_posix.comports()
print("---------------------------------\nPortlar taranıyor. Cihaz aranıyor....\n---------------------------------")
for port in ports:
	time.sleep(0.2)
	print port.device

port = port.device
boud = 9600
ser1 = serial.Serial(port, boud)

start = raw_input("---------------------------------\nKablo takılsın mı ? Y/N\n---------------------------------\n ? - ")
if (start == 'y' or start == 'Y'):
	ser1.write('1')
elif (start == 'n' or start == 'N'):
	ser1.write('0')

while True:
	
	time.sleep(5)
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)

	cikar = '0'
	tak = '1'

	if (plugged == True) and int(percent) >= 99:
		print("Şarjınız tam dolu. Kablo çıkarılıyor...\n---------------------------------");
		ser1.write(cikar)
	elif (plugged == False) and int(percent) < 15:
		print("Takılıyor...")
		ser1.write(tak)
		if plugged == True:
			print("Takıldı")
	else:
		print("Stabil : " + "%" + percent)
