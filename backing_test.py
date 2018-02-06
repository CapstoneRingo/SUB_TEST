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


print" ... welcome to VIRUS CITY!!!!"
print"Using port " + USB_PORT

#Open port for communication	
serPort = serial.Serial(USB_PORT, 19200, timeout=0)

# setHigh(gpioIndex)
# This function takes the index of the Pin that is to be set and executes 
# command to set that specific index to the HIGH state (3.3V)
def setHigh(gpioIndex, setPort):
	print"HIGH"
	serPort.write("gpio set " + gpioIndex  + "\r")
	return;

# setLow(gpioIndex)
# This function takes the index of the Pin that is to be cleared and executes 
# command to set that specific index to the LOW state (~0V)
def setLow(gpioIndex, setPort):
	print "LOW"
	serPort.write("gpio clear " + gpioIndex  + "\r")
	return;




def main():
	i = 0
#	print"Press Q to quit"
	while True:
		setHigh(GPIO_7, serPort)
		print '65'
		time.sleep(2)
		setLow(GPIO_7, serPort)
		print '68'
		time.sleep(2)
		i = i+1
		print i

main()


