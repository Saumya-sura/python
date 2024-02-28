
import cal
def main():
    print("Choose an operation:")
    print("1. Calculate sin")
    print("2. Calculate cos")
    print("3. Calculate square root")
    print("4. Calculate power")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2']:
        value = float(input("Enter the value: "))
        if choice == '1':
            result = cal.calculate_sin(value)
            print(f"The sin value of {value} is {result}")
        else:
            result = cal.calculate_cos(value)
            print(f"The cos value of {value} is {result}")
    elif choice == '3':
        value = float(input("Enter the value: "))
        result = cal.calculate_sqrt(value)
        print(f"The square root of {value} is {result}")
    elif choice == '4':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = cal.calculate_power(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()