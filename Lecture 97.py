from tkinter import *

Main_Windows = Tk()

def SayHello():
    print("Hello World")

def _Main_Windows_():
   text1 = Label(Main_Windows,text="Hello World",width=20,fg="red",font=('Consolar',76)).grid(row=0,column=0)
   Main_Windows.mainloop()



_Main_Windows_()