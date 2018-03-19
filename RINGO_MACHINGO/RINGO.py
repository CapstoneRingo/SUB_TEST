import serial
from MachineLib import *
from MachineComponents import *

TRAY_IN_POSITION = Position(100,0)
TRAY_OUT_POSITION = Position(600,0)

# All units in MM
class RINGO:

    def __init__(self):

        # Read in config file
        self.readConfigFile()

        # Configure serial ports
        self.configurePorts()

        # Configure TinyG controller
        self.configureTinyG()

        # Setup machine components/stations
        self.head = Head(self.tinyG,self.pneumaticsPort)
        self.jig = OverlayPlacement(self.pneumaticsPort)
        self.backingRemoval = BackingRemoval(self.pneumaticsPort,self.tinyG)

        self.trays = Trays(TRAY_IN_POSITION,TRAY_OUT_POSITION,12,80)

    def readConfigFile(self):
        pass

    def configurePorts(self):
        self.pneumaticsPort =  serial.Serial('/dev/ttyACM0',9600,timeout=0)

        self.tinyG = TinyG('USB0')

    def configureTinyG(self):

        # set units to metric
        self.tinyG.write('G21')

        # set travel for axes
        self.tinyG.write('{tr1:15}')
        self.tinyG.write('{tr2:10.5}')
        self.tinyG.write('{tr3:8}')

        # home axes
        self.tinyG.write('G28.2 Y0 X0')
        self.tinyG.write('G28.3 X0 Y0')

    def pickPCB(self,number):

        # get pcb position
        t = self.trays.getTouchpad(number)
        p = t.inPosition

        # send head to position
        self.head.move(p,20)

        # perform operations
        self.head.rotateUp()
        self.head.extend()
        # add in forward motion/jiggling motion
        self.head.grab()
        self.head.retract()
        self.head.rotateDown()

    def placePCB(self,number):

        # get pcb position
        t = self.trays.getTouchpad(number)
        p = t.outPosition

        # send head to position
        self.head.move(p,20)

        # perform operations
        self.headrotateUp()
        self.head.extend()
        self.head.drop()
        self.head.retract()
        self.head.rotateDown()
