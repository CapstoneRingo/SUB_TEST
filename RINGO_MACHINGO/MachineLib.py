import serial
import time

# Class as a wrapper/interface for pneumatics----------------------------------
class Pneumatic:

    def __init__(self,name,pin_no):
        # Initialize properties
        self.name = name
        self.pinNo = str(pin_no)

        # Actuate OFF for starters
        self.state = 0
        self.actuate(1)
        self.actuate(0)

        # try:
        #     # Write out to serial port
        #     port = serial.Serial('/dev/ttyACM0',baudrate=115200,timeout=None)
        # except:
        #     port = serial.Serial('/dev/ttyACM1',baudrate=115200,timeout=None)
        #
        # port.write('gpio set ' + self.pinNo + ' \r')
        # port.write('gpio clear ' + self.pinNo + ' \r')

        # port.close()

    def actuate(self,cmd):

        # On/Off command
        if cmd == 1:
            cmd = "set"
            disp = "HIGH"
            self.state = 1
        else:
            cmd = "clear"
            disp = "LOW"
            self.state = 0

        # Try
        try:
            # Write out to serial port
            port = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=None)
        except:
            time.sleep(1)
            print "*******Couldn't open port /dev/ttyACM0; trying to open /dev/ttyACM0 again"
            port = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=None)

        port.write('gpio ' + cmd + ' ' + self.pinNo + ' \r')

        # Display to console
        print "Pneumatic device <%s> set to %s via %s GPIO #%s" % (self.name,
        disp, port.name, self.pinNo)

        # time.sleep(0.25)

        port.close()
        time.sleep(0.1)

        return

# Class for XY position--------------------------------------------------------
class Position:

    def __init__(self,x=0,y=0):
        self.X = x
        self.Y = y

# Class for TinyG controller interface----------------------------------------
class TinyG:

    def __init__(self):
        pass
        # Configure serial port
        #self.configurePort()

        # Setup axes
        #self.configGantry()

    def configurePort(self):

        try:
            self.serPort = serial.Serial('/dev/ttyUSB0',baudrate=115200,timeout=0)
        except:
            print "Couldn't open USB0"
            self.serPort = serial.Serial('/dev/ttyUSB1',baudrate=115200,timeout=0)

        print "TinyG using port " + self.serPort.name

    def write(self,cmd):

        try:
            port = serial.Serial('/dev/ttyUSB0',baudrate=115200,timeout=0)
        except:
            print "###Couldn't open /dev/ttyUSB0; trying /dev/ttyUSB1"
            port = serial.Serial('/dev/ttyUSB1',baudrate=115200,timeout=0)

        port.write(cmd + " \r")
        print "TinyG wrote out %s via %s" % (cmd, port.name)
        port.close()
        time.sleep(0.1)

# Class for PCB---------------------------------------------------------------
class Touchpad:

    def __init__(self):

        self.inPosition = Position()
        self.outPosition = Position()
        self.currentPosition = Position()

# Class for Tray---------------------------------------------------------------
class Trays:

    def __init__(self,in_position,out_position,row_spacing,column_spacing,
    nrows=25,ncols=2):

        # assign position of bottom-right touchpads for In and Out
        self.inPosition = in_position
        self.outPosition = out_position

        # assign cols and rows
        self.nrows = nrows
        self.ncols = ncols
        self.npads = nrows * ncols

        # keep track of spacing
        self.col_spacing = column_spacing
        self.row_spacing = row_spacing

        # create touchpad array
        self.assignTouchpads()

    def assignTouchpads(self):

        self.touchpads = []

        # for each col
        for i in range(self.ncols):
            # for each row
            for j in range(self.nrows):
                t = Touchpad()

                # Assign In tray position
                xin = self.inPosition.X + i*self.col_spacing
                yin = self.inPosition.Y + j*self.row_spacing
                t.inPosition = Position(xin,yin)
                t.currentPosition = t.inPosition

                # Assign Out tray position
                xout = self.outPosition.X + i*self.col_spacing
                yout = self.outPosition.Y + (self.nrows - j - 1)*self.row_spacing
                t.outPosition = Position(xout,yout)

                self.touchpads.append(t)

    def getTouchpadPosition(self,number):
        return self.touchpads[number-1].currentPosition

    def getTouchpad(self,number):
        return self.touchpads[number-1]
