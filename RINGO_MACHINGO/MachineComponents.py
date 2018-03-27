from MachineLib import *
import time

# Head-------------------------------------------------------------------------
class Head:

    def __init__(self,tinyG,headPins):

        self.tinyG = tinyG # assign machine tinyG to this guy

        # Define pneumatic components
        self.linear = Pneumatic('Head (Linear)',str(headPins[0]))
        self.rotary = Pneumatic('Head (Rotary)',str(headPins[1]))
        self.vacuum = Pneumatic('Vacuum',str(headPins[2]))
        self.roller = Pneumatic('Roller',str(headPins[3]))

        # Define position
        self.position = Position()

        # Startup commands
        self.retract()
        self.rollerUp()
        self.rotateUp()

    def extend(self):
        self.linear.actuate(1)
        return

    def retract(self):
        self.linear.actuate(0)
        return

    def grab(self):
        self.vacuum.actuate(0)
        return

    def drop(self):
        self.vacuum.actuate(1)
        return

    def rotateDown(self):
        self.rotary.actuate(1)
        return

    def rotateUp(self):
        self.rotary.actuate(0)
        return

    def rollerDown(self):
        self.roller.actuate(1)
        return

    def rollerUp(self):
        self.roller.actuate(0)
        return

    #def move(self,position,speed):

        self.moveToNeutral(speed)

        x = position.X
        y = position.Y

        # Send X-axis command
        xcmd = "G1 X%f F%f" %(x,speed)
        self.tinyG.write(xcmd)
        self.position.X = x

        # Send Y-axis command
        ycmd = "G1 Y%f F%f" %(y,speed)
        self.tinyG.write(ycmd)
        self.position.Y = y

    #def moveToNeutral(self,speed):
        # Pull the head up
        self.retract()
        self.rotateUp()

        # Move Y to zero
        cmd = "G1 Y0 F%f" % speed
        self.tinyG.write(cmd)
        self.position.Y = 0



# Class for overlay placement--------------------------------------------------
class OverlayPlacement:

    def __init__(self,overlayPin):

        # pneumatics
        self.jig = Pneumatic('Jig Extension',str(overlayPin))

        self.position = Position()

        # Startup commands
        self.retract()

    def extend(self):
        self.jig.actuate(1)
        return

    def retract(self):
        self.jig.actuate(0)
        return

# Class for backing removal----------------------------------------------------
class BackingRemoval:

    def __init__(self,tinyG,backingPin):

        # tinyG
        self.tinyG = tinyG

        # Pneumatics
        #self.pinner = Pneumatic("Pinner",str(backingPin[0]))
        self.pusher = Pneumatic("Pusher",str(backingPin[1]))
        self.motor = Pneumatic("DCMotor",str(backingPin[2]))

        # position
        self.position = Position()

    def pin(self):
        self.pinner.actuate(1)
        return

    def unPin(self):
        self.pinner.actuate(0)
        return

    def push(self):
        self.pusher.actuate(0)
        time.sleep(1)
        self.pusher.actuate(1)
        return

    def motorOn(self):
        self.motor.actuate(0)
        return

    def motorOff(self):
        self.motor.actuate(1)
        return
