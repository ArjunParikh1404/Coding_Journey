# Read integers, square them, and output the sorted squared values

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
