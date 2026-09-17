# Given four integer arrays of length n, count the number of index tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0.
# Time Complexity = O(n²), Space Complexity = O(n²)
# Leetcode = 454

nums1 = list(map(int, input("Enter the 1st list: ").split()))

nums2 = list(map(int, input("Enter the 2nd list: ").split()))

nums3 = list(map(int, input("Enter the 3rd list: ").split()))

nums4 = list(map(int, input("Enter the 4th list: ").split()))

pair_sums = {}

for i in nums1:
    for j in nums2:
        s = i + j
        pair_sums[s] = pair_sums.get(s, 0) + 1

total = 0

for k in nums3:
    for l in nums4:
        total += pair_sums.get(-(k + l), 0)

print(total)
