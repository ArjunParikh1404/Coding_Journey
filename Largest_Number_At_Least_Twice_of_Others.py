# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 747

nums = list(map(int, input("Enter the array : ").split()))

high = max(nums)
index = 0

for i in range(len(nums)):
    if nums[i] == high:
        index = i
    elif nums[i] * 2 > high:
        print("-1")
        break
    
else:
    print(index)
