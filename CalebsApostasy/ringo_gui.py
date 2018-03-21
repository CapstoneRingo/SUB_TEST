#	FILE NAME 	:	ringo_gui.py
#	AUTHOR 		: 	Caleb Groves
# 	CONTRIBUTORS   	: 	Nolan McCulloch
#	DATE CREATED   	:	3 Mar 2018
#	PYTHON VER     	:	2.7
#	REVISION       	:	1.0.2

import Tkinter as tk
import devices
from TinyG import TinyG
import serial

# Device TKinter View
class device_TK:

    def __init__(self,parent,name,GPIO,port,testmode=0):
        self.device = devices.device(name,GPIO,port) # define serial device
        self.testmode = testmode
        self.device.setLow(self.testmode) # set device to OFF initially
        self.state = 0

        self.frame = tk.Frame(parent) # define GUI frame object
        self.label = tk.Label(self.frame,justify='left',anchor='center',
        text=self.device.name + ':',width=20)
        self.button = tk.Button(self.frame,text='OFF',fg='white',bg='red',
        command=self.switch,width=10)

        # Pack together in frame grid
        self.label.grid(row=0,column=0)
        self.button.grid(row=0,column=1)

    def switch(self):
        self.state ^= 1 # switch state

        if self.state == 1:
            self.device.setHigh(self.testmode)
            self.button.config(text='ON',bg='green')
        elif self.state == 0:
            self.device.setLow(self.testmode)
            self.button.config(text='OFF',bg='red')

# Gantry Controls GUI
class GantryControls:

    def __init__(self,parent,tinyG):
        self.parent = parent
        self.tinyG = tinyG
        self.UIFrame = tk.LabelFrame(self.parent,text='Gantry Controls')

        # Define buttons
        self.defineUIControls()

        self.UIFrame.pack(side=tk.RIGHT)

    def defineUIControls(self):
        # Make buttons
        self.posXButton = tk.Button(self.UIFrame,text='+X',command=self.jogXPos)
        self.negXButton = tk.Button(self.UIFrame,text='-X',command=self.jogXNeg)
        self.posYButton = tk.Button(self.UIFrame,text='+Y',command=self.jogYPos)
        self.negYButton = tk.Button(self.UIFrame,text='-Y',command=self.jogYNeg)

        # arrange in Frame
        self.UIFrame.columnconfigure(5,minsize=20)
        self.UIFrame.rowconfigure(5,minsize=20)

        self.posYButton.grid(row=1,rowspan=2,column=3,columnspan=1,ipadx=3,
        ipady=3)
        self.negYButton.grid(row=4,rowspan=2,column=3,columnspan=1,ipadx=3,
        ipady=3)
        self.negXButton.grid(row=3,rowspan=1,column=1,columnspan=2,ipadx=3,
        ipady=3)
        self.posXButton.grid(row=3,rowspan=1,column=4,columnspan=2,ipadx=3,
        ipady=3)

    def jogXPos(self):
        self.tinyG.write('G0 X10')

    def jogXNeg(self):
        self.tinyG.write('G0 X-10')

    def jogYPos(self):
        self.tinyG.write('G0 Y10')

    def jogYNeg(self):
        self.tinyG.write('G0 Y-10')

# Backing Axis Controls UI
class BackingAxisControls:

    def __init__(self,parent,tinyG):
        self.parent = parent

        self.tinyG = tinyG

        self.UIFrame = tk.LabelFrame(self.parent,text='Backing Axis')

        # Define buttons
        self.defineUIControls()

        self.UIFrame.pack(side=tk.RIGHT)

    def defineUIControls(self):

        self.upButton = tk.Button(self.UIFrame,text='Up',command=self.jogUp)
        self.downButton = tk.Button(self.UIFrame,text='Down',command=self.jogDown)

        # arrange
        self.UIFrame.columnconfigure(3,minsize=10)
        self.UIFrame.rowconfigure(7,minsize=20)

        self.upButton.grid(row=2, column=2, rowspan=2, columnspan=1,
        ipadx=3, ipady=3)
        self.downButton.grid(row=7, column=2, rowspan=2, columnspan=1,
        ipadx=3, ipady=3)

    def jogUp(self):
        self.tinyG.write('G0 Z5')

    def jogDown(self):
        self.tinyG.write('G0 Z-5')

# RINGO GUI main app class: create instance to run application
class RINGO_GUI:

    # Initialize: build all widgets, link and pack, and start main loop
    def __init__(self,test_mode=0):
        # define USB port to command pneumatics with
        self.testmode = test_mode

        if test_mode == 0:
            USB_PORT_0 = "/dev/ttyACM0"
            USB_PORT_1 = "/dev/ttyACM1"

            # Set up serial connection
            try:
                self.port = serial.Serial(USB_PORT_0, 9600, timeout=None)
            except Exception as e:
                 self.port = serial.Serial(USB_PORT_1, 9600, timeout=None)

            print "Using serial port " + self.port.port

        else:
            self.port = 'Poop'


        # define root
        self.root = tk.Tk()
        self.root.title('RINGO MACHINE-GO')

        # initialize devices list
        self.devices = []

        # Define devices
        self.define_devices()

        # TinyG controller
        self.tinyG = TinyG('USB0')

        # Make Axis Controls
        self.create_axis_controls()

        # Add G-code text box
        self.gCodeInput()

        # Begin main loop
        self.root.mainloop()

    def define_devices(self):

        # Define pneumatics frame
        self.pneumaticsFrame = tk.LabelFrame(self.root,text='Pneumatics Controls')

        # Define all of the pneumatics controls
        self.add_pneumatic('0','0')
        self.add_pneumatic('1','1')
        self.add_pneumatic('2','2')
        self.add_pneumatic('3','3')
        self.add_pneumatic('4','5')
        self.add_pneumatic('5','4')
        self.add_pneumatic('6','6')
        self.add_pneumatic('7','7')

        for d in self.devices:
            d.frame.pack()

        # pack pneumatics frame into main window
        self.pneumaticsFrame.pack()

    def add_pneumatic(self,name,GPIO):
        self.devices.append(device_TK(self.pneumaticsFrame,name,GPIO,self.port,
        self.testmode))

    def create_axis_controls(self):
        # Create label frame for buttons
        self.gantryControls = GantryControls(self.root,self.tinyG)
        self.backingAxisControls = BackingAxisControls(self.root,self.tinyG)

    def gCodeInput(self):
        # Add Frame
        self.gCodeFrame = tk.LabelFrame(self.root,text='G Code Input')
        self.gCodeEdit = tk.Entry(self.gCodeFrame,bd=5)
        self.gCodeEdit.pack(side=tk.LEFT)
        self.gCodeSend = tk.Button(self.gCodeFrame,text='SEND',command=self.writeGCode)
        self.gCodeSend.pack(side=tk.RIGHT)
        self.gCodeFrame.pack(side=tk.RIGHT)

    def writeGCode(self):
        # Get text from gCodeEdit
        gCmd = self.gCodeEdit.get()

        self.tinyG.write(gCmd)


    def on_closing(self):
        if self.testmode == 0:
            self.port.close()
            print "%s closed. Goodbye!" % (self.port.name)
        else:
            print "Ending test. Good day!"


# Main application
if __name__ == '__main__':

    window = RINGO_GUI(0)
