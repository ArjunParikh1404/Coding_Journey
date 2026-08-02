# Given an integer array nums and a non-negative integer k, rotate the array to the right by k positions, modifying the array in-place if possible.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 189

nums = list(map(int, input("Enter the array : ").split()))

k = int(input("Enter the value of K : "))
end = len(nums) - k

for i in range(len(nums) - 1):
    nums[i],nums[end] = nums[end],nums[i]
    
    if end == len(nums) - 1:
        end = len(nums) - k
    else:
        end += 1
        
print(nums)
