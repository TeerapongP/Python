class User:
    department_input =input("Department Name : ")
    employee_input =input("Employee #1 Name : ")
    salary_input = int(input("Salary : "))
    choice_input = ''
    total_sum = 0
    
    def Calculate(self):
        tax_cal = 0
        if(self.salary_input>=30000):
            vat_cal = self.salary_input-(self.salary_input*(3/100))   
            
        elif(self.salary_input>=15000):    
            vat_cal = self.salary_input-(self.salary_input*(1.5/100)) 

        tax_cal = self.salary_input - vat_cal
        total = self.salary_input - tax_cal
        self.total_sum = self.total_sum + total

        print("Employee Name :",self.employee_input,"Salary :",self.salary_input,"Bath","Tax :",tax_cal,"Bath","Total :",total,"Bath")

    def Loop_choice(self):
        i = 1
        
        print("Do you have any Employee in this department [Y/N] : ")
        self.choice_input = str(input().upper())

        while(self.choice_input != "Y" and self.choice_input != "N"):
            print("Incorect answes , Try agains")
            print("Do you have any Employee in this department [Y/N] : ")
            self.choice_input = str(input().upper())

        while(self.choice_input == "Y"):
           
            self.employee_input =input("Employee #"+ str(i+1)+" Name : ")
            self.salary_input = int(input("Salary : "))
            self.Calculate()

            print("Do you have any Employee in this department [Y/N] : ")
            self.choice_input = str(input().upper())
            
        print("Department Name :",self.department_input,"Total Employee",str(i+1),"Sum Salary : ",self.total_sum)

        print("Do you have more Department [Y/N] : ")
        self.choice_input = str(input().upper())
        
        while(self.choice_input == "Y"):
            self.department_input =input("Department Name : ")
            self.employee_input =input("Employee #"+ str(i+1)+" Name : ")
            self.salary_input = int(input("Salary : "))

            print("Do you have any Employee in this department [Y/N] : ")
            self.choice_input = str(input().upper())
            
        print("End of Program")        

Display = User()
Display.Calculate()
Display.Loop_choice()


