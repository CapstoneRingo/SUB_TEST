# This Script is to be used as a blink test with delay
# using the GPIO code given from Numato.

#see GPIO_COMMANDS.txt for available commands and descriptions.

#LIBRARIES USED

import sys
import serial
import time




USB_PORT = "/dev/ttyUSB1"

print"Using port " + USB_PORT

#Open port for communication
serPort = serial.Serial(port=USB_PORT, baudrate=115200, timeout=0)




def main():
	while(1):
		serPort.write("G0 Y10 \r")
		time.sleep(1)
		serPort.write("G0 Y-10 \r")
		time.sleep(1)

main()
