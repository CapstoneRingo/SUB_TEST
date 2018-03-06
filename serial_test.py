import devices

# Create USB Port
port1 = serial.Serial('/dev/ttyACM0',19200,timeout=None)

# Define Ringo Machinego devices
head_lin = devices('Head_Linear','0',port1)
head_rot = devices('Head_Rotary','1',port1)
roller = devices('Roller','2',port1)
jig = devices('Jig','3',port1)
vacuum = devices('Vacuum','4',port1)
overlay_pusher = devices('Overlay_Pusher','5',port1)
backing_pinner = devices('Backing_Pinner','6',port1)
