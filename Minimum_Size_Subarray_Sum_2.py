# Given an array of positive integers and a target sum, find the length of the smallest contiguous subarray whose sum is greater than or equal to the target; return 0 if no such subarray exists.
# Time Complexity = (O(n log n)), Space Complexity = O(1)
# Leetcode = 209

from bisect import bisect_left

nums = list(map(int, input("Enter the array : ").split()))
target = int(input("Enter the target : "))

prefix = [0]

for i in range(len(nums)):
    prefix.append(prefix[-1] + nums[i])

op = float('inf')

for i in range(len(nums)):
    required = prefix[i] + target

    j = bisect_left(prefix, required)

    if j <= len(nums):
        op = min(op, j - i)

print(0 if op == float('inf') else op)
