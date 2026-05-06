# String in detailed

# A string is a sequence of characters used to store text.
# Strings are immutable → once created, they cannot be changed.


# Single quotes
str1 = 'Harshad'
# Double quotes
str2 = "Dhuppe"
# Triple quotes (multiline strings / docstrings)
str3 = '''This is a
multi-line string.'''
str4 = """Another
multi-line string example.  """


name = "Harshad"
a = ""       # Empty string
b = ' '      # String with a single space
c = 'Hello, World!'  # String with text



# Accessing Characters (Indexing)
print(name)
print(name[0])  # First character
print(name[-1]) # Last character
print(name[0:5]) # Substring from index 0 to 4
print(name[:5])  # Substring from start to index 4
print(name[5:])  # Substring from index 5 to end
print(name[-5:]) # Last 5 characters
print(name[::-1]) # Reverse string
print(name.upper()) # Uppercase
print(name.lower()) # Lowercase
print(name.capitalize()) # Capitalize first letter
print(name * 2) # Repeat string
print(name + " Dhuppe") # Concatenate strings
print(len(name)) # Length of string
print("String operations completed.")


# Strings are Immutable ⚠️
s = "Hello"
# s[0] = 'h' ❌ ERROR - Strings are immutable
# To modify a string, create a new one
s = 'h' + s[1:]  # Create a new string
print("Modified string:", s)



# String Concatenation & Repetition
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World
print(a * 3)        # HelloHelloHello
print("Concatenation and repetition done.")




#  Raw Strings (r"") - Used to ignore escape sequences (paths, regex).
path = r"C:\Users\Harshad\Docs"
print(path)
print("Raw string example completed.")




# Formatted Strings (f-strings)
name = "Harshad"
age = 20
print(f"My name is {name} and I am {age} years old")
print(f"Sum = {10 + 20}")
print("Formatted string example completed.")



# Split & Join
sentence = "Hello World     from Python"
words = sentence.split(" ")  # Split by space
print(words)
joined = "-".join(words)     # Join with hyphen
joined = ' '.join(words)     # Join with space

print(joined)
print("Split and join example completed.")




# Iterating Through Strings
name = "Harshad"
for char in name:
    print(char)
print("String iteration completed.")


for character in name:
    print(character.upper())

for character in name:
    print(character.lower())

for character in name:
    print(character.capitalize())

for character in name:
    print(character * 3)  # Repeat each character 3 times

for character in name:
    print(character + "-")  # Concatenate each character with a hyphen

for character in name:
    print(f"Character: {character}")  # Formatted string output

for character in name:
    print(f"{character} ASCII: {ord(character)}")  # Print character with its ASCII value

for character in name:
    print(f"Index of {character}: {name.index(character)}")  # Print character with its index

for character in name:
    print(f"{character} in uppercase: {character.upper()}")  # Print character in uppercase





if "Harshad" in name:
    print("Found 'Harshad' in the name.")
else:
    print("'Harshad' not found in the name.")



print(name.replace("Harshad", "Hars")) # Replace substring
print(name.split("s")) # Split string
print(" ".join(["Hello", "World"])) # Join strings  
print("String manipulations completed.")



# Syntax of String Slicing in Python
# substring = s[start : end : step]

# Parameters:

# s: The original string.
# start (optional): Starting index (inclusive). Defaults to 0 if omitted.
# end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
# step (optional): Interval between indices. A positive value slices from left to right, while a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).
# Return Type: The result of a slicing operation is always a string (str type) that contains a subset of the characters from the original string.


example="hello"
print(example.count('l')) # Count occurrences of 'l'
example.find('o') # Find index of 'o'
example.index('e') # Find index of 'e'
example.startswith('h') # Check if starts with 'h'
example.endswith('o') # Check if ends with 'o'
example.isalpha() # Check if all characters are alphabetic
example.isdigit() # Check if all characters are digits
example.isspace() # Check if all characters are whitespace
example.strip() # Remove leading/trailing whitespace
example.lstrip() # Remove leading whitespace
example.rstrip() # Remove trailing whitespace
example.center(11) # Center string in a field of width 11
example.zfill(10) # Pad string with zeros to width 10
example.swapcase() # Swap case of characters
example.title() # Title case
example.partition('l') # Partition string at first 'l'
example.rpartition('l') # Partition string at last 'l'
example.splitlines() # Split string at line breaks
example.encode() # Encode string to bytes




s = "abcdefghijklmno"
print(s[-4:1]) # Empty string, as -4 is after 1
print(s[:-3]) # 'abcdefghijklm'
print(s[2:-2]) # 'cdefghijklmn'
print(s[-5:-2]) # 'klm'
print(s[1:-1]) # 'bcdefghijklmn'
print(s[-8:-1:2]) # 'hjl'
print(s[-1:-8:-2]) # 'omkig'
print(s[::-1]) # 'onmlkjihgfedcba'
print(s[-3::-1]) # 'mlkjihgfedcba'
print(s[-1::-1]) # 'onmlkjihgfedcba'
print(s[::]) # 'abcdefghijklmno'
print(s[::2]) # 'acegikmo'
print(s[1::2]) # 'bdfhjln'
print(s[::3]) # 'adgjm'
print("String slicing examples completed.\n\n")


str1 = "  Hello World  !!  "
print(str1)
print(str1.strip()) # Remove leading/trailing whitespace
print(str1.lstrip()) # Remove leading whitespace
print(str1.rstrip()) # Remove trailing whitespac e
print(str1.center(30)) # Center string in a field of width 30
print(str1.zfill(30)) # Pad string with zeros to width 30
print(str1.swapcase()) # Swap case of characters
print(str1.title()) # Title case
print(str1.partition('W')) # Partition string at first 'W'
print(str1.rpartition('o')) # Partition string at last 'o'
print(str1.splitlines()) # Split string at line breaks
print(str1.encode()) # Encode string to bytes
print("Additional string methods examples completed.")


str2 = "Silver Spoon"
print(str2.count('o')) # Count occurrences of 'o'
print(str2.find('S')) # Find index of 'S'
print(str2.index('p')) # Find index of 'p'
print(str2.startswith('S')) # Check if starts with 'S'
print(str2.endswith('n')) # Check if ends with 'n'
print(str2.isalpha()) # Check if all characters are alphabetic
print(str2.isdigit()) # Check if all characters are digits
print(str2.isspace()) # Check if all characters are whitespace
print(str2.split(' ')) # Split string by space
print(str2.split('r')) # Split string by 'r'
print(str2.split('i')) # Split string by 'i'
print("SilsiI".split(' ')) # Split string by space
print("SilsiI".split('I')) # Split string by 'I'
print("SilsiI".split('s')) # Split string by 's'
print("SilsiI".split('S')) # Split string by 'S'

str3 = "sususususu"
print(str3.split("su")) # Split string by 'su'
print(str3.split("sus")) # Split string by 'sus'
print(str3.split('u')) # Split string by 'u'
print(str3.split('s')) # Split string by 's'


str4 = "  Leading And Arailing Spaces   "
str5 = str4.capitalize()

str6 = "HeLLo WoRLD"
print(str6.center(50,'*')) # Center string with '*' padding
print(str6.zfill(50)) # Pad string with zeros to width 50
print(str6.swapcase()) # Swap case of characters
print(str6.title()) # Title case
print("Final string methods examples completed.")



str7 = "Data-Science-Is-Fun"
print(str7.partition('-')) # Partition string at first '-'
print(str7.rpartition('-')) # Partition string at last '-'
print("Data-Science-Is-Fun".splitlines()) # Split string at line breaks
print("Data-Science-Is-Fun".encode()) # Encode string to bytes
print("All string method examples completed.")