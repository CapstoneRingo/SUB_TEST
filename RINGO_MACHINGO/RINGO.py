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

        print "Initializing head for first time"
        self.head = Head(self.tinyG,headPins)
        print "Initializing jig for first time"
        self.jig = OverlayPlacement(jigPin)
        print "Initializing backing removal for first time"
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
        #time.sleep(3)

        # put pneumatics into initial start positions
        print "Making sure head and jig are in correct position for homing"

        #self.head.extend()
        self.head.retract()
        time.sleep(0.02)
        # time.sleep(0.5)
        self.head.rollerUp()
        # time.sleep(0.5)
        self.head.rotateUp()
        # time.sleep(0.5)
        self.jig.retract()
        # time.sleep(0.5)
        self.head.drop()
        # time.sleep(0.5)
        self.backingRemoval.motorOff()
        # time.sleep(0.5)
        # set back to absolute(global) positioning
        self.tinyG.write('g90')

        # FAILSAFE
        r = raw_input("IS IT SAFE FOR HOMING??? (ENTER <YES> TO CONTINUE) ")

        if r == '<YES>':
            pass
        else:
            return

        # Home the tinyG
        self.tinyG.write('g28.2 x0 y0 z0')
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

        # reset machine to default values
        self.tinyG.write('{"defa":1}')

        # set units to mm
        self.tinyG.write('G21')

        # Set step sizes (deg/rev)
        self.tinyG.write('{1sa:1.8}')
        self.tinyG.write('{2sa:1.8}')
        self.tinyG.write('{3sa:1.8}')

        # Set microstepping
        self.tinyG.write('{1mi:2}')
        self.tinyG.write('{2mi:2}')
        self.tinyG.write('{3mi:2}')

        # Set polarity of motors
        self.tinyG.write('{2po:0}')
        self.tinyG.write('{3po:0}')
        self.tinyG.write('{1po:0}')

        # set travel for axes (mm/rev)
        self.tinyG.write('{1tr:15}') # x-axis: should be 1tr:15
        self.tinyG.write('{2tr:10.5}') # y-axis: should be 2tr:10.5
        self.tinyG.write('{3tr:8}') # z-axis: should be 3tr:8

        #Set limit switches
        self.tinyG.write('$XSN=1')
        self.tinyG.write('$XSX=0')
        self.tinyG.write('$YSN=1')
        self.tinyG.write('$YSX=0')
        self.tinyG.write('$ZSN=1')
        self.tinyG.write('$ZSX=0')
        self.tinyG.write('$ST=0')
        self.tinyG.write('G90') # absolute positioning

        # Set axis speeds (mm/min)
        self.tinyG.write('{xsv:1000}') # max homing speed (mm/min)
        self.tinyG.write('{xvm:10000}') # set max x fast travel velocity
        self.tinyG.write('{xfr:10000}') # set max x feed velocity
        self.tinyG.write('{xtm:1000}') # set maximum x travel (for now)
        self.tinyG.write('{xtn:-1000}') # set minimum x travel (for now)

        self.tinyG.write('{ysv:1000}')
        self.tinyG.write('{yvm:15000}')
        self.tinyG.write('{yfr:10000}')
        self.tinyG.write('{ytm:1000}')
        self.tinyG.write('{ytn:-1000}')

        #Set Axis Acceleration
        self.tinyG.write('{xjm:65}')
        self.tinyG.write('{yjm:40}')

        # Homing settings
        self.tinyG.write('{xlb:5}') # backoff from limit distance
        self.tinyG.write('{ylb:5}')

        # Power settings
        self.tinyG.write('{3pm:3}') # only power z axis when moving

    def moveX(self,posx,speed):
        cmd = 'g1 f%f x%f' % (speed, posx)
        self.tinyG.write(cmd)

        status = False

        while (not self.getGStatus(5)):
            status = self.getGStatus(5)

        print "Machine is moving"

        while (not self.getGStatus(3)):
            status = self.getGStatus(3)

        print "Move completed!"
        return


    def getGStatus(self,code):
        self.tinyG.write('{sr:{stat:t}}')
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
