import serial

# Class as a wrapper/interface for pneumatics----------------------------------
class Pneumatic:

    def __init__(self,name,pin_no,serial_port):
        # Initialize properties
        self.name = name
        self.pinNo = str(pin_no)
        self.serialPort = serial_port # a pyserial port connection object

        # Actuate OFF for starters
        self.state = 0
        self.actuate(0)

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
            self.serialPort.write("gpio " + cmd + " " + self.pinNo + "\r")
        except:
            if self.serialPort == '/dev/ttyACM0':
                self.serialPort = '/dev/ttyACM1'
            elif self.serialPort == '/dev/ttyACM1':
                self.serialPort = '/dev/ttyACM0'

            print "Serial port switched to %s" % (self.serialPort.name)

            self.actuate(cmd) # run the pneumatics command again

        # Display to console
        print "Pneumatic device <%s> set to %s via %s GPIO #%s" % (self.name,
        disp, self.serialPort.name, self.pinNo)

        return

# Class for XY position--------------------------------------------------------
class Position:

    def __init__(self,x=0,y=0):
        self.X = x
        self.Y = y

# Class for TinyG controller interface----------------------------------------
class TinyG:

    def __init__(self,serialPort):

        # Configure serial port
        self.configurePort(serialPort)

        # Setup axes
        #self.configGantry()

    def configurePort(self,port):
        port_name = '/dev/tty' + port # concatenate port name

        self.serPort = serial.Serial(port=port_name,baudrate=115200,timeout=0)
        print "TinyG using port " + self.serPort.name

    def write(self,cmd):
        self.serPort.write(cmd + " \r")

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
