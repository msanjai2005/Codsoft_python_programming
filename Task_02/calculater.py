print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    operation = input("Enter choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == '1':
            result = number1 + number2
            print(f"The result is: {result}")

        elif operation == '2':
            result = number1 - number2
            print(f"The result is: {result}")

        elif operation == '3':
            result = number1 * number2
            print(f"The result is: {result}")

        elif operation == '4':
            if number2 == 0:
                print("Error! Division by zero.")
            else:
                result = number1 / number2
                print(f"The result is: {result}")
    else:
        print("Invalid Input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
