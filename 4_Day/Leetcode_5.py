# Link : https://leetcode.com/problems/contains-duplicate
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Method 1 : Using Set (Prefer this method as it is more efficient)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# Method 2 : Using Sorting 
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
# Method 3 : Using Hash Map
class Solution(object):
    def containsDuplicate(self, nums):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = True
        return False
    
# Method 4 : Using Counter from Collections
from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        count = Counter(nums)
        for key in count:
            if count[key] > 1:
                return True
        return False
    
# Method 5 : Using List (Not recommended as it is less efficient)
class Solution(object):
    def containsDuplicate(self, nums):
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False
    
# Method 6 : Using Set with Early Exit
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Method 7 : Using List Comprehension (Not recommended as it is less efficient)
class Solution(object):
    def containsDuplicate(self, nums):
        return any(nums.count(num) > 1 for num in nums)
    

# Method 8 : Using Set with Length Comparison
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
    

# Method 9 : Using Dictionary (Not recommended as it is less efficient)
class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        for num in nums:
            if num in count:
                return True
            count[num] = 1
        return False
    
# Method 10 : Using Set with Generator Expression
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        return any(num in seen or seen.add(num) for num in nums)