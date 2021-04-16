username = input("ENTER USERNAME :")
passw = input("ENTER PASSWORD :")
vat = 7 / 100

if username == "admin" and passw == "1234":
    print("Done !!")
    print("------ Wellcme to MangaBook ------")
    print("1. Select Product ")
    userSelected = int(input("Enter Number : "))
    if userSelected == 1:
        print("1. เจ้าสาวผมเป็นแฝดห้า 45 BATH")
        print("2. มหาศึกคนชนเทพ 145 BATH")
        print("3. Attack on titan 55 BATH")
        userSelected2 = int(input("Enter Number : "))
        if userSelected2 == 1:
            price_all = 45 + (45 * vat)
            print(price_all,"THB")
            money = int(input("Enter Money: "))
            result = money - price_all
            print( '%.2f'%result, "THB")
        elif userSelected2 ==2:
            price_all = 145 + (145 * vat)
            print(price_all, "THB")
            money = (input("Enter Money: "))
            result = money - price_all
            print( '%.2f'%result, "THB")
        elif userSelected2 == 3:
            price_all = 55 + (55 * vat)
            print(price_all, "THB")
            money = (input("Enter Money: "))
            result = money - price_all
            print( '%.2f'%result, "THB")
else:
    print("เลิกปลอมนะคะลูก")