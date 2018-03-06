import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('RINGO MACHINGO CONTROLS')
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill='both')
win.mainloop()
