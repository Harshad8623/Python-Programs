#--------------------Count the number of digits in the number--------------------


# Method 1 : Using Mathematical Operations
def count_digits1(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
# Time Complexity : O(log10(n))
# Space Complexity : O(1)


# Method 2 : Using String Conversion
def count_digits2(n):
    n = abs(n)
    return len(str(n))
# Time Complexity : O(n) because of string conversion.
# Space Complexity : O(n) because of string conversion.



# Method 3 : Using log10 function from math module
import math
def count_digits3(n):
    n = abs(n)
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1 # why this works : log10(n) gives us the number of digits in the number minus 1. So we need to add 1 to get the actual number of digits. We also need to handle the case when n is 0 because log10(0) is undefined. In that case, we return 1 because 0 has 1 digit.
# Time Complexity : O(1)
# Space Complexity : O(1)
# insted of math.floor we can also use int() to get the integer part of the log10(n) because log10(n) will always be a positive number for n > 0. So we can simply return int(math.log10(n)) + 1 to get the number of digits in the number. This will also work for n = 0 because int(math.log10(0)) will raise a ValueError, so we need to handle that case separately by returning 1 when n is 0.


# Method 4 : Using Recursion
def count_digits4(n):
    n = abs(n)
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + count_digits4(n // 10) # why this works : We keep dividing the number by 10 until we reach a single digit. Each time we divide, we count 1 digit. When we reach a single digit, we return 1 because it has 1 digit. The total count is the number of times we divided plus 1 for the last single digit. We also need to handle the case when n is 0 because it has 1 digit.
# Time Complexity : O(log10(n))
# Space Complexity : O(log10(n)) because of recursive call stack.


# Test the function
print(count_digits1(1234))   # Output: 4 Method 1 : Using Mathematical Operations
print(count_digits2(1234))   # Output: 4 Method 2 : Using String Conversion
print(count_digits3(1234))   # Output: 4 Method 3 : Using log10 function
print(count_digits4(1234))   # Output: 4 Method 4 : Using Recursion

# Best for coding rounds : Method 1 and Method 3 because they have O(1) space complexity and O(log10(n)) time complexity. Method 2 is not recommended because of its O(n) space complexity due to string conversion. Method 4 is also not recommended because of its O(log10(n)) space complexity due to recursive call stack.
# Best for interviews : Method 1 and Method 3 because they have O(1) space complexity and O(log10(n)) time complexity. Method 2 is not recommended because of its O(n) space complexity due to string conversion. Method 4 is also not recommended because of its O(log10(n)) space complexity due to recursive call stack. However, if the interviewer specifically asks for a recursive solution, then Method 4 can be used.