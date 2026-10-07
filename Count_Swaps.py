# Sort an array in Bubble Sort and count the number of swaps.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the array : ").split()))

swaps = 0

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swaps += 1

print(nums)
print("Number of swaps :", swaps)
