# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 905

nums = list(map(int, input("Enter the Array : ").split()))

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] % 2 == 0:
        left += 1
    elif nums[right] % 2 == 1:
        right -= 1
    else:
        nums[left], nums[right] = nums[right], nums[left]
        
print(nums)
