import time

welcome_message = '''
Dear User,
    Welcome to the simple calculator! This calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, division and other basic operations. You can enter two numbers and an operator to get the result. The calculator will continue to run until you decide to exit. We hope you find this calculator useful and easy to use!'''
print(welcome_message)
time.sleep(2)
while True:
    calculator_choice = input("Please choose operation (derivative, addition, subtraction, multiplication, division): ").lower().strip()

    if calculator_choice not in ["derivative", "addition", "subtraction", "multiplication", "division"]:
        print("Error: Invalid operation choice.")
        continue

    if calculator_choice == "derivative":
        print("\nChoose a function:")
        print("1. f(x) = x**2")
        print("2. f(x) = x**3")
        print("3. f(x) = x**2 + 3x + 1")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "4":
            print("Goodbye!")
            break
        x = float(input("Enter the value of x: "))
        h = 0.00001
        if choice == "1":
            derivative = ((x + h) ** 2 - x ** 2) / h
        elif choice == "2":
            derivative = ((x + h) ** 3 - x ** 3) / h
        elif choice == "3":
            derivative = (((x + h) ** 2 + 3 * (x + h) + 1) - (x ** 2 + 3 * x + 1)) / h
        else:
            print("Error: Invalid derivative choice.")
            continue

        print("The approximate derivative at x =", x, "is:", derivative)
        continue

    try:
        num1 = float(input("Enter the first number here: "))
        num2 = float(input("Enter the second number here: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    if calculator_choice == "addition":
        result = num1 + num2
        op = "+"
    elif calculator_choice == "subtraction":
        result = num1 - num2
        op = "-"
    elif calculator_choice == "multiplication":
        result = num1 * num2
        op = "*"
    elif calculator_choice == "division":
        if num2 == 0:
            print("Error: Division by zero.")
            continue
        result = num1 / num2
        op = "/"

    print("The result of", num1, op, num2, "is:", result)
