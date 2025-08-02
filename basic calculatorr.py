
# basic calculator for= +,-,*,/

def calculator():
    print("Welcome to My Calculator!")
    print("Operations:")
    print(" +  --> Addition")
    print(" -  --> Subtraction")
    print(" *  --> Multiplication")
    print(" /  --> Division")

    op = input("Enter an operator (+, -, *, /): ")

    if op not in ['+', '-', '*', '/']:
        print("Invalid operator. Please try again.")
        return

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Numbers only!")
        return

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b

    print(f"The result of {a} {op} {b} is: {result}")

# Start the calculator
calculator()
