# Program to check Even or Odd



# First way to check Even or Odd using if-else statement
num = int(input("Enter a Number : "))
if num % 2 == 0:
    print(num, "is an Even Number")
else:
    print(num, "is Odd Number")




# Another way to check Even or Odd using Function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a Number : "))
result = check_even_odd(number)
print(number, "is an", result, "Number")



# Another way to check Even or Odd using Ternary Operator
number = int(input("Enter a Number : "))
result = "Even" if number % 2 == 0 else "Odd"
print(number, "is an", result, "Number")




# Another way to check Even or Odd using Lambda Function
check_even_odd_lambda = lambda num: "Even" if num % 2 == 0 else "Odd"
number = int(input("Enter a Number : "))
result = check_even_odd_lambda(number)
print(number, "is an", result, "Number")
