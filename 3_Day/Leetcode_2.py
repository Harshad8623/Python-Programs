# Link : https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Problem : Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.   
# Solution :

# Method 1 : Using String Slicing
class Solution(object):
    def reverse(self, x):
        if x>0:
            return int(str(x)[::-1])
        x = abs(x)
        return -1*int(str(x)[::-1])
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Probelm Faced : If reversed number goes outside this range: −2^31 to 2^31−1 then return 0. So we need to check for that as well.
# Solution :
class Solution(object):
    def reverse(self, x):
        if x >= 0:
            rev = int(str(x)[::-1])
            return rev if rev <= 2**31 - 1 else 0
        rev = -int(str(abs(x))[::-1])
        return rev if rev >= -2**31 else 0
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes



# Method 2 : Using Mathematical Operations  (Better Approach)
class Solution(object):
    def reverse(self, x):
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and pop > 7 ):
                return 0
            rev = rev * 10 + pop
        return sign * rev
# Time Complexity: O(log10(n))
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
