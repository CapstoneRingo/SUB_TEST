# This Script is to be used as a script to test the head design, controlling the 
# various pnumatic valves that steer and control the head. This progrogram's 
# purpose is to outline the various functions and movements of this subsystem.  

#see GPIO_COMMANDS.txt for available commands and descriptions. 

#LIBRARIES USED

import sys
import serial
import time

#GPIO PINS AVAILABLE

GPIO_0 = '0'
GPIO_1 = '1'
GPIO_2 = '2'		# Drive Roller (REMOVAL)				- OUT
GPIO_3 = '3'		# Z-Axis Actuator (FRAME - POS 2)		- OUT
GPIO_4 = '4'		# Z-Axis Actuator (FRAME - POS 1)		- OUT
GPIO_5 = '5'		# Vacuum Control (HEAD)					- OUT
GPIO_6 = '6'		# Rotation Actuator (HEAD)				- OUT
GPIO_7 = '7'		# Z-Axis Actuator (HEAD)				- OUT
GPIO_8 = '8'
GPIO_9 = '9'
GPIO_10 = 'A'
GPIO_11 = 'B'
GPIO_12 = 'C'
GPIO_13 = 'D'
GPIO_14 = 'E'		# Limit Switch (AXIS - Y)				- IN
GPIO_15 = 'F'		# Limit Switch (AXIS - X)				- IN


USB_PORT = "/dev/ttyACM0"


print" ... welcome to VIRUS CITY!!!!"
print"Using port " + USB_PORT

#Open port for communication	
serPort = serial.Serial(USB_PORT, 19200, timeout=0)

# GetPCBFromTray_IN
#
# This function manages the retrieval of PCB's from the input tray. It may be  
# responsible for checking if the tray has the correct orientation and the PCB's 
# are facing the right direction. This function should also increment the PCB 
# count after it has sucessfully picked up a PCB, manage the column it retrieved 
# the PCB's from and automatically increment to the next position if no PCB has 
# been retrieved. 


def GetPCBFromTray_IN():

# SetPCBInJig
#
# This function manages the placement of the PCB's into the PCB overlay jig. It 
# is responsible for reliably placing the PCB in the calculated anchor position 
# of the Jig. 

# QUESTION: Should the jig be able to detect if a PCB has been correctly placed? 
# This would cover the condition where the PCB falls out of the jig or is not 
# correctly placed.  


def SetPCBInJig():

# GetOVERLAYFromRemoval
#
# This function moves the head over backing removal location and manages the 
# suction pull of the overlay and checks the to make sure the overlay makes it 
# on the head before placing the overlay on the PCB. 

# NOTE: I will be using different versions of GetOVERLAYFromRemoval in all the 
# subsystems that require use the removal. Though this function will isolate the
# function requirements of the head for this section, It will eventually 
# be the combination of all the sub-system test functions in the integrated 
# script. 

def GetOVERLAYFromRemoval():

# SetOVERLAYInJig
#
# This function is responsible controlling the head movements required for 
# placing an overlay with the backing removed in the placement jig. 


# NOTE: Should the jig be able to detect if a PCB has been correctly placed? 
# This would cover the condition where the PCB falls out of the jig or is not 
# correctly placed. 

def SetOVERLAYInJig():

# RollOVERLAYInJig
#
# This function is responsible for managing the roller and coordinating the 
# movement of the roller and the verticle position of the overlay (position 1 == 
# tallest position) 

def RollOVERLAYInJig(): 

# GetPCBFromJig
#
# This function will control the head movements and commands necessary to 
# retrive a rolled overlay and PCB from the overlay placement jig. It will 
# require activate the second position of the second roller actuator and 
# activate the suction of the pnumatic valve.    

def GetPCBFromJig():

# SetPCBInInsp
#
# This function simply sets the overlay in the inspection area and awaits the 
# inspection for bubbles, deformatilities and imperfections to take place. 	

def SetPCBInInsp():

# GetPCBInInsp
#
# This function simply gets the overlay from the inspection area.	

def GetPCBFromInsp():

# SetPCBInTray_OUT
# 
# This function is responsible for keeping track of the available positions in 
# the empty output tray. This function controls the twisting and setting of the 
# overlay in the tray. 

def SetPCBInTray_OUT():

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


