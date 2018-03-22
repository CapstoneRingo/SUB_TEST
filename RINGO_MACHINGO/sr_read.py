import serial

# Define and open the serial port for the tinyG
# 0 timeout means it will return immediately returning anywhere from zero to
# the requested number of bytes
try:
    s = serial.Serial('/dev/ttyUSB0',baudrate=115200,timeout=0)
except:
    s = serial.Serial('/dev/ttyUSB1',baudrate=115200,timeout=0)


# Function for writing out to the tinyG
def write(cmd):
    s.write(cmd + ' \r')
    return

# Function for reading from the tinyG after sending a command to it
def read(cmd,bytes):
    s.write(cmd + ' \r')
    print s.read(bytes)

# Move the X axis to posx (mm) at speed (mm/min: good testing speeds are 300-500)
def moveX(posx,speed):
    cmd = 'g1 f%f x%f \r' % (speed, posx)
    s.open()
    s.write(cmd)

    status = False

    while(not getStatus(5)):
        status = getStatus(5)

    print "Machine is moving"

    while(not getStatus(3)):
        status = getStatus(3)

    print "Move completed!"
    s.close()
    return

# Checks to see if the tinyG's status matches the code that you give it.
# Pertinent codes are: 3 (machine stopped), 5 (machine running)
def getStatus(code):
    s.write('{sr:{stat:t}} \r')
    sr = s.read(100)

    a = sr.find('\"stat\":' + str(code))

    if a != -1:
        return True
    else:
        return False

# turns off the automatic status report returns from tinyG (i.e. it will only
# return status reports when we ask it to)
write('{sv:0}')
write('g91') # turn on relative positioning for tinyG
s.close() # close serial port on startup
