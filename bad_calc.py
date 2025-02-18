
def calculator():
        a = float(input("First number:"))
        b = float(input("Second number:"))
        op = input("Enter operation (+, -, *, /): ")
        
        
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
            print("Not sure what happened man")

calculator()

