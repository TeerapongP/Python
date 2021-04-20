import math
Menu_List = []

def ShowBill():#เเสดงบิล

    Result_Total = 0
    Result_Vat = 0
    vat = 7/100
    print("---- My FOOD ----")
    for i in range(len(Menu_List)):
        print("รายการอาหารที่สั่ง :",Menu_List[i][0])
        Result_Vat += int(Menu_List[i][1])
    print("VAT IS 7%")
    Result_Total = Result_Vat+(Result_Vat * vat)
    print("ราคารวม :",math.ceil(Result_Total),"Bath")
    



while True:

    Menu_Name = input("ENTER MENU : ")#ใส่ชื่อMenu อาหาร
    if (Menu_Name.lower() == "exit"): 

       break

    else:

        Menu_Price = int(input("PRICE : "))
        Menu_List.append([Menu_Name,Menu_Price])

ShowBill()