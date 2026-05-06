'''
What is an Escape Sequence?
An escape sequence is a special combination of characters that starts with a backslash \ and is used to represent characters that are difficult or impossible to type directly in a string.

In simple words:
Escape sequences tell Python “don’t take this character literally, treat it specially.
'''


"""
        Important Escape Sequences

Escape Sequence	              Meaning
    \n	                    New line
    \t	                    Horizontal tab
    \'	                    Single quote
    \"	                    Double quote
    \\	                    Backslash
    \r	                    Carriage return
    \b	                    Backspace
    \f	                    Form feed
    \v	                    Vertical tab
    \0	                    Null character
"""

print("Hello\nWorld")
print("Hello\tWorld")
print('It\'s a beautiful day')
print("She said, \"Hello!\"")
print("This is a backslash: \\")
print("Hello World!\rPython")  # Cursor moves to start, overwrites text.
print("Hello\bWorld")   
print("Hello\fWorld")
print("Hello\vWorld")
print("Hello\fWorld") # Form feed may not show visible effect in some environments.
print("Hello\0World")  # Null character may not show visible effect.
print("\u2764") # Unicode for a heart symbol
print("\u03B1") # Unicode for Greek letter alpha
print("\U0001F600") # Unicode for grinning face emoji
print("\U0001F680")  # 🚀
print("\U0001F4BB")  # 💻



import time
for i in "|/-\\":
    print("\r" + i, end="")
    time.sleep(0.6)