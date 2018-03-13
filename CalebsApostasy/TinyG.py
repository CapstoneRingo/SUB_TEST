import serial

class TinyG:

    def __init__(self,port):

        # Configure serial port
        self.configurePort(port)

        # Setup axes
        self.configGantry()

    def configurePort(self,port):
        port_name = '/dev/tty' + port # concatenate port name
        
        self.serPort = serial.Serial(port=port_name,baudrate=115200,timeout=0)
        print "TinyG using port " + port_name

    def write(self,cmd):
        self.serPort.write(cmd + " \r")

    def configGantry(self):

        # Home machine
        self.write('G28.3 X0 Y0 Z0')

        # Set to relative positioning mode
        self.write('G91')

        self.write('G21') # set units to mm
        self.write('{tr1:15}') # X-axis travel set to 15mm/rev (gearbox+belt)
        self.write('{tr2:105}') # Y-axis travel set to 105mm/rev (belt only)
        self.write('{tr3:20}') # Z-axis travel?
