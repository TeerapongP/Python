import math

time = int(input("Input time parking (minute) : " )) #ทำการรับค่าเวลาจาก User
print("-" * 60)

hr = int(time / 60)  #ทำการคำนวนเวลาจาก นาที เป็น ชั่วโมง
minutes = time % 60 #ทำการหารเอาเศษออกมาเเสดง
print("\t Time : ",hr,"Hour",minutes,"minutes")

print("-" * 60)
result = (hr*30)+(minutes*50)/100
print("Total price = ",'%.2f' %result,"Bath")