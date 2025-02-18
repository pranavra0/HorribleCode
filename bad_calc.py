

def calculator():
        a = input("First number:")
        b = input("Second number:")
        op = input("Enter operation (+, -, *, /): ")
        
        if op == '+':
            print("Result:", float(a) + float(b))
        elif op == '-':
            print("Result:", float(a) - float(b))
        elif op == '*':
            print("Result:", float(a) * float(b))
        elif op == '/':
            if (float(b) == 0):
                print("Error: Division by zero")
            else:
                print("Result:", float(a) / float(b))
        else:
            print("Not sure what happened man")
calculator()

