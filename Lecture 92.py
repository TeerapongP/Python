from tkinter import *


def SayHello():
    print("Hello World")

Main_Windows = Tk()

button = Button(Main_Windows,text="Click Me",command= SayHello)
button.place(x=50,y=20)
Main_Windows.mainloop()

