# Merge two sorted arrays nums1 and nums2 in-place into nums1 using a three-pointer approach from the end
# Input : nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  Output: [1,2,2,3,5,6]
# this code is for if nums1 != m + n
# Time Complexity = O(m + n) Space Complexity = O(1)

nums1 = list(map(int, input("Enter the nums1 array :").split()))

m = int(input("Enter the value of m :"))

nums2 = list(map(int, input("Enter the nums2 array :").split()))

n = int(input("Enter the value of n :"))

right = m + n - 1
left = 0
count = 0

while len(nums2) > n:
    nums2.pop()
    
while m > 0:
    nums2.append(nums1[m-1])
    m -= 1
    
while left <= right:
    if nums2[left] <= nums2[right]:
        nums1[count] = nums2[left]
        count += 1
        left += 1
    else:
        nums1[count] = nums2[right]
        count += 1
        right -= 1
        
print(nums1)
