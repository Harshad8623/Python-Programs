# Link : https://leetcode.com/problems/two-sum/description/
# 1. Two Sum
# Approach : Hash Map
# Problem : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution :
class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i, j in enumerate(nums):
            comp = target - j
            if comp in s:
                return [s[comp], i]
            s[j] = i
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No



# Based on this TWO SUM Other questions
# 1. Contains Duplicate
# Problem Given an integer array nums, return True if any value appears at least twice.
# e.g Input: [1,2,3,1]
# Output: True
# Solution :
lst = [1, 2, 3, 4]
def dup(lst):
    s = set()
    for i in lst:
        if i in s:
            return True
        s.add(i)
    return False
print(dup(lst))

# Another shorter pythonic way
def dup(lst):
    return len(lst) != len(set(lst))
print(dup([1,2,3,1]))



# 2. Valid Anagram
# Problem Given two strings s and t, return True if t is an anagram of s
# e.g Input: s = "anagram", t = "nagaram"
# Output: True
# Solution :
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

# Another shorter pythonic way
def isAnagram(s, t):
    return sorted(s) == sorted(t)


# 3. Group Anagrams
# Problem Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# e.g Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]