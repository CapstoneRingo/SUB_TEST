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
    s.write(cmd)

    status = 0

    while(status != '5'):
        status = getStatus()

    print "Machine is moving"

    while(status != '3'):
        status = getStatus()

    print "Move completed!"
    return

def getStatus():
    s.write('{sr:{stat:t}} \r')
    sr = s.read(100)

    a = sr.find('stat')

    try:
        b = sr[a + 6]
    except:
        b = 'poop'

    return b

write('g91')
