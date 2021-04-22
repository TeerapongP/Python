User_Input  = int(input("Enter Round: "))
sum = 0
for i in range(User_Input ):
    input_number = int(input("Number "+str(i+1)+" : "))
    sum += input_number
print(sum)

