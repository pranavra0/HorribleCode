
def calculator():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
        
        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)
        else:
            print("Error: Invalid operation")
    except ValueError:
        print("Error: Invalid input")

calculator()

