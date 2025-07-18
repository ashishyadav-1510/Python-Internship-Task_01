def get_number(prompt):
    """Prompt the user for a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operator():
    """Prompt the user to choose a valid operator."""
    valid_operators = ['+', '-', '*', '/', '%']
    while True:
        op = input("Enter an operator (+, -, *, /, %): ").strip()
        if op in valid_operators:
            return op
        else:
            print("Invalid operator! Please choose from +, -, *, /, %.")

def calculate(num1, num2, operator):
    """Perform the calculation based on the operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Modulus by zero!"
        return num1 % num2

def main():
    print("=== Basic Calculator ===\n")

    num1 = get_number("Enter the first number: ")
    operator = get_operator()
    num2 = get_number("Enter the second number: ")

    result = calculate(num1, num2, operator)
    print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
