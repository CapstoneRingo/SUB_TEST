import serial

s = serial.Serial('/dev/ttyUSB0',baudrate=115200,timeout=0)

def write(cmd):
    s.write(cmd + ' \r')
    return

def read(cmd,bytes):
    #s.write('{sr:f}')
    s.write(cmd + ' \r')
    print s.read(bytes)

write('{sv:0}')

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

def getStatus(code):
    s.write('{sr:{stat:t}} \r')
    sr = s.read(100)

    a = sr.find('\"stat\":' + str(code))

    if a != -1:
        return True
    else:
        return False

write('g91')
s.close()
