# Sort the array in Insertion Sort and Count Comparisons
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the list :").split()))

count = 0

for i in range(1,len(nums)):
    a = i
    while a > 0:
        count += 1

        if nums[a - 1] > nums[a]:
            nums[a - 1], nums[a] = nums[a], nums[a - 1]
            a -= 1
        else:
            break

print(nums)
print("Total Comparisons :", count)
