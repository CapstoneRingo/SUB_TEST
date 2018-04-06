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



	command = 0

	menu = "\n\n\n*********************************\nMAIN MENU: Select an Option"
	menu = menu + "\n   1. Turn Pin HIGH"
	menu = menu + "\n   2. Turn Pin LOW"
	menu = menu + "\n   3. PWM TEST"
	menu = menu + "\n   Enter 'exit' to quit and 'help' for deets"

	sub_menu_1 = "\n   Select GPIO Pin: "

	sub_menu_2 = "\n\nFUNCTION LIST"
	sub_menu_2 = sub_menu_2 + "\n  a. SetMotorSpeed() "
	sub_menu_2 = sub_menu_2 + "\n  b. SetPWMParameters() "

	confirm = "\nSet pin "
	confirm_h = " to high."
	confirm_l = " to low."

	help_t = "\n\n HELP: \nEnter the number of letter in front of the period\n"
	help_t = help_t + "to select a function from the menu or sub-menu"

	error = "\nLook ... it's obvious this is your first time ... so, um - yeah?"

	while command != 'exit':
		command = input(menu)

		if command == "help":
			print(help_t)
		elif command == "1":
			pin = input(sub_menu_1)
			setHigh(pin, setPort)
			print(confirm, pin, confirm_h)
		elif command == "2":
			pin = input(sub_menu_1)
			setLow(pin, setPort)
			print(confirm, pin, confirm_l)
		elif command == "3":
			command_2 = input(sub_menu_2)
			print("\nYeah .. this part isn't finished, still in Nirvanna?")
		elif command != "exit":
			print(error)
main()
