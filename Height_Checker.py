# Given an array heights, return the number of indices where the current order differs from the sorted (non-decreasing) order.
# Time Complexity = O(n log n), Space Complexity = O(n)
# Leetcode = 1051

nums = list(map(int, input("Enter the Array : ").split()))
exp = sorted(nums)

pos = 0
count = 0

while pos < len(nums):
    if nums[pos] != exp[pos]:
        count += 1
    pos += 1
    
print(count)
