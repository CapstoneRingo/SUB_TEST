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

z0 = 31
x0 = 367
delx1 = 1
delz1 = 2
delx2 = 2
delz2 = 5
delx3 = 10
delz3 = 10
zfinal = 10

#Get into initial position
r.head.grab()
r.tinyG.write('g0 x'+str(x0))
r.tinyG.write('g0 z'+str(z0))

#Start peel
r.tinyG.write('g1 f80 x'+str(x0-delx1)+' z'+str(z0-delz1))
r.tinyG.write('g1 f80 x'+str(x0-delx2)+' z'+str(z0-delz2))
#raw_input('?')
r.tinyG.write('g1 f120 x'+str(x0-delx3)+'z'+str(z0-delz3))
#r.tinyG.write('g0 z'+str(zfinal))

raw_input('?')
r.tinyG.write('g0 x'+str(x0))
r.tinyG.write('g0 z'+str(z0))
time.sleep(3)
r.head.drop()

#Pull overlay over knife
#r.tinyG.write('g1 f800 x300')

#r.tinyG.write('g0 y200')
#time.sleep(10)
#r.head.retract()
#r.head.drop()
