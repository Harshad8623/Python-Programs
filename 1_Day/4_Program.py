print("Hello World")
print(100)
print(3.14)
print(True)
print(None)
print("This is a string.")
print('Another string example.')
print("Special characters: \n\t\" ' \\")
print("Unicode characters: 😊, ñ, ü, 中")
print("Escape sequences: Line1\nLine2\tTabbed")
print("Raw string example: C:\\Users\\Name")
print("Raw string example: C:\ Users\ Name")   # THIS WORKS BUT THE FOLLOWING WILL NOT WORK
# print("Raw string example: C:\Users\Name")   # THIS WILL CAUSE AN ERROR DUE TO UNRECOGNIZED ESCAPE SEQUENCE
print("Raw string example: C:\\ Users\\ Name") # THIS WORKS PRINT ONLY ONE / NOT TWO //
str1 = """
"hejejj" 'rrwr'
"""
print(str1)


print(r"Raw string with escape sequences: \n \t \\") # THIS WILL PRINT AS IT IS WITHOUT INTERPRETING \n \t \\
print("Multiline string example:\nThis is line one.\nThis is line two.")
print("""This is a multiline string using triple quotes.
It can span multiple lines.""")
print('''Another multiline string example.
Using single quotes.''')
print("String concatenation: " + "Hello, " + "World!")
print("String repetition: " + "Ha! " * 3)
print("Formatted string: {} + {} = {}".format(2, 3, 2 + 3))
print(f"Formatted string with f-string: {5} * {4} = {5 * 4}")
print("Boolean values: ", True, False)  # Comment about boolean values
print("NoneType example: ", None)  # Comment about NoneType example
print("End of examples.")



print(10 + 20)
print(5 * 3)
print('5'* 3) # '555'
print(10 / 3)   # 3.3333333333333335
print(2 ** 3)
print(10 % 3)
print(15 - 7)
print(10 // 3)
print("(10 + 5)" * 2)
print(3.5 + 2.1)
print(7.2 * 3.0)
print(9.0 / 2.0)
print(4.0 ** 2)
print(8.5 % 3.0)
print(12.0 - 5.5)
print(14.0 // 4.0)
print("Mathematical operations completed.")
print("Thank you for using the math operations script.")

print(True and False)
print(True or False)
print(not True)
print(not False)


print("Sum is:", 10 + 20)
print(10 + 20, "is the sum.")
print("A =", 10, "B =", 20)
print("Calculating sum:", 10 + 20)
print("Result:", 10 + 20)
print("Final sum is", 10 + 20)
print("Addition:", 5 + 3)
print("Multiplication:", 4 * 2)
print("Division:", 20 / 4)
print("Subtraction:", 15 - 5)
print("Exponentiation:", 2 ** 3)
print("Modulus:", 10 % 3)
print("Floor Division:", 10 // 3)
print("All operations completed.")


print("Sum is:", 10 + 20)
print(10 + 20, "is the sum.")
print("A =", 10, "B =", 20)
print("Calculating sum:", 10 + 20)
print("Result:", 10 + 20)


print("Hello" + "World")
print("Age: " + str(20))
print("Marks: " + str(95.5))
print("Is Student: " + str(True))
print("Value: " + str(None))
print("Concatenation completed.")
print("Thank you for using the concatenation script.")


print("Hello","World")
print("Sum is", 10+20)
print("Name:","Harshad","Roll:", 21)
print("Values:", 10, 3.14, True, None)
print("All print statements executed.")
print("Thank you for using the print script.")
print("Hello\tWorld\nWelcome to Python!")


print("12+56", "Hello" + 'World', 12+56)
print("12+56", "Hello" + "World", 12+56)
print("12+56", 'Hello' + 'World', 12+56)
print("12+56", 'Hello' + "World", 12+56)
print("All combinations executed.")



print("Hello" * 3)
print("Hello-" * 5)
print("*" * 10)
print("Repeat completed.")



print("Hello\nWorld")
print("Line1\nLine2\nLine3")
print("Tab\tSeparated\tValues")
print("Escape sequences demonstrated.")
print("Hello\tWorld")
print("Hello\\World")
print('He said, "Hello World!"')
print("It's a beautiful day!")
print("""
Hello
This is a
Multi-line string
""")
print(r"C:\Users\Harshad\Desktop")
print(r"Hello\nWorld")   # \n NOT treated as newline
print("Escape sequences examples completed.")



print(f"Sum of 10 and 20 is {10 + 20}")
print(f"Multiplication of 5 and 4 is {5 * 4}")
print(f"Division of 20 by 4 is {20 / 4}")
print(f"Exponentiation of 2 to the power 3 is {2 ** 3}")
print(f"Subtraction of 15 and 5 is {15 - 5}")
print("Formatted strings examples completed.")



name = "Harshad"
age = 20
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old".format(name, age))
print("Personalized greeting using format completed.")



# print("Age: " + 20)   # ❌ TypeError
# print("Marks: " + 95.5)  # ❌ TypeError
# print("Is Student: " + True)  # ❌ TypeError
# print("Value: " + None)  # ❌ TypeError
# print("Type errors demonstrated.")

print("Age:", 20)
print("Marks:", 95.5)
print("Is Student:", True)
print("Value:", None)
print("Type errors resolved.")


print("Age: " + str(20))
print("Marks: " + str(95.5))
print("Is Student: " + str(True))
print("Value: " + str(None))
print("Type errors resolved.")



print("Hello", end=" ")
print("World")
print("Welcome", end="***")
print("to Python!") 


print("2025", "11", "18", sep="-")
print("2025", "11", "18", sep="/")
print("2025", "11", "18", sep=".")
print("End and sep parameters demonstrated.")

print("Hello", "world", sep="-", end="***")  # CUSTOM SEPARATOR AND ENDING
print("Welcome to Python!")

print("Hello", "world", sep="-")  # CUSTOM SEPARATOR
print("Welcome to Python!")

print("Hello", "world", end="-")  # CUSTOM ENDING 
print("Welcome to Python!")

str6 = " Hello,    World!"
str9 = "   " # String with only spaces
print(str6.isspace()) # False
print(str9.isspace()) # True