import math

time = int(input("Input time parking (miinute) : " ))
print("-" * 60)

hr = int(time *0.016667) #ทำการคำนวน แปลง นาที เป็น ชั่วโมง
minutes = math.floor((((time/3600)*60)*10)) 
print("\t Time : ",hr,"Hour",minutes,"minutes")

print("-" * 60)
print("Total price = ",math.ceil((hr*30)+((minutes*50)/100)),"BATH")