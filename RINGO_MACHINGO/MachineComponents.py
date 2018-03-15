from MachineLib import *
import time

# Head-------------------------------------------------------------------------
class Head:

    def __init__(self,tinyG,serial_port):

        self.tinyG = tinyG # assign machine tinyG to this guy

        # Define pneumatic components
        self.linear = Pneumatic('Head (Linear)',0,serial_port)
        self.rotary = Pneumatic('Head (Rotary)',1,serial_port)
        self.vacuum = Pneumatic('Vacuum',2,serial_port)
        self.roller = Pneumatic('Roller',3,serial_port)

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

        # Move Y to zero
        cmd = "G1 Y0 F%f" % speed
        self.tinyG.write(cmd)
        self.position.Y = 0



# Class for overlay placement--------------------------------------------------
class OverlayPlacement:

    def __init__(self,serial_port):

        # pneumatics
        self.jig = Pneumatic('Jig Extension',4,serial_port)

        self.position = Position()

    def extend():
        self.jig.actuate(1)
        return

    def retract():
        self.jig.actuate(0)
        return

# Class for backing removal----------------------------------------------------
class BackingRemoval:

    def __init__(self,serial_port,tinyG):

        # tinyG
        self.tinyG = tinyG

        # Pneumatics
        self.pinner = Pneumatic("Pinner",5,serial_port)
        self.pusher = Pneumatic("Pusher",6,serial_port)

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
