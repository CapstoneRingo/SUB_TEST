from RINGO import *
import time

r = RINGO()

for i in range(25):
    r.gcode('g0 x200 y220')
    time.sleep(8)
    r.gcode('g28.2 x0 y0')
    time.sleep(8)
