from tkinter import *

Main_Windows = Tk()

def SayHello():
    print("Hello World")

def _Main_Windows_():
    button = Button(Main_Windows,text="Click Me",command= SayHello)
    button.place(x=50,y=20)
    Main_Windows.mainloop()

_Main_Windows_()