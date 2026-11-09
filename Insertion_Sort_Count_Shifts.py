# Sort the array in Insertion Sort and Count Shifts
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the list :").split()))

count = 0

for i in range(1,len(nums)):
    a = i
    while a > 0 and nums[a - 1] > nums[a]:
        nums[a - 1], nums[a] = nums[a], nums[a - 1]

        count += 1
        a -= 1

print("Sorted Array :", nums)
print("Total Shifts :", count)
