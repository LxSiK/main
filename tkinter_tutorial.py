# incorporating TK
from tkinter import *
from tkinter import ttk
 
 # performing the calculation
def calculate(*args):
     try:
         value = float(feet.get())
         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
     except ValueError:
         pass
 
 # setting up the main application window
root = Tk()
root.title("Feet to Meters")
 
 # creating a content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 
 # creating the entry widget
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
 
 # creating the remaining widgets
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
 
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
 
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
 
# polishing
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

# start the event loop
root.mainloop()