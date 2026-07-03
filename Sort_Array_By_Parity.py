# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 905

nums = list(map(int, input("Enter the Array : ").split()))

p1 = 0
p2 = 0

while p2 < len(nums):
    if nums[p2] % 2 == 0:
        nums[p1], nums[p2] = nums[p2], nums[p1]
        p1 += 1
    p2 += 1
    
print(nums)
