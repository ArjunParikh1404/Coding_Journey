# Given a sorted array, remove duplicates in-place so each value appears once; return k = number of unique elements, and ensure first k positions contain those unique values in order.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode 26

nums = list(map(int, input("Enter the array : ").split()))

p1 = 0
p2 = 1 

while p2 < len(nums):
    if nums[p1] != nums[p2]:
        p1 += 1
        nums[p1] = nums[p2]

    p2 += 1
        
print(nums)
print("unique numbers =", p1+1)
