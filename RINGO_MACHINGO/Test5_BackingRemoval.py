#Trial 12
#note = z22 is required to get roller out of way
#Note - z32 is new zmax
import time
#r.head.rotateDown()
#r.tinyG.write('g0 x378')
#r.tinyG.write('g0 y428')
#time.sleep(10)
#r.backingRemoval.push()
#time.sleep(1)
#r.head.extend()
#time.sleep(0.5)
#r.head.grab()
#time.sleep(0.5)

# z0 = 31.0
# x0 = 367.0
#
# delx1 = 1.0
# delz1 = 2.0
#
# delx2 = 3.0 #3.4
# delz2 = 6.4
#
# delx3 = 5.5 #4.5
# delz3 = 8.0
# delz4 = 8.5


JIG_OVERLAY_DROP_X = 200
JIG_OVERLAY_DROP_Y = 200

#Constants
z0 = 31.0
x0 = 367.0

delx1 = 1.2
delz1 = 2.0

delx2 = 3.4 #3
delz2 = 6.4

delx3 = 5.0 #6
delz3 = 7.5


peel_status = '0'
while peel_status == '0':
    #Get into initial position
    r.backingRemoval.motorOn()
    r.head.rotateDown()
    r.head.retract()
    r.backingRemoval.push()
    r.tinyG.write('g0 x377')
    r.tinyG.write('g0 y435')
    time.sleep(7)
    r.head.extend()
    time.sleep(1)
    r.head.grab()
    time.sleep(1)

    r.tinyG.write('g0 x'+str(x0))
    r.tinyG.write('g0 z'+str(z0))

    for i in range(2):
        r.tinyG.write('g1 f80 x'+str(x0-delx1)+' z'+str(z0-delz1))
        time.sleep(0.5)
        r.tinyG.write('g1 f160 x'+str(x0-delx2)+' z'+str(z0-delz2))
        r.tinyG.write('g1 f160 x'+str(x0-delx3)+' z'+str(z0-delz3))
        if i < 1:
            r.tinyG.write('g0 x'+str(x0))
            r.tinyG.write('g0 z'+str(z0))

    peel_status = raw_input('Peel Successful?')
    time.sleep(1)
    if peel_status == '1':
        #Pull overlay over knife
        r.tinyG.write('g1 f200 x361')
        r.tinyG.write('g0 z23.3')
        r.tinyG.write('g1 f200 x359')
        r.tinyG.write('g0 z22.8')
        r.tinyG.write('g1 f200 x357')
        r.tinyG.write('g0 z22.3')
        r.tinyG.write('g1 f200 x355')
        r.tinyG.write('g1 f200 x320 z'+str(z0-delz4))
        #r.tinyG.write('g1 f400 x300')
        r.tinyG.write('g0 x230')
        r.tinyG.write('g28.2 z0')
        time.sleep(20)
        r.backingRemoval.motorOff()
        r.head.retract()
        time.sleep(1)
        r.tinyG.write('g0 x' + str(JIG_OVERLAY_DROP_X) + ' y' + str(JIG_OVERLAY_DROP_Y))
        time.sleep(4)
        r.head.drop()
        time.sleep(1)

    elif peel_status == '0':
        r.tinyG.write('g0 z10')
        r.tinyG.write('g0 x200')
        time.sleep(3)
        r.head.drop()
        r.head.retract()

# time.sleep(10)
# r.head.retract()
# r.head.drop()
