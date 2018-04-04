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

delx1 = 1.0
delz1 = 2.0

delx2 = 3.0
delz2 = 7

delx3 = 5.0
delz3 = 8.0


#Get into initial position
r.backingRemoval.push()
r.tinyG.write('g0 x377')
r.tinyG.write('g0 y430')
answer = raw_input('Ready? (1=Yes, 0=No): ')

if answer == '1':
    r.head.extend()
    time.sleep(1)

r.head.grab()
r.tinyG.write('g0 x'+str(x0))
r.tinyG.write('g0 z'+str(z0))

#Start peel
answer = raw_input('Start Peel?')

if answer == '1':
    for i in range(2):
        r.tinyG.write('g1 f40 x'+str(x0-delx1)+' z'+str(z0-delz1))
        time.sleep(0.5)
        r.tinyG.write('g1 f80 x'+str(x0-delx2)+' z'+str(z0-delz2))
        r.tinyG.write('g1 f80 x'+str(x0-delx3)+' z'+str(z0-delz3))
        if i < 1:
            r.tinyG.write('g0 x'+str(x0))
            r.tinyG.write('g0 z'+str(z0))

answer = raw_input('Peel Successful?')
time.sleep(1)
if answer == '1':
    #Pull overlay over knife
    r.tinyG.write('g1 f200 x300')
    r.tinyG.write('g0 x200')
    time.sleep(15)
    r.head.retract()
    r.tinyG.write('g0 y165')
    r.tinyG.write('g0 x314')
    raw_input('Take Picture?')
    r.head.drop()

elif answer == '0':
    r.tinyG.write('g0 x'+str(x0))
    r.tinyG.write('g0 z'+str(z0))
    time.sleep(3)
    r.head.drop()
    r.head.retract()

# time.sleep(10)
# r.head.retract()
# r.head.drop()
