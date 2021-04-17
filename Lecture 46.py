multiplication_table = int(input("สูตรคูณเเม่ไรดีใส่มา ? : "))
for i in range(1,12):
    for j in range(12):
        print(i, "x", j + 1, "=", multiplication_table * (j + 1))