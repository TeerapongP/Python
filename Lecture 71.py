Menu_List = []
Price_List = []

def ShowBill():#เเสดงบิล

    Result_Total = 0
    vat = 7/100
    print("---- My FOOD ----")
    for i in range(len(Menu_List)):
        Result_Total += Price_List[i]
        print(Menu_List[i],Price_List[i],"Bath")
    print("VAT IS 7%")
    print("ราคารวม :",Result_Total+(Result_Total*vat),"BATH")    
        
while True:

    Menu_Name = input("ENTER MENU : ")#ใส่ชื่อMenu อาหาร
    if (Menu_Name.lower() == "exit"): 

       break

    else:

        Menu_Price = int(input("PRICE : "))
        Menu_List.append(Menu_Name)
        Price_List.append(Menu_Price)

ShowBill()