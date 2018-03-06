import serial

# Class for keeping track of devices to communicate
# with over USB. Has properties for the GPIO pin,
# the serial port, and methods for setting hi or lo.
class device:

    def __init__(self,name,pin,port):
        self.name = name
        self.GPIO = pin
        self.port = port # a pyserial port connection object

    def setHigh(self):
        self.port.write("gpio set " + gpioIndex + "\r")
        print "Device %s set to HIGH via %s GPIO #%s" %(self.name, self.port.name, self.pin)
        return

    def setLow(self):
        self.port.write("gpio clear " + gpioIndex + "\r")
        print "Device %s set to LOW via %s GPIO #%s" %(self.name, self.port.name, self.pin)
