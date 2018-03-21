from MachineLib import *
import serial

s = serial.Serial('/dev/ttyACM1',baudrate=115200,timeout=None)

p = Pneumatic('roller',1,s)
