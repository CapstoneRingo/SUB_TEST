from MachineLib import *
import time

# Head-------------------------------------------------------------------------
class Head:

    def __init__(self,tinyG,serial_port,headPins):

        self.tinyG = tinyG # assign machine tinyG to this guy

        # Define pneumatic components
        self.linear = Pneumatic('Head (Linear)',str(headPins[0]),serial_port)
        self.rotary = Pneumatic('Head (Rotary)',str(headPins[1]),serial_port)
        self.vacuum = Pneumatic('Vacuum',str(headPins[2]),serial_port)
        self.roller = Pneumatic('Roller',str(headPins[3]),serial_port)

        # Define position
        self.position = Position()

    def extend(self):
        self.linear.actuate(1)
        return

    def retract(self):
        self.linear.actuate(0)
        return

    def grab(self):
        self.vacuum.actuate(1)
        return

    def drop(self):
        self.vacuum.actuate(0)
        return

    def rotateDown(self):
        self.rotary.actuate(1)
        return

    def rotateUp(self):
        self.rotary.actuate(0)
        return

    def move(self,position,speed):

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

    def moveToNeutral(self,speed):
        # Pull the head up
        self.retract()
        self.rotateUp()

        # Move Y to zero
        cmd = "G1 Y0 F%f" % speed
        self.tinyG.write(cmd)
        self.position.Y = 0



# Class for overlay placement--------------------------------------------------
class OverlayPlacement:

    def __init__(self,serial_port,overlayPin):

        # pneumatics
        self.jig = Pneumatic('Jig Extension',str(overlayPin),serial_port)

        self.position = Position()

    def extend(self):
        self.jig.actuate(1)
        return

    def retract(self):
        self.jig.actuate(0)
        return

# Class for backing removal----------------------------------------------------
class BackingRemoval:

    def __init__(self,serial_port,tinyG,backingPin):

        # tinyG
        self.tinyG = tinyG

        # Pneumatics
        self.pinner = Pneumatic("Pinner",str(backingPin[0]),serial_port)
        self.pusher = Pneumatic("Pusher",str(backingPin[1]),serial_port)

        # position
        self.position = Position()

    def pin(self):
        self.pinner.actuate(1)
        return

    def unPin(self):
        self.pinner.actuate(0)
        return

    def push(self):
        self.pusher.actuate(1)
        time.sleep(1)
        self.pusher.actuate(0)
        return
