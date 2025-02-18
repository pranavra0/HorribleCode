def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            b = float(input("Enter second number: "))
        
            if op in operations:
                print("Result:", operations[op](a, b))
            else:
                print("Error: Invalid operation")
        except ValueError:
            print("Error: Invalid input")
            continue
        else:
            break

calculator()