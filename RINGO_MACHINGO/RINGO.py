import serial
from MachineLib import *
from MachineComponents import *
import time

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
        headPins = [1, 2, 4, 3]
        jigPin = 7
        backingPins = [6,5,0]

        self.head = Head(self.tinyG,self.pneumaticsPort,headPins)
        self.jig = OverlayPlacement(self.pneumaticsPort,jigPin)
        self.backingRemoval = BackingRemoval(self.pneumaticsPort,self.tinyG,backingPins)

        self.trays = Trays(TRAY_IN_POSITION,TRAY_OUT_POSITION,12,80)

        self.getSettled()

    def getSettled(self):
        self.tinyG.write('g0 y1')
        self.tinyG.write('g0 y-1')

        time.sleep(3)

        self.head.extend()
        self.head.retract()
        self.head.rollerUp()
        self.head.rotateUp()
        self.jig.retract()

    def readConfigFile(self):
        pass

    def configurePorts(self):
        try:
            self.pneumaticsPort =  serial.Serial('/dev/ttyACM0',115200,timeout=None)
        except:
            self.pneumaticsPort =  serial.Serial('/dev/ttyACM1',115200,timeout=None)

        self.tinyG = TinyG('USB0')

    def configureTinyG(self):

        # set units to metric
        self.tinyG.write('G21')

        # Set step sizes
        self.tinyG.write('{1sa:1.8}')
        self.tinyG.write('{2sa:1.8}')
        self.tinyG.write('{3sa:1.8}')

        # Set microstepping
        self.tinyG.write('{1mi:8}')
        self.tinyG.write('{2mi:8}')
        self.tinyG.write('{3mi:8}')

        # Set polarity of motors
        self.tinyG.write('{2po:0}')
        self.tinyG.write('{3po:0}')
        self.tinyG.write('{1po:1}')

        # set travel for axes
        self.tinyG.write('{1tr:15}') # should be 1tr:15
        self.tinyG.write('{2tr:10.5}') # should be 2tr:10.5
        self.tinyG.write('{3tr:8}') # should be 3tr:8

        self.tinyG.write('$XSN=1')
        self.tinyG.write('$YSN=1')
        self.tinyG.write('$ZSN=1')
        self.tinyG.write('$ST=0')

        self.tinyG.write('G91') # relative positioning

        # home axes
        #self.tinyG.write('G28.2 Y0 X0')
        #self.tinyG.write('G28.3 X0 Y0')

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

r = RINGO()
