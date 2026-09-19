# Sort an array using Selection sort 
# Time Complexity = O(n²), Space Complexity = O(1)
# Leetcode = 912 

nums = list(map(int, input("Enter the array :").split()))

for i in range(len(nums)):
    
    small = float('inf')
    index = i
    
    for j in range(i, len(nums)):
        if nums[j] < small:
            small = nums[j]
            index = j 
    
    nums[i],nums[index] = nums[index],nums[i]
    
print(nums)
