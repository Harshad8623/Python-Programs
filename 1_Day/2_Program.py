# Programs for Calculator

# method 1 : using if else statements
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Invalid operator")
print("Result:", result)


# method 2 : using functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:   
    print("Invalid operator")
print("Result:", result)




# method 3 : using eval function
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")
expression = num1 + operator + num2
try:
    result = eval(expression)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("Error:", e)




# method 4 : using a dictionary to map operators to functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None 
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator in operations:
    result = operations[operator](num1, num2)
    print("Result:", result)
else:
    print("Invalid operator")




# method 5 : using a while loop to allow multiple calculations until the user decides to exit
def add(a, b):
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}   
while True: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ")
    if operator == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    elif operator in operations:
        result = operations[operator](num1, num2)
        print("Result:", result)
    else:
        print("Invalid operator")



# method 6 : using a class to create a calculator object
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero is not allowed.")
            return None
calculator = Calculator()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = calculator.add(num1, num2)
elif operator == "-":
    result = calculator.subtract(num1, num2)
elif operator == "*":   
    result = calculator.multiply(num1, num2)
elif operator == "/":
    result = calculator.divide(num1, num2)
else:
    print("Invalid operator")
print("Result:", result)



# method 7 : using a match case
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    case _:
        print("Invalid operator")
print("Result:", result)





# method 8 : using a lambda function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")   
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: Division by zero is not allowed."
}
if operator in operations:
    result = operations[operator](num1, num2)
    print("Result:", result)
else:
    print("Invalid operator")
