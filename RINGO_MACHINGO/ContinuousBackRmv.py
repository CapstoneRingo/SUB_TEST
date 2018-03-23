#	FILE NAME 		:	ContinuousBackRmv.py
#	AUTHOR 			: 	Nolan McCulloch
# 	CONTRIBUTORS	: 	Caleb Groves, Spencer Diehl
#	DATE CREATED	:	23 MAR 2018
#	PYTHON VER		:	2.7
#	REVISION		:	1.0.1

#	INFO
#   This programm simply homes the gantry axis system and then moves to the
#   position directly in front of the backing removal station. It then initiates
#   and runs a full backing removal routine.

#   The program has 2 main modes. A single removal mode or a continuous removal
#   mode where the backings are removed continuously and dropped in a specified
#   location.

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
BKRM_POS1_X = 375           # mm - position of first vacuum contact
BKRM_POS2_X =               # mm - position to create initial peel
BKRM_POS3_X =               # mm - position to completely remove backing
DROP_POS_X  = 250           # mm - position of backing drop

BKRM_POS1_Y = 430           # mm - position of first vacuum contact
DROP_POS_Y  = 250           # mm - position of backing drop

BKRM_POS1_Z = 0             # mm - position of roller at first overlay contact
BKRM_POS1_Z = 10            # mm - position of roller to create initial peel
BKRM_POS1_Z = 15            # mm - position of roller to release backing paper

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
    r.gcode('g0 x'+str(BKRM_POS1_X))
    r.gcode('g0 y'+str(BKRM_POS1_Y))
    time.sleep(CRIT_DELAY)

    # Head sequence required to pick up an overlay
    r.backingRemoval.push()
    r.head.extend()
    r.head.grab()
    r.backingRemoval.motorOn()

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
