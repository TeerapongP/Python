from tkinter import *

Main_Windows = Tk()

def SayHello():
    print("Hello World")

def _Main_Windows_():
    button = Button(Main_Windows,text="Click Me",command= SayHello,width=20,height=3,bg="red").grid(row=0,column=0) 
    button2 = Button(Main_Windows,text="Click Me2",command= SayHello,width=20,height=3,bg="green").grid(row=1,column=0)
    button3 = Button(Main_Windows,text="Click Me2",command= SayHello,width=20,height=3,bg="blue").grid(row=2,column=0)
    
    Main_Windows.mainloop()



_Main_Windows_()