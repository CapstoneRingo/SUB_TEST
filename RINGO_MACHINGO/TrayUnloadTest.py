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
BKRM_POS1_X = 377           # mm - position of first vacuum contact
BKRM_POS2_X = 365           # mm - position to create initial peel
BKRM_POS3_X = 355           # mm - position to completely remove backing
DROP_POS_X  = 250           # mm - position of backing drop

BKRM_POS1_Y = 430           # mm - position of first vacuum contact
DROP_POS_Y  = 250           # mm - position of backing drop

BKRM_POS1_Z = 35            # mm - position of roller at first overlay contact
BKRM_POS1_Z = 10            # mm - drop of roller to create initial peel
BKRM_POS1_Z = 15            # mm - drop of roller to release backing paper

CRIT_DELAY = 10             # seconds - maximium travel time delay
DRAG_DELAY = 5              # seconds - delay required to remove backing

DRAG_SPEED =                # mm / min - speed gantry when removing

CONTIN_MODE = False
END_COUNT = 0

# DEFINE GLOBALS
r = RINGO()                 # create and init Machine Object
count = 1
Current_Pos = 0

# getCurrentPos()
#
#   This function retrieves the current position from the text file where an
#   uncomplete position will be stored.
def getCurrentPos() :
    data = open("meta.txt","r")
    str = data.read()
    Current_Pos = str.split("pos:")[1]
    data.close()


# resetCurrentPos()
#
#   This function sets the current position to zero.
def resetCurrentPos() :
    Current_Pos = 0
    data = open("meta.txt","w")
    str = "pos:" + 0
    data.write(str)
    data.close()

# setCurrentPos()
#
#   This function sets the current position to the given value.
def resetCurrentPos(newPos) :
    Current_Pos = newPos
    data = open("meta.txt","w")
    str = "pos:" + newPos
    data.write(str)
    data.close()


def getPCB() :




def main() :
    #SPENCER: Pretty sure these are done when r = RINGO() is created
    #r.getSettled()                  # does this need to come before homing?
    #r.home()                        # Q: is there a way to home? Can we wrap this?

    getOverlay()
    while(CONTIN_MODE) :
        getOverlay()

main()
