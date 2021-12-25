import csv

from datetime import date

#ทำการเขียนไฟล์ Csv
with open('buffet.csv', 'w') as write:
    writer = csv.writer(write)
    writer.writerow(["Day","Time","Number of child","Number of adult", "Total"])

    # ทำการดึงค่าเวลา
    fullDate = date.today()
    day = fullDate.strftime("%d/%m/%y")
    time = fullDate.strftime('%H:%M')
    data = []

    con = ''

    #ลูป
    while True: #
        con = str(input('ต้องการทำรายการใช่หรือไม่? (y/n) : ').lower())
        if con == 'y':
           child_input = int (input ("จงใส่จำนวนของเด็ก : "))
           adult_input = int(input ("จงใส่จำนวนผู้ใหญ่ : "))

           
           child_many = child_input * 158
           adult_many = adult_input * 199
           total = child_many + adult_many
           
           print("ราคาผู้ใหญ่", child_many, "baht")
           print("ราคาเด็ก", adult_many, "baht")
           print("ราคาทั้งหมด", total, "baht")
           
           #ทำการเพิ่มค่า Key เเละ Values เข้าไปใน Array ที่มีชื่อว่า data
           data.append({day,time,child_input, adult_input,total})
        else:
            #ทำการเขียนไฟล์
            writer.writerow(data)
            break
