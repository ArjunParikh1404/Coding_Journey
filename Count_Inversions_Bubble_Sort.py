# Count the number of inversions in an array using Bubble Sort.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the array :").split()))

count = 0

for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            count += 1

print("Sorted Array :", nums)
print("Number of Inversions :", count)
