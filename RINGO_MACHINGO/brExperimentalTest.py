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

z0 = 31.0
x0 = 367.0

delx1 = 1.0
delz1 = 2.0

delx2 = 3.0 #3
delz2 = 6.4

delx3 = 4.5 #6
delz3 = 7.5
delz4 = 9.0


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
answer = '1'#raw_input('Start Peel?')
raw_input()
if answer == '1':
    for i in range(2):
        r.tinyG.write('g1 f80 x'+str(x0-delx1)+' z'+str(z0-delz1))
        time.sleep(0.5)
        r.tinyG.write('g1 f160 x'+str(x0-delx2)+' z'+str(z0-delz2))
        r.tinyG.write('g1 f160 x'+str(x0-delx3)+' z'+str(z0-delz3))

        if i < 1:
            r.tinyG.write('g0 x'+str(x0))
            r.tinyG.write('g0 z'+str(z0))

answer = raw_input('Peel Successful?')
time.sleep(1)
if answer == '1':
    #Pull overlay over knife
    r.tinyG.write('g1 f1000 x362')
    r.tinyG.write('g0 z23')
    r.tinyG.write('g1 f1000 x359')
    r.tinyG.write('g0 z22')
    r.tinyG.write('g1 f200 x330 z'+str(z0-delz4))
    #r.tinyG.write('g1 f400 x300')
    r.tinyG.write('g0 x230')
    time.sleep(12)
    r.head.retract()
    r.tinyG.write('g0 x314 y165')
    raw_input('Take Picture?')
    r.head.drop()

elif answer == '0':
    r.tinyG.write('g0 x'+str(x0))
    r.tinyG.write('g0 z'+str(z0))
    r.tinyG.write('g28.2 z0')
    time.sleep(3)
    r.head.drop()
    r.head.retract()

# time.sleep(10)
# r.head.retract()
# r.head.drop()
