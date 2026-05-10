# Link : https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Solution :

# Metghod 1 : Using Stack
class Solution(object):
    def isValid(self, s):
        stack = []
        
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    


class Solution:
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            # Opening bracket
            if char in "({[":
                stack.append(char)
            # Closing bracket
            else:
                # Stack empty OR not matching
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        # Valid only if stack becomes empty
        return len(stack) == 0
    

# Time Complexity : O(n) where n is the length of the string.
# Space Complexity : O(n) in the worst case when all characters are opening brackets.

# Another approach : Using String Replacement
class Solution(object):
    def isValid(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return not s
    
# Time Complexity : O(n^2) in the worst case when the string is made up of only one type of bracket.
# Space Complexity : O(n) because of string replacement creating new strings.

# Another approach : Using Stack and Hash Map
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack