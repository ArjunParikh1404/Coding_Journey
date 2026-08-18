# Given an array of integers, use a hash set to determine whether the array contains any duplicate values.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 217

nums = list(map(int, input("Enter the array :").split()))

s = set()

duplicate = False

for i in nums:
    if i in s:
        duplicate = True
        print("Yes array contains duplicates.")
        break
    
    s.add(i)

else:
    print("Array doesn't contain duplicates.")
