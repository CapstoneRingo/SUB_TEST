#Purpose - Test overlay dispenser. Dispenses 100 overlays and
#uses the vacuum head to place overlays into a user provided bin
#at x200 y200.

#Take 17 sec to complete each cycle, or about 28 min to do 100
#overlays

import time

x_pick = 377
y_pick = 430

x_drop = 200
y_drop = 200

r.tinyG.write('g0 x'+str(x_drop)' y'+str(y_drop))
time.sleep(4)

#Repeat for 100 overlays
for i in range(100):
    #Move head to pickup location
    r.tinyG.write('g0 y'+str(y_pick))
    r.tinyG.write('g0 x'+str(x_pick))
    time.sleep(6)

    #Push an overlay out of dispenser
    r.backingRemoval.push()
    time.sleep(1)

    #Grab the overlay
    r.head.extend()
    r.head.grab()
    time.sleep(1)

    #Pull the overlay away from dispenser and release at drop location
    r.tinyG.write('g0 x'+str(x_drop))
    time.sleep(2)
    r.head.retract()
    r.tinyG.write('g0 y'+str(y_drop))
    time.sleep(4)
    r.head.drop()
