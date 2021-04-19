name = input("ENTER NAME : ")
lastName = input("ENTER LAST NAME : ")

print("HELLO !! %s  %s " %(name.capitalize(),lastName.capitalize()))

text = "POP"
textFormatted = "Wellcome %s %s "%(name.capitalize(),lastName.capitalize())
print(textFormatted.center(22,"-"))
print("จำนวนตัวอักษรของชื่อ",len(name),"ตัว","จำนวนตัวอักษรของนามสกุล",len(lastName),"ตัว")