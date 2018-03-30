#	FILE NAME 		:	TrayUnloadTest.py
#	AUTHOR 			  : 	Nolan McCulloch
#	CONTRIBUTORS	: 	Caleb Groves, Spencer Diehl
#	DATE CREATED	:	23 MAR 2018
#	PYTHON VER		:	2.7
#	REVISION		  :	1.0.1

#	INFO
#   This program iterates through an input tray, storing the current current
#   count of the PCB being used at the moment to determine which PCB to grab
#   next. This information is saved in a ______ file and checked every
#   itteration to ensure that in the event of device shutdown or restart, it
#   can begin from the same location that it left off.

#   Because the process is currently openloop, it must make some assumptions
#   about the orientation of the trays, PCB's and head. Below is a small diagram
#   that illustrates the correct orientation of each element. Note that the
#   starting location is noted with an 'S' and the ending location is noted with
#   an 'E' for each tray.

#          Top (closest to X - X' Motor)
#   |---------------------------------------|
#   |               In Tray                 |
#   | S                                     |
#   |---------------------------------------|
#   |                                       |
#   |                                     E |
#   |---------------------------------------|
#
#   |---------------------------------------|
#   |               Out Tray                |
#   | E                                     |
#   |---------------------------------------|
#   |                                       |
#   |                                     S |
#   |---------------------------------------|
#       Bottom (closest to control unit)
#
#       TRAY ORIENTATION (TOP DOWN VIEW)

#   TESTS
#   Below are enumerated tests and data that can be collected using this program
#   1. Validation - can the machine pull an overlay from a tray.
#   2. 3 Shot Burst - setting the END_COUNT to 3, can the machine pull three
#       PCB's consecutively from the tray?
#   3. Pick of 50 - Pick all 50 PCB's from the input tray? We are looking for
#       any positional error that creeps into the picking operation.
#   4. Grab Location - How consistent is the vacuum position from PCB to PCB?
#   5. Pick and Place - Can the machine pick an overlay up and place it directly
#       back in the same location?
#   6. Pick and Place Next - Can the machine pick up and overlay and place it in
#       the next tray?
#   7. Pick and Place 3 - same procedure as 6, but for 3 PCB's
#   8. Pick and Place 50 - same procedure as 6, but for 50 PCB's

from RINGO import *
import time

# DEFINE CONSTANTS
TRAY_POS1_X = 585           # mm - position of OUT start
TRAY_POS2_X = 670           # mm - position to OUT end
TRAY_POS3_X = 785           # mm - position to IN end
TRAY_POS4_X = 890           # mm - poistion to IN start
DROP_POS_X  = 333           # mm - position of PCB drop

TRAY_POS1_Y =  54           # mm - position of first vacuum contact
DROP_POS_Y  = 198           # mm - position of backing drop
Y_OFFSET    =   8.5         # gain - offset multiplier to calculate position

CRIT_DELAY = 7              # seconds - maximium travel time delay

Y_SPEED = 800               # mm / min - speed gantry when removing

CONTIN_MODE = True
DROP_MODE = True            # 1 - drop at location | 0 - drop in out tray
COMPLETE_FLAG = False       # flag to indicate that all PCB's in output Tray
END_COUNT = 5

# DEFINE GLOBALS
r = RINGO()                 # create and init Machine Object
count = 0
currPos = 0

# getCurrentPos()
#
#   This function retrieves the current position from the text file where an
#   uncomplete position will be stored.
def getCurrentPos() :
    global currPos

    data = open("meta.txt","r")
    str = data.read()
    currPos = str.split("pos:")[1]
    data.close()


# resetCurrentPos()
#
#   This function sets the current position to zero.
def resetCurrentPos() :
    global currPos

    currPos = 0
    data = open("meta.txt","w")
    str = "pos:" + 0
    data.write(str)
    data.close()

# setCurrentPos()
#
#   This function sets the current position to the given value.
def resetCurrentPos(newPos) :
    global currPos

    currPos = newPos
    data = open("meta.txt","w")
    str = "pos:" + newPos
    data.write(str)
    data.close()

# getXPosIn()
#
#   This function calculates and returns the correct X position of the Input
def getXPosIn() :
    global currPos
    global TRAY_POS4_X
    global TRAY_POS3_X

    if(currPos < 25) :
        return TRAY_POS4_X
    else :
        return TRAY_POS3_X

# getXPosOut()
#
#   This function calculates and returns the correct X position of the Output
def getXPosOut() :
    global DROP_MODE
    global DROP_POS_X
    global currPos
    global TRAY_POS1_X
    global TRAY_POS2_X

    if(DROP_MODE) :
        return DROP_POS_X
    else :
        if(currPos < 25) :
            return TRAY_POS1_X
        else :
            return TRAY_POS2_X

# getYPosIn()
#
#   This function calculate and returns the correct Y position of the Input
def getYPosIn() :
    global currPos
    global TRAY_POS1_Y
    global Y_OFFSET

    trayPos = TRAY_POS1_Y + ((currPos % 25) * Y_OFFSET)
    currPos += 1

    return trayPos


# getYPosOut()
#
#   This function calculate and returns the correct Y position of the Output
def getYPosOut() :
    global DROP_MODE
    global DROP_POS_Y
    global currPos

    if(DROP_MODE) :
        return DROP_POS_Y
    else :
        return TRAY_POS1_Y + (((49 - currPos) % 25) * Y_OFFSET)


# getPCB()
#
#   This function manages all the movements and actions required to get the
#   next PCB.
def getPCB() :
    global CONTIN_MODE
    global count
    global END_COUNT
    global r

    # Update the continuous mode
    if(CONTIN_MODE and count == END_COUNT) :
        CONTIN_MODE = False

    x_pos = getXPosIn()
    y_pos = getYPosIn()
    x_pos_out = getXPosOut()
    y_pos_out = getYPosOut()

    print("X Position: ",x_pos)
    print("Y Position: ",y_pos)
    print("X Position Out: ",x_pos_out)
    print("Y Position Out: ",y_pos_out)

    print("Knight to A4!")

    # Move to pickup location, grab durring movement
    r.tinyG.write('g0 x' + str(x_pos))
    time.sleep(CRIT_DELAY)
    r.tinyG.write('g1 F800 y' + str(y_pos))
    r.head.extend()
    time.sleep(5 + ((currPos % 25)) / 2)
    r.head.grab()
    time.sleep(2)

    # Move to drop location - drop PCB
    r.head.retract()
    r.tinyG.write('g0 y' + str(0))
    time.sleep(3)
    r.head.rotateDown()
    r.tinyG.write('g0 x' + str(x_pos_out))
    time.sleep(CRIT_DELAY)
    r.tinyG.write('g0 y' + str(y_pos_out))
    time.sleep(4)
    r.head.drop()
    r.head.rotateUp()

    # Return to HOME
    r.tinyG.write('g0 y' + str(1))
    r.tinyG.write('g0 x' + str(1))
    time.sleep(CRIT_DELAY + 5)



def main() :
    global CONTIN_MODE

    getPCB()
    while(CONTIN_MODE) :
        #response = raw_input("Run Again? (enter 'y') : ")
        #if response == 'y' :
        #    getPCB()
        #else :
        #    CONTIN_MODE = False
        getPCB()

    print("TrayUnloadTest is complete")
main()
