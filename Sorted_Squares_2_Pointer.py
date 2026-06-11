# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order using 2 pointer technique.
# Time Complexity = O(n) , Space Complexity = O(n)

nums = list(map(int, input("Enter the Array : ").split()))

result = [0] * len(nums)

left = 0
right = len(nums) - 1
pos = len(nums) - 1

while left <= right:
    if abs(nums[right]) > abs(nums[left]):
        result[pos] = nums[right] ** 2
        right -= 1
        
    else:
        result[pos] = nums[left] ** 2
        left += 1
        
    pos -= 1
    
print(result)
