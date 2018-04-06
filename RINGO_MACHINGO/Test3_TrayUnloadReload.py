#	FILE NAME 		:	MIGHTY_JOE_YOUNG.py
#	AUTHOR 			: 	Nolan McCulloch
#	CONTRIBUTORS	: 	Caleb Groves, Spencer Diehl
#	DATE CREATED	:	5 April 2018
#	PYTHON VER		:	2.7
#	REVISION		:	1.0.1

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
#   |                                     E |
#   |---------------------------------------|
#   |                                       |
#   | S                                     |
#   |---------------------------------------|
#
#   |---------------------------------------|
#   |               Out Tray                |
#   |                                     S |
#   |---------------------------------------|
#   |                                       |
#   | E                                     |
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
TRAY_POS1_X = 560.0         # mm - position of OUT end
TRAY_POS2_X = 647.7         # mm - position to OUT start
TRAY_POS3_X = 783.0         # mm - position to IN start
TRAY_POS4_X = 871.0         # mm - poistion to IN end

TRAY_POS1_Y =  49.5         # mm - position of first vacuum contact
TRAY_POS2_Y = 253.0         # mm - position of last vacuum contact

Y_OFFSET    =   8.44        # gain - offset multiplier to calculate position

JOG_POS_Y   =   5.0         # mm - y Position of Jog Position

CRIT_DELAY = 7              # seconds - maximium travel time delay

CONTIN_MODE = True
COMPLETE_FLAG = False       # flag to indicate that all PCB's in output Tray
END_COUNT = 51

# DEFINE GLOBALS
#r = RINGO()                 # create and init Machine Object
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
        return TRAY_POS3_X
    else :
        return TRAY_POS4_X

# getXPosOut()
#
#   This function calculates and returns the correct X position of the Output
def getXPosOut() :
    global currPos
    global TRAY_POS1_X
    global TRAY_POS2_X

    if(currPos < 25) :
        return TRAY_POS2_X
    else :
        return TRAY_POS1_X

# getYPosIn()
#
#   This function calculate and returns the correct Y position of the Input
def getYPosIn() :
    global currPos
    global TRAY_POS1_Y
    global Y_OFFSET

    trayPos = TRAY_POS1_Y + ((currPos % 25.0) * Y_OFFSET)

    return trayPos


# getYPosOut()
#
#   This function calculate and returns the correct Y position of the Output
def getYPosOut() :
    global currPos
    global Y_OFFSET
    global TRAY_POS2_Y

    trayPos_out = TRAY_POS2_Y - ((currPos % 25.0) * Y_OFFSET)
    currPos += 1
    return trayPos_out


def getPCB(x_pos, y_pos) :
    global r

    # Move to pickup location, grab durring movement
    r.tinyG.write('g0 x' + str(x_pos))
    time.sleep(5)
    r.tinyG.write('g0 y' + str(y_pos))
    r.head.extend()
    time.sleep(4)
    r.head.grab()
    time.sleep(0.5)
    r.head.retract()
    r.tinyG.write('g0 y40')
    time.sleep(4)

# setInOutput
#
# This function takes the two output positions and writes to them.
def setInOutput(x_pos_out, y_pos_out) :
    global r

    # Place in Output
    r.tinyG.write('g0 x' + str(x_pos_out))
    time.sleep(7)
    r.tinyG.write('g0 y' + str(y_pos_out))
    time.sleep(4)
    r.head.extend()
    time.sleep(0.5)
    r.tinyG.write('g0 y' + str(JOG_POS_Y))
    r.head.drop()
    time.sleep(4)

# getPCB()
#
#   This function manages all the movements and actions required to get the
#   next PCB.
def run() :
    global CONTIN_MODE
    global currPos
    global END_COUNT
    global r

    # Update the continuous mode
    if(CONTIN_MODE and currPos == END_COUNT) :
        CONTIN_MODE = False
    else :
        x_pos = getXPosIn()
        y_pos = getYPosIn()
        x_pos_out = getXPosOut()
        y_pos_out = getYPosOut()

        print("GET --> X Position: ",x_pos,"\t Y Position: ",y_pos)
        print("SET --> X Position: ",x_pos_out,"\t Y Position: ",y_pos_out)

        print("Knight to A4!")

        getPCB(x_pos, y_pos)
        setInOutput(x_pos_out, y_pos_out)

def main() :
    global CONTIN_MODE
    global currPos

    run()
    while(CONTIN_MODE) :
        print('CURRENT POSITION : ',currPos)
        runForrest()


    print("TrayUnloadTest is complete")
main()
