# Sum of digits in the number
def sum_of_digits(n):
    total = 0          # avoid using sum variable name as it is a built-in function in python
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
print(sum_of_digits(1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(1)
# Currently handling non negative integers only. We can also handle negative integers by taking absolute value of n at the beginning of the function.

# Solution :
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
print(sum_of_digits(-1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(1)


# Another approach : Using String Conversion
def sum_of_digits(n):
    n = abs(n)
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(-1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(n) because of string conversion and list comprehension.  

# Another approach : Using Recursion
def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(-1234))
# Time Complexity : O(log10(n))
# Space Complexity : O(log10(n)) because of recursive call stack.