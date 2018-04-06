# Testing RINGO homing routine; machine is assumed to start ~10 seconds away
# from home position, and x100 y220 to be a safe spot for initialization.
from RINGO import *

X = 25 # specify number of test runs to do

# open file for writing test results
outFile = open('homing_test_results.txt','w')

for i in range(X):
    # write out that run i is starting
    startStr = "Starting homing run %d" % i
    print startStr
    outFile.write(startStr + ' \n')

    r = RINGO()
    # Wait for the standard time, then input "<YES>"
    # Wait for the standard time, then input "<YES>"
    # print out confirmation message
    endStr =  "Homing run %d is complete" % i
    print endStr
    outFile.write(endStr + ' \n')
    # send to x100 y220
    r.gcode('g0 x100 y220')
    time.sleep(8)
    r.head.extend()
    r.head.rotateDown()
    r.head.rollerDown()
    r.jig.extend()
    # write out to file


# print out to console that test is complete
endMessage = "Homing test completed using %d runs" % X
print endMessage
# write out results to file
outFile.write(endMessage + '\n')
outFile.close()
