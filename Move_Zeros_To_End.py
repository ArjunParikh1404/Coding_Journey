# Moves all non-zero elements to the front of the array while shifting zeros to the end, preserving the relative order of non-zero elements.

nums = list(map(int,input("Enter the Array : ").split()))

j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print(nums)
