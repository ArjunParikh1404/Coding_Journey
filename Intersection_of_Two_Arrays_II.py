# Find the intersection of two arrays, including duplicate elements based on their frequency in both arrays.
# Time Complexity = O(n + m), Space Complexity = O(min(n, m))
# Leetcode = 350

nums1 = list(map(int, input("Enter the 1st list:").split()))

nums2 = list(map(int, input("Enter the 2nd list:").split()))

hmap = {}
op = []

for i in nums1:
    if i in hmap:
        hmap[i] += 1
    else:
        hmap[i] = 1
        
for val in nums2:
    if val in hmap and hmap[val] > 0:
            op.append(val)
            hmap[val] -= 1
            
print(op)
