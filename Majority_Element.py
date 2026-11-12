# Given an array nums, return the element that appears more than n/2 times.
# Time complexity = O(n), Space complexity = O(n)
# Leetcode = 169

nums = list(map(int, input("Enter the list :").split()))

seen = {}

for val in nums:
    if val in seen:
        seen[val] += 1
    else:
        seen[val] = 1

for key, val in seen.items():
    if val > len(nums) // 2:
        print(key)
        break
