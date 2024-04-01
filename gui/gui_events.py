import tkinter
from tkinter import messagebox

def on_off():
    global switch
    if switch:
        button2.config(command=lambda: None)
        button2.config(text="Gee!")
    else:
        button2.config(command=peekaboo)
        button2.config(text="Peekaboo")
    switch = not switch

def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")

def do_nothing():
    pass

switch = True
window = tkinter.Tk()

button1 = tkinter.Button(window, text="On/Off", command=on_off)
button1.pack()

button2 = tkinter.Button(window, text="Peekaboo", command=peekaboo)
button2.pack()

window.mainloop()