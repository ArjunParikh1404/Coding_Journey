# Write a Python program to arrange a list of words in alphabetical order.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(str, input("Enter the list:").split()))

for i in range(len(nums)):
    for j in range(1, len(nums)):
        
        if nums[j-1] > nums[j]:
            nums[j-1],nums[j] = nums[j], nums[j-1]
        
print(nums)
