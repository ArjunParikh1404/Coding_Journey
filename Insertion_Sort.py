# Sort the array in Insertion Sort
# Time Complexity = O(n²), Space Complexity = O(1)
# Leetcode = 147 

nums = list(map(int, input("Enter the list :").split()))

for i in range(1,len(nums)):
    a = i
    while nums[a - 1] > nums[a] and a > 0:
        nums[a - 1], nums[a] = nums[a], nums[a - 1]
        
        a -= 1
        
print(nums)
