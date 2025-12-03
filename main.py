from src.calculator import add, subtract, multiply, divide

print("Welcome to the Simple CLI Calculator!")

while True:
    try:
        num1_str = input("Enter the first number (or 'q' to quit): ").lower().strip()
        if num1_str == 'q':
            break
        num1 = float(num1_str)
        operator = input("Enter an operator (+, -, *, /) (or 'q' to quit): ").lower().strip()
        if operator == 'q':
            break
        num2_str = input("Enter the second number (or 'q' to quit): ").lower().strip()
        if num2_str == 'q':
            break
        num2 = float(num2_str)

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n")
    another_calculation = input("Do you want to perform another calculation? (yes/no/q to quit): ").lower().strip()
    if another_calculation != 'yes' and another_calculation != 'q':
        break
    elif another_calculation == 'q':
        break
