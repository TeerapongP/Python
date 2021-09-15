class User:
    department_input =input("Department Name : ")
    employee_input =input("Employee #1 Name : ")
    salary_input = int(input("Salary : "))
    choice_input = ''
    vat_cal=0
    tax_cal=0
    total = 0
    total_sum = 0
    def Calculate(self):
        
        if(self.salary_input>=30000):

            self.vat_cal = self.salary_input-(self.salary_input*(3/100))   
            self.tax_cal = self.salary_input -self.vat_cal
            
        elif(self.salary_input>=15000):    
            self.vat_cal = self.salary_input-(self.salary_input*(1.5/100))    
            self.tax_cal = self.salary_input -self.vat_cal

        self.total = self.salary_input - self.tax_cal
        self.total_sum = self.total_sum + self.salary_input

    def Loop_choice(self):
        i = 1
        print("Employee Name :",self.employee_input,"Salary :",self.salary_input,"Bath","Tax :",self.tax_cal,"Bath","Total :",self.total,"Bath")    
        print("Do you have any Employee in this department [Y/N] : ")
        self.choice_input = str(input().upper())

        while(self.choice_input != "Y" and self.choice_input != "N"):
            print("Incorect answes , Try agains")
            print("Do you have any Employee in this department [Y/N] : ")
            self.choice_input = str(input().upper())

        while(self.choice_input == "Y"):
           
            self.employee_input =input("Employee #"+ str(i+1)+" Name : ")
            self.salary_input = int(input("Salary : "))
            self.total_sum = self.total_sum + self.salary_input

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


