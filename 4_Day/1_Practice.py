# Program to find factorial of a number

# Best Method : Using Iteration
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Explanation : We check if the number is negative. If it is, we return a message that factorial is not defined. Otherwise, we initialize result to 1 and iterate from 2 to n, multiplying result by each number in the range. Finally, we return result.
# Time Complexity : O(n) where n is the input number.
# Space Complexity : O(1) as we are using only a constant amount of space.


# Method 2 : Using Recursion (Not recommended due to potential stack overflow for large n)
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Explanation : We check if the number is negative, zero, or one. If it's negative, we return a message that factorial is not defined. If it's zero or one, we return 1. For other positive integers, we return n multiplied by the factorial of n - 1.
# Time Complexity : O(n) where n is the input number.
# Space Complexity : O(n) due to the recursive call stack.


# Method 3 : Using Math Library (Not recommended as it is not a manual implementation)
import math
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return math.factorial(n)
# Explanation : We check if the number is negative. If it is, we return a message that factorial is not defined. Otherwise, we use the built-in math.factorial function to calculate and return the factorial.
# Time Complexity : O(1) as the math.factorial function is optimized.
# Space Complexity : O(1) as we are using only a constant amount of space.