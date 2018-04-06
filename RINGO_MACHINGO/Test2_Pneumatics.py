from MachineLib import *
import serial
from RINGO import *
import time

r =RINGO()

r.Pneumatic
s = serial.Serial('/dev/ttyACM1',baudrate=115200,timeout=None)

p = Pneumatic('roller',1,s)


a1 = Pneumatic("Pusher",str(backingPin[1]))
a2 = Pneumatic('Jig Extension',str(overlayPin))
a3 = Pneumatic('Head (Linear)',str(headPins[0]))
a4 = Pneumatic('Head (Rotary)',str(headPins[1]))
a5 = Pneumatic('Roller',str(headPins[3]))

X=50
for i in range(X):
    a1.actuate(0)
    time.delay(0.5)
    a1.actuate(1)
    time.delay(0.5)
    a2.actuate(0)
    time.delay(0.5)
    a2.actuate(1)
    time.delay(0.5)
    a3.actuate(0)
    time.delay(0.5)
    a3.actuate(1)
    time.delay(0.5)
    a4.actuate(0)
    time.delay(0.5)
    a4.actuate(1)
    time.delay(0.5)
    a5.actuate(0)
    time.delay(0.5)
    a5.actuate(1)
    time.delay(0.5)
