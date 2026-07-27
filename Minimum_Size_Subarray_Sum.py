# Given an array of positive integers and a target sum, find the length of the smallest contiguous subarray whose sum is greater than or equal to the target; return 0 if no such subarray exists.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 209

nums = list(map(int, input("Enter the array : ").split()))
target = int(input("Enter the target : "))

fast = 0
slow = 0
total = nums[0]
size = 1
op = float('inf')

while fast < len(nums):
    
    if total < target:
        if fast == len(nums) - 1:
            break
        fast += 1
        total += nums[fast]
        size += 1
    else:
        op = min(op, size)
            
        total -= nums[slow]
        slow += 1
        size -= 1
        
print(op)
