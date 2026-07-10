# Find the leftmost index in an array where the sum of elements on its left equals the sum of elements on its right; return -1 if no such index exists.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 724

nums = list(map(int, input("Enter the array : ").split()))

total = sum(nums)
ltotal = 0

for i in range(len(nums)):
    rtotal = total - ltotal - nums[i]
    
    if rtotal == ltotal:
        print(i)
        break
        
    ltotal += nums[i]
    
else:
    print("-1")
