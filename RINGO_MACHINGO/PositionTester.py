from RINGO import *
import time

CRIT_DELAY = 3              # sec - delay of movement

r = RINGO()

x_position = 0
y_position = 0

# Tray Location Estimation
while(True) :
    print("\n****************************\nINPUT\nEnter 'nope' for no change")

    y_next = input("Enter the next 'Y' position: ")
    x_next = input("Enter the next 'X' position: ")

    if(y_next != 'nope') :
        y_position = y_next
    if(x_next != 'nope') :
        x_position = x_next

    r.TinyG.write('g1 F800 y' + str(y_position))
    time.sleep(CRIT_DELAY)
    r.TinyG.write('g0 x' + str(x_position))
    time.sleep(CRIT_DELAY)
