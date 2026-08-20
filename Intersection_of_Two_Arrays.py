# Given two arrays, return the unique elements that appear in both arrays.
# Time Complexity = O(n + m), Space Complexity = O(n + m)
# Leetcode = 349

nums1 = list(map(int, input("Enter the 1st array :").split()))

nums2 = list(map(int, input("Enter the 2nd array :").split()))

nums1 = set(nums1)
nums2 = set(nums2)

result = nums1 & nums2

print(result)
