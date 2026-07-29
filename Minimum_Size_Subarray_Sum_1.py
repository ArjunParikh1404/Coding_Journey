# Given an array of positive integers and a target sum, find the length of the smallest contiguous subarray whose sum is greater than or equal to the target; return 0 if no such subarray exists.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 209

nums = list(map(int, input("Enter the array : ").split()))
target = int(input("Enter the target : "))

total = 0
slow = 0
op = float('inf')

for fast in range(len(nums)):
    total += nums[fast]
    
    while total >= target:
        op = min(op, fast - slow + 1)
        total -= nums[slow]
        slow += 1
    
print(0 if op == float('inf') else op)
