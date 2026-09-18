# Sort an array in Bubble sort.
# Time Complexity = O(n²), Space Complexity = O(1)
# Leetcode = 912 

nums = list(map(int, input("Enter the array :").split()))

for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            
print(nums)
