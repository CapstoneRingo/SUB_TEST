import tkinter as tk
import devices
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

# RINGO GUI main app class: create instance to run application
class RINGO_GUI:

    # Initialize: build all widgets, link and pack, and start main loop
    def __init__(self,test_mode=0):
        # define USB port to command pneumatics with
        self.testmode = test_mode

        if test_mode == 0:
            self.port = serial.Serial('/dev/ttyACM0',19200,timeout=None)
        else:
            self.port = 'Poop'


        # define root
        self.root = tk.Tk()
        self.root.title('RINGO MACHINE-GO')

        # initialize devices list
        self.devices = []

        # Define devices
        self.define_devices()

        # Define widgets

        # Layout widgets

        # Begin main loop
        self.root.mainloop()

    def define_devices(self):
        self.devices.append(device_TK(self.root,'Head (Linear)','0',self.port,
        self.testmode))
        self.devices.append(device_TK(self.root,'Head (Rotary)','1',self.port,
        self.testmode))
        self.devices.append(device_TK(self.root,'Roller','2',self.port,
        self.testmode))
        self.devices.append(device_TK(self.root,'Jig','3',self.port,self.testmode))
        self.devices.append(device_TK(self.root,'Overlay Pusher','5',self.port,
        self.testmode))
        self.devices.append(device_TK(self.root,'Vacuum','4',self.port,
        self.testmode))
        self.devices.append(device_TK(self.root,'Backing Pinner','6',self.port,
        self.testmode))

        for d in self.devices:
            d.frame.pack()

# Main application
if __name__ == '__main__':

    window = RINGO_GUI(1)
