import math

System_Menu = {"ข้าวมันไก่":40,"ข้าวหมูทอด":50,"โจ๊กหมู":35}
Menu_List = []

def ShowBill():#เเสดงบิลเเละทำการคำนวน

    Result_Total = 0
    vat = 7/100
    Result_Vat = 0

    print("---- My FOOD ----")
    for i in range(len(Menu_List)):
        print("รายการอาหารที่สั่ง :",Menu_List[i][0],Menu_List[i][1],"Bath") 
        Result_Total += Menu_List[i][1]
        Result_Vat = Result_Total+(Result_Total*vat)

    print("VAT 7%")
    print("ราคาก่อนรวม Vat :",Result_Total,"Bath")
    print("ราคาหลังรวม Vat :",math.ceil(Result_Vat),"Bath")
    
#ฟังชั่น Loop
while True:

    Menu_Name = input("ENTER MENU : ")#ใส่ชื่อMenu อาหาร
    if (Menu_Name.lower() == "exit"): 
        break

    else:
        Menu_List.append([Menu_Name,System_Menu[Menu_Name]])

ShowBill()