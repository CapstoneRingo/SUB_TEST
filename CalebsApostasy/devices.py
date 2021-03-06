import serial

# Class for keeping track of devices to communicate
# with over USB. Has properties for the GPIO pin,
# the serial port, and methods for setting hi or lo.
class device:

    def __init__(self,name,pin,port):
        self.name = name
        self.GPIO = pin
        self.port = port # a pyserial port connection object

    def setHigh(self,test=0):

        if test == 1:
            return

        self.port.write("gpio set " + self.GPIO + "\r")
        print "Device %s set to HIGH via %s GPIO #%s" % (self.name,
        self.port.name, self.GPIO)
        return

    def setLow(self,test=0):

        if test == 1:
            return

        self.port.write("gpio clear " + self.GPIO + "\r")
        print "Device %s set to LOW via %s GPIO #%s" % (self.name,
        self.port.name, self.GPIO)
        return
