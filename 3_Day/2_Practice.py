# Count the number of digits in the number

# Method 1 : Using Mathematical Operations
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
print(count_digits(1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(1)   

# Method 2 : Using String Conversion
def count_digits(n):
    n = abs(n)
    return len(str(n))
print(count_digits(1234))
# Time Complexity : O(n) because of string conversion.
# Space Complexity : O(n) because of string conversion.

# Method 3 : Using log10 function from math module
import math
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1
print(count_digits(1234))   
# Time Complexity : O(1)    
# Space Complexity : O(1)   
# why this works : log10(n) gives us the number of digits in the number minus 1. So we need to add 1 to get the actual number of digits. We also need to handle the case when n is 0 because log10(0) is undefined. In that case, we return 1 because 0 has 1 digit.



# Method 4 : Using Recursion
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(log10(n)) because of recursive call stack.
# why this works : We keep dividing the number by 10 until we reach a single digit. Each time we divide, we count 1 digit. When we reach a single digit, we return 1 because it has 1 digit. The total count is the number of times we divided plus 1 for the last single digit. We also need to handle the case when n is 0 because it has 1 digit.
