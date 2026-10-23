# Given two integer arrays, compute their intersection by returning all unique elements present in both arrays.
# Time Complexity = O(n+m), Space Complexity = O(n+k)

nums1 = list(map(int,input("Enter the 1st Array:").split()))

nums2 = list(map(int,input("Enter the 2nd Array:").split()))

hset = set(nums1)
op = []

for i in nums2:
    if i in hset:
        op.append(i)

print(op)
