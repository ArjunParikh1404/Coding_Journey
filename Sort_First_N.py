# Given a list of integers and an integer k, sort the first k elements in ascending order while keeping the remaining elements in their original positions.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the list:").split()))
n = int(input("Enter the number :"))

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if nums[j] > nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            i = j
        else:
            break

print(nums)
