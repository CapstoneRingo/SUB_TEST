import serial
from MachineLib import *
from MachineComponents import *
import time

# All units in MM
class RINGO:

    def __init__(self):

        # Read in config file
        self.readConfigFile()

        # Configure TinyG controller
        self.configureTinyG()

        # Setup machine components/stations
        headPins = [1, 2, 4, 3]
        jigPin = 7
        backingPins = [6,5,0]

        self.head = Head(self.tinyG,headPins)
        self.jig = OverlayPlacement(jigPin)
        self.backingRemoval = BackingRemoval(self.tinyG,backingPins)

        self.getSettled()

    # Function that makes sure the pneumatics and axes are in the right
    # spots for machine operation
    def getSettled(self):
        # set to relative positioning, jog the y axis
        self.tinyG.write('g91')
        self.tinyG.write('g0 y1')
        self.tinyG.write('g0 y-1')

        # Seems to be necessary
        time.sleep(3)

        # put pneumatics into initial start positions
        self.head.extend()
        self.head.retract()
        self.head.rollerUp()
        self.head.rotateUp()
        self.jig.retract()

        # set back to absolute(global) positioning
        self.tinyG.write('g90')

        # FAILSAFE
        r = raw_input("IS IT SAFE FOR HOMING??? (ENTER <YES> TO CONTINUE) ")

        if r == '<YES>':
            pass
        else:
            return

        # Home the tinyG
        self.tinyG.write('g28.2 x0 g28.2 y0')
        # self.tinyG.write('{xtm:1000}') # max travel
        # self.tinyG.write('{xtn:0}') # infinite axis
        # self.tinyG.write('{ytm:470}')
        # self.tinyG.write('{ytn:0}')
        self.checkHoming()

    # Checks the homing
    def checkHoming(self):
        r = raw_input("HAS HOMING OPERATION BEEN COMPLETED??? (ENTER <YES> TO CONTINUE) ")

        if r == "<YES>":
            print "HOMING STATED TO BE COMPLETE"
        else:
            print "NOT A VALID CONFIRMATION FOR HOMING COMPLETION"
            self.checkHoming()

    def readConfigFile(self):
        pass

    def configureTinyG(self):
        self.tinyG = TinyG()

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
        self.tinyG.write('{1po:0}')

        # set travel for axes
        self.tinyG.write('{1tr:15}') # should be 1tr:15
        self.tinyG.write('{2tr:10.5}') # should be 2tr:10.5
        self.tinyG.write('{3tr:8}') # should be 3tr:8

        self.tinyG.write('$XSN=3')
        self.tinyG.write('$YSN=3')
        self.tinyG.write('$ZSN=3')
        self.tinyG.write('$ST=0')
        self.tinyG.write('G90') # relative positioning

        # Set axis speeds
        self.tinyG.write('{xsv:800}') # max homing speed (mm/min)
        self.tinyG.write('{xvm:10000}')
        self.tinyG.write('{xfr:10000}')
        self.tinyG.write('{xtm:1000}')
        self.tinyG.write('{xtn:-1000}')


        self.tinyG.write('{ysv:800}')
        self.tinyG.write('{yvm:10000}')
        self.tinyG.write('{yfr:10000}')
        self.tinyG.write('{ytm:1000}')
        self.tinyG.write('{ytn:-1000}')

        # Homing settings
        self.tinyG.write('{xlb:10}')
        self.tinyG.write('{ylb:10}')

        # Power settings
        self.tinyG.write('{3pm:3}')

    def moveX(self,posx,speed):
        cmd = 'g1 f%f x%f \r' % (speed, posx)

        status = False

        while (not self.getGStatus(5)):
            status = self.getGStatus(5)

        print "Machine is moving"

        while (not self.getGStatus(3)):
            status = self.getGStatus(3)

        print "Move completed!"
        return


    def getGStatus(self,code):
        self.tinyG.write('{sr:{stat:t}} \r')
        sr = self.tinyG.serPort.read(100)

        a = sr.find('\"stat\":' + str(code))

        if a != -1:
            return True
        else:
            return False

    def gcode(self,cmd):
        self.tinyG.write(cmd)
        return

    def stop(self):
        self.gcode('!')
        return

    def resume(self):
        self.gcode('~')
        return

    def flushGcode(self):
        self.gcode('%')
        return
