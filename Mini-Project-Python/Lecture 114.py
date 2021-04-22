from forex_python.bitcoin import BtcConverter
import datetime
import matplotlib.pyplot as plt


# เเสดงฟีเจอร์ของโปรเเกรม

class Menu_Program:

    def Show_Menu(self):
        print("-" * 60)
        print("This is Program Trade Cryptocurrency And BTC Chart Program")
        print("-" * 60)
        print("1. BITCOINS CONVERTER TO CERREBCY PROGRAM : ")
        print("2. BTC CHART CHANGE (THB) PROGRAM")
        print("3. CONVERT BITCOINS TO AMOUNT CURRENCY  PREVIOUS DATE ")


# ฟังชั่นเลือก Menu
class Select_Menu():

    def Menu_Selects(self, Input_User):

        self.User_Input = Input_User

        #คำนวณการเเรกเปลี่ยนเหรียญ Bitcoins
        if Input_User == 1:
            def Convert_btc_to_cur():
                print("-" * 40)
                print("BITCOINS Converter TO Cerrency PROGRAM")

                Input_BitCoins: float = float(input("Input Bitcoins : "))
                Input_Cerrency: str = input("Please Input Cerrency : ")

                btc = BtcConverter()
                result_price = btc.convert_btc_to_cur(Input_BitCoins, Input_Cerrency.upper())

                print(result_price,Input_Cerrency.upper())
                print("-" * 40)

            Convert_btc_to_cur()

        #เเสดงเหรียญ BTC วันที่เท่าไหร่
        if Input_User == 2:
            def Date_BTC():
                print("-" * 40)
                print("BTC Chart Change (THB) PROGRAM")
                print("โปรแกรมจะแสดงผลตั้งแต่วันที่เลือกไม่เกิน 3 ปี")
                print("กรุณาเลือกก่อนวันที่ 6 มิถุนายน 2013")
                print("Input start date : (ex. 2013 6 24)")
                start_date_year = int(input("Input year: "))
                start_date_month = int(input("Input month: "))
                start_date_day = int(input("Input day: "))

                btc = BtcConverter()

                start_date = datetime.date(start_date_year, start_date_month, start_date_day)
                end_date = datetime.date(start_date_year + 3, start_date_month, start_date_day)
                result_price_list = btc.get_previous_price_list("THB", start_date, end_date)

                date_result = result_price_list.keys()
                rate_result = result_price_list.values()

                plt.title("BTC Chart Change PROGRAM")
                plt.plot(date_result, rate_result)
                plt.xlabel("Date")
                plt.ylabel("BTC / THB Rate")
                plt.show()

            Date_BTC()

        #เลือกการเเลกเปลี่ยนวันก่อนหน้านั้น
        if Input_User == 3:
            def previous_date():
                print("-" * 60)
                print("CONVERT BITCOINS TO AMOUNT CURRENCY  PREVIOUS DATE")
                print("Input start date : (ex. 2013 6 24)")
                start_date_year = int(input("Input year: "))
                start_date_month = int(input("Input month: "))
                start_date_day = int(input("Input day: "))

                Input_BitCoins = float(input("Input Bitcoins : "))
                Input_Cerrency = input("Please Input Cerrency : ")

                btc = BtcConverter()

                set_date = datetime.datetime(start_date_year, start_date_month, start_date_day)
                btc_convert = btc.convert_btc_to_cur_on(Input_BitCoins,Input_Cerrency,set_date)

                print("%.5f"%btc_convert,Input_Cerrency.upper())
                print("-" * 40)

            previous_date()


Menu_Programs = Menu_Program()
Menu_Programs.Show_Menu()

Select_MenuS = Select_Menu()
Select_MenuS.Menu_Selects(int(input("ENTER NUMBER : ")))
