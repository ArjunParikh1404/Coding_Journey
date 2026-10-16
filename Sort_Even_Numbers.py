# Given a list of integers, sort only the even numbers in ascending order, while keeping odd numbers in their original positions.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the list: ").split()))
n = len(nums)

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] % 2 == 0 and nums[j + 1] % 2 == 0:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
