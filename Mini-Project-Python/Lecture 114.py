from forex_python.bitcoin import BtcConverter
import datetime
import matplotlib.pyplot as plt

#เเสดงฟีเจอร์ของโปรเเกรม
class Menu_Program:

    def Show_Menu(self):
        print("-"*60)
        print("This is Program Trade Cryptocurrency And BTC Chart Program")
        print("-"*60)
        print("1. Trade Cryptocurrency : ")
        print("2. BTC Chart Change (THB) PROGRAM")
class Select_Menu(Menu_Program):
    
    User_Input = ""

    def Menu_Selects(self,Input_User):
        self.User_Input = Input_User
        if(Input_User  == 2 ):
            def Show_BTC():
                print("-"*40)
                print("BTC Chart Change (THB) PROGRAM")
                print("โปรแกรมจะแสดงผลตั้งแต่วันที่เลือกไม่เกิน 2 ปี")
                print("กรุณาเลือกก่อนวันที่ 6 มิถุนายน 2013")
                print("Input start date : (ex. 2013 6 24)")
                start_date_year = int(input("Input year: "))
                start_date_month = int(input("Input month: "))
                start_date_day = int(input("Input day: "))

                btc = BtcConverter()
                start_date = datetime.date(start_date_year, start_date_month, start_date_day)
                end_date = datetime.date(start_date_year + 2, start_date_month, start_date_day)
                result_price_list = btc.get_previous_price_list("THB", start_date, end_date)

                date_result = result_price_list.keys()
                rate_result = result_price_list.values()

                plt.title("BTC Chart Change PROGRAM")
                plt.plot(date_result, rate_result)
                plt.xlabel("Date")
                plt.ylabel("BTC / THB Rate")
                plt.show()


        Show_BTC()

Menu_Programs = Menu_Program()
Menu_Programs.Show_Menu()

Select_MenuS = Select_Menu()
Select_MenuS.Menu_Selects(int(input("ENTER NUMBER : ")))












