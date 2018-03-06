# import tkinter as tk
# from tkinter import ttk
#
# win = tk.Tk()
# win.title('RINGO MACHINGO CONTROLS')
# tabControl = ttk.Notebook(win)
# tab1 = ttk.Frame(tabControl)
# tabControl.add(tab1, text='Tab 1')
# tabControl.pack(expand=1, fill='both')
# win.mainloop()
#


import tkinter as tk


# Main Window Application Class
class Window:

    def __init__(self):
        self.root = tk.Tk() # main Window
        self.label = tk.Label(self.root, fg='green', text='Begin')
        self.button = tk.Button(self.root, text='Increment', width=25, command=self.inc_lbl)
        self.button2 = tk.Button(self.root, text='Decrement', width=25, command=self.dec_lbl)

        self.counter = 0 # counter var

        # Pack widgets
        self.label.pack()
        self.button.pack()
        self.button2.pack()

        # Start main main
        self.root.mainloop()

    def inc_lbl(self):
        # increment counter
        self.counter += 1
        self.label.config(text=str(self.counter))

    def dec_lbl(self):
        self.counter -= 1
        self.label.config(text=str(self.counter))


# Run from command line
if __name__ == '__main__':
    window = Window()
