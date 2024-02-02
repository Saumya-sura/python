num = int(input("Enter the number of rows: "))

for row in range(num, 0, -1):
    for column in range(num-row):
        print("   ", end="")
    for column in range(row, 0, -1):
        print(column, end="  ")
    print()