from tkinter import *

Main_Windows = Tk()

def SayHello():
    print("Hello World")

def _Main_Windows_():
    button = Button(Main_Windows,text="Click Me",command= SayHello).grid(row=0,column=0) 
    button2 = Button(Main_Windows,text="Click Me2",command= SayHello).grid(row=1,column=0)
    button3 = Button(Main_Windows,text="Click Me2",command= SayHello).grid(row=2,column=0)
    Main_Windows.mainloop()


_Main_Windows_()