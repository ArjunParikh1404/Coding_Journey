# Sort only even numbers using Selection Sort
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the array :").split()))

for i in range(len(nums)):

    if nums[i] % 2 == 0:

        small = float('inf')
        index = i

        for j in range(i, len(nums)):

            if nums[j] % 2 == 0 and nums[j] < small:
                small = nums[j]
                index = j

        nums[i], nums[index] = nums[index], nums[i]

print(nums)
