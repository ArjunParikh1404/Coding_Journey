# Given an array nums and integer k, return true if any duplicate values occur within k indices of each other; otherwise return false.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 219

nums = list(map(int, input("Enter the array:").split()))

k = int(input("Enter the value of k :"))

hmap = {}

for ind, val in enumerate(nums):
    if val in hmap and ind - hmap[val] <= k:
        print("True")
        break
    
    hmap[val] = ind
    
else:
    print("False")
