# Merge two sorted arrays nums1 and nums2 in-place into nums1 (LeetCode 88 - Merge Sorted Array) using a three-pointer approach from the end
# Input : nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]    
# Time Complexity = O(m+n), Space Complexity = O(1)

nums1 = list(map(int, input("Enter the nums1 array :").split()))
m = int(input("Enter the value of m :"))

nums2 = list(map(int, input("Enter the nums2 array :").split()))
n = len(nums2)

p1 = m - 1
p2 = n - 1
p3 = m + n -1

while p3 >= 0:
    if p1 < 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
    elif p2 < 0:
        nums1[p3] = nums1[p1]
        p1 -= 1
    else:    
        if nums1[p1] >= nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
    
    p3 -= 1

print(nums1)
