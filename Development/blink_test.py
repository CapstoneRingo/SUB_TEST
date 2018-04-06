#	FILE NAME 		:	blink_test.py
#	AUTHOR 			: 	Nolan McCulloch
# 	CONTRIBUTORS	: 	Numato Labs
#	DATE CREATED	:	Feb 2018
#	PYTHON VER		:	2.7
#	REVISION		:	2.1.2

#	INFO
# This Script is to be used as a blink test with delay
# using the GPIO code given from Numato.

#see GPIO_COMMANDS.txt for available commands and descriptions.

#LIBRARIES USED

import sys
import serial
import time

#GPIO PINS AVAILABLE

GPIO_0 = '0'
GPIO_1 = '1'
GPIO_2 = '2'
GPIO_3 = '3'
GPIO_4 = '4'
GPIO_5 = '5'
GPIO_6 = '6'
GPIO_7 = '7'
GPIO_8 = '8'
GPIO_9 = '9'
GPIO_10 = 'A'
GPIO_11 = 'B'
GPIO_12 = 'C'
GPIO_13 = 'D'
GPIO_14 = 'E'
GPIO_15 = 'F'


USB_PORT = "/dev/ttyACM0"
DRIVER_PORT = "/dev/ttyUSB0"

print" ... welcome to VIRUS CITY!!!!"

# Set up serial connection
serPort = serial.Serial(USB_PORT, 115200, timeout=None)
driverPort = serial.Serial(DRIVER_PORT, 115200, timeout=None)


# setHigh(gpioIndex)
# This function takes the index of the Pin that is to be set and executes
# command to set that specific index to the HIGH state (3.3V)
def setHigh(gpioIndex):
	serPort.write("gpio set " + gpioIndex  + "\r")
	return;

# setLow(gpioIndex)
# This function takes the index of the Pin that is to be cleared and executes
# command to set that specific index to the LOW state (~0V)
def setLow(gpioIndex):
	serPort.write("gpio clear " + gpioIndex  + "\r")
	return;


def fun_seq():
	setLow(GPIO_0)
	setLow(GPIO_1)
	setLow(GPIO_2)
	#setLow(GPIO_3)
	#setLow(GPIO_4)
	#setLow(GPIO_5)
	#setLow(GPIO_6)
	#setLow(GPIO_7)
	time.sleep(.5)
	setHigh(GPIO_0)
	setHigh(GPIO_1)
	setHigh(GPIO_2)
	#setHigh(GPIO_3)
	#setHigh(GPIO_4)
	#setHigh(GPIO_5)
	#setHigh(GPIO_6)
	#setHigh(GPIO_7)
	time.sleep(1)

	#driverPort.write("G0 Y10 \r")
	time.sleep(1)
	#driverPort.write("G0 Y-10 \r")
	time.sleep(1)

	setLow(GPIO_0)
	time.sleep(.25)
	setLow(GPIO_1)
	time.sleep(.25)
	setLow(GPIO_2)
	time.sleep(.25)
	#setLow(GPIO_3)
	#time.sleep(.25)
	#setLow(GPIO_4)
	#time.sleep(.25)
	#setLow(GPIO_5)
	#time.sleep(.25)
	#setLow(GPIO_6)
	#time.sleep(.25)
	#setLow(GPIO_7)
	#time.sleep(.25)
	#setHigh(GPIO_7)
	#time.sleep(.25)
	#setHigh(GPIO_6)
	#time.sleep(.25)
	#setHigh(GPIO_5)
	#time.sleep(.25)
	#setHigh(GPIO_4)
	#time.sleep(.25)
	#setHigh(GPIO_3)
	#time.sleep(.25)
	setHigh(GPIO_2)
	time.sleep(.25)
	setHigh(GPIO_1)
	time.sleep(.25)
	setHigh(GPIO_0)
	time.sleep(1)


def main():
	i = 0

	# initialize all pins high.
	setHigh(GPIO_0)
	setHigh(GPIO_1)
	setHigh(GPIO_2)
	setHigh(GPIO_3)
	setHigh(GPIO_4)
	setHigh(GPIO_5)
	setHigh(GPIO_6)
	setHigh(GPIO_7)

#	print"Press Q to quit"
	while True:
		fun_seq()
		i = i+1
		serPort.close()
		time.sleep(0.25)
		serPort.open()
		serPort.xonxoff = True
		print i

main()
