num = int(input("enter the cost: "))
if num>100000:
    print("15% tax would be applied")
elif 50000<num<=100000:
    print("10% tax would be applied")
else:
    print("5% tax would be applied")