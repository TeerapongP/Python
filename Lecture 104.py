class Customer:
    Name_Customer = ""
    Last_Name_Customer = ""
    Age_Customer = 0

    def Add_Name_Me(self):
        Customer_Values.Name_Customer = input("ENTER NAME : ")
        print("Name IS :",self.Name_Customer)
       

    def Add_Name_BMK_Member(self):
        Customer_Values.Name_Customer = input("ENTER NAME : ")
        print("Member IS :",self.Name_Customer)
        

Customer_Values = Customer()
Customer_Values.Add_Name_Me()
Customer_Values.Add_Name_BMK_Member()
