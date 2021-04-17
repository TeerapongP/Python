multiplication_table = int(input("สูตรคูณเเม่ไรดีใส่มา ? : "))
for i in range(multiplication_table):
    for j in range(12):
        print(i+1, "x", j+1, "=", multiplication_table * (j+1))