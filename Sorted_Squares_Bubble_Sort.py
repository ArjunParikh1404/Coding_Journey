# Read integers, square them, and output the sorted squared values using Bubble sort technique.
# Time Complexity = O(n^2), Space Complexity = O(1)

nums = list(map(int,input("Enter the Array : ").split()))

for i in range(len(nums)):
    nums[i] = nums[i]*nums[i]

temp = 0

for x in range(len(nums)):    
    for j in range(1, len(nums)):
        if nums[j] <= nums[j-1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            
print(nums)
