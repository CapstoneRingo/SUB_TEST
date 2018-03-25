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
#   that illustrates the correct orientation of each element. s

#   TESTS
#   Below are enumerated tests and data that can be collected using this program
#   1. Validation - can all the devices work together to get stuff done.
#   2. 3 Shot Burst - setting the END_COUNT to 3, can the machine do 3
#       consecutive removals. We can measure vacuum position variance from
#       overlay to overlay and error in the positioning to help determine how
#       often the head should be home'd.
#   3. Run of 50 - THE ULTIAMTE CHALLENGE! Can this do what we think it will do
#       for an extended period of time?
#   4. Edge Testing - What happens when the overlay is upside down? What happens
#       if there is not an overlay in position?
#   5. Placement - The third position can easily be set to the location of the
#       placement subsystem. We can test dropping multiple overlays into the
#       jig to see if there are issues with the placement stuff without having
#       to build and program the whole system.

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


def getOverlay() :
    # Define and display the itteration
    count += count
    print("Overlays Removed = " + count)

    #OPTIONAL FEATURE: shut down after 'n' overlays are placed
    if(count == END_COUNT) :
       CONTIN_MODE = False

    # Rotate Head down and go to 'Grab overlay from stack' position
    r.head.rotateDown()
    r.gcode('g0 y'+str(BKRM_POS1_Y))
    r.gcode('g0 x'+str(BKRM_POS1_X))
    time.sleep(CRIT_DELAY)

    raw_input("Continue?")

    # Head sequence required to pick up an overlay
    r.backingRemoval.push()
    r.head.extend()
    r.head.grab()
    r.backingRemoval.motorOn()

    raw_input("Continue?")
    #Pull overlay up to roller and recenter vacuum head

    # Completely pull overly over roller at complete remove position.
    r.gcode('g1 F20 x'+str(BKRM_POS2_X)) # CHANGE TO SLOW!!!
    r.gcode('g1 F40 z'+str(BKRM_POS2_Z))
    time.sleep(DRAG_DELAY)

    # Retract the head system and return backing removal to rest state
    r.backingRemoval.motorOff()
    r.head.retract()

    # Move to drop location.
    r.gcode('g0 x'+str(BKRM_POS3_X))
    time.sleep(CRIT_DELAY)

    # Drop the overlay and get into joggin position.
    r.head.drop()
    r.head.rotateUp()



def main() :
    #SPENCER: Pretty sure these are done when r = RINGO() is created
    #r.getSettled()                  # does this need to come before homing?
    #r.home()                        # Q: is there a way to home? Can we wrap this?

    getOverlay()
    while(CONTIN_MODE) :
        getOverlay()

main()
