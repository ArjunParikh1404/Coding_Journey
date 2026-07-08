# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 448

nums = list(map(int, input("Enter the Array : ").split()))

for i in range(len(nums)):
    index = abs(nums[i]) - 1
    if nums[index] > 0:
        nums[index] *= -1

for i in range(len(nums)):
    if nums[i] > 0:
        print(i + 1, end=" ")
