# Given an array of characters s, reverse the array in-place using O(1) extra memory.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 344

s = list(map(str, input("Enter the string separated by space : ").split()))

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
    
print(s)
