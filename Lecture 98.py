from tkinter import *

_Main_Windows_  = Tk()

def _left_Click_Button(event):
    print("Left Click")

def _Double_Click_Button(event):
    print("Double Click")
 
def _Main_Button_Windows():
    _My_Button = Button(_Main_Windows_,text="Click Me.")
    _My_Button.pack()
    _My_Button.bind('<Button-1>',_left_Click_Button)
    _My_Button.bind('<Double-1>',_Double_Click_Button)
    _Main_Windows_.mainloop()

def Main_Function():
    _Main_Button_Windows()

Main_Function()