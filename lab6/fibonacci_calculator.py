import calculator
def main():
    print("Choose an operation:")
    print("1. Generate Fibonacci series")
    print("2. Calculate factorial")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        n = int(input("Enter the number to generate Fibonacci series up to: "))
        fib_series = calculator.fibonacci(n)
        print("Fibonacci series:", fib_series)
    elif choice == '2':
        num = int(input("Enter the number to calculate factorial: "))
        result = calculator.factorial(num)
        print(f"The factorial of {num} is {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()