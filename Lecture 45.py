input_user = int(input("Enter Round: "))
sum = 0
for i in range(input_user):
    input_number = int(input("Number "+str(i+1)+" : "))
    sum += input_number
print(sum)

