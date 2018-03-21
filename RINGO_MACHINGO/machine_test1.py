from RINGO import *
import time

r = RINGO()

r.gcode('g0 x500 y220')
moves = 0

while(1):
    r.gcode('g0 x250 y200')
    r.gcode('g0 x700 y220')
    time.sleep(11)
    moves += 1
    print "%d complete movements" % (moves)
