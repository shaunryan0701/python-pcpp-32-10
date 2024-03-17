import tkinter
from tkinter import messagebox

def click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()

skylight = tkinter.Tk()
skylight.title("Yeah this is bollocks")
button = tkinter.Button(skylight, text="Bye", command=click)
button2 = tkinter.Button(skylight, text="Hello", command=click)
button3 = tkinter.Button(skylight, text="Nope", command=click)
button.place(x=10, y=10)
button2.place(x=20, y=40)
button3.place(x=30, y=70)

skylight.mainloop()