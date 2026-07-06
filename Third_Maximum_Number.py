# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 414

nums = list(map(int, input("Enter the Array : ").split()))

p1 = None
p2 = None
p3 = None

for i in nums:
    if i == p1 or i == p2 or i == p3:
        continue
    
    if p1 is None or i > p1:
        p1, p2, p3 = i, p1, p2
    elif p2 is None or (p1 > i > p2):
        p2, p3 = i, p2
    elif p3 is None or (p2 > i > p3):
        p3 = i
        
print(p1 if p3 is None else p3)
