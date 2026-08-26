# Given an array nums and a target, return the indices of two numbers that add up to target.
# Time complexity = O(n), Space complexity = O(n)
# Leetcode = 1

nums = list(map(int, input("Enter the list :").split()))
target = int(input("Enter the target :"))

seen = {}

for key, val in enumerate(nums):
    complement = target - val
    
    if complement in seen:
        print(seen[complement], key)
        break
    
    seen[val] = key
