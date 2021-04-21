
def login():
    username = input("ENTER USERNAME :")
    passw = input("ENTER PASSWORD :")
    if username == "admin" and passw == "1234":
        return True
    else:
        return False


def ShowMenu():
    print("------MangaBook------")
    print("1. vat Calculate")
    print("2. Price Calculate")


def MenuSelect():
    userSelected = int(input(">>"))
    return userSelected


def vatCalculate(priceCalculate):
    vat = 7 / 100
    result = priceCalculate + (priceCalculate * vat)
    return result


def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()
ShowMenu()
MenuSelect()


