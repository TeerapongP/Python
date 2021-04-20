from tkinter import *
import math

_Main_Windows_ = Tk()

def _Calculate_Function_(event):

    #คำนวน
    _Result_Calculate_ = float(_Text_Box_Weight_.get())/math.pow(float(_Text_Box_Height_.get())/100,2)

    #เเสดงค่าออกมา
    _Lable_Result_.configure(text="%.2f" %(_Result_Calculate_))

    #ฟังชั่น IF-ELIF-ELSE
    if(_Result_Calculate_>30):
        _Lable_Show_Function_.configure(text="อ้วนมาก.")

    elif(_Result_Calculate_>25.0 and 29.9):
        _Lable_Show_Function_.configure(text="อ้วน.")

    elif(_Result_Calculate_>23.0 and 24.9):
        _Lable_Show_Function_.configure(text="น้ำหนักเกินนะเราอะ.")

    elif(_Result_Calculate_>18.6 and 22.9):
        _Lable_Show_Function_.configure(text="น้ำหนักปกติ เหมาะสม.")
    
    else:
        _Lable_Show_Function_.configure(text="ผอมเกินไป.")

 #เเสดงค่าตัวอักษร ส่วนสูงกับน้ำหนัก
_Height_Lable_ = Label(_Main_Windows_,text='ส่วนสูง (CM.) :',font=("Consola")).grid(row=0,column=0)
_Weight_Lable_ = Label(_Main_Windows_,text='น้ำหนัก (KG.) :',font=("Consola")).grid(row=1,column=0)

 #เเสดงกล่องรับค่าส่วนสูงกับน้ำหนัก
_Text_Box_Height_ = Entry(_Main_Windows_,font=("Consola"))
_Text_Box_Height_.grid(row=0,column=1)
_Text_Box_Weight_ = Entry(_Main_Windows_,font=("Consola"))
_Text_Box_Weight_.grid(row=1,column=1)

 #เเสดงปุ่มคำนวนน้ำหนักเเละส่วนสูง
_Calculate_Button = Button(_Main_Windows_,text="คำนวนน้ำหนัก",font=("Consola"))
_Calculate_Button.grid(row=2,column=0)
_Calculate_Button.bind('<Button-1>',_Calculate_Function_)

#เเสดงผลลัพม์ของน้ำหนัก
_Lable_Result_ = Label(_Main_Windows_,text="ผลลัพธ์",font=("Consola"))
_Lable_Result_.grid(row=2,column=1)

#เเสดงค่าว่าอ้วนไหม
_Lable_Show_Function_ = Label(_Main_Windows_,text="",font=("Consola"))
_Lable_Show_Function_.grid(row=2,column=2)
_Main_Windows_.mainloop()

