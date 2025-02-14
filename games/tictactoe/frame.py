# display all frame effects

import tkinter as tk

#set up set of different effects
effects = {
    "flat" : tk.FLAT,
    "rasied" : tk.RAISED,
    "sunken" : tk.SUNKEN,
}

#set up window
window = tk.Tk()

for index, relief in effects.items():
    frame = tk.Frame(master = window, relief = relief, borderwidth = 5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master = frame, text = index)
    label.pack()


#set up frame
#frame =tk.Frame()
#rame.pack()
#set up button & assign it to the frame
#button = tk.Button(master = frame, text = "click me",)
#utton.pack()




###############GO FROM THE GEOMETRY MANAGER SECTION OF https://realpython.com/python-gui-tkinter/


window.mainloop()
