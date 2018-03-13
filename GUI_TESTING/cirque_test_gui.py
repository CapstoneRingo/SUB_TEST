from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Cirque Overlay Applicator")

        self.pause_resume_text = "pause"


        self.progress_label = Label(master, text="Progress: ")
        self.reject_label = Label(master, text="Rejected: ")


        self.start_button = Button(master, text="start", command=lambda: self.update("start"), command=self.color_change, bg="green")
        self.pause_resume_button = Button(master, text_variable=self.resume_text, command=lambda: self.update("pause"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.progress_label.grid(row=0, column=0, sticky=W)
        self.reject_label.grid(row=0, column=1, columnspan=2, sticky=E)


        self.start_button.grid(row=2, column=0)
        self.pause_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "start":
            print("Starting the Program")
            # Do something useful (start with calibration/zero position)
        elif method == "pause":
            self.pause_resume_text = "resume"
            print("System Paused")
            # Stop the process, but save the variables 
        elif method == "resume":
            self.pause_resume_text = "pause"
            print("System Resumed")

        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()