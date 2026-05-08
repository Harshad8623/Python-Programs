# Link: https://leetcode.com/problems/palindrome-number/
# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Solution :

# Method 1 : Using String Slicing
class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False
# Time Complexity : O(n)
# Space Complexity : O(n)

# Method 2 : Using Mathematical Operations
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp != 0:
            pop = temp % 10
            temp //= 10
            rev = rev * 10 + pop
        return rev == x
# Time Complexity : O(log10(n))
# Space Complexity : O(1)


# version 2 : Better Approach
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        return x == rev or x == rev // 10
# Time Complexity : O(log10(n))
# Space Complexity : O(1)
# Why this works : We only reverse half of the number and compare it with the other half. If the number is odd, we can ignore the middle digit by rev // 10. This way we avoid overflow issues and also reduce the number of iterations.