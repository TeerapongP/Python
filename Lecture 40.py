# if False:
#     print("Hello Welcome")
#     if True:
#         print("Yo ! Mister A")
username = input("ENTER USERNAME :")
passw = input("ENTER PASSWORD :")

if username == "admin" and passw == "1234":
    print("Done !!")
    print("------MangaBook------")
    print("1. vat Calculate")
    print("2. Price Calculate")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Enter Price: "))
        vat = 7 / 100
        result = price + (price * vat)
        print(result,"THB")
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2,"THB")
else:
    print("เลิกปลอมนะขอร้อง")