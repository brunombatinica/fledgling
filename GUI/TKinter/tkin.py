import tkinter as tk

#set up window
window = tk.Tk()

#set up frame
frame =tk.Frame()
frame.pack()
#set up button & assign it to the frame
button = tk.Button(master = frame, text = "click me",)
button.pack()


window.mainloop()
