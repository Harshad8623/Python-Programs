# Multiplication table printer program
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Another way to print multiplication table using function
def print_multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(number)



# Another way to print multiplication table using list comprehension
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
for line in multiplication_table:
    print(line)


# Another way to print multiplication table using while loop
number = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1




# Another way to print multiplication table using recursion
def print_multiplication_table_recursive(n, i=1):
    if i > 10:
        return
    print(n, "x", i, "=", n * i)
    print_multiplication_table_recursive(n, i + 1)
number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table_recursive(number)



# Another way to print multiplication table using lambda function
print_multiplication_table_lambda = lambda n: [print(f"{n} x {i} = {n * i}") for i in range(1, 11)]
number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table_lambda(number)



# Another way to print multiplication table using map function
def multiplication_line(n, i):
    return f"{n} x {i} = {n * i}"
number = int(input("Enter a number to print its multiplication table: "))
lines = map(lambda i: multiplication_line(number, i), range(1, 11))
for line in lines:
    print(line)


# Another way to print multiplication table using a class
class MultiplicationTable:
    def __init__(self, number):
        self.number = number
    def print_table(self):
        for i in range(1, 11):
            print(self.number, "x", i, "=", self.number * i)
number = int(input("Enter a number to print its multiplication table: "))
table = MultiplicationTable(number)
table.print_table()



# Another way to print multiplication table using a dictionary to store the results
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table_dict = {i: number * i for i in range(1, 11)}
for i, result in multiplication_table_dict.items():
    print(f"{number} x {i} = {result}")


# Another way to print multiplication table using a list of tuples to store the results
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table_list = [(i, number * i) for i in range(1, 11)]
for i, result in multiplication_table_list:
    print(f"{number} x {i} = {result}")


# Another way to  print multiplication table using a generator expression
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table_generator = (f"{number} x {i} = {number * i}" for i in range(1, 11))
for line in multiplication_table_generator:
    print(line)


# Another way to print multiplication table using a while loop to allow multiple tables until the user decides to exit
while True:
    number = int(input("Enter a number to print its multiplication table (or -1 to exit): "))
    if number == -1:
        break
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)